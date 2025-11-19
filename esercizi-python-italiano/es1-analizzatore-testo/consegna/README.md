# Esercizio 1: Analizzatore di Testo

## Livello: BASE

## Obiettivi didattici
- **Informatica**: Manipolazione stringhe, funzioni, cicli, condizioni
- **Italiano**: Analisi testuale, elementi grammaticali, struttura del testo

## Descrizione
Crea un programma Python che analizza un testo fornito dall'utente e fornisce statistiche dettagliate.

## Requisiti

Il programma deve:
1. Chiedere all'utente di inserire un testo (può essere una frase, un paragrafo o una poesia)
2. Calcolare e mostrare:
   - Numero totale di caratteri (con e senza spazi)
   - Numero di parole
   - Numero di frasi (considerate separate da `.`, `!`, `?`)
   - Numero di vocali e consonanti
   - Parola più lunga e più corta
   - Lunghezza media delle parole
3. Mostrare i risultati in modo chiaro e formattato

## Esempio di Output

```
=== ANALIZZATORE DI TESTO ===

Inserisci il testo da analizzare:
> La vita è bella. Ogni giorno è un dono!

--- STATISTICHE ---
Caratteri totali: 37
Caratteri (senza spazi): 30
Parole: 8
Frasi: 2
Vocali: 16
Consonanti: 14

Parola più lunga: giorno (6 lettere)
Parola più corta: è (1 lettere)
Lunghezza media parole: 3.75 lettere
```

## Suggerimenti
- Usa il metodo `.split()` per dividere il testo in parole
- Per contare vocali, puoi creare una stringa con tutte le vocali e verificare se ogni carattere è contenuto
- La funzione `len()` restituisce la lunghezza di una stringa
- Usa cicli `for` per iterare sui caratteri o sulle parole

## Estensioni opzionali (per chi finisce prima)
- Mostrare la frequenza di ogni lettera dell'alfabeto
- Identificare e contare le congiunzioni comuni (e, ma, o, né, ecc.)
- Calcolare la percentuale di parole lunghe (oltre 7 lettere)

## Consegna
Salva il programma come `analizzatore.py` e testalo con almeno 3 testi diversi:
1. Una frase breve
2. Un paragrafo più lungo
3. Una poesia di 4-6 versi
