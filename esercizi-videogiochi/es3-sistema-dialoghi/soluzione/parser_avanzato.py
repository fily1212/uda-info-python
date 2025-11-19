# 🎮 PARSER TESTUALE AVANZATO - Stile Inform6/Infocom
# Scrivi comandi in linguaggio naturale!

import re

class Oggetto:
    """Un oggetto di gioco con proprietà"""
    def __init__(self, nome, sinonimi, descrizione, raccoglibile=True, usabile=False):
        self.nome = nome
        self.sinonimi = sinonimi  # lista di nomi alternativi
        self.descrizione = descrizione
        self.raccoglibile = raccoglibile
        self.usabile = usabile
        self.stato = {}  # dizionario per stati (aperto, acceso, ecc.)

    def corrisponde(self, parola):
        """Verifica se la parola si riferisce a questo oggetto"""
        return parola.lower() in [self.nome.lower()] + [s.lower() for s in self.sinonimi]


class Personaggio:
    """Un NPC con cui dialogare"""
    def __init__(self, nome, descrizione, dialoghi):
        self.nome = nome
        self.descrizione = descrizione
        self.dialoghi = dialoghi  # dizionario argomento: risposta
        self.incontrato = False

    def parla(self, argomento=None):
        """Dialoga con il personaggio"""
        if not self.incontrato:
            self.incontrato = True
            return f"{self.nome}: {self.dialoghi.get('prima_volta', 'Salve.')}"

        if argomento and argomento in self.dialoghi:
            return f"{self.nome}: {self.dialoghi[argomento]}"
        elif argomento:
            return f"{self.nome}: Non so nulla di '{argomento}'."
        else:
            return f"{self.nome}: {self.dialoghi.get('generale', 'Sì?')}"


class Stanza:
    """Una location del gioco"""
    def __init__(self, nome, descrizione, descrizione_lunga=None):
        self.nome = nome
        self.descrizione = descrizione  # descrizione breve
        self.descrizione_lunga = descrizione_lunga or descrizione
        self.uscite = {}
        self.oggetti = []
        self.personaggi = []
        self.visitata = False
        self.illuminata = True

    def aggiungi_oggetto(self, oggetto):
        self.oggetti.append(oggetto)

    def rimuovi_oggetto(self, oggetto):
        if oggetto in self.oggetti:
            self.oggetti.remove(oggetto)

    def aggiungi_personaggio(self, personaggio):
        self.personaggi.append(personaggio)

    def descrivi(self, prima_volta=False):
        """Descrizione della stanza"""
        if not self.illuminata:
            return "È buio pesto. Non vedi nulla."

        if prima_volta or not self.visitata:
            testo = f"\n{'='*70}\n📍 {self.nome}\n{'='*70}\n\n{self.descrizione_lunga}"
            self.visitata = True
        else:
            testo = f"\n{self.nome}"

        # Oggetti visibili
        if self.oggetti:
            testo += f"\n\n🔍 Vedi: {', '.join([o.nome for o in self.oggetti])}"

        # Personaggi
        if self.personaggi:
            testo += f"\n\n👤 C'è: {', '.join([p.nome for p in self.personaggi])}"

        # Uscite
        if self.uscite:
            testo += f"\n\n🚪 Uscite evidenti: {', '.join(self.uscite.keys())}"

        return testo


class ParserTestuale:
    """Parser di comandi in linguaggio naturale"""

    # Dizionario verbi con sinonimi
    VERBI = {
        'prendi': ['prendi', 'raccogli', 'afferra', 'prenda', 'take', 'get'],
        'lascia': ['lascia', 'posa', 'drop', 'metti giù'],
        'guarda': ['guarda', 'esamina', 'osserva', 'ispeziona', 'look', 'l', 'x'],
        'usa': ['usa', 'utilizza', 'use', 'adopera'],
        'apri': ['apri', 'open', 'schiudi'],
        'parla': ['parla', 'dialoga', 'talk', 'chiedi', 'domanda'],
        'vai': ['vai', 'va', 'muovi', 'go', 'cammina'],
        'inventario': ['inventario', 'inv', 'i', 'inventory'],
        'aiuto': ['aiuto', 'help', 'h', '?'],
    }

    # Articoli e preposizioni da ignorare
    PAROLE_IGNORABILI = ['il', 'la', 'lo', 'gli', 'le', 'un', 'una',
                          'al', 'alla', 'allo', 'con', 'a', 'di', 'da']

    def __init__(self, gioco):
        self.gioco = gioco

    def pulisci_input(self, comando):
        """Rimuovi articoli e preposizioni"""
        parole = comando.lower().split()
        return [p for p in parole if p not in self.PAROLE_IGNORABILI]

    def identifica_verbo(self, parola):
        """Trova il verbo base dato un sinonimo"""
        for verbo, sinonimi in self.VERBI.items():
            if parola in sinonimi:
                return verbo
        return None

    def trova_oggetto(self, nome_oggetto, dove='stanza'):
        """Trova un oggetto nella stanza o inventario"""
        if dove == 'stanza':
            oggetti = self.gioco.stanza_corrente.oggetti
        elif dove == 'inventario':
            oggetti = self.gioco.inventario
        else:  # entrambi
            oggetti = self.gioco.stanza_corrente.oggetti + self.gioco.inventario

        for oggetto in oggetti:
            if oggetto.corrisponde(nome_oggetto):
                return oggetto
        return None

    def trova_personaggio(self, nome):
        """Trova un personaggio nella stanza"""
        for pg in self.gioco.stanza_corrente.personaggi:
            if nome.lower() in pg.nome.lower():
                return pg
        return None

    def parse(self, comando):
        """Analizza e esegue il comando"""
        if not comando.strip():
            return "❓ Cosa?"

        parole = self.pulisci_input(comando)

        if not parole:
            return "❓ Cosa?"

        # Identifica il verbo
        verbo = self.identifica_verbo(parole[0])

        if not verbo:
            return f"❓ Non capisco '{parole[0]}'."

        # Esegui azione basata sul verbo
        if verbo == 'guarda':
            if len(parole) == 1:
                return self.gioco.stanza_corrente.descrivi(prima_volta=True)
            else:
                nome_oggetto = ' '.join(parole[1:])
                oggetto = self.trova_oggetto(nome_oggetto, dove='entrambi')
                if oggetto:
                    return f"🔍 {oggetto.descrizione}"
                else:
                    return f"❓ Non vedi nessun '{nome_oggetto}'."

        elif verbo == 'prendi':
            if len(parole) < 2:
                return "❓ Cosa vuoi prendere?"

            nome_oggetto = ' '.join(parole[1:])
            oggetto = self.trova_oggetto(nome_oggetto, dove='stanza')

            if not oggetto:
                return f"❓ Non c'è nessun '{nome_oggetto}' qui."

            if not oggetto.raccoglibile:
                return f"❌ Non puoi prendere {oggetto.nome}."

            self.gioco.stanza_corrente.rimuovi_oggetto(oggetto)
            self.gioco.inventario.append(oggetto)
            return f"✅ Preso: {oggetto.nome}."

        elif verbo == 'lascia':
            if len(parole) < 2:
                return "❓ Cosa vuoi lasciare?"

            nome_oggetto = ' '.join(parole[1:])
            oggetto = self.trova_oggetto(nome_oggetto, dove='inventario')

            if not oggetto:
                return f"❓ Non hai nessun '{nome_oggetto}'."

            self.gioco.inventario.remove(oggetto)
            self.gioco.stanza_corrente.aggiungi_oggetto(oggetto)
            return f"✅ Lasciato: {oggetto.nome}."

        elif verbo == 'usa':
            if len(parole) < 2:
                return "❓ Cosa vuoi usare?"

            nome_oggetto = ' '.join(parole[1:])
            oggetto = self.trova_oggetto(nome_oggetto, dove='entrambi')

            if not oggetto:
                return f"❓ Non hai/vedi '{nome_oggetto}'."

            return self.gioco.usa_oggetto(oggetto)

        elif verbo == 'parla':
            if len(parole) < 2:
                # Parla con chiunque sia nella stanza
                if self.gioco.stanza_corrente.personaggi:
                    pg = self.gioco.stanza_corrente.personaggi[0]
                    return pg.parla()
                else:
                    return "❓ Non c'è nessuno con cui parlare."
            else:
                # Cerca il personaggio
                nome_pg = parole[1]
                pg = self.trova_personaggio(nome_pg)

                if not pg:
                    return f"❓ Non c'è nessun '{nome_pg}' qui."

                # Cerca argomento (parole dopo "di")
                argomento = None
                if 'di' in parole:
                    idx = parole.index('di')
                    if idx + 1 < len(parole):
                        argomento = ' '.join(parole[idx+1:])

                return pg.parla(argomento)

        elif verbo == 'vai':
            if len(parole) < 2:
                return "❓ Dove vuoi andare?"

            direzione = parole[1]

            if direzione in self.gioco.stanza_corrente.uscite:
                self.gioco.stanza_corrente = self.gioco.stanza_corrente.uscite[direzione]
                return self.gioco.stanza_corrente.descrivi()
            else:
                return f"❌ Non puoi andare a {direzione}."

        elif verbo == 'inventario':
            if self.gioco.inventario:
                return "🎒 INVENTARIO:\n  " + "\n  ".join([f"• {o.nome}" for o in self.gioco.inventario])
            else:
                return "🎒 Inventario vuoto."

        elif verbo == 'aiuto':
            return self.mostra_aiuto()

        return f"❓ Non so come fare '{comando}'."

    def mostra_aiuto(self):
        return """
╔══════════════════════════════════════════════════════════╗
║                    ❓ COMANDI DISPONIBILI                 ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  🚶 MOVIMENTO:                                            ║
║    vai [direzione] - es: "vai nord", "vai est"          ║
║    [direzione] - es: "nord", "su", "dentro"             ║
║                                                          ║
║  👁️ OSSERVAZIONE:                                         ║
║    guarda - Osserva la stanza                           ║
║    esamina [oggetto] - es: "esamina chiave"             ║
║    guarda [oggetto] - es: "guarda porta"                ║
║                                                          ║
║  🤲 MANIPOLAZIONE:                                        ║
║    prendi [oggetto] - es: "prendi spada"                ║
║    lascia [oggetto] - es: "lascia torcia"               ║
║    usa [oggetto] - es: "usa chiave"                     ║
║    apri [oggetto] - es: "apri porta"                    ║
║                                                          ║
║  💬 INTERAZIONE:                                          ║
║    parla con [personaggio] - es: "parla con mago"       ║
║    chiedi di [argomento] - es: "chiedi di tesoro"       ║
║                                                          ║
║  📦 ALTRO:                                                ║
║    inventario / inv / i - Mostra inventario             ║
║    aiuto - Mostra questo messaggio                      ║
║                                                          ║
║  💡 SUGGERIMENTI:                                         ║
║    - Puoi usare sinonimi (prendi/raccogli/afferra)      ║
║    - Gli articoli sono opzionali ("la spada" = "spada") ║
║    - Esamina tutto! La descrizione rivela indizi        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
        """


class GiocoTestuale:
    """Il gioco principale"""
    def __init__(self):
        self.stanza_corrente = None
        self.inventario = []
        self.parser = ParserTestuale(self)
        self.flags = {}  # stati del gioco

    def usa_oggetto(self, oggetto):
        """Logica per usare oggetti (personalizzabile)"""
        # Esempio di logica condizionale
        if oggetto.nome == "chiave d'oro":
            if self.stanza_corrente.nome == "Porta del Tesoro":
                self.flags['porta_aperta'] = True
                return "🔓 Usi la chiave d'oro. La porta si apre con un clic!"
            else:
                return "❓ Non c'è nulla da aprire qui con questa chiave."

        elif oggetto.nome == "torcia":
            if not oggetto.stato.get('accesa', False):
                oggetto.stato['accesa'] = True
                return "🔥 Accendi la torcia. La luce illumina l'oscurità!"
            else:
                return "La torcia è già accesa."

        return f"Non sai come usare {oggetto.nome}."

    def crea_mondo(self):
        """Crea il mondo del gioco: La Cripta del Mago"""

        # STANZE
        entrata = Stanza(
            "Entrata della Cripta",
            "Entrata di una cripta buia.",
            "Sei all'ingresso di un'antica cripta. I muri di pietra sono coperti "
            "di muschio e l'aria è fredda e umida. Una scala scende nelle tenebre a nord. "
            "Un vecchio cartello arrugginito recita: 'Qui giace il Mago Aldrin'."
        )

        corridoio = Stanza(
            "Corridoio Buio",
            "Un corridoio oscuro.",
            "Un corridoio stretto e buio. Senza luce è impossibile vedere. "
            "Le pareti sono scivolose e fredde al tatto."
        )
        corridoio.illuminata = False  # Serve la torcia!

        sala_statue = Stanza(
            "Sala delle Statue",
            "Una sala con statue inquietanti.",
            "Una vasta sala circolare. Quattro statue di guerrieri in armatura "
            "ti circondano, fissandoti con occhi di pietra. I loro sguardi sembrano "
            "seguirti ovunque. Al centro c'è un antico altare."
        )

        biblioteca = Stanza(
            "Biblioteca del Mago",
            "Una biblioteca polverosa.",
            "Scaffali pieni di libri antichi si ergono fino al soffitto. "
            "La polvere vola nell'aria. Un vecchio scrittoio occupa un angolo. "
            "C'è ancora qualcosa di magico in questo luogo..."
        )

        porta_tesoro = Stanza(
            "Porta del Tesoro",
            "Una porta massiccia d'oro.",
            "Di fronte a te si erge una porta massiccia decorata con simboli dorati. "
            "Una serratura a forma di teschio richiede una chiave speciale. "
            "Dall'altra parte senti un'energia pulsante..."
        )

        camera_tesoro = Stanza(
            "Camera del Tesoro",
            "La camera del tesoro!",
            "✨ SEI NELLA CAMERA DEL TESORO! ✨\n"
            "Oro, gemme e artefatti magici brillano ovunque. "
            "Al centro, su un piedistallo, riposa il leggendario LIBRO DI ALDRIN."
        )

        # COLLEGA STANZE
        entrata.uscite = {'nord': corridoio, 'giù': corridoio}
        corridoio.uscite = {'sud': entrata, 'su': entrata, 'nord': sala_statue}
        sala_statue.uscite = {'sud': corridoio, 'est': biblioteca, 'nord': porta_tesoro}
        biblioteca.uscite = {'ovest': sala_statue}
        porta_tesoro.uscite = {'sud': sala_statue}

        # OGGETTI
        torcia = Oggetto(
            "torcia",
            ["fiaccola", "luce", "lampada"],
            "Una torcia di legno con uno straccio unto. Potrebbe essere accesa.",
            raccoglibile=True,
            usabile=True
        )

        chiave = Oggetto(
            "chiave d'oro",
            ["chiave", "chiave dorata"],
            "Una piccola chiave d'oro decorata con un teschio. Deve aprire qualcosa di importante.",
            raccoglibile=True,
            usabile=True
        )

        libro_incantesimi = Oggetto(
            "libro degli incantesimi",
            ["libro", "grimorio", "tomo"],
            "Un vecchio grimorio con copertina in pelle. Le pagine sono piene di formule arcane. "
            "C'è un indizio scritto: 'La chiave dorme dove i guerrieri vegliano'.",
            raccoglibile=True
        )

        statua = Oggetto(
            "statua del guerriero",
            ["statua", "guerriero"],
            "Una statua di pietra di un antico guerriero. Alla base c'è una piccola nicchia... "
            "C'è qualcosa che brilla dentro!",
            raccoglibile=False
        )

        # Aggiungi oggetti alle stanze
        entrata.aggiungi_oggetto(torcia)
        biblioteca.aggiungi_oggetto(libro_incantesimi)
        sala_statue.aggiungi_oggetto(statua)
        sala_statue.aggiungi_oggetto(chiave)  # Nascosta nella statua

        # PERSONAGGI
        fantasma = Personaggio(
            "Fantasma del Mago Aldrin",
            "Un'apparizione spettrale di un vecchio mago dalla lunga barba.",
            {
                'prima_volta': "Ohhh... Un visitatore dopo tanti secoli... "
                               "Benvenuto nella mia umile dimora...",
                'generale': "Cosa vuoi sapere, viandante?",
                'tesoro': "Il mio tesoro è protetto. Solo chi è degno può raggiungerlo. "
                          "Avrai bisogno di luce e della mia chiave dorata.",
                'chiave': "La chiave è nascosta dove i miei guerrieri vegliano eternamente. "
                          "Cerca bene...",
                'libro': "Il Libro contiene tutta la mia conoscenza magica. "
                         "Ma prima devi superare le prove."
            }
        )

        biblioteca.aggiungi_personaggio(fantasma)

        return entrata

    def verifica_condizioni_vittoria(self):
        """Controlla se il giocatore ha vinto"""
        # Se prende il libro di Aldrin dalla camera del tesoro
        for oggetto in self.inventario:
            if 'libro' in oggetto.nome.lower() and 'aldrin' in oggetto.nome.lower():
                return True
        return False

    def avvia(self):
        """Loop principale del gioco"""
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║            🏛️ LA CRIPTA DEL MAGO ALDRIN 🏛️              ║
║                                                          ║
║         Un'avventura testuale interattiva                ║
║                  in stile Inform/Infocom                 ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

📖 STORIA:

Hai sentito leggende su un antico mago di nome Aldrin, morto secoli fa.
Si dice che la sua cripta contenga un tesoro di conoscenza magica.

Armato solo di coraggio (e forse di una torcia), entri nella cripta...

💡 SUGGERIMENTO: Scrivi comandi in linguaggio naturale!
   Esempio: "prendi la torcia", "guarda la statua", "vai nord"

   Scrivi 'aiuto' per vedere tutti i comandi.
        """)

        input("\n⏎ Premi INVIO per iniziare la tua avventura...")

        # Crea mondo
        self.stanza_corrente = self.crea_mondo()

        # Mostra prima stanza
        print(self.stanza_corrente.descrivi(prima_volta=True))

        # Game loop
        while True:
            comando = input("\n> ").strip()

            if comando.lower() in ['esci', 'quit', 'q']:
                print("\n👋 Grazie per aver giocato!")
                break

            # Gestione movimento diretto (senza "vai")
            direzioni = ['nord', 'sud', 'est', 'ovest', 'su', 'giù', 'dentro', 'fuori',
                        'n', 's', 'e', 'o']
            if comando.lower() in direzioni:
                comando = f"vai {comando}"

            # Parse comando
            risposta = self.parser.parse(comando)
            print(f"\n{risposta}")

            # Logica speciale: illumina corridoio se torcia accesa
            for oggetto in self.inventario:
                if oggetto.nome == "torcia" and oggetto.stato.get('accesa'):
                    # Trova il corridoio e illuminalo
                    for stanza_nome, stanza in [('corridoio', s) for s in [self.stanza_corrente]]:
                        if 'Corridoio' in stanza.nome:
                            stanza.illuminata = True

            # Apri porta tesoro se hai chiave
            if self.flags.get('porta_aperta') and self.stanza_corrente.nome == "Porta del Tesoro":
                if 'nord' not in self.stanza_corrente.uscite:
                    # Crea camera tesoro e collegala
                    tesoro = Stanza(
                        "Camera del Tesoro",
                        "La camera del tesoro!",
                        "✨ SEI NELLA CAMERA DEL TESORO! ✨\n"
                        "Oro, gemme e artefatti magici brillano ovunque. "
                        "Al centro, su un piedistallo, riposa il leggendario LIBRO DI ALDRIN."
                    )

                    libro_aldrin = Oggetto(
                        "Libro di Aldrin",
                        ["libro", "libro magico"],
                        "Il leggendario Libro di Aldrin! Contiene tutta la saggezza magica del grande mago.",
                        raccoglibile=True
                    )
                    tesoro.aggiungi_oggetto(libro_aldrin)

                    self.stanza_corrente.uscite['nord'] = tesoro
                    tesoro.uscite['sud'] = self.stanza_corrente

            # Verifica vittoria
            if self.verifica_condizioni_vittoria():
                print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║                 🏆 VITTORIA! 🏆                          ║
║                                                          ║
║       Hai trovato il Libro di Aldrin!                   ║
║       La conoscenza magica è ora tua!                   ║
║                                                          ║
║           Sei un vero avventuriero!                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
                """)
                break


if __name__ == "__main__":
    gioco = GiocoTestuale()
    gioco.avvia()
