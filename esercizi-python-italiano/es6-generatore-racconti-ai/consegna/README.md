# Esercizio 6: Generatore di Racconti con AI (Gemini)

## Livello: AVANZATO

## Obiettivi didattici
- **Informatica**: API REST, gestione chiavi API, librerie esterne, async/await, error handling
- **Italiano**: Prompt engineering, valutazione testi generati da AI, editing letterario

## Descrizione
Estendi il generatore di racconti dell'Esercizio 5 utilizzando l'API di Google Gemini per generare racconti originali e creativi basati su parametri forniti dall'utente.

## Cos'è Gemini?
Google Gemini è un modello di intelligenza artificiale avanzato che può generare testi creativi, rispondere a domande e molto altro. In questo esercizio, lo useremo per creare racconti letterari.

## Requisiti

Il programma deve:
1. Permettere all'utente di scegliere:
   - Genere del racconto (mistero, avventura, fantasy, romantico, ecc.)
   - Lunghezza (breve, media, lunga)
   - Tema/argomento specifico
   - Personaggio principale (nome e caratteristiche)
2. Costruire un prompt efficace per Gemini
3. Chiamare l'API di Gemini per generare il racconto
4. Mostrare il racconto generato in modo formattato
5. Salvare i racconti in file di testo
6. Gestire errori (API key mancante, errori di rete, ecc.)

## Setup API Key

### Ottenere la chiave API gratuita:
1. Vai su [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Accedi con il tuo account Google
3. Crea una nuova API key
4. Copia la chiave

### Configurare la chiave:
Crea un file `.env` nella stessa cartella del programma:
```
GEMINI_API_KEY=la_tua_chiave_qui
```

**IMPORTANTE:** Non condividere mai la tua API key e non caricarla su GitHub!

## Installazione dipendenze

```bash
pip install google-generativeai python-dotenv
```

## Struttura del prompt

Un buon prompt per generare racconti dovrebbe includere:
- Genere e stile narrativo
- Lunghezza desiderata
- Personaggi e ambientazione
- Tema o messaggio
- Tono (serio, ironico, poetico, ecc.)

Esempio:
```
Scrivi un racconto di genere [GENERE] di circa [N] parole.
Il protagonista è [NOME], un/una [DESCRIZIONE].
Il racconto deve essere ambientato [DOVE/QUANDO].
Tema centrale: [TEMA].
Stile: [STILE] e [TONO].
```

## Esempio di Output

```
=== GENERATORE DI RACCONTI AI ===

🤖 Powered by Google Gemini

--- CONFIGURAZIONE RACCONTO ---

Genere:
  1. Mistero
  2. Avventura
  3. Fantasy
  4. Romantico
  5. Fantascienza
Scegli (1-5): 1

Lunghezza:
  1. Breve (~300 parole)
  2. Media (~600 parole)
  3. Lunga (~1000 parole)
Scegli (1-3): 2

Inserisci il nome del protagonista: Elena
Descrizione del protagonista: una detective esperta
Ambientazione: Milano contemporanea
Tema del racconto: un quadro rubato

Genera anche un titolo? (s/n): s

✨ Generazione in corso...

╔════════════════════════════════════════════╗
║        L'ENIGMA DELLA GALLERIA             ║
╠════════════════════════════════════════════╣

[Racconto generato da Gemini...]

Elena, detective esperta con anni di esperienza
alle spalle, ricevette una chiamata inaspettata...

[... resto del racconto ...]

╚════════════════════════════════════════════╝

💾 Salvare questo racconto? (s/n): s
✅ Racconto salvato in: racconti_ai/racconto_20240115_143022.txt

🔄 Generare un altro racconto? (s/n):
```

## Suggerimenti di implementazione

### 1. Configurazione Gemini
```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
```

### 2. Generazione testo
```python
response = model.generate_content(prompt)
racconto = response.text
```

### 3. Gestione errori
```python
try:
    response = model.generate_content(prompt)
    if response.text:
        return response.text
except Exception as e:
    print(f"Errore: {e}")
    return None
```

## Funzionalità richieste

### Base
- [ ] Configurazione API key da file .env
- [ ] Menu interattivo per scegliere parametri
- [ ] Costruzione prompt dinamico
- [ ] Chiamata API e recupero testo
- [ ] Visualizzazione formattata
- [ ] Salvataggio su file

### Avanzate (opzionali)
- [ ] Generazione titolo automatica
- [ ] Scelta dello stile narrativo (1a persona, 3a persona, ecc.)
- [ ] Rigenerazione se il racconto non piace
- [ ] Stima token/costi
- [ ] Salvataggio in formato Markdown
- [ ] Export in PDF

## Esempio di prompt avanzato

```python
prompt = f"""Sei un autore di racconti professionista.

Scrivi un racconto completo in italiano con queste caratteristiche:

GENERE: {genere}
LUNGHEZZA: circa {parole} parole
PROTAGONISTA: {nome}, {descrizione}
AMBIENTAZIONE: {ambientazione}
TEMA: {tema}
TONO: {tono}

Il racconto deve:
- Avere una struttura in tre atti (introduzione, sviluppo, conclusione)
- Includere dialoghi vivaci e realistici
- Usare un linguaggio ricco e descrittivo
- Concludersi con un finale soddisfacente ma non scontato

Inizia direttamente con il racconto, senza prefazioni.
"""
```

## Limiti API gratuita

Google Gemini offre un tier gratuito con limiti:
- 60 richieste al minuto
- Lunghezza massima output: ~2000 parole

Gestisci questi limiti nel tuo codice!

## Estensioni creative

1. **Modalità collaborativa:** L'utente scrive l'inizio, Gemini continua
2. **Editing AI:** Chiedi a Gemini di migliorare un racconto esistente
3. **Traduzione:** Genera in italiano e traduci in altre lingue
4. **Analisi critica:** Chiedi a Gemini di analizzare il racconto generato
5. **Variazioni:** Genera 3 versioni diverse dello stesso racconto

## Riflessioni etiche

Discuti con la classe:
- Cosa significa "creatività" quando un'AI scrive?
- I racconti generati da AI sono "autentici"?
- Come citare correttamente un testo generato da AI?
- Quali sono i rischi dell'uso di AI nella scrittura creativa?

## Consegna

1. Salva il programma come `genera_racconto_ai.py`
2. Crea il file `.env` con la tua API key
3. Genera almeno 3 racconti di generi diversi
4. Salva i racconti nella cartella `racconti_ai/`
5. Scrivi un breve commento critico su uno dei racconti generati

## Valutazione

- Funzionamento corretto dell'API (30%)
- Qualità del prompt engineering (25%)
- Gestione errori e UX (20%)
- Creatività parametri configurabili (15%)
- Riflessione critica sui risultati (10%)
