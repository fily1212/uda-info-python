# ES02 - Grafici e Visualizzazione di Segnali 📊

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐ FACILE |
| **Durata Stimata** | 3-4 ore |
| **Linguaggio** | Python 3.8+ |
| **Librerie Richieste** | matplotlib, numpy |
| **Prerequisiti** | ES01 Segnali Sinusoidali completato |
| **Argomento TLC** | Visualizzazione e analisi segnali |

---

## 🎓 Concetti Fondamentali

### Perché Visualizzare i Segnali? 📈
In telecomunicazioni, il **grafico di un segnale** è spesso più informativo che i numeri:
- Individuare **anomalie** a occhio
- Misurare **ampiezza, periodo, frequenza**
- Confrontare **segnali diversi**
- Osservare **interferenze e distorsioni**
- Analizzare **spettro di frequenza** (FFT)

### Tipi di Segnali da Visualizzare 〰️

#### Segnale Sinusoidale (Puro)
```
y(t) = A × sin(2πft + φ)

Caratteristiche:
- Forma: curva liscia e periodica
- Frequenza costante
- Ampiezza costante
- Fase costante
```

#### Segnale Quadro (Rettangolare)
```
     │─┐ ┌─┐ ┌─┐
  A  │ │ │ │ │ │
     │─┘ └─┘ └─┘
     └──────────── t

Descrizione:
- Alterna fra valori min/max
- Transizioni istantanee (ideale)
- Frequenza costante
```

#### Segnale Triangolare
```
     │ ╱╲ ╱╲ ╱╲
  A  │╱  ╲╱  ╲╱  ╲
     └──────────── t

Descrizione:
- Rampa su/giù lineare
- Transizioni graduali
- Simmetrico
```

#### Segnale Dente di Sega
```
     │   ╱|   ╱|   ╱|
  A  │  ╱ |  ╱ |  ╱ |
     │ ╱  │ ╱  │ ╱  │
     └────────────────── t

Descrizione:
- Rampa lineare su, reset istantaneo
- Asimmetrico
```

#### Segnale Rumore
```
     │ ·´·´·´·´·´·´·´·´
  A  │·´·´·´·´·´·´·´·´·
     │´·´·´·´·´·´·´·´·´
     └──────────────────── t

Descrizione:
- Valori casuali
- Nessun periodo
```

### Parametri Visibili nel Grafico 🔍

```
        │        ┌─ Vmax = Ampiezza di picco
        │       ╱│╲
     A  │      ╱ │ ╲ ─┐
        │     ╱  │  ╲ ├─ Ampiezza picco-picco = 2A
        │────────┼──────
        │        │
    -A  │        └─ Vmin = -Ampiezza di picco
        │
        └────┼────────┼────┼────── t
          t0        T  t0+T
          └────────┘
        Periodo T = 1/f
```

### Matplotlib Basics 🎨

```python
import matplotlib.pyplot as plt

# Struttura base
fig, ax = plt.subplots()           # Crea figura e assi
ax.plot(x, y, 'b-', label='...')   # Traccia linea
ax.set_xlabel('Tempo (s)')          # Etichetta asse X
ax.set_ylabel('Ampiezza (V)')       # Etichetta asse Y
ax.set_title('Titolo Grafico')      # Titolo
ax.grid(True)                        # Griglia
ax.legend()                          # Legenda
plt.show()                           # Visualizza
```

---

## 📐 Formule e Generazione Segnali

### Campionamento e Array Temporale
```python
# Campionamento
fs = 44100 Hz  (sample rate, campioni al secondo)
T_campione = 1 / fs

# Generare array di tempi
import numpy as np
t = np.linspace(0, durata, num_campioni)
#   da 0 a durata, con num_campioni punti
```

### Segnale Sinusoidale 〰️
```
y(t) = A × sin(2πft + φ)

Implementazione:
y = A * np.sin(2 * np.pi * f * t + phi_radianti)
```

