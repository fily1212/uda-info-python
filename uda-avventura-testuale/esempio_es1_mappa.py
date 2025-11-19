"""
ESEMPIO ESERCIZIO 1: MAPPA E MOVIMENTO
======================================

Questo esempio mostra come creare una mappa di stanze connesse
e permettere al giocatore di muoversi tra loro.

OBIETTIVI:
- Creare almeno 8 stanze
- Connettere le stanze con direzioni logiche
- Scrivere descrizioni brevi ma evocative
- Testare il movimento

COME USARE QUESTO ESEMPIO:
1. Leggi il codice per capire la struttura
2. Esegui il file: python esempio_es1_mappa.py
3. Prova a muoverti tra le stanze
4. Modifica le stanze per creare la TUA mappa
"""

from text_adventure_engine import Game, Room

# ============================================================================
# CREAZIONE DEL GIOCO
# ============================================================================

game = Game(
    title="Esplorazione del Castello",
    author="Esempio Es1",
    intro="""
    Ti trovi di fronte alle rovine di un antico castello.
    La nebbia avvolge le mura di pietra e un senso di mistero
    pervade l'aria. È tempo di esplorare...
    """
)

# ============================================================================
# CREAZIONE DELLE STANZE
# ============================================================================

# Stanza 1: Ingresso
ingresso = Room(
    name="Ingresso del Castello",
    description="""
    Ti trovi nell'ingresso del castello. Il grande portone di legno
    alle tue spalle è semi-aperto, lasciando filtrare una debole luce.
    Il pavimento è coperto di foglie secche e polvere. Due corridoi
    si aprono a nord e a est, mentre una scala sale verso l'alto.
    """,
    short_desc="Sei nell'ingresso del castello. Corridoi a nord e est, scala su."
)

# Stanza 2: Corridoio Ovest
corridoio_ovest = Room(
    name="Corridoio Ovest",
    description="""
    Un lungo corridoio si estende verso ovest. Le pareti sono decorate
    con arazzi ormai sbiaditi che raffigurano scene di battaglie antiche.
    Torce spente sono appese alle pareti. A nord vedi una porta di legno
    massiccio.
    """,
    short_desc="Corridoio con arazzi sbiaditi. Porta a nord."
)

# Stanza 3: Sala da Pranzo
sala_pranzo = Room(
    name="Sala da Pranzo",
    description="""
    Entri in una vasta sala da pranzo. Un enorme tavolo di quercia occupa
    il centro della stanza, con sedie polverose disposte intorno. Candelabri
    di ferro battuto pendono dal soffitto. Finestre alte e strette lasciano
    entrare raggi di luce pallida. Una porta si apre a ovest.
    """,
    short_desc="Grande sala da pranzo con tavolo di quercia. Porta a ovest."
)

# Stanza 4: Cucina
cucina = Room(
    name="Cucina",
    description="""
    La cucina del castello è sorprendentemente grande. Un camino enorme
    domina una parete, con pentole e padelle ancora appese sopra.
    Scaffali pieni di vasellame polveroso si allineano lungo le pareti.
    Un odore stantio permea l'aria. Si può tornare a sud.
    """,
    short_desc="Cucina con grande camino e vasellame polveroso."
)

# Stanza 5: Corridoio Est
corridoio_est = Room(
    name="Corridoio Est",
    description="""
    Questo corridoio è più stretto di quello ovest. Armature vuote
    sono disposte lungo le pareti, come sentinelle silenziose.
    Alcune sono arrugginite, altre stranamente lucide. Il corridoio
    continua verso est e a nord c'è una porta.
    """,
    short_desc="Corridoio con armature. Continua a est, porta a nord."
)

# Stanza 6: Biblioteca
biblioteca = Room(
    name="Biblioteca",
    description="""
    Sei nella biblioteca del castello. Scaffali altissimi stracolmi
    di libri ricoprono ogni parete dal pavimento al soffitto. Una
    scala a pioli è appoggiata a uno scaffale. L'odore di carta
    vecchia e cuoio ti avvolge. C'è qualcosa di magico in questo luogo.
    """,
    short_desc="Biblioteca piena di libri antichi e scaffali enormi."
)

# Stanza 7: Armeria
armeria = Room(
    name="Armeria",
    description="""
    L'armeria del castello. Rastrelliere vuote mostrano dove un tempo
    erano appese spade, lance e scudi. Alcune armi giacciono ancora
    sul pavimento, arrugginite dal tempo. Un manichino con un'armatura
    completa sta in un angolo, come a guardia della stanza.
    """,
    short_desc="Armeria con rastrelliere vuote e armi arrugginite."
)

# Stanza 8: Torre di Guardia
torre = Room(
    name="Torre di Guardia",
    description="""
    Sali le scale e arrivi alla torre di guardia. Finestre strette
    si aprono su tutti i lati, offrendo una vista mozzafiato sulla
    campagna circostante. Il vento soffia attraverso le aperture
    creando un suono inquietante. Una scala scende verso il basso.
    """,
    short_desc="Torre di guardia con vista sulla campagna."
)

# ============================================================================
# AGGIUNTA STANZE AL GIOCO
# ============================================================================

game.add_room("ingresso", ingresso)
game.add_room("corridoio_ovest", corridoio_ovest)
game.add_room("sala_pranzo", sala_pranzo)
game.add_room("cucina", cucina)
game.add_room("corridoio_est", corridoio_est)
game.add_room("biblioteca", biblioteca)
game.add_room("armeria", armeria)
game.add_room("torre", torre)

# ============================================================================
# CONNESSIONE DELLE STANZE
# ============================================================================

# Dall'ingresso
game.connect_rooms("ingresso", "nord", "corridoio_ovest", bidirectional=True)
game.connect_rooms("ingresso", "est", "corridoio_est", bidirectional=True)
game.connect_rooms("ingresso", "su", "torre", bidirectional=True)

# Dal corridoio ovest
game.connect_rooms("corridoio_ovest", "nord", "cucina", bidirectional=True)
game.connect_rooms("corridoio_ovest", "est", "sala_pranzo", bidirectional=True)

# Dal corridoio est
game.connect_rooms("corridoio_est", "nord", "biblioteca", bidirectional=True)
game.connect_rooms("corridoio_est", "est", "armeria", bidirectional=True)

# ============================================================================
# CONFIGURAZIONE E AVVIO
# ============================================================================

# Imposta la stanza di partenza
game.set_start("ingresso")

# Avvia il gioco
if __name__ == "__main__":
    print("\n" + "="*70)
    print("ESEMPIO ESERCIZIO 1: MAPPA E MOVIMENTO")
    print("="*70)
    print("\nQuesto è un esempio di mappa con 8 stanze connesse.")
    print("Prova a esplorarle tutte!")
    print("\nCONSIGLIO: Fai una mappa su carta mentre giochi per orientarti.")
    print("="*70 + "\n")

    game.start()
