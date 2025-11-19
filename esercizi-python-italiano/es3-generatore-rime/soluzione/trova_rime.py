# Generatore di Rime - SOLUZIONE
# Esercizio 3 - UDA Italiano + Informatica


# Vocabolario di parole italiane organizzato per facilitare le rime
VOCABOLARIO = [
    # Parole in -ore
    "amore", "cuore", "fiore", "dolore", "colore", "calore", "splendore",
    "rumore", "sapore", "odore", "errore", "vigore",

    # Parole in -are
    "amare", "cantare", "sognare", "volare", "camminare", "ballare",
    "guardare", "parlare", "pensare", "creare", "nuotare",

    # Parole in -ello/a
    "bello", "castello", "fratello", "uccello", "coltello",
    "bella", "stella", "sorella", "pelle", "cappella",

    # Parole in -ino/a
    "bambino", "mattino", "vicino", "cammino", "destino", "giardino",
    "bambina", "mattina", "vicina", "collina", "marina",

    # Parole in -ento/a
    "vento", "momento", "argento", "talento", "tormento", "lento",
    "senta", "violenta", "lenta",

    # Parole in -ia
    "poesia", "magia", "allegria", "melodia", "nostalgia", "energia",
    "fantasia", "armonia", "malinconia",

    # Parole in -anza
    "speranza", "danza", "stanza", "anza", "lontananza", "costanza",

    # Parole in -ione
    "canzone", "stagione", "emozione", "passione", "razione", "azione",
    "stazione", "nazione", "tradizione",

    # Parole varie
    "cielo", "mare", "terra", "luna", "sole", "notte", "giorno",
    "vita", "morte", "tempo", "mondo", "pace", "guerra"
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
    return parola[-n_caratteri:].lower()


def trova_rime(parola, vocabolario, n_caratteri=3):
    """
    Trova tutte le parole nel vocabolario che rimano con la parola data
    Args:
        parola (str): La parola per cui cercare rime
        vocabolario (list): Lista di parole disponibili
        n_caratteri (int): Numero di caratteri del suffisso da confrontare
    Returns:
        list: Lista di parole che rimano (escludendo la parola stessa)
    """
    parola_lower = parola.lower()
    suffisso_cercato = estrai_suffisso(parola_lower, n_caratteri)

    rime = []
    for parola_voc in vocabolario:
        parola_voc_lower = parola_voc.lower()
        # Verifica se il suffisso corrisponde e non è la parola stessa
        if (estrai_suffisso(parola_voc_lower, n_caratteri) == suffisso_cercato
                and parola_voc_lower != parola_lower):
            rime.append(parola_voc)

    return sorted(rime)  # Ordina alfabeticamente


def mostra_rime(parola, rime, n_caratteri=3):
    """
    Mostra le rime trovate in modo formattato
    Args:
        parola (str): La parola originale
        rime (list): Lista di rime trovate
        n_caratteri (int): Numero di caratteri del suffisso
    """
    print(f"\n🔍 Ricerca rime per \"{parola}\"...\n")

    if not rime:
        print("❌ Nessuna rima trovata nel vocabolario.")
        print("   Prova con un'altra parola o aggiungi parole al vocabolario!\n")
        return

    print(f"✅ Rime trovate ({len(rime)}):")
    for rima in rime:
        print(f"  ✓ {rima}")

    suffisso = estrai_suffisso(parola, n_caratteri)
    print(f"\nTerminazione comune: -{suffisso}")
    print()


def aggiungi_parola(vocabolario):
    """
    Permette all'utente di aggiungere una nuova parola al vocabolario
    Args:
        vocabolario (list): Il vocabolario esistente
    """
    nuova_parola = input("\nInserisci la nuova parola da aggiungere: ").strip()

    if nuova_parola:
        if nuova_parola.lower() in [p.lower() for p in vocabolario]:
            print(f"⚠️  La parola '{nuova_parola}' è già nel vocabolario!")
        else:
            vocabolario.append(nuova_parola)
            print(f"✅ Parola '{nuova_parola}' aggiunta al vocabolario!")
    else:
        print("❌ Parola non valida.")


def salva_vocabolario(vocabolario, nome_file="vocabolario.txt"):
    """
    Salva il vocabolario in un file di testo
    Args:
        vocabolario (list): Lista di parole
        nome_file (str): Nome del file
    """
    with open(nome_file, "w", encoding="utf-8") as file:
        for parola in sorted(vocabolario):
            file.write(parola + "\n")
    print(f"✅ Vocabolario salvato in {nome_file}")


def main():
    """
    Funzione principale del programma
    """
    print("╔" + "═" * 40 + "╗")
    print("║" + " GENERATORE DI RIME ".center(40) + "║")
    print("╚" + "═" * 40 + "╝")
    print(f"\nVocabolario caricato: {len(VOCABOLARIO)} parole\n")

    vocabolario = VOCABOLARIO.copy()  # Copia per permettere modifiche

    while True:
        print("─" * 42)
        print("Opzioni:")
        print("  1. Cerca rime")
        print("  2. Aggiungi parola al vocabolario")
        print("  3. Salva vocabolario")
        print("  4. Esci")
        print("─" * 42)

        scelta = input("\nScegli un'opzione (1-4): ").strip()

        if scelta == "1":
            parola = input("\nInserisci una parola: ").strip()
            if parola:
                # Prova prima con 3 caratteri, poi con 2 se non trova nulla
                rime = trova_rime(parola, vocabolario, n_caratteri=3)
                if not rime:
                    # Prova con 2 caratteri per rime più generiche
                    rime = trova_rime(parola, vocabolario, n_caratteri=2)
                    mostra_rime(parola, rime, n_caratteri=2)
                else:
                    mostra_rime(parola, rime, n_caratteri=3)
            else:
                print("❌ Parola non valida.\n")

        elif scelta == "2":
            aggiungi_parola(vocabolario)

        elif scelta == "3":
            salva_vocabolario(vocabolario)

        elif scelta == "4":
            print("\n👋 Arrivederci, poeta!")
            print("   'Le parole sono ponti tra i cuori.' 📝\n")
            break

        else:
            print("❌ Opzione non valida. Riprova.\n")


if __name__ == "__main__":
    main()
