# Es4: Analizzatore di Spettro

**Livello:** INTERMEDIO
**Durata stimata:** 6-7 ore

## Descrizione

Analizzatore di spettro software che utilizza FFT (Fast Fourier Transform) per visualizzare il contenuto frequenziale di segnali. Include water-fall plot e spettrogramma per analizzare segnali variabili nel tempo.

## Obiettivi

### Competenze TLC
- Comprendere la trasformata di Fourier discreta (DFT/FFT)
- Analizzare il contenuto frequenziale di segnali
- Identificare componenti armoniche e rumore
- Comprendere concetti di banda, risoluzione frequenziale
- Implementare filtri nel dominio della frequenza

### Competenze Informatica
- Utilizzo di librerie FFT (NumPy, SciPy)
- Manipolazione e visualizzazione di dati ad alta dimensionalità
- Spettrogrammi (Short-Time Fourier Transform - STFT)
- Visualizzazione 2D/3D con matplotlib
- Gestione di grandi dataset audio/segnali

## Consegna

Il programma deve:

1. **Leggere e analizzare segnali:**
   - Carica file audio (WAV) o genera segnali sintetici
   - Campiona il segnale a frequenza definita (es: 44.1 kHz)
   - Applica finestra (Hann, Hamming) per ridurre spettral leakage

2. **Calcolare e visualizzare FFT:**
   - Trasformata di Fourier veloce (FFT)
   - Spettro di ampiezza: `|X(f)| = sqrt(Real^2 + Imag^2)`
   - Spettro di fase: `∠X(f) = atan2(Imag, Real)`
   - Scala logaritmica (dB) per migliore visualizzazione

3. **Implementare visualizzazioni:**
   - **Spettro:** Ampiezza vs Frequenza
   - **Spettrogramma:** Frequenza × Tempo (colore = intensità)
   - **Water-fall:** Evoluzione temporale dello spettro
   - **Spettro di potenza:** Potenza vs Frequenza

4. **Analizzare caratteristiche:**
   - Identifica picchi (componenti armoniche)
   - Calcola banda occupata
   - Stima SNR e noise floor
   - Rileva interferenze

## Esempio di Utilizzo

```
=== ANALIZZATORE DI SPETTRO ===

Scegli sorgente segnale:
1. Genera segnale sintetico (100Hz + rumore)
2. Carica file audio (WAV)
3. Genera segnale 3 sinusoidi (50Hz, 150Hz, 300Hz)
4. Esci

Scelta: 1

Parametri:
Frequenza campionamento: 44100 Hz
Durata: 1 sec
Risoluzione FFT: 2048 punti

Analisi completata:
- Picco principale: 100.0 Hz (-6.5 dB)
- Armoniche rilevate: 200 Hz (-15.2 dB), 300 Hz (-20.1 dB)
- Noise floor: -60 dB
- Banda occupata (-3dB): 95-105 Hz (10 Hz)

Visualizzazioni generate:
✓ Spettro ampiezza
✓ Spettrogramma (STFT)
✓ Water-fall 3D
```

## Suggerimenti

- Usa `np.fft.fft()` per trasformata veloce
- Applica finestra (`scipy.signal.windows`) prima di FFT
- Converti in dB: `10 * log10(|X(f)|^2 / X_ref^2)`
- Per spettrogramma usa `scipy.signal.spectrogram()` o STFT
- Usa colormaps viridis/magma per water-fall
- Normalizza le frequenze: `f = np.fft.fftfreq(N, 1/fs)`
- Filtra il DC (frequenza 0) per migliore scala

## Esempio di Codice Struttura

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

class AnalizzatoreSpettro:
    def __init__(self, fs=44100):
        self.fs = fs  # Frequenza campionamento

    def genera_segnale(self, frequenze=[100], durata=1, snr_db=20):
        """Genera segnale sintetico con armoniche"""
        t = np.arange(0, durata, 1/self.fs)
        segnale = np.zeros_like(t)

        for f in frequenze:
            segnale += np.sin(2 * np.pi * f * t)

        # Aggiungi rumore gaussiano
        potenza_segnale = np.mean(segnale**2)
        snr_lineare = 10**(snr_db/10)
        potenza_rumore = potenza_segnale / snr_lineare
        rumore = np.random.normal(0, np.sqrt(potenza_rumore), len(t))

        return segnale + rumore

    def analizza_fft(self, segnale):
        """Calcola FFT e spettro"""
        # Applica finestra Hann
        finestra = signal.windows.hann(len(segnale))
        segnale_finestrato = segnale * finestra

        # FFT
        X = np.fft.fft(segnale_finestrato)
        freqs = np.fft.fftfreq(len(segnale), 1/self.fs)

        # Spettro ampiezza in dB
        ampiezza = np.abs(X)
        ampiezza_db = 20 * np.log10(ampiezza + 1e-10)

        return freqs, ampiezza_db

    def visualizza_spettro(self, segnale):
        """Visualizza spettro di ampiezza"""
        freqs, ampiezza_db = self.analizza_fft(segnale)

        # Mostra solo frequenze positive
        idx_pos = freqs > 0

        plt.figure(figsize=(12, 6))
        plt.plot(freqs[idx_pos], ampiezza_db[idx_pos], linewidth=1)
        plt.xlabel('Frequenza (Hz)')
        plt.ylabel('Ampiezza (dB)')
        plt.title('Spettro di Ampiezza')
        plt.grid(True)
        plt.xlim(0, self.fs/2)
        plt.show()

    def spettrogramma(self, segnale):
        """Calcola e visualizza spettrogramma"""
        f, t, Sxx = signal.spectrogram(segnale, fs=self.fs)

        plt.figure(figsize=(12, 6))
        plt.pcolormesh(t, f, 10*np.log10(Sxx + 1e-10), shading='gouraud')
        plt.ylabel('Frequenza (Hz)')
        plt.xlabel('Tempo (sec)')
        plt.title('Spettrogramma')
        plt.colorbar(label='Potenza (dB)')
        plt.show()

# Utilizzo
analizzatore = AnalizzatoreSpettro(fs=44100)
segnale = analizzatore.genera_segnale(frequenze=[100, 300], durata=2)
analizzatore.visualizza_spettro(segnale)
analizzatore.spettrogramma(segnale)
```

## Concetti Chiave

- **FFT:** Converte dominio tempo → dominio frequenza (O(N log N))
- **Risoluzione:** Δf = fs / N (dipende da lunghezza segnale)
- **Finestra:** Riduce spettral leakage (trade-off ampiezza/larghezza)
- **Spettrogramma:** STFT = FFT su finestre mobili
- **dB scale:** Rappresenta meglio il range dinamico

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🌈📊**
