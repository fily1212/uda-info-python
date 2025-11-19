# Es5: Calcolo Probabilità

**Livello:** FACILE
**Durata stimata:** 2-3 ore

## Descrizione

Programma per calcolare probabilità di eventi semplici, composti, indipendenti e complementari con esempi pratici.

## Obiettivi

### Competenze Matematica
- Probabilità classica: P(E) = casi favorevoli / casi possibili
- Eventi complementari: P(non E) = 1 - P(E)
- Eventi indipendenti: P(A ∩ B) = P(A) × P(B)
- Probabilità condizionata
- Unione di eventi: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

### Competenze Informatica
- Input/output formattato
- Operazioni con frazioni
- Modulo `fractions` per calcoli esatti
- Funzioni matematiche

## Consegna

Il programma deve calcolare:

### 1. Probabilità Semplice
- Dati casi favorevoli e casi possibili
- Calcolare P(E) e mostrarla come frazione e percentuale

### 2. Evento Complementare
- Data P(E), calcolare P(non E)

### 3. Eventi Indipendenti
- Date P(A) e P(B), calcolare P(A e B)
- Esempio: due estrazioni con reimmissione

### 4. Eventi Dipendenti
- Probabilità condizionata: P(A|B)
- Esempio: estrazioni senza reimmissione

### 5. Unione di Eventi
- P(A o B) con eventi disgiunti e non disgiunti

### 6. Esempi Pratici
- Carte da gioco
- Dadi
- Urne con palline
- Monete

## Esempio di Utilizzo

```
=== CALCOLATORE PROBABILITÀ ===

Scegli il tipo di calcolo:
1. Probabilità semplice
2. Evento complementare
3. Eventi indipendenti (A e B)
4. Unione di eventi (A o B)
5. Probabilità condizionata
6. Esempi pratici

Scelta: 1

Inserisci casi favorevoli: 13
Inserisci casi possibili: 52

Risultato:
P(E) = 13/52 = 1/4 = 0.25 = 25%

Esempio: Probabilità di pescare un cuori da un mazzo di carte
```

## Esempi Pratici da Implementare

### Carte da Gioco (52 carte)
- P(cuori) = 13/52 = 1/4
- P(asso) = 4/52 = 1/13
- P(figura) = 12/52 = 3/13

### Dadi
- P(6 su 1 dado) = 1/6
- P(doppio 6 su 2 dadi) = 1/36
- P(somma 7 su 2 dadi) = 6/36 = 1/6

### Urna
- Urna: 5 rosse, 3 blu, 2 verdi
- P(rossa) = 5/10 = 1/2
- P(non rossa) = 5/10 = 1/2
- P(2 rosse senza reimmissione) = (5/10) × (4/9) = 20/90 = 2/9

## Suggerimenti di Codice

```python
from fractions import Fraction

def probabilita_semplice(favorevoli, possibili):
    """Calcola P(E) = favorevoli / possibili"""
    prob = Fraction(favorevoli, possibili)
    percentuale = (favorevoli / possibili) * 100
    return prob, percentuale

def evento_complementare(prob):
    """Calcola P(non E) = 1 - P(E)"""
    return 1 - prob

def eventi_indipendenti(prob_a, prob_b):
    """P(A e B) = P(A) × P(B)"""
    return prob_a * prob_b

def unione_eventi(prob_a, prob_b, prob_a_e_b=0):
    """P(A o B) = P(A) + P(B) - P(A e B)"""
    return prob_a + prob_b - prob_a_e_b
```

## Formule Utili

```
Probabilità base:
P(E) = casi_favorevoli / casi_possibili

Evento complementare:
P(non E) = 1 - P(E)

Eventi indipendenti:
P(A e B) = P(A) × P(B)

Eventi mutuamente esclusivi:
P(A o B) = P(A) + P(B)

Eventi non mutuamente esclusivi:
P(A o B) = P(A) + P(B) - P(A e B)

Probabilità condizionata:
P(A|B) = P(A e B) / P(B)
```

## Estensioni

- Teorema di Bayes
- Variabili aleatorie
- Valore atteso
- Problemi del compleanno
- Simulazioni Monte Carlo per verificare i calcoli

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🎲📐**