### Segnale Quadro ⬜
```
Definizione:
y(t) = {  +A,  se 0 ≤ (t mod T) < T/2
        { -A,  se T/2 ≤ (t mod T) < T

Implementazione:
from scipy.signal import square
y = A * square(2 * np.pi * f * t + phi)
```

### Segnale Triangolare 🔺
```
Definizione:
- Rampa su da -A a +A in T/2
- Rampa giù da +A a -A in T/2

Implementazione:
from scipy.signal import sawtooth
y = A * sawtooth(2 * np.pi * f * t + phi, width=0.5)
```

### Segnale Dente di Sega 🔻
```
Definizione:
- Rampa su da -A a +A in T
- Reset istantaneo

Implementazione:
from scipy.signal import sawtooth
y = A * sawtooth(2 * np.pi * f * t + phi)  # width=1 (default)
```

---

## 💻 Funzioni Python da Implementare

### Livello 1: Generazione Segnali di Base ✅

```python
import numpy as np
import matplotlib.pyplot as plt

def segnale_sinusoidale(ampiezza, frequenza, fase_gradi=0, durata=1, fs=1000):
    """
    Genera segnale sinusoidale.

    Args:
        ampiezza (float): Ampiezza A [V, A, ...]
        frequenza (float): Frequenza f [Hz]
        fase_gradi (float): Fase φ [gradi, default=0]
        durata (float): Durata segnale [secondi, default=1]
        fs (int): Sample rate [Hz, default=1000]

    Returns:
        tuple: (tempo_array, ampiezza_array)
        - tempo_array: np.array con istanti di tempo
        - ampiezza_array: np.array con valori segnale

    Esempio:
        >>> t, y = segnale_sinusoidale(10, 50, 0, 1, 1000)
        >>> len(t)
        1000
    """
    # 1. Convertire fase da gradi a radianti
    # 2. Generare array tempi con np.linspace()
    # 3. Calcolare segnale: y = A * sin(2πft + φ)
    # 4. Ritornare (t, y)


def segnale_quadro(ampiezza, frequenza, fase_gradi=0, durata=1, fs=1000):
    """
    Genera segnale quadro (rettangolare).

    Returns:
        tuple: (tempo_array, ampiezza_array)
    """
    # Usare scipy.signal.square oppure implementare manualmente


def segnale_triangolare(ampiezza, frequenza, fase_gradi=0, durata=1, fs=1000):
    """
    Genera segnale triangolare.

    Returns:
        tuple: (tempo_array, ampiezza_array)
    """
    # Usare scipy.signal.sawtooth con width=0.5


def segnale_dente_sega(ampiezza, frequenza, fase_gradi=0, durata=1, fs=1000):
    """
    Genera segnale dente di sega (sawtooth).

    Returns:
        tuple: (tempo_array, ampiezza_array)
    """
    # Usare scipy.signal.sawtooth con width=1
```

### Livello 2: Visualizzazione Singoli Segnali 📊

```python
def traccia_segnale(ampiezza, frequenza, tipo='sin', titolo=None, save_path=None):
    """
    Traccia singolo segnale nel tempo.

    Args:
        ampiezza (float): Ampiezza [V, A]
        frequenza (float): Frequenza [Hz]
        tipo (str): Tipo segnale ('sin', 'quadro', 'triangolo', 'sega')
        titolo (str): Titolo personalizzato (opzionale)
        save_path (str): Path per salvare immagine (opzionale)

    Returns:
        matplotlib.figure.Figure: Figura per test

    Comportamento:
        - Visualizza 2-3 periodi del segnale
        - Mostra griglia
        - Etichette assi comprensibili
        - Legenda con parametri (A, f, T)
    """
    # 1. Calcolare numero periodi da visualizzare
    # 2. Generare segnale opportuno
    # 3. Creare figura con plt.subplots()
    # 4. Tracciare segnale
    # 5. Aggiungere griglia, etichette, legenda
    # 6. Opzionale: salvare con plt.savefig()
    # 7. Ritornare figura


def estrai_parametri_visivi(t, y):
    """
    Estrae parametri dal segnale generato.

    Args:
        t (np.array): Array tempi
        y (np.array): Array valori segnale

    Returns:
        dict: {
            'ampiezza': A,
            'periodo_stimato': T,
            'frequenza_stimata': f,
            'valore_max': max(y),
            'valore_min': min(y),
            'valore_rms': rms
        }

    Nota: Importante per validare la generazione corretta!
    """
    # Calcolare statistiche dal segnale generato
```

### Livello 3: Segnali Sovrapposti 🎼

```python
def sovrapponi_segnali(segnali_lista, titolo=None, save_path=None):
    """
    Sovrappone più segnali sullo stesso grafico.

    Args:
        segnali_lista (list): Lista di tuple (tipo, A, f, φ)
            Esempio: [
                ('sin', 10, 50, 0),
                ('sin', 5, 100, 90),
                ('quadro', 8, 50, 0)
            ]
        titolo (str): Titolo personalizzato
        save_path (str): Path per salvare

    Returns:
        matplotlib.figure.Figure: Figura sovrapposta

    Comportamento:
        - Colori diversi per ogni segnale
        - Legenda con tipo e parametri
        - X-axis: tempo
        - Y-axis: ampiezza totale
    """
    # 1. Generare array tempi comune
    # 2. Generare ogni segnale
    # 3. Tracciare tutti con colori diversi
    # 4. Aggiungere legenda dettagliata
    # 5. Ritornare figura


def segnale_composito_somma(segnali_lista, durata=1, fs=1000):
    """
    Somma più segnali element-wise.

    Args:
        segnali_lista: Lista di (tipo, A, f, φ)
        durata: Durata totale
        fs: Sample rate

    Returns:
        tuple: (t_array, y_somma_array)
    """
    # Sommare i segnali: y_totale = Σ yi(t)
```

### Livello 4: Parametri e Misure 🔍

```python
def misura_periodo(t, y, metodo='zeri'):
    """
    Misura periodo dal segnale.

    Args:
        t (np.array): Array tempi
        y (np.array): Array valori
        metodo (str): 'zeri' (zero crossing) o 'picchi'

    Returns:
        float: Periodo stimato [s]

    Metodo 'zeri':
        - Trovare crossing dello zero
        - Distanza fra due crossing = mezza periodo
    """
    # Metodo zero crossing è più robusto


def misura_frequenza(t, y):
    """
    Misura frequenza dal segnale (inverso del periodo).

    Returns:
        float: Frequenza stimata [Hz]
    """
    # Usare misura_periodo


def misura_ampiezza(y):
    """
    Misura ampiezza dal segnale.

    Returns:
        dict: {
            'picco': max(y),
            'ampiezza': (max(y) - min(y)) / 2,
            'rms': √(mean(y²))
        }
    """


def disegna_parametri_su_grafico(t, y, titolo=None):
    """
    Traccia segnale con parametri evidenziati.

    Elementi visualizzati:
        - Segnale: linea continua
        - Ampiezza: linee orizzontali tratteggiate
        - Periodo: frecce orizzontali
        - Picchi/valli: punti evidenziati
    """
```

### Livello 5: Animazioni (Bonus) 🎬

```python
from matplotlib.animation import FuncAnimation

def anima_segnale(ampiezza, frequenza, durataAnimazione=5):
    """
    Crea animazione di segnale sinusoidale.

    Args:
        ampiezza: Ampiezza segnale
        frequenza: Frequenza segnale
        durataAnimazione: Durata animazione [s]

    Returns:
        matplotlib.animation.FuncAnimation

    Comportamento:
        - "Disegna" il segnale progressivamente
        - Mostra punto corrente in movimento
        - Aggiorna griglia per 5 secondi
    """
    # Usare FuncAnimation con update function
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### Esempio 1: Onda Radio FM 📻
```python
# Radio RaiRadio1 a 89.7 MHz
f_fm = 89.7e6  # Hz
A = 1          # Ampiezza normalizzata

t, y = segnale_sinusoidale(A, f_fm, durata=1e-6)  # 1 microsecondo
# Attenzione: 1 periodo @ 89.7 MHz = 11.1 ns
#             Occorrono TANTI campioni!

traccia_segnale(A, f_fm, tipo='sin', titolo='Onda FM 89.7 MHz')
```

### Esempio 2: Corrente Alternata in Casa ⚡
```python
# AC domestica: 230V @ 50 Hz
V_picco = 230 * np.sqrt(2)  # ~325V
f_ac = 50  # Hz

t, y = segnale_sinusoidale(V_picco, f_ac, durata=0.1)  # 100 ms = 5 periodi
traccia_segnale(V_picco, f_ac, tipo='sin', titolo='AC 230V 50Hz (Domestico)')
```

### Esempio 3: Segnale Audio 🎵
```python
# Nota La: 440 Hz
f_nota = 440  # Hz
durata = 2    # 2 secondi

t, y = segnale_sinusoidale(1, f_nota, durata=durata, fs=44100)
traccia_segnale(1, f_nota, tipo='sin', titolo='Nota La (440 Hz)')
```

### Esempio 4: Segnale PWM (Modulazione Larghezza Impulso) 🔌
```python
# PWM utilizzato nei circuiti digitali
f = 20000  # 20 kHz
durata = 1e-3  # 1 ms

t, y = segnale_quadro(1, f, durata=durata)
traccia_segnale(1, f, tipo='quadro', titolo='PWM 20 kHz')
```

### Esempio 5: Segnali Composti (Modulazione AM) 📶
```python
# AM: Portante (1 MHz) modulata da segnale audio (10 kHz)
f_portante = 1e6   # 1 MHz
f_modulante = 10e3  # 10 kHz

# Onda AM: s(t) = [A + m(t)] × cos(2πf_c×t)
# Dove m(t) = sin(2πf_m×t) è il segnale modulante

t = np.linspace(0, 0.005, 5000)  # 5 ms
modulante = 0.5 * np.sin(2 * np.pi * f_modulante * t)
portante = np.cos(2 * np.pi * f_portante * t)
segnale_am = (1 + modulante) * portante

plt.figure()
plt.plot(t, segnale_am)
plt.title('Segnale AM: Portante 1MHz Modulata da 10kHz')
plt.show()
```

---

## 🧪 Test Cases (8-10 casi)

```python
import numpy as np

# TEST 1: Segnale sinusoidale - lunghezza array
t, y = segnale_sinusoidale(10, 50, durata=1, fs=1000)
assert len(t) == len(y)
assert len(t) == 1000  # 1s × 1000 Hz

# TEST 2: Segnale sinusoidale - valori
t, y = segnale_sinusoidale(10, 50, fase_gradi=0, durata=0.02, fs=1000)
# Il primo campione (t≈0) dovrebbe avere y≈0
assert abs(y[0] - 0) < 0.1

# TEST 3: Segnale sinusoidale - fase 90°
t, y = segnale_sinusoidale(10, 50, fase_gradi=90, durata=0.02, fs=1000)
# t=0 con φ=90° dovrebbe avere y≈A
assert abs(y[0] - 10) < 0.1

# TEST 4: Segnale sinusoidale - ampiezza corretta
t, y = segnale_sinusoidale(5, 100, durata=0.1, fs=1000)
assert abs(max(y) - 5) < 0.01
assert abs(min(y) + 5) < 0.01

# TEST 5: Segnale quadro - alternanza
t, y = segnale_quadro(1, 100, durata=0.02, fs=10000)
# Un segnale quadro deve alternare fra +A e -A
valori_unici = set(np.round(y, 3))
assert len(valori_unici) <= 3  # +A, -A, e possibilmente 0

# TEST 6: Segnale triangolare - range
t, y = segnale_triangolare(2, 50, durata=0.04, fs=1000)
assert max(y) <= 2 + 0.01
assert min(y) >= -2 - 0.01

# TEST 7: Misura periodo corretto
t, y = segnale_sinusoidale(10, 100, durata=0.1, fs=10000)
periodo_misurato = misura_periodo(t, y)
periodo_atteso = 1 / 100  # 0.01 s
assert abs(periodo_misurato - periodo_atteso) < 0.001

# TEST 8: Misura frequenza corretta
t, y = segnale_sinusoidale(10, 200, durata=0.1, fs=10000)
freq_misurata = misura_frequenza(t, y)
assert abs(freq_misurata - 200) < 5  # Entro 5 Hz

# TEST 9: Segnali sovrapposti - somma corretta
t1, y1 = segnale_sinusoidale(5, 100, durata=0.02, fs=1000)
t2, y2 = segnale_sinusoidale(3, 100, durata=0.02, fs=1000)
t, y_soma = segnale_composito_somma([('sin', 5, 100, 0), ('sin', 3, 100, 0)],
                                    durata=0.02, fs=1000)
assert np.allclose(y_soma, y1 + y2, atol=0.01)

# TEST 10: Parametri visivi - RMS corretta
t, y = segnale_sinusoidale(10, 50, durata=1, fs=1000)
param = estrai_parametri_visivi(t, y)
rms_teorico = 10 / np.sqrt(2)  # A / sqrt(2)
assert abs(param['valore_rms'] - rms_teorico) < 0.1
```

---

## 🛠️ Step Implementazione (7-8 passaggi)

### STEP 1: Setup e Import ✅
- [ ] Creare file `soluzione.py`
- [ ] Importare: `numpy as np`, `matplotlib.pyplot as plt`
- [ ] Opzionale: `scipy.signal` per funzioni avanzate
- [ ] Verificare versioni: `numpy >= 1.19`, `matplotlib >= 3.0`

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
```

### STEP 2: Segnale Sinusoidale Base 〰️
- [ ] Implementare `segnale_sinusoidale()`
- [ ] Gestire conversione fase gradi→radianti
- [ ] Array tempi con `np.linspace(0, durata, fs*durata)`
- [ ] Formula: `y = A * np.sin(2*π*f*t + φ_rad)`
- [ ] Testare: ampiezza, fase, frequenza corrette

```python
def segnale_sinusoidale(A, f, fase_gradi=0, durata=1, fs=1000):
    phi_rad = np.radians(fase_gradi)
    t = np.linspace(0, durata, int(fs * durata), endpoint=False)
    y = A * np.sin(2 * np.pi * f * t + phi_rad)
    return t, y
```

### STEP 3: Altri Tipi di Segnali ⬜🔺
- [ ] Implementare `segnale_quadro()`, `segnale_triangolare()`, `segnale_dente_sega()`
- [ ] Usare `scipy.signal.square()` e `scipy.signal.sawtooth()`
- [ ] Verificare parametri ampiezza e frequenza

### STEP 4: Tracciamento Base 📊
- [ ] Implementare `traccia_segnale()`
- [ ] Visualizzare 2-3 periodi del segnale
- [ ] Aggiungere: griglia, etichette assi, titolo, legenda
- [ ] Testare: visualizzazione correttamente leggibile

### STEP 5: Estrazione Parametri 🔍
- [ ] Implementare `estrai_parametri_visivi()`
- [ ] Calcolare: max, min, RMS
- [ ] Stimare: periodo (zero crossing), frequenza, ampiezza
- [ ] Testare con segnali noti

### STEP 6: Segnali Sovrapposti 🎼
- [ ] Implementare `segnale_composito_somma()`
- [ ] Sommare segnali element-wise
- [ ] Implementare `sovrapponi_segnali()` per visualizzazione
- [ ] Testare: somma corretta, colori e legenda

### STEP 7: Misurazioni Precise 📐
- [ ] Implementare `misura_periodo()` con zero crossing
- [ ] Implementare `misura_frequenza()` e `misura_ampiezza()`
- [ ] Implementare `disegna_parametri_su_grafico()`
- [ ] Testare con frequenze note

### STEP 8: Test Completo e Validazione ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare precisione delle misurazioni
- [ ] Controllare grafica leggibile
- [ ] Opzionale: aggiungere animazione

---

## 💡 Trucchi Python & Matplotlib 🎯

### Trucchi NumPy 🐍
1. **Generare array tempi efficienti:**
   ```python
   t = np.linspace(0, durata, int(fs*durata), endpoint=False)
   # endpoint=False evita durata esatta (che causerebbe aliasing)
   ```

2. **Conversione gradi-radianti:**
   ```python
   phi_rad = np.radians(fase_gradi)  # Preferibile a fase*π/180
   fase_gradi = np.degrees(phi_rad)
   ```

3. **Trovare zero crossing:**
   ```python
   zero_crossing = np.where(np.diff(np.sign(y)))[0]
   # Cambi di segno indicano attraversamenti dello zero
   ```

4. **Calcolare RMS (Root Mean Square):**
   ```python
   rms = np.sqrt(np.mean(y**2))
   # Per sinusoide: RMS = A/√2
   ```

5. **Concatenare array temporali:**
   ```python
   t_combined = np.concatenate([t1, t2 + t1[-1]])
   # Assicura continuità temporale
   ```

### Trucchi Matplotlib 📊
1. **Figura e assi per test:**
   ```python
   fig, ax = plt.subplots(figsize=(12, 6))
   # Ritorna fig per asset in test
   ```

2. **Colori e stili coerenti:**
   ```python
   colori = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
   ax.plot(t, y, color=colori[0], linestyle='-', linewidth=2)
   ```

3. **Etichette assi con unità:**
   ```python
   ax.set_xlabel('Tempo (s)')
   ax.set_ylabel('Ampiezza (V)')
   ax.set_title('Segnale 50 Hz')
   ```

4. **Griglia logaritmica (per FFT):**
   ```python
   ax.set_xscale('log')
   ax.set_yscale('log')
   # Utile per spettro di frequenza
   ```

5. **Salvare figure alta qualità:**
   ```python
   plt.savefig(path, dpi=300, bbox_inches='tight')
   # dpi=300 per stampa, dpi=100 per web
   ```

### Trucchi TLC 📡
1. **Sample rate sufficientemente alto:**
   ```
   Teorema Nyquist: fs >= 2 × f_max
   Pratica: fs >= 10 × f_max (per grafica liscia)
   ```

2. **Memoria e performance:**
   ```python
   # Frequenza alta (MHz) richiede fs molto alto
   f = 100e6 Hz  # 100 MHz
   durata = 1e-6 s  # 1 microsecondo
   campioni = 100e6 * 1e-6 = 100 (gestibile)
   # MA: 1 millisecondo = 100.000 campioni!
   ```

3. **Visualizzare periodi significativi:**
   ```python
   # Visualizzare almeno 2-3 periodi per riconoscere frequenza
   T = 1 / f
   durata = 3 * T  # 3 periodi
   ```

4. **RMS vs Picco:**
   ```
   Segnale AC sinusoidale:
   - Valore picco = V_max
   - Valore RMS = V_max / √2
   - Es: 230V RMS (AC casa) = 325V picco
   ```

5. **Attenuazione e scala dB:**
   ```python
   # Decibel: dB = 20 × log10(V_out / V_in)
   # Spesso usato in TLC per attenuazione
   ```

---

## ⚠️ Errori Comuni (Grafici + Codice) 🐛

### Errori di Visualizzazione 📈

1. **Sample rate troppo basso**
   ```
   ❌ f = 1 MHz, fs = 100 kHz (Nyquist violato!)
   ✅ f = 1 MHz, fs = 20 MHz (10× la frequenza)

   Risultato: Aliasing, onda disegnata male
   ```

2. **Confondere durata e numero campioni**
   ```python
   ❌ t = np.linspace(0, 1000, 1000)  # 0-1000 secondi!
   ✅ t = np.linspace(0, 1, 1000)     # 0-1 secondo
   ✅ campioni = int(fs * durata)     # Sempre così
   ```

3. **Griglia troppo fitta o assente**
   ```python
   ❌ Senza griglia: difficile leggere valori
   ✅ ax.grid(True, alpha=0.3)  # Griglia visibile ma non invadente
   ```

4. **Range assi non adatto**
   ```python
   ❌ ax.set_ylim([-0.5, 0.5])  # Se ampiezza è 10!
   ✅ ax.set_ylim([-A*1.2, A*1.2])  # Con margine 20%
   ```

5. **Legenda incomprensibile**
   ```python
   ❌ ax.plot(t, y1, label='sin')
   ✅ ax.plot(t, y1, label='Segnale 50Hz A=10V')
   ```

### Errori di Codice 💻

1. **Confondere fase gradi vs radianti**
   ```python
   ❌ y = A * np.sin(2*π*f*t + 90)  # 90 radianti!
   ✅ y = A * np.sin(2*π*f*t + np.radians(90))
   ```

2. **Offset temporale errato**
   ```python
   ❌ t = np.linspace(0, durata, fs*durata)
       # Ultimo punto esattamente a durata!
       # Potrebbe creare discontinuità

   ✅ t = np.linspace(0, durata, fs*durata, endpoint=False)
   ```

3. **Memory leak con figure**
   ```python
   ❌ for i in range(100):
        plt.figure()  # Accumula in memoria!

   ✅ for i in range(100):
        fig, ax = plt.subplots()
        # ... usa figura
        plt.close(fig)  # Libera memoria
   ```

4. **Indici array confusi**
   ```python
   ❌ periodo = t[100]  # t[100] è il valore, non il periodo!
   ✅ periodo = t[100] - t[50]  # Differenza fra istanti
   ```

5. **Zero crossing errato**
   ```python
   ❌ zero_idx = np.where(y == 0)[0]  # Raramente esatto!
   ✅ zero_idx = np.where(np.diff(np.sign(y)))[0]
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: FFT e Spettro di Frequenza ⭐
Visualizzare lo spettro di frequenza di un segnale:
```python
def calcola_spettro(t, y):
    """
    Calcola FFT (Fast Fourier Transform).

    Returns:
        (frequenze, magnitudini)

    Grafico:
    - X: Frequenza [Hz]
    - Y: Magnitudine [dB]
    """
    from scipy.fft import fft, fftfreq
    N = len(y)
    yf = fft(y)
    xf = fftfreq(N, t[1]-t[0])[:N//2]
    return xf, 20*np.log10(np.abs(yf[:N//2]))
```

### Sfida 2: Rumore Gaussiano ⭐
Aggiungere rumore realistico a un segnale:
```python
def aggiungi_rumore_gaussiano(segnale, snr_db=20):
    """
    Aggiunge rumore Gaussiano a SNR specificato.

    SNR (dB) = 10 × log10(P_segnale / P_rumore)
    """
    potenza_segnale = np.mean(segnale**2)
    potenza_rumore = potenza_segnale / (10**(snr_db/10))
    rumore = np.random.normal(0, np.sqrt(potenza_rumore), len(segnale))
    return segnale + rumore
```

### Sfida 3: Distorsione Armonica ⭐
Aggiungere armoniche (multipli della frequenza fondamentale):
```python
def segnale_con_armoniche(f_fondamentale, armoniche_dict, durata=1, fs=1000):
    """
    Crea segnale con armoniche.

    Args:
        f_fondamentale: Frequenza base [Hz]
        armoniche_dict: {'armonica': 2, 'ampiezza': 0.3}
            Es: 2a armonica con 30% dell'ampiezza

    Segnale risultante:
    y = A₁ × sin(f) + A₂ × sin(2f) + A₃ × sin(3f) + ...
    """
```

### Sfida 4: Modulazione AM Interattiva ⭐⭐
Visualizzare modulazione AM con controlli:
```python
def simula_modulazione_am(f_portante, f_modulante, indice_modulazione=0.5):
    """
    AM: s(t) = [A + m(t)] × cos(2πf_c×t)

    Visualizzare:
    1. Segnale modulante (bassa frequenza)
    2. Portante (alta frequenza)
    3. Inviluppo modulato
    4. Segnale AM finale
    """
```

### Sfida 5: Oscilloscopio Virtuale ⭐⭐
Simulare un oscilloscopio reale:
```python
def oscilloscopio_virtuale(segnale, fs, trigger_livello=0):
    """
    Visualizzazione stile oscilloscopio:
    - Grid realistico (divisioni 1-2-5)
    - Linea centrale (0V)
    - Trigger automatico
    - Misurazioni: Vp-p, freq, periodo, duty cycle
    """
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione
- [NumPy - Array Generation](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Matplotlib - Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [SciPy - Signal Processing](https://docs.scipy.org/doc/scipy/reference/signal.html)

### TLC - Visualizzazione
- [Wikipedia: Oscilloscope](https://en.wikipedia.org/wiki/Oscilloscope)
- [Wikipedia: Waveform](https://en.wikipedia.org/wiki/Waveform)
- [Nyquist-Shannon Theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem)

### Tutorial Python
- [Real Python: Matplotlib](https://realpython.com/matplotlib-guide/)
- [SciPy: Signal Processing Tutorial](https://scipy-lectures.org/intro/scipy/auto_examples/)

---

## 🎯 Preparazione Esercizi Successivi 🔮

### ES03 - Legge di Ohm ⚡
- Calcolare tensione AC nel tempo: V(t) = V_picco × sin(2πft)
- Visualizzare corrente attraverso resistenza

### ES04 - Circuiti AC 🔌
- Graficare impedenza vs frequenza
- Visualizzare fase fra tensione e corrente

### ES05 - Mezzi Trasmissivi 📡
- Attenuazione segnale durante propagazione
- FFT per analizzare distorsione

### ES06+ - Modulazione 📶
- AM, FM, FSK già studiate
- Visualizzare spettro di segnali modulati

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi tutta la consegna
[ ] Installa: pip install numpy matplotlib scipy
[ ] Verifica versioni

IMPLEMENTAZIONE:
[ ] Step 1: Import e setup
[ ] Step 2: Segnale sinusoidale
[ ] Step 3: Segnali quadro, triangolo, sega
[ ] Step 4: Tracciamento base
[ ] Step 5: Estrazione parametri
[ ] Step 6: Segnali sovrapposti
[ ] Step 7: Misurazioni precise
[ ] Step 8: Test completo

VALIDAZIONE:
[ ] Tutti i 10 test passano
[ ] Grafici leggibili e corretti
[ ] Parametri misurati accuarti
[ ] Nessun memory leak

BONUS:
[ ] Almeno 1 sfida bonus
[ ] FFT spettro frequenza
[ ] Aggiunta rumore realistica
```

---

## 🎓 Conclusione

Hai imparato a **visualizzare segnali** - uno skill fondamentale in TLC. Ora puoi analizzare a occhio ampiezza, frequenza, fase e identificare problemi.

**Prossimo step:** ES03 - Applicare concetti a circuiti reali con la Legge di Ohm! ⚡

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS