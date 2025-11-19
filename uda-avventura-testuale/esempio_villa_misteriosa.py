"""
IL MISTERO DELLA VILLA ABBANDONATA
===================================

Avventura testuale completa che dimostra tutte le caratteristiche
del motore: mappa, descrizioni atmosferiche, oggetti interattivi,
puzzle, NPC e dialoghi.

GENERE: Giallo/Investigativo
DURATA: 20-30 minuti
DIFFICOLTÀ: Media

STORIA:
Sei un detective privato chiamato a investigare la misteriosa
scomparsa del Professor Blackwood, un ricco studioso che viveva
in una villa isolata. La polizia non ha trovato nulla, ma la
famiglia sospetta qualcosa di sinistro...
"""

from text_adventure_engine import Game, Room, Item, NPC

# ============================================================================
# CREAZIONE GIOCO
# ============================================================================

game = Game(
    title="Il Mistero della Villa Abbandonata",
    author="Sistema Didattico - Esempio Completo",
    intro="""
    La pioggia batte incessante mentre il tuo taxi si allontana,
    lasciandoti davanti ai cancelli arrugginiti della Villa Blackwood.
    Il tuo impermeabile ti protegge a malapena dall'acquazzone mentre
    osservi l'imponente struttura vittoriana che si staglia contro
    il cielo plumbeo.

    Sei il detective Morgan, specializzato in casi irrisolti. La famiglia
    Blackwood ti ha assunto dopo che la polizia ha archiviato il caso
    della scomparsa del Professor Edmund Blackwood come "allontanamento
    volontario". Ma qualcosa non torna. Un uomo brillante, all'apice
    della carriera, con una famiglia che lo ama... perché dovrebbe
    sparire senza lasciare traccia?

    Le finestre della villa sono buie, le imposte chiuse. Un brivido
    ti percorre la schiena - e non è per il freddo. Con una mano sulla
    tua torcia elettrica, spingi il cancello. Cigola in modo inquietante.

    È tempo di scoprire la verità...
    """
)

# ============================================================================
# STANZE CON DESCRIZIONI DETTAGLIATE
# ============================================================================

# --- ESTERNO ---

vialetto = Room(
    name="Vialetto d'Ingresso",
    description="""
    Il vialetto di ghiaia conduce dalla strada al portico della villa.
    Erbacce crescono tra le pietre, segno che nessuno se ne prende cura
    da tempo. Alberi spogli si ergono ai lati come guardiani silenziosi,
    i loro rami nudi graffiano il cielo grigio.

    La villa davanti a te è una struttura vittoriana a tre piani,
    costruita in pietra scura che sembra assorbire la poca luce
    disponibile. Le finestre sono occhi ciechi, le imposte chiuse
    le fanno sembrare palpebre serrate.

    Il portico è a nord. Il cancello da cui sei entrato è a sud.
    """,
    short_desc="Vialetto tra alberi spogli. Villa a nord, cancello a sud."
)

portico = Room(
    name="Portico",
    description="""
    Il portico è coperto da un tetto sostenuto da colonne di marmo,
    ora macchiate dalla pioggia e dal tempo. Foglie morte si accumulano
    negli angoli, formando cumuli umidi. Il pavimento di pietra è
    scivoloso per l'acqua che gocciola dalle grondaie rotte.

    La porta d'ingresso è imponente: legno massiccio di quercia scura
    con intarsi metallici ormai ossidati. Ha una maniglia di ottone
    appannato e una serratura antica. Sorprendentemente, la porta
    sembra socchiusa.

    Il vialetto è a sud. La porta conduce a nord, all'interno.
    """,
    short_desc="Portico coperto con porta d'ingresso socchiusa."
)

# --- PIANO TERRA ---

ingresso = Room(
    name="Ingresso Principale",
    description="""
    Entri in un ampio ingresso che un tempo doveva essere maestoso.
    Un lampadario di cristallo pende dal soffitto alto, coperto di
    polvere e ragnatele. La luce della tua torcia si riflette nei
    cristalli, creando riflessi spettrali sulle pareti.

    Una scala di marmo con ringhiera di ferro battuto sale verso i
    piani superiori, curvandosi elegantemente. Il corrimano è coperto
    di polvere - nessuno l'ha toccato da settimane. Ai piedi della
    scala c'è un tappeto persiano scolorito.

    Porte si aprono in varie direzioni: a ovest il salone, a est
    la biblioteca, a nord sembra esserci un corridoio. La porta
    d'uscita è a sud. La scala sale verso l'alto.

    L'odore di chiuso e polvere permea l'aria. Ogni tuo passo
    risuona nel silenzio tombale.
    """,
    short_desc="Ingresso con lampadario e scala di marmo. Porte ovest, est, nord."
)

salone = Room(
    name="Salone",
    description="""
    Il salone è una stanza vasta con soffitti alti e pareti rivestite
    di pannelli di legno scuro. Mobili coperti da teli bianchi
    sembrano fantasmi nella penombra. La tua torcia rivela divani,
    poltrone e tavolini dalle forme distorte sotto i lenzuoli.

    Un camino di marmo nero domina la parete ovest. È freddo e vuoto,
    ma ceneri recenti giacciono nella griglia. Qualcuno ha acceso un
    fuoco qui, e non molto tempo fa.

    Sulla mensola del camino ci sono cornici con fotografie di famiglia
    e alcuni soprammobili. Un grande specchio appeso sopra il camino
    riflette la stanza, moltiplicando le ombre.

    Finestre alte danno sul giardino laterale, ma le imposte chiuse
    bloccano ogni luce esterna. Si può tornare a est verso l'ingresso.
    """,
    short_desc="Salone con mobili coperti e camino di marmo nero."
)

biblioteca = Room(
    name="Biblioteca",
    description="""
    Entri in una biblioteca che toglie il fiato. Scaffali di legno
    scuro si estendono dal pavimento al soffitto su tutte le pareti,
    stracolmi di libri di ogni dimensione. Una scala a pioli
    scorrevole permette di raggiungere i volumi più alti.

    Al centro della stanza c'è una grande scrivania di mogano, coperta
    di carte, libri aperti e strani strumenti. Sembra che qualcuno
    stesse lavorando qui e si sia alzato all'improvviso, lasciando
    tutto com'era.

    L'odore di carta vecchia e cuoio è forte. La polvere danza nella
    luce della torcia come lucciole impazzite. Su una parete, tra
    gli scaffali, noti uno strano dipinto che sembra fuori posto.

    Una porta a est conduce a quello che sembra uno studio privato.
    L'ingresso è a ovest.
    """,
    short_desc="Biblioteca ricca di libri con scrivania centrale. Porta a est."
)

studio = Room(
    name="Studio Privato",
    description="""
    Lo studio privato del Professor Blackwood. È una stanza più piccola
    e intima della biblioteca, chiaramente il suo rifugio personale.
    Pareti rivestite di legno scuro creano un'atmosfera raccolta.

    Una poltrona di pelle consumata è posizionata vicino a una
    finestra, con un tavolino accanto su cui giacciono una pipa e
    un libro aperto. La poltrona ha ancora l'impronta di qualcuno
    seduto, come se il professore si fosse appena alzato.

    Mensole piene di tomi antichi e oggetti curiosi: una clessidra,
    un globo terrestre, strani congegni meccanici. Su una parete
    c'è una cassaforte di ferro, chiusa. Sopra la cassaforte, una
    targa recita: "La verità è nelle stelle".

    Si può tornare a ovest verso la biblioteca.
    """,
    short_desc="Studio privato con poltrona di pelle e cassaforte."
)

corridoio = Room(
    name="Corridoio",
    description="""
    Un lungo corridoio si estende da est a ovest. Ritratti di
    famiglia pendono dalle pareti - antenati dei Blackwood che
    ti fissano con occhi severi dai loro pesanti cornici dorate.

    Il pavimento di legno scricchiola sotto i tuoi passi. Alcune
    assi sono allentate. La carta da parati floreale si sta
    staccando in più punti, rivelando l'intonaco sottostante.

    A est c'è una porta chiusa - la cucina. A ovest il corridoio
    finisce in una porta che sembra condurre a una serra. A sud
    puoi tornare all'ingresso.
    """,
    short_desc="Corridoio con ritratti. Cucina a est, serra a ovest."
)

cucina = Room(
    name="Cucina",
    description="""
    La cucina è sorprendentemente moderna per una villa così antica.
    Elettrodomestici in acciaio inox brillano debolmente alla luce
    della torcia. Ma c'è qualcosa di inquietante: piatti sporchi
    nel lavello, cibo andato a male sul tavolo, una tazza di caffè
    con muffa verde che vi galleggia.

    È chiaro che qualcuno stava facendo colazione - e si è fermato
    di colpo. Il pane è ancora nel tostapane. Il latte, marcio, è
    fuori dal frigorifero. Come se il tempo si fosse fermato a
    metà di una mattina normale.

    Una porta sul retro conduce al giardino (nord). Il corridoio
    è a ovest.
    """,
    short_desc="Cucina moderna con colazione interrotta. Giardino a nord."
)

serra = Room(
    name="Serra",
    description="""
    La serra è attaccata alla villa sul lato ovest. Grandi pannelli
    di vetro formano il soffitto e le pareti, anche se molti sono
    incrinati o rotti. La pioggia gocciola attraverso le crepe,
    formando pozzanghere sul pavimento di piastrelle.

    Piante esotiche crescono selvagge, non più curate. Rampicanti
    si arrampicano ovunque, alcune piante sono morte, altre sono
    cresciute fuori controllo. L'odore è di terra bagnata e
    vegetazione in decomposizione.

    Tavoli da lavoro sono sparsi di vasi, attrezzi da giardinaggio,
    sacchi di terriccio. In un angolo c'è una piccola scrivania
    con un registro e alcuni documenti.

    Il corridoio è a est. Una porta di vetro conduce al giardino (nord).
    """,
    short_desc="Serra con piante selvagge e tavoli da lavoro."
)

giardino = Room(
    name="Giardino Sul Retro",
    description="""
    Il giardino dietro la villa è stato lasciato andare. Quella che
    un tempo era un'aiuola curata è ora un groviglio di erbacce e
    rovi. Un sentiero di pietra, quasi completamente coperto dalla
    vegetazione, serpeggia tra le piante.

    La pioggia ha trasformato il terreno in fango. Alberi da frutto
    non potati estendono rami nodosi come artigli. In fondo al
    giardino, quasi nascosto da cespugli, intravedi una piccola
    costruzione - sembra un capanno o una rimessa.

    La cucina è a sud. La serra è raggiungibile a sud-ovest.
    Il capanno è a nord, anche se la vegetazione rende difficile
    il passaggio.
    """,
    short_desc="Giardino incolto con sentiero verso un capanno a nord."
)

capanno = Room(
    name="Capanno degli Attrezzi",
    description="""
    Il capanno è piccolo e buio. L'odore di legno marcio e attrezzi
    arrugginiti è forte. Rastrelli, pale e seghe sono appesi alle
    pareti o ammucchiati negli angoli.

    Ma c'è qualcosa di strano. Il pavimento... sembra troppo pulito
    in un angolo. Come se qualcuno avesse spostato qualcosa di recente.
    Infatti, le assi del pavimento in quell'angolo sembrano allentate.

    C'è una botola! Qualcuno ha scavato sotto il capanno.

    Il giardino è a sud.
    """,
    short_desc="Capanno con attrezzi. Botola nel pavimento."
)

# --- SOTTERRANEO ---

sotterraneo = Room(
    name="Sotterraneo Segreto",
    description="""
    Scendi una scala traballante e ti ritrovi in un sotterraneo
    segreto. L'aria è umida e fredda. Le pareti sono di terra
    battuta rinforzata con travi di legno.

    La tua torcia illumina quello che sembra un laboratorio
    improvvisato. Tavoli con provette, microscopi, documenti
    sparsi ovunque. È chiaro che il Professor Blackwood stava
    conducendo esperimenti qui, lontano da occhi indiscreti.

    Su una parete c'è una grande bacheca coperta di foto,
    ritagli di giornale, stringhe che collegano vari elementi.
    Sembra la bacheca di un investigatore ossessionato.

    Una scrivania in un angolo ha un cassetto chiuso a chiave.
    Sopra la scrivania, appeso al muro, c'è un certificato
    incorniciato.

    L'unica via d'uscita è la scala che risale al capanno (su).
    """,
    short_desc="Laboratorio segreto sotterraneo con bacheca investigativa."
)

# ============================================================================
# OGGETTI INTERATTIVI
# ============================================================================

# --- OGGETTI DI INDIZI ---

fotografia = Item(
    name="fotografia",
    description="""
    Una fotografia incorniciata mostra il Professor Blackwood con
    una donna elegante e un ragazzo adolescente. Tutti sorridono.
    Sul retro, scritto a mano: "Edmund, Sarah e James - Estate 1985".

    La famiglia del professore. Ma dove sono ora?
    """,
    can_take=True,
    aliases=["foto", "cornice"]
)

diario = Item(
    name="diario",
    description="""
    Un diario con copertina di pelle consumata. Le ultime pagine
    scritte sono recenti. L'ultima annotazione risale a tre settimane fa.
    """,
    can_take=True,
    aliases=["libro", "taccuino"]
)

def leggi_diario(game, item):
    game.state["diario_letto"] = True
    return """
    Leggi le ultime pagine del diario:

    "10 Marzo - Ho fatto una scoperta incredibile. I documenti che
    ho trovato nella vecchia dimora di mio nonno rivelano la verità
    sulla Stella di Ceylon. Non è solo una leggenda!

    15 Marzo - Qualcuno sta seguendo le mie ricerche. Ho ricevuto
    chiamate anonime. Devo essere più cauto.

    18 Marzo - Ho deciso. Sposterò il mio laboratorio nel sotterraneo
    segreto del capanno. Nessuno saprà. La combinazione della
    cassaforte contiene le coordinate: 3-7-4-2. Le stelle non mentono.

    20 Marzo - Se dovesse succedermi qualcosa, ho lasciato tutto
    in mani fidate. L'ispettore Morrison sa dove guardare."

    Poi... nient'altro. Le pagine seguenti sono bianche.
    """

diario.add_action("leggi", leggi_diario)
diario.add_action("usa", leggi_diario)

# --- OGGETTI INTERATTIVI ---

dipinto = Item(
    name="dipinto",
    description="""
    Un dipinto a olio che raffigura un cielo notturno stellato.
    È stranamente fuori posto tra i libri. La cornice sembra
    leggermente distaccata dalla parete, come se fosse stata
    mossa di recente.
    """,
    can_take=False,
    aliases=["quadro", "pittura"]
)

def sposta_dipinto(game, item):
    if game.state.get("dipinto_spostato"):
        return "Il dipinto è già spostato, rivelando una nicchia."

    game.state["dipinto_spostato"] = True

    # Crea e aggiungi la chiave
    chiave = Item(
        name="chiave",
        description="Una piccola chiave d'ottone. Ha inciso il numero '1885'.",
        can_take=True,
        aliases=["chiavetta"]
    )
    biblioteca = game.get_room("biblioteca")
    if biblioteca:
        biblioteca.add_item(chiave)

    return """
    Sposti il dipinto scoprendo una piccola nicchia scavata nel muro!
    All'interno c'è una chiave d'ottone con inciso '1885'.
    """

dipinto.add_action("spingi", sposta_dipinto)
dipinto.add_action("sposta", sposta_dipinto)
dipinto.add_action("tocca", sposta_dipinto)

cassaforte = Item(
    name="cassaforte",
    description="""
    Una cassaforte di ferro con combinazione numerica a quattro cifre.
    Sopra, una targa recita: "La verità è nelle stelle".
    """,
    can_take=False,
    aliases=["safe", "casseforte"]
)

def apri_cassaforte(game, item):
    if game.state.get("cassaforte_aperta"):
        return "La cassaforte è già aperta."

    if not game.state.get("diario_letto"):
        return """
        La cassaforte richiede una combinazione di quattro cifre.
        Ma quali? Forse c'è un indizio da qualche parte...
        """

    # Se ha letto il diario, sa la combinazione: 3742
    game.state["cassaforte_aperta"] = True

    # Aggiungi il documento segreto
    documento = Item(
        name="documento",
        description="""
        Un fascicolo di documenti antichi riguardanti la "Stella di Ceylon",
        un diamante leggendario che si credeva perduto. Ci sono mappe,
        lettere, certificati di proprietà...

        Il Professor Blackwood aveva trovato dove si trovava il diamante!
        """,
        can_take=True,
        aliases=["fascicolo", "documenti"]
    )

    game.current_room.add_item(documento)

    return """
    Inserisci la combinazione 3-7-4-2. Click! La cassaforte si apre.

    All'interno trovi un fascicolo di documenti antichi riguardanti
    un diamante leggendario chiamato "Stella di Ceylon".
    """

cassaforte.add_action("apri", apri_cassaforte)
cassaforte.add_action("usa", apri_cassaforte)

botola = Item(
    name="botola",
    description="""
    Una botola di legno nel pavimento del capanno. È chiusa da un
    lucchetto arrugginito.
    """,
    can_take=False,
    aliases=["porta", "lucchetto"]
)

def apri_botola(game, item):
    chiave_item = game.find_item_in_inventory("chiave")

    if not chiave_item:
        return """
        La botola è chiusa con un lucchetto. Ti serve una chiave.
        Il lucchetto ha inciso '1885'.
        """

    if game.state.get("botola_aperta"):
        return "La botola è già aperta."

    game.state["botola_aperta"] = True

    # Apri il passaggio
    capanno_room = game.get_room("capanno")
    sotterraneo_room = game.get_room("sotterraneo")

    if capanno_room and sotterraneo_room:
        capanno_room.add_exit("giù", "sotterraneo")
        sotterraneo_room.add_exit("su", "capanno")

    return """
    Usi la chiave con il numero 1885 sul lucchetto. Si apre con un click!
    Sollevi la botola rivelando una scala che scende in un sotterraneo.

    Cosa nascondeva qui il Professor Blackwood?
    """

botola.add_action("apri", apri_botola)
botola.add_action("usa", apri_botola)

# --- OGGETTI FINALI NEL SOTTERRANEO ---

bacheca = Item(
    name="bacheca",
    description="""
    Una grande bacheca investigativa. Foto di vari individui sono
    appuntate, con stringhe che le collegano. Ritagli di giornale
    parlano di furti di gioielli storici. Mappe con annotazioni.

    Al centro, la foto di un uomo dall'aria sinistra. Sotto: "Marcus
    Vane - trafficante d'arte".

    Il Professor Blackwood stava indagando su un criminale!
    """,
    can_take=False,
    aliases=["board", "pannello"]
)

cassetto = Item(
    name="cassetto",
    description="Un cassetto della scrivania, chiuso a chiave.",
    can_take=False,
    aliases=["scrivania"]
)

def apri_cassetto(game, item):
    if game.state.get("cassetto_aperto"):
        return "Il cassetto è già aperto."

    # Richiede un gesto simbolico: aver capito il mistero
    if game.state.get("diario_letto") and game.state.get("cassaforte_aperta"):
        game.state["cassetto_aperto"] = True

        # Crea la lettera finale
        lettera = Item(
            name="lettera",
            description="Una lettera scritta dal Professor Blackwood.",
            can_take=True
        )

        def leggi_lettera(game_ref, letter):
            game_ref.game_won = True
            return """
            La lettera è indirizzata all'Ispettore Morrison:

            "Caro Ispettore,

            Se stai leggendo questa lettera, significa che qualcosa mi è
            successo. Come temevo, Marcus Vane ha scoperto le mie ricerche
            sulla Stella di Ceylon.

            Ho tutte le prove della sua rete di traffico d'arte. I documenti
            nella cassaforte dimostrano che il diamante è legalmente di
            proprietà del museo nazionale, rubato 50 anni fa dalla sua
            famiglia.

            Non potevo andare alla polizia apertamente - Vane ha contatti
            ovunque. Per questo ho creato questo laboratorio segreto.

            Ho incontrato Vane ieri sera. Gli ho detto che avrei consegnato
            tutto alle autorità. Mi ha minacciato, ma non sono un codardo.

            Se mi è successo qualcosa, cerca nei documenti. La verità è
            nelle stelle - e nei fatti.

            Con stima,
            Professor Edmund Blackwood

            P.S. - Dì a Sarah e James che li amo. Li ho mandati via per
            proteggerli. Quando tutto sarà finito, spero di rivederli."

            ───────────────────────────────────────────────────

            🎉 MISTERO RISOLTO! 🎉

            Hai scoperto la verità: il Professor Blackwood non è scomparso
            volontariamente. È stato vittima di Marcus Vane, un criminale
            che voleva impedirgli di rivelare i suoi traffici.

            Con le prove che hai trovato - il diario, i documenti, la
            bacheca investigativa e questa lettera - puoi finalmente
            portare il caso alla polizia e ottenere giustizia per il
            professore.

            CASO CHIUSO.
            """

        lettera.add_action("leggi", leggi_lettera)
        lettera.add_action("usa", leggi_lettera)

        game.current_room.add_item(lettera)

        return """
        Con un po' di lavoro, riesci a forzare il cassetto.
        All'interno trovi una lettera sigillata con scritto:
        "All'Ispettore Morrison - DA APRIRE IN CASO DI EMERGENZA"
        """
    else:
        return "Il cassetto è chiuso. Forse dovrai prima capire di più sul mistero..."

cassetto.add_action("apri", apri_cassetto)
cassetto.add_action("usa", apri_cassetto)

# ============================================================================
# NPC
# ============================================================================

# Un fantasma/apparizione del professore che appare nel salone
# (per rendere l'atmosfera più inquietante)

fantasma = NPC(
    name="figura",
    description="""
    Una figura indistinta che sembra fatta di nebbia e ombre.
    Quando provi a mettere a fuoco, scompare, per riapparire
    nell'angolo dell'occhio. Ha la forma di un uomo anziano...
    """,
    aliases=["ombra", "apparizione", "spirito"],
    dialogue={
        'default': """
        La figura non risponde con parole, ma senti un sussurro
        nella tua mente: "La verità... è sepolta... dove crescono
        i fiori che non sbocciano mai..."

        Poi svanisce. Era reale o frutto della tua immaginazione?
        """
    }
)

# ============================================================================
# SETUP GIOCO
# ============================================================================

# Aggiungi tutte le stanze
game.add_room("vialetto", vialetto)
game.add_room("portico", portico)
game.add_room("ingresso", ingresso)
game.add_room("salone", salone)
game.add_room("biblioteca", biblioteca)
game.add_room("studio", studio)
game.add_room("corridoio", corridoio)
game.add_room("cucina", cucina)
game.add_room("serra", serra)
game.add_room("giardino", giardino)
game.add_room("capanno", capanno)
game.add_room("sotterraneo", sotterraneo)

# Collegamenti
game.connect_rooms("vialetto", "nord", "portico", bidirectional=True)
game.connect_rooms("portico", "nord", "ingresso", bidirectional=True)
game.connect_rooms("ingresso", "ovest", "salone", bidirectional=True)
game.connect_rooms("ingresso", "est", "biblioteca", bidirectional=True)
game.connect_rooms("ingresso", "nord", "corridoio", bidirectional=True)
game.connect_rooms("biblioteca", "est", "studio", bidirectional=True)
game.connect_rooms("corridoio", "est", "cucina", bidirectional=True)
game.connect_rooms("corridoio", "ovest", "serra", bidirectional=True)
game.connect_rooms("cucina", "nord", "giardino", bidirectional=True)
game.connect_rooms("serra", "nord", "giardino", bidirectional=False)  # Solo andata
game.connect_rooms("giardino", "sud", "cucina", bidirectional=False)
game.connect_rooms("giardino", "nord", "capanno", bidirectional=True)
# La botola collega capanno e sotterraneo ma si apre solo con la chiave

# Aggiungi oggetti alle stanze
salone.add_item(fotografia)
biblioteca.add_item(diario)
biblioteca.add_item(dipinto)
studio.add_item(cassaforte)
capanno.add_item(botola)
sotterraneo.add_item(bacheca)
sotterraneo.add_item(cassetto)

# Aggiungi il fantasma al salone (opzionale, per atmosfera)
salone.add_npc(fantasma)

# Evento: quando entri in cucina per la prima volta
def evento_cucina(game_ref, room):
    if not room.visited:
        print("\n" + "="*70)
        print("Mentre osservi la cucina, ti sembra di sentire un rumore")
        print("al piano di sopra. Un tonfo sordo, come se qualcosa fosse")
        print("caduto. Il tuo cuore accelera...")
        print("Ma poi... silenzio. Probabilmente solo la vecchia casa che")
        print("si assesta.")
        print("="*70 + "\n")

cucina.on_enter = evento_cucina

# Punto di partenza
game.set_start("vialetto")

# ============================================================================
# AVVIO
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("IL MISTERO DELLA VILLA ABBANDONATA")
    print("="*70)
    print("\nAvventura investigativa completa.")
    print("\nOBIETTIVO: Scopri cosa è successo al Professor Blackwood.")
    print("\nCONSIGLI:")
    print("- Esplora tutte le stanze")
    print("- Leggi il diario")
    print("- Cerca oggetti nascosti")
    print("- Presta attenzione agli indizi")
    print("\nPercorso soluzione (spoiler):")
    print("1. Esplora la villa")
    print("2. Trova e leggi il diario in biblioteca")
    print("3. Sposta il dipinto per trovare la chiave")
    print("4. Apri la cassaforte nello studio (combinazione 3742)")
    print("5. Vai al capanno in giardino")
    print("6. Usa la chiave per aprire la botola")
    print("7. Scendi nel sotterraneo")
    print("8. Apri il cassetto e leggi la lettera finale")
    print("="*70 + "\n")

    game.start()
