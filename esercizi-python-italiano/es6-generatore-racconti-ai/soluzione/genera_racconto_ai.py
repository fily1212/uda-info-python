# Generatore di Racconti con AI (Gemini) - SOLUZIONE
# Esercizio 6 - UDA Italiano + Informatica

import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import datetime


# Mappatura lunghezze in parole
LUNGHEZZE = {
    "breve": 300,
    "media": 600,
    "lunga": 1000
}

# Stili narrativi disponibili
STILI = {
    "1": "narratore onnisciente in terza persona",
    "2": "prima persona dal punto di vista del protagonista",
    "3": "stile epistolare (lettere/diario)",
    "4": "narratore inaffidabile",
}

# Toni disponibili
TONI = {
    "1": "serio e drammatico",
    "2": "leggero e ironico",
    "3": "poetico e lirico",
    "4": "noir e oscuro",
    "5": "avventuroso ed epico"
}


def carica_configurazione():
    """
    Carica la configurazione dell'API Gemini
    Returns:
        bool: True se la configurazione è riuscita
    """
    # Carica variabili d'ambiente dal file .env
    load_dotenv()

    # Ottieni la API key
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        print("❌ ERRORE: API key non trovata!")
        print("   Crea un file .env con: GEMINI_API_KEY=la_tua_chiave")
        print("   Ottieni una chiave gratuita da: https://makersuite.google.com/app/apikey")
        return False

    # Configura Gemini
    try:
        genai.configure(api_key=api_key)
        print("✅ Configurazione API completata\n")
        return True
    except Exception as e:
        print(f"❌ Errore nella configurazione: {e}")
        return False


def crea_prompt(genere, lunghezza, nome, descrizione, ambientazione, tema,
                stile="1", tono="1", genera_titolo=False):
    """
    Crea un prompt ottimizzato per Gemini
    """
    num_parole = LUNGHEZZE.get(lunghezza, 600)
    stile_narrativo = STILI.get(stile, STILI["1"])
    tono_racconto = TONI.get(tono, TONI["1"])

    if genera_titolo:
        prompt = f"""Sei un autore professionista di racconti in lingua italiana.

Genera un racconto completo con queste caratteristiche:

TITOLO: Genera un titolo accattivante e appropriato
GENERE: {genere}
LUNGHEZZA: circa {num_parole} parole
PROTAGONISTA: {nome}, {descrizione}
AMBIENTAZIONE: {ambientazione}
TEMA CENTRALE: {tema}
STILE NARRATIVO: {stile_narrativo}
TONO: {tono_racconto}

ISTRUZIONI:
- Struttura il racconto in tre atti (introduzione, sviluppo, conclusione)
- Includi dialoghi vivaci e realistici quando appropriato
- Usa un linguaggio ricco, descrittivo e letterario
- Sviluppa il tema in modo profondo e significativo
- Crea un finale soddisfacente ma non scontato
- Usa la punteggiatura italiana corretta

FORMATO OUTPUT:
TITOLO: [titolo del racconto]

[testo del racconto]

Inizia con "TITOLO:" seguito dal titolo, poi una riga vuota, poi il racconto.
Non aggiungere prefazioni o note dell'autore.
"""
    else:
        prompt = f"""Sei un autore professionista di racconti in lingua italiana.

Scrivi un racconto completo con queste caratteristiche:

GENERE: {genere}
LUNGHEZZA: circa {num_parole} parole
PROTAGONISTA: {nome}, {descrizione}
AMBIENTAZIONE: {ambientazione}
TEMA CENTRALE: {tema}
STILE NARRATIVO: {stile_narrativo}
TONO: {tono_racconto}

ISTRUZIONI:
- Struttura il racconto in tre atti (introduzione, sviluppo, conclusione)
- Includi dialoghi vivaci e realistici quando appropriato
- Usa un linguaggio ricco, descrittivo e letterario
- Sviluppa il tema in modo profondo e significativo
- Crea un finale soddisfacente ma non scontato
- Usa la punteggiatura italiana corretta

Inizia direttamente con il racconto, senza prefazioni o titoli.
"""

    return prompt


def genera_racconto(prompt, model_name='gemini-pro'):
    """
    Chiama l'API di Gemini per generare il racconto
    """
    try:
        print("✨ Connessione a Gemini...")
        model = genai.GenerativeModel(model_name)

        print("📝 Generazione del racconto in corso...")
        print("   (Questo potrebbe richiedere 10-30 secondi)\n")

        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.9,  # Più creativo
                top_p=0.95,
                top_k=40,
                max_output_tokens=2048,
            )
        )

        if response.text:
            return response.text
        else:
            print("⚠️ La risposta è vuota. Riprova.")
            return None

    except Exception as e:
        print(f"❌ Errore durante la generazione: {e}")
        print("\nPossibili cause:")
        print("  - API key non valida")
        print("  - Limite di richieste superato")
        print("  - Problemi di connessione")
        return None


