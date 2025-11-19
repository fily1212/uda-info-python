# Esercizio 3: Generatore di Rime

## Livello: INTERMEDIO

## Obiettivi didattici
- **Informatica**: Dizionari, liste, manipolazione stringhe, pattern matching, file
- **Italiano**: Rime, metrica, terminazioni delle parole, poesia

## Descrizione
Crea un programma Python che trova parole in rima data una parola di input. Il programma deve avere un vocabolario di parole italiane e trovare quelle che rimano.

## Cos'è una Rima?
Due parole rimano quando hanno la stessa terminazione sonora dall'ultima vocale accentata in poi.

Esempi:
- **amore** - **cuore** (terminano in -ore)
- **stella** - **bella** (terminano in -ella)
- **cantare** - **sognare** (terminano in -are)

## Requisiti

Il programma deve:
1. Avere un vocabolario di almeno 50 parole italiane comuni
2. Chiedere all'utente una parola
3. Trovare tutte le parole nel vocabolario che rimano con quella data
4. Mostrare le rime trovate raggruppate per tipo di terminazione
5. Gestire il caso in cui non ci siano rime

## Funzionalità opzionali
- Salvare il vocabolario in un file esterno
- Permettere all'utente di aggiungere nuove parole al vocabolario
- Classificare le rime (baciata, alternata, incrociata)

## Esempio di Output

```
=== GENERATORE DI RIME ===

Vocabolario caricato: 50 parole

Inserisci una parola: amore

🔍 Ricerca rime per "amore"...

Rime trovate (3):
  ✓ cuore
  ✓ fiore
  ✓ dolore

Terminazione comune: -ore

Vuoi cercare un'altra parola? (s/n): n
Arrivederci, poeta! 📝
```

## Suggerimenti
- Usa un dizionario o una lista per memorizzare le parole
- Per trovare le rime, confronta gli ultimi 2-3 caratteri delle parole
- La funzione `parola.endswith(suffisso)` verifica se una parola termina con un certo suffisso
- Per un algoritmo più preciso:
  ```python
  def estrai_suffisso(parola, n_caratteri=3):
      return parola[-n_caratteri:].lower()
  ```

## Vocabolario minimo richiesto
Crea un vocabolario con almeno 50 parole che copra varie terminazioni:
- Parole in -are (amare, sognare, cantare...)
- Parole in -ore (amore, fiore, cuore...)
- Parole in -ello/a (bello, stella, castello...)
- Parole in -ino/a (bambino, mattino, vicino...)
- Parole in -ento/a (vento, momento, lento...)

## Estensioni opzionali
- Ordinare le rime alfabeticamente
- Mostrare il numero di sillabe di ogni rima
- Creare una funzione che genera versi in rima automaticamente
- Implementare rime imperfette (assonanza, consonanza)

## Consegna
Salva il programma come `trova_rime.py` e testa con almeno 5 parole diverse dimostrando che il tuo vocabolario è vario.
