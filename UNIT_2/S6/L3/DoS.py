# Importazione dei moduli necessari
import socket  # Per la comunicazione di rete
import time    # Per la misurazione del tempo

def main():
    # Richiesta dell'indirizzo IP del target
    target_ip = input("Inserisci IP target: ")
    # Richiesta della porta UDP del target
    target_port = int(input("Inserisci porta UDP target: "))
    # Richiesta del numero di pacchetti da inviare (1 KB ciascuno)
    num_packets = int(input("Numero di pacchetti da inviare (1 KB ciascuno): "))

    # Definisce la dimensione di ogni pacchetto (1 KB)
    packet_size = 1024
    
    # Blocco try-except per gestire gli errori di rete
    try:
        # Crea un socket UDP (SOCK_DGRAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Messaggio di inizio dell'invio
        print(f"\n[INFO] Invio a {target_ip}:{target_port}...")
        
        # Registra il tempo di inizio
        start_time = time.time()
        # Ciclo per inviare i pacchetti
        for i in range(1, num_packets + 1):
            # Crea un pacchetto riempito di caratteri 'X'
            packet = b'X' * packet_size
            # Invia il pacchetto al target via UDP
            sock.sendto(packet, (target_ip, target_port))
        
        # Calcola il tempo trascorso
        elapsed = time.time() - start_time
        # Calcola il throughput (velocità di trasmissione)
        rate = (num_packets * packet_size) / elapsed if elapsed > 0 else num_packets * packet_size
        
        # Stampa i risultati della simulazione
        print(f"\nPacchetti inviati: {num_packets}")
        print(f"Tempo: {elapsed:.2f}s")
        print(f"Throughput: {rate/1024:.2f} KB/s")
        
        # Chiude il socket
        sock.close()
    # Gestisce qualsiasi errore di rete o esecuzione
    except Exception as e:
        print(f"[ERRORE] {e}")

# Punto di ingresso principale del programma
if __name__ == "__main__":
    main()
