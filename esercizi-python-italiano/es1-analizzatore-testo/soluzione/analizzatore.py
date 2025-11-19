# Analizzatore di Testo - SOLUZIONE
# Esercizio 1 - UDA Italiano + Informatica

def conta_caratteri(testo):
    """
    Conta i caratteri totali e senza spazi
    Args:
        testo (str): Il testo da analizzare
    Returns:
        tuple: (caratteri_totali, caratteri_senza_spazi)
    """
    caratteri_totali = len(testo)
    caratteri_senza_spazi = len(testo.replace(" ", ""))
    return caratteri_totali, caratteri_senza_spazi


def conta_parole(testo):
    """
    Conta il numero di parole nel testo
    Args:
        testo (str): Il testo da analizzare
    Returns:
        int: Numero di parole
    """
    parole = testo.split()
    return len(parole)


def conta_frasi(testo):
    """
    Conta il numero di frasi (separate da . ! ?)
    Args:
        testo (str): Il testo da analizzare
    Returns:
        int: Numero di frasi
    """
    # Conta i separatori di frase
    contatore = 0
    separatori = ['.', '!', '?']

    for carattere in testo:
        if carattere in separatori:
            contatore += 1

    return contatore


def conta_vocali_consonanti(testo):
    """
    Conta vocali e consonanti nel testo
    Args:
        testo (str): Il testo da analizzare
    Returns:
        tuple: (vocali, consonanti)
    """
    vocali = "aeiouAEIOUàèéìòùÀÈÉÌÒÙ"
    contatore_vocali = 0
    contatore_consonanti = 0

    for carattere in testo:
        if carattere.isalpha():  # Solo lettere
            if carattere in vocali:
                contatore_vocali += 1
            else:
                contatore_consonanti += 1

    return contatore_vocali, contatore_consonanti


def trova_parola_piu_lunga_e_corta(testo):
    """
    Trova la parola più lunga e più corta
    Args:
        testo (str): Il testo da analizzare
    Returns:
        tuple: (parola_lunga, parola_corta)
    """
    # Rimuovi punteggiatura dalle parole
    import string
    parole = testo.split()
    parole_pulite = []

    for parola in parole:
        # Rimuovi punteggiatura
        parola_pulita = parola.strip(string.punctuation)
        if parola_pulita:  # Solo se non è vuota
            parole_pulite.append(parola_pulita)

    if not parole_pulite:
        return "", ""

    parola_lunga = max(parole_pulite, key=len)
    parola_corta = min(parole_pulite, key=len)

    return parola_lunga, parola_corta


def calcola_lunghezza_media(testo):
    """
    Calcola la lunghezza media delle parole
    Args:
        testo (str): Il testo da analizzare
    Returns:
        float: Lunghezza media
    """
    import string
    parole = testo.split()

    if not parole:
        return 0

    lunghezza_totale = 0
    for parola in parole:
        # Rimuovi punteggiatura
        parola_pulita = parola.strip(string.punctuation)
        lunghezza_totale += len(parola_pulita)

    return lunghezza_totale / len(parole)


def main():
    """
    Funzione principale del programma
    """
    print("=== ANALIZZATORE DI TESTO ===\n")

    # Chiedi all'utente di inserire il testo
    testo = input("Inserisci il testo da analizzare:\n> ")

    # Chiamata alle funzioni
    caratteri_totali, caratteri_senza_spazi = conta_caratteri(testo)
    num_parole = conta_parole(testo)
    num_frasi = conta_frasi(testo)
    num_vocali, num_consonanti = conta_vocali_consonanti(testo)
    parola_lunga, parola_corta = trova_parola_piu_lunga_e_corta(testo)
    lunghezza_media = calcola_lunghezza_media(testo)

    # Stampa i risultati
    print("\n--- STATISTICHE ---")
    print(f"Caratteri totali: {caratteri_totali}")
    print(f"Caratteri (senza spazi): {caratteri_senza_spazi}")
    print(f"Parole: {num_parole}")
    print(f"Frasi: {num_frasi}")
    print(f"Vocali: {num_vocali}")
    print(f"Consonanti: {num_consonanti}")
    print()
    print(f"Parola più lunga: {parola_lunga} ({len(parola_lunga)} lettere)")
    print(f"Parola più corta: {parola_corta} ({len(parola_corta)} lettere)")
    print(f"Lunghezza media parole: {lunghezza_media:.2f} lettere")


if __name__ == "__main__":
    main()
