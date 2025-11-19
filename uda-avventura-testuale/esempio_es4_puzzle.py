"""
ESEMPIO ESERCIZIO 4: PUZZLE ED EVENTI
======================================

Questo esempio mostra come creare puzzle logici integrati nella narrazione
e un sistema di eventi che modificano il mondo di gioco.

OBIETTIVI:
- Progettare puzzle logici e creativi
- Implementare eventi che cambiano lo stato del gioco
- Usare callback on_enter/on_exit per eventi automatici
- Gestire flag e condizioni complesse

PUZZLE DIMOSTRATI:
1. Puzzle delle statue (logica e osservazione)
2. Puzzle della combinazione (indizi sparsi)
3. Evento temporale (dopo N turni succede qualcosa)
"""

from text_adventure_engine import Game, Room, Item, NPC

# ============================================================================
# CREAZIONE GIOCO
# ============================================================================

game = Game(
    title="Il Tempio delle Quattro Stagioni",
    author="Esempio Es4",
    intro="""
    Sei un archeologo che ha appena scoperto l'ingresso di un antico
    tempio perduto. Secondo le leggende, il tempio custodisce un tesoro
    inestimabile, ma è protetto da enigmi creati dai saggi antichi.

    Solo chi comprende il ciclo delle stagioni potrà accedere alla
    camera del tesoro...
    """
)

# ============================================================================
# STANZE
# ============================================================================

ingresso = Room(
    name="Ingresso del Tempio",
    description="""
    Entri in una sala circolare illuminata da una luce misteriosa che
    sembra provenire dalle pareti stesse. Al centro c'è un altare di
    pietra con incisa un'iscrizione. Quattro porte si aprono nelle
    direzioni cardinali, ciascuna decorata con simboli diversi.
    """,
    short_desc="Sala circolare con altare centrale e quattro porte."
)

sala_primavera = Room(
    name="Sala della Primavera",
    description="""
    Questa sala è decorata con motivi floreali. Fiori di pietra
    sbocciano dalle pareti. Al centro c'è una statua di donna che
    tiene un seme nella mano tesa.
    """,
    short_desc="Sala decorata con fiori. Statua di donna con seme."
)

sala_estate = Room(
    name="Sala dell'Estate",
    description="""
    Il calore sembra emanare dalle pareti dorate di questa sala.
    Simboli di sole decorano il soffitto. Una statua di guerriero
    tiene in alto una spada fiammeggiante.
    """,
    short_desc="Sala calda e dorata. Statua di guerriero con spada."
)

sala_autunno = Room(
    name="Sala dell'Autunno",
    description="""
    Foglie dorate di metallo pendono dal soffitto, tintinnando
    lievemente. Una statua di anziano saggio tiene un libro aperto.
    """,
    short_desc="Sala con foglie metalliche. Statua di saggio con libro."
)

sala_inverno = Room(
    name="Sala dell'Inverno",
    description="""
    L'aria qui è gelida. Cristalli di ghiaccio decorano le pareti.
    Una statua di vecchio incappucciato tiene un bastone nodoso.
    """,
    short_desc="Sala gelida con cristalli. Statua di vecchio con bastone."
)

sala_tesoro = Room(
    name="Camera del Tesoro",
    description="""
    La camera del tesoro! Le pareti sono coperte d'oro e gemme.
    Al centro, su un piedistallo, brilla la Corona delle Stagioni,
    il leggendario artefatto che hai cercato!
    """,
    short_desc="Camera del tesoro con la Corona delle Stagioni!"
)

# ============================================================================
# OGGETTI E PUZZLE
# ============================================================================

# --- ALTARE CENTRALE CON INDIZIO ---
altare = Item(
    name="altare",
    description="""
    L'altare ha quattro fessure disposte in cerchio, ciascuna con
    un simbolo stagionale: un germoglio, un sole, una foglia, un fiocco
    di neve. Sotto, un'iscrizione recita:

    "Il ciclo è eterno: dalla rinascita alla crescita,
     dalla maturità al riposo, per tornare ancora.
     Offri i doni nel giusto ordine e la via si aprirà."
    """,
    can_take=False,
    aliases=["piedistallo", "iscrizione"]
)

altare.set_property("slot_primavera", None)
altare.set_property("slot_estate", None)
altare.set_property("slot_autunno", None)
altare.set_property("slot_inverno", None)

def usa_altare(game, item):
    """Controlla se tutti gli oggetti sono al posto giusto."""
    p = item.get_property("slot_primavera")
    e = item.get_property("slot_estate")
    a = item.get_property("slot_autunno")
    i = item.get_property("slot_inverno")

    if p and e and a and i:
        # Controlla l'ordine corretto
        if p == "seme" and e == "spada" and a == "libro" and i == "bastone":
            # Apri la porta del tesoro!
            game.state["porta_aperta"] = True
            return """
            Gli oggetti si illuminano! Una luce dorata emana dall'altare.
            Un rombo sordo risuona nel tempio e la parete nord si apre,
            rivelando una camera nascosta!

            "Il ciclo è completo. Procedi, cercatore della verità."
            """
        else:
            # Reset tutto
            item.set_property("slot_primavera", None)
            item.set_property("slot_estate", None)
            item.set_property("slot_autunno", None)
            item.set_property("slot_inverno", None)
            return """
            Gli oggetti tremano e vengono espulsi dalle fessure,
            cadendo a terra con fragore. L'ordine non è corretto!
            Devi ricominciare.
            """
    else:
        return """
        L'altare ha quattro fessure. Devi inserire gli oggetti corretti
        in ciascuna, seguendo il ciclo delle stagioni.
        """

altare.add_action("usa", usa_altare)

# --- OGGETTI DELLE STATUE ---
# Questi oggetti vengono ottenuti risolvendo i mini-puzzle in ogni sala

seme = Item(
    name="seme",
    description="Un seme di cristallo verde, simbolo della rinascita primaverile.",
    can_take=True,
    aliases=["germoglio", "seme cristallo"]
)

spada = Item(
    name="spada",
    description="Una piccola spada cerimoniale, simbolo della forza estiva.",
    can_take=True,
    aliases=["spada fiammeggiante", "lama"]
)

libro = Item(
    name="libro",
    description="Un libro antico, simbolo della saggezza autunnale.",
    can_take=True,
    aliases=["tomo", "volume"]
)

bastone = Item(
    name="bastone",
    description="Un bastone di legno nodoso, simbolo del riposo invernale.",
    can_take=True,
    aliases=["staff", "verga"]
)

# --- STATUE CON MINI-PUZZLE ---

# Statua Primavera: Puzzle di poesia
statua_primavera = Item(
    name="statua",
    description="""
    La statua di una giovane donna sorride dolcemente. Nella mano
    tesa tiene un seme di cristallo. Ai suoi piedi c'è un'iscrizione:

    "Dimmi: cosa cresce senza radici,
     sale senza gambe,
     e tocca il cielo senza mani?"
    """,
    can_take=False,
    aliases=["donna", "statua primavera"]
)

# Quando il giocatore "parla" alla statua può rispondere
def parla_statua_primavera(game, item):
    risposta = input("La tua risposta: ").strip().lower()
    if "mont" in risposta or "collina" in risposta:
        if not game.state.get("seme_ottenuto"):
            game.state["seme_ottenuto"] = True
            game.current_room.add_item(seme)
            return """
            La statua annuisce e apre la mano. Il seme di cristallo
            cade a terra con un tintinnio melodioso.

            "Corretto, cercatore. La montagna cresce, sale e tocca il cielo."
            """
        else:
            return "Hai già ottenuto il seme."
    else:
        return """
        La statua scuote la testa lentamente.
        "Pensa ancora, cercatore. La risposta è nella natura stessa."
        """

statua_primavera.add_action("parla", parla_statua_primavera)
statua_primavera.add_action("usa", parla_statua_primavera)

# Statua Estate: Puzzle di coraggio (semplice interazione)
statua_estate = Item(
    name="statua",
    description="""
    Il guerriero di pietra ha un'espressione fiera. Impugna una
    spada fiammeggiante puntata verso l'alto. Un'iscrizione dice:

    "Solo chi osa affrontare il fuoco merita la forza dell'estate."
    """,
    can_take=False,
    aliases=["guerriero", "statua estate"]
)

def tocca_statua_estate(game, item):
    if not game.state.get("spada_ottenuta"):
        game.state["spada_ottenuta"] = True
        game.current_room.add_item(spada)
        return """
        Con coraggio, tocchi la spada fiammeggiante. Sorprendentemente,
        non brucia! La statua la rilascia nella tua mano.

        "Il vero fuoco arde nel cuore, non nella mano."
        """
    else:
        return "Hai già preso la spada."

statua_estate.add_action("tocca", tocca_statua_estate)
statua_estate.add_action("prendi", tocca_statua_estate)

# Statua Autunno: Puzzle di lettura
statua_autunno = Item(
    name="statua",
    description="""
    Il vecchio saggio tiene aperto un libro di pietra. Le pagine
    mostrano simboli misteriosi. Sopra la statua, un'iscrizione:

    "La conoscenza si acquisisce leggendo. Leggi ciò che mostro."
    """,
    can_take=False,
    aliases=["saggio", "statua autunno", "anziano"]
)

def leggi_statua_autunno(game, item):
    if not game.state.get("libro_ottenuto"):
        game.state["libro_ottenuto"] = True
        game.current_room.add_item(libro)
        return """
        Leggi attentamente i simboli sul libro di pietra. Lentamente
        cominci a comprenderli: sono antiche rune che parlano del
        ciclo delle stagioni.

        Il libro si materializza nelle tue mani, ora reale e non più di pietra.

        "Chi cerca di comprendere, comprende. Chi comprende, riceve."
        """
    else:
        return "Hai già il libro."

statua_autunno.add_action("leggi", leggi_statua_autunno)
statua_autunno.add_action("osserva", leggi_statua_autunno)

# Statua Inverno: Puzzle di pazienza (aspetta N turni)
statua_inverno = Item(
    name="statua",
    description="""
    Il vecchio incappucciato si appoggia a un bastone nodoso.
    La sua espressione è serena, paziente. Un'iscrizione recita:

    "L'inverno insegna la pazienza. Attendi, e riceverai."
    """,
    can_take=False,
    aliases=["vecchio", "statua inverno", "incappucciato"]
)

def aspetta_inverno(game, item):
    if not game.state.get("attesa_inverno_iniziata"):
        game.state["attesa_inverno_iniziata"] = True
        game.state["turni_attesa"] = game.turn_count + 3  # Aspetta 3 turni
        return """
        Ti fermi davanti alla statua e aspetti pazientemente...
        (Prova a fare altre azioni, poi torna qui dopo qualche turno)
        """
    elif game.state.get("bastone_ottenuto"):
        return "Hai già il bastone."
    else:
        return "Continua ad aspettare con pazienza..."

statua_inverno.add_action("aspetta", aspetta_inverno)
statua_inverno.add_action("usa", aspetta_inverno)

# Callback per dare il bastone dopo l'attesa
def check_inverno_callback(game, room):
    """Controlla se sono passati abbastanza turni."""
    if (game.state.get("attesa_inverno_iniziata") and
        not game.state.get("bastone_ottenuto") and
        game.turn_count >= game.state.get("turni_attesa", 999)):

        game.state["bastone_ottenuto"] = True
        if bastone not in room.items:
            room.add_item(bastone)
            print("\n" + "="*70)
            print("La statua si muove lentamente e posa il bastone ai tuoi piedi.")
            print('"La pazienza è ricompensata, cercatore."')
            print("="*70 + "\n")

sala_inverno.on_enter = check_inverno_callback

# ============================================================================
# SETUP GIOCO
# ============================================================================

# Aggiungi stanze
game.add_room("ingresso", ingresso)
game.add_room("primavera", sala_primavera)
game.add_room("estate", sala_estate)
game.add_room("autunno", sala_autunno)
game.add_room("inverno", sala_inverno)
game.add_room("tesoro", sala_tesoro)

# Connessioni
game.connect_rooms("ingresso", "nord", "primavera", bidirectional=True)
game.connect_rooms("ingresso", "est", "estate", bidirectional=True)
game.connect_rooms("ingresso", "sud", "autunno", bidirectional=True)
game.connect_rooms("ingresso", "ovest", "inverno", bidirectional=True)

