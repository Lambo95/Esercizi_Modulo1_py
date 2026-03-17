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

#Boolean
""" anni=int(input("Quanti anni hai? "))
patente=str(input("Hai la patente? (si/no) "))
res=anni >= 18 and patente == "si"
print(f"Puoi guidare: {bool(res)}") 


utente=str(input("Scegli un utente: Premium o Ritardo "))

if utente == "Premium":
        print("Puoi entrare in biblioteca")
elif utente == "Ritardo":
    print("Non puoi entrare in biblioteca")
else:
    print("Hai inserito un valore non valido")    """

#Operazioni aritmetiche

""" soldi= float(input("Quanti soldi hai? "))
prezzo= float(input("Quanto costa l'oggetto? "))
print(f"Hai {soldi} euro, il prezzo dell'oggetto e' {prezzo} euro, puoi comprare: {soldi//prezzo} oggetti e ti restano {soldi%prezzo} euro")
 """

#if, elif, else

""" età= int(input("Quanti anni hai? "))
if età < 18:
    print("Sei minorenne")
elif età < 65:
    print("Sei adulto")
else:
    print("Sei anziano") """

# Esercizio 1: Controllo Multiplo di 3
# Verifica se un numero è multiplo di 3 utilizzando l'operatore modulo.

""" numero=int(input("inserisci un numero: "))
if numero % 3 == 0:
    print(f"{numero} e' multiplo di 3")
else:
    print(f"{numero} non e' multiplo di 3") """
    
# Esercizio 2: Verifica Voto Sufficiente
# Controllo se il voto inserito è sufficiente (>= 18).

""" voto=int(input("Inserisci il tuo voto: "))
if voto >= 18:
    print(f"Voto sufficiente: {voto}")
else:
    print(f"Voto insufficiente: {voto}") """

# Esercizio 3: Vocale o Consonante
# Distingui se un carattere è una vocale o consonante tramite le strutture condizionali.
""" lettera=str(input("Inserisci una lettera: "))
if lettera in "aeiou":
    print(f"{lettera} e' una vocale")
else:
    print(f"{lettera} e' una consonante") """

# Esercizio 4: Numero Positivo, Negativo o Zero
# Determina se un numero è positivo, negativo o zero.

""" numero=int(input("Inserisci un numero: "))
if numero > 0:
    print(f"{numero} e' positivo")
elif numero < 0:
    print(f"{numero} e' negativo")
else:
    print(f"{numero} e' zero") """
    
# Esercizio 5: Maggiore tra Tre Numeri
# Trova il numero maggiore tra tre variabili.

""" a=int(input("Inserisci un numero: "))
b=int(input("Inserisci un numero: "))
c=int(input("Inserisci un numero: "))

if a > b and a > c:
    print(f"{a} e' il numero maggiore")
elif b > a and b > c:
    print(f"{b} e' il numero maggiore")
else:
    print(f"{c} e' il numero maggiore") """

# Esercizio 6: Calcolo Prezzo Biglietto
# Calcola il prezzo del biglietto in base all'età:
""" Sotto i 12 anni: 5 euro
    Tra i 13 e i 64 anni: 10 euro
    Oltre i 65 anni: 7 euro """
    
""" eta=int(input("Quanti anni hai? "))

if eta < 12:
    print("Il prezzo del biglietto e' 5 euro")
elif eta < 65:
    print("Il prezzo del biglietto e' 10 euro")
else:
    print("Il prezzo del biglietto e' 7 euro") """


# Esercizio 7: Classificazione Triangoli
# Identifica se un triangolo è equilatero, isoscele, o scaleno basandoti sulle lunghezze dei suoi lati.
""" a=input("Inserisci la lunghezza del primo lato del triangolo: ")
b=input("Inserisci la lunghezza del secondo lato del triangolo: ")
c=input("Inserisci la lunghezza del terzo lato del triangolo: ")

if a == b == c:
    print("Il triangolo e' equilatero")
elif a == b or b == c or a == c:
    print("Il triangolo e' isoscele")
else:
    print("Il triangolo e' scaleno") """

#ciclo while

""" numero=int(input("Inserisci un numero o 0 per uscire: "))
while numero != 0:
       
    if numero % 2 == 0:
        print(f"{numero} e' pari")
    else:
        print(f"{numero} e' dispari")

    numero=int(input("Inserisci un numero \n o inserisci 0 per uscire: "))
print("Esci") """

