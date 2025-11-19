# Generatore di Racconti con AI (Gemini)
# Esercizio 6 - UDA Italiano + Informatica

import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import datetime


def carica_configurazione():
    """
    Carica la configurazione dell'API Gemini
    Returns:
        bool: True se la configurazione è riuscita
    """
    # TODO: Carica il file .env
    # TODO: Ottieni la API key
    # TODO: Configura genai
    pass


def crea_prompt(genere, lunghezza, nome, descrizione, ambientazione, tema, genera_titolo=False):
    """
    Crea un prompt per Gemini basato sui parametri
    Args:
        genere (str): Genere del racconto
        lunghezza (str): breve, media, lunga
        nome (str): Nome protagonista
        descrizione (str): Descrizione protagonista
        ambientazione (str): Dove/quando è ambientato
        tema (str): Tema centrale
        genera_titolo (bool): Se generare anche un titolo
    Returns:
        str: Il prompt costruito
    """
    # TODO: Costruisci un prompt efficace
    # Suggerimento: usa le f-string per inserire i parametri
    pass


def genera_racconto(prompt):
    """
    Chiama l'API di Gemini per generare il racconto
    Args:
        prompt (str): Il prompt da inviare
    Returns:
        str: Il racconto generato, o None in caso di errore
    """
    # TODO: Crea il modello
    # TODO: Genera il contenuto
    # TODO: Gestisci eventuali errori
    pass


def mostra_racconto(testo, titolo=None):
    """
    Mostra il racconto in modo formattato
    Args:
        testo (str): Il testo del racconto
        titolo (str): Titolo opzionale
    """
    # TODO: Stampa il racconto in modo bello
    pass


def salva_racconto(testo, titolo=None, cartella="racconti_ai"):
    """
    Salva il racconto in un file
    Args:
        testo (str): Il testo del racconto
        titolo (str): Titolo opzionale
        cartella (str): Cartella dove salvare
    Returns:
        str: Percorso del file salvato
    """
    # TODO: Crea la cartella se non esiste
    # TODO: Genera nome file con timestamp
    # TODO: Salva il contenuto
    pass


def menu_principale():
    """
    Gestisce il menu interattivo
    """
    # TODO: Implementa il menu per raccogliere i parametri dall'utente
    # - Genere
    # - Lunghezza
    # - Personaggio
    # - Ambientazione
    # - Tema
    pass


def main():
    """
    Funzione principale del programma
    """
    print("=== GENERATORE DI RACCONTI AI ===")
    print("🤖 Powered by Google Gemini\n")

    # TODO: Carica configurazione
    # TODO: Verifica che l'API key sia presente
    # TODO: Avvia il menu principale


if __name__ == "__main__":
    main()
