# Esercizio 2: Generatore di Haiku

## Livello: INTERMEDIO

## Obiettivi didattici
- **Informatica**: Liste, dizionari, random, funzioni, strutture dati
- **Italiano**: Poesia giapponese, sillabe, metrica, creatività letteraria

## Descrizione
Crea un programma Python che genera automaticamente haiku rispettando la metrica tradizionale giapponese.

## Cos'è un Haiku?
L'haiku è una forma di poesia giapponese composta da 3 versi con questa struttura sillabica:
- **Verso 1**: 5 sillabe
- **Verso 2**: 7 sillabe
- **Verso 3**: 5 sillabe

Temi tipici: natura, stagioni, emozioni, momenti fugaci.

## Requisiti

Il programma deve:
1. Avere un database di parole/frasi organizzato per numero di sillabe
2. Generare haiku casuali rispettando la metrica 5-7-5
3. Permettere all'utente di generare più haiku
4. Mostrare ogni haiku in modo formattato e poetico

## Struttura suggerita

```python
# Database parole organizzate per sillabe
parole_5_sillabe = [...]
parole_7_sillabe = [...]
# Oppure combinazioni di parole che totalizzano le sillabe giuste
```

## Esempio di Output

```
=== GENERATORE DI HAIKU ===

Premi INVIO per generare un haiku (q per uscire):

╔═══════════════════════╗
║                       ║
║  Petali di rosa      ║  (5 sillabe)
║  Cadono lentamente qui  ║  (7 sillabe)
║  Primavera arriva     ║  (5 sillabe)
║                       ║
╚═══════════════════════╝

Premi INVIO per generare un haiku (q per uscire):
```

## Suggerimenti
- Usa `import random` per selezionare parole casuali
- Crea liste separate per ogni conteggio sillabico
- Puoi combinare 2-3 parole per raggiungere il numero di sillabe richiesto
  - Esempio 5 sillabe: "luna" (2) + "splende" (3) = 5
- La funzione `random.choice(lista)` seleziona un elemento casuale
- Per una versione semplificata, crea frasi complete già con il conteggio giusto

## Database minimo richiesto
Almeno:
- 10 frasi/combinazioni da 5 sillabe
- 10 frasi/combinazioni da 7 sillabe

## Estensioni opzionali
- Salvare gli haiku generati in un file di testo
- Permettere all'utente di scegliere un tema (natura, amore, stagioni)
- Verificare che gli haiku abbiano senso grammaticale
- Aggiungere colori con moduli come `colorama`

## Consegna
Salva il programma come `haiku_generator.py` e genera almeno 5 haiku diversi per dimostrare la varietà del tuo database.
