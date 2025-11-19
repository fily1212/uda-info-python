# Esercizio 5: Generatore di Racconti

## Livello: AVANZATO

## Obiettivi didattici
- **Informatica**: Strutture dati complesse, randomizzazione, logica, funzioni, file I/O
- **Italiano**: Struttura narrativa, personaggi, trama, elementi del racconto

## Descrizione
Crea un programma Python che genera automaticamente racconti brevi combinando elementi narrativi casuali ma mantenendo una coerenza di base.

## Elementi di un Racconto

Un racconto completo deve avere:
1. **Personaggio principale** (protagonista)
2. **Ambientazione** (dove e quando)
3. **Conflitto/Problema** (cosa accade)
4. **Sviluppo** (come evolve la situazione)
5. **Conclusione** (come si risolve)

## Requisiti

Il programma deve:
1. Avere database di elementi narrativi:
   - Personaggi (nome, caratteristiche)
   - Luoghi (ambientazioni)
   - Conflitti/Problemi
   - Azioni/Eventi
   - Conclusioni
2. Generare racconti casuali ma coerenti
3. Permettere all'utente di scegliere il genere (avventura, mistero, fantasy, ecc.)
4. Mostrare il racconto in modo formattato
5. Salvare i racconti generati in file di testo

## Struttura suggerita

```python
PERSONAGGI = [
    {"nome": "Marco", "tipo": "giovane studente", "caratteristica": "curioso"},
    {"nome": "Sofia", "tipo": "detective", "caratteristica": "intelligente"},
    ...
]

LUOGHI = [
    {"dove": "in una biblioteca antica", "quando": "al tramonto"},
    {"dove": "in una foresta oscura", "quando": "a mezzanotte"},
    ...
]

CONFLITTI = [
    "trovò un libro misterioso che parlava di un tesoro nascosto",
    "scoprì che qualcuno stava tramando un complotto",
    ...
]
```

## Esempio di Output

```
=== GENERATORE DI RACCONTI ===

Scegli il genere:
1. Avventura
2. Mistero
3. Fantasy
4. Romantico
5. Casuale

> 2

╔═══════════════════════════════════════════════════╗
║                 IL SEGRETO PERDUTO                ║
╠═══════════════════════════════════════════════════╣

C'era una volta Sofia, una detective intelligente.

Un giorno, in una biblioteca antica al tramonto,
Sofia scoprì che qualcuno stava tramando un complotto
per rubare un antico manoscritto.

Con coraggio e astuzia, Sofia iniziò a seguire le
tracce lasciate dal misterioso ladro. Dopo giorni
di indagini, raccolse prove sufficienti per
smascherare il colpevole.

Alla fine, la verità venne a galla: il bibliotecario
aveva agito per proteggere il manoscritto da
un'organizzazione pericolosa. Sofia comprese le
sue ragioni e insieme trovarono un modo per
mettere al sicuro l'antico testo.

╚═══════════════════════════════════════════════════╝

Vuoi salvare questo racconto? (s/n): s
✅ Racconto salvato in racconti/racconto_001.txt

Generare un altro racconto? (s/n):
```

## Suggerimenti
- Usa dizionari per organizzare elementi complessi (personaggi, luoghi)
- Crea template di frasi che si adattano ai diversi elementi
- Usa la funzione `random.choice()` per selezionare elementi casuali
- Per ogni genere, crea liste specifiche di elementi coerenti
- Numera automaticamente i racconti salvati

## Database minimo richiesto
Per ogni genere:
- Almeno 5 personaggi diversi
- Almeno 5 ambientazioni
- Almeno 5 conflitti
- Almeno 5 sviluppi possibili
- Almeno 5 conclusioni

## Estensioni opzionali
- Generare un titolo accattivante per ogni racconto
- Permettere all'utente di scegliere alcuni elementi (es. nome personaggio)
- Aggiungere dialoghi tra personaggi
- Creare racconti più lunghi con capitoli
- Implementare un sistema di "morale della storia"
- Esportare in formato HTML con formattazione avanzata

## Consegna
1. Salva il programma come `genera_racconto.py`
2. Crea una cartella `racconti/` per salvare le storie generate
3. Genera almeno 5 racconti di generi diversi
4. Dimostra che i racconti hanno senso narrativo

## Valutazione
Il programma sarà valutato su:
- Varietà degli elementi narrativi
- Coerenza dei racconti generati
- Qualità della formattazione
- Creatività nell'implementazione
- Funzionamento corretto del salvataggio file
