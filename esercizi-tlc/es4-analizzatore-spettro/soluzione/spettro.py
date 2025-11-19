# Analizzatore di Spettro FFT - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def analizza_spettro(frequenze=[440, 880], ampiezze=[1, 0.5], durata=1):
    fs = 8000  # freq campionamento
    t = np.linspace(0, durata, int(fs * durata))

    # Genera segnale composito
    segnale = np.zeros_like(t)
    for f, a in zip(frequenze, ampiezze):
        segnale += a * np.sin(2 * np.pi * f * t)

    # FFT
    N = len(segnale)
    fft_vals = fft(segnale)
    fft_freq = fftfreq(N, 1/fs)

    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Dominio tempo
    ax1.plot(t[:1000], segnale[:1000])
    ax1.set_xlabel('Tempo (s)')
    ax1.set_ylabel('Ampiezza')
    ax1.set_title('Segnale nel Tempo')
    ax1.grid(True, alpha=0.3)

    # Dominio frequenza
    ax2.plot(fft_freq[:N//2], np.abs(fft_vals[:N//2]))
    ax2.set_xlabel('Frequenza (Hz)')
    ax2.set_ylabel('Magnitudine')
    ax2.set_title('Spettro (FFT)')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('spettro.png', dpi=150)
    plt.show()

    print(f"🌈 Componenti spettrali: {frequenze} Hz")

analizza_spettro([440, 880, 1320], [1, 0.5, 0.25])
