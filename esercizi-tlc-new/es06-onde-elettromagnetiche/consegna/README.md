# ES06 - Onde Elettromagnetiche 📡

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐⭐ BASE |
| **Durata Stimata** | 3-4 ore |
| **Linguaggio** | Python 3.8+ |
| **Prerequisiti** | ES01-ES05 completati, Concetti base fisica delle onde |
| **Argomento TLC** | Propagazione: Onde Elettromagnetiche e Spettro |

---

## 🎓 Concetti Fondamentali

### Che cos'è un'Onda Elettromagnetica? 🌊

Un'**onda elettromagnetica** è la propagazione nello spazio di campi elettrici e magnetici variabili che oscillano fra loro perpendicolarmente, trasportando energia senza bisogno di mezzo materiale.

```
CONCETTO SEMPLICE (senza Maxwell):
Una onda EM è come lanciare uno sasso in acqua: le onde si propagano
verso l'esterno. Qui invece di acqua, il "mezzo" è lo spazio stesso!
```

**Caratteristiche:**
- Si propaga nel vuoto alla velocità della luce: **c = 3 × 10⁸ m/s**
- Trasporta ENERGIA (non materia)
- Non ha bisogno di mezzo materiale (diversamente dal suono)
- Usata in TUTTE le telecomunicazioni moderni

**Esempi reali:**
- Radio FM/AM 📻
- WiFi, Bluetooth 📶
- 4G/5G 📱
- Microonde 🔥
- Luce visibile 💡
- Raggi X (medicina) 🏥
- Raggi gamma (nucleare) ☢️

---

### Relazione Fondamentale: c = λ × f ⚡

La velocità di propagazione di un'onda EM dipende da 3 parametri:

```
c = λ × f

Dove:
- c = velocità della luce (3×10⁸ m/s)
- λ = lunghezza d'onda (lambda) [metri]
- f = frequenza [Hz]
```

**Significato fisico:**
```
Lunghezza d'onda (λ)        Frequenza (f)
  = distanza tra          = numero di onde
    due creste              al secondo

Se f aumenta → λ diminuisce (INVERSO)
Se λ aumenta → f diminuisce (INVERSO)
```

**Esempi numerici:**
```
1) WiFi 2.4 GHz:
   λ = c / f = (3×10⁸) / (2.4×10⁹) = 0.125 m = 12.5 cm

2) FM 100 MHz:
   λ = (3×10⁸) / (100×10⁶) = 3 m

3) Luce verde (f=600 THz=600×10¹² Hz):
   λ = (3×10⁸) / (600×10¹²) = 500 nm = 500×10⁻⁹ m
```

---

### Lo Spettro Elettromagnetico 🌈

L'**insieme di tutte le frequenze/lunghezze d'onda** si chiama **spettro EM**:

```
SPETTRO ELETTROMAGNETICO (in frequenza crescente)

Nome            Freq.           Lambda      Applicazioni
─────────────────────────────────────────────────────────
Radio           300 Hz          1000 km     AM/FM/Ricezione
(onde lunghe)   - 300 kHz       - 1 km

Radio           1 MHz           300 m       Radio AM, CB
(onde medie)    - 30 MHz        - 10 m

Radio           30 MHz          10 m        Radio FM, TV
(onde corte)    - 300 MHz       - 1 m

Microonde       300 MHz         1 m         WiFi, 4G/5G,
(UHF, SHF)      - 300 GHz       - 1 mm      Forni a microonde

Infrarosso      300 GHz         1 mm        Telecomandi,
(IR)            - 400 THz       - 750 nm    Termografia

Luce Visibile   400 THz         750 nm      Occhio umano
(Visibile)      - 800 THz       - 380 nm    Fibra ottica

UV              800 THz         380 nm      Sterilizzazione
(Ultravioletto) - 30 PHz        - 10 nm

Raggi X         30 PHz          10 nm       Radiografie
                - 30 EHz        - 0.01 nm

Raggi Gamma     > 30 EHz        < 0.01 nm   Nucleare
                                            Astronomia
```

**Bande di frequenza standard:**
```
VLF (Very Low):    3 kHz - 30 kHz      (Comunicazioni marittime)
LF (Low):          30 kHz - 300 kHz    (Radio AM)
MF (Medium):       300 kHz - 3 MHz     (Radio AM europeo)
HF (High):         3 MHz - 30 MHz      (Radio onda corta)
VHF (Very High):   30 MHz - 300 MHz    (Radio FM, TV, Aerei)
UHF (Ultra High):  300 MHz - 3 GHz     (WiFi, Cellulari, TV)
SHF (Super High):  3 GHz - 30 GHz      (Satelliti, Radar, 5G)
EHF (Extremely):   30 GHz - 300 GHz    (5G millimetriche)
```

---

### Le Antenne: Come Funzionano? 📶

Un'**antenna** è un dispositivo che **converte segnali elettrici in onde EM** (trasmissione) oppure **converte onde EM in segnali elettrici** (ricezione).

**Principio fondamentale:**
```
TRASMISSIONE (TX):
Segnale elettrico → Antenna → Onda EM che si propaga

RICEZIONE (RX):
Onda EM che arriva → Antenna → Segnale elettrico
```

**Tipi di antenne comuni:**
```
1) DIPOLO
   │  ▲
   │  │   ◄── Lunghezza ≈ λ/2
   │  │
   └─────────────────────

   Usato in: Radio FM, WiFi, Cellulari

2) PARABOLA
   ╱───────╲
   │       │  ◄── Riflette onde verso fuoco
   │   ●   │     Riceve segnale concentrato
   ╲───────╱

   Usato in: Satelliti, Radar, Dish TV

3) MONOPOLO
       ▲
       │  ◄── Lunghezza ≈ λ/4 (sul piano di massa)
       │
   ───┴───────

   Usato in: Cellulari, CB radio
```

**Relazione lunghezza d'onda - antenna:**
- Antenna efficace quando **L ≈ λ** oppure **L ≈ λ/2**
- Più alta frequenza → antenna più piccola
- Per WiFi (λ=12.5cm) → antenna di pochi cm ✓
- Per FM (λ=3m) → antenna di ~1.5m ✓

---

## 💻 Funzioni Python da Implementare

### Livello 1: Conversioni Lunghezza d'Onda ✅

```python
def calcola_lunghezza_onda(frequenza_hz, velocita=3e8):
    """
    Calcola lunghezza d'onda da frequenza.

    Args:
        frequenza_hz (float): Frequenza in Hz
        velocita (float): Velocità propagazione m/s (default: velocità luce)

    Returns:
        float: Lunghezza d'onda in metri

    Formula: λ = c / f

    Esempio:
        >>> calcola_lunghezza_onda(2.4e9)  # WiFi
        0.125  # 12.5 cm
    """
    # λ = c / f

def calcola_frequenza_da_onda(lunghezza_onda_m, velocita=3e8):
    """
    Calcola frequenza da lunghezza d'onda.

    Args:
        lunghezza_onda_m (float): Lunghezza d'onda in metri
        velocita (float): Velocità propagazione m/s

    Returns:
        float: Frequenza in Hz

    Formula: f = c / λ
    """
    # f = c / λ
```

### Livello 2: Classificazione Spettro EM 🌈

```python
def classifica_banda_frequenza(frequenza_hz):
    """
    Classifica una frequenza nella banda appropriata.

    Args:
        frequenza_hz (float): Frequenza in Hz

    Returns:
        str: Nome banda (es: 'VLF', 'LF', 'MF', 'HF', 'VHF', 'UHF', 'SHF', 'EHF')

    Bande:
    - VLF: 3 kHz - 30 kHz
    - LF:  30 kHz - 300 kHz
    - MF:  300 kHz - 3 MHz
    - HF:  3 MHz - 30 MHz
    - VHF: 30 MHz - 300 MHz
    - UHF: 300 MHz - 3 GHz
    - SHF: 3 GHz - 30 GHz
    - EHF: 30 GHz - 300 GHz

    Esempio:
        >>> classifica_banda_frequenza(2.4e9)
        'UHF'
        >>> classifica_banda_frequenza(100e6)
        'VHF'
    """

def identifica_applicazione(frequenza_hz):
    """
    Identifica l'applicazione tipica di una frequenza.

    Returns:
        str: Descrizione applicazione (es: 'Radio FM', 'WiFi', '4G LTE', etc)

    Esempio:
        >>> identifica_applicazione(89.7e6)
        'Radio FM'
        >>> identifica_applicazione(2.4e9)
        'WiFi 2.4GHz / Bluetooth'
    """
```

### Livello 3: Proprietà Antenne 📶

```python
def calcola_lunghezza_antenna_dipolo(frequenza_hz):
    """
    Calcola lunghezza ottimale dipolo (λ/2).

    Args:
        frequenza_hz (float): Frequenza in Hz

    Returns:
        float: Lunghezza antenna in metri (λ/2)

    Esempio:
        >>> calcola_lunghezza_antenna_dipolo(100e6)  # FM
        1.5  # 3m/2
    """

def calcola_lunghezza_antenna_monopolo(frequenza_hz):
    """
    Calcola lunghezza ottimale monopolo (λ/4).

    Args:
        frequenza_hz (float): Frequenza in Hz

    Returns:
        float: Lunghezza antenna in metri (λ/4)
    """

def verifica_antenna_applicazione(lunghezza_m, frequenza_hz):
    """
    Verifica se antenna è appropriata per frequenza.

    Returns:
        tuple: (bool, str)
               True se lunghezza ≈ λ/2 o λ/4 ± 10%
               Stringa con dettagli
    """
```

### Livello 4: Analisi Spettro Completa 📊

```python
def analisi_spettro_completa(frequenza_hz):
    """
    Analisi completa di una frequenza.

    Returns:
        dict: {
            'frequenza_hz': float,
            'frequenza_mhz': float,
            'frequenza_ghz': float,
            'lunghezza_onda_m': float,
            'lunghezza_onda_cm': float,
            'lunghezza_onda_nm': float,
            'banda': str,
            'applicazione': str,
            'dipolo_lunghezza_m': float,
            'monopolo_lunghezza_m': float
        }

    Esempio:
        >>> info = analisi_spettro_completa(2.4e9)
        >>> print(info['banda'])
        'UHF'
    """
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### WiFi 2.4 GHz 📶

```python
# Calcolo:
f = 2.4e9  # Hz
λ = 3e8 / 2.4e9
# λ = 0.125 m = 12.5 cm

# Antenna dipolo: 6.25 cm
# Antenna monopolo: 3.125 cm

# Applicazione:
# - Wifi 802.11b/g/n
# - Bluetooth
# - Forni a microonde
# - Cordless phones
```

### Radio FM 100 MHz 📻

```python
# Calcolo:
f = 100e6  # Hz
λ = 3e8 / 100e6
# λ = 3 m

# Antenna dipolo: 1.5 m (tipica radio auto)
# Banda: VHF

# Standard: 88-108 MHz in Italia
```

### Luce Visibile (Verde) 💚

```python
# Calcolo:
λ = 550e-9  # 550 nanometri
f = 3e8 / 550e-9
# f ≈ 545 THz

# Banda: Visibile
# Applicazione: Fibra ottica, comunicazioni ottiche
```

### Banda 4G LTE 📱

```python
# Bande comuni:
# Band 7:  2.6 GHz  (λ ≈ 11.5 cm)
# Band 3:  1.8 GHz  (λ ≈ 16.7 cm)
# Band 1:  2.1 GHz  (λ ≈ 14.3 cm)

# Studio: Frequenze medie → antenne piccole
```

---

## 🧪 Test Cases (8-10 casi)

```python
# TEST 1: Lunghezza d'onda WiFi
lambda_wifi = calcola_lunghezza_onda(2.4e9)
assert abs(lambda_wifi - 0.125) < 1e-3
print(f"✓ WiFi 2.4GHz: λ = {lambda_wifi:.3f} m = {lambda_wifi*100:.1f} cm")

# TEST 2: Lunghezza d'onda FM
lambda_fm = calcola_lunghezza_onda(100e6)
assert abs(lambda_fm - 3.0) < 1e-6
print(f"✓ FM 100MHz: λ = {lambda_fm} m")

# TEST 3: Frequenza da onda
f = calcola_frequenza_da_onda(3.0)  # Onda FM
assert abs(f - 100e6) < 1e3
print(f"✓ λ=3m → f = {f/1e6:.1f} MHz")

# TEST 4: Classificazione banda VHF
banda = classifica_banda_frequenza(100e6)
assert banda == 'VHF'
print(f"✓ 100 MHz → {banda}")

# TEST 5: Classificazione banda UHF
banda = classifica_banda_frequenza(2.4e9)
assert banda == 'UHF'
print(f"✓ 2.4 GHz → {banda}")

# TEST 6: Antenna dipolo WiFi
lunghezza = calcola_lunghezza_antenna_dipolo(2.4e9)
assert abs(lunghezza - 0.0625) < 1e-4
print(f"✓ Dipolo WiFi: {lunghezza*100:.1f} cm")

# TEST 7: Antenna monopolo FM
lunghezza = calcola_lunghezza_antenna_monopolo(100e6)
assert abs(lunghezza - 0.75) < 1e-6
print(f"✓ Monopolo FM: {lunghezza} m")

# TEST 8: Analisi spettro completa
analisi = analisi_spettro_completa(2.4e9)
assert analisi['banda'] == 'UHF'
assert analisi['lunghezza_onda_cm'] == 12.5
print(f"✓ Analisi WiFi: {analisi['applicazione']}")

# TEST 9: Velocità diversa (fibra ottica)
lambda_fibra = calcola_lunghezza_onda(1e14, velocita=2e8)  # Luce in fibra
assert abs(lambda_fibra - 2e-6) < 1e-9
print(f"✓ Luce in fibra (n=1.5): λ = {lambda_fibra*1e9:.0f} nm")

# TEST 10: Validazione input negativo
try:
    calcola_lunghezza_onda(-1e9)
    assert False, "Dovrebbe lanciare eccezione"
except ValueError:
    print("✓ Validazione frequenza negativa")
```

---

## 🛠️ Step Implementazione (7-10 passaggi)

### STEP 1: Setup e Validazione ✅
- [ ] Creare file `soluzione.py`
- [ ] Aggiungere docstring iniziale
- [ ] Implementare `calcola_lunghezza_onda()` con validazione
- [ ] Implementare `calcola_frequenza_da_onda()` con validazione

```python
def calcola_lunghezza_onda(frequenza_hz, velocita=3e8):
    if frequenza_hz <= 0:
        raise ValueError("Frequenza deve essere positiva")
    if velocita <= 0:
        raise ValueError("Velocità deve essere positiva")
    return velocita / frequenza_hz
```

### STEP 2: Spettro EM - Dizionario Bande 📊
- [ ] Creare dizionario con bande di frequenza
- [ ] Implementare `classifica_banda_frequenza()`
- [ ] Testare con 5 frequenze diverse

```python
BANDE_EM = {
    'VLF': (3e3, 30e3),
    'LF':  (30e3, 300e3),
    'MF':  (300e3, 3e6),
    'HF':  (3e6, 30e6),
    'VHF': (30e6, 300e6),
    'UHF': (300e6, 3e9),
    'SHF': (3e9, 30e9),
    'EHF': (30e9, 300e9)
}
```

### STEP 3: Identificazione Applicazioni 📡
- [ ] Creare dizionario applicazioni per frequenza
- [ ] Implementare `identifica_applicazione()`
- [ ] Aggiungere commenti su casi speciali

```python
APPLICAZIONI = {
    # Banda FM: 88-108 MHz
    (88e6, 108e6): 'Radio FM',
    # WiFi: 2.4-2.5 GHz
    (2.4e9, 2.5e9): 'WiFi 2.4GHz / Bluetooth',
    # etc...
}
```

### STEP 4: Calcoli Antenna 📶
- [ ] Implementare `calcola_lunghezza_antenna_dipolo()`
- [ ] Implementare `calcola_lunghezza_antenna_monopolo()`
- [ ] Testare con frequenze standard

```python
def calcola_lunghezza_antenna_dipolo(frequenza_hz):
    lambda_val = calcola_lunghezza_onda(frequenza_hz)
    return lambda_val / 2  # λ/2

def calcola_lunghezza_antenna_monopolo(frequenza_hz):
    lambda_val = calcola_lunghezza_onda(frequenza_hz)
    return lambda_val / 4  # λ/4
```

### STEP 5: Verifica Antenna 🔍
- [ ] Implementare `verifica_antenna_applicazione()`
- [ ] Permettere tolleranza ±10%
- [ ] Ritornare messaggio descrittivo

### STEP 6: Funzione Analisi Completa 📈
- [ ] Implementare `analisi_spettro_completa()`
- [ ] Convertire frequenza in diverse unità
- [ ] Convertire lunghezza d'onda in diverse unità
- [ ] Combinare tutte le funzioni precedenti

### STEP 7: Visualizzazione Spettro 📊 (BONUS)
- [ ] Creare funzione che stampa spettro EM ASCII art
- [ ] Marcare la posizione della frequenza input
- [ ] Mostrare applicazioni correlate

### STEP 8: Test Completo ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare gestione eccezioni
- [ ] Testare edge cases (frequenze molto alte/basse)

### STEP 9: Grafici con Matplotlib 📊
- [ ] Installare matplotlib se non presente
- [ ] Creare grafico spettro EM (scala logaritmica)
- [ ] Evidenziare bande comuni (FM, WiFi, 4G, ecc.)

### STEP 10: Documentazione Finale 📚
- [ ] Aggiungere docstring complete
- [ ] Creare file `esempi.py` con casi reali
- [ ] Documentare assunzioni

---

## 💡 Trucchi Python & TLC 🎯

### Trucchi Python 🐍

1. **Notazione scientifica per grandi numeri:**
   ```python
   2.4e9  # = 2.4 × 10⁹ = 2,400,000,000
   550e-9 # = 550 × 10⁻⁹ = 0.00000000055
   ```

2. **Dizionari per lookup frequenze:**
   ```python
   BANDE = {
       'VLF': (3e3, 30e3),
       'FM': (88e6, 108e6),
       'WiFi': (2.4e9, 2.5e9)
   }
   ```

3. **Tupla per range check:**
   ```python
   for nome, (f_min, f_max) in BANDE.items():
       if f_min <= freq <= f_max:
           return nome
   ```

4. **Fattori di conversione unità:**
   ```python
   lambda_cm = lambda_m * 100
   lambda_nm = lambda_m * 1e9
   freq_mhz = freq_hz / 1e6
   freq_ghz = freq_hz / 1e9
   ```

### Trucchi TLC 📡

1. **Relazione inversa f-λ:**
   ```
   Se f raddoppia → λ si dimezza
   Se λ triplica → f si dimezza
   ```

2. **Scala logaritmica per spettro:**
   - Frequenza varia da 10³ Hz a 10²⁵ Hz
   - Impossibile su scala lineare
   - Usare sempre scala LOG

3. **Antenna sizing:**
   - Piccole antenne: alte frequenze (GHz)
   - Grandi antenne: basse frequenze (MHz)
   - WiFi: antenna pochi cm (λ/2 ≈ 6cm)
   - FM: antenna ~1.5m (λ/2 = 1.5m)

4. **Veloctà propagazione varia:**
   ```
   Vuoto:        c = 3.00 × 10⁸ m/s
   Rame:         c = 2.00 × 10⁸ m/s
   Fibra ottica: c = 2.00 × 10⁸ m/s (n≈1.5)
   Aria:         c ≈ 3.00 × 10⁸ m/s
   ```

5. **Memoria bande radio:**
   ```
   Radio AM:  300-3000 kHz (MF)
   Radio FM:  88-108 MHz (VHF)
   WiFi:      2.4-2.5 GHz (UHF)
   4G:        700 MHz - 2.6 GHz (UHF/SHF)
   5G:        700 MHz - 28 GHz (UHF/SHF/EHF)
   ```

---

## ⚠️ Errori Comuni (Fisici + Codice) 🐛

### Errori Fisici 📉

1. **Confondere frequenza con periodo**
   ```
   ❌ "La lunghezza d'onda è 100 Hz"
   ✅ "La frequenza è 100 Hz"
   ✅ "Il periodo è 0.01 secondi"
   ```

2. **Unità sbagliate**
   ```
   ❌ λ = 3e8 / 2.4  (non compatibili: m/s ÷ numero?)
   ✅ λ = 3e8 / 2.4e9 (m/s ÷ Hz = m)
   ```

3. **Antenna troppo piccola/grande**
   ```
   ❌ Antenna 1cm per frequenza 100 MHz
      (dovrebbe essere 1.5m!)
   ✅ Antenna 6cm per WiFi 2.4 GHz
   ```

4. **Velocità propagazione sbagliata**
   ```
   ❌ λ = 3e8 / f per onde in acqua
   ✅ λ = c_acqua / f ≈ (3e8/1.33) / f
   ```

### Errori di Codice 💻

1. **Divisione per zero**
   ```python
   ❌ def calcola_lunghezza(f):
        return 3e8 / f  # Crash se f=0

   ✅ def calcola_lunghezza(f):
        if f <= 0:
            raise ValueError("...")
        return 3e8 / f
   ```

2. **Confusione notazione scientifica**
   ```python
   ❌ 2.4 GHz = 2.4e6  (SBAGLIATO! è e9)
   ✅ 2.4 GHz = 2.4e9
   ✅ 100 MHz = 100e6 = 1e8
   ```

3. **Ordine grandezza sbagliato**
   ```python
   ❌ lambda_cm = lambda_m / 100  # Dividi invece di moltiplicare
   ✅ lambda_cm = lambda_m * 100
   ```

4. **Test con precisione esatta**
   ```python
   ❌ if lambda_value == 0.125:  # Problemi float!
   ✅ if abs(lambda_value - 0.125) < 1e-6
   ```

5. **Dizionario con errori di sintassi**
   ```python
   ❌ BANDE = {'FM': (88e6, 108e6)}
       banda = BANDE['fm']  # KeyError: 'fm'

   ✅ Usare minuscole consistenti oppure
      banda = BANDE.get('FM', None)
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Spettro EM Visuale ⭐

Creare una stampa ASCII del spettro con la frequenza evidenziata:

```python
def visualizza_spettro(frequenza_hz):
    """
    Stampa spettro EM in scala logaritmica con freccia
    che indica la frequenza input.

    Output:
    ┌─────────────────────────────────────────────────┐
    │ VLF    LF    MF    HF   VHF   UHF    SHF   EHF  │
    │  ↓                              ↑                │
    │ 3k    30k   300k   3M   30M  300M   3G    30G Hz │
    │                           ⬆ TUA FREQUENZA       │
    └─────────────────────────────────────────────────┘
    """
```

### Sfida 2: Convertitore Automatico ⭐

Funzione che stampa tabella di conversione automatica:

```python
def tabella_conversione_frequenza(frequenza_hz):
    """
    Ritorna tabella:

    Frequenza: 2.4 GHz (2,400,000,000 Hz)
    Lunghezza d'onda: 12.5 cm (0.125 m, 125,000,000 nm)
    Banda: UHF
    Applicazione: WiFi 2.4GHz / Bluetooth
    Antenna dipolo: 6.25 cm
    Antenna monopolo: 3.125 cm
    """
```

### Sfida 3: Validator Banda Legale ⭐

```python
def valida_banda_legale(frequenza_hz, paese='IT'):
    """
    Controlla se la frequenza è legale nel paese.

    Paesi supportati:
    - IT (Italia)
    - US (USA)
    - EU (Europa)
    - CN (Cina)

    Returns:
        (bool, str): (è_legale, motivo)
    """
```

### Sfida 4: Calcolo Perdita Propagazione ⭐⭐

Implementare Path Loss (perdita di segnale in propagazione):

```python
def calcola_path_loss(potenza_tx_dbm, distanza_m, frequenza_hz):
    """
    Path Loss (dB) = 20*log10(f) + 20*log10(d) + 20*log10(4π/c)

    Ritorna:
        float: Potenza ricevuta in dBm

    Esempio:
        tx = 20 dBm, d=100m, f=2.4GHz
        pl ≈ 60 dB
        rx ≈ 20 - 60 = -40 dBm
    """
```

### Sfida 5: Grafico Spettro con Matplotlib ⭐⭐

```python
def disegna_spettro_em(frequenze_highlight=[]):
    """
    Crea grafico matplotlib del spettro EM
    con scala logaritmica.

    Features:
    - Asse X logaritmico (10³ a 10²⁵ Hz)
    - Colori diversi per bande
    - Etichette applicazioni
    - Linee verticali per frequenze highlight
    - Legenda
    """
    import matplotlib.pyplot as plt
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione Python
- [Python math module](https://docs.python.org/3/library/math.html)
- [Python f-strings](https://docs.python.org/3/tutorial/inputoutput.html)
- [Matplotlib visualization](https://matplotlib.org/)

### TLC - Onde Elettromagnetiche
- [Wikipedia: Electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum)
- [Wikipedia: Radio frequency](https://en.wikipedia.org/wiki/Radio_frequency)
- [ARRL Antenna Handbook](https://www.arrl.org/)

### Standard Internazionali
- ITU-R: Radio Regulations
- IEEE 802.11: WiFi Standard
- 3GPP: Cellular Standards

### Letture Consigliate
1. Sklar, "Digital Communications" (Cap 2-3)
2. Proakis & Salehi, "Fundamentals of Communication Systems"
3. Tafazolli, "LTE-Advanced for Mobile Broadband"

---

## 🎯 Preparazione Esercizi Successivi 🔮

Questo esercizio prepara:

1. **ES07 - Porte Logiche** 🔧
   - Segnali digitali (0/1) come particelle di onda EM

2. **ES08 - Circuiti Combinatori** ⚡
   - Circuiti elaborano segnali EM ricevuti

3. **ES09 - Simulatore Circuiti Web** 💻
   - Visualizzare segnali con Canvas HTML5

4. **ES10 - Sicurezza Elettrica** ⚠️
   - Effetti biologici onde EM (SAR)

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi tutta la consegna
[ ] Comprendi relazione c = λ × f
[ ] Familiarizzati con spettro EM
[ ] Conosci antenne comuni

IMPLEMENTAZIONE:
[ ] Step 1: Setup e validazione
[ ] Step 2: Classificazione banda
[ ] Step 3: Identificazione applicazioni
[ ] Step 4: Calcoli antenna
[ ] Step 5: Verifica antenna
[ ] Step 6: Analisi completa
[ ] Step 7: Visualizzazione spettro
[ ] Step 8: Test cases (10+)

VALIDAZIONE:
[ ] Tutti i test passano
[ ] Funzioni hanno docstring
[ ] Eccezioni per input invalidi
[ ] Nessun crash con edge cases

BONUS:
[ ] 1-2 sfide bonus completate
[ ] File esempi.py con casi reali
[ ] Grafico matplotlib dello spettro
```

---

## 🎓 Conclusione

Hai imparato i fondamenti delle **onde elettromagnetiche** che sono la base di TUTTE le telecomunicazioni moderni. Dall'antenna di una radio FM al WiFi del tuo laptop, tutto sfrutta questi concetti!

**Prossimo step:** ES07 - Porte Logiche (come i segnali EM vengono elaborati) 🔧

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS
