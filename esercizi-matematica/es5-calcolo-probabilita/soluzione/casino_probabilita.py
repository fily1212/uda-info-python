# 🎰 CASINÒ DELLA PROBABILITÀ - SOLUZIONE
# Impara la probabilità giocando!

import random
import time

class CasinoProbabilita:
    def __init__(self):
        self.crediti = 100
        self.vittorie = 0
        self.sconfitte = 0

    def mostra_stato(self):
        print(f"\n💰 Crediti: {self.crediti} | ✅ Vittorie: {self.vittorie} | ❌ Sconfitte: {self.sconfitte}")

    def gioco_moneta(self):
        """STORIA: Un misterioso mercante ti sfida a testa o croce"""
        print("\n" + "="*60)
        print("🪙 GIOCO DELLA MONETA")
        print("="*60)
        print("\n📖 STORIA:")
        print("Un mercante ti ferma per strada...")
        print('"Scommetti! Indovina testa o croce e raddoppi i soldi!"')

        scommessa = int(input("\nQuanto vuoi scommettere? (max {}): ".format(self.crediti)))
        if scommessa > self.crediti or scommessa <= 0:
            print("❌ Scommessa non valida!")
            return

        scelta = input("Testa o Croce? (T/C): ").upper()

        print("\n🎬 Il mercante lancia la moneta...")
        time.sleep(1)
        print("⏳ La moneta gira in aria...")
        time.sleep(1)

        risultato = random.choice(['T', 'C'])
        print(f"🪙 Risultato: {'TESTA' if risultato == 'T' else 'CROCE'}!\n")

        if scelta == risultato:
            vincita = scommessa * 2
            self.crediti += scommessa
            self.vittorie += 1
            print(f"🎉 HAI VINTO! +{scommessa} crediti!")
            print(f"📊 Probabilità di vincita era: 50% (1/2)")
        else:
            self.crediti -= scommessa
            self.sconfitte += 1
            print(f"💔 Hai perso! -{scommessa} crediti")
            print(f"📊 Probabilità di perdita era: 50% (1/2)")

    def gioco_dadi_somma(self):
        """STORIA: Una scommessa su due dadi in una taverna"""
        print("\n" + "="*60)
        print("🎲🎲 SCOMMESSA DEI DUE DADI")
        print("="*60)
        print("\n📖 STORIA:")
        print("In una taverna, dei giocatori lanciano due dadi...")
        print('"Scommetti sulla somma! Se indovini, vinci 5 volte la posta!"')
        print("\n💡 SUGGERIMENTO: Quale somma è più probabile?")
        print("   - Somma 2: solo con 1+1 (1 modo)")
        print("   - Somma 7: con 1+6, 2+5, 3+4, 4+3, 5+2, 6+1 (6 modi!)")

        scommessa = int(input("\nQuanto scommetti? (max {}): ".format(self.crediti)))
        if scommessa > self.crediti or scommessa <= 0:
            print("❌ Scommessa non valida!")
            return

        scelta = int(input("Su quale somma scommetti? (2-12): "))
        if scelta < 2 or scelta > 12:
            print("❌ Somma non valida!")
            return

        print("\n🎬 I dadi vengono lanciati...")
        time.sleep(1)

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        somma = dado1 + dado2

        print(f"🎲 Dado 1: {dado1}")
        print(f"🎲 Dado 2: {dado2}")
        print(f"➕ Somma: {somma}\n")

        # Calcola probabilità
        prob_map = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
                   8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}

        if scelta == somma:
            vincita = scommessa * 5
            self.crediti += vincita - scommessa
            self.vittorie += 1
            print(f"🎉 INCREDIBILE! Hai indovinato!")
            print(f"💰 Vinci {vincita} crediti! (+{vincita - scommessa})")
        else:
            self.crediti -= scommessa
            self.sconfitte += 1
            print(f"❌ Non hai indovinato...")
            print(f"💸 Perdi {scommessa} crediti")

        print(f"\n📊 Probabilità di {scelta}: {prob_map[scelta]*100:.2f}%")
        print(f"📊 Probabilità di {somma}: {prob_map[somma]*100:.2f}%")
        print(f"💡 La somma più probabile è 7 (16.67%)")

    def gioco_tre_carte(self):
        """STORIA: Il classico gioco delle tre carte"""
        print("\n" + "="*60)
        print("🃏 GIOCO DELLE TRE CARTE")
        print("="*60)
        print("\n📖 STORIA:")
        print("Un imbonitore mescola tre carte sul tavolo...")
        print('"Trova la Regina di Cuori e vinci il triplo!"')
        print("\n🎴 Ci sono: Regina di Cuori ❤️, Fante di Picche ♠️, Re di Fiori ♣️")

        scommessa = int(input("\nQuanto scommetti? (max {}): ".format(self.crediti)))
        if scommessa > self.crediti or scommessa <= 0:
            print("❌ Scommessa non valida!")
            return

        # Mescola
        carte = ['Regina❤️', 'Fante♠️', 'Re♣️']
        random.shuffle(carte)

        print("\n🎬 L'imbonitore mescola le carte...")
        time.sleep(1)
        print("🃏 🃏 🃏")
        print("1️⃣  2️⃣  3️⃣")

        scelta = int(input("\nQuale carta scegli? (1-3): "))
        if scelta < 1 or scelta > 3:
            print("❌ Scelta non valida!")
            return

        print(f"\n🎬 Giri la carta {scelta}...")
        time.sleep(1)

        carta_scelta = carte[scelta - 1]
        print(f"\n🃏 Hai pescato: {carta_scelta}!")

        if 'Regina' in carta_scelta:
            vincita = scommessa * 3
            self.crediti += vincita - scommessa
            self.vittorie += 1
            print(f"\n🎉 FANTASTICO! Hai trovato la Regina!")
            print(f"💰 Vinci {vincita} crediti! (+{vincita - scommessa})")
        else:
            self.crediti -= scommessa
            self.sconfitte += 1
            print(f"\n❌ Non è la Regina... Era la carta {carte.index('Regina❤️') + 1}!")
            print(f"💸 Perdi {scommessa} crediti")

        print(f"\n📊 Probabilità di vincita: 33.33% (1/3)")
        print(f"📊 Probabilità di perdita: 66.67% (2/3)")

    def lezione_probabilita(self):
        """Lezione interattiva sulla probabilità"""
        print("\n" + "="*60)
        print("📚 LEZIONE: PROBABILITÀ E VINCITE")
        print("="*60)

        print("""
La probabilità si calcola così:
P(evento) = casi favorevoli / casi possibili

Esempi dai giochi:
🪙 Moneta: P(Testa) = 1/2 = 50%
🎲 Due dadi somma 7: P(7) = 6/36 = 16.67%
🃏 Tre carte (Regina): P(Regina) = 1/3 = 33.33%

EVENTI INDIPENDENTI:
La probabilità di due eventi che accadono insieme:
P(A e B) = P(A) × P(B)

Esempio: Probabilità di fare TESTA due volte di fila?
P(T e T) = 1/2 × 1/2 = 1/4 = 25%

EVENTI COMPLEMENTARI:
P(non A) = 1 - P(A)

Esempio: Probabilità di NON fare 7 con due dadi?
P(non 7) = 1 - 6/36 = 30/36 = 83.33%
        """)

        input("\nPremi INVIO per continuare...")

    def gioca(self):
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║        🎰 BENVENUTO AL CASINÒ DELLA PROBABILITÀ! 🎰      ║
║                                                          ║
║  Impara la probabilità giocando e scommettendo!         ║
║  Parti con 100 crediti. Riesci ad arrivare a 200?       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
        """)

        while self.crediti > 0:
            self.mostra_stato()

            if self.crediti >= 200:
                print("\n🏆🏆🏆 CONGRATULAZIONI! HAI VINTO IL CASINÒ! 🏆🏆🏆")
                print("Hai dimostrato di capire la probabilità!")
                break

            print("\n" + "-"*60)
            print("MENU GIOCHI:")
            print("1. 🪙 Testa o Croce (50% di vincita)")
            print("2. 🎲 Somma di Due Dadi (varia 2.78%-16.67%)")
            print("3. 🃏 Tre Carte (33.33% di vincita)")
            print("4. 📚 Lezione sulla Probabilità")
            print("5. 🚪 Esci dal casinò")

            scelta = input("\nCosa vuoi fare? (1-5): ")

            if scelta == '1':
                self.gioco_moneta()
            elif scelta == '2':
                self.gioco_dadi_somma()
            elif scelta == '3':
                self.gioco_tre_carte()
            elif scelta == '4':
                self.lezione_probabilita()
            elif scelta == '5':
                break
            else:
                print("❌ Scelta non valida!")

        if self.crediti <= 0:
            print("\n💔 Hai finito i crediti! GAME OVER")
            print("💡 Ricorda: la casa vince sempre... a meno che non capisci la probabilità!")

        print(f"\n📊 STATISTICHE FINALI:")
        print(f"   Crediti finali: {self.crediti}")
        print(f"   Vittorie: {self.vittorie}")
        print(f"   Sconfitte: {self.sconfitte}")
        if self.vittorie + self.sconfitte > 0:
            win_rate = self.vittorie / (self.vittorie + self.sconfitte) * 100
            print(f"   Percentuale vittorie: {win_rate:.1f}%")


if __name__ == "__main__":
    casino = CasinoProbabilita()
    casino.gioca()
