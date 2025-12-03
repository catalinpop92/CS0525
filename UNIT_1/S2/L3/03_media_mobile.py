#Descrizione: Scrivi una funzione che calcoli la media mobile di una lista di numeri. La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # lista di esempio
n = 3  # dimensione della finestra per la media mobile

def media_mobile(numeri, n):
 
    risultato = []      # lista che conterrà le medie calcolate
    somma = 0           # somma corrente degli elementi nella finestra mobile

    for i in range(len(numeri)):
        # Aggiungo il valore corrente alla somma della finestra
        somma += numeri[i]

        # Se l'indice supera la dimensione n, rimuovo l'elemento più vecchio
        # che esce dalla finestra (elemento in posizione i-n)
        if i >= n:
            somma -= numeri[i - n]

        # Larghezza reale della finestra:
        # per i < n-1 la finestra contiene solo i+1 elementi,
        # dopo di che la finestra ha esattamente n elementi.
        larghezza = min(i + 1, n)

        # Calcolo la media corrente e la aggiungo al risultato
        risultato.append(somma / larghezza)

    return risultato


# Eseguo la funzione sull'esempio e stampo il risultato
print(media_mobile(numeri, n))