def estrai_titolo_e_testo(testo_completo):
    """
    Estrae titolo e testo se presenti
    Returns:
        tuple: (titolo, testo) o (None, testo)
    """
    linee = testo_completo.strip().split('\n')

    # Cerca "TITOLO:" nelle prime righe
    for i, linea in enumerate(linee[:5]):
        if linea.startswith("TITOLO:"):
            titolo = linea.replace("TITOLO:", "").strip()
            # Il resto è il testo
            testo = '\n'.join(linee[i+1:]).strip()
            return titolo, testo

    # Nessun titolo trovato
    return None, testo_completo.strip()


def mostra_racconto(testo, titolo=None):
    """
    Mostra il racconto in modo formattato
    """
    larghezza = 70
    print()
    print("╔" + "═" * larghezza + "╗")

    if titolo:
        # Mostra il titolo
        print("║" + titolo.upper().center(larghezza) + "║")
        print("╠" + "═" * larghezza + "╣")

    print("║" + " " * larghezza + "║")

    # Dividi il testo in paragrafi
    paragrafi = testo.split('\n\n')

    for paragrafo in paragrafi:
        if not paragrafo.strip():
            continue

        # Dividi il paragrafo in parole
        parole = paragrafo.strip().split()
        riga_corrente = ""

        for parola in parole:
            # Verifica se aggiungere la parola supera la larghezza
            if len(riga_corrente) + len(parola) + 1 <= larghezza - 4:
                riga_corrente += parola + " "
            else:
                # Stampa la riga e inizia una nuova
                print("║  " + riga_corrente.ljust(larghezza - 4) + "  ║")
                riga_corrente = parola + " "

        # Stampa l'ultima riga del paragrafo
        if riga_corrente:
            print("║  " + riga_corrente.ljust(larghezza - 4) + "  ║")

        # Riga vuota tra paragrafi
        print("║" + " " * larghezza + "║")

    print("╚" + "═" * larghezza + "╝")
    print()


def salva_racconto(testo, titolo=None, genere="", cartella="racconti_ai"):
    """
    Salva il racconto in un file
    """
    # Crea la cartella se non esiste
    if not os.path.exists(cartella):
        os.makedirs(cartella)
        print(f"📁 Cartella '{cartella}/' creata")

    # Genera nome file con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_file = f"racconto_{timestamp}.txt"
    percorso = os.path.join(cartella, nome_file)

    # Scrivi il file
    with open(percorso, "w", encoding="utf-8") as file:
        file.write("=" * 70 + "\n")
        if titolo:
            file.write(titolo.upper().center(70) + "\n")
            file.write("=" * 70 + "\n\n")
        else:
            file.write(" RACCONTO GENERATO DA AI ".center(70) + "\n")
            file.write("=" * 70 + "\n\n")

        file.write(f"Generato il: {datetime.now().strftime('%d/%m/%Y alle %H:%M')}\n")
        if genere:
            file.write(f"Genere: {genere}\n")
        file.write(f"Generato da: Google Gemini AI\n")
        file.write("\n" + "-" * 70 + "\n\n")
        file.write(testo)
        file.write("\n\n" + "=" * 70 + "\n")

    print(f"✅ Racconto salvato in: {percorso}")
    return percorso


def menu_genere():
    """Menu per la selezione del genere"""
    print("\n📚 GENERE DEL RACCONTO\n")
    print("  1. 🔍 Mistero/Giallo")
    print("  2. 🗺️  Avventura")
    print("  3. ✨ Fantasy")
    print("  4. 💕 Romantico")
    print("  5. 🚀 Fantascienza")
    print("  6. 👻 Horror")
    print("  7. 📖 Realista/Drammatico")

    scelta = input("\nScegli (1-7): ").strip()

    generi = {
        "1": "mistero/giallo",
        "2": "avventura",
        "3": "fantasy",
        "4": "romantico",
        "5": "fantascienza",
        "6": "horror",
        "7": "realista"
    }

    return generi.get(scelta, "narrativa generale")


def menu_lunghezza():
    """Menu per la selezione della lunghezza"""
    print("\n📏 LUNGHEZZA DEL RACCONTO\n")
    print("  1. Breve (~300 parole, 2-3 minuti di lettura)")
    print("  2. Media (~600 parole, 4-5 minuti di lettura)")
    print("  3. Lunga (~1000 parole, 7-8 minuti di lettura)")

    scelta = input("\nScegli (1-3): ").strip()

    lunghezze = {
        "1": "breve",
        "2": "media",
        "3": "lunga"
    }

    return lunghezze.get(scelta, "media")


