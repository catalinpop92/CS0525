import socket
import time
import ipaddress  # Validazione IP


def get_valid_ip():
    # Richiede un IPv4 valido
    while True:
        ip = input("Inserisci IP target: ")
        try:
            ipaddress.IPv4Address(ip)
            return ip
        except ipaddress.AddressValueError:
            print("[ERRORE] IP non valido.")


def get_valid_port():
    # Richiede una porta UDP valida
    while True:
        port = input("Inserisci porta UDP target (1-65535): ")
        if port.isdigit() and 1 <= int(port) <= 65535:
            return int(port)
        print("[ERRORE] Porta non valida.")


def get_valid_packet_count(max_packets=9999999):
    # Limita il numero di pacchetti per evitare abusi
    while True:
        count = input(f"Numero pacchetti (max {max_packets}): ")
        if count.isdigit() and 0 < int(count) <= max_packets:
            return int(count)
        print("[ERRORE] Numero pacchetti non valido.")


def main():
    # Input validati
    target_ip = get_valid_ip()
    target_port = get_valid_port()
    num_packets = get_valid_packet_count()

    packet_size = 1024  # 1 KB
    sent_packets = 0

    try:
        # Creazione socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        start_time = time.time()
        print(f"\n[INFO] Invio a {target_ip}:{target_port}...")

        # Invio pacchetti
        for _ in range(num_packets):
            sock.sendto(b'X' * packet_size, (target_ip, target_port))
            sent_packets += 1

    except KeyboardInterrupt:
        # Interruzione manuale
        print("\n[INTERRUZIONE] Operazione fermata dall'utente.")

    except Exception as e:
        # Errori generici
        print(f"[ERRORE] {e}")

    finally:
        # Calcolo statistiche finali
        elapsed = time.time() - start_time if 'start_time' in locals() else 0
        total_bytes = sent_packets * packet_size
        rate = total_bytes / elapsed if elapsed > 0 else 0

        print("\n--- RISULTATI ---")
        print(f"Pacchetti inviati: {sent_packets}")
        print(f"Tempo: {elapsed:.2f}s")
        print(f"Throughput: {rate / 1024:.2f} KB/s")

        # Chiusura socket
        try:
            sock.close()
        except:
            pass


if __name__ == "__main__":
    # Entry point del programma
    main()
