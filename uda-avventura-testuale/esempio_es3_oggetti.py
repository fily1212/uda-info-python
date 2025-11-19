"""
ESEMPIO ESERCIZIO 3: OGGETTI OSSERVABILI E INTERATTIVI
=======================================================

Questo esempio mostra come creare oggetti con azioni multiple
e comportamenti personalizzati.

OBIETTIVI:
- Creare oggetti con descrizioni dettagliate
- Definire azioni custom oltre a quelle base
- Alcuni oggetti prendibili, altri fissi
- Oggetti che reagiscono a azioni specifiche

AZIONI DIMOSTRATE:
- osserva (legge la descrizione)
- prendi (se can_take=True)
- usa (azione custom)
- apri (azione custom)
- leggi (azione custom)
- tocca (azione custom)
"""

from text_adventure_engine import Game, Room, Item

# ============================================================================
# CREAZIONE DEL GIOCO
# ============================================================================

game = Game(
    title="Lo Studio dello Scienziato Pazzo",
    author="Esempio Es3",
    intro="""
    Sei un detective privato incaricato di investigare la scomparsa
    del Professor Aldebaran, un brillante ma eccentrico scienziato.
    Le autorità hanno trovato il suo laboratorio abbandonato da settimane.

    Entri nello studio polveroso, pieno di oggetti strani e misteriosi...
    """
)

# ============================================================================
# CREAZIONE STANZE
# ============================================================================

studio = Room(
    name="Studio del Professore",
    description="""
    Lo studio è in disordine totale. Scaffali stracolmi di libri,
    strumenti scientifici sparsi ovunque, carte ammucchiate sulla scrivania.
    L'aria sa di carta vecchia e sostanze chimiche.
    """,
    short_desc="Studio in disordine con libri e strumenti scientifici."
)

laboratorio = Room(
    name="Laboratorio",
    description="""
    Il laboratorio privato del professore. Tavoli ingombri di provette,
    becher e strani macchinari. Alcune sostanze emettono un debole bagliore.
    """,
    short_desc="Laboratorio con attrezzature scientifiche."
)

# ============================================================================
# CREAZIONE OGGETTI CON AZIONI CUSTOM
# ============================================================================

# --- OGGETTO 1: DIARIO ---
# Oggetto prendibile con azione "leggi"

diario = Item(
    name="diario",
    description="Un diario di pelle consumato, chiuso con un laccio. Sembra molto usato.",
    can_take=True,
    aliases=["libro", "taccuino", "quaderno"]
)

def leggi_diario(game, item):
    """Azione custom per leggere il diario."""
    return """
    Apri il diario e leggi l'ultima pagina scritta:

    "15 Marzo - L'esperimento sta dando risultati straordinari!
    La formula funziona, ma gli effetti collaterali sono preoccupanti.
    Devo nascondere le note nel CASSETTO SEGRETO prima che qualcuno
    le trovi. La combinazione è il mio anno di nascita: 1952."

    Il resto delle pagine è illeggibile, coperto di schizzi di inchiostro.
    """

diario.add_action("leggi", leggi_diario)
diario.add_action("usa", leggi_diario)  # "usa diario" fa la stessa cosa

# --- OGGETTO 2: SCRIVANIA ---
# Oggetto fisso (non prendibile) con azione "apri"

scrivania = Item(
    name="scrivania",
    description="""
    Una massiccia scrivania di mogano, coperta di carte, libri aperti
    e strani strumenti. Ha tre cassetti. Quello centrale sembra avere
    un meccanismo di chiusura particolare.
    """,
    can_take=False,
    aliases=["tavolo", "desk"]
)

# Proprietà custom per gestire lo stato
scrivania.set_property("cassetto_aperto", False)