def menu_stile():
    """Menu per la selezione dello stile narrativo"""
    print("\n🎭 STILE NARRATIVO\n")
    for k, v in STILI.items():
        print(f"  {k}. {v.capitalize()}")

    scelta = input(f"\nScegli (1-{len(STILI)}): ").strip()
    return scelta if scelta in STILI else "1"


def menu_tono():
    """Menu per la selezione del tono"""
    print("\n🎨 TONO DEL RACCONTO\n")
    for k, v in TONI.items():
        print(f"  {k}. {v.capitalize()}")

    scelta = input(f"\nScegli (1-{len(TONI)}): ").strip()
    return scelta if scelta in TONI else "1"


def menu_principale():
    """
    Gestisce il menu interattivo
    """
    print("=" * 72)
    print(" CONFIGURAZIONE RACCONTO ".center(72, "="))
    print("=" * 72)

    # Raccolta parametri
    genere = menu_genere()
    lunghezza = menu_lunghezza()
    stile = menu_stile()
    tono = menu_tono()

    print("\n👤 PERSONAGGIO PRINCIPALE\n")
    nome = input("Nome del protagonista: ").strip() or "Alex"
    descrizione = input("Descrizione (es: giovane detective): ").strip() or "persona coraggiosa"

    print("\n🌍 AMBIENTAZIONE\n")
    ambientazione = input("Dove/quando (es: Italia contemporanea): ").strip() or "epoca contemporanea"

    print("\n💡 TEMA\n")
    tema = input("Tema centrale (es: la ricerca della verità): ").strip() or "il coraggio di cambiare"

    print("\n📝 OPZIONI AGGIUNTIVE\n")
    genera_titolo = input("Vuoi che l'AI generi anche un titolo? (s/n): ").lower().strip() == 's'

    # Riepilogo
    print("\n" + "─" * 72)
    print(" RIEPILOGO ".center(72, "─"))
    print("─" * 72)
    print(f"Genere: {genere}")
    print(f"Lunghezza: {lunghezza} (~{LUNGHEZZE[lunghezza]} parole)")
    print(f"Stile: {STILI[stile]}")
    print(f"Tono: {TONI[tono]}")
    print(f"Protagonista: {nome}, {descrizione}")
    print(f"Ambientazione: {ambientazione}")
    print(f"Tema: {tema}")
    print(f"Genera titolo: {'Sì' if genera_titolo else 'No'}")
    print("─" * 72)

    conferma = input("\n✅ Procedere con la generazione? (s/n): ").lower().strip()
    if conferma != 's':
        return None

    # Crea il prompt
    prompt = crea_prompt(genere, lunghezza, nome, descrizione,
                        ambientazione, tema, stile, tono, genera_titolo)

    # Genera il racconto
    testo_generato = genera_racconto(prompt)

    if testo_generato:
        # Estrai titolo se presente
        titolo, testo = estrai_titolo_e_testo(testo_generato)

        return {
            "testo": testo,
            "titolo": titolo,
            "genere": genere,
            "lunghezza": lunghezza
        }
    else:
        return None


def main():
    """
    Funzione principale del programma
    """
    print("╔" + "═" * 70 + "╗")
    print("║" + " GENERATORE DI RACCONTI AI ".center(70) + "║")
    print("║" + " Powered by Google Gemini ".center(70) + "║")
    print("╚" + "═" * 70 + "╝")
    print()

    # Carica configurazione
    if not carica_configurazione():
        return

    racconti_generati = 0

    while True:
        # Menu principale
        racconto = menu_principale()

        if racconto:
            # Mostra il racconto
            mostra_racconto(racconto["testo"], racconto["titolo"])
            racconti_generati += 1

            # Salva
            salva = input("💾 Vuoi salvare questo racconto? (s/n): ").lower().strip()
            if salva == 's':
                salva_racconto(
                    racconto["testo"],
                    racconto["titolo"],
                    racconto["genere"]
                )

        # Continua?
        print()
        continua = input("🔄 Vuoi generare un altro racconto? (s/n): ").lower().strip()
        if continua != 's':
            print(f"\n👋 Sessione terminata!")
            print(f"   Hai generato {racconti_generati} raccont{'o' if racconti_generati == 1 else 'i'}.")
            print("   'L'intelligenza artificiale amplifica la creatività umana.' 🤖✨\n")
            break


if __name__ == "__main__":
    main()