""" Esercizio 1: Contare da 1 a 5
Dichiarare i = 1
Inserire ciclo while i <= 5
Stampare i e incrementare i """

""" i=1
while i<=5:
    print(i)
    i+=1 """

""" Esercizio 2: Contare numeri pari da 2 a 10
Dichiarare i = 2
Inserire ciclo while i <= 10
Stampare i e incrementare di 2 """
""" i=2
while i<=10:
    print(i)
    i+=2 """

""" Esercizio 3: Sommare numeri da 1 a 10
Dichiarare i = 1 e somma = 0
Inserire ciclo while i <= 10
Incrementare somma e stampare il risultato """
""" i=1
somma=0
while i<=10:
    somma+=i
    print("Somma =", somma, i)
    i+=1

     """

""" Esercizio 4: Stampare tabellina di un numero
Dichiarare n = 7 e i = 1
Stampare tabellina fino a i = 10 """

""" n=7
i=1
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1 """
    
""" Esercizio 5: Somma dei numeri inseriti dall'utente
Richiede all'utente di inserire numeri finché non digita 0
Calcolare e stampare la somma totale """
""" numero=int(input("Inserisci un numero o premi 0 per uscire :"))
somma =0
while numero != 0:
    somma += numero
    print(f"La somma del numeri inseriti è {somma}")
    numero=int(input("Inserisci un numero o premi 0 per uscire :"))
print(f"Somma finale: {somma} -- Sei uscito") """
    

""" Esercizio 6: Indovinare il numero
Variabile segreto = 7
L'utente deve indovinare il numero con tentativi successivi """
""" numero=int(input("Indovina il numero:"))
segreto=7
while numero!=segreto:
    print(f"Il numero {numero} non è quello corretto! Ritenta")
    numero=int(input("Indovina il numero:"))
print("Hai vinto! -- Esci") """

""" Esercizio 7: Stampare numeri dispari fino a 15
Dichiarare i = 1
Incrementare di 2 ogni iterazione per stampare i numeri dispari """
""" i=1
while i<=15:
    print(i)
    i+=2  """

""" Esercizio per gli studenti
Calcolare la somma delle cifre di un numero """
""" numero_str=str(input("Inserisci un numero:"))
str_len= len(numero_str)
print(str_len)
i=0
somma=0
while i<str_len:
    somma+=int(numero_str[i])
    print(somma)
    i+=1 """

#ciclo FOR
""" nomi=["Giuseppe", "Giorgio", "Giovanni", "Gianluca"]
for i, val in enumerate(nomi):
    print(i, val) """
    
""" Stampa dei Numeri da 1 a 10
Usa for i in range(1, 11) per stampare i numeri da 1 a 10. """
""" for i in range(1, 11):
    print(i) """

""" Stampa dei Numeri Pari da 1 a 20
Utilizza for i in range(2, 21, 2) per stampare i numeri pari. Questo sfrutta l'incremento di 2. """
""" for i in range(2, 21, 2):
    print(i) """

""" Stampa di Ogni Lettera di una Parola
Assegna una parola a una variabile e usa for c in parola per stampare ogni carattere singolarmente. """
""" parola=str(input("Inserisci una parola:"))
for c in parola:
    print(c) """

""" Somma dei Numeri da 1 a 100
Dichiarare una variabile somma e usare un ciclo for per calcolare e stampare la somma totale. """
""" somma=0
for i in range(1,100): #perché 101?
    somma+=i
print(somma) """

""" Stampa della Tabellina del 3
Stampare la tabellina del 3 utilizzando un ciclo for. """
""" for i in range(3,31,3):
    print(i) """

""" Calcolo del Fattoriale di un Numero
Dichiarare variabili per il numero e il fattoriale e calcolare il fattoriale usando for.
 """
""" n = 5
fattoriale = 1
for i in range(1, n+1):
    fattoriale *= i
    print(fattoriale)
print("Fattoriale =", fattoriale) """
 
""" Conteggio delle Vocali in una Parola
Dichiarare una parola e contare le vocali presenti utilizzando for con una condizione if. """
""" parola=str(input("Inserisci una parola:"))
count=0
vocali= ["a", "e", "i", "o", "u"]
for v in parola:
    if v in vocali:
        count +=1
print(f"La parola {parola} ha {count} vocali") """

""" Stampa di una Matrice 3x3
Utilizzare cicli for annidati per stampare una matrice 3x3. """ #da vedere
""" for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end="  ")
    print() """

