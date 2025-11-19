# Es7: Combinatoria

**Livello:** BASE
**Durata stimata:** 2-3 ore

## Descrizione

Programma per calcolare fattoriali, permutazioni, disposizioni e combinazioni, con applicazioni pratiche.

## Obiettivi

### Competenze Matematica
- Calcolare fattoriali
- Comprendere permutazioni (con e senza ripetizione)
- Calcolare disposizioni semplici e con ripetizione
- Calcolare combinazioni semplici
- Applicare il calcolo combinatorio a problemi reali

### Competenze Informatica
- Ricorsione vs iterazione
- Modulo `math.factorial()`
- Funzioni matematiche
- Gestione numeri grandi

## Consegna

Il programma deve calcolare:

### 1. Fattoriale
- n! = n × (n-1) × (n-2) × ... × 2 × 1
- Esempio: 5! = 120

### 2. Permutazioni Semplici
- P(n) = n!
- Quanti modi di ordinare n oggetti distinti
- Esempio: 3 persone in fila = 3! = 6 modi

### 3. Permutazioni con Ripetizione
- P(n; k₁, k₂, ...) = n! / (k₁! × k₂! × ...)
- Esempio: Anagrammi di "MAMMA" = 5! / (3! × 2!) = 10

### 4. Disposizioni Semplici
- D(n, k) = n! / (n-k)!
- Scegliere k oggetti da n con ordine importante
- Esempio: Podio di 3 su 8 atleti = D(8,3) = 336

### 5. Disposizioni con Ripetizione
- D'(n, k) = n^k
- Esempio: Codice PIN 4 cifre = 10^4 = 10000

### 6. Combinazioni Semplici
- C(n, k) = n! / (k! × (n-k)!)
- Scegliere k oggetti da n senza ordine
- Esempio: Ambo del lotto (2 su 90) = C(90,2) = 4005

## Esempio di Utilizzo

```
=== CALCOLATORE COMBINATORIA ===

Scegli il calcolo:
1. Fattoriale (n!)
2. Permutazioni semplici (P_n)
3. Permutazioni con ripetizione
4. Disposizioni semplici (D_{n,k})
5. Disposizioni con ripetizione (D'_{n,k})
6. Combinazioni (C_{n,k})
7. Esempi pratici

Scelta: 6

Inserisci n (totale elementi): 90
Inserisci k (elementi da scegliere): 2

Risultato:
C(90, 2) = 4005

Esempio: Numero di ambi possibili al gioco del Lotto
```

## Formule

```
Fattoriale:
n! = n × (n-1)!
0! = 1

Permutazioni semplici:
P(n) = n!

Permutazioni con ripetizione:
P(n; k₁, k₂, ..., kₘ) = n! / (k₁! × k₂! × ... × kₘ!)

Disposizioni semplici:
D(n, k) = n! / (n - k)!

Disposizioni con ripetizione:
D'(n, k) = n^k

Combinazioni semplici:
C(n, k) = n! / (k! × (n - k)!)
```

## Suggerimenti di Codice

```python
import math

def fattoriale(n):
    """Calcola n!"""
    return math.factorial(n)
    # Oppure ricorsivamente:
    # if n <= 1:
    #     return 1
    # return n * fattoriale(n - 1)

def permutazioni(n):
    """P(n) = n!"""
    return math.factorial(n)

def disposizioni(n, k):
    """D(n,k) = n! / (n-k)!"""
    return math.factorial(n) // math.factorial(n - k)

def disposizioni_rip(n, k):
    """D'(n,k) = n^k"""
    return n ** k

def combinazioni(n, k):
    """C(n,k) = n! / (k! * (n-k)!)"""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    # Oppure usa math.comb(n, k) in Python 3.8+
```

## Esempi Pratici da Implementare

### Codici e Password
- **Targa auto** (2 lettere + 3 cifre + 2 lettere): D'(26,2) × D'(10,3) × D'(26,2)
- **PIN bancario** (4 cifre): D'(10,4) = 10000
- **Password** (6 caratteri alfanumerici): D'(62,6) ≈ 56 miliardi

### Giochi
- **Tombola**: estrarre 90 numeri in ordine = P(90)
- **Lotto**: ambo (2 su 90) = C(90,2) = 4005
- **Superenalotto**: sestina (6 su 90) = C(90,6) ≈ 622 milioni

### Gruppi e Squadre
- **Scegliere 5 studenti** da classe di 25 = C(25,5)
- **Formare squadre di calcio** (11 da 20) = C(20,11)

### Anagrammi
- **ROMA**: 4! = 24
- **MAMMA**: 5! / (3! × 2!) = 10
- **MATEMATICA**: 10! / (3! × 2! × 2!) = 151200

## Estensioni

- Calcolare coefficienti binomiali
- Triangolo di Pascal/Tartaglia
- Principio di inclusione-esclusione
- Generare tutte le combinazioni/permutazioni
- Stimare probabilità usando combinatoria

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🔢📐**