def apri_scrivania(game, item):
    """Azione per aprire il cassetto segreto."""
    if item.get_property("cassetto_aperto"):
        return "Il cassetto segreto è già aperto."

    # Controlla se il giocatore ha letto il diario
    if "anno_scoperto" in game.state and game.state["anno_scoperto"]:
        item.set_property("cassetto_aperto", True)
        # Crea e aggiungi la chiave alla stanza
        chiave = Item(
            name="chiave",
            description="Una piccola chiave di ottone con inciso '42'.",
            can_take=True,
            aliases=["chiavetta"]
        )
        game.current_room.add_item(chiave)
        return """
        Ricordando l'annotazione del diario, provi con la combinazione 1952.
        Click! Il cassetto si apre rivelando una piccola chiave di ottone.
        """
    else:
        return """
        Il cassetto centrale ha una serratura a combinazione numerica.
        Ti servono quattro cifre, ma quali?
        """

scrivania.add_action("apri", apri_scrivania)
scrivania.add_action("usa", apri_scrivania)

# --- OGGETTO 3: LAMPADA ---
# Oggetto prendibile con azione speciale

lampada = Item(
    name="lampada",
    description="""
    Una lampada ad olio antiquata, ancora funzionante. La luce tremolante
    proietta ombre danzanti sulle pareti.
    """,
    can_take=True,
    aliases=["lanterna", "luce"]
)

lampada.set_property("accesa", True)

def usa_lampada(game, item):
    """Accendi/spegni la lampada."""
    accesa = item.get_property("accesa")
    if accesa:
        item.set_property("accesa", False)
        return "Spegni la lampada. L'oscurità ti avvolge."
    else:
        item.set_property("accesa", True)
        return "Accendi la lampada. La luce tremolante torna a illuminare la stanza."

lampada.add_action("usa", usa_lampada)

# --- OGGETTO 4: QUADRO ---
# Oggetto fisso che nasconde qualcosa

quadro = Item(
    name="quadro",
    description="""
    Un ritratto a olio del Professor Aldebaran in gioventù. Ti fissa
    con occhi penetranti. Sembra leggermente storto sulla parete.
    """,
    can_take=False,
    aliases=["ritratto", "dipinto", "pittura"]
)

quadro.set_property("spostato", False)

def tocca_quadro(game, item):
    """Sposta il quadro e rivela una cassaforte."""
    if item.get_property("spostato"):
        return "Il quadro è già spostato, rivelando la cassaforte."

    item.set_property("spostato", True)
    # Aggiungi cassaforte alla stanza
    cassaforte = Item(
        name="cassaforte",
        description="""
        Una piccola cassaforte a muro. Ha una serratura a chiave.
        Il numero '42' è inciso sul frontale.
        """,
        can_take=False,
        aliases=["safe", "casseforte"]
    )

    def apri_cassaforte(game_ref, cassa):
        # Controlla se il giocatore ha la chiave
        chiave = game_ref.find_item_in_inventory("chiave")
        if chiave:
            game_ref.game_won = True
            return """
            Usi la chiave con il numero 42. La cassaforte si apre!

            All'interno trovi un fascicolo con la scritta "PROGETTO FENIX - TOP SECRET".
            Documenti che descrivono un esperimento pericoloso...

            Hai trovato le prove della scomparsa del professore!
            Missione completata!
            """
        else:
            return "La cassaforte è chiusa a chiave. Ti serve la chiave giusta."

    cassaforte.add_action("apri", apri_cassaforte)
    cassaforte.add_action("usa", apri_cassaforte)

    game.current_room.add_item(cassaforte)
    return """
    Sposti il quadro scoprendo... una cassaforte nascosta nella parete!
    Il quadro ora pende storto al lato.
    """

quadro.add_action("tocca", tocca_quadro)
quadro.add_action("spingi", tocca_quadro)
quadro.add_action("usa", tocca_quadro)

# --- OGGETTO 5: PROVETTE ---
# Oggetto osservabile ma pericoloso da prendere

