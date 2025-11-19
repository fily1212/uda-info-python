# 🚪 ESCAPE ROOM MATEMATICA - SOLUZIONE
# Risolvi enigmi di combinatoria per fuggire!

from math import factorial, comb, perm
import time
import random

class EscapeRoom:
    def __init__(self):
        self.enigmi_risolti = 0
        self.tempo_inizio = time.time()
        self.tentativi_falliti = 0

    def mostra_tempo(self):
        """Mostra tempo trascorso"""
        elapsed = int(time.time() - self.tempo_inizio)
        minuti = elapsed // 60
        secondi = elapsed % 60
        return f"{minuti:02d}:{secondi:02d}"

    def animazione_testo(self, testo, delay=0.03):
        """Stampa testo con effetto macchina da scrivere"""
        for char in testo:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def intro(self):
        print("\n" + "="*70)
        print(" "*20 + "🚪 ESCAPE ROOM MATEMATICA 🚪")
        print("="*70)

        self.animazione_testo("""
Ti svegli in una stanza misteriosa...
Le pareti sono coperte di formule matematiche.
C'è una porta chiusa con 5 lucchetti.

Ogni lucchetto richiede la soluzione di un enigma di COMBINATORIA.
Solo risolvendo tutti gli enigmi potrai fuggire!

La stanza si sta... restringendo? Meglio sbrigarsi!
        """, 0.02)

        input("\n⏎ Premi INVIO per iniziare...")

    def enigma_1_codice_cassaforte(self):
        """Permutazioni: codice di una cassaforte"""
        print("\n" + "="*70)
        print("🔒 LUCCHETTO 1: LA CASSAFORTE")
        print("="*70)

        self.animazione_testo("""
Trovi una cassaforte con un display digitale.
C'è un biglietto accanto:

"Il codice è composto da 4 cifre DIVERSE scelte tra: 1, 2, 3, 4, 5
Quante combinazioni possibili ci sono?"

SUGGERIMENTO: Si tratta di DISPOSIZIONI (l'ordine conta!)
Formula: D(n,k) = n!/(n-k)! = P(n,k)
        """)

        print("\n📝 Calcola il numero di combinazioni possibili:")
        n = 5  # cifre disponibili
        k = 4  # cifre da scegliere

        risposta_corretta = perm(n, k)

        while True:
            try:
                risposta = int(input("Quante combinazioni possibili? "))

                if risposta == risposta_corretta:
                    print("\n✅ CORRETTO!")
                    print(f"   D(5,4) = 5!/(5-4)! = 5!/1! = 120")
                    print(f"   Ci sono infatti {risposta_corretta} modi di disporre 4 cifre tra 5!")
                    time.sleep(2)
                    print("\n🔓 *CLICK* Il primo lucchetto si apre!")
                    self.enigmi_risolti += 1
                    break
                else:
                    self.tentativi_falliti += 1
                    print(f"\n❌ Sbagliato! La cassaforte emette un suono sinistro...")
                    print(f"   Suggerimento: D(n,k) = n × (n-1) × ... × (n-k+1)")
                    print(f"   Con n=5 cifre e k=4 posizioni: 5 × 4 × 3 × 2 = ?")

            except ValueError:
                print("❌ Inserisci un numero!")

    def enigma_2_comitato(self):
        """Combinazioni: scegliere membri di un comitato"""
        print("\n" + "="*70)
        print("🔒 LUCCHETTO 2: IL COMITATO SEGRETO")
        print("="*70)

        self.animazione_testo("""
Sul muro appare una scritta luminosa:

"Un comitato segreto di 10 membri deve eleggere un sottogruppo di 3 leader.
L'ordine NON importa (non ci sono gerarchie).
In quanti modi diversi possono scegliere i 3 leader?"

SUGGERIMENTO: Si tratta di COMBINAZIONI (l'ordine NON conta!)
Formula: C(n,k) = n! / (k!(n-k)!)
        """)

        print("\n📝 Calcola il numero di modi:")
        n = 10
        k = 3

        risposta_corretta = comb(n, k)

        while True:
            try:
                risposta = int(input("Quanti modi possibili? "))

                if risposta == risposta_corretta:
                    print("\n✅ ESATTO!")
                    print(f"   C(10,3) = 10! / (3! × 7!) = {risposta_corretta}")
                    print(f"   = (10 × 9 × 8) / (3 × 2 × 1) = 720 / 6 = 120")
                    time.sleep(2)
                    print("\n🔓 *CLICK* Il secondo lucchetto cede!")
                    self.enigmi_risolti += 1
                    break
                else:
                    self.tentativi_falliti += 1
                    print(f"\n❌ No! Le pareti si avvicinano un po'...")
                    print(f"   Ricorda: C(n,k) = C(10,3) = 10!/(3!×7!)")

            except ValueError:
                print("❌ Inserisci un numero!")

    def enigma_3_anagrammi(self):
        """Permutazioni: anagrammi di una parola"""
        print("\n" + "="*70)
        print("🔒 LUCCHETTO 3: GLI ANAGRAMMI")
        print("="*70)

        self.animazione_testo("""
Una tastiera magica appare dal pavimento.
Sopra c'è scritto:

"La parola chiave è: ROMA
Quanti anagrammi diversi si possono formare con queste 4 lettere?"

SUGGERIMENTO: Permutazioni di n elementi
Formula: P(n) = n!
        """)

        print("\n📝 Calcola il numero di anagrammi:")
        n = 4  # lettere in ROMA

        risposta_corretta = factorial(n)

        while True:
            try:
                risposta = int(input("Quanti anagrammi? "))

                if risposta == risposta_corretta:
                    print("\n✅ PERFETTO!")
                    print(f"   P(4) = 4! = 4 × 3 × 2 × 1 = {risposta_corretta}")
                    print(f"   Alcuni esempi: ROMA, RAMO, MORA, ARMO, OMAR, ...")
                    time.sleep(2)
                    print("\n🔓 *CLICK* Il terzo lucchetto si sblocca!")
                    self.enigmi_risolti += 1
                    break
                else:
                    self.tentativi_falliti += 1
                    print(f"\n❌ Errore! Il soffitto scende leggermente...")
                    print(f"   Con 4 lettere diverse: 4! = 4 × 3 × 2 × 1 = ?")

            except ValueError:
                print("❌ Inserisci un numero!")

    def enigma_4_pizza(self):
        """Combinazioni: toppings della pizza"""
        print("\n" + "="*70)
        print("🔒 LUCCHETTO 4: LA PIZZA PERFETTA")
        print("="*70)

        self.animazione_testo("""
Appare un ologramma di una pizzeria...

"Il pizzaiolo fantasma offre 8 ingredienti diversi:
Pomodoro, Mozzarella, Prosciutto, Funghi, Olive, Peperoni, Salsiccia, Cipolla

Vuoi scegliere ESATTAMENTE 4 ingredienti per la tua pizza.
In quanti modi diversi puoi farlo?"

SUGGERIMENTO: Combinazioni (l'ordine degli ingredienti non conta!)
        """)

        print("\n📝 Calcola le possibili combinazioni:")
        n = 8  # ingredienti disponibili
        k = 4  # ingredienti da scegliere

        risposta_corretta = comb(n, k)

        while True:
            try:
                risposta = int(input("Quante pizze diverse? "))

                if risposta == risposta_corretta:
                    print("\n✅ BRAVISSIMO!")
                    print(f"   C(8,4) = 8! / (4! × 4!) = {risposta_corretta}")
                    print(f"   = (8 × 7 × 6 × 5) / (4 × 3 × 2 × 1) = 1680 / 24 = 70")
                    time.sleep(2)
                    print("\n🔓 *CLICK* Il quarto lucchetto si apre!")
                    print("   (E ti appare magicamente una pizza! 🍕)")
                    self.enigmi_risolti += 1
                    break
                else:
                    self.tentativi_falliti += 1
                    print(f"\n❌ Sbagliato! La stanza diventa più piccola...")
                    print(f"   Formula: C(8,4) = 8!/(4!×4!)")

            except ValueError:
                print("❌ Inserisci un numero!")

    def enigma_5_podio(self):
        """Permutazioni: podio di una gara"""
        print("\n" + "="*70)
        print("🔒 LUCCHETTO 5: IL PODIO FINALE")
        print("="*70)

        self.animazione_testo("""
L'ultimo enigma! La porta vibra...

"In una gara partecipano 12 atleti.
Quanti podi diversi (1°, 2°, 3° posto) sono possibili?
Ricorda: l'ordine è importante!"

SUGGERIMENTO: Disposizioni! Il 1° è diverso dal 2° è diverso dal 3°!
        """)

        print("\n📝 Calcola i possibili podi:")
        n = 12  # atleti
        k = 3   # posizioni sul podio

        risposta_corretta = perm(n, k)

        while True:
            try:
                risposta = int(input("Quanti podi possibili? "))

                if risposta == risposta_corretta:
                    print("\n✅ FENOMENALE!!!")
                    print(f"   D(12,3) = 12!/(12-3)! = 12!/9!")
                    print(f"   = 12 × 11 × 10 = {risposta_corretta}")
                    time.sleep(2)
                    print("\n🔓 *CLICK* L'ULTIMO LUCCHETTO SI APRE!")
                    self.enigmi_risolti += 1
                    break
                else:
                    self.tentativi_falliti += 1
                    print(f"\n❌ No! La porta emette scintille...")
                    print(f"   Con 12 atleti e 3 posizioni: 12 × 11 × 10 = ?")

            except ValueError:
                print("❌ Inserisci un numero!")

    def finale(self):
        """Sequenza finale di fuga"""
        print("\n" + "="*70)
        tempo_finale = self.mostra_tempo()

        self.animazione_testo("""
🎉🎉🎉 TUTTI I LUCCHETTI APERTI! 🎉🎉🎉

La porta si apre lentamente con un cigolio...
Una luce abbagliante invade la stanza!

Corri verso l'uscita...
        """, 0.04)

        time.sleep(1)

        print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              🏆 MISSIONE COMPLETATA! 🏆                   ║
║                                                           ║
║            SEI FUGGITO DALL'ESCAPE ROOM!                 ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)

        print(f"\n📊 STATISTICHE:")
        print(f"   ⏱️  Tempo impiegato: {tempo_finale}")
        print(f"   ✅ Enigmi risolti: {self.enigmi_risolti}/5")
        print(f"   ❌ Tentativi falliti: {self.tentativi_falliti}")

        if self.tentativi_falliti == 0:
            print(f"\n🌟 PERFECT! Nessun errore! Sei un genio della combinatoria!")
        elif self.tentativi_falliti <= 3:
            print(f"\n⭐ Ottimo lavoro! Pochi errori!")
        else:
            print(f"\n💪 Ce l'hai fatta! Continua a studiare!")

        print(f"\n📚 COSA HAI IMPARATO:")
        print(f"   • Permutazioni: P(n) = n!")
        print(f"   • Disposizioni: D(n,k) = n!/(n-k)!")
        print(f"   • Combinazioni: C(n,k) = n!/(k!(n-k)!)")

    def gioca(self):
        """Funzione principale del gioco"""
        self.intro()

        # I 5 enigmi
        self.enigma_1_codice_cassaforte()
        self.enigma_2_comitato()
        self.enigma_3_anagrammi()
        self.enigma_4_pizza()
        self.enigma_5_podio()

        # Finale
        self.finale()


if __name__ == "__main__":
    room = EscapeRoom()
    room.gioca()