""" Uso di Operatore Continue
Stampare i numeri da 1 a 10 saltando il 5 con if e continue. """
""" for i in range(1, 11):
    if i == 5:
        continue
    print(i) """

""" Uso di Operatore Break
Stampare i numeri da 1 a 10 e fermarsi al 7 includendo il 7 con if e break. """
""" for i in range(1, 11):
    if i == 7:
        break
    print(i) """
    
#Liste
# Creare una lista con cinque numeri, aggiungere un numero alla fine, sostituire il terzo numero e stampare la lista finale.

""" lista =[1,2,3,4,5]
lista.append(6)
lista.remove(3)
lista.insert(2, 100)

print(lista) """

#tuple
#Creare una tupla con 3 colori, stampa il primo e l'ultimo, conta quante volte compare in colore

""" colori=("giallo", "giallo","rosso")
print(colori[0], colori[-1])
duplicati = 0

for i in range(len(colori)):
    print(i)
    for j in range(i + 1, len(colori)):
        print(j)
        if colori[i] == colori[j]:
            duplicati += 1

print(duplicati) """


#set
""" Immaginiamo due corsi universitari: Corso A e Corso B.
Vogliamo sapere:
· Chi frequenta entrambi i corsi. #&
· Chi frequenta solo il corso A.
. Chi frequenta solo il corso B.
· Chi frequenta almeno un corso. ?
· Quanti studenti unici ci sono in totale. |"""

""" corso_a = {"Paolo","Gianluca","Marco","Anna"}
corso_b = {"Mario", "Paolo", "Anna", "Teresa"}

print(f"{corso_a & corso_b} frequentano entrambi i corsi")
print(f"{corso_a-corso_b} frequntano solo il corso A")
print(f"{corso_b-corso_a} frequentano solo il corso B")

print(f"Glis tudenti dei corsi sono: {corso_a|corso_b}") """

#Dizionari
""" Crea un dizionario che rappresenti uno studente con le
seguenti chiavi: "nome", "età" e "corso". Poi:
· Modifica il valore di "età".
· Aggiungi una nuova chiave "matricola".
· Usa get() per recuperare un valore sconosciuto senza
errore.
· Itera su tutte le coppie chiave-valore e stampale.
 """
""" 
studente={"nome": "Giovanni","Età":32,"Corso":"Python"}
studente["Età"]="26"
studente["matricola"]=1

studente.get("classe")

for chiave, val in studente.items():
    print(chiave, val)
 """
#Dizionari, set e tuple

"""  Esercizio 1: Somma dei numeri pari in una lista
Creare una lista di numeri.
Calcolare la somma dei numeri pari utilizzando un ciclo for e l'operatore modulo.
Stampa del risultato. """
""" numeri=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for n in numeri:
    if n%2 == 0:
        n+=n
        print(n)
print(n)
         """

""" Esercizio 2: Creare una lista senza duplicati
Creazione di una lista con duplicati.
Utilizzando un ciclo for per creare una nuova lista senza duplicati mantenendo l'ordine.
Stampa del risultato. """
""" lista_duplicati = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_senza_duplicati = []
for n in lista_duplicati:
    if n not in lista_senza_duplicati:
        lista_senza_duplicati.append(n)
print("Lista senza duplicati:", lista_senza_duplicati) """


""" Esercizio 3: Rotazione di una lista
Rotare una lista di k posizioni a destra.
Utilizzo di slicing per ottenere la lista ruotata.
Stampa del risultato. """

""" lista = [1, 2, 3, 4, 5]
k = 2
rotata = lista[k:] + lista[:k]
print("Lista rotata:", rotata) """


""" Esercizio 4: Intersezione di due liste
Creare due liste.
Trovare l'intersezione tra le due liste senza utilizzare set.
Stampa dell'intersezione. """

""" lista_1 =[1,2,3,4,5,6] 
lista_2 =[6,7,8,9,10]

intersezione = [n for n in lista_1 if n in lista_2]
print("Intersezione:", intersezione) """

""" Esercizio 5: Conversione di una lista di tuple in dizionario
Data una lista di tuple, convertirla in un dizionario.
Utilizzare la funzione dict() per effettuare la conversione.
Stampa del dizionario risultante. """
""" lista_tupla=[("a", 1), ("b", 2), ("c", 3)]
dizionario_tupla= dict(lista_tupla)
print(dizionario_tupla) """

""" Esercizio 6: Somma di tutte le tuple
Sommare gli elementi all'interno di una lista di tuple.
Utilizzare la funzione sum() e un ciclo for.
Stampa della somma totale. """
""" tupla_lista=[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
somma=0
for tupla in tupla_lista:
    somma+=sum(tupla)
print(somma)     """


""" Esercizio 7: Tuple con massimo e minimo di una lista
Creare una dupla contenente il minimo e il massimo di una lista.
Utilizzare le funzioni min() e max() per ottenere i valori.
Stampa della dupla risultante. """
""" tupla_lista=(1,3,5,8,9)
print(min(tupla_lista), max(tupla_lista)) """


""" Ordinare una Lista di Tuple
Abbiamo creato una lista di tuple e l'abbiamo ordinata per il secondo elemento di ciascuna. 
Abbiamo usato la funzione sorted con una lambda per specificare il criterio d'ordinamento. """
""" nomi_eta=[("Giovanni", 32), ("Paolo", 26), ("Luigi", 19), ("Teresa", 32)]
nomi_eta_ordinata=sorted(nomi_eta, key=lambda eta: eta[1])
print(nomi_eta_ordinata) """

""" Creare una Tupla con Numeri Pari
Partendo da una tupla di numeri, abbiamo estratto i numeri pari per formare una nuova tupla. """
""" tupla=(1,2,3,4,5,6,7,8,9)
tupla_pari=tuple(n for n in tupla if n % 2 ==0)
print(tupla_pari) """

""" Invertire una Tupla
Abbiamo dimostrato come si inverte una tupla utilizzando la funzione reversed """
""" tupla=(1,2,3,4,5,6,7,8,9)
tupla_invertita= tuple(reversed(tupla))
print(tupla_invertita) """

""" Conversione di Stringa in Tupla di Caratteri Unici
Abbiamo convertito una stringa in una tupla contenente solo i caratteri unici utilizzando l'oggetto set. """
""" stringa="Ciao, come stai?"
tupla_caratteri=tuple(set(stringa.lower()))
print(tupla_caratteri) """

""" Zippare Due Liste in una Lista di Tuple
Abbiamo combinato due liste in una lista di tuple utilizzando la funzione zip. """
""" lista_1=["Chiara", "Marco", "Luca"]
lista_2=["Paolo","Franco","Roberto"]

lista_combinata=list(zip(lista_1,lista_2))
print(lista_combinata) """

""" Differenza Simmetrica tra Set
Abbiamo calcolato la differenza simmetrica tra vari set creando un nuovo set contenente elementi unici di ciascun insieme. """

""" A = {1, 2, 3}
B = {3, 4, 5}
C = {5, 6}
diff = A ^ B ^ C
print("Diff simmetrica:", diff) """

""" Filtrare Parole Uniche in una Frase
Dalla frase data, abbiamo creato un set di parole uniche utilizzando split e set. """
""" frase="Ciao, come va? Ciao, tutto bene ed a te come va?"
parole_uniche=set(frase.split())
print(parole_uniche) """

""" Unione di Set da Lista di Liste
Abbiamo mostrato come unire diverse liste di numeri in un unico set senza duplicati. """
""" liste = [[1, 2, 3], [3, 4, 5], [6, 7]]
unione = set().union(*map(set, liste))
print("Unione:", unione) """

""" Esercizio 1: Operazioni con i Set
Creazione di variabili set e esecuzione di operazioni di intersezione, differenza e conteggio degli elementi unici. """
""" set_1={1,2,3,4,5}
set_2={4,5,6,7,8}

intersezione=set(set_1&set_2)
print(intersezione)
differenza=set(set_1-set_2)
print(differenza)
cont_elementi=(len(set_1 | set_2))
print(cont_elementi) """

""" Esercizio 2: Generazione di Numeri Casuali
Uso della libreria random per generare set di numeri casuali e stampa dei risultati. """
""" import random

s_numeri= {random.randint(1,150) for _ in range(10)} #me né aspettavo 9..
print(s_numeri) """

""" Esercizio 3: Conteggio delle Occorrenze delle Parole
Conta delle occorrenze di parole in una frase utilizzando dizionari? e le funzioni split e get. """
""" frase = "Ciao, come va? Ciao, tutto bene ed a te come va?"

frase = frase.replace(",", "").replace("?", "")

parole = frase.split()

conteggio = {}

for parola in parole:
    parola = parola.lower()
    conteggio[parola] = conteggio.get(parola, 0) + 1

print(conteggio) """
    


""" Esercizio 4: Inversione di Chiavi e Valori nei Dizionari
Inversione di chiavi e valori in un dizionario con un ciclo for e la funzione items. """
""" nomi_eta={"Paolo": 30, "Giulia": 25, "Maria": 28, "Giuseppe": 32}
#nomi_eta_invertito={}
nomi_eta_invertito={valore: chiave for chiave, valore in nomi_eta.items()} """


""" for chiave, valore in nomi_eta.items():
    nomi_eta_invertito[valore]=chiave"""
""" print(nomi_eta_invertito)  """

""" Esercizio 5: Creazione di un Dizionario da Due Liste
Utilizzo di dict e zip per creare un dizionario da due liste di chiavi e valori. """
""" lista_chiavi = ["A", "B", "C", "D", "E"]
lista_valori = [1, 2, 3, 4, 5]
dizionario = dict(zip(lista_chiavi, lista_valori))
print(dizionario)
 """
""" Esercizio 6: Raggruppamento per Lunghezza delle Parole
Raggruppare le parole in base alla loro lunghezza usando un dizionario vuoto iniziale e la funzione setdefault. """
""" frase="Mi piace il cibo, ma non mi piace la cucina"
parole=frase.split()
dizionario={}
for parola in parole:
    lunghezza=len(parola)
    dizionario.setdefault(lunghezza, []).append(parola)
print(dizionario) """

""" Esercizio 7: Frequenza delle Lettere in una Parola
Calcolare la frequenza di ciascuna lettera in una parola utilizzando un dizionario vuoto e un ciclo for. """

""" frase_1 = "Ciao, come va? Ciao, tutto bene ed a te come va?"

frase_1 = frase_1.replace(",", "").replace("?", "")

conteggio = {}

for c in frase_1.lower():
    conteggio[c] = conteggio.get(c, 0) + 1

print(conteggio) """

#Fuonzioni
""" Esercizio :Definisci una funzione chiamata media che:
· Riceve una lista di numeri (parametro)
· Calcola e restituisce la media (somma/numero elementi)

Ad esempio:
print(media([2, 4, 6])) # Stampa 4

Usa len() e sum() per renderla semplice, leggibile ed efficace. """
""" def media(*args):
    return sum(args)/len(args)

numeri=int(input("Inserisci numero o premi 0 per uscire: "))

lista_numeri=[]
while (numeri != 0):
    lista_numeri.append(numeri)
    numeri=int(input("Inserisci numero o premi 0 per uscire: "))
    
print(f"La lista di numeri è {lista_numeri} la cui media è {media(*lista_numeri)}") """

#Creazione agenda
""" Aggiungi Contatto
Crea un contatto sotto forma di dizionario con nome, numero e email.
Aggiunge il contatto alla lista della rubrica. """

""" agenda={}
def aggiungi_contatto():
    print("*************Aggiungi nuovo contatto*****************")
    nome=str(input("Inserisci nome: "))
    numero=int(input("Inserisci numero: "))
    mail=str(input("Inserisci mail: "))
    
    agenda[nome] = {"numero": numero, "mail": mail}
    print("Contatto aggiunto!") """

""" Modifica Contatto
Cerca un contatto nella rubrica per nome.
Modifica il numero o l'email del contatto, se specificato. """
""" def modifica_contatto():
    print("************* Modifica contatto *****************")
    nome = input("Quale contatto vuoi modificare? Inserisci il nome: ")

    if nome not in agenda:
        print("Contatto non trovato.")
        return

    print(f"Contatto attuale: {agenda[nome]}")

    print("Modifica:")
    numero = input("Inserisci nuovo numero: ")
    mail = input("Inserisci nuova mail: ")

    agenda[nome]["numero"] = numero
    agenda[nome]["mail"] = mail

    print("Contatto modificato con successo!") """

""" Elimina Contatto
Rimuove un contatto dalla rubrica per nome. """
""" def elimina_contatto():
    print("************* Elimina contatto *****************")
    nome = input("Quale contatto vuoi eliminare? Inserisci il nome: ")

    if nome not in agenda:
        print("Contatto non trovato.")
        return

    print(f"Contatto selezionato: {agenda[nome]}")

    conferma = input(f"Sei sicuro di voler eliminare {nome}? (s/n): ").lower()

    if conferma == "s":
        agenda.pop(nome)
        print("Contatto eliminato con successo!")
    else:
        print("Nessuna operazione effettuata.") """

