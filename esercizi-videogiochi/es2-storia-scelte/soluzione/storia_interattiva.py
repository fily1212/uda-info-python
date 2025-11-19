# 📖 STORIA INTERATTIVA A SCELTE MULTIPLE - SOLUZIONE
# "Il Mistero della Biblioteca Proibita"

import time

class ScenaInterattiva:
    def __init__(self, testo, scelte=None, finale=False):
        self.testo = testo
        self.scelte = scelte if scelte else []
        self.finale = finale

    def mostra(self):
        """Visualizza la scena con effetto typing"""
        print("\n" + "="*70)
        for char in self.testo:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print("\n" + "="*70)

    def mostra_scelte(self):
        """Mostra le scelte disponibili"""
        if self.finale:
            return None

        print("\n💭 Cosa fai?\n")
        for i, scelta in enumerate(self.scelte, 1):
            print(f"  {i}. {scelta['testo']}")

        while True:
            try:
                risposta = int(input("\n👉 Scelta: "))
                if 1 <= risposta <= len(self.scelte):
                    return self.scelte[risposta - 1]
                else:
                    print("❌ Scelta non valida!")
            except ValueError:
                print("❌ Inserisci un numero!")


class StoriaInterattiva:
    def __init__(self):
        self.scene = self.crea_storia()
        self.scena_corrente = 'inizio'
        self.inventario = []
        self.karma = 0  # Tiene traccia delle scelte morali

    def crea_storia(self):
        """Definisce l'albero narrativo completo"""

        scene = {
            'inizio': ScenaInterattiva(
                """
📚 IL MISTERO DELLA BIBLIOTECA PROIBITA 📚

Sei uno studente del prestigioso College Arcanum.
È mezzanotte, e giri per i corridoi deserti della scuola.

Improvvisamente, noti una luce provenire dalla Biblioteca Proibita,
un luogo off-limits per gli studenti. La porta è socchiusa...

Voci sussurrate filtrano dall'interno:
"...il libro... stanotte... nessuno deve sapere..."
                """,
                scelte=[
                    {
                        'testo': 'Entro silenziosamente per investigare',
                        'prossima': 'entrata_biblioteca',
                        'karma': 0
                    },
                    {
                        'testo': 'Corro a chiamare il preside',
                        'prossima': 'chiama_preside',
                        'karma': 5
                    },
                    {
                        'testo': 'Rimango nascosto e osservo',
                        'prossima': 'osserva',
                        'karma': 2
                    }
                ]
            ),

            'entrata_biblioteca': ScenaInterattiva(
                """
Entri furtivamente nella biblioteca.
Tra gli scaffali polverosi, vedi due figure incappucciate.

Stanno cercando qualcosa... un libro antico con copertina dorata!
Uno di loro si volta improvvisamente verso di te!

"Chi va là?!" grida.
                """,
                scelte=[
                    {
                        'testo': '"Sono solo uno studente! Non dirò nulla!"',
                        'prossima': 'scoperto_paura',
                        'karma': -3
                    },
                    {
                        'testo': '"Fermi! Lasciate quel libro!"',
                        'prossima': 'scoperto_coraggioso',
                        'karma': 5
                    },
                    {
                        'testo': 'Scappo via di corsa',
                        'prossima': 'fuga',
                        'karma': -1
                    }
                ]
            ),

            'chiama_preside': ScenaInterattiva(
                """
Corri verso l'ufficio del preside e bussi forte.
Il preside, ancora in pigiama, apre la porta sconvolto.

"Cosa succede a quest'ora?!"

Gli spieghi della biblioteca. Lui impallidisce.
"QUELLA biblioteca? Seguimi, subito!"

Correte insieme verso la biblioteca, ma trovate tutto tranquillo.
Nessuna traccia degli intrusi. Il libro dorato è sparito.

Il preside ti guarda serio: "Hai fatto la cosa giusta a chiamarmi,
ma ora dobbiamo trovare quel libro prima che sia troppo tardi!"
                """,
                scelte=[
                    {
                        'testo': 'Aiuto il preside nelle ricerche',
                        'prossima': 'aiuta_preside',
                        'karma': 5
                    },
                    {
                        'testo': 'Propongo di indagare da solo',
                        'prossima': 'indaga_solo',
                        'karma': 2
                    }
                ]
            ),

            'osserva': ScenaInterattiva(
                """
Rimani nascosto dietro una colonna, osservando.

Le due figure prendono un libro dorato e lo mettono in una borsa.
"Perfetto. Ora portiamolo nel bosco per il rituale!"

Escono dalla biblioteca dirigendosi verso l'uscita posteriore.
Hai sentito tutto. Che fai?
                """,
                scelte=[
                    {
                        'testo': 'Li seguo di nascosto nel bosco',
                        'prossima': 'segue_bosco',
                        'karma': 3
                    },
                    {
                        'testo': 'Vado a svegliare il preside',
                        'prossima': 'chiama_preside_tardi',
                        'karma': 4
                    },
                    {
                        'testo': 'Torno in camera, non sono affari miei',
                        'prossima': 'finale_indifferente',
                        'karma': -5,
                        'finale': True
                    }
                ]
            ),

            'scoperto_coraggioso': ScenaInterattiva(
                """
"Hai coraggio, ragazzo," dice una delle figure togliendosi il cappuccio.

È la professoressa Nightshade, insegnante di Storia Arcana!
"Ma non capisci cosa stai facendo. Questo libro..."

L'altra figura si toglie il cappuccio: è Marcus, lo studente più popolare!

"...questo libro contiene un incantesimo per salvare qualcuno che amiamo,"
continua Marcus. "Mia sorella è malata. Solo questo incantesimo può salvarla."

La professoressa aggiunge: "Ma usarlo è proibito. Ci costerà tutto."
                """,
                scelte=[
                    {
                        'testo': '"Vi aiuterò. Facciamolo insieme."',
                        'prossima': 'aiuta_rituale',
                        'karma': 5
                    },
                    {
                        'testo': '"Spiacente, ma è contro le regole."',
                        'prossima': 'finale_legge',
                        'karma': -3,
                        'finale': True
                    },
                    {
                        'testo': '"Cerchiamo un\'altra soluzione!"',
                        'prossima': 'cerca_soluzione',
                        'karma': 8
                    }
                ]
            ),

            'aiuta_rituale': ScenaInterattiva(
                """
Nel cuore del bosco, tracciate un cerchio magico.
Il libro emette una luce dorata quando la professoressa legge l'incantesimo.

L'energia scorre tra voi tre. Senti il potere, la speranza, il sacrificio.

FLASH!

Un'esplosione di luce. Quando apri gli occhi, il libro è cenere.
Marcus riceve un messaggio: "Funziona! Mia sorella sta meglio!"

Ma la professoressa è svenuta. L'incantesimo ha preso la sua magia.
Non potrà più insegnare.

Ti guarda con un sorriso: "Ne è valsa la pena. Hai un cuore d'oro, ragazzo."

🏆 FINALE: IL SACRIFICIO

Hai scelto di aiutare, rischiando tutto per salvare una vita.
Marcus e sua sorella non dimenticheranno mai il tuo coraggio.
La professoressa Nightshade perde i suoi poteri ma trova la pace.

La vera magia è nell'amicizia e nel sacrificio.

KARMA FINALE: {}
                """,
                finale=True
            ),

            'cerca_soluzione': ScenaInterattiva(
                """
"Aspettate!" gridi. "Ci deve essere un altro modo!"

Passi la notte cercando nei libri della biblioteca.
All'alba, trovi un passaggio nascosto:

"L'incantesimo può essere compiuto senza sacrificio se tre cuori puri
si uniscono nella luce della luna piena..."

È stanotte! Correte sul tetto della scuola.
Sotto la luna, unite le mani. Il libro risplende.

L'incantesimo funziona! La sorella di Marcus guarisce, e nessuno
perde i propri poteri!

Il preside vi trova lì: "Avete infranto le regole... ma avete anche
mostrato cosa significa la vera magia. Siete perdonati."

🏆 FINALE PERFETTO: LA SAGGEZZA

Hai trovato una soluzione dove tutti vincono!
Coraggio, intelligenza e cuore hanno trionfato.
Diventi leggenda nella scuola.

KARMA FINALE: {}
                """,
                finale=True
            ),

            'finale_legge': ScenaInterattiva(
                """
"Mi dispiace, ma le regole sono regole," dici con fermezza.

Chiami la sicurezza. Professoressa Nightshade e Marcus vengono espulsi.
La sorella di Marcus muore due settimane dopo.

Marcus ti passa davanti in corridoio senza guardarti.
Il senso di colpa ti perseguita per anni.

Hai fatto la cosa "giusta" secondo le regole...
Ma a quale prezzo?

⚖️ FINALE: LA LEGGE FREDDA

A volte, seguire ciecamente le regole causa più danno che bene.
Hai imparato che la giustizia non è sempre bianca o nera.

KARMA FINALE: {}
                """,
                finale=True
            ),

            'finale_indifferente': ScenaInterattiva(
                """
Torni in camera e ti infili sotto le coperte.

Il giorno dopo, la scuola è sottosopra: il libro proibito è sparito.
La professoressa Nightshade è scomparsa.
Marcus è in lacrime: sua sorella è peggiorata.

Tu sai cosa è successo quella notte, ma non hai fatto nulla.

Gli anni passano. Diventi qualcuno di successo, ma quella notte
ti tormenta nei sogni. E se avessi fatto qualcosa?

😔 FINALE: L'INDIFFERENZA

A volte, non fare nulla è la scelta peggiore.
Il tuo silenzio ha conseguenze che ti perseguitano.

KARMA FINALE: {}
                """,
                finale=True
            ),

            # Aggiungi altri rami narrativi...
            'segue_bosco': ScenaInterattiva(
                """
Segui le figure nel bosco oscuro...
[Continua la storia...]
                """,
                scelte=[
                    {'testo': 'Continua', 'prossima': 'aiuta_rituale', 'karma': 3}
                ]
            ),
        }

        return scene

    def gioca(self):
        """Loop principale del gioco"""
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          📖 STORIA INTERATTIVA A SCELTE 📖               ║
║                                                          ║
║      Ogni scelta cambia il destino della storia!        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
        """)

        input("⏎ Premi INVIO per iniziare...")

        while True:
            # Mostra scena corrente
            scena = self.scene[self.scena_corrente]
            scena.mostra()

            # Se è un finale, termina
            if scena.finale:
                print(scena.testo.format(self.karma))
                break

            # Mostra scelte e ottieni input
            scelta = scena.mostra_scelte()

            if scelta:
                # Aggiorna karma
                self.karma += scelta.get('karma', 0)

                # Passa alla prossima scena
                self.scena_corrente = scelta['prossima']

                time.sleep(1)


if __name__ == "__main__":
    storia = StoriaInterattiva()
    storia.gioca()
