# Es7: Campionamento e Nyquist

**Livello:** BASE-INTERMEDIO
**Durata stimata:** 4-5 ore

## Descrizione

Dimostrazione interattiva del teorema del campionamento di Nyquist-Shannon. Visualizza fenomeni di aliasing quando si campiona a frequenza insufficiente e la ricostruzione corretta usando interpolazione sinc.

## Obiettivi

### Competenze TLC
- Comprendere il teorema del campionamento di Nyquist
- Identificare frequenza di campionamento minima (Nyquist rate)
- Comprendere il fenomeno dell'aliasing
- Implementare filtri anti-aliasing
- Applicare interpolazione per ricostruzione

### Competenze Informatica
- Simulazione di processi di campionamento
- Visualizzazione di segnali continui e discreti
- Interpolazione numerica (lineare, sinc)
- Utilizzo di NumPy per operazioni vettoriali
- Manipolazione di segnali nel dominio tempo e frequenza

## Consegna

Il programma deve:

1. **Generare segnali sinusoidali:**
   - Segnale continuo a frequenza f_signal
   - Campionamento a frequenza fs
   - Visualizzazione comparativa

2. **Dimostrare il teorema di Nyquist:**
   - fs > 2 * f_max → ricostruzione corretta
   - fs < 2 * f_max → aliasing
   - Caso limite: fs = 2 * f_max (ambiguo)

3. **Visualizzare aliasing:**
   - Segnale originale (continuo)
   - Segnale campionato (punti discreti)
   - Segnale ricostituito (interpolazione)
   - Frequenza alias che appare

4. **Implementare filtri anti-aliasing:**
   - Filtra segnale prima del campionamento
   - Previene aliasing
   - Confronta con/senza filtro

5. **Ricostruzione mediante interpolazione:**
   - Interpolazione lineare semplice
   - Interpolazione sinc (ideale)
   - Confronta qualità ricostruzione

## Esempio di Utilizzo

```
=== TEOREMA DEL CAMPIONAMENTO E ALIASING ===

Parametri:
Frequenza segnale: 1000 Hz
Frequenza campionamento: 8000 Hz
Durata: 0.005 sec (5 periodi)

Analisi Nyquist:
├─ Frequenza Nyquist = fs/2 = 4000 Hz
├─ Frequenza segnale = 1000 Hz < 4000 Hz
├─ Condizione: ✓ SODDISFATTA
└─ Risultato: Ricostruzione CORRETTA

Segnale campionato:
- Numero campioni: 40
- Intervallo campionamento: 0.125 ms
- Banda occupata: 0-8000 Hz

[Grafico comparativo: segnale continuo vs campionato vs ricostruito]

--- CASO DI ALIASING ---

Frequenza segnale: 7000 Hz
Frequenza campionamento: 8000 Hz

Analisi Nyquist:
├─ Frequenza Nyquist = 4000 Hz
├─ Frequenza segnale = 7000 Hz > 4000 Hz
├─ Condizione: ✗ NON SODDISFATTA
└─ Risultato: ALIASING!

Frequenza alias apparente: |7000 - 8000| = 1000 Hz
Il segnale a 7000 Hz appare come 1000 Hz!

[Grafico: segnale originale a 7000 Hz vs alias a 1000 Hz]
```

## Suggerimenti

- Genera segnale continuo con tanti punti (es: 1000 punti/periodo)
- Campiona selezionando ogni N-esimo punto
- Per ricostruzione lineare: interpolazione tra campioni
- Implementa sinc ideale (o sinc windowed approssimato)
- Mostra sia dominio tempo che frequenza
- Usa colori diversi per segnale continuo/campionato/ricostruito
- Aggiungi filtro anti-aliasing (passa-basso prima campionamento)

## Esempio di Codice Struttura

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, interpolate

class CampionatoreSegnali:
    def __init__(self, fs):
        self.fs = fs  # Frequenza campionamento
        self.nyquist = fs / 2

    def genera_segnale_continuo(self, f_signal, durata, num_punti=1000):
        """Genera segnale sinusoidale continuo"""
        t_continuo = np.linspace(0, durata, num_punti)
        x_continuo = np.sin(2 * np.pi * f_signal * t_continuo)
        return t_continuo, x_continuo

    def campiona_segnale(self, t_continuo, x_continuo):
        """Campiona il segnale a frequenza fs"""
        # Intervallo campionamento
        Ts = 1 / self.fs
        # Indici dei campioni
        indici = np.arange(0, len(t_continuo),
                          len(t_continuo) / (self.fs * t_continuo[-1]))
        indici = indici.astype(int)
        indici = indici[indici < len(t_continuo)]

        t_campionato = t_continuo[indici]
        x_campionato = x_continuo[indici]

        return t_campionato, x_campionato

    def ricostruisci_lineare(self, t_campionato, x_campionato, t_continuo):
        """Ricostruzione mediante interpolazione lineare"""
        f = interpolate.interp1d(t_campionato, x_campionato,
                                kind='linear', fill_value='extrapolate')
        x_ricostruito = f(t_continuo)
        return x_ricostruito

    def ricostruisci_sinc(self, t_campionato, x_campionato, t_continuo):
        """Ricostruzione mediante interpolazione sinc"""
        x_ricostruito = np.zeros_like(t_continuo)

        for i, t in enumerate(t_continuo):
            # Sinc interpolation: x(t) = Σ x[n] * sinc(π(t - nTs)/Ts)
            sincsum = 0
            Ts = 1 / self.fs

            for n, x_n in enumerate(x_campionato):
                arg = np.pi * (t - t_campionato[n]) / Ts
                if np.abs(arg) < 1e-10:
                    sincsum += x_n
                else:
                    sincsum += x_n * np.sin(arg) / arg

            x_ricostruito[i] = sincsum

        return x_ricostruito

    def visualizza_campionamento(self, f_signal, durata=0.01):
        """Visualizza il processo di campionamento"""
        t_cont, x_cont = self.genera_segnale_continuo(f_signal, durata)
        t_camp, x_camp = self.campiona_segnale(t_cont, x_cont)
        x_ricost_lin = self.ricostruisci_lineare(t_camp, x_camp, t_cont)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        # Grafico 1: Segnale continuo vs campionato
        ax1.plot(t_cont, x_cont, 'b-', label='Segnale continuo', linewidth=2)
        ax1.scatter(t_camp, x_camp, color='red', s=100,
                   label='Campioni', zorder=5)
        ax1.set_ylabel('Ampiezza')
        ax1.set_title(f'Campionamento a fs={self.fs} Hz, f_signal={f_signal} Hz')
        ax1.legend()
        ax1.grid(True)

        # Grafico 2: Comparazione ricostruzioni
        ax2.plot(t_cont, x_cont, 'b-', label='Continuo', linewidth=2)
        ax2.plot(t_cont, x_ricost_lin, 'g--', label='Ricostruito (lineare)',
                linewidth=2)
        ax2.scatter(t_camp, x_camp, color='red', s=50, zorder=5)
        ax2.set_xlabel('Tempo (sec)')
        ax2.set_ylabel('Ampiezza')
        ax2.set_title('Ricostruzione del Segnale')
        ax2.legend()
        ax2.grid(True)

        plt.tight_layout()
        plt.show()

        # Analisi Nyquist
        print(f"\nAnalisi Campionamento:")
        print(f"├─ Frequenza segnale: {f_signal} Hz")
        print(f"├─ Frequenza campionamento: {self.fs} Hz")
        print(f"├─ Frequenza Nyquist: {self.nyquist} Hz")
        print(f"├─ Condizione fs > 2*f: {self.fs > 2*f_signal}")
        if self.fs > 2*f_signal:
            print(f"└─ Risultato: ✓ RICOSTRUZIONE CORRETTA")
        else:
            alias_freq = np.abs(f_signal - self.fs)
            print(f"└─ Risultato: ✗ ALIASING a {alias_freq} Hz")

# Utilizzo
campionatore = CampionatoreSegnali(fs=8000)

# Caso 1: Campionamento corretto
print("CASO 1: f_signal = 1000 Hz")
campionatore.visualizza_campionamento(f_signal=1000)

# Caso 2: Aliasing
print("\nCASO 2: f_signal = 7000 Hz (ALIASING!)")
campionatore.visualizza_campionamento(f_signal=7000)
```

## Teorema di Nyquist-Shannon

**Enunciato:** Un segnale band-limited con frequenza massima f_max può essere ricostruito esattamente dal suo campionamento se campionato a frequenza fs ≥ 2·f_max.

**Conseguenze:**
- Nyquist rate = 2·f_max (minimo teorico)
- fs/2 = frequenza di Nyquist (massima frequenza rappresentabile)
- Se fs < 2·f_max → aliasing

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 📏📊**
