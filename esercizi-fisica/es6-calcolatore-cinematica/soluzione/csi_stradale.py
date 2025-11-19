# 🚔 CSI STRADALE - Investigatore di Incidenti
# Usa la fisica per risolvere casi!

import numpy as np
import matplotlib.pyplot as plt
import time

class InvestigatoreCSI:
    def __init__(self):
        self.casi_risolti = 0
        self.g = 9.81  # accelerazione gravità

    def animazione_testo(self, testo):
        for char in testo:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()

    def intro(self):
        print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║          🚔 CSI STRADALE - INVESTIGATORE FISICO 🔍       ║
║                                                           ║
║  Usa la CINEMATICA per risolvere misteri stradali!      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)

        self.animazione_testo("""
Sei un investigatore della polizia scientifica.
Il tuo compito: usare la FISICA per scoprire la verità sugli incidenti!

Strumenti a disposizione:
- 📏 Metro laser per misurare distanze
- ⏱️  Cronometro di precisione
- 📸 Fotocamera per tracce di frenata
- 🧮 Calcolatrice scientifica
- 🧠 La tua conoscenza della cinematica!
        """)

        input("\n⏎ Premi INVIO per iniziare le investigazioni...")

    def caso_1_eccesso_velocita(self):
        """Moto uniforme: calcolare velocità da spazio e tempo"""
        print("\n" + "="*70)
        print("🚨 CASO 1: ECCESSO DI VELOCITÀ")
        print("="*70)

        self.animazione_testo("""
📋 RAPPORTO:
Luogo: Autostrada A1, km 245
Ora: 03:30 AM

Un'auto è stata fermata per eccesso di velocità.
L'autista nega: "Stavo rispettando il limite di 130 km/h!"

I tutor automatici hanno registrato:
- Ingresso casello Sud: ore 03:00:00
- Uscita casello Nord: ore 03:30:00
- Distanza tra i caselli: 75 km

DOMANDA: Qual era la velocità MEDIA dell'auto?
Stava davvero rispettando il limite?
        """)

        print("\n🔬 ANALISI:")
        print("Formula: v = s/t (velocità = spazio / tempo)")
        print("\nDati:")
        print(f"  s = 75 km")
        print(f"  t = 30 minuti = 0.5 ore")

        # L'utente deve calcolare
        while True:
            try:
                risposta = float(input("\nQual era la velocità media (km/h)? "))
                velocita_corretta = 75 / 0.5

                if abs(risposta - velocita_corretta) < 1:
                    print(f"\n✅ CORRETTO!")
                    print(f"   v = s/t = 75 km / 0.5 h = {velocita_corretta:.0f} km/h")
                    print(f"\n📊 CONCLUSIONE:")
                    print(f"   Limite: 130 km/h")
                    print(f"   Velocità rilevata: {velocita_corretta:.0f} km/h")
                    print(f"   Eccesso: +{velocita_corretta - 130:.0f} km/h")
                    print(f"\n⚖️ VERDETTO: COLPEVOLE! Multa salata in arrivo! 💸")
                    self.casi_risolti += 1
                    break
                else:
                    print(f"❌ Ricontrolla i calcoli!")

            except ValueError:
                print("Inserisci un numero valido!")

        input("\n⏎ Premi INVIO per il prossimo caso...")

    def caso_2_frenata_emergenza(self):
        """Moto uniformemente accelerato: calcolare velocità iniziale"""
        print("\n" + "="*70)
        print("🚨 CASO 2: INVESTIMENTO PEDONALE")
        print("="*70)

        self.animazione_testo("""
📋 RAPPORTO:
Luogo: Via Roma, attraversamento pedonale
Ora: 14:20

Un pedone è stato investito.
L'autista sostiene: "Andavo a 30 km/h! Il limite in città!"

PROVE RACCOLTE:
- Tracce di frenata: 25 metri
- Condizioni asciutte (coeff. attrito: μ = 0.7)
- L'auto si è fermata dopo la frenata

DOMANDA: A che velocità andava REALMENTE prima di frenare?
        """)

        print("\n🔬 ANALISI:")
        print("Formula: v² = v0² + 2as")
        print("Dove:")
        print("  v = 0 (si ferma)")
        print("  v0 = velocità iniziale (incognita)")
        print("  a = decelerazione = -μ × g = -0.7 × 9.81 ≈ -6.87 m/s²")
        print("  s = 25 m (traccia frenata)")
        print("\nRisolvendo: v0 = √(-2as) = √(2 × 6.87 × 25)")

        # Calcoli
        a = -0.7 * self.g  # decelerazione
        s = 25  # metri
        v0_ms = np.sqrt(-2 * a * s)  # m/s
        v0_kmh = v0_ms * 3.6  # km/h

        while True:
            try:
                print("\n⚠️ Suggerimento: Calcola prima v0 in m/s, poi converti in km/h")
                risposta = float(input("Velocità iniziale (km/h)? "))

                if abs(risposta - v0_kmh) < 5:
                    print(f"\n✅ ESATTO!")
                    print(f"   v0 = √(2 × 6.87 × 25) = √343 ≈ {v0_ms:.1f} m/s")
                    print(f"   v0 = {v0_ms:.1f} × 3.6 = {v0_kmh:.1f} km/h")
                    print(f"\n📊 CONCLUSIONE:")
                    print(f"   Limite dichiarato: 30 km/h")
                    print(f"   Velocità reale: {v0_kmh:.1f} km/h")
                    print(f"   Eccesso: +{v0_kmh - 30:.1f} km/h")
                    print(f"\n⚖️ VERDETTO: COLPEVOLE! Stava andando al DOPPIO del limite!")
                    self.casi_risolti += 1

                    # Visualizza grafico
                    self.grafico_frenata(v0_ms, a, s)
                    break
                else:
                    print(f"❌ Ricontrolla! Usa v0 = √(-2as)")

            except ValueError:
                print("Inserisci un numero!")

        input("\n⏎ Premi INVIO per il prossimo caso...")

    def grafico_frenata(self, v0, a, s_tot):
        """Visualizza grafico della frenata"""
        t_stop = -v0 / a
        t = np.linspace(0, t_stop, 100)

        s = v0 * t + 0.5 * a * t**2
        v = v0 + a * t

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Posizione
        ax1.plot(t, s, 'b-', linewidth=2)
        ax1.axhline(y=s_tot, color='r', linestyle='--', label='Punto di arresto')
        ax1.set_xlabel('Tempo (s)')
        ax1.set_ylabel('Distanza (m)')
        ax1.set_title('🚗 Distanza di Frenata')
        ax1.grid(True, alpha=0.3)
        ax1.legend()

        # Velocità
        ax2.plot(t, v, 'r-', linewidth=2)
        ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        ax2.set_xlabel('Tempo (s)')
        ax2.set_ylabel('Velocità (m/s)')
        ax2.set_title('🚗 Velocità durante Frenata')
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('analisi_frenata.png', dpi=150)
        plt.show()
        print("📊 Grafico salvato: analisi_frenata.png")

    def caso_3_caduta_ponte(self):
        """Caduta libera: quanto è alto il ponte?"""
        print("\n" + "="*70)
        print("🚨 CASO 3: CADUTA DAL PONTE")
        print("="*70)

        self.animazione_testo("""
📋 RAPPORTO:
Luogo: Ponte sul fiume Po
Ora: 21:45

Un oggetto è caduto dal ponte nel fiume.
Dobbiamo determinare l'altezza del ponte per le misure di sicurezza.

PROVE RACCOLTE:
- Video della caduta dal cellulare di un testimone
- Analisi video: tempo di caduta = 3.2 secondi
- Oggetto partito da fermo

DOMANDA: Qual è l'altezza del ponte?
        """)

        print("\n🔬 ANALISI:")
        print("Caduta libera: h = ½gt²")
        print("Dove:")
        print(f"  g = {self.g} m/s²")
        print(f"  t = 3.2 s")

        t = 3.2
        h_corretta = 0.5 * self.g * t**2

        while True:
            try:
                risposta = float(input("\nAltezza del ponte (metri)? "))

                if abs(risposta - h_corretta) < 2:
                    print(f"\n✅ PERFETTO!")
                    print(f"   h = ½gt² = 0.5 × 9.81 × 3.2² = {h_corretta:.1f} m")

                    # Velocità impatto
                    v_impatto = self.g * t
                    print(f"\n⚠️ DATO AGGIUNTIVO:")
                    print(f"   Velocità impatto: v = gt = 9.81 × 3.2 = {v_impatto:.1f} m/s")
                    print(f"   ({v_impatto * 3.6:.1f} km/h)")
                    print(f"\n📊 CONCLUSIONE:")
                    print(f"   Ponte alto circa {h_corretta:.0f} metri")
                    print(f"   Necessario installare reti di protezione!")
                    self.casi_risolti += 1

                    # Grafico caduta
                    self.grafico_caduta_libera(t, h_corretta)
                    break
                else:
                    print(f"❌ Ricontrolla! Formula: h = ½gt²")

            except ValueError:
                print("Inserisci un numero!")

        input("\n⏎ Caso risolto! Premi INVIO...")

    def grafico_caduta_libera(self, t_tot, h_tot):
        """Visualizza caduta libera"""
        t = np.linspace(0, t_tot, 100)
        h = h_tot - 0.5 * self.g * t**2
        v = self.g * t

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Altezza
        ax1.plot(t, h, 'b-', linewidth=2)
        ax1.axhline(y=0, color='r', linestyle='--', label='Livello acqua')
        ax1.set_xlabel('Tempo (s)')
        ax1.set_ylabel('Altezza (m)')
        ax1.set_title('📏 Caduta Libera - Altezza')
        ax1.invert_yaxis()
        ax1.grid(True, alpha=0.3)
        ax1.legend()

        # Velocità
        ax2.plot(t, v, 'r-', linewidth=2)
        ax2.set_xlabel('Tempo (s)')
        ax2.set_ylabel('Velocità (m/s)')
        ax2.set_title('⚡ Velocità durante caduta')
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('analisi_caduta.png', dpi=150)
        plt.show()
        print("📊 Grafico salvato: analisi_caduta.png")

    def finale(self):
        """Riepilogo finale"""
        print("\n" + "="*70)
        print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              🏆 INVESTIGAZIONI COMPLETATE! 🏆            ║
║                                                           ║
║         Hai usato la FISICA per fare GIUSTIZIA!         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)

        print(f"\n📊 CASI RISOLTI: {self.casi_risolti}/3")
        print(f"\n📚 FORMULE USATE:")
        print(f"   • Moto uniforme: v = s/t")
        print(f"   • Moto accelerato: v² = v0² + 2as")
        print(f"   • Caduta libera: h = ½gt²")
        print(f"\n💡 La fisica non mente! I numeri rivelano la verità!")

    def indaga(self):
        """Funzione principale"""
        self.intro()
        self.caso_1_eccesso_velocita()
        self.caso_2_frenata_emergenza()
        self.caso_3_caduta_ponte()
        self.finale()


if __name__ == "__main__":
    investigatore = InvestigatoreCSI()
    investigatore.indaga()
