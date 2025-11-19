# Modulazione Segnali - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def modulazione_AM(fc=1000, fm=100, m=0.5, durata=0.05):
    """Modulazione di Ampiezza"""
    fs = 50000  # frequenza campionamento
    t = np.linspace(0, durata, int(fs * durata))

    # Portante e modulante
    portante = np.cos(2 * np.pi * fc * t)
    modulante = np.cos(2 * np.pi * fm * t)

    # Segnale AM
    segnale_AM = (1 + m * modulante) * portante

    # Grafici
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8))

    # Segnale modulante
    ax1.plot(t[:500], modulante[:500], 'b-')
    ax1.set_title('Segnale Modulante')
    ax1.set_ylabel('Ampiezza')
    ax1.grid(True, alpha=0.3)

    # Portante
    ax2.plot(t[:500], portante[:500], 'r-')
    ax2.set_title(f'Portante (fc={fc} Hz)')
    ax2.set_ylabel('Ampiezza')
    ax2.grid(True, alpha=0.3)

    # Segnale AM
    ax3.plot(t[:500], segnale_AM[:500], 'g-')
    ax3.set_title(f'Segnale AM (m={m})')
    ax3.set_xlabel('Tempo (s)')
    ax3.set_ylabel('Ampiezza')
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('modulazione_AM.png', dpi=150)
    plt.show()

    print(f"\n📡 MODULAZIONE AM")
    print(f"   Frequenza portante: {fc} Hz")
    print(f"   Frequenza modulante: {fm} Hz")
    print(f"   Indice modulazione: {m}")
    print(f"   Larghezza banda: {2*fm} Hz\n")

def modulazione_FM(fc=1000, fm=100, beta=5, durata=0.05):
    """Modulazione di Frequenza"""
    fs = 50000
    t = np.linspace(0, durata, int(fs * durata))

    modulante = np.cos(2 * np.pi * fm * t)

    # Segnale FM
    segnale_FM = np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

    plt.figure(figsize=(12, 6))
    plt.plot(t[:1000], segnale_FM[:1000], 'b-')
    plt.title(f'Modulazione FM (fc={fc} Hz, fm={fm} Hz, β={beta})')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Ampiezza')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('modulazione_FM.png', dpi=150)
    plt.show()

    print(f"📡 MODULAZIONE FM")
    print(f"   Deviazione freq: {beta * fm} Hz")
    print(f"   Larghezza banda (Carson): {2*(beta+1)*fm} Hz\n")

def modulazione_PM(fc=1000, fm=100, phi_m=np.pi/2, durata=0.05):
    """Modulazione di Fase"""
    fs = 50000
    t = np.linspace(0, durata, int(fs * durata))

    modulante = np.cos(2 * np.pi * fm * t)
    segnale_PM = np.cos(2 * np.pi * fc * t + phi_m * modulante)

    plt.figure(figsize=(12, 6))
    plt.plot(t[:1000], segnale_PM[:1000], 'r-')
    plt.title(f'Modulazione PM (fc={fc} Hz, φₘ={phi_m:.2f} rad)')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Ampiezza')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('modulazione_PM.png', dpi=150)
    plt.show()

def main():
    print("=== SIMULATORE MODULAZIONI ===\n")
    print("1. Modulazione AM")
    print("2. Modulazione FM")
    print("3. Modulazione PM")

    scelta = input("\nScegli (1-3): ")

    if scelta == "1":
        modulazione_AM(fc=1000, fm=50, m=0.7)
    elif scelta == "2":
        modulazione_FM(fc=1000, fm=50, beta=5)
    elif scelta == "3":
        modulazione_PM(fc=1000, fm=50, phi_m=np.pi/2)

if __name__ == "__main__":
    main()
