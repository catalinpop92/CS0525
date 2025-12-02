#include <stdio.h> // libreria standard per input/output (printf, scanf)

int main() {
    // numero di elementi e variabili per somma/media
    int n;
    double valore, somma = 0.0, risultato;

    // chiede all'utente quanti numeri inserire
    printf("Quanti numeri vuoi inserire? ");
    //eseguo un controllo sull'input per assicurarmi che sia un intero positivo, nel caso contrario interrompo il programma 
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Numero non valido. Interrompo il programma.\n");
        return 1;
    }

    // legge n numeri uno per uno e accumula la somma
    for (int i = 0; i < n; i++) {
        printf("Inserisci il numero %d: ", i + 1);  // chiede il numero e tengo conto dell'indice
        // controllo sull'input per assicurarmi che sia un numero valido
        if (scanf("%lf", &valore) != 1) {
            printf("Input non valido. Interrompo il programma.\n");
            return 1;
        }
        somma += valore; // accumula la somma dei numeri inseriti
    }

    // calcola la media aritmetica e il risultato viene assegnato alla variabile "risultato"
    risultato = somma / n;

    // stampa il risultato formattato
    printf("La media aritmetica di %d numeri è: %lf\n", n, risultato);

    return 0;
}