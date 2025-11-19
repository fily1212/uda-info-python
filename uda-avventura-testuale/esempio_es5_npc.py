"""
ESEMPIO ESERCIZIO 5: NPC E DIALOGHI
====================================

Questo esempio mostra come creare NPC caratterizzati con dialoghi
dinamici che cambiano in base agli eventi e alle azioni del giocatore.

OBIETTIVI:
- Creare NPC con personalità distinte
- Implementare dialoghi a stati multipli
- Far sì che i dialoghi influenzino la storia
- Usare gli NPC per fornire indizi e oggetti

TECNICHE DIMOSTRATE:
- Stati dei dialoghi (default, dopo eventi, ecc.)
- NPC che danno oggetti
- NPC che reagiscono all'inventario del giocatore
- Relazioni tra NPC
"""

from text_adventure_engine import Game, Room, Item, NPC

# ============================================================================
# CREAZIONE GIOCO
# ============================================================================

game = Game(
    title="Il Mercato del Porto",
    author="Esempio Es5",
    intro="""
    Sei un mercante in cerca di una rara spezia chiamata "Zafferano Stellare"
    per completare un importante affare. Sei arrivato al famoso mercato
    del porto, dove si dice si possa trovare qualsiasi cosa...
    se si sa con chi parlare.

    Il sole del pomeriggio illumina le bancarelle colorate. L'aria
    è piena di odori speziati e voci che contrattano.
    """
)

# ============================================================================
# STANZE
# ============================================================================

piazza_mercato = Room(
    name="Piazza del Mercato",
    description="""
    La piazza è affollata di bancarelle e commercianti che gridano
    le loro offerte. Tessuti colorati sventolano al vento, montagne
    di frutta esotica attirano lo sguardo, e l'odore di spezie
    riempie l'aria. A nord c'è la taverna, a est il porto.
    """,
    short_desc="Piazza affollata di mercanti. Taverna a nord, porto a est."
)

taverna = Room(
    name="Taverna del Gabbiano",
    description="""
    La taverna è affollata di marinai e mercanti che bevono e
    chiacchierano. Un bancone di legno scuro domina un lato della
    stanza, dietro cui il taverniere serve birra. Tavoli sparsi
    sono occupati da clienti rumorosi.
    """,
    short_desc="Taverna rumorosa con marinai e mercanti."
)

porto = Room(
    name="Porto",
    description="""
    Le banchine del porto sono animate da scaricatori che trasportano
    casse e barili. Navi di ogni tipo sono ormeggiate, con vele
    di colori diversi. Gabbiani gridano sopra le tue testa.
    Un vecchio marinaio ripara una rete da pesca.
    """,
    short_desc="Porto con navi ormeggiate e scaricatori al lavoro."
)

retrobottega = Room(
    name="Retrobottega della Spezieria",
    description="""
    Un piccolo locale segreto pieno di barattoli, sacchi e contenitori
    di ogni tipo. L'odore qui è così intenso che quasi stordisce.
    Scaffali dal pavimento al soffitto traboccano di spezie rare.
    """,
    short_desc="Retrobottega segreto pieno di spezie rare."
)

# ============================================================================
# NPC CON DIALOGHI DINAMICI
# ============================================================================

# --- NPC 1: MERCANTE DI SPEZIE ---
# Questo NPC ha dialoghi che cambiano in base alle azioni del giocatore

mercante = NPC(
    name="mercante",
    description="""
    Un uomo corpulento con una barba curata e vestiti elaborati.
    Le sue mani sono macchiate di polveri colorate - probabilmente
    spezie. Ti guarda con occhio esperto, valutando se sei un
    cliente serio o un perditempo.
    """,
    aliases=["uomo", "spezierie", "commerciante"],
    dialogue={
        'default': """
            Benvenuto! Cerchi spezie? Ne ho di ogni tipo... beh, quasi.
            Lo Zafferano Stellare? Ah, quello è raro. Molto raro.
            Non lo vendo a chiunque. Devi dimostrarmi che sei un
            mercante serio. Portami una prova del tuo mestiere.
        """,
        'dopo_moneta': """
            Vedo che hai la Moneta del Mercante! Bene, allora sei
            davvero uno di noi. Ma lo Zafferano Stellare... non ce
            l'ho qui in mostra. È troppo prezioso. È nel mio
            retrobottega segreto. Però la porta è chiusa a chiave.
        """,
        'dopo_chiave': """
            Hai la chiave! Perfetto. Il retrobottega è dietro la
            tenda rossa. Lì troverai lo Zafferano Stellare. Ma
            attenzione: costa 100 monete d'oro. Le hai?
        """,
        'finale': """
            Affare fatto! Piacere di fare affari con te.
            Torna quando vuoi!
        """
    }
)

# Callback per il mercante
def parla_mercante_callback(game, npc):
    """Cambia il dialogo in base a cosa ha il giocatore."""
    if game.find_item_in_inventory("zafferano"):
        npc.set_dialogue_state('finale')
    elif game.find_item_in_inventory("chiave retrobottega"):
        npc.set_dialogue_state('dopo_chiave')
    elif game.find_item_in_inventory("moneta mercante"):
        # Se parli dopo aver ottenuto la moneta, ti dà la chiave
        if not game.state.get("chiave_ricevuta"):
            game.state["chiave_ricevuta"] = True
            chiave = Item(
                name="chiave retrobottega",
                description="Una piccola chiave di ottone con inciso un simbolo di spezie.",
                can_take=True,
                aliases=["chiave"]
            )
            game.inventory.append(chiave)
            # Apri il passaggio
            piazza_mercato.add_exit("ovest", "retrobottega")
            retrobottega.add_exit("est", "piazza_mercato")

        npc.set_dialogue_state('dopo_chiave')
    else:
        npc.set_dialogue_state('default')

mercante.on_talk = parla_mercante_callback

# --- NPC 2: TAVERNIERE ---
# Questo NPC fornisce informazioni se gli compri da bere

taverniere = NPC(
    name="taverniere",
    description="""
    Un uomo robusto con un grembiule macchiato di birra. Ha un
    sorriso amichevole ma occhi astuti. Sa tutto quello che succede
    in porto - e sa come farsi pagare per le informazioni.
    """,
    aliases=["barista", "oste"],
    dialogue={
        'default': """
            Benvenuto alla Taverna del Gabbiano! Cosa posso servirti?
            Una birra? Costa 5 monete... o se preferisci informazioni,
            quelle costano un po' di più. *strizza l'occhio*
        """,
        'dopo_birra': """
            Allora, cercavi informazioni? Ah, lo Zafferano Stellare!
            Solo il mercante nella piazza ne ha. Ma è un tipo diffidente.
            Non vende a chiunque. Dice di voler vedere la "Moneta del
            Mercante" prima di fare affari seri. È una specie di...
            come dire... carta di presentazione tra mercanti.

            Io ne ho una da qualche parte... un marinaio me l'ha data
            per saldare un debito. Se vuoi, te la do per... diciamo
            20 monete?
        """,
        'dopo_compra': """
            Grazie per l'affare! Se hai bisogno d'altro, sono qui.
        """
    }
)

# Oggetto: Birra
birra = Item(
    name="birra",
    description="Una pinta di birra schiumosa.",
    can_take=True
)

# Oggetto: Moneta del Mercante
moneta_mercante = Item(
    name="moneta mercante",
    description="""
    Una moneta d'oro con incisi simboli mercantili. È un segno
    di riconoscimento tra i mercanti più seri.
    """,
    can_take=True,
    aliases=["moneta"]
)

def parla_taverniere_callback(game, npc):
    """Gestisce gli acquisti dal taverniere."""
    if game.state.get("moneta_comprata"):
        npc.set_dialogue_state('dopo_compra')
    elif game.state.get("birra_comprata"):
        # Offri di vendere la moneta
        npc.set_dialogue_state('dopo_birra')
    else:
        npc.set_dialogue_state('default')

taverniere.on_talk = parla_taverniere_callback

# --- NPC 3: VECCHIO MARINAIO ---
# Questo NPC ti dà monete se gli fai un favore

marinaio = NPC(
    name="marinaio",
    description="""
    Un vecchio lupo di mare con la pelle bruciata dal sole e dal
    sale. Ha una cicatrice che gli attraversa il volto e manca
    di alcuni denti. Sta riparando una rete da pesca.
    """,
    aliases=["vecchio", "lupo di mare", "pescatore"],
    dialogue={
        'default': """
            Argh, maledette reti! Si rompono sempre nel momento sbagliato.
            Dovrei andare a comprarmi del nuovo cordame, ma sono al verde.
            Se qualcuno mi prestasse 10 monete per il cordame, gliene
            renderei 30 quando torno dalla pesca domani. Giuro sulla
            barba di Nettuno!
        """,
        'dopo_prestito': """
            Grazie! Ora posso sistemare la rete. Aspetta un attimo...
            *fruga nelle tasche* Ecco, prendi queste monete come anticipo!
            Sono un uomo di parola!
        """,
        'finale': """
            Buon vento e buona fortuna, amico!
        """
    }
)

