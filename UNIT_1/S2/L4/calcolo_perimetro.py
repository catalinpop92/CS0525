import math

def leggi_positivo(prompt):
    """
    Legge un numero positivo dall'utente.
    Continua a chiedere finché l'utente non inserisce un valore numerico > 0.
    Funzione riutilizzabile da tutte le figure geometriche.
    """
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Inserisci un valore maggiore di zero.")
                continue
            return val
        except ValueError:
            print("Valore non valido. Inserisci un numero.")


def perimetro_quadrato():
    """Calcola il perimetro del quadrato leggendo il lato."""
    lato = leggi_positivo("Inserisci il lato del quadrato: ")
    return 4 * lato

def perimetro_cerchio():
    """
    Calcola la circonferenza del cerchio.
    Usa math.pi per ottenere un valore accurato di π.
    """
    r = leggi_positivo("Inserisci il raggio del cerchio: ")
    return 2 * math.pi * r

def perimetro_rettangolo():
    """Calcola il perimetro del rettangolo leggendo base e altezza."""
    base = leggi_positivo("Inserisci la base del rettangolo: ")
    altezza = leggi_positivo("Inserisci l'altezza del rettangolo: ")
    return 2 * base + 2 * altezza


def main():
    print("Calcolo del perimetro di figure geometriche")
    print("1) Quadrato")
    print("2) Cerchio")
    print("3) Rettangolo")

    funzioni = {
        "1": perimetro_quadrato,
        "2": perimetro_cerchio,
        "3": perimetro_rettangolo
    }

    # Ciclo che si ripete finché l'utente non inserisce una scelta valida
    while True:
        scelta = input("Scegli una figura (1-3): ")

        # Controllo: se la scelta corrisponde a una chiave del dizionario,
        # allora è un input valido e possiamo eseguire la funzione associata.
        if scelta in funzioni:
            risultato = funzioni[scelta]()   # Esegue il calcolo del perimetro
            print(f"Il perimetro è: {risultato}")
            break    # Scelta corretta → usciamo dal ciclo

        # Se non è valida, informiamo l'utente e ripetiamo il ciclo.
        else:
            print("Scelta non valida. Inserisci un valore tra 1 e 3.\n")



# Avvia il programma solo se eseguito direttamente.
if __name__ == "__main__":
    main()
