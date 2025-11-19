# Quiz Letterario Flask - SOLUZIONE
# Esercizio 4 - UDA Italiano + Informatica

from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'chiave-segreta-quiz-letterario-2024'


# Domande sulla letteratura italiana
DOMANDE = [
    {
        "domanda": "Chi ha scritto 'La Divina Commedia'?",
        "opzioni": ["Dante Alighieri", "Francesco Petrarca", "Giovanni Boccaccio", "Ludovico Ariosto"],
        "risposta": "Dante Alighieri",
        "spiegazione": "Dante Alighieri scrisse la Divina Commedia tra il 1304 e il 1321."
    },
    {
        "domanda": "In che anno è stato pubblicato 'I Promessi Sposi'?",
        "opzioni": ["1827", "1840", "1861", "1900"],
        "risposta": "1827",
        "spiegazione": "La prima edizione de 'I Promessi Sposi' fu pubblicata nel 1827."
    },
    {
        "domanda": "Chi è l'autore del 'Canzoniere'?",
        "opzioni": ["Francesco Petrarca", "Dante Alighieri", "Giacomo Leopardi", "Ugo Foscolo"],
        "risposta": "Francesco Petrarca",
        "spiegazione": "Il Canzoniere è la raccolta di poesie di Francesco Petrarca dedicata a Laura."
    },
    {
        "domanda": "Quale di queste opere è stata scritta da Giovanni Boccaccio?",
        "opzioni": ["Il Decameron", "L'Orlando Furioso", "La Gerusalemme Liberata", "Il Cortegiano"],
        "risposta": "Il Decameron",
        "spiegazione": "Il Decameron è una raccolta di 100 novelle scritte da Boccaccio nel 1350."
    },
    {
        "domanda": "Chi ha scritto 'L'infinito'?",
        "opzioni": ["Giacomo Leopardi", "Alessandro Manzoni", "Giuseppe Ungaretti", "Eugenio Montale"],
        "risposta": "Giacomo Leopardi",
        "spiegazione": "'L'infinito' è uno dei più famosi idilli di Giacomo Leopardi (1819)."
    },
    {
        "domanda": "In quale città è ambientato 'I Promessi Sposi'?",
        "opzioni": ["Milano e Lecco", "Roma", "Firenze", "Venezia"],
        "risposta": "Milano e Lecco",
        "spiegazione": "La storia si svolge principalmente tra Lecco e Milano durante il XVII secolo."
    },
    {
        "domanda": "Chi ha scritto 'Se questo è un uomo'?",
        "opzioni": ["Primo Levi", "Italo Calvino", "Alberto Moravia", "Cesare Pavese"],
        "risposta": "Primo Levi",
        "spiegazione": "Primo Levi scrisse questo libro testimonianza sull'Olocausto nel 1947."
    },
    {
        "domanda": "Quale movimento letterario ha fondato Filippo Tommaso Marinetti?",
        "opzioni": ["Futurismo", "Ermetismo", "Neorealismo", "Decadentismo"],
        "risposta": "Futurismo",
        "spiegazione": "Marinetti pubblicò il Manifesto del Futurismo nel 1909."
    },
    {
        "domanda": "Chi è l'autore de 'Il nome della rosa'?",
        "opzioni": ["Umberto Eco", "Italo Calvino", "Leonardo Sciascia", "Andrea Camilleri"],
        "risposta": "Umberto Eco",
        "spiegazione": "'Il nome della rosa' fu pubblicato da Umberto Eco nel 1980."
    },
    {
        "domanda": "Completa: 'Nel mezzo del cammin di nostra vita...'",
        "opzioni": ["mi ritrovai per una selva oscura", "vidi una luce splendente", "incontrai il mio destino", "conobbi l'amore"],
        "risposta": "mi ritrovai per una selva oscura",
        "spiegazione": "È il celebre incipit della Divina Commedia di Dante."
    },
    {
        "domanda": "Chi ha scritto 'Le Myricae'?",
        "opzioni": ["Giovanni Pascoli", "Gabriele D'Annunzio", "Giosuè Carducci", "Giuseppe Ungaretti"],
        "risposta": "Giovanni Pascoli",
        "spiegazione": "'Myricae' è la prima raccolta poetica di Pascoli, pubblicata nel 1891."
    },
    {
        "domanda": "Quale scrittore italiano ha vinto il Premio Nobel nel 1997?",
        "opzioni": ["Dario Fo", "Italo Calvino", "Umberto Eco", "Alberto Moravia"],
        "risposta": "Dario Fo",
        "spiegazione": "Dario Fo vinse il Nobel per la Letteratura nel 1997."
    },
]


