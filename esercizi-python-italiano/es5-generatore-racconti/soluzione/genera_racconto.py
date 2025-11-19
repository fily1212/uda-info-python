# Generatore di Racconti - SOLUZIONE
# Esercizio 5 - UDA Italiano + Informatica

import random
import os
from datetime import datetime


# Database di personaggi
PERSONAGGI = [
    {"nome": "Marco", "tipo": "giovane studente", "caratteristica": "curioso e coraggioso"},
    {"nome": "Sofia", "tipo": "detective", "caratteristica": "intelligente e astuta"},
    {"nome": "Leonardo", "tipo": "artista", "caratteristica": "creativo e sognatore"},
    {"nome": "Giulia", "tipo": "scienziata", "caratteristica": "razionale e determinata"},
    {"nome": "Alessandro", "tipo": "cavaliere", "caratteristica": "valoroso e leale"},
    {"nome": "Chiara", "tipo": "maga", "caratteristica": "saggia e misteriosa"},
    {"nome": "Matteo", "tipo": "giornalista", "caratteristica": "curioso e tenace"},
    {"nome": "Elena", "tipo": "archeologa", "caratteristica": "avventurosa e colta"},
    {"nome": "Francesco", "tipo": "musicista", "caratteristica": "sensibile e appassionato"},
    {"nome": "Anna", "tipo": "professoressa", "caratteristica": "paziente e perspicace"},
]

# Database di luoghi
LUOGHI = [
    {"dove": "in una biblioteca antica", "quando": "al tramonto"},
    {"dove": "in una foresta oscura", "quando": "a mezzanotte"},
    {"dove": "in un castello abbandonato", "quando": "durante un temporale"},
    {"dove": "in una piccola città di mare", "quando": "all'alba"},
    {"dove": "in un laboratorio segreto", "quando": "nel cuore della notte"},
    {"dove": "in un mercato orientale", "quando": "sotto il sole cocente"},
    {"dove": "in una villa misteriosa", "quando": "durante una festa"},
    {"dove": "nelle profondità di una grotta", "quando": "all'imbrunire"},
    {"dove": "in una vecchia stazione ferroviaria", "quando": "in una fredda sera d'inverno"},
    {"dove": "in un giardino incantato", "quando": "sotto la luna piena"},
]

# Database di conflitti per genere
CONFLITTI = {
    "mistero": [
        "scoprì un libro antico con simboli incomprensibili che sembravano nascondere un segreto",
        "trovò una serie di lettere che rivelavano un complotto dimenticato da tempo",
        "si imbatté in strani eventi che non avevano spiegazione razionale",
        "venne a conoscenza di un crimine che tutti credevano risolto, ma che nascondeva la verità",
        "notò strani comportamenti in persone che conosceva da sempre",
        "ricevette un messaggio anonimo che la condusse su una pista inaspettata",
    ],
    "avventura": [
        "trovò una mappa che indicava la posizione di un tesoro leggendario",
        "dovette intraprendere un viaggio pericoloso per salvare qualcuno che amava",
        "scoprì l'esistenza di un mondo nascosto che nessuno conosceva",
        "fu coinvolto in una missione importante che avrebbe cambiato molte vite",
        "si ritrovò a dover attraversare terre inesplorate per completare una missione",
        "scoprì di possedere un talento speciale che lo rese protagonista di grandi imprese",
    ],
    "fantasy": [
        "scoprì di avere poteri magici che non sapeva di possedere",
        "trovò un artefatto antico che conteneva una magia dimenticata",
        "venne scelto da una profezia per compiere una grande impresa",
        "incontrò una creatura magica che gli chiese aiuto",
        "dovette affrontare una maledizione che minacciava il regno",
        "scoprì di essere l'erede di una stirpe di maghi potenti",
    ],
    "romantico": [
        "incontrò una persona speciale che cambiò la sua vita per sempre",
        "ritrovò un amore perduto dopo molti anni di separazione",
        "dovette scegliere tra due amori, entrambi importanti",
        "scoprì che l'amore può nascere nei momenti più inaspettati",
        "scrisse lettere d'amore che non ebbe mai il coraggio di spedire",
        "si innamorò della persona meno adatta, creando una situazione complicata",
    ],
}

# Database di sviluppi narrativi
SVILUPPI = [
    "Con coraggio e determinazione, {pronome} iniziò a indagare più a fondo",
    "Dopo molte difficoltà e ostacoli apparentemente insuperabili, {pronome} non si arrese",
    "Grazie alla {sua_caratteristica}, {pronome} riuscì a fare progressi significativi",
    "Nonostante i dubbi e le paure, {pronome} decise di andare avanti",
    "Con l'aiuto di nuovi alleati inaspettati, {pronome} proseguì nella {sua_missione}",
    "Affrontando pericoli e sfide, {pronome} scoprì qualcosa di importante su {se_stesso}",
]

EVENTI_INTERMEDI = [
    "Lungo il percorso, incontrò persone che cambiarono la sua prospettiva",
    "Durante il viaggio, scoprì indizi che lo condussero sempre più vicino alla verità",
    "Nel corso delle sue ricerche, fece scoperte sorprendenti",
    "Mentre procedeva, si rese conto che la situazione era più complessa di quanto pensasse",
    "Attraversando momenti di dubbio, trovò la forza di continuare",
]

# Database di conclusioni
CONCLUSIONI = [
    "Alla fine, tutto si risolse nel migliore dei modi e {pronome} poté finalmente trovare pace",
    "La verità venne finalmente a galla, rivelando un finale inaspettato ma soddisfacente",
    "Dopo tante peripezie, {pronome} raggiunse il {suo_obiettivo} e ne uscì trasformato",
    "Il viaggio si concluse, ma {pronome} aveva imparato lezioni preziose che avrebbe portato con sé per sempre",
    "Quando tutto sembrò perduto, una soluzione inaspettata portò a un lieto fine",
    "Con saggezza acquisita dall'esperienza, {pronome} risolse la situazione in modo brillante",
]

MORALI = [
    "A volte, il coraggio di cercare la verità è la più grande vittoria",
    "Le avventure più grandi iniziano con un piccolo passo",
    "Non tutto ciò che brilla è oro, ma ogni esperienza ha un valore",
    "Il vero tesoro non è ciò che troviamo, ma ciò che diventiamo cercandolo",
    "Ogni fine è un nuovo inizio",
]

# Titoli per genere
TITOLI_INIZIO = {
    "mistero": ["Il Segreto", "L'Enigma", "Il Mistero", "Il Caso", "L'Ombra"],
    "avventura": ["La Ricerca", "Il Viaggio", "L'Impresa", "La Scoperta", "L'Avventura"],
    "fantasy": ["La Magia", "L'Incantesimo", "La Profezia", "Il Sortilegio", "Il Regno"],
    "romantico": ["L'Amore", "Il Destino", "Il Cuore", "I Sentimenti", "La Storia"],
}

TITOLI_FINE = {
    "mistero": ["Perduto", "Nascosto", "Dimenticato", "Sepolto", "Celato"],
    "avventura": ["Leggendario", "Impossibile", "Epico", "Incredibile", "Straordinario"],
    "fantasy": ["Incantato", "Magico", "Fatato", "Mistico", "Arcano"],
    "romantico": ["Eterno", "Impossibile", "Proibito", "Perfetto", "Sincero"],
}


def ottieni_pronome(genere_grammaticale):
    """Restituisce il pronome in base al genere"""
    return "egli" if genere_grammaticale == "M" else "ella"


def ottieni_articolo_possessivo(genere_grammaticale):
    """Restituisce gli articoli possessivi"""
    return {
        "sua": "sua" if genere_grammaticale == "F" else "suo",
        "la_sua": "la sua" if genere_grammaticale == "F" else "il suo",
    }


def genera_titolo(genere):
    """Genera un titolo casuale per il racconto"""
    if genere in TITOLI_INIZIO:
        inizio = random.choice(TITOLI_INIZIO[genere])
        fine = random.choice(TITOLI_FINE[genere])
        return f"{inizio} {fine}"
    else:
        # Titolo generico
        parole = ["Storia", "Racconto", "Avventura", "Destino", "Viaggio"]
        aggettivi = ["Straordinario", "Misterioso", "Incredibile", "Inaspettato", "Magico"]
        return f"{random.choice(parole)} {random.choice(aggettivi)}"