""" Cerca Contatto
Cerca un contatto nella rubrica e stampa i suoi dettagli. """
""" def visualizza_contatto():
    print("************* Contatto *****************")
    nome = input("Quale contatto vuoi visualizzare? Inserisci il nome: ")

    if nome not in agenda:
        print("Contatto non trovato.")
        return

    print(f"Contatto selezionato: {agenda[nome]}")
 """

""" Mostra Contatti
Visualizza tutti i contatti presenti nella rubrica in ordine alfabetico. """
#def chiama_menu():
""" Funzione che stampa il menu' e chiama la funzione scelta """
   # print("***************** Agenda V 1.0.0 ********************")
    #print("Ciao, cosa vuoi fare?\n")

"""  while True:
        menu = int(input(
            "Premi: \n"
            " 1 per aggiungere contatto \n"
            " 2 per modificare contatto \n"
            " 3 per eliminare contatto \n"
            " 4 per cercare contatto \n"
            " 5 per vedere i contatti esistenti \n"
            " 0 per uscire: "
        ))

        scelta(menu) """

""" if menu == 0:
            break
def scelta(menu):
    match menu:
        case 1:
            aggiungi_contatto()
        case 2:
            modifica_contatto()
        case 3:
            elimina_contatto()
        case 4:
            visualizza_contatto()
        case 5:
            print("Contatti esistenti:")
            print(agenda)
        case 0:
            print("Uscita dal programma")
        case _:
            print("Scelta non valida")

chiama_menu() """

#funzioni
#Scrivere un programma che analizzi un testo.
#Calcolare il numero totale di parole.
#Calcolare la frequenza di ciascuna parola.
#Estrarre le parole uniche utilizzando un set.
#Mostrare le cinque parole più frequenti.
#Calcolare la lunghezza media delle parole.
#Funzioni Implementate

""" testo_analisi=str(input("Inserisci il testo da analizzare: ")) """

#puliscitesto: Riceve una stringa e rimuove i simboli di punteggiatura, trasformando il testo in minuscolo.
""" def pulisci_testo(testo):
    simboli = ",?!.:;"
    for s in simboli:
        testo = testo.replace(s, "")
    return testo.lower() """


#contaparole: Divide il testo in una lista di parole e restituisce il numero totale.
""" def conta_parole(testo):
    testo = pulisci_testo(testo)
    parole = testo.split()
    return len(parole)


dizionario={} """

#frequenza_parole: Calcola e restituisce un dizionario con la frequenza di ciascuna parola nel testo.
""" def frequenza_parole(testo):
    testo = pulisci_testo(testo)
    parole = testo.split()
    diz = {}

    for p in parole:
        diz[p] = diz.get(p, 0) + 1

    return diz
 """

#parole_uniche: Restituisce un insieme di parole uniche dal testo. 
""" def parole_uniche(testo):
    testo = pulisci_testo(testo)
    parole = testo.split()
    return set(parole) """


#top_n_parole: Ordina le parole per frequenza in ordine decrescente e restituisce le prime n parole.        
""" def top_n_parole(testo, n):
    diz = frequenza_parole(testo)
    ordinate = sorted(diz.items(), key=lambda x: x[1], reverse=True)
    return ordinate[:n] """

        
#lunghezza_media: Calcola la lunghezza media delle parole nel testo pesata per la frequenza.    
""" def lunghezza_media(testo):
    testo = pulisci_testo(testo)
    parole = testo.split()
    somma = sum(len(p) for p in parole)
    media = somma / len(parole)
    return media """

""" def menu():
    testo = input("Inserisci il testo da analizzare: ")

    while True:
        print("\n--- MENU ANALISI TESTO ---")
        print("1) Conta parole")
        print("2) Parole uniche")
        print("3) Frequenza parole")
        print("4) Top N parole")
        print("5) Lunghezza media parole")
        print("0) Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            print("Numero totale di parole:", conta_parole(testo))

        elif scelta == "2":
            print("Parole uniche:", parole_uniche(testo))

        elif scelta == "3":
            print("Frequenza parole:", frequenza_parole(testo))

        elif scelta == "4":
            n = int(input("Quante parole vuoi visualizzare? "))
            print("Top", n, "parole:", top_n_parole(testo, n))

        elif scelta == "5":
            print("Lunghezza media delle parole:", lunghezza_media(testo))

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")

menu() """

        
    







