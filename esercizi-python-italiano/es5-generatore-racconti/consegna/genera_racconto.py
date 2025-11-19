# Generatore di Racconti
# Esercizio 5 - UDA Italiano + Informatica

import random
import os


# TODO: Completa i database con almeno 5 elementi per categoria

PERSONAGGI = [
    {"nome": "Marco", "tipo": "giovane studente", "caratteristica": "curioso"},
    {"nome": "Sofia", "tipo": "detective", "caratteristica": "intelligente"},
    # Aggiungi altri personaggi...
]

LUOGHI = [
    {"dove": "in una biblioteca antica", "quando": "al tramonto"},
    {"dove": "in una foresta oscura", "quando": "a mezzanotte"},
    # Aggiungi altri luoghi...
]

CONFLITTI = {
    "mistero": [
        "scoprì un libro misterioso con simboli strani",
        # Aggiungi altri conflitti per il genere mistero...
    ],
    "avventura": [
        "trovò una mappa di un tesoro nascosto",
        # Aggiungi altri conflitti per il genere avventura...
    ],
    # Aggiungi altri generi...
}

SVILUPPI = [
    "Con coraggio e determinazione",
    "Dopo molte difficoltà",
    # Aggiungi altri sviluppi...
]

CONCLUSIONI = [
    "tutto si risolse nel migliore dei modi",
    "la verità venne finalmente a galla",
    # Aggiungi altre conclusioni...
]


def genera_titolo():
    """
    Genera un titolo casuale per il racconto
    Returns:
        str: Il titolo generato
    """
    # TODO: Implementa la generazione del titolo
    pass


def genera_racconto(genere="casuale"):
    """
    Genera un racconto completo
    Args:
        genere (str): Il genere del racconto
    Returns:
        dict: Dizionario con titolo e testo del racconto
    """
    # TODO: Implementa la logica di generazione
    # - Seleziona elementi casuali
    # - Combina gli elementi in un racconto coerente
    # - Restituisci titolo e testo
    pass


def mostra_racconto(racconto):
    """
    Mostra il racconto in modo formattato
    Args:
        racconto (dict): Dizionario con titolo e testo
    """
    # TODO: Stampa il racconto in modo bello
    pass


def salva_racconto(racconto, cartella="racconti"):
    """
    Salva il racconto in un file di testo
    Args:
        racconto (dict): Dizionario con titolo e testo
        cartella (str): Nome della cartella dove salvare
    """
    # TODO: Implementa il salvataggio
    # - Crea la cartella se non esiste
    # - Genera un nome file progressivo
    # - Salva il racconto
    pass


def main():
    """
    Funzione principale del programma
    """
    print("=== GENERATORE DI RACCONTI ===\n")

    # TODO: Implementa il menu e il loop principale
    # - Mostra opzioni di genere
    # - Genera racconto
    # - Chiedi se salvare
    # - Chiedi se continuare


if __name__ == "__main__":
    main()