def parla_marinaio_callback(game, npc):
    """Gestisce il prestito al marinaio."""
    if game.state.get("marinaio_pagato"):
        npc.set_dialogue_state('finale')

marinaio.on_talk = parla_marinaio_callback

# --- NPC 4: MENDICANTE ---
# Questo NPC ti dà le monete iniziali se sei gentile

mendicante = NPC(
    name="mendicante",
    description="""
    Un'anziana donna in stracci seduta su un angolo della piazza.
    Ha occhi gentili nonostante la vita dura. Tende la mano verso
    i passanti, ma pochi le danno retta.
    """,
    aliases=["donna", "anziana", "vecchia"],
    dialogue={
        'default': """
            Per favore signore, una moneta per una povera vecchia?
            Ho freddo e fame...
        """,
        'dopo_aiuto': """
            Che il cielo ti benedica, figliolo! Sei una persona buona.
            Lascia che ti dica qualcosa: questo porto è pieno di affaristi,
            ma ci sono ancora brave persone. Il taverniere, per esempio,
            sembra burbero ma ha cuore d'oro. Parlagli, potrebbe aiutarti.

            Ah, e prendi questo. *ti porge una borsa* L'ho trovata ieri.
            Dentro ci sono delle monete. Tu ne hai più bisogno di me.
        """,
        'finale': """
            Grazie ancora, caro. Che la fortuna ti accompagni!
        """
    }
)

# Borsa con monete iniziali
borsa = Item(
    name="borsa",
    description="Una piccola borsa di cuoio con 30 monete d'oro dentro.",
    can_take=True
)

def parla_mendicante_callback(game, npc):
    """Gestisce l'interazione con la mendicante."""
    if game.state.get("mendicante_aiutata"):
        npc.set_dialogue_state('finale')

mendicante.on_talk = parla_mendicante_callback

# ============================================================================
# OGGETTO FINALE: ZAFFERANO STELLARE
# ============================================================================

zafferano = Item(
    name="zafferano",
    description="""
    Lo Zafferano Stellare! Fili dorati che brillano con luce propria.
    È incredibilmente raro e prezioso. Questo è esattamente ciò che
    cercavi!
    """,
    can_take=True,
    aliases=["zafferano stellare", "spezia"]
)

# Quando prendi lo zafferano, vinci
original_take = game.cmd_take

def custom_take(parsed):
    result = original_take(parsed)
    if game.find_item_in_inventory("zafferano") and not game.game_won:
        game.game_won = True
        print("\n" + "="*70)
        print("🎉 HAI OTTENUTO LO ZAFFERANO STELLARE! 🎉")
        print("="*70)
        print("Finalmente hai la spezia che cercavi!")
        print("Il tuo affare può essere completato.")
        print("MISSIONE COMPIUTA!")
        print("="*70 + "\n")
    return result

game.cmd_take = custom_take

# ============================================================================
# COMANDI CUSTOM PER GLI ACQUISTI
# ============================================================================

# Sistema di monete semplificato
game.state["monete"] = 0

def cmd_compra(parsed):
    """Comando custom per comprare cose."""
    target = parsed.get('target', '').lower()

    if 'birra' in target:
        if game.state["monete"] >= 5:
            game.state["monete"] -= 5
            game.state["birra_comprata"] = True
            game.inventory.append(birra)
            return "Compri una birra per 5 monete. Il taverniere sorride."
        else:
            return "Non hai abbastanza monete! (Ti servono 5)"

    elif 'moneta' in target and game.current_room == taverna:
        if game.state.get("birra_comprata"):
            if game.state["monete"] >= 20:
                game.state["monete"] -= 20
                game.state["moneta_comprata"] = True
                game.inventory.append(moneta_mercante)
                return """
                Compri la Moneta del Mercante per 20 monete.
                Il taverniere te la porge con un sorriso.
                "Usala bene!" dice.
                """
            else:
                return "Non hai abbastanza monete! (Ti servono 20)"
        else:
            return "Il taverniere non vuole venderla ancora. Prova a comprare una birra prima."

    return "Non puoi comprare quello qui."

# Comando per dare monete
def cmd_dai(parsed):
    """Comando per dare cose agli NPC."""
    target = parsed.get('target', '')

    if 'mendicante' in target.lower() or (game.current_room == piazza_mercato and mendicante in game.current_room.npcs):
        if game.state["monete"] >= 1:
            game.state["monete"] -= 1
            game.state["mendicante_aiutata"] = True
            game.inventory.append(borsa)
            game.state["monete"] += 30  # La borsa ha 30 monete
            return """
            Dai una moneta alla mendicante. I suoi occhi si illuminano.
            Lei ti ringrazia calorosamente e ti dà la borsa che ha trovato.

            Dentro ci sono 30 monete d'oro! La sua generosità supera la tua.
            """
        else:
            return "Non hai monete da dare!"

    elif 'marinaio' in target.lower() or (game.current_room == porto and marinaio in game.current_room.npcs):
        if game.state.get("marinaio_pagato"):
            return "Hai già aiutato il marinaio."
        if game.state["monete"] >= 10:
            game.state["monete"] -= 10
            game.state["marinaio_pagato"] = True
            game.state["monete"] += 30  # Ti restituisce 30
            return """
            Presti 10 monete al marinaio. Lui ti ringrazia e, sorprendentemente,
            ti dà subito 30 monete come anticipo! È davvero un uomo di parola.

            "Non dimenticare mai un favore!" dice con un sorriso sdentato.
            """
        else:
            return "Non hai abbastanza monete! (Ti servono 10)"

    return "A chi vuoi dare qualcosa?"

# Aggiungi comandi custom
original_process = game.process_command

def custom_process(command):
    # Comandi custom
    if command.strip().lower().startswith("compra"):
        parts = command.split(maxsplit=1)
        target = parts[1] if len(parts) > 1 else ""
        return cmd_compra({'target': target})
    elif command.strip().lower().startswith("dai") or command.strip().lower().startswith("presta"):
        parts = command.split()
        target = " ".join(parts[1:]) if len(parts) > 1 else ""
        return cmd_dai({'target': target})
    elif command.strip().lower() in ["monete", "soldi", "oro"]:
        return f"Hai {game.state['monete']} monete d'oro."

    return original_process(command)

game.process_command = custom_process

# ============================================================================
# SETUP GIOCO
# ============================================================================

# Aggiungi stanze
game.add_room("piazza", piazza_mercato)
game.add_room("taverna", taverna)
game.add_room("porto", porto)
game.add_room("retrobottega", retrobottega)

# Collegamenti
game.connect_rooms("piazza", "nord", "taverna", bidirectional=True)
game.connect_rooms("piazza", "est", "porto", bidirectional=True)
# Il retrobottega si apre solo dopo aver parlato col mercante

# Aggiungi NPC
piazza_mercato.add_npc(mercante)
piazza_mercato.add_npc(mendicante)
taverna.add_npc(taverniere)
porto.add_npc(marinaio)

# Aggiungi zafferano al retrobottega
retrobottega.add_item(zafferano)

# Monete iniziali
game.state["monete"] = 5  # Parti con poche monete

# Start
game.set_start("piazza")

# ============================================================================
# AVVIO
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("ESEMPIO ESERCIZIO 5: NPC E DIALOGHI")
    print("="*70)
    print("\nQuesto esempio mostra:")
    print("- NPC con personalità distinte")
    print("- Dialoghi che cambiano in base agli eventi")
    print("- NPC che danno oggetti e informazioni")
    print("- Sistema di economia semplificato")
    print("\nOBIETTIVO: Ottieni lo Zafferano Stellare!")
    print("\nCOMANDI SPECIALI:")
    print("- 'monete' per vedere quante ne hai")
    print("- 'compra <cosa>' per comprare")
    print("- 'dai <cosa> a <npc>' per dare oggetti/monete")
    print("\nSOLUZIONE:")
    print("1. Dai una moneta alla mendicante → ottieni borsa con 30 monete")
    print("2. Vai in taverna, compra birra (5 monete)")
    print("3. Parla col taverniere, compra moneta mercante (20 monete)")
    print("4. Torna in piazza, parla col mercante → ottieni chiave")
    print("5. Vai nel retrobottega, prendi lo zafferano")
    print("="*70 + "\n")

    game.start()
