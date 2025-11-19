# Es6: Filtri Digitali

**Livello:** INTERMEDIO-AVANZATO
**Durata stimata:** 7-8 ore

## Descrizione

Progettazione e implementazione di filtri digitali FIR e IIR (passa-basso, passa-alto, passa-banda). Analisi della risposta in frequenza, fase, gruppo-ritardo e validazione della stabilità con diagrammi di Bode e poli-zeri.

## Obiettivi

### Competenze TLC
- Comprendere la teoria dei filtri digitali (FIR vs IIR)
- Progettare filtri con specifiche di banda
- Analizzare risposta in frequenza e fase
- Comprendere concetti di stabilità e causalità
- Applicare finestre (Hamming, Blackman) per design FIR

### Competenze Informatica
- Utilizzo di librerie DSP (scipy.signal)
- Implementazione di equazioni alle differenze
- Visualizzazione di risposta in frequenza (Bode, poli-zeri)
- Applicazione di filtri a segnali reali
- Validazione numerica della stabilità

## Consegna

Il programma deve:

1. **Filtri FIR (Finite Impulse Response):**
   - Progettazione con finestre (Hamming, Hann, Blackman)
   - Specifiche: ordine, frequenza taglio, attuazione
   - Equazione differenza: y[n] = Σ b[k]*x[n-k]
   - Sempre stabile (poli in z=0)

2. **Filtri IIR (Infinite Impulse Response):**
   - Progettazione Butterworth, Chebyshev
   - Specifiche: ordine, Rp (ripple), Rs (attenuazione)
   - Equazione differenza: y[n] = Σ b[k]*x[n-k] - Σ a[k]*y[n-k]
   - Verifica poli dentro cerchio unitario (stabilità)

3. **Tipi di filtri:**
   - **Passa-basso:** Taglia alte frequenze
   - **Passa-alto:** Taglia basse frequenze
   - **Passa-banda:** Taglia basse e alte
   - **Elimina-banda (notch):** Elimina banda stretta

4. **Visualizzazioni:**
   - Risposta in ampiezza (mag. lineare e dB)
   - Risposta in fase
   - Gruppo-ritardo (group delay)
   - Diagramma poli-zeri
   - Diagrammi di Bode

5. **Applicazione pratica:**
   - Filtra segnale rumoroso
   - Confronta FIR vs IIR
   - Analizza latenza e ordine

## Esempio di Utilizzo

```
=== PROGETTATORE FILTRI DIGITALI ===

Scegli tipo filtro:
1. FIR passa-basso (Hamming)
2. IIR passa-basso (Butterworth)
3. IIR passa-banda (Chebyshev)
4. Confronta FIR vs IIR
5. Esci

Scelta: 1

Parametri FIR passa-basso:
Frequenza campionamento: 8000 Hz
Frequenza taglio: 1000 Hz
Ordine filtro: 51
Finestra: Hamming

Filtro progettato:
├─ Tipo: FIR (Finite Impulse Response)
├─ Ordine: 51
├─ Coefficienti: 52
├─ Stabilità: Garantita (FIR)
├─ Latenza: 25.5 ms
├─ Banda transizione: ~500 Hz
└─ Attenuazione stopband: ~53 dB

Risposta in frequenza:
┌──────┐
│ ┐    │ Passa-basso: 0-1000 Hz
│ │ ┌──┼─┐
│ │ │  │ │
└─┴─┴──┼─┴──────────────────────
  0   1k      4k      8k Hz

Caratteristiche:
✓ Risposta piatta in banda passante
✓ Transizione netta attorno a 1 kHz
✗ Latenza di gruppo costante (25.5 ms)
```

## Suggerimenti

- Usa `scipy.signal.firwin()` per design FIR
- Usa `scipy.signal.butter()`, `cheby1()` per design IIR
- Visualizza risposta: `scipy.signal.freqz()`
- Controlla stabilità IIR: poli di `scipy.signal.pole_zero_gain()`
- Applica filtro: `scipy.signal.lfilter()` o `sosfilt()`
- Usa second-order sections (SOS) per IIR numericamente stabili
- Confronta latenza: FIR lineare vs IIR (group delay)

## Esempio di Codice Struttura

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

class ProgettatoreFiltri:
    def __init__(self, fs=8000):
        self.fs = fs  # Frequenza campionamento

    def progetta_fir_passa_basso(self, fc, ordine, finestra='hamming'):
        """Progetta filtro FIR passa-basso con finestra"""
        # Normalizza frequenza di taglio (0-1, dove 1 = fs/2)
        fc_norm = fc / (self.fs / 2)

        # Progettazione
        coefficienti = signal.firwin(ordine + 1, fc_norm, window=finestra)

        return coefficienti

    def progetta_iir_passa_basso(self, fc, ordine, tipo='butter'):
        """Progetta filtro IIR passa-basso"""
        fc_norm = fc / (self.fs / 2)

        if tipo == 'butter':
            b, a = signal.butter(ordine, fc_norm, btype='low')
        elif tipo == 'cheby1':
            b, a = signal.cheby1(ordine, rp=0.5, Wn=fc_norm, btype='low')

        return b, a

    def analizza_filtro_fir(self, coefficienti):
        """Analizza risposta filtro FIR"""
        w, h = signal.freqz(coefficienti, [1])

        # Converti frequenza normalizzata a Hz
        freqs = w * self.fs / (2 * np.pi)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        # Risposta in ampiezza (dB)
        ax1.plot(freqs, 20 * np.log10(np.abs(h)))
        ax1.set_ylabel('Ampiezza (dB)')
        ax1.set_title('Risposta in Ampiezza')
        ax1.grid(True)
        ax1.set_xlim(0, self.fs/2)

        # Risposta in fase
        ax2.plot(freqs, np.angle(h) * 180 / np.pi)
        ax2.set_ylabel('Fase (gradi)')
        ax2.set_xlabel('Frequenza (Hz)')
        ax2.set_title('Risposta in Fase')
        ax2.grid(True)
        ax2.set_xlim(0, self.fs/2)

        plt.tight_layout()
        plt.show()

    def analizza_filtro_iir(self, b, a):
        """Analizza risposta filtro IIR e stabilità"""
        # Risposta in frequenza
        w, h = signal.freqz(b, a)
        freqs = w * self.fs / (2 * np.pi)

        # Poli e zeri
        z, p, k = signal.tf2zpk(b, a)

        fig = plt.figure(figsize=(14, 5))

        # Risposta ampiezza
        ax1 = fig.add_subplot(131)
        ax1.plot(freqs, 20 * np.log10(np.abs(h)))
        ax1.set_ylabel('Ampiezza (dB)')
        ax1.set_title('Risposta Ampiezza')
        ax1.grid(True)
        ax1.set_xlim(0, self.fs/2)

        # Risposta fase
        ax2 = fig.add_subplot(132)
        ax2.plot(freqs, np.angle(h) * 180 / np.pi)
        ax2.set_ylabel('Fase (gradi)')
        ax2.set_title('Risposta Fase')
        ax2.grid(True)
        ax2.set_xlim(0, self.fs/2)

        # Poli-zeri
        ax3 = fig.add_subplot(133)
        # Cerchio unitario
        theta = np.linspace(0, 2*np.pi, 100)
        ax3.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3)

        # Zeri (O) e Poli (X)
        ax3.scatter(np.real(z), np.imag(z), marker='o',
                   s=100, c='blue', label='Zeri')
        ax3.scatter(np.real(p), np.imag(p), marker='x',
                   s=100, c='red', label='Poli')

        ax3.set_xlabel('Parte Reale')
        ax3.set_ylabel('Parte Immaginaria')
        ax3.set_title('Poli-Zeri')
        ax3.grid(True)
        ax3.legend()
        ax3.axis('equal')

        plt.tight_layout()
        plt.show()

        # Verifica stabilità
        stabilita = all(np.abs(p) < 1)
        print(f"Stabilità: {'✓ STABILE' if stabilita else '✗ INSTABILE'}")

    def applica_filtro(self, segnale, b, a):
        """Applica filtro IIR a segnale"""
        y = signal.lfilter(b, a, segnale)
        return y

# Utilizzo
progettatore = ProgettatoreFiltri(fs=8000)

# Progettazione FIR
coef_fir = progettatore.progetta_fir_passa_basso(fc=1000, ordine=51)
progettatore.analizza_filtro_fir(coef_fir)

# Progettazione IIR
b, a = progettatore.progetta_iir_passa_basso(fc=1000, ordine=4, tipo='butter')
progettatore.analizza_filtro_iir(b, a)
```

## Concetti Chiave

- **FIR:** Sempre stabile, fase lineare possibile, ordine alto
- **IIR:** Ordine basso, feedback, verifica stabilità necessaria
- **Gruppo-ritardo:** Ritardo in ogni frequenza
- **Transizione:** Band width tra passante e stopband
- **Finestra:** Trade-off main lobe width vs side lobes

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🎛️📊**
