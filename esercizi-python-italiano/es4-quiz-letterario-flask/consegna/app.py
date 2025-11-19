# Quiz Letterario Flask
# Esercizio 4 - UDA Italiano + Informatica

from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'chiave-segreta-quiz-letterario'  # Cambia in produzione!


# TODO: Aggiungi almeno 10 domande sulla letteratura italiana
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
    # Aggiungi altre domande...
]


@app.route('/')
def index():
    """
    Homepage del quiz
    """
    # TODO: Renderizza il template index.html
    pass


@app.route('/quiz')
def quiz():
    """
    Pagina con le domande del quiz
    """
    # TODO: Implementa la logica del quiz
    # - Inizializza sessione se nuova
    # - Mostra domanda corrente
    # - Gestisci punteggio
    pass


@app.route('/verifica', methods=['POST'])
def verifica():
    """
    Verifica la risposta data dall'utente
    """
    # TODO: Controlla se la risposta è corretta
    # - Aggiorna punteggio
    # - Passa alla domanda successiva
    pass


@app.route('/risultati')
def risultati():
    """
    Mostra i risultati finali
    """
    # TODO: Mostra punteggio finale
    pass


@app.route('/reset')
def reset():
    """
    Resetta il quiz
    """
    # TODO: Pulisci la sessione e riporta alla home
    pass


if __name__ == '__main__':
    app.run(debug=True)