def genera_racconto(genere="casuale"):
    """Genera un racconto completo"""

    # Determina il genere effettivo
    generi_disponibili = list(CONFLITTI.keys())
    if genere == "casuale" or genere not in generi_disponibili:
        genere = random.choice(generi_disponibili)

    # Seleziona elementi casuali
    personaggio = random.choice(PERSONAGGI)
    luogo = random.choice(LUOGHI)
    conflitto = random.choice(CONFLITTI[genere])
    sviluppo = random.choice(SVILUPPI)
    evento = random.choice(EVENTI_INTERMEDI)
    conclusione = random.choice(CONCLUSIONI)
    morale = random.choice(MORALI)

    # Determina il genere grammaticale dal nome
    nomi_femminili = ["Sofia", "Giulia", "Chiara", "Elena", "Anna"]
    genere_grammaticale = "F" if personaggio["nome"] in nomi_femminili else "M"

    # Pronomi e possessivi
    pronome = ottieni_pronome(genere_grammaticale)
    possessivi = ottieni_articolo_possessivo(genere_grammaticale)

    # Sostituzioni per rendere il testo coerente
    sviluppo = sviluppo.format(
        pronome=pronome,
        sua_caratteristica=possessivi["sua"] + " " + personaggio["caratteristica"],
        sua_missione=possessivi["la_sua"] + " missione",
    )

    conclusione = conclusione.format(
        pronome=pronome,
        suo_obiettivo=possessivi["la_sua"] + " obiettivo",
    )

    # Costruisce il racconto
    testo = f"""C'era una volta {personaggio['nome']}, {personaggio['tipo']} {personaggio['caratteristica']}.

Un giorno, {luogo['dove']} {luogo['quando']}, {personaggio['nome']} {conflitto}.

{sviluppo}. {evento}.

{conclusione}.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💭 Morale: {morale}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    titolo = genera_titolo(genere)

    return {
        "titolo": titolo,
        "testo": testo,
        "genere": genere,
        "personaggio": personaggio["nome"],
    }


def mostra_racconto(racconto):
    """Mostra il racconto in modo formattato"""
    larghezza = 60
    print()
    print("╔" + "═" * larghezza + "╗")
    print("║" + racconto["titolo"].upper().center(larghezza) + "║")
    print("╠" + "═" * larghezza + "╣")
    print("║" + f"Genere: {racconto['genere'].capitalize()}".center(larghezza) + "║")
    print("╠" + "═" * larghezza + "╣")
    print("║" + " " * larghezza + "║")

    # Dividi il testo in righe
    for linea in racconto["testo"].split("\n"):
        if len(linea) <= larghezza - 4:
            print("║  " + linea.ljust(larghezza - 4) + "  ║")
        else:
            # Spezza le righe lunghe
            parole = linea.split()
            riga_corrente = ""
            for parola in parole:
                if len(riga_corrente) + len(parola) + 1 <= larghezza - 4:
                    riga_corrente += parola + " "
                else:
                    print("║  " + riga_corrente.ljust(larghezza - 4) + "  ║")
                    riga_corrente = parola + " "
            if riga_corrente:
                print("║  " + riga_corrente.ljust(larghezza - 4) + "  ║")

    print("║" + " " * larghezza + "║")
    print("╚" + "═" * larghezza + "╝")
    print()


def salva_racconto(racconto, cartella="racconti"):
    """Salva il racconto in un file di testo"""

    # Crea la cartella se non esiste
    if not os.path.exists(cartella):
        os.makedirs(cartella)

    # Genera un nome file unico con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_file = f"racconto_{timestamp}.txt"
    percorso = os.path.join(cartella, nome_file)

    # Salva il racconto
    with open(percorso, "w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write(racconto["titolo"].upper().center(60) + "\n")
        file.write("=" * 60 + "\n\n")
        file.write(f"Genere: {racconto['genere'].capitalize()}\n")
        file.write(f"Personaggio principale: {racconto['personaggio']}\n")
        file.write(f"Data di creazione: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        file.write("-" * 60 + "\n\n")
        file.write(racconto["testo"])
        file.write("\n\n" + "=" * 60 + "\n")

    print(f"✅ Racconto salvato in: {percorso}")
    return percorso


def menu_genere():
    """Mostra il menu per la selezione del genere"""
    print("\n📚 Scegli il genere del racconto:\n")
    print("  1. 🔍 Mistero")
    print("  2. 🗺️  Avventura")
    print("  3. ✨ Fantasy")
    print("  4. 💕 Romantico")
    print("  5. 🎲 Casuale (sorpresa!)")
    print()

    scelta = input("Inserisci il numero (1-5): ").strip()

    mapping = {
        "1": "mistero",
        "2": "avventura",
        "3": "fantasy",
        "4": "romantico",
        "5": "casuale",
    }

    return mapping.get(scelta, "casuale")


def main():
    """Funzione principale del programma"""
    print("╔" + "═" * 58 + "╗")
    print("║" + " GENERATORE DI RACCONTI ".center(58) + "║")
    print("║" + " Crea storie uniche con un click! ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")

    racconti_generati = 0

    while True:
        # Selezione genere
        genere = menu_genere()

        # Genera il racconto
        print("\n✍️  Generazione del racconto in corso...\n")
        racconto = genera_racconto(genere)

        # Mostra il racconto
        mostra_racconto(racconto)
        racconti_generati += 1

        # Chiedi se salvare
        salva = input("💾 Vuoi salvare questo racconto? (s/n): ").lower().strip()
        if salva == "s":
            salva_racconto(racconto)

        # Chiedi se continuare
        print()
        continua = input("📖 Vuoi generare un altro racconto? (s/n): ").lower().strip()
        if continua != "s":
            print(f"\n👋 Grazie per aver usato il Generatore di Racconti!")
            print(f"   Hai generato {racconti_generati} raccont{'o' if racconti_generati == 1 else 'i'}.")
            print("   'Ogni storia è un viaggio, ogni viaggio è una storia.' ✨\n")
            break


if __name__ == "__main__":
    main()
