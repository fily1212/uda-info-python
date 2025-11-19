# 🎮 STORY PLAYER - Gioca storie create con l'editor
# Player console per file JSON

import json
import sys

class StoryPlayer:
    """Player per storie interattive in formato JSON"""

    def __init__(self, file_json):
        try:
            with open(file_json, 'r', encoding='utf-8') as f:
                self.storia = json.load(f)
        except FileNotFoundError:
            print(f"❌ File '{file_json}' non trovato!")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"❌ Errore nel parsing di '{file_json}'!")
            sys.exit(1)

        self.scena_corrente = self.storia.get('scena_iniziale', 'inizio')
        self.inventario = self.storia.get('inventario_iniziale', [])
        self.visite = {}  # Traccia scene visitate

    def gioca(self):
        """Loop principale del gioco"""
        print("\n" + "═" * 70)
        print(f"  📖 {self.storia['titolo']}")
        if self.storia.get('autore'):
            print(f"  di {self.storia['autore']}")
        print("═" * 70)

        if self.storia.get('descrizione'):
            print(f"\n{self.storia['descrizione']}\n")

        input("⏎ Premi INVIO per iniziare...")

        while True:
            if not self.mostra_scena():
                break

    def mostra_scena(self):
        """Mostra una scena e gestisce le scelte"""
        if self.scena_corrente not in self.storia['scene']:
            print(f"\n❌ ERRORE: Scena '{self.scena_corrente}' non trovata!")
            return False

        scena = self.storia['scene'][self.scena_corrente]

        # Segna come visitata
        if self.scena_corrente not in self.visite:
            self.visite[self.scena_corrente] = 0
        self.visite[self.scena_corrente] += 1

        # Header
        print("\n" + "─" * 70)
        print(f"📍 {self.scena_corrente.upper()}")
        if self.visite[self.scena_corrente] > 1:
            print(f"   (Visitata {self.visite[self.scena_corrente]} volte)")
        print("─" * 70 + "\n")

        # Testo scena
        print(self.formatta_testo(scena['testo']))

        # Mostra inventario se presente
        if self.inventario:
            print(f"\n🎒 Inventario: {', '.join(self.inventario)}")

        # Controlla se è una scena finale
        if scena.get('tipo') == 'finale':
            print("\n" + "═" * 70)
            print("🏁 FINE DELLA STORIA 🏁".center(70))
            print("═" * 70)

            finale_tipo = scena.get('finale_tipo', 'neutro')
            if finale_tipo == 'buono':
                print("\n✨ HAI RAGGIUNTO UN FINALE POSITIVO! ✨\n")
            elif finale_tipo == 'cattivo':
                print("\n💀 HAI RAGGIUNTO UN FINALE NEGATIVO 💀\n")
            else:
                print()

            # Statistiche
            print(f"Scene visitate: {len(self.visite)}/{len(self.storia['scene'])}")
            print(f"Oggetti raccolti: {len(self.inventario)}")

            return False

        # Mostra scelte
        scelte = scena.get('scelte', [])
        if not scelte:
            print("\n⚠️ Nessuna scelta disponibile. Fine della storia.")
            return False

        print("\n" + "─" * 70)
        print("Cosa fai?")
        print("─" * 70)

        scelte_valide = []
        for i, scelta in enumerate(scelte, 1):
            # Controlla condizioni (se implementate)
            if 'richiede_oggetto' in scelta:
                if scelta['richiede_oggetto'] not in self.inventario:
                    print(f"{i}. [🔒 Richiede: {scelta['richiede_oggetto']}]")
                    continue

            scelte_valide.append((i - 1, scelta))
            print(f"{i}. {scelta['testo']}")

        if not scelte_valide:
            print("\n❌ Nessuna scelta disponibile (mancano oggetti necessari).")
            return False

        # Input giocatore
        while True:
            try:
                scelta_input = input("\n> ").strip()

                # Comandi speciali
                if scelta_input.lower() in ['esci', 'quit', 'q']:
                    print("\n👋 Partita terminata.")
                    return False

                if scelta_input.lower() in ['inventario', 'inv', 'i']:
                    if self.inventario:
                        print(f"🎒 Inventario: {', '.join(self.inventario)}")
                    else:
                        print("🎒 Inventario vuoto")
                    continue

                scelta_num = int(scelta_input) - 1

                # Trova la scelta
                scelta_selezionata = None
                for idx, scelta in scelte_valide:
                    if idx == scelta_num:
                        scelta_selezionata = scelta
                        break

                if scelta_selezionata:
                    # Gestisci modifiche inventario
                    if 'aggiungi_oggetto' in scelta_selezionata:
                        obj = scelta_selezionata['aggiungi_oggetto']
                        self.inventario.append(obj)
                        print(f"\n✅ Hai ottenuto: {obj}")
                        input("⏎ Premi INVIO per continuare...")

                    if 'rimuovi_oggetto' in scelta_selezionata:
                        obj = scelta_selezionata['rimuovi_oggetto']
                        if obj in self.inventario:
                            self.inventario.remove(obj)
                            print(f"\n❌ Hai perso: {obj}")
                            input("⏎ Premi INVIO per continuare...")

                    # Vai alla prossima scena
                    self.scena_corrente = scelta_selezionata['prossima_scena']
                    return True
                else:
                    print("❌ Scelta non valida!")

            except ValueError:
                print("❌ Inserisci un numero!")
            except KeyboardInterrupt:
                print("\n\n👋 Partita terminata.")
                return False

    def formatta_testo(self, testo, larghezza=70):
        """Formatta il testo per una migliore leggibilità"""
        parole = testo.split()
        righe = []
        riga_corrente = []
        lunghezza_corrente = 0

        for parola in parole:
            if lunghezza_corrente + len(parola) + 1 <= larghezza:
                riga_corrente.append(parola)
                lunghezza_corrente += len(parola) + 1
            else:
                righe.append(' '.join(riga_corrente))
                riga_corrente = [parola]
                lunghezza_corrente = len(parola)

        if riga_corrente:
            righe.append(' '.join(riga_corrente))

        return '\n'.join(righe)


def main():
    """Funzione principale"""
    if len(sys.argv) < 2:
        print("""
╔═══════════════════════════════════════════════════════════╗
║                  🎮 STORY PLAYER                          ║
╚═══════════════════════════════════════════════════════════╝

Uso: python player.py <file_storia.json>

Esempio:
    python player.py la_mia_avventura.json

Comandi durante il gioco:
    i, inventario    - Mostra inventario
    esci, quit, q    - Esci dal gioco
        """)
        sys.exit(1)

    file_storia = sys.argv[1]
    player = StoryPlayer(file_storia)
    player.gioca()


if __name__ == "__main__":
    main()