@app.route('/')
def index():
    """Homepage del quiz"""
    return render_template('index.html')


@app.route('/inizia')
def inizia():
    """Inizializza il quiz"""
    # Mescola le domande per ogni nuovo tentativo
    session['domande'] = random.sample(DOMANDE, len(DOMANDE))
    session['indice_corrente'] = 0
    session['punteggio'] = 0
    session['risposte'] = []  # Memorizza le risposte date

    return redirect(url_for('quiz'))


@app.route('/quiz')
def quiz():
    """Mostra la domanda corrente"""
    if 'domande' not in session:
        return redirect(url_for('index'))

    indice = session.get('indice_corrente', 0)
    domande = session.get('domande', [])

    # Se abbiamo finito le domande, vai ai risultati
    if indice >= len(domande):
        return redirect(url_for('risultati'))

    domanda_corrente = domande[indice]

    return render_template(
        'quiz.html',
        domanda=domanda_corrente,
        numero_domanda=indice + 1,
        totale_domande=len(domande)
    )


@app.route('/verifica', methods=['POST'])
def verifica():
    """Verifica la risposta e passa alla domanda successiva"""
    if 'domande' not in session:
        return redirect(url_for('index'))

    risposta_utente = request.form.get('risposta')
    indice = session.get('indice_corrente', 0)
    domande = session.get('domande', [])

    if indice < len(domande):
        domanda_corrente = domande[indice]
        risposta_corretta = domanda_corrente['risposta']

        # Verifica se la risposta è corretta
        corretta = (risposta_utente == risposta_corretta)

        if corretta:
            session['punteggio'] = session.get('punteggio', 0) + 1

        # Salva la risposta dell'utente
        if 'risposte' not in session:
            session['risposte'] = []

        session['risposte'].append({
            'domanda': domanda_corrente['domanda'],
            'risposta_utente': risposta_utente,
            'risposta_corretta': risposta_corretta,
            'corretta': corretta,
            'spiegazione': domanda_corrente.get('spiegazione', '')
        })

        # Passa alla domanda successiva
        session['indice_corrente'] = indice + 1

    return redirect(url_for('quiz'))


@app.route('/risultati')
def risultati():
    """Mostra i risultati finali"""
    if 'punteggio' not in session:
        return redirect(url_for('index'))

    punteggio = session.get('punteggio', 0)
    totale = len(session.get('domande', []))
    percentuale = (punteggio / totale * 100) if totale > 0 else 0
    risposte = session.get('risposte', [])

    # Determina il messaggio in base al punteggio
    if percentuale >= 90:
        messaggio = "Eccellente! Sei un vero esperto di letteratura italiana!"
    elif percentuale >= 70:
        messaggio = "Molto bene! Hai una buona conoscenza della letteratura italiana."
    elif percentuale >= 50:
        messaggio = "Discreto! C'è ancora spazio per migliorare."
    else:
        messaggio = "Continua a studiare! La letteratura italiana è affascinante."

    return render_template(
        'risultati.html',
        punteggio=punteggio,
        totale=totale,
        percentuale=percentuale,
        messaggio=messaggio,
        risposte=risposte
    )


@app.route('/reset')
def reset():
    """Resetta il quiz"""
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