provette = Item(
    name="provette",
    description="""
    Un set di provette contenenti liquidi colorati: blu elettrico,
    verde fosforescente, rosso sangue. Alcune bollono leggermente
    anche senza fonte di calore.
    """,
    can_take=False,  # Troppo pericolose!
    aliases=["provetta", "fiale", "liquidi"]
)

def prendi_provette(game, item):
    """Messaggio custom quando provi a prenderle."""
    return """
    Stai per afferrare le provette quando noti dei simboli di pericolo
    sulle etichette. Meglio non toccare sostanze chimiche sconosciute!
    """

# Sovrascriviamo il messaggio di default
provette.can_take = False

# --- OGGETTO 6: MICROSCOPIO ---
# Oggetto osservabile con dettagli

microscopio = Item(
    name="microscopio",
    description="""
    Un microscopio ottico professionale di ottima qualità. C'è ancora
    un vetrino posizionato sotto l'obiettivo.
    """,
    can_take=False,
    aliases=["vetrino"]
)

def usa_microscopio(game, item):
    """Guarda nel microscopio."""
    return """
    Guardi attraverso il microscopio. Sul vetrino vedi cellule strane,
    di forma irregolare, che sembrano muoversi anche se dovrebbero
    essere morte. Alcune hanno tentacoli microscopici.

    Cosa stava studiando il professore?!
    """

microscopio.add_action("usa", usa_microscopio)
microscopio.add_action("osserva", usa_microscopio)

# ============================================================================
# SETUP STANZE E OGGETTI
# ============================================================================

# Aggiungi oggetti allo studio
studio.add_item(diario)
studio.add_item(scrivania)
studio.add_item(lampada)
studio.add_item(quadro)

# Aggiungi oggetti al laboratorio
laboratorio.add_item(provette)
laboratorio.add_item(microscopio)

# Setup gioco
game.add_room("studio", studio)
game.add_room("laboratorio", laboratorio)
game.connect_rooms("studio", "nord", "laboratorio", bidirectional=True)
game.set_start("studio")

# ============================================================================
# CALLBACK PER MARCARE CHE IL DIARIO È STATO LETTO
# ============================================================================

def on_read_diary_callback(game_obj, item):
    """Quando leggi il diario, segna che hai scoperto l'anno."""
    game.state["anno_scoperto"] = True

diario.actions["leggi"] = on_read_diary_callback.__get__(diario, Item)

# Redefiniamo per includere il set dello stato
def leggi_diario_v2(game, item):
    game.state["anno_scoperto"] = True
    return """
    Apri il diario e leggi l'ultima pagina scritta:

    "15 Marzo - L'esperimento sta dando risultati straordinari!
    La formula funziona, ma gli effetti collaterali sono preoccupanti.
    Devo nascondere le note nel CASSETTO SEGRETO prima che qualcuno
    le trovi. La combinazione è il mio anno di nascita: 1952."

    Il resto delle pagine è illeggibile, coperto di schizzi di inchiostro.
    """

diario.add_action("leggi", leggi_diario_v2)
diario.add_action("usa", leggi_diario_v2)

# ============================================================================
# AVVIO
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("ESEMPIO ESERCIZIO 3: OGGETTI OSSERVABILI E INTERATTIVI")
    print("="*70)
    print("\nQuesta avventura mostra diversi tipi di oggetti:")
    print("- Oggetti prendibili e fissi")
    print("- Azioni custom (leggi, apri, tocca, usa)")
    print("- Oggetti che rivelano altri oggetti")
    print("- Stati degli oggetti (aperto/chiuso, acceso/spento)")
    print("\nOBIETTIVO: Scopri cosa è successo al professore!")
    print("\nSUGGERIMENTO PUZZLE:")
    print("1. Leggi il diario")
    print("2. Apri il cassetto segreto")
    print("3. Sposta il quadro")
    print("4. Apri la cassaforte")
    print("="*70 + "\n")

    game.start()
