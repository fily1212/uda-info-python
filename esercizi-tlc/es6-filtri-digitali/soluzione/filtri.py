# Filtri Digitali - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def filtro_passa_basso(fc=1000, fs=10000, order=5):
    """Filtro passa-basso Butterworth"""
    nyq = 0.5 * fs
    normal_cutoff = fc / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low')

    # Risposta in frequenza
    w, h = signal.freqz(b, a, worN=2000)
    freq = w * fs / (2 * np.pi)

    plt.figure(figsize=(10, 6))
    plt.plot(freq, 20 * np.log10(abs(h)), 'b')
    plt.title(f'Filtro Passa-Basso (fc={fc} Hz)')
    plt.xlabel('Frequenza (Hz)')
    plt.ylabel('Magnitudine (dB)')
    plt.grid(True)
    plt.axvline(fc, color='r', linestyle='--', label=f'fc={fc} Hz')
    plt.legend()
    plt.savefig('filtro.png', dpi=150)
    plt.show()

    print(f"🎛️ Filtro passa-basso creato (fc={fc} Hz, ordine={order})")

filtro_passa_basso(fc=1000, fs=10000, order=5)
