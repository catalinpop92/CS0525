print("Programma che genera un nome per la tua band")

#dentro la variabile si salva l'input digitato dall'utente
string_city = input("Inserisci il nome della tua città: ")
#finchè la stringa inserita non è composta da solo caratteri si richiede l'input
while not string_city.isalpha():
    string_city = input("Inserisci solo lettere: ") 

#dentro la variabile si salva l'input digitato dall'utente
string_animal_name = input("Inserisci il nome del tuo animale domestico: ")
#finchè la stringa inserita non è composta da solo caratteri si richiede l'input
while not string_animal_name.isalpha():
    string_animal_name = input("Inserisci solo lettere: ") 

#si stampa una stringa formattata concatenando una stringa statica con due stringhe dinamiche 
print(f"Il nome della tua band è: {string_city} {string_animal_name}")