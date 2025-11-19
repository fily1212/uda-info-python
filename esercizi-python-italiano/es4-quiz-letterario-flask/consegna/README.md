# Esercizio 4: Quiz Letterario con Flask

## Livello: AVANZATO

## Obiettivi didattici
- **Informatica**: Web development, Flask, HTML, routing, sessioni, template
- **Italiano**: Letteratura italiana, autori, opere, citazioni, periodi letterari

## Descrizione
Crea un'applicazione web interattiva con Flask che propone un quiz sulla letteratura italiana. L'utente risponde a domande e alla fine riceve un punteggio.

## Requisiti

### Backend (Flask)
1. Almeno 10 domande sulla letteratura italiana
2. Sistema di punteggio
3. Pagine:
   - Homepage con introduzione
   - Pagina quiz con domande
   - Pagina risultati con punteggio finale
4. Routing corretto tra le pagine

### Frontend (HTML/CSS)
1. Design pulito e leggibile
2. Bottoni per le risposte
3. Feedback visivo (risposte corrette/sbagliate)
4. Layout responsive (opzionale)

### Contenuti
Le domande possono riguardare:
- Autori e loro opere
- Citazioni famose
- Periodi letterari
- Personaggi di romanzi
- Date storiche della letteratura

## Struttura del progetto

```
quiz-letterario/
├── app.py              # Applicazione Flask principale
├── templates/
│   ├── index.html      # Homepage
│   ├── quiz.html       # Pagina delle domande
│   └── risultati.html  # Pagina dei risultati
└── static/
    └── style.css       # Stili CSS (opzionale)
```

## Esempio di domande

```python
DOMANDE = [
    {
        "domanda": "Chi ha scritto 'La Divina Commedia'?",
        "opzioni": ["Dante Alighieri", "Petrarca", "Boccaccio", "Ariosto"],
        "risposta": "Dante Alighieri"
    },
    {
        "domanda": "In che anno è stato pubblicato 'I Promessi Sposi'?",
        "opzioni": ["1827", "1840", "1861", "1900"],
        "risposta": "1827"
    },
    # ... altre domande
]
```

## Esempio di Output (Web)

**Homepage:**
```
╔════════════════════════════════════╗
║   QUIZ LETTERATURA ITALIANA        ║
╠════════════════════════════════════╣
║                                    ║
║  Testa le tue conoscenze sulla     ║
║  letteratura italiana!             ║
║                                    ║
║  10 domande                        ║
║  1 punto per risposta corretta     ║
║                                    ║
║  [  INIZIA IL QUIZ  ]              ║
║                                    ║
╚════════════════════════════════════╝
```

**Pagina Quiz:**
```
Domanda 1/10

Chi ha scritto 'La Divina Commedia'?

[ Dante Alighieri ]
[ Petrarca ]
[ Boccaccio ]
[ Ariosto ]
```

**Risultati:**
```
Quiz completato!

Punteggio: 8/10

Ottimo lavoro! Hai una buona conoscenza
della letteratura italiana.

[ RICOMINCIA ]
```

## Installazione Flask

Prima di iniziare, installa Flask:
```bash
pip install flask
```

## Funzionamento Flask base

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## Suggerimenti
- Usa `session` di Flask per memorizzare il punteggio tra le pagine
- Usa `request.method == 'POST'` per gestire l'invio delle risposte
- Randomizza l'ordine delle domande per ogni tentativo
- Usa template Jinja2 per rendere dinamico l'HTML

## Estensioni opzionali
- Timer per ogni domanda
- Classifica dei migliori punteggi
- Categorie di domande (Dante, Petrarca, Letteratura moderna, ecc.)
- Spiegazione della risposta corretta
- Statistiche dettagliate (percentuale risposte corrette per categoria)

## Consegna
1. Salva l'applicazione Flask come `app.py`
2. Crea i template HTML necessari
3. Testa l'applicazione aprendo http://localhost:5000
4. Fai almeno 3 test completi del quiz

## Come eseguire
```bash
python app.py
```
Poi apri il browser a: http://localhost:5000
