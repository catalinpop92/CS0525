#include <stdio.h> // libreria standard per input/output (printf, scanf)

int main() {
    // dichiarazione di tre variabili intere:
    // a, b = operandi; risultato = prodotto
    int a, b, risultato;

    // il printf stampa testo nel terminale 
    printf("Inserisci il primo numero intero: ");
    // lo scanf legge un intero da stdin e lo salva dentro la variabile selezionata tramite puntatore &
    scanf("%d", &a);

    printf("Inserisci il secondo numero intero: ");
    scanf("%d", &b);
    //vengono moltiplicati i valori che sono dentro le variabili e il risultato viene assegnato alla variabile "risultato" tramite l'uguale
    risultato = a * b;

    // stampa il risultato formattato
    printf("Il risultato della moltiplicazione di %d per %d è: %d\n", a, b, risultato);

    // termine del programma (0 indica successo)
    return 0;
}