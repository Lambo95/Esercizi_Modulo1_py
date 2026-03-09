""" print("Lamberto")

nome= input("Inserisci il tuo nome: ")
eta= int(input("Inserisci la tua eta: "))

print(f"Mi chiamo {nome} e ho {eta} anni, il doppio dei miei anni è {eta*2}")
 """
#TIPI DI DATI

""" # Esercizio 1 

x = 7
y = 3
somma = x + y
print(somma)


# Esercizio 2

prezzo = 19.99
quantità = 3
print(prezzo * quantità)


# Esercizio 3

x = 10
print ( x > 5 ) 

# Esercizio 4

a = 5
b = 2.5
print(a+b) """

#CASTING

"""
num_int = int(input("Inserisci un numero intero: "))
num_float = float(num_int)
print(num_float)
num_str = str(num_int)
print(f"il tuo numero intero in stringa e' {num_str}") """

#Esercizi Modulo 1: tipi di dati, casting e variabili

# Esercizio 1 

""" Creare tre variabili: nome (stringa), età (intero) e città (stringa).
Stampare le variabili. """
"""
nome = "Lamberto"
età = 30
città = "Torino"

print("Mi chiamo ", nome, ", ho ", età, " anni e vivo in ", città)
"""

# Esercizio 2

"""Creare una variabile x, assegnarle un valore e aggiornarla.
Stampare il valore prima e dopo l'aggiornamento. """
"""
x = 2.5
print("Prima:", x)
x = 6
print("Dopo:", x) 

"""
# Esercizio 3
# Somma di due variabili intere e stampa del risultato.
"""
x = 12
y = 18
print("Somma di", x, "e", y, "=", x + y)  


# Esercizio 4
# Scambio dei valori tra due variabili x e y.

x = 15
y = 11

print("Valori scambiati - prima: ", x, y); 
x, y = y, x; 
print("Valori scambiati - dopo: ", x, y)  


# Esercizio 5 
# Calcolo dell'area di un rettangolo utilizzando base e altezza.

base = 5
altezza = 10
area = base * altezza
print("Area rettangolo con base", base, "e altezza", altezza, "e'", area)  


# Esercizio 6 
# Somma di un numero intero con un decimale e stampa del risultato.

a = 12
b = 23.12
print("Somma di", a, "e", b, "e'", a + b)  


# Esercizio 7
# Calcolare la media di tre numeri.

x, y, z = 15, 18, 22
media = (x + y + z) / 3
print("Media di", x, y, z, "e'", media)  


# Esercizio 8 
# Concatenazione di due stringhe.

s1 = "Mi chiamo "
s2 = "Lamberto "
s3 = "e ho 30 anni"
print("Concatenazione di", s1, "-", s2,"-", s3, "e'", s1 + s2 + s3)  


# Esercizio 9 
# Ripetizione della parola "ciao" tre volte utilizzando una stringa.

print("Ciao " * 3)  


# Esercizio 10 
# Uso di variabili boolean per verificare se un numero è maggiore di un altro.

a = 12
b = 18
c = 30 
print(a < b)
print(b > c) 
print(a < c)  


# Esercizio 11 
# Trasformare un intero in un float e stamparlo.

x = 22
y = float(x)
print("Il numero float di", x, "e'", y)  


# Esercizio 12
# Convertire un numero in una stringa e stamparlo.

n = 1893
s = str(n)

print("Il numero in formato stringa è: " + s)  


# Esercizio 13
# Uso di variabili booleane per valutare valori positivi, negativi, nulli e una stringa vuota.

print (bool(1))
print (bool(0))
print (bool(-1))
print (bool(""))
 """

#Stringhe e operazioni
#Prendi una frase ed invertila e stampala
""" stringa=str((input("Inserisci una stringa: ")))
print("Stringa invertita:", stringa[::-1]) """

#Controlla se una frase è un palindromo
""" frase=str((input("Inserisci una stringa: ")))

if frase == frase[::-1]: #solo uguale errore ...
    print(f"La frase inserita {frase} e' palindroma")
else:
    print(f"La frase inserita {frase} non e' palindroma") """
    
#1. Estrarre Primo e Ultimo Carattere:
#Dichiarazione di una variabile testo e utilizzo della funzione print per stampare il primo e l'ultimo carattere della stringa tramite gli indici 0 e -1.
""" testo="Prova"
print(f"La prima lettera della parola {testo} è {testo[0]} l'ultima è {testo[-1]}") """

#2. Convertire in Maiuscolo e Minuscolo:
#Conversione di una stringa con caratteri misti in tutte lettere maiuscole usando upper() e tutte minuscole con lower().
""" stringa="TeStO"
print(f"La parola {stringa} tutta maiuscolo è {stringa.upper()} mentre tutta minuscolo è {stringa.lower()}") """

#3. Contare Occorrenze di una Lettera:
#Utilizzo del metodo count() per contare quante volte una lettera specifica appare in un testo.
""" testo= str(input("Inserisci una parola o frase: "))
lettera= str(input("Scegli una lettera: "))

print(f"In {testo} la lettera {lettera} compare: {testo.count(lettera)}") """

#4. Verificare Inizio e Fine di una Parola:
#Controllo se una stringa inizia o finisce con una determinata lettera utilizzando startswith() ed endswith().
""" parola= str(input("Inserisci una parola: "))
lettera= str(input("Scegli una lettera: "))
print(f"La {parola} inizia con la lettera {parola[0]} la lettera scelta corrisponde? {parola.startswith(lettera)} e finisce con la lettera {parola[-1]} la lettera scelta corrisponde? {parola.endswith(lettera)}")
 """

#5. Invertire una Stringa:
#Utilizzo dello slicing con passo negativo per invertire l'ordine dei caratteri in una stringa.
""" stringa=str((input("Inserisci una stringa: ")))
print("Stringa invertita:", stringa[::-1]) """

#6. Rimuovere Spazi Iniziali e Finali:
#Applicazione della funzione strip() per eliminare gli spazi all'inizio e alla fine di una stringa.
""" frase= "  Stavo studiando PYTHON la sera   "
print(frase.strip()) """

#7. Ripetere le Prime Tre Lettere:
#Estrazione delle prime tre lettere di una parola e ripetizione per tre volte con l'operatore di moltiplicazione delle stringhe.
""" parola= str(input("Inserisci una parola: "))
print(f"la parola {parola} inizia con {parola[:3]}")
numero= int(input("Scegli quante volte ripetere "))
print(f"l'inizio della parola {parola[:3]} ripetuta {numero} volte è \n {parola[:3]*numero}") """





 
