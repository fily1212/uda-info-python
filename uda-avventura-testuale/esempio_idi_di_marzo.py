"""
LE IDI DI MARZO - Un Complotto a Roma
======================================

Avventura testuale storica ambientata nell'Antica Roma, 44 a.C.
Il giorno prima dell'assassinio di Giulio Cesare.

GENERE: Storico/Thriller Politico
DURATA: 25-35 minuti
DIFFICOLTÀ: Media-Alta

NOTA DIDATTICA:
Questa avventura è storicamente ispirata ma prende libertà narrative.
I personaggi e gli eventi sono reali, ma la trama del giocatore è
fittizia. Include riferimenti storici accurati per scopo educativo.

STORIA:
Sei Marcus Verus, un liberto (ex-schiavo liberato) che lavora come
scriba personale per il senatore Decimus Brutus. È il 14 marzo del
44 a.C., e domani il Senato si riunirà nella Curia di Pompeo.

Mentre trascrivi documenti nel tablinum del tuo padrone, scopri per
caso una lettera cifrata che parla di un complotto contro il dittatore
Giulio Cesare. Cosa farai? Avvertire Cesare? Rimanere in silenzio?
Unirti ai congiurati?

La storia di Roma è nelle tue mani...
"""

from text_adventure_engine import Game, Room, Item, NPC

# ============================================================================
# CREAZIONE GIOCO
# ============================================================================

game = Game(
    title="Le Idi di Marzo - Un Complotto a Roma",
    author="Sistema Didattico - Esempio Storico",
    intro="""
    ═══════════════════════════════════════════════════════════════════
                        ROMA, 14 MARZO 44 a.C.
    ═══════════════════════════════════════════════════════════════════

    Il sole del tardo pomeriggio getta lunghe ombre sui tetti di Roma.
    Dalla finestra del tablinum vedi il Foro Romano animato dalla solita
    folla: mercanti che contrattano, senatori in toga che discutono,
    schiavi che corrono per commissioni dei loro padroni.

    Sei MARCUS VERUS, un uomo fortunato. Nato schiavo, sei stato liberato
    dal tuo padrone in riconoscimento della tua intelligenza e della tua
    educazione. Ora servi come scriba personale del senatore Decimus Brutus,
    un uomo influente e amico personale del dittatore Giulio Cesare.

    Il tuo lavoro è semplice: copiare lettere, tradurre dal greco, tenere
    i conti. Vivi bene per gli standard di un liberto. Hai una stanza tutta
    tua, mangi ogni giorno, puoi leggere i libri della biblioteca del
    padrone.

    Ma oggi qualcosa è diverso. Nell'aria di Roma si respira tensione.
    I senatori sussurrano negli angoli. Gli sguardi sono cupi. E tu,
    poco fa, mentre sistemavi dei rotoli nella biblioteca, hai intravisto
    una lettera sigillata con uno strano simbolo...

    Una lettera che potrebbe cambiare il corso della storia.

    ═══════════════════════════════════════════════════════════════════
                    14 MARZO - POMERIGGIO INOLTRATO
                       Mancano poche ore al tramonto
    ═══════════════════════════════════════════════════════════════════
    """
)

# ============================================================================
# STANZE - DOMUS DI DECIMUS BRUTUS
# ============================================================================

atrium = Room(
    name="Atrium",
    description="""
    L'atrium è il cuore della domus. Il soffitto è aperto al centro
    (compluvium), lasciando entrare la luce del giorno. Sotto, una vasca
    di marmo (impluvium) raccoglie l'acqua piovana. Ai lati, colonne
    dipinte di rosso pompeiano sostengono il tetto.

    Le pareti sono decorate con affreschi che raffigurano scene mitologiche:
    Romolo e Remo allattati dalla lupa, il ratto delle Sabine. Statue di
    marmo dei Lares (dei protettori della casa) vegliano dagli angoli.

    Il pavimento è un mosaico elaborato che rappresenta un labirinto.
    Al centro dell'impluvium galleggia un petalo di rosa.

    A nord c'è il tablinum (lo studio). A est le camere da letto.
    A ovest il triclinium (sala da pranzo). A sud la porta principale
    che conduce alla strada.
    """,
    short_desc="Atrium con impluvium centrale. Tablinum nord, camere est, triclinium ovest."
)

tablinum = Room(
    name="Tablinum (Studio)",
    description="""
    Il tablinum è lo studio del senatore Brutus. Una stanza sobria ma
    elegante, con pareti rivestite di pannelli di legno scuro. La luce
    entra da una finestra che dà sul peristilio (giardino interno).

    Una grande scrivania di legno di cedro domina la stanza, coperta
    di tavolette di cera, rotoli di papiro, stili per scrivere.
    Accanto alla scrivania, un armadio chiuso a chiave dove il senatore
    conserva i documenti importanti.

    Sulla parete, una maschera mortuaria di un antenato di Brutus
    ti fissa con occhi di cera. È tradizione romana conservare le
    maschere degli antenati illustri.

    Questo è il tuo luogo di lavoro. Qui passi le giornate a copiare
    lettere e tenere i registri.

    L'atrium è a sud. Una porta conduce al peristilio a nord.
    """,
    short_desc="Studio del senatore con scrivania e documenti. Peristilio nord."
)

cubiculum = Room(
    name="Cubiculum (Tua Camera)",
    description="""
    La tua camera è piccola ma confortevole - un privilegio raro per
    un liberto. Un letto con materasso di lana, un piccolo tavolo,
    uno sgabello, una lucerna a olio, un baule per i tuoi pochi averi.

    Sulla parete hai appeso la tessera (tavoletta) che certifica la
    tua libertà, il documento più prezioso che possiedi. Senza quella,
    saresti ancora uno schiavo.

    Dalla finestra stretta vedi un vicolo laterale. Bambini giocano
    tra le pozzanghere. Un gatto randagio cerca cibo.

    Semplice, ma è casa tua.

    L'atrium è a ovest.
    """,
    short_desc="La tua piccola camera con letto e baule."
)

triclinium = Room(
    name="Triclinium (Sala da Pranzo)",
    description="""
    Il triclinium è dove il senatore riceve gli ospiti per i banchetti.
    Tre divani (kline) sono disposti a ferro di cavallo intorno a un
    tavolo basso. I nobili romani mangiano sdraiati, appoggiati sul
    gomito sinistro.

    Gli affreschi sulle pareti mostrano scene di banchetti dionisiaci:
    satiri, ninfe, grappoli d'uva. Il pavimento è un mosaico con
    pesci e creature marine.

    Un'iscrizione sul mosaico recita: "Cave canem" (Attenti al cane),
    anche se la domus non ha cani.

    Stasera il triclinium è vuoto. Il senatore cenerà fuori.

    L'atrium è a est.
    """,
    short_desc="Sala da pranzo con divani e mosaici elaborati."
)

peristilium = Room(
    name="Peristilium (Giardino)",
    description="""
    Il peristilio è un giardino interno circondato da un colonnato.
    È un'oasi di pace nel caos di Roma. Piante aromatiche crescono
    in vasi: rosmarino, lavanda, mirto. Al centro c'è una fontana
    con una statua di Nettuno.

    L'acqua della fontana zampilla dolcemente. Uccelli cinguettano
    tra i rami di un piccolo fico. L'aria profuma di fiori.

    Lungo il colonnato ci sono panche di marmo dove sedersi a leggere
    o meditare. Questo è il tuo posto preferito per pensare.

    Il tablinum è a sud. A est c'è la biblioteca.
    """,
    short_desc="Giardino interno con colonnato e fontana."
)

biblioteca = Room(
    name="Bibliotheca (Biblioteca)",
    description="""
    La biblioteca è il tesoro della domus. Scaffali di legno contengono
    rotoli di papiro e codici: opere di Cicerone, Virgilio, Omero in
    greco, trattati di filosofia stoica, storie di Livio.

    Alcuni rotoli sono conservati in cilindri di cuoio per proteggerli.
    Altri sono chiusi con sigilli di cera. La stanza profuma di papiro
    antico e inchiostro.

    Un leggio di legno regge un'opera aperta: "De Bello Gallico" di
    Giulio Cesare. Il senatore Brutus lo stava leggendo.

    Su un tavolo laterale noti una cassetta di legno con un lucchetto.
    Contiene documenti che il senatore considera particolarmente
    riservati.

    Il peristilio è a ovest.
    """,
    short_desc="Biblioteca ricca di rotoli e opere antiche."
)

# ============================================================================
# STANZE - ROMA ESTERNA
# ============================================================================

via = Room(
    name="Via Sacra",
    description="""
    Esci dalla domus e ti ritrovi sulla Via Sacra, una delle strade
    principali di Roma. È affollata anche a quest'ora del pomeriggio.

    Mercanti vendono ceramiche, tessuti, spezie dall'Oriente.
    "Olive! Olive fresche da Hispania!" grida un venditore.
    Schiavi portano lettighe con nobili all'interno.
    Un gruppo di soldati marcia verso la caserma.

    L'odore è un misto di profumi: pane appena sfornato, olio d'oliva,
    spezie, ma anche sporcizia urbana e sudore di moltitudine.

    Roma è viva, pulsante, caotica. Ma oggi c'è qualcosa nell'aria...
    una tensione. Le persone sussurrano. Gli sguardi sono nervosi.

    A nord puoi vedere il Foro Romano. A est c'è una taberna (taverna).
    La domus di Brutus è a nord.
    """,
    short_desc="Via Sacra affollata di romani. Foro nord, taberna est, domus nord."
)

foro = Room(
    name="Foro Romano",
    description="""
    Il Foro Romano, il cuore pulsante di Roma. Templi maestosi si
    ergono ai lati: il Tempio di Saturno, il Tempio di Vesta con
    le Vestali che custodiscono il fuoco sacro.

    La Rostra, la tribuna degli oratori, domina la piazza. Da lì
    Cicerone ha pronunciato le sue Filippiche. Da lì Cesare ha
    parlato al popolo.

    Gruppi di senatori in toga discutono animatamente. Riconosci
    alcuni volti: Marco Antonio, fedele di Cesare, parla con un
    gruppo di veterani. Cassio Longino, con la sua faccia scavata
    e gli occhi cupi, fissa la Curia in lontananza.

    Un'aquila vola sopra i templi. Un presagio? I romani credono
    molto negli omen.

    La Via Sacra è a sud. A ovest ci sono le Terme.
    """,
    short_desc="Foro Romano con templi e senatori. Vie ovest (Terme), sud (Via Sacra)."
)

taberna = Room(
    name="Taberna (Taverna)",
    description="""
    Entri in una taberna tipica di Roma. Piccola, rumorosa, piena
    di fumo di lucerne e odore di vino. Uomini seduti su sgabelli
    bevono, giocano a dadi, chiacchierano.

    Il taverniere, un uomo grasso con grembiule macchiato, versa
    vino annacquato in coppe di terracotta. Sul bancone: olive,
    pane, formaggio, pesci salati.

    Agli angoli, conversazioni sussurrate. Questo è il tipo di posto
    dove si sentono pettegolezzi, voci, segreti. Il tipo di posto
    dove un uomo attento può imparare molto.

    Un gruppo di veterani parla di Cesare. Un mercante si lamenta
    delle tasse. Un mendicante chiede spiccioli.

    La Via Sacra è a ovest.
    """,
    short_desc="Taverna rumorosa con bevitori e pettegolezzi."
)

terme = Room(
    name="Thermae (Terme)",
    description="""
    Le terme pubbliche sono affollate come sempre. I romani vengono
    qui non solo per lavarsi, ma per socializzare, fare affari,
    sentire notizie.

    Il calidarium (stanza calda) è pieno di vapore. Uomini nudi
    conversano nella piscina. Schiavi strofinano i clienti con
    lo strigile (raschietto) per rimuovere sudore e olio.

    Nel frigidarium (stanza fredda) altri si immergono in acqua
    gelida. Le voci riechegiano sulle pareti di marmo.

    Senatori si mescolano con mercanti, soldati con artigiani.
    Qui le gerarchie sociali si allentano - tutti sono nudi.

    Nelle terme si ascoltano i segreti di Roma...

    Il Foro è a est.
    """,
    short_desc="Terme pubbliche piene di vapore e conversazioni."
)

# ============================================================================
# OGGETTI - INDIZI E PUZZLE
# ============================================================================

# --- LETTERA CIFRATA (oggetto chiave) ---

lettera_cifrata = Item(
    name="lettera",
    description="""
    Una lettera scritta su papiro di buona qualità, sigillata con
    cera rossa. Il sigillo mostra un pugnale - un simbolo insolito.

    Il testo è in latino, ma alcune parole sono cifrate. Riconosci
    la cifra di Cesare! Ironico che sia usata contro di lui...

    Nella cifra di Cesare, ogni lettera è sostituita con quella
    tre posizioni dopo nell'alfabeto (A→D, B→E, etc.).
    """,
    can_take=True,
    aliases=["papiro", "documento", "missiva"]
)

def leggi_lettera_cifrata(game, item):
    game.state["lettera_letta"] = True
    return """
    Leggi attentamente la lettera, decifrando le parti cifrate:

    ─────────────────────────────────────────────────────────────

    "Fratres in libertatem,

    LGXVWB PDUFLB, alle IDI DI MARZO, nella CXULD GL SRPSHB.
    Il tiranno cadrà. EUXWXV et FDVVLXV hanno raccolto i consensi.
    Venti e tre senatori sono pronti.

    Le VWHOOH hanno parlato. L'DUXVSH non ha ascoltato.
    Domani Roma sarà di nuovo libera.

    Per RPQLEXV WBUDQQLV!

    - Amicus Libertatis"

    ─────────────────────────────────────────────────────────────

    Decifrando (con spostamento -3):
    - LGXVWB PDUFLB = IDIBUS MARTIIS (Idi di Marzo)
    - CXULD GL SRPSHB = CURIA DI POMPEO
    - EUXWXV = BRUTUS
    - FDVVLXV = CASSIUS
    - VWHOOH = STELLE (riferimento agli aruspici)
    - DUXVSH = ARUSPICE
    - RPQLEXV WBUDQQLV = OMNIBUS TYRANNIS (a tutti i tiranni)

    Il messaggio è chiaro: un complotto per uccidere Cesare domani
    alle Idi di Marzo, nella Curia di Pompeo. Guidato da Bruto
    e Cassio, con ventitre senatori congiurati.

    Senti un brivido lungo la schiena. Questo è alto tradimento.
    E tu, ora, sei a conoscenza del complotto...

    Cosa farai?
    """

lettera_cifrata.add_action("leggi", leggi_lettera_cifrata)
lettera_cifrata.add_action("decifra", leggi_lettera_cifrata)
lettera_cifrata.add_action("usa", leggi_lettera_cifrata)

# --- CASSETTA CHIUSA (nella biblioteca) ---

cassetta = Item(
    name="cassetta",
    description="""
    Una piccola cassetta di legno di cedro, finemente intarsiata.
    Ha un lucchetto di bronzo. Pesa abbastanza - c'è qualcosa dentro.

    Il lucchetto non è complicato, ma forzarlo sarebbe evidente.
    Forse c'è una chiave da qualche parte?
    """,
    can_take=False,
    aliases=["scatola", "cofanetto"]
)

def apri_cassetta(game, item):
    chiave = game.find_item_in_inventory("chiave bronzo")

    if not chiave:
        return """
        La cassetta è chiusa con un lucchetto di bronzo. Potresti
        forzarlo, ma il senatore se ne accorgerebbe. Ti serve la chiave.
        """

    if game.state.get("cassetta_aperta"):
        return "La cassetta è già aperta."

    game.state["cassetta_aperta"] = True

    # Aggiungi la lettera cifrata
    biblioteca_room = game.get_room("biblioteca")
    if biblioteca_room:
        biblioteca_room.add_item(lettera_cifrata)

    return """
    Usi la chiave di bronzo. Il lucchetto si apre con un click.

    All'interno della cassetta trovi diversi documenti:
    - Lettere tra senatori
    - Una lista di nomi
    - Una lettera sigillata con un simbolo strano: un pugnale

    Prendi la lettera sigillata. Le tue mani tremano...
    """

cassetta.add_action("apri", apri_cassetta)
cassetta.add_action("usa", apri_cassetta)

# --- CHIAVE DI BRONZO (nascosta) ---

chiave_bronzo = Item(
    name="chiave bronzo",
    description="""
    Una piccola chiave di bronzo, nascosta sotto un rotolo.
    Ha la forma giusta per aprire la cassetta nella biblioteca.
    """,
    can_take=True,
    aliases=["chiave", "chiavetta"]
)

# --- DE BELLO GALLICO (libro di Cesare) ---

de_bello_gallico = Item(
    name="de bello gallico",
    description="""
    "Commentarii de Bello Gallico" - I Commentari sulla Guerra Gallica,
    scritti da Giulio Cesare stesso. L'opera è aperta sul leggio.

    Leggi un passaggio famoso:
    "Gallia est omnis divisa in partes tres..."
    (Tutta la Gallia è divisa in tre parti...)

    L'ironia ti colpisce: stai leggendo le parole di un uomo che
    potrebbe morire domani. Un uomo che ha conquistato terre lontane
    ma non vede il pericolo nella sua stessa città.
    """,
    can_take=False,
    aliases=["libro", "commentarii", "rotolo"]
)

def leggi_de_bello(game, item):
    # Se leggi attentamente, trovi la chiave nascosta tra le pagine
    if not game.state.get("chiave_trovata"):
        game.state["chiave_trovata"] = True
        biblioteca_room = game.get_room("biblioteca")
        if biblioteca_room:
            biblioteca_room.add_item(chiave_bronzo)

        return """
        Mentre sfoglia il rotolo, qualcosa cade sul pavimento con
        un tintinnio metallico. Una chiave di bronzo! Era nascosta
        tra le pagine.

        Il senatore Brutus doveva averla messa lì per non perderla.
        """
    else:
        return "I commentari di Cesare sulle sue campagne galliche. Opera storica fondamentale."

de_bello_gallico.add_action("leggi", leggi_de_bello)
de_bello_gallico.add_action("sfoglia", leggi_de_bello)
de_bello_gallico.add_action("usa", leggi_de_bello)

# --- TAVOLETTA DI CERA (per scrivere) ---

tavoletta = Item(
    name="tavoletta",
    description="""
    Una tavoletta di legno ricoperta di cera scura. Su questa si
    scrive con uno stilo, incidendo la cera. Si può cancellare
    lisciando la cera con il lato piatto dello stilo.

    È il tuo strumento di lavoro quotidiano.
    """,
    can_take=True,
    aliases=["tabula", "cera"]
)

def usa_tavoletta(game, item):
    if game.state.get("lettera_letta"):
        return """
        Hai già tutte le informazioni importanti. Cosa vorresti
        scrivere sulla tavoletta?

        (In un gioco più complesso, qui potresti comporre un
        messaggio da mandare a Cesare...)
        """
    else:
        return "Scrivi e cancelli pensieri casuali sulla cera. Nulla di importante."

tavoletta.add_action("usa", usa_tavoletta)
tavoletta.add_action("scrivi", usa_tavoletta)

# --- DENARIUS (moneta) ---

denarius = Item(
    name="denarius",
    description="""
    Un denarius d'argento. Sul dritto c'è il profilo di Cesare con
    la corona d'alloro. Sul retro, simboli del suo potere.

    È controverso che Cesare abbia messo la sua faccia sulle monete
    mentre è ancora vivo - un gesto che molti senatori considerano
    monarchico, da re. A Roma, la parola "re" è un insulto.

    Questa moneta è una delle ragioni per cui lo odiano...
    """,
    can_take=True,
    aliases=["moneta", "denaro", "argento"]
)

# --- TESSERA LIBERTATIS (certificato di libertà) ---

tessera = Item(
    name="tessera",
    description="""
    La tua tessera libertatis, il certificato che prova la tua
    libertà. Senza questo documento, saresti ancora uno schiavo.

    C'è scritto:

    "MARCUS VERUS, servus, est nunc LIBER per voluntatem
    DECIMI BRUTI ALBINI. Anno DCCX ab Urbe Condita."

    (Marcus Verus, schiavo, è ora LIBERO per volontà di
    Decimus Brutus Albinus. Anno 710 dalla Fondazione di Roma.)

    Il tuo bene più prezioso. La tua libertà.
    """,
    can_take=False,  # È appesa al muro
    aliases=["certificato", "documento libertà"]
)

# ============================================================================
# NPC - PERSONAGGI STORICI
# ============================================================================

# --- DECIMUS BRUTUS (padrone, congiurato) ---

decimus = NPC(
    name="decimus",
    description="""
    Decimus Brutus Albinus, tuo padrone e senatore di Roma. Un uomo
    sulla quarantina, atletico, con la toga perfettamente drappeggiata.
    Ha il volto di chi ha visto molte battaglie - è stato generale
    nelle campagne di Cesare.

    Ma oggi il suo volto è teso. I suoi occhi evitano i tuoi.
    Qualcosa lo tormenta.
    """,
    aliases=["brutus", "senatore", "padrone", "decimo"],
    dialogue={
        'default': """
        Marcus, hai finito di copiare le lettere che ti ho lasciato?
        Bene, bene. Domani... domani sarà un giorno importante.
        Il Senato si riunisce. Potrebbero esserci... cambiamenti.

        *Ti guarda intensamente*

        Tu sei un uomo intelligente, Marcus. Troppo intelligente,
        forse. Ricorda: ciò che vedi e senti in questa casa,
        resta in questa casa. La tua libertà... è preziosa. Non
        metterla a rischio facendo domande pericolose.

        Capisci?
        """,
        'dopo_lettera': """
        *Ti fissa con occhi acuti*

        Vedo nei tuoi occhi che sai qualcosa. Sai, vero?

        Allora ascolta bene, Marcus. Roma è sull'orlo del baratro.
        Cesare si è proclamato dittatore perpetuo. PERPETUO! Vuole
        essere re in tutto tranne che nel nome.

        I nostri antenati hanno cacciato i re 500 anni fa. Non
        permetteremo che tornino. Domani... domani faremo ciò che
        deve essere fatto. Per Roma. Per la Repubblica.

        Tu cosa farai, Marcus? Sei con noi... o contro di noi?
        """,
        'finale': """
        Hai fatto la tua scelta. Ora dobbiamo vivere con le
        conseguenze. La storia ci giudicherà.
        """
    }
)

def parla_decimus_callback(game, npc):
    if game.state.get("scelta_fatta"):
        npc.set_dialogue_state('finale')
    elif game.state.get("lettera_letta"):
        npc.set_dialogue_state('dopo_lettera')
    else:
        npc.set_dialogue_state('default')

decimus.on_talk = parla_decimus_callback

# --- CASSIO LONGINO (congiurato principale) ---

cassius = NPC(
    name="cassius",
    description="""
    Gaius Cassius Longinus. Un uomo magro dal volto scavato e occhi
    intensi, quasi fanatici. Veterano delle guerre, ma soprattutto
    un idealista repubblicano fanatico.

    Lo vedi alle Terme, immerso nel calidarium. Anche qui, il suo
    volto è cupo, perso in pensieri profondi.
    """,
    aliases=["gaius", "longino"],
    dialogue={
        'default': """
        *Ti guarda sospettoso*

        Tu sei lo scriba di Decimus, vero? Cosa ci fai qui?

        *Pausa*

        Beh, non importa. Domani saprai tutto. Domani Roma sarà
        di nuovo libera. Il tiranno cadrà, e la Repubblica rinascerà.

        Cesare pensa di essere un dio. Domani scoprirà di essere
        fatto di carne e sangue come tutti noi.

        *Ride amaramente*

        Ventitre pugnali glielo dimostreranno.
        """,
        'dopo_lettera': """
        Ah, quindi sai. Decimus ti ha parlato?

        Bene. Allora sappi questo: ciò che facciamo, lo facciamo
        per Roma. Non per ambizione personale. Per la LIBERTÀ.

        Cesare deve morire. È l'unico modo.

        Se hai dubbi, pensa a questo: preferisci vivere in ginocchio
        davanti a un re, o in piedi come cittadino libero?

        La risposta è ovvia.
        """
    }
)

def parla_cassius_callback(game, npc):
    if game.state.get("lettera_letta"):
        npc.set_dialogue_state('dopo_lettera')

cassius.on_talk = parla_cassius_callback

# --- VETERANO (soldato fedele a Cesare) ---

veterano = NPC(
    name="veterano",
    description="""
    Un vecchio soldato con cicatrici sul volto e mani callose.
    Indossa una tunica militare semplice. È chiaro che ha combattuto
    nelle legioni di Cesare in Gallia.

    Beve vino nella taberna, circondato da altri veterani.
    """,
    aliases=["soldato", "legionario"],
    dialogue={
        'default': """
        Cesare? Il miglior generale che Roma abbia mai avuto!

        *Batte il pugno sul tavolo*

        Ho combattuto con lui in Gallia. L'ho visto attraversare
        il Rubicone. L'ho visto sconfiggere Pompeo. È un DIO tra
        gli uomini!

        E questi senatori viziati osano criticarlo? Loro che non
        hanno mai tenuto una spada, mai dormito sotto le stelle,
        mai versato sangue per Roma?

        Se qualcuno osasse fare del male a Cesare, noi veterani
        faremmo scorrere fiumi di sangue per vendicarlo. FIUMI.

        Ricordatelo.
        """,
        'avvertimento': """
        *Ti guarda serio*

        Dici che c'è un complotto? Contro CESARE?

        *Si alza di scatto*

        Dove? Chi? Parla!

        Se dici la verità, devo avvertire il comandante. Se menti...
        pagherai caro per aver diffuso voci false.

        Sei sicuro di quello che dici?
        """
    }
)

def parla_veterano_callback(game, npc):
    if game.state.get("avverti_veterani"):
        npc.set_dialogue_state('avvertimento')

veterano.on_talk = parla_veterano_callback

# --- CALPURNIA (moglie di Cesare) - NPC opzionale ---

calpurnia = NPC(
    name="calpurnia",
    description="""
    Calpurnia, moglie di Giulio Cesare. Una donna elegante sulla
    quarantina, con una stola (veste) di lino finissimo e gioielli d'oro.

    Ha gli occhi rossi, come se avesse pianto. Il suo volto è
    pallido, preoccupato.
    """,
    aliases=["moglie", "donna"],
    dialogue={
        'default': """
        *Ti guarda con occhi supplichevoli*

        Tu... tu servi un senatore, vero? Forse puoi aiutarmi.

        Ho fatto un sogno terribile stanotte. Ho visto mio marito,
        Gaius Julius, coperto di sangue. Pugnalato. Morente.
        Mi supplicava aiuto con le mani tese...

        *Lacrime le rigano le guance*

        Ho paura. Una paura profonda. Gli ho chiesto di non andare
        al Senato domani. Ma lui... lui non ascolta mai i presagi.
        Ride dei sogni, degli aruspici, dei prodigi.

        Ma io SO. So che qualcosa di terribile sta per accadere.

        Se... se senti qualcosa, qualsiasi cosa che riguardi mio
        marito... ti prego, avvertimi. Ti prego.
        """,
        'avvertita': """
        *Afferra le tue mani*

        Grazie. GRAZIE. Devo andare da lui subito. Devo convincerlo
        a non andare al Senato domani. Devo...

        Che gli dei ti benedicano, straniero. Mi hai salvato.
        Forse... forse hai salvato Roma stessa.
        """
    }
)

def parla_calpurnia_callback(game, npc):
    if game.state.get("avverti_calpurnia"):
        npc.set_dialogue_state('avvertita')

calpurnia.on_talk = parla_calpurnia_callback

# ============================================================================
# SISTEMA DI SCELTE E FINALI MULTIPLI
# ============================================================================

def scelta_finale():
    """Gestisce la scelta finale del giocatore."""
    print("\n" + "═"*70)
    print("                    MOMENTO DELLA SCELTA")
    print("═"*70)
    print("""
Ora conosci il complotto. Domani, alle Idi di Marzo, ventitre
senatori guidati da Bruto e Cassio uccideranno Giulio Cesare
nella Curia di Pompeo.

Cosa farai?

1. AVVERTIRE CESARE
   Puoi parlare con Calpurnia, sua moglie, che ti ha implorato di
   aiutarla. Lei convincerà Cesare a non andare al Senato.
   La storia cambierà. Ma i congiurati potrebbero vendicarsi su di te.

2. RIMANERE IN SILENZIO
   Puoi non fare nulla. Lasciare che la storia faccia il suo corso.
   Cesare morirà, la Repubblica... forse rinascerà. O forse scoppierà
   una guerra civile. Non è affare tuo. Tu sei solo uno scriba.

3. AVVERTIRE I VETERANI
   Puoi dire ai veterani fedeli a Cesare del complotto. Loro arresteranno
   i congiurati. Ma sarà un bagno di sangue. E tu sarai un traditore per
   il tuo padrone Decimus, che ti ha dato la libertà.

Cosa scegli? (1/2/3)
    """)
    print("═"*70 + "\n")

# Oggetto finale speciale per attivare la scelta

scelta_finale_obj = Item(
    name="scelta",
    description="Il momento di decidere il destino di Roma.",
    can_take=False,
    visible=False
)

def usa_scelta(game, item):
    if not game.state.get("lettera_letta"):
        return "Non hai ancora scoperto il complotto."

    if game.state.get("scelta_fatta"):
        return "Hai già fatto la tua scelta."

    scelta_finale()

    # Aspetta input del giocatore
    risposta = input("La tua scelta (1, 2 o 3): ").strip()

    game.state["scelta_fatta"] = True

    if risposta == "1":
        # Avverte Cesare
        game.state["scelta"] = "cesare"
        game.state["avverti_calpurnia"] = True

        # Sposta Calpurnia al Foro se non c'è già
        foro_room = game.get_room("foro")
        if foro_room and calpurnia not in foro_room.npcs:
            foro_room.add_npc(calpurnia)

        return """
        Hai deciso: avvertirai Cesare attraverso Calpurnia.

        È rischioso. Se i congiurati scopriranno che sei stato tu...
        Ma non puoi permettere che un omicidio accada mentre tu
        sapevi e non hai fatto nulla.

        VAI AL FORO. Troverai Calpurnia lì. Parlale.
        """

    elif risposta == "2":
        # Rimane in silenzio
        game.state["scelta"] = "silenzio"
        game.game_won = True

        return """
        Hai deciso: rimarrai in silenzio.

        ═══════════════════════════════════════════════════════════

                            EPILOGO - SILENZIO

        ═══════════════════════════════════════════════════════════

        Non fai nulla. Bruci la lettera. Continui la tua vita.

        Il giorno dopo, 15 marzo 44 a.C., Giulio Cesare va al Senato
        nonostante gli avvertimenti di Calpurnia e degli aruspici.

        Nella Curia di Pompeo, ventitre senatori lo circondano.
        Ventitre pugnali lo colpiscono. 23 ferite.

        Cade ai piedi della statua di Pompeo, suo vecchio nemico.
        Le sue ultime parole, secondo alcuni, sono:
        "Καὶ σύ, τέκνον;" (Anche tu, figlio?) rivolte a Bruto.

        Cesare è morto. La Repubblica è... salvata?

        No.

        Segue una guerra civile brutale. Marco Antonio e Ottaviano
        (futuro Augusto) vendicheranno Cesare. I congiurati moriranno
        tutti, uno ad uno. Bruto si suiciderà a Filippi.

        E la Repubblica? Non tornerà mai. Ottaviano diventerà Augusto,
        primo imperatore di Roma. L'Impero è nato.

        Tu, Marcus Verus, hai assistito a uno dei momenti cruciali
        della storia. E hai scelto di non interferire.

        Hai fatto la scelta giusta? La storia non può rispondere.
        Solo tu puoi giudicare.

        ═══════════════════════════════════════════════════════════
                            FINE - FINIS
        ═══════════════════════════════════════════════════════════

        Grazie per aver giocato.

        NOTA STORICA: Questo è ciò che è realmente accaduto nella
        storia. Il 15 marzo 44 a.C., Giulio Cesare fu assassinato
        da congiurati repubblicani guidati da Bruto e Cassio.
        La loro azione non salvò la Repubblica, ma portò a guerre
        civili e alla nascita dell'Impero Romano.
        """

    elif risposta == "3":
        # Avverte i veterani
        game.state["scelta"] = "veterani"
        game.state["avverti_veterani"] = True

        return """
        Hai deciso: avvertirai i veterani di Cesare.

        È la scelta più pericolosa per te. Il tuo padrone Decimus
        è uno dei congiurati. Se scopre che li hai traditi...

        Ma forse salverai Cesare. E forse eviterai una guerra civile.

        VAI ALLA TABERNA. Parla con il veterano.
        """

    else:
        return "Scelta non valida. Riprova con 1, 2 o 3."

scelta_finale_obj.add_action("usa", usa_scelta)

# ============================================================================
# FINALI ALTERNATIVI
# ============================================================================

def finale_cesare_salvato():
    """Finale dove Cesare viene avvertito."""
    return """
    ═══════════════════════════════════════════════════════════════

                    EPILOGO - LA STORIA CAMBIATA

    ═══════════════════════════════════════════════════════════════

    Calpurnia ti ringrazia con lacrime di gioia. Corre da Cesare
    e, con le tue informazioni, finalmente lo convince.

    Il 15 marzo 44 a.C., Giulio Cesare NON va al Senato.
    Manda un messaggio dicendo di essere malato.

    I congiurati sono sconcertati. Aspettano nella Curia di Pompeo,
    pugnali nascosti nelle toghe. Ma Cesare non arriva.

    Nei giorni seguenti, Cesare, ora allertato, fa arrestare
    discretamente i principali congiurati. Bruto, Cassio, Decimus...
    tutti esiliati o giustiziati.

    Il tuo padrone Decimus Brutus muore in esilio. Prima di partire,
    ti guarda negli occhi. "Tu," dice semplicemente. "Sei stato tu."

    Confermi con un cenno. Non parla più. Parte per non tornare mai.

    Hai salvato Cesare. Ma a che prezzo?

    Cesare vive ancora molti anni. Consolida il suo potere. La
    Repubblica è morta comunque - ma senza guerra civile. Cesare
    diventa, di fatto, il primo imperatore.

    La storia è cambiata. In meglio? In peggio? Non puoi saperlo.

    Tu, Marcus Verus, sei diventato un eroe per i cesariani.
    Cesare stesso ti premia con terre e ricchezze. Sei un uomo
    libero e ricco.

    Ma nelle notti insonni, ti chiedi: ho fatto bene a cambiare
    il corso della storia? Chi sono io per decidere il destino
    di Roma?

    Non c'è risposta.

    ═══════════════════════════════════════════════════════════════
                        FINE ALTERNATIVA - FINIS
    ═══════════════════════════════════════════════════════════════

    NOTA: Questo è un "what if" storico. Nella realtà, Cesare fu
    davvero assassinato il 15 marzo 44 a.C. Questa avventura esplora
    cosa sarebbe potuto accadere se...

    Grazie per aver giocato!
    """

def finale_veterani():
    """Finale dove i veterani arrestano i congiurati."""
    return """
    ═══════════════════════════════════════════════════════════════

                    EPILOGO - SANGUE NEL FORO

    ═══════════════════════════════════════════════════════════════

    Il veterano ti crede. Raduna i suoi compagni d'armi.

    La notte tra il 14 e il 15 marzo, soldati fedeli a Cesare
    irrompono nelle case dei congiurati. Arresti di massa.
    Bruto, Cassio, Decimus, tutti gli altri.

    Ventitre senatori arrestati. Alcuni cercano di resistere.
    C'è un bagno di sangue. Il Foro si tinge di rosso.

    Cesare, informato del complotto, ordina esecuzioni immediate.
    Nessun processo. La giustizia militare è rapida e brutale.

    Il tuo padrone Decimus ti vede tra i soldati. Capisce.
    Le sue ultime parole prima dell'esecuzione:
    "Traditore. Ti avevo dato la libertà..."

    Cesare è salvo. Ma Roma è sconvolta. Il Senato è decimato.
    I cittadini sono divisi tra sostenitori e oppositori.

    Hai evitato l'assassinio di Cesare, ma hai scatenato una
    repressione terribile. Centinaia di sospetti repubblicani
    vengono arrestati nei mesi seguenti.

    La paura regna su Roma.

    Cesare vive, ma governa con pugno di ferro. La Repubblica
    è definitivamente morta. E tu ne sei complice.

    Ti premiano come eroe. Ma di notte, sogni i volti dei
    condannati. Sogni Decimus che ti chiama traditore.

    Hai salvato un uomo. Ma a che prezzo?

    ═══════════════════════════════════════════════════════════════
                        FINE ALTERNATIVA - FINIS
    ═══════════════════════════════════════════════════════════════

    NOTA: Questo è un "what if" storico basato su una scelta
    più violenta. La storia reale vide l'assassinio di Cesare
    senza preavvisi efficaci.

    Grazie per aver giocato!
    """

# Aggiungi callback per i finali alternativi
def controlla_finale_alternativo():
    """Controlla se è stato raggiunto un finale alternativo."""
    if game.state.get("scelta") == "cesare" and game.state.get("parlato_calpurnia_finale"):
        game.game_won = True
        print(finale_cesare_salvato())

    elif game.state.get("scelta") == "veterani" and game.state.get("parlato_veterano_finale"):
        game.game_won = True
        print(finale_veterani())

# Override del comando parla per gestire finali
original_talk = game.cmd_talk

def custom_talk(parsed):
    result = original_talk(parsed)

    # Controlla se ha parlato con Calpurnia dopo la scelta
    if game.state.get("scelta") == "cesare":
        if "calpurnia" in parsed.get("target", "").lower():
            game.state["parlato_calpurnia_finale"] = True
            controlla_finale_alternativo()

    # Controlla se ha parlato con veterano dopo la scelta
    elif game.state.get("scelta") == "veterani":
        if "veterano" in parsed.get("target", "").lower() or "soldato" in parsed.get("target", "").lower():
            game.state["parlato_veterano_finale"] = True
            controlla_finale_alternativo()

    return result

game.cmd_talk = custom_talk

# ============================================================================
# SETUP GIOCO
# ============================================================================

# Aggiungi stanze
game.add_room("atrium", atrium)
game.add_room("tablinum", tablinum)
game.add_room("cubiculum", cubiculum)
game.add_room("triclinium", triclinium)
game.add_room("peristilium", peristilium)
game.add_room("biblioteca", biblioteca)
game.add_room("via", via)
game.add_room("foro", foro)
game.add_room("taberna", taberna)
game.add_room("terme", terme)

# Collegamenti - Domus
game.connect_rooms("atrium", "nord", "tablinum", bidirectional=True)
game.connect_rooms("atrium", "est", "cubiculum", bidirectional=True)
game.connect_rooms("atrium", "ovest", "triclinium", bidirectional=True)
game.connect_rooms("tablinum", "nord", "peristilium", bidirectional=True)
game.connect_rooms("peristilium", "est", "biblioteca", bidirectional=True)
game.connect_rooms("atrium", "sud", "via", bidirectional=True)

# Collegamenti - Roma esterna
game.connect_rooms("via", "nord", "foro", bidirectional=True)
game.connect_rooms("via", "est", "taberna", bidirectional=True)
game.connect_rooms("foro", "ovest", "terme", bidirectional=True)

# Aggiungi oggetti
cubiculum.add_item(tessera)
cubiculum.add_item(tavoletta)
cubiculum.add_item(denarius)
tablinum.add_item(scelta_finale_obj)
biblioteca.add_item(cassetta)
biblioteca.add_item(de_bello_gallico)

# Aggiungi NPC
tablinum.add_npc(decimus)
terme.add_npc(cassius)
taberna.add_npc(veterano)
# Calpurnia appare al foro solo se scegli di avvertirla

# Punto di partenza
game.set_start("cubiculum")

# ============================================================================
# AVVIO
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("LE IDI DI MARZO - Un Complotto a Roma")
    print("="*70)
    print("\nAvventura storica ambientata nell'Antica Roma, 44 a.C.")
    print("\nOBIETTIVO: Scopri il complotto e decidi il destino di Roma.")
    print("\nCARATTERISTICHE:")
    print("- Personaggi storici reali (Bruto, Cassio, Cesare)")
    print("- Riferimenti storici accurati")
    print("- Puzzle basati su cultura romana (cifra di Cesare)")
    print("- Finali multipli basati sulle tue scelte")
    print("- Dilemmi morali complessi")
    print("\nGUIDA RAPIDA:")
    print("1. Esplora la domus (casa) del senatore Brutus")
    print("2. Trova e leggi 'de bello gallico' nella biblioteca")
    print("3. Prendi la chiave che cade dal libro")
    print("4. Apri la cassetta con la chiave")
    print("5. Leggi e decifra la lettera")
    print("6. Usa il comando 'usa scelta' nel tablinum")
    print("7. Scegli il destino di Roma!")
    print("\nNOTA STORICA:")
    print("Il 15 marzo 44 a.C. (le Idi di Marzo), Giulio Cesare fu")
    print("assassinato da un gruppo di senatori nella Curia di Pompeo.")
    print("Questa avventura esplora quel momento cruciale della storia.")
    print("="*70 + "\n")

    game.start()
