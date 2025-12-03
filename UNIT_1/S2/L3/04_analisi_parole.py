#Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola. Ignora la punteggiatura e considera le parole in modo case-insensitive.
import re #importo il modulo per le espressioni regolari

testo = "Ciao, ciao! Come stai? Stai bene?"

# Esempio di output atteso: {'ciao': 2, 'come': 1, 'stai': 2, 'bene': 1}

def analisi(text):
    # formatto tutto in minuscolo per rendere il conteggio case-insensitive
    text = text.lower()

    # rimuovo la punteggiatura: sostituisco tutto ciò che NON è lettera, cifra o spazio con stringa vuota
    # [^\w\s] = caratteri non-word e non-whitespace
    text = re.sub(r"[^\w\s]", "", text)

    # divido il testo in parole usando gli spazi
    parole = text.split()

    # dizionario per contare le occorrenze
    occorrenze = {}
    for parola in parole:
        # se la parola è già presente incremento il conteggio, altrimenti la inizializzo a 1
        if parola in occorrenze:
            occorrenze[parola] += 1
        else:
            occorrenze[parola] = 1

    return occorrenze
        

# stampa il risultato dell'analisi sul testo di esempio
print(analisi(testo))