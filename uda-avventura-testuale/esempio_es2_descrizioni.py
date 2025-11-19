"""
ESEMPIO ESERCIZIO 2: DESCRIZIONI AMBIENTALI E ATMOSFERA
========================================================

Questo esempio mostra come scrivere descrizioni dettagliate e atmosferiche
per creare immersione nel giocatore.

OBIETTIVI:
- Scrivere descrizioni di 100-200 parole per ogni stanza
- Usare dettagli sensoriali (vista, udito, olfatto, tatto)
- Mantenere coerenza di stile e tono
- Creare atmosfera attraverso le parole

TECNICHE NARRATIVE USATE:
- Show, don't tell (mostra, non dire)
- Dettagli specifici invece di generalizzazioni
- Metafore e similitudini
- Appello ai cinque sensi
"""

from text_adventure_engine import Game, Room

# ============================================================================
# CREAZIONE DEL GIOCO
# ============================================================================

game = Game(
    title="La Cripta Dimenticata",
    author="Esempio Es2",
    intro="""
    Il vento notturno sibila tra le lapidi del vecchio cimitero mentre
    ti avvicini all'ingresso di una cripta abbandonata. La luna piena
    getta ombre lunghe e inquietanti. L'aria sa di terra bagnata e foglie
    marce. Un brivido ti percorre la schiena... non per il freddo, ma per
    qualcosa di più profondo, primordiale. Il terrore dell'ignoto.

    Con una lanterna tremante in mano, spingi la pesante porta di pietra.
    Si apre con un gemito che sembra un lamento...
    """
)

# ============================================================================
# STANZE CON DESCRIZIONI DETTAGLIATE
# ============================================================================

# NOTA: Osserva come ogni descrizione usa:
# 1. Dettagli visivi specifici
# 2. Suoni
# 3. Odori
# 4. Sensazioni tattili (temperatura, texture)
# 5. Emozioni evocate

# Stanza 1: L'Anticamera
anticamera = Room(
    name="Anticamera della Cripta",
    description="""
    L'anticamera è stretta e oppressiva. Le pareti di pietra grezza
    trasudano umidità, e gocce d'acqua cadono dal soffitto basso con
    un ritmico *plip-plop* che riecheggia nel silenzio sepolcrale.
    La tua lanterna proietta ombre danzanti che sembrano figure
    spettrali in movimento.

    L'aria è gelida, così fredda che vedi il tuo respiro condensarsi
    in nuvolette bianche. Un odore penetrante di muffa e decomposizione
    ti aggredisce le narici, facendoti quasi vomitare. Sotto i piedi,
    il pavimento è viscido e irregolare - devi fare attenzione a non
    scivolare.

    Davanti a te, un corridoio si apre verso nord, inghiottito dal buio.
    Alle tue spalle, la porta d'entrata è ancora socchiusa, mostrando
    un ultimo spiraglio della notte stellata all'esterno - una via di fuga
    che sembra sempre più allettante ad ogni secondo che passa.
    """,
    short_desc="Anticamera umida e oppressiva. Corridoio a nord, uscita a sud."
)

# Stanza 2: Corridoio dei Teschi
corridoio_teschi = Room(
    name="Corridoio dei Teschi",
    description="""
    Il corridoio si estende davanti a te come la gola di un mostro
    antidiluviano. Ciò che ti fa gelare il sangue, però, sono le pareti:
    centinaia, forse migliaia di teschi umani sono incastonati nella
    pietra, formando un macabro mosaico di morte. I loro occhi vuoti
    sembrano seguirti mentre cammini, le loro bocche spalancate in
    eterni urli muti.

    La tua lanterna illumina i volti ossuti, creando giochi di luce
    e ombra che li fanno sembrare vivi. Giureresti di aver visto uno
    muovere la mascella... ma forse è solo la tua immaginazione che
    lavora troppo. Un suono sottile riempie il corridoio: un sussurro
    quasi impercettibile, come se i morti stessi stessero conversando
    tra loro.

    L'odore di morte è qui ancora più forte, mescolato con qualcosa
    di dolciastro che ti fa girare lo stomaco. Il pavimento è cosparso
    di ossa più piccole - dita, costole - che scricchiolano sotto i
    tuoi passi.

    Il corridoio continua sia a nord che a est. A sud puoi tornare
    all'anticamera.
    """,
    short_desc="Corridoio con pareti fatte di teschi. Continua nord ed est."
)

# Stanza 3: Cripta Principale
cripta = Room(
    name="Cripta Principale",
    description="""
    Entri nella camera principale della cripta, e il tuo respiro si
    blocca in gola. È una sala circolare enorme, con un soffitto a
    volta così alto che la luce della tua lanterna non riesce a
    raggiungerne la sommità. L'oscurità sopra di te è assoluta,
    primordiale, come fissare nell'abisso stesso.

    Al centro della stanza, un sarcofago di marmo nero si erge su
    un piedistallo. È magnifico e terrificante al tempo stesso:
    decorato con rune incise che sembrano pulsare di una luce
    verdognola tenue. La pietra è così levigata che riflette la
    fiamma della lanterna come uno specchio oscuro.

    Intorno al sarcofago, sei statue di angeli piangenti formano
    un cerchio protettivo. Ma questi angeli non sono messaggeri
    di speranza: i loro volti sono contorti in espressioni di
    puro terrore, le ali spezzate, le mani protese come per
    supplicare pietà. Lacrime di pietra solcano le loro guance.

    L'atmosfera qui è soffocante. Senti un peso invisibile sul
    petto, come se l'aria stessa ti stesse schiacciando. Un
    ronzio a bassa frequenza pervade la stanza, così basso da
    essere più sentito nelle ossa che udito con le orecchie.
    Qualcosa qui è... sbagliato. Innaturale.

    Puoi tornare a sud.
    """,
    short_desc="Vasta cripta circolare con sarcofago nero al centro e angeli piangenti."
)

# Stanza 4: Camera degli Ossari
ossario = Room(
    name="Camera degli Ossari",
    description="""
    Entri in una camera laterale e ti rendi conto con orrore che
    ogni centimetro delle pareti è occupato da nicchie scavate
    nella pietra. In ciascuna nicchia riposano i resti di un corpo:
    ossa disposte con cura meticolosa, teschi posizionati in modo
    da guardare verso il centro della stanza.

    Non sono solo poche tombe. Sono centinaia. Migliaia, forse.
    I morti di intere generazioni accumulati in questo spazio
    claustrofobico. La stanza sembra comprimersi su di te,
    soffocante nella sua morbosità.

    Ciò che disturba di più, però, è l'ordine. Qualcuno ha
    organizzato questi resti con cura ossessiva. Le ossa sono
    pulite, bianche, disposte in pattern geometrici perfetti.
    Alcuni teschi portano corone di fiori secchi ormai ridotti
    in polvere. Altri hanno monete di rame ossidate poste sulle
    orbite oculari.

    L'aria qui è secca, quasi polverosa. Ogni tuo movimento
    solleva invisibili particelle che danzano nella luce della
    lanterna. Il silenzio è assoluto, rotto solo dal battito
    accelerato del tuo cuore.

    Puoi tornare a ovest.
    """,
    short_desc="Camera piena di nicchie con resti umani ordinati meticolosamente."
)

# ============================================================================
# CONFIGURAZIONE DEL GIOCO
# ============================================================================

game.add_room("anticamera", anticamera)
game.add_room("corridoio", corridoio_teschi)
game.add_room("cripta", cripta)
game.add_room("ossario", ossario)

# Collegamenti
game.connect_rooms("anticamera", "nord", "corridoio", bidirectional=True)
game.connect_rooms("corridoio", "nord", "cripta", bidirectional=True)
game.connect_rooms("corridoio", "est", "ossario", bidirectional=True)

# Stanza iniziale
game.set_start("anticamera")

# ============================================================================
# AVVIO
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("ESEMPIO ESERCIZIO 2: DESCRIZIONI AMBIENTALI E ATMOSFERA")
    print("="*70)
    print("\nQuesto esempio dimostra l'uso di descrizioni dettagliate")
    print("per creare atmosfera horror/gotica.")
    print("\nOSSERVA:")
    print("- Uso di dettagli sensoriali (vista, udito, olfatto, tatto)")
    print("- Metafore e similitudini ('come la gola di un mostro')")
    print("- Show don't tell (non dice 'fa paura', lo mostra)")
    print("- Coerenza di tono e stile")
    print("="*70 + "\n")

    game.start()
