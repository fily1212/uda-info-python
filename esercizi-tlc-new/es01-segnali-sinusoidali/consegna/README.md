# ES01 - Segnali Sinusoidali 📡

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐ FACILE |
| **Durata Stimata** | 2-3 ore |
| **Linguaggio** | Python 3.8+ |
| **Prerequisiti** | Conoscenza base trigonometria, Python base |
| **Argomento TLC** | Fondamenti: Segnali e Parametri |

---

## 🎓 Concetti Fondamentali

### Che cos'è un Segnale? 📻
Un **segnale** è una variazione di una grandezza fisica nel tempo che trasporta informazione.

```
Segnale = Variazione di una grandezza nel tempo
```

**Esempi reali:**
- Onde radio FM (musica)
- Vibrazioni dell'aria (suono)
- Variazione di tensione in un filo
- Onde electromagnetic (WiFi, 4G)

### Classificazione: Continuo vs Discreto 🔄

#### Segnale Continuo (Analogico) 🌊
- Definito in **ogni istante** di tempo
- Assume **infiniti valori**
- Esempio: voce umana, corrente AC in casa

```
Rappresentazione:
        │     ╱╲     ╱╲
Ampiezza│    ╱  ╲   ╱  ╲
        │   ╱    ╲ ╱    ╲
    ────┼──────────────────── Tempo
        │
```

#### Segnale Discreto (Digitale) 📊
- Definito solo a **specifici istanti** (campioni)
- Assume valori da un **insieme finito**
- Esempio: MP3, file audio digitale

```
Rappresentazione:
        │    ●        ●
Ampiezza│   ● ●      ● ●
        │  ●   ●    ●   ●
    ────┼──────────────────── Tempo
        │
    Campioni (discreti)
```

### Il Segnale Sinusoidale 〰️

La forma d'onda più importante in telecomunicazioni è la **sinusoide**:

```
y(t) = A × sin(2πft + φ)
```

Dove:
- **A** = Ampiezza [Volt, Ampere, dBm, ...] - massima deviazione da zero
- **f** = Frequenza [Hz] - quante oscillazioni al secondo
- **t** = Tempo [secondi]
- **φ** = Fase [radianti o gradi] - traslazione temporale
- **ω = 2πf** = Pulsazione [rad/s]

#### Parametri Chiave 🔧

##### Ampiezza (A)
- Definisce l'altezza massima dell'onda
- **Unità:** Volt (V), Ampere (A), dBm, ...
- **Formula:** A = (Vmax - Vmin) / 2

```
        │        ●
     A  │       ● ●
        │      ●   ●
     ───┼─────●─────●────
        │    ●       ●
    -A  │   ●         ●
        │  ●           ●
        └──────────────────
```

##### Periodo (T)
- Tempo per **completare un'oscillazione** completa
- **Unità:** secondi (s), millisecondi (ms), microsecondi (μs), nanosecondi (ns)
- **Formula:** T = 1/f

```
Inizio ├──────┤ Fine (1 periodo)
       │ ╱╲   │ ╱╲
       │╱  ╲  │╱  ╲
       ────────────
       └──T──┘
```

##### Frequenza (f)
- Numero di oscillazioni al **secondo**
- **Unità:** Hertz (Hz)
- **Formula:** f = 1/T
- **Pulsazione:** ω = 2πf [rad/s]

**Conversioni frequenza:**
```
1 Hz      = 1 oscillazione/secondo
1 kHz     = 1.000 Hz = 10³ Hz
1 MHz     = 1.000.000 Hz = 10⁶ Hz
1 GHz     = 1.000.000.000 Hz = 10⁹ Hz
```

##### Fase (φ)
- **Traslazione temporale** dell'onda
- **Unità:** radianti (rad) o gradi (°)
- **Conversione:** 360° = 2π rad, 1° = π/180 rad
- **Significato fisico:** ritardo/anticipo rispetto a riferimento

```
Fase 0°    │     ●
           │    ● ●
      ─────┼───●   ●────

Fase 90°   │   ●
           │  ●  ●
      ─────┼─●    ●───  (anticipata)
```

---

## 📐 Formule e Relazioni Fondamentali

### Conversioni Tempo-Frequenza

```
Frequenza (Hz)  ←──→  Periodo (s)
       f = 1/T
       T = 1/f
```

### Conversioni Unità Frequenza

```
Tabella conversione:
MHz      kHz       Hz
100  =  100.000 = 100.000.000
2.4  =   2.400  = 2.400.000
0.5  =     500  =   500.000
```

### Lunghezza d'Onda (λ)

```
λ = c / f

Dove:
- λ = Lunghezza d'onda [metri]
- c = Velocità luce = 3 × 10⁸ m/s
- f = Frequenza [Hz]
```

**Esempi:**
- WiFi 2.4 GHz: λ = 3×10⁸ / 2.4×10⁹ = 0.125 m = 12.5 cm
- Radio FM 100 MHz: λ = 3×10⁸ / 100×10⁶ = 3 m

---

## 💻 Funzioni Python da Implementare

### Livello 1: Conversioni di Base ✅

```python
def calcola_frequenza(periodo):
    """
    Calcola frequenza dal periodo.

    Args:
        periodo (float): Periodo in secondi

    Returns:
        float: Frequenza in Hz

    Raises:
        ValueError: se periodo <= 0

    Esempio:
        >>> calcola_frequenza(0.01)
        100.0
    """
    # T = 0.01s → f = 1/0.01 = 100 Hz


def calcola_periodo(frequenza):
    """
    Calcola periodo dalla frequenza.

    Args:
        frequenza (float): Frequenza in Hz

    Returns:
        float: Periodo in secondi

    Raises:
        ValueError: se frequenza <= 0

    Esempio:
        >>> calcola_periodo(1000)
        0.001
    """
    # f = 1000 Hz → T = 1/1000 = 0.001s
```

### Livello 2: Conversioni Unità Frequenza 📊

```python
def hz_to_khz(frequenza_hz):
    """Converte Hz a kHz"""
    # Divide per 1000


def khz_to_hz(frequenza_khz):
    """Converte kHz a Hz"""
    # Moltiplica per 1000


def hz_to_mhz(frequenza_hz):
    """Converte Hz a MHz"""
    # Divide per 1.000.000


def mhz_to_hz(frequenza_mhz):
    """Converte MHz a Hz"""
    # Moltiplica per 1.000.000


def hz_to_ghz(frequenza_hz):
    """Converte Hz a GHz"""
    # Divide per 1.000.000.000


def ghz_to_hz(frequenza_ghz):
    """Converte GHz a Hz"""
    # Moltiplica per 1.000.000.000


def converti_frequenza(valore, da_unita, a_unita):
    """
    Conversione generica fra unità.

    Args:
        valore (float): Valore numerico
        da_unita (str): Unità sorgente ('Hz', 'kHz', 'MHz', 'GHz')
        a_unita (str): Unità destinazione

    Returns:
        float: Valore convertito

    Esempio:
        >>> converti_frequenza(2.4, 'GHz', 'MHz')
        2400.0
    """
```

### Livello 3: Lunghezza d'Onda 🌊

```python
def calcola_lunghezza_onda(frequenza_hz, velocita_propagazione=3e8):
    """
    Calcola lunghezza d'onda.

    Args:
        frequenza_hz (float): Frequenza in Hz
        velocita_propagazione (float): Velocità in m/s (default: velocità luce)

    Returns:
        float: Lunghezza d'onda in metri

    Formula:
        λ = c / f

    Esempio:
        >>> calcola_lunghezza_onda(1e6)  # 1 MHz
        300.0
    """


def calcola_frequenza_da_onda(lunghezza_onda, velocita_propagazione=3e8):
    """
    Inverso: da lunghezza d'onda a frequenza.

    Formula:
        f = c / λ
    """
```

### Livello 4: Segnale Sinusoidale 〰️

```python
import math

def valutare_segnale_sinusoidale(ampiezza, frequenza, fase_gradi, tempo):
    """
    Valuta segnale sinusoidale in un istante.

    Args:
        ampiezza (float): Ampiezza A [V, A, ...]
        frequenza (float): Frequenza f [Hz]
        fase_gradi (float): Fase φ [gradi]
        tempo (float): Istante t [secondi]

    Returns:
        float: Valore y(t) = A × sin(2πft + φ)

    Esempio:
        >>> valutare_segnale_sinusoidale(10, 50, 0, 0.01)
        # Calcola 10 * sin(2π*50*0.01 + 0)
    """
    # Convertire fase da gradi a radianti
    # Calcolare 2πf
    # Applicare formula


def parametri_sinusoide(ampiezza, frequenza):
    """
    Calcola tutti i parametri sinusoidale.

    Args:
        ampiezza (float): Ampiezza
        frequenza (float): Frequenza in Hz

    Returns:
        dict: {'ampiezza': ..., 'frequenza': ..., 'periodo': ...,
               'pulsazione': ..., 'lunghezza_onda': ...}

    Esempio:
        >>> param = parametri_sinusoide(5, 100)
        >>> param['periodo']
        0.01
    """
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### Radio FM 📻
```
Banda:       88 - 108 MHz
Lunghezza d'onda: 3.4 - 2.8 metri
Applicazione: Trasmissione musica
Esempio: RaiRadio 1 su 89.7 MHz
```

### WiFi 📶
```
Banda 2.4 GHz:   2.400 - 2.500 GHz  (più penetrazione)
Banda 5 GHz:     5.150 - 5.850 GHz  (più veloce)
Lunghezza d'onda 2.4 GHz: 12.5 cm
Lunghezza d'onda 5 GHz:   6 cm
```

### Voce Umana 🎤
```
Banda:       300 - 3.400 Hz
Periodo:     1/300 ≈ 3.3 ms (bassa) a 1/3400 ≈ 0.3 ms (alta)
Lunghezza d'onda: ~100 m (grave) a ~10 m (acuto)
Nota: In aria con v ≈ 340 m/s
```

### Reti di Telecomunicazione 🌐
```
WWAN (Wide Area):
- 4G/LTE:    700 MHz - 2.6 GHz
- 5G NR:     700 MHz - 28 GHz
- Radio UHF: 400 - 500 MHz

WLAN (Local Area):
- WiFi:      2.4 / 5 GHz
- Bluetooth: 2.4 GHz

Comunicazioni Spaziali:
- GPS:       1.2 - 1.6 GHz
- Satellite: 10 - 20 GHz
```

---

## 🧪 Test Cases (8-10 casi)

```python
# TEST 1: Conversione base frequenza-periodo
assert abs(calcola_frequenza(0.02) - 50) < 1e-9
assert abs(calcola_periodo(50) - 0.02) < 1e-9

# TEST 2: Relazione inversa
f = 1000
assert abs(calcola_periodo(f) * f - 1.0) < 1e-9

# TEST 3: Conversioni Hz-kHz
assert abs(hz_to_khz(1000) - 1.0) < 1e-9
assert abs(khz_to_hz(1.5) - 1500) < 1e-9

# TEST 4: Conversioni MHz-GHz
assert abs(hz_to_mhz(1e6) - 1.0) < 1e-9
assert abs(ghz_to_hz(2.4) - 2.4e9) < 1e-9

# TEST 5: Conversione generica
assert abs(converti_frequenza(100, 'MHz', 'kHz') - 100000) < 1e-9
assert abs(converti_frequenza(2.4, 'GHz', 'MHz') - 2400) < 1e-9

# TEST 6: Lunghezza d'onda
lambda_1mhz = calcola_lunghezza_onda(1e6)  # Deve essere 300m
assert abs(lambda_1mhz - 300) < 1e-6

# TEST 7: WiFi
lambda_2_4ghz = calcola_lunghezza_onda(2.4e9)  # Deve essere ~0.125m
assert abs(lambda_2_4ghz - 0.125) < 1e-3

# TEST 8: Segnale sinusoidale
y = valutare_segnale_sinusoidale(10, 50, 0, 0)  # t=0, fase=0
assert abs(y - 0) < 1e-9  # sin(0) = 0

# TEST 9: Fase 90°
y = valutare_segnale_sinusoidale(10, 50, 90, 0)  # φ=90°
assert abs(y - 10) < 1e-9  # sin(π/2) = 1

# TEST 10: Validazione
try:
    calcola_frequenza(-0.5)  # Errore: periodo negativo
    assert False, "Dovrebbe lanciare eccezione"
except ValueError:
    pass
```

---

## 🛠️ Step Implementazione (7-8 passaggi)

### STEP 1: Setup e Validazione ✅
- [ ] Creare file `soluzione.py`
- [ ] Aggiungere docstring iniziale
- [ ] Implementare `calcola_frequenza()` e `calcola_periodo()`
- [ ] **Validazione:** Lanciare `ValueError` se input <= 0

```python
def calcola_frequenza(periodo):
    if periodo <= 0:
        raise ValueError("Periodo deve essere positivo")
    return 1 / periodo
```

### STEP 2: Conversioni Hz-kHz-MHz-GHz 📊
- [ ] Implementare 6 funzioni di conversione bidirezionali
- [ ] Testare con valori tipici TLC:
  - 89.7 MHz (Radio FM)
  - 2.4 GHz (WiFi)
  - 1000 Hz (audio)

### STEP 3: Funzione Conversione Generica 🔄
- [ ] Creare dizionario con fattori di conversione
- [ ] Validare unità (solo 'Hz', 'kHz', 'MHz', 'GHz')
- [ ] Testare tutte le combinazioni

```python
FATTORI = {
    'Hz': 1,
    'kHz': 1e3,
    'MHz': 1e6,
    'GHz': 1e9
}
```

### STEP 4: Lunghezza d'Onda 🌊
- [ ] Implementare `calcola_lunghezza_onda()`
- [ ] Testare con esempi:
  - 1 MHz → 300 m
  - 100 MHz → 3 m
  - 2.4 GHz → 0.125 m
- [ ] Parametro opzionale velocità propagazione

### STEP 5: Segnale Sinusoidale - Base 〰️
- [ ] Implementare `valutare_segnale_sinusoidale()`
- [ ] Conversione gradi→radianti
- [ ] Formula: `A * sin(2*π*f*t + φ)`
- [ ] Testare ai punti notevoli:
  - t=0, φ=0° → y=0
  - t=0, φ=90° → y=A
  - t=T/4, φ=0° → y=A

### STEP 6: Parametri Sinusoide 📋
- [ ] Implementare `parametri_sinusoide()`
- [ ] Calcolare: periodo, pulsazione, lunghezza d'onda
- [ ] Ritornare dizionario ben strutturato

### STEP 7: Test Completo ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare validazione eccezioni
- [ ] Testare con dati reali TLC

### STEP 8: Documentazione e Esempi 📚
- [ ] Aggiungere docstring complete
- [ ] Creare file `esempi.py` con casi reali
- [ ] Documentare assunzioni e limiti

---

## 💡 Trucchi Python & TLC 🎯

### Trucchi Python 🐍
1. **Modulo math:** `import math` per `sin()`, `pi`, `degrees()`, `radians()`
   ```python
   import math
   math.sin(math.pi/2)  # = 1.0
   math.radians(90)     # = π/2
   ```

2. **Validazione input:** Lanciare eccezioni presto
   ```python
   if not isinstance(frequenza, (int, float)):
       raise TypeError("Frequenza deve essere numero")
   ```

3. **Precisione float:** Usare `1e-9` per confronti
   ```python
   assert abs(risultato - atteso) < 1e-9
   ```

4. **Dizionari per mappature:** Fattori di conversione
   ```python
   FATTORI = {'Hz': 1, 'kHz': 1e3, 'MHz': 1e6, 'GHz': 1e9}
   valore_hz = valore * FATTORI[unita]
   ```

5. **F-string per output leggibile:**
   ```python
   print(f"Frequenza: {f:.2f} Hz = {f/1e6:.1f} MHz")
   ```

### Trucchi TLC 📡
1. **Potenze di 10:** Le conversioni sono sempre moltiplicazioni/divisioni per 10³
   ```
   Hz → kHz: ÷ 10³
   MHz → GHz: ÷ 10³
   ```

2. **Velocità luce:** Sempre c = 3×10⁸ m/s (in vuoto)
   - In materiali: c' = c/n dove n = indice rifrazione
   - Fibra ottica: n ≈ 1.48, quindi c' ≈ 2×10⁸ m/s

3. **Memoria conversioni frequenza:**
   ```
   Radio FM: ~100 MHz → lunghezza d'onda ~3 metri
   WiFi: ~2.4 GHz → lunghezza d'onda ~12 cm
   ```

4. **Fase:** Spesso rappresentata come frazione di periodo
   ```
   90° = T/4 (un quarto di periodo)
   180° = T/2 (mezzo periodo)
   270° = 3T/4
   ```

5. **Fattore di forma segnale:**
   ```
   Sinusoidale: valore_rms = Ampiezza / √2
   Rettangolare: valore_rms = Ampiezza
   ```

---

## ⚠️ Errori Comuni (Fisici + Codice) 🐛

### Errori Fisici 📉

1. **Confondere Frequenza e Periodo**
   ```
   ❌ SBAGLIATO: "Periodo di 100 Hz"
   ✅ GIUSTO: "Frequenza di 100 Hz" oppure "Periodo di 0.01 s"
   ```

2. **Unità mancanti**
   ```
   ❌ SBAGLIATO: "La frequenza è 2.4"
   ✅ GIUSTO: "La frequenza è 2.4 GHz"
   ```

3. **Confondere fase in gradi vs radianti**
   ```
   ❌ sin(90)  = 0.8939 (90 radianti!)
   ✅ sin(π/2) = 1.0 (90 gradi convertiti)
   ✅ sin(math.radians(90)) = 1.0
   ```

4. **Lunghezza d'onda in materiali**
   ```
   ❌ λ = c / f  (solo in vuoto!)
   ✅ λ = c' / f = (c/n) / f  (in materiale)
   ```

5. **Velocità propagazione variabile**
   ```
   Vuoto:        c = 3×10⁸ m/s
   Rame:         c = 2×10⁸ m/s
   Fibra ottica: c = 2×10⁸ m/s (n≈1.5)
   Aria:         c = 3×10⁸ m/s
   ```

### Errori di Codice 💻

1. **Divisione per zero**
   ```python
   ❌ def calcola_frequenza(periodo):
        return 1 / periodo  # Crash se periodo=0

   ✅ def calcola_frequenza(periodo):
        if periodo <= 0:
            raise ValueError("Periodo deve essere > 0")
        return 1 / periodo
   ```

2. **Gradi vs Radianti**
   ```python
   ❌ y = 10 * math.sin(90)  # Sbagliato! 90 radianti
   ✅ y = 10 * math.sin(math.radians(90))  # Giusto!
   ```

3. **Overflow numerico**
   ```python
   # Attenzione a frequenze molto grandi
   ❌ t = 1 / (2 * 3.14159 * 1e15)  # Numero piccolissimo!
   ✅ Usare notazione scientifica: 1e-15
   ```

4. **Confronto float esatto**
   ```python
   ❌ if calcola_periodo(100) == 0.01:  # Potrebbe fallire!
   ✅ if abs(calcola_periodo(100) - 0.01) < 1e-9:
   ```

5. **Unità sbagliate nel dizionario**
   ```python
   ❌ FATTORI = {'Hz': 1, 'Khz': 1e3}  # Minuscola in Khz!
   ✅ FATTORI = {'Hz': 1, 'kHz': 1e3}  # Maiuscola K
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Simulatore di Onda Radio ⭐
Creare funzione che simula un'onda radio FM:
```python
def simula_radio_fm(frequenza_mhz, durata_secondi, campioni_al_secondo=44100):
    """
    Genera campioni di segnale FM.

    Args:
        frequenza_mhz: Frequenza in MHz (es: 89.7)
        durata_secondi: Durata della simulazione
        campioni_al_secondo: Sample rate

    Returns:
        list: Campioni [y(t0), y(t1), ..., y(tN)]
    """
    # Usa valutare_segnale_sinusoidale per ogni campione
```

**Test:**
```python
campioni = simula_radio_fm(89.7, 0.01)  # 10 ms
assert len(campioni) == 441  # 44100 * 0.01
```

### Sfida 2: Conversione Batch ⭐
Creare tabella di conversione interattiva:
```python
def tabella_conversione_frequenza(valori_hz, unita_output='MHz'):
    """
    Converte lista di frequenze.

    Ritorna tabella formattata:
    Hz          kHz      MHz     GHz
    1000        1.0      0.001   0.000001
    1e6         1000     1.0     0.001
    """
```

### Sfida 3: Validatore Banda Radiofonica ⭐
```python
def valida_banda_rf(frequenza_hz, tipo_banda):
    """
    Valida se frequenza rientra in banda legale.

    Bande:
    - 'FM': 88-108 MHz
    - 'WiFi2.4': 2.4-2.5 GHz
    - 'WiFi5': 5.15-5.85 GHz
    - '4G': 700 MHz - 2.6 GHz
    - 'GPS': 1.2-1.6 GHz

    Returns: bool
    """
```

### Sfida 4: Segnali Composti (Fourier) ⭐⭐
```python
def segnale_composito(frequenze, ampiezze, tempi):
    """
    Somma più segnali sinusoidali.

    y_totale(t) = Σ Ai × sin(2πfi×t)

    Args:
        frequenze: [f1, f2, f3, ...]
        ampiezze: [A1, A2, A3, ...]
        tempi: [t1, t2, ..., tN]

    Returns:
        list: Valori totali per ogni tempo
    """
    # Sommazione di sinusoidi
```

### Sfida 5: Decoherence Segnale (Attenuazione) ⭐⭐
```python
def attenuazione_propagazione(potenza_trasmessa_dbm, distanza_m,
                              frequenza_hz, ambiente='libero'):
    """
    Calcola perdita di potenza in propagazione.

    Path Loss (dB) = 20*log10(f) + 20*log10(d) + 20*log10(4π/c)

    Ambienti:
    - 'libero': Spazio libero
    - 'urbano': Con edifici
    - 'interiore': Dentro edifici

    Returns:
        float: Potenza ricevuta in dBm
    """
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione Python
- [math module](https://docs.python.org/3/library/math.html) - Funzioni trigonometriche
- [numpy tutorial](https://numpy.org/) - Arrays per segnali (esercizio successivo)

### TLC - Fondamenti
- [Wikipedia: Sine Wave](https://en.wikipedia.org/wiki/Sine_wave)
- [Wikipedia: Radio Frequency](https://en.wikipedia.org/wiki/Radio_frequency)
- [Spectrum Allocation](https://en.wikipedia.org/wiki/Radio_spectrum)

### Standard Internazionali
- ITU-R: Radiocommunication regulations
- IEEE 802.11: Standard WiFi
- 3GPP: Standard 4G/5G

### Letture Consigliate
1. Sklar, "Digital Communications" (Cap 1-2)
2. Proakis, "Digital Communications" (Cap 2)
3. Tafazolli, "LTE-Advanced for Mobile Broadband"

---

## 🎯 Preparazione Esercizi Successivi 🔮

Questo esercizio prepara:

1. **ES02 - Grafici Segnali** 📊
   - Visualizzerai sinusoidi con matplotlib
   - Userai `valutare_segnale_sinusoidale()` per generare dati

2. **ES03 - Legge di Ohm** ⚡
   - Tensione nel circuito è spesso sinusoidale
   - Formula: V(t) = V_max × sin(2πft)

3. **ES04 - Circuiti AC** 🔌
   - Impedenza dipende da frequenza: Z = R + jωL - j/(ωC)
   - Pulsazione ω = 2πf è fondamentale

4. **ES05 - Mezzi Trasmissivi** 📡
   - Attenuazione dipende dalla frequenza
   - Lunghezza d'onda determina antenna design

5. **ES06+ - Modulazione e Trasmissione** 📶
   - Segnali compositi: portante + modulazione
   - FM: frequenza varia, AM: ampiezza varia

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi tutta la consegna
[ ] Comprendi le formule matematiche
[ ] Identifica gli 8 step
[ ] Crea file soluzione.py

IMPLEMENTAZIONE:
[ ] Step 1: Setup e validazione
[ ] Step 2: Conversioni base Hz-kHz-MHz-GHz
[ ] Step 3: Conversione generica
[ ] Step 4: Lunghezza d'onda
[ ] Step 5: Segnale sinusoidale
[ ] Step 6: Parametri sinusoide
[ ] Step 7: Test (almeno 10 cases)
[ ] Step 8: Documentazione

VALIDAZIONE:
[ ] Tutti i test passano
[ ] Funzioni hanno docstring
[ ] Eccezioni per input invalidi
[ ] Nessun crash con edge cases

BONUS:
[ ] Almeno 1 sfida bonus completata
[ ] File esempi.py con casi reali
[ ] Commenti su trucchi TLC usati
```

---

## 🎓 Conclusione

Hai imparato i fondamenti dei **segnali sinusoidali** che sono l'alfabeto delle telecomunicazioni. Ogni trasmissione (radio, WiFi, 4G, fibra) usa questi concetti.

**Prossimo step:** ES02 - Visualizzare questi segnali con grafici! 📊

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS