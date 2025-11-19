# 🎮 MOTORE BASE AVVENTURA TESTUALE - SOLUZIONE
# Un castello misterioso da esplorare!

class Stanza:
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione
        self.uscite = {}  # direzione: stanza_destinazione
        self.oggetti = []
        self.visitata = False

    def aggiungi_uscita(self, direzione, stanza):
        """Collega questa stanza a un'altra"""
        self.uscite[direzione] = stanza

    def aggiungi_oggetto(self, oggetto):
        """Aggiungi un oggetto alla stanza"""
        self.oggetti.append(oggetto)

    def rimuovi_oggetto(self, oggetto):
        """Rimuovi oggetto dalla stanza"""
        if oggetto in self.oggetti:
            self.oggetti.remove(oggetto)

    def descrivi(self):
        """Mostra descrizione della stanza"""
        print(f"\n{'='*60}")
        print(f"📍 {self.nome}")
        print(f"{'='*60}")

        if not self.visitata:
            print(f"\n{self.descrizione}")
            self.visitata = True
        else:
            print(f"\nSei di nuovo {self.nome.lower()}.")

        # Mostra uscite
        if self.uscite:
            print(f"\n🚪 Uscite: {', '.join(self.uscite.keys())}")

        # Mostra oggetti
        if self.oggetti:
            print(f"\n🔍 Vedi: {', '.join(self.oggetti)}")


class Giocatore:
    def __init__(self, nome="Avventuriero"):
        self.nome = nome
        self.stanza_corrente = None
        self.inventario = []

    def muovi(self, direzione):
        """Muovi il giocatore in una direzione"""
        if direzione in self.stanza_corrente.uscite:
            self.stanza_corrente = self.stanza_corrente.uscite[direzione]
            self.stanza_corrente.descrivi()
            return True
        else:
            print(f"\n❌ Non puoi andare in quella direzione!")
            return False

    def prendi(self, oggetto):
        """Prendi un oggetto"""
        if oggetto in self.stanza_corrente.oggetti:
            self.stanza_corrente.rimuovi_oggetto(oggetto)
            self.inventario.append(oggetto)
            print(f"\n✅ Hai preso: {oggetto}")
        else:
            print(f"\n❌ Non c'è nessun '{oggetto}' qui!")

    def mostra_inventario(self):
        """Mostra inventario"""
        if self.inventario:
            print(f"\n🎒 INVENTARIO: {', '.join(self.inventario)}")
        else:
            print(f"\n🎒 Inventario vuoto")


class MotoreGioco:
    def __init__(self):
        self.giocatore = None
        self.comandi = {
            'nord': self.vai_nord,
            'n': self.vai_nord,
            'sud': self.vai_sud,
            's': self.vai_sud,
            'est': self.vai_est,
            'e': self.vai_est,
            'ovest': self.vai_ovest,
            'o': self.vai_ovest,
            'guarda': self.guarda,
            'inventario': self.inventario,
            'inv': self.inventario,
            'prendi': self.prendi,
            'aiuto': self.aiuto,
            'esci': self.esci,
        }

    def crea_mondo(self):
        """Crea il mondo di gioco: Il Castello Misterioso"""

        # Crea stanze
        ingresso = Stanza(
            "nell'Ingresso del Castello",
            "Un vasto atrio con soffitti altissimi. La polvere danza nei raggi di luce "
            "che filtrano dalle finestre rotte. Vedi un grande portone a nord e corridoi "
            "a est e ovest."
        )

        salone = Stanza(
            "nel Salone delle Feste",
            "Un tempo magnifico, ora è un luogo decadente. I lampadari penzolano dal "
            "soffitto, e vecchi ritratti ti osservano dalle pareti."
        )

        biblioteca = Stanza(
            "nella Biblioteca",
            "Scaffali pieni di libri antichi si ergono fino al soffitto. C'è odore di "
            "carta vecchia e mistero. Una scala a chiocciola sale verso l'alto."
        )

        cucina = Stanza(
            "nella Cucina",
            "Pentole arrugginite e stoviglie rotte giacciono ovunque. Un vecchio forno "
            "in pietra domina la stanza. Qualcosa scintilla sul tavolo..."
        )

        torre = Stanza(
            "sulla Torre",
            "Sei in cima alla torre. Il vento soffia forte. La vista è mozzafiato, ma "
            "l'altezza fa girare la testa. C'è un vecchio baule nell'angolo."
        )

        cripta = Stanza(
            "nella Cripta",
            "Scendi scale umide e scivolose. L'aria è fredda e pesante. Bare di pietra "
            "sono allineate lungo le pareti. Un brivido ti percorre la schiena..."
        )

        # Collega stanze
        ingresso.aggiungi_uscita('nord', salone)
        ingresso.aggiungi_uscita('est', biblioteca)
        ingresso.aggiungi_uscita('ovest', cucina)

        salone.aggiungi_uscita('sud', ingresso)
        salone.aggiungi_uscita('sotto', cripta)

        biblioteca.aggiungi_uscita('ovest', ingresso)
        biblioteca.aggiungi_uscita('su', torre)

        cucina.aggiungi_uscita('est', ingresso)

        torre.aggiungi_uscita('giù', biblioteca)

        cripta.aggiungi_uscita('su', salone)

        # Aggiungi oggetti
        cucina.aggiungi_oggetto("chiave d'oro")
        cucina.aggiungi_oggetto("lanterna")
        torre.aggiungi_oggetto("mappa antica")
        torre.aggiungi_oggetto("spada arrugginita")
        biblioteca.aggiungi_oggetto("libro di incantesimi")
        cripta.aggiungi_oggetto("tesoro")

        return ingresso

    def vai_nord(self, _):
        self.giocatore.muovi('nord')

    def vai_sud(self, _):
        self.giocatore.muovi('sud')

    def vai_est(self, _):
        self.giocatore.muovi('est')

    def vai_ovest(self, _):
        self.giocatore.muovi('ovest')

    def guarda(self, _):
        self.giocatore.stanza_corrente.descrivi()

    def inventario(self, _):
        self.giocatore.mostra_inventario()

    def prendi(self, args):
        if args:
            oggetto = ' '.join(args)
            self.giocatore.prendi(oggetto)
        else:
            print("\n❓ Cosa vuoi prendere?")

    def aiuto(self, _):
        print("""
╔══════════════════════════════════════════════════════════╗
║                    ❓ AIUTO                               ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  COMANDI DI MOVIMENTO:                                   ║
║    nord/n, sud/s, est/e, ovest/o                        ║
║    su, giù, sotto                                        ║
║                                                          ║
║  COMANDI DI INTERAZIONE:                                 ║
║    guarda - Osserva la stanza                           ║
║    prendi [oggetto] - Prendi un oggetto                 ║
║    inventario/inv - Mostra inventario                   ║
║                                                          ║
║  ALTRO:                                                  ║
║    aiuto - Mostra questo messaggio                      ║
║    esci - Esci dal gioco                                ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
        """)

    def esci(self, _):
        print("\n👋 Grazie per aver giocato! Alla prossima avventura!")
        return 'ESCI'

    def avvia(self):
        """Avvia il gioco"""
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           🏰 IL CASTELLO MISTERIOSO 🏰                   ║
║                                                          ║
║        Un'avventura testuale interattiva                 ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

📖 STORIA:
Sei un avventuriero che ha sentito leggende su un tesoro nascosto
in un castello abbandonato. Armato solo di coraggio, entri nel
castello per trovare il leggendario tesoro...

Scrivi 'aiuto' per vedere i comandi disponibili.
        """)

        nome = input("\n👤 Come ti chiami? ")
        self.giocatore = Giocatore(nome if nome else "Avventuriero")

        print(f"\n✨ Benvenuto, {self.giocatore.nome}!")

        # Crea mondo e posiziona giocatore
        stanza_iniziale = self.crea_mondo()
        self.giocatore.stanza_corrente = stanza_iniziale

        # Mostra prima stanza
        stanza_iniziale.descrivi()

        # Game loop
        while True:
            comando = input("\n> ").lower().strip()

            if not comando:
                continue

            # Dividi comando e argomenti
            parti = comando.split()
            cmd = parti[0]
            args = parti[1:] if len(parti) > 1 else []

            # Esegui comando
            if cmd in self.comandi:
                risultato = self.comandi[cmd](args)
                if risultato == 'ESCI':
                    break
            else:
                print(f"\n❓ Comando '{cmd}' non riconosciuto. Scrivi 'aiuto' per la lista.")

            # Controlla vittoria
            if 'tesoro' in self.giocatore.inventario:
                print(f"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║              🏆 CONGRATULAZIONI! 🏆                      ║
║                                                          ║
║        Hai trovato il tesoro del castello!               ║
║          Sei un vero avventuriero!                       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
                """)
                break


if __name__ == "__main__":
    gioco = MotoreGioco()
    gioco.avvia()