# La camera del tesoro si apre solo dopo il puzzle
def check_porta_tesoro(game, room):
    if game.state.get("porta_aperta"):
        # Crea connessione alla camera del tesoro
        if "su" not in room.exits:
            room.add_exit("su", "tesoro")
            tesoro_room = game.get_room("tesoro")
            if tesoro_room:
                tesoro_room.add_exit("giù", "ingresso")

ingresso.on_enter = check_porta_tesoro

# Aggiungi oggetti
ingresso.add_item(altare)
sala_primavera.add_item(statua_primavera)
sala_estate.add_item(statua_estate)
sala_autunno.add_item(statua_autunno)
sala_inverno.add_item(statua_inverno)

# Corona del tesoro (obiettivo finale)
corona = Item(
    name="corona",
    description="""
    La leggendaria Corona delle Stagioni! Intarsiata con gemme che
    rappresentano le quattro stagioni, brilla di luce propria.
    Questo è il tesoro che cercavi!
    """,
    can_take=True,
    aliases=["corona stagioni", "tesoro"]
)

# Quando prendi la corona, vinci
def prendi_corona(game, item):
    game.game_won = True
    return """
    Afferri la Corona delle Stagioni. Nel momento in cui la tocchi,
    una sensazione di pace e completezza ti pervade.

    Il ciclo delle stagioni, eterno e perfetto, ora è rappresentato
    in questo artefatto nelle tue mani.

    🎉 HAI COMPLETATO LA QUEST DEL TEMPIO! 🎉
    """

# Sovrascrivi l'azione di prendere
original_take = game.cmd_take
def custom_take(parsed):
    if parsed.get('target') and 'corona' in parsed.get('target').lower():
        if game.current_room and game.current_room.find_item('corona'):
            game.game_won = True
            return prendi_corona(game, corona)
    return original_take(parsed)

game.cmd_take = custom_take

sala_tesoro.add_item(corona)

# Start
game.set_start("ingresso")

# ============================================================================
# FUNZIONE HELPER PER INSERIRE OGGETTI NELL'ALTARE
# ============================================================================

# Override del comando "usa" per gestire "usa X con altare"
original_use = game.cmd_use

def custom_use(parsed):
    target = parsed.get('target', '').lower()
    secondary = parsed.get('secondary', '').lower()

    # Controlla se sta usando qualcosa con l'altare
    if 'altare' in target or 'altare' in secondary:
        item_name = target if 'altare' in secondary else secondary

        # Trova l'oggetto
        item = game.find_item_in_inventory(item_name)
        if not item:
            return f"Non hai nessun {item_name}."

        # Determina lo slot
        slot_map = {
            'seme': ('slot_primavera', 'seme'),
            'spada': ('slot_estate', 'spada'),
            'libro': ('slot_autunno', 'libro'),
            'bastone': ('slot_inverno', 'bastone')
        }

        found = False
        for key, (slot, value) in slot_map.items():
            if key in item_name:
                altare.set_property(slot, value)
                game.inventory.remove(item)
                found = True
                return f"Inserisci {item.name} nella fessura appropriata dell'altare."

        if not found:
            return "Quest'oggetto non sembra adatto all'altare."

    # Altrimenti usa il comando normale
    return original_use(parsed)

game.cmd_use = custom_use

# ============================================================================
# AVVIO
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("ESEMPIO ESERCIZIO 4: PUZZLE ED EVENTI")
    print("="*70)
    print("\nQuesto esempio mostra:")
    print("- Puzzle logici integrati nella storia")
    print("- Eventi che modificano il mondo")
    print("- Uso di stati e flag")
    print("- Callback on_enter per eventi automatici")
    print("\nOBIETTIVO: Risolvi gli enigmi delle quattro stagioni!")
    print("\nSOLUZIONE:")
    print("1. Visita ogni sala stagionale")
    print("2. Risolvi il puzzle di ogni statua per ottenere l'oggetto")
    print("3. Usa gli oggetti con l'altare nell'ordine giusto")
    print("4. Entra nella camera del tesoro")
    print("="*70 + "\n")

    game.start()
