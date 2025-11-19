# Generatore di Rime
# Esercizio 3 - UDA Italiano + Informatica


# TODO: Crea un vocabolario con almeno 50 parole italiane
# Organizza le parole per facilitare la ricerca delle rime
VOCABOLARIO = [
    "amore",
    "cuore",
    "fiore",
    # Aggiungi almeno altre 47 parole...
]


def estrai_suffisso(parola, n_caratteri=3):
    """
    Estrae gli ultimi n caratteri di una parola (il suffisso)
    Args:
        parola (str): La parola da cui estrarre il suffisso
        n_caratteri (int): Numero di caratteri da estrarre
    Returns:
        str: Il suffisso in minuscolo
    """
    # TODO: Implementa questa funzione
    pass


def trova_rime(parola, vocabolario, n_caratteri=3):
    """
    Trova tutte le parole nel vocabolario che rimano con la parola data
    Args:
        parola (str): La parola per cui cercare rime
        vocabolario (list): Lista di parole disponibili
        n_caratteri (int): Numero di caratteri del suffisso da confrontare
    Returns:
        list: Lista di parole che rimano
    """
    # TODO: Implementa la logica per trovare le rime
    # Suggerimento: confronta i suffissi delle parole
    pass


def mostra_rime(parola, rime):
    """
    Mostra le rime trovate in modo formattato
    Args:
        parola (str): La parola originale
        rime (list): Lista di rime trovate
    """
    # TODO: Stampa le rime in modo chiaro
    pass


def main():
    """
    Funzione principale del programma
    """
    print("=== GENERATORE DI RIME ===\n")
    print(f"Vocabolario caricato: {len(VOCABOLARIO)} parole\n")

    # TODO: Implementa il loop principale
    # - Chiedi all'utente una parola
    # - Trova e mostra le rime
    # - Chiedi se vuole continuare


if __name__ == "__main__":
    main()
