# ES03 - Legge di Ohm e Circuiti Elementari ⚡

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐ FACILE |
| **Durata Stimata** | 2-3 ore |
| **Linguaggio** | Python 3.8+ |
| **Prerequisiti** | ES01 Segnali Sinusoidali, fisica di base |
| **Argomento TLC** | Fondamenti circuiti: tensione, corrente, resistenza, potenza |

---

## 🎓 Concetti Fondamentali

### Le Tre Grandezze Elettriche Fondamentali ⚙️

#### 1. Tensione Elettrica (V) 🔋
**Definizione:** Differenza di potenziale fra due punti. "Pressione" che spinge gli elettroni.

```
Simbolo: V
Unità: Volt (V)
Simbolo circuito:
    ┌─────┐
    │  ⊕  │  (+ polo positivo, - polo negativo)
    └─────┘
```

**Caratteristiche:**
- Genera il flusso di corrente
- Si misura fra due punti (con multimetro in parallelo)
- Può essere positiva o negativa
- Unità derivate: mV (millivolt), μV (microvolt), kV (chilovolt)

**Esempi:**
- Batteria AA: 1.5V
- AC domestica (Europa): 230V efficace (RMS)
- Batteria auto: 12V
- Tensione segnale audio: mV (millivolt)

#### 2. Corrente Elettrica (I) 🔌
**Definizione:** Flusso di cariche (elettroni) in un circuito. Quantità di carica al secondo.

```
Simbolo: I
Unità: Ampere (A)
Formula: I = Q / t  (carica / tempo)
         1 A = 1 Coulomb / 1 secondo
```

**Caratteristiche:**
- Flusso di cariche (positivo per convenzione, da + a -)
- Si misura in serie nel circuito (con multimetro in serie)
- Può essere positiva o negativa
- Unità derivate: mA (milliampere), μA (microampere), nA (nanoampere)

**Esempi:**
- Corrente corpo umano (letale): >0.1A
- Corrente corrente fisica AC domestica (10A): Lampada
- Corrente circuiti digitali: mA (milliampere)
- Corrente sensori: μA (microampere)

#### 3. Resistenza Elettrica (R) 🚧
**Definizione:** Opposizione al flusso di corrente. Proprietà del materiale che ostacola il movimento di elettroni.

```
Simbolo: R
Unità: Ohm (Ω)
Simbolo circuito:
    ─────▭▭▭─────
```

**Caratteristiche:**
- Dipende da: materiale, lunghezza, temperatura
- Sempre positiva (in circuiti passivi)
- Unità derivate: kΩ (kilohm), MΩ (megaohm), mΩ (milliohm)
- Formula: R = ρ × L / A
  - ρ = resistività materiale [Ω·m]
  - L = lunghezza [m]
  - A = sezione trasversale [m²]

**Materiali:**
```
Conduttore (bassa R): Rame, alluminio (R << 1 Ω/metro)
Semiconduttore (media R): Silicio, germanio
Isolante (alta R): Plastica, vetro (R > 10¹² Ω)
Resistore (controllata): Carbonio, film metallico
```

**Esempi:**
- Filo di rame 1m, 1mm²: ~0.017 Ω
- Resistore standard: 1 Ω - 10 MΩ
- Corpo umano secco: 10-100 kΩ
- Corpo umano bagnato: 1 kΩ (pericoloso!)

---

## 📐 Legge di Ohm e Formule Derivate

### La Legge di Ohm 🎯

La **Legge di Ohm** è la relazione fondamentale fra tensione, corrente e resistenza:

```
V = R × I

Dove:
- V = Tensione [Volt]
- R = Resistenza [Ohm]
- I = Corrente [Ampere]
```

**Interpretazione fisica:**
```
Tensione = Resistenza × Corrente
Pressione = Ostacolo × Flusso
```

**Rappresentazione grafica:**
```
I (A)
│
│     V=100V
│    ╱
│   ╱  V=50V
│  ╱  ╱
│ ╱  ╱ (meno resistenza = più corrente)
├─────────────────── R (Ω)
0
```

### Derivate della Legge di Ohm 🔀

```
V = R × I      (Tensione)
I = V / R      (Corrente)
R = V / I      (Resistenza)
```

### Potenza Elettrica 💡

La **potenza** è l'energia trasferita per unità di tempo.

```
P = V × I    (Potenza = Tensione × Corrente)

Unità: Watt (W)
1 W = 1 Volt × 1 Ampere = 1 Joule/secondo
```

**Forme alternative:**
```
P = V × I           (Tensione × Corrente)
P = I² × R          (Corrente² × Resistenza)
P = V² / R          (Tensione² / Resistenza)
```

**Significato:** La potenza dissipata nel resistore dipende sia dalla tensione che dalla corrente.

**Esempi:**
```
Lampadina 60W @ 230V:  I = P/V = 60/230 ≈ 0.26 A
Resistore 100Ω, 10V:   P = V²/R = 100/100 = 1 W
Circuito 5V, 2A:       P = V×I = 5×2 = 10 W
```

### Conversioni Unità Tensione/Corrente

```
Tensione:           Corrente:
1 V                 1 A
1 mV = 10⁻³ V      1 mA = 10⁻³ A
1 μV = 10⁻⁶ V      1 μA = 10⁻⁶ A
1 nV = 10⁻⁹ V      1 nA = 10⁻⁹ A
1 kV = 10³ V       1 kA = 10³ A
```

---

## 💻 Funzioni Python da Implementare

### Livello 1: Conversioni di Base Unità ✅

```python
def converti_tensione(valore, da_unita, a_unita):
    """
    Converte tensione fra unità diverse.

    Args:
        valore (float): Valore numerico
        da_unita (str): Unità sorgente ('V', 'mV', 'μV', 'nV', 'kV')
        a_unita (str): Unità destinazione

    Returns:
        float: Valore convertito

    Esempio:
        >>> converti_tensione(5000, 'mV', 'V')
        5.0
    """
    # Usare dizionario con fattori


def converti_corrente(valore, da_unita, a_unita):
    """
    Converte corrente fra unità diverse.

    Args:
        valore (float): Valore numerico
        da_unita (str): Unità sorgente ('A', 'mA', 'μA', 'nA', 'kA')
        a_unita (str): Unità destinazione

    Returns:
        float: Valore convertito

    Esempio:
        >>> converti_corrente(500, 'mA', 'A')
        0.5
    """
    # Usare dizionario con fattori


def converti_resistenza(valore, da_unita, a_unita):
    """
    Converte resistenza fra unità diverse.

    Args:
        valore (float): Valore numerico
        da_unita (str): Unità sorgente ('Ω', 'kΩ', 'MΩ', 'mΩ')
        a_unita (str): Unità destinazione

    Returns:
        float: Valore convertito

    Esempio:
        >>> converti_resistenza(10, 'kΩ', 'Ω')
        10000.0
    """
    # Usare dizionario con fattori
```

### Livello 2: Legge di Ohm 🎯

```python
def calcola_tensione(resistenza, corrente):
    """
    Calcola tensione dalla Legge di Ohm.

    Legge di Ohm: V = R × I

    Args:
        resistenza (float): Resistenza [Ohm]
        corrente (float): Corrente [Ampere]

    Returns:
        float: Tensione [Volt]

    Raises:
        ValueError: se resistenza o corrente < 0

    Esempio:
        >>> calcola_tensione(100, 0.5)
        50.0
    """


def calcola_corrente(tensione, resistenza):
    """
    Calcola corrente dalla Legge di Ohm.

    Legge di Ohm: I = V / R

    Args:
        tensione (float): Tensione [Volt]
        resistenza (float): Resistenza [Ohm]

    Returns:
        float: Corrente [Ampere]

    Raises:
        ValueError: se resistenza == 0
        ValueError: se resistenza < 0 o tensione < 0
    """


def calcola_resistenza(tensione, corrente):
    """
    Calcola resistenza dalla Legge di Ohm.

    Legge di Ohm: R = V / I

    Args:
        tensione (float): Tensione [Volt]
        corrente (float): Corrente [Ampere]

    Returns:
        float: Resistenza [Ohm]

    Raises:
        ValueError: se corrente == 0
        ValueError: se corrente < 0 o tensione < 0
    """
```

### Livello 3: Potenza Elettrica 💡

```python
def calcola_potenza_vi(tensione, corrente):
    """
    Calcola potenza da tensione e corrente.

    Formula: P = V × I [Watt]

    Args:
        tensione (float): Tensione [Volt]
        corrente (float): Corrente [Ampere]

    Returns:
        float: Potenza [Watt]

    Esempio:
        >>> calcola_potenza_vi(230, 0.26)
        59.8
    """


def calcola_potenza_ri(resistenza, corrente):
    """
    Calcola potenza da resistenza e corrente.

    Formula: P = I² × R [Watt]

    Args:
        resistenza (float): Resistenza [Ohm]
        corrente (float): Corrente [Ampere]

    Returns:
        float: Potenza [Watt]
    """


def calcola_potenza_vr(tensione, resistenza):
    """
    Calcola potenza da tensione e resistenza.

    Formula: P = V² / R [Watt]

    Args:
        tensione (float): Tensione [Volt]
        resistenza (float): Resistenza [Ohm]

    Returns:
        float: Potenza [Watt]

    Esempio:
        >>> calcola_potenza_vr(10, 100)
        1.0
    """


def parametri_circuito(tensione, resistenza, corrente=None):
    """
    Calcola tutti i parametri di un circuito elementare.

    Args:
        tensione (float): Tensione [V] (se None, calcolata)
        resistenza (float): Resistenza [Ω]
        corrente (float): Corrente [A] (se None, calcolata)

    Returns:
        dict: {
            'tensione': V,
            'corrente': I,
            'resistenza': R,
            'potenza': P,
            'energia_1h': P×3600  # Joule in 1 ora
        }

    Logica:
        - Almeno 2 parametri devono essere dati
        - Calcolare il terzo
        - Validare coerenza

    Esempio:
        >>> param = parametri_circuito(tensione=10, resistenza=100)
        >>> param['corrente']
        0.1
    """
```

### Livello 4: Validazione e Sicurezza 🛡️

```python
def valida_circuito(tensione, corrente, resistenza):
    """
    Valida coerenza legge di Ohm.

    Args:
        tensione (float): Tensione [V]
        corrente (float): Corrente [A]
        resistenza (float): Resistenza [Ω]

    Returns:
        bool: True se V ≈ R × I (entro tolleranza)

    Raises:
        ValueError: se valori non positivi
        Warning: se valori fisicamente pericolosi
    """
    # Verificare: V ≈ R × I
    # Segnalare: I > 0.05 A (pericoloso per corpo umano)


def classifica_condizione(corrente_ma):
    """
    Classifica effetti di corrente attraverso corpo umano.

    Args:
        corrente_ma (float): Corrente in mA

    Returns:
        str: Descrizione dell'effetto

    Classificazione:
    1-5 mA:        Lieve sensazione, nessun pericolo
    5-10 mA:       Dolore, paralisi muscolare temporanea
    10-50 mA:      Fibrillazione ventricolare (PERICOLOSO)
    > 50 mA:       Ustioni gravi, possibile morte

    Esempio:
        >>> classifica_condizione(20)
        'PERICOLOSO: Rischio fibrillazione ventricolare'
    """
```

### Livello 5: Circuiti Elementari 🔌

```python
def resistor_colori_a_ohm(banda1, banda2, banda3):
    """
    Decodifica colori resistore.

    Codifica colori resistori:
    0=Nero, 1=Marrone, 2=Rosso, 3=Arancione, 4=Giallo,
    5=Verde, 6=Blu, 7=Violetto, 8=Grigio, 9=Bianco

    Banda 1-2: Prime due cifre
    Banda 3: Moltiplicatore (10^n)

    Args:
        banda1 (int): 0-9 (prima cifra)
        banda2 (int): 0-9 (seconda cifra)
        banda3 (int): 0-9 (moltiplicatore 10^n)

    Returns:
        float: Resistenza in Ohm

    Esempio:
        >>> resistor_colori_a_ohm(1, 0, 2)  # Marrone, Nero, Rosso
        1000  # 10 × 100
    """
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### Esempio 1: Lampadina Incandescente 💡
```
Dati:
- Potenza nominale: 60 W
- Tensione nominale: 230 V (AC)
- Formula: P = V × I

Calcolo corrente:
I = P / V = 60 / 230 ≈ 0.26 A

Calcolo resistenza (a regime):
R = V / I = 230 / 0.26 ≈ 885 Ω

Dato interessante:
- A freddo: R ~ 50 Ω
- A caldo: R ~ 900 Ω (forte variazione con T°)
```

### Esempio 2: Circuito Amplificatore 📻
```
Stadio amplificatore con alimentazione 12V:
- Tensione alimentazione: VCC = 12 V
- Corrente assorbita: I = 0.5 A
- Potenza dissipata: P = 12 × 0.5 = 6 W

Dissipazione calore:
- Senza dissipatore: 6 W / 10 cm² = 0.6 W/cm²
- Temperatura: Può raggiungere 100°C!
- Con dissipatore: Temperatura ridotta (importante per affidabilità)
```

### Esempio 3: Divisore di Tensione (Attenuatore) ⚖️
```
Configurazione:
          R1
    ┌─────▭▭▭─────┐
    │              ├──── Vout
    │   R2        ├──
   ───▭▭▭─────────┘
   ─
   ─ GND

Formula divisore:
Vout = Vin × R2 / (R1 + R2)

Esempio pratico:
- Vin = 10 V
- R1 = 90 Ω, R2 = 10 Ω
- Vout = 10 × 10 / 100 = 1 V (attenuazione 10×)

Applicazione TLC:
- Attenuatori RF per ridurre livello segnale
- Adattamento impedenza (matching)
```

### Esempio 4: LED con Resistore di Limitazione 🔴
```
Caratteristiche LED rosso:
- Tensione forward: VF = 2.0 V
- Corrente massima: IF = 20 mA
- Potenza: P = VF × IF = 2.0 × 0.02 = 0.04 W (40 mW)

Circuito da 5V:
      5V
       │
      ▭▭▭ R limitazione
       │
       │
      ╱ LED
      \ (2V)
       │
      GND

Calcolo resistore:
V_resistore = V_totale - V_LED = 5 - 2 = 3 V
I_desiderata = 10 mA (50% del max per affidabilità)
R = V_resistore / I = 3 / 0.01 = 300 Ω
Potenza resistore: P = 3 × 0.01 = 0.03 W (30 mW)

Scelta standard: R = 330 Ω (E12 series)
```

### Esempio 5: Trasduttore Segnale (Sensore) 📊
```
Sensore di temperatura (NTC):
- Resistenza @ 25°C: R = 10 kΩ
- Variazione: dR/dT ≈ -350 Ω/°C

Circuito di misura:
      5V
       │
      ▭▭▭ R_pull-up = 10kΩ
       │
       ├──── Vout → ADC (analogico-digitale)
       │
      ▭▭▭ R_ntc (variabile)
       │
      GND

Analisi:
- A 25°C: R_ntc = 10 kΩ → Vout = 5 × 10/(10+10) = 2.5 V
- A 35°C: R_ntc ≈ 6.5 kΩ → Vout = 5 × 6.5/(10+6.5) ≈ 2 V
- Variazione: 0.5 V per 10°C (50 mV/°C)
```

---

## 🧪 Test Cases (8-10 casi)

```python
# TEST 1: Legge di Ohm - Calcolo tensione
assert abs(calcola_tensione(100, 0.5) - 50) < 1e-9

# TEST 2: Legge di Ohm - Calcolo corrente
assert abs(calcola_corrente(50, 100) - 0.5) < 1e-9

# TEST 3: Legge di Ohm - Calcolo resistenza
assert abs(calcola_resistenza(50, 0.5) - 100) < 1e-9

# TEST 4: Relazione inversa (coerenza)
V = 230
R = 100
I = calcola_corrente(V, R)
V_calcolato = calcola_tensione(R, I)
assert abs(V - V_calcolato) < 1e-9

# TEST 5: Potenza - Metodo V×I
assert abs(calcola_potenza_vi(10, 2) - 20) < 1e-9

# TEST 6: Potenza - Metodo I²×R
assert abs(calcola_potenza_ri(100, 0.1) - 1) < 1e-9

# TEST 7: Potenza - Metodo V²/R
assert abs(calcola_potenza_vr(10, 100) - 1) < 1e-9

# TEST 8: Equivalenza tre metodi potenza
# Dato V=10V, R=100Ω, calcolare I e poi P tre volte
I = calcola_corrente(10, 100)
p1 = calcola_potenza_vi(10, I)
p2 = calcola_potenza_ri(100, I)
p3 = calcola_potenza_vr(10, 100)
assert abs(p1 - p2) < 1e-9 and abs(p2 - p3) < 1e-9

# TEST 9: Validazione circuito coerente
assert valida_circuito(10, 0.1, 100) == True

# TEST 10: Validazione circuito incoerente
assert valida_circuito(10, 0.1, 50) == False  # V ≠ R×I
```

---

## 🛠️ Step Implementazione (7-8 passaggi)

### STEP 1: Setup e Conversioni di Base ✅
- [ ] Creare file `soluzione.py`
- [ ] Implementare `converti_tensione()`, `converti_corrente()`, `converti_resistenza()`
- [ ] Usare dizionari con fattori di conversione:
  ```python
  FATTORI_TENSIONE = {
      'nV': 1e-9, 'μV': 1e-6, 'mV': 1e-3, 'V': 1, 'kV': 1e3
  }
  ```
- [ ] Testare conversioni comuni (mV↔V, mA↔A)

### STEP 2: Legge di Ohm Base 🎯
- [ ] Implementare `calcola_tensione()`, `calcola_corrente()`, `calcola_resistenza()`
- [ ] Aggiungere validazione:
  - Resistenza != 0
  - Valori non negativi
  - Lanciare `ValueError` se invalidi
- [ ] Testare con valori tipici:
  - 5V, 100Ω → 0.05A
  - 230V, 0.26A → 885Ω
  - 12V, 0.5A → 24Ω

### STEP 3: Potenza Elettrica 💡
- [ ] Implementare tre funzioni: `calcola_potenza_vi()`, `calcola_potenza_ri()`, `calcola_potenza_vr()`
- [ ] Verificare equivalenza (date V, R, calcolare I e testare tutti e tre i metodi)
- [ ] Testare con esempi:
  - Lampadina 60W @ 230V
  - LED 5V, 10mA
  - Resistore 100Ω, 10V

### STEP 4: Parametri Circuito Globali 📋
- [ ] Implementare `parametri_circuito()`
- [ ] Gestire 3 casi: dati (V, R), (V, I), (R, I)
- [ ] Calcolare il parametro mancante
- [ ] Ritornare dizionario con: V, I, R, P, energia_1h
- [ ] Testare con circuiti reali

### STEP 5: Validazione e Sicurezza 🛡️
- [ ] Implementare `valida_circuito()` - verificare coerenza legge di Ohm
- [ ] Implementare `classifica_condizione()` - effetti corrente corpo umano
- [ ] Aggiungere avvertimenti per correnti > 50mA
- [ ] Testare con valori pericolosi

### STEP 6: Resistori e Codice Colori 🎨
- [ ] Implementare `resistor_colori_a_ohm()`
- [ ] Codifica colori: 0-9, moltiplicatore
- [ ] Testare esempi:
  - Marrone-Nero-Rosso → 10 × 10² = 1 kΩ
  - Rosso-Violetto-Arancione → 27 × 10³ = 27 kΩ
  - Verde-Blu-Giallo → 56 × 10⁴ = 560 kΩ

### STEP 7: Test Completo ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare eccezioni lanciate
- [ ] Testare edge cases:
  - Resistenza = 0
  - Corrente = 0
  - Tensione = 0

### STEP 8: Documentazione e Esempi 📚
- [ ] Aggiungere docstring complete
- [ ] Creare file `esempi_pratici.py` con:
  - Lampadina da 60W
  - Circuito amplificatore 12V
  - LED con resistore
  - Sensore NTC
- [ ] Documentare assunzioni

---

## 💡 Trucchi Python & TLC 🎯

### Trucchi Python 🐍
1. **Dizionari per fattori di conversione:**
   ```python
   FATTORI = {'mV': 1e-3, 'V': 1, 'kV': 1e3}
   valore_v = valore_mv * FATTORI['mV'] / FATTORI['V']
   ```

2. **Validazione multipla:**
   ```python
   if not (isinstance(V, (int, float)) and V >= 0):
       raise ValueError("Tensione deve essere numero >= 0")
   ```

3. **Precauzione divisione per zero:**
   ```python
   if R == 0:
       raise ValueError("Resistenza non può essere zero")
   I = V / R  # Sicuro
   ```

4. **Dizionario per parametri:**
   ```python
   param = {
       'tensione': V,
       'corrente': I,
       'resistenza': R,
       'potenza': P
   }
   return param
   ```

5. **F-string per output fisico:**
   ```python
   print(f"V = {V:.2f} V")
   print(f"I = {I*1000:.1f} mA")  # Conversione inline
   print(f"P = {P:.2f} W @ {R/1000:.1f} kΩ")
   ```

### Trucchi TLC 📡
1. **Valori standard resistori (E12 series):**
   ```
   10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82
   + moltiplicatori: 10^n
   Esempio: 470 Ω, 2.2 kΩ, 100 kΩ
   ```

2. **Potenza dissipata = calore:**
   ```
   P = 1 W su resistore 0.6 cm² → ΔT ≈ 100°C
   Sempre considerare dissipatore per P > 0.5 W
   ```

3. **Resistenza dipende da temperatura:**
   ```
   R(T) = R0 × [1 + α × (T - T0)]
   α = coefficiente temp. (rame: 0.004/°C)
   ```

4. **Impedenza in AC:**
   ```
   Per segnali AC sinusoidali:
   - Resistore: Z = R (indipendente da frequenza)
   - Induttore: Z = jωL (aumenta con frequenza)
   - Condensatore: Z = 1/(jωC) (diminuisce con frequenza)
   ```

5. **Dissipazione potenza in cavi:**
   ```
   P_loss = I² × R_cavo
   Es: 10A su cavo 0.1Ω → P_loss = 10W
   Importante: Usare sezione cavo adeguata!
   ```

---

## ⚠️ Errori Comuni (Fisici + Codice) 🐛

### Errori Fisici 📉

1. **Confondere tensione e corrente**
   ```
   ❌ "Corrente di 230V" (unità sbagliata!)
   ✅ "Tensione di 230V" oppure "Corrente di 10A"
   ```

2. **Dimenticare unità derivate**
   ```
   ❌ I = 0.5  (unità assente!)
   ✅ I = 0.5 A  (sempre specificare)
   ```

3. **Confondere potenza nominale con reale**
   ```
   ❌ Lampadina 60W @ 230V, collegata @ 115V
       Potenza reale: P = 115²/885 ≈ 15W (4× meno!)
   ✅ Utilizzare sempre tensione nominale
   ```

4. **Negligenza resistenza cavi**
   ```
   ❌ Cavo 100m @ 10A: perdita = 10² × 1Ω = 100W!
   ✅ Calcolare sezione cavo: V_perdita < 3% di V_tot
   ```

5. **Temperatura cambia resistenza**
   ```
   ❌ Misurare R a freddo, usarla a caldo (errore ~20%)
   ✅ Considerare R(T) o misurare a regime termico
   ```

### Errori di Codice 💻

1. **Divisione per zero non controllata**
   ```python
   ❌ def calcola_corrente(V, R):
        return V / R  # Crash se R=0

   ✅ def calcola_corrente(V, R):
        if R == 0:
            raise ValueError("R non può essere 0")
        return V / R
   ```

2. **Confondere moltiplicatori unità**
   ```python
   ❌ mV_to_V = 1000  # SBAGLIATO!
   ✅ mV_to_V = 1e-3  # mV = 10⁻³ V

   # Quando converti: V = mV × 1e-3
   ```

3. **Float precision**
   ```python
   ❌ if calcola_tensione(100, 0.1) == 10:  # Potrebbe fallire
   ✅ if abs(calcola_tensione(100, 0.1) - 10) < 1e-9:
   ```

4. **Validazione incompleta**
   ```python
   ❌ R_lista = [100, 200, -50]  # Resistenza negativa!
   ✅ for R in R_lista:
        if R <= 0:
            raise ValueError(f"Resistenza {R} invalida")
   ```

5. **Unità miste**
   ```python
   ❌ P = 10 * 5  # 10V × 5A o 10mA × 5kΩ?
   ✅ P = 10  # V
       * 5  # A
       # P = 50 W (con unità chiare)
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Simulatore Circuito Interattivo ⭐
```python
def simula_circuito_rc(V, R, C, durata, fs=1000):
    """
    Simula carica/scarica circuito RC.

    Equazione:
    V_C(t) = V × (1 - exp(-t/τ))
    τ = R × C (costante tempo)

    Genera:
    - Array tempi
    - Tensione su condensatore
    - Corrente nel circuito
    """
```

### Sfida 2: Analisi Potenza 3-Fase ⭐
```python
def potenza_3fase(V_rms, corrente_rms, cos_phi):
    """
    Calcola potenze in sistema 3-fase.

    Potenza attiva: P = √3 × V × I × cos(φ)
    Potenza reattiva: Q = √3 × V × I × sin(φ)
    Potenza apparente: S = √3 × V × I
    """
```

### Sfida 3: Codice Colori Inverso ⭐
```python
def ohm_a_resistor_colori(resistenza_ohm):
    """
    Inverso di resistor_colori_a_ohm.

    Input: 4700 (4.7 kΩ)
    Output: (Giallo, Violetto, Rosso)  # 47 × 10²
    """
```

### Sfida 4: Calcolo Sezione Cavo ⭐⭐
```python
def calcola_sezione_cavo(corrente_a, lunghezza_m, caduta_max_perc=3):
    """
    Calcola sezione cavo rame per perdita accettabile.

    Dato:
    - Corrente [A]
    - Lunghezza [m]
    - Caduta tensione max [%]

    Restituisce sezione in mm² (standard: 0.5, 1, 1.5, 2.5, 4, 6, ...)
    """
```

### Sfida 5: Bilancio Termico Circuito ⭐⭐
```python
def temperatura_componente(P_watts, area_cm2, ambient_temp_c=25):
    """
    Stima temperatura componente con dissipatore.

    Resistenza termica: θ ≈ 100/√A [°C/W] (senza dissipatore)
    Con dissipatore: θ ≈ 10 [°C/W]

    T_giunzione = T_ambiente + P × θ
    """
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione Python
- [Python: math module](https://docs.python.org/3/library/math.html)
- [Python: Exception handling](https://docs.python.org/3/tutorial/errors.html)

### Fisica Elettrica
- [Wikipedia: Ohm's Law](https://en.wikipedia.org/wiki/Ohm%27s_law)
- [Wikipedia: Electrical Resistance](https://en.wikipedia.org/wiki/Electrical_resistance)
- [Wikipedia: Electric Power](https://en.wikipedia.org/wiki/Electric_power)

### TLC - Applicazioni
- [Resistor Color Code](https://en.wikipedia.org/wiki/Resistor#Color_coding)
- [IEEE 1541-2002: Prefissi Unità](https://en.wikipedia.org/wiki/Metric_prefix)

### Libri
1. Millman & Grabel, "Microelectronics" (Cap. 1)
2. Sedra & Smith, "Microelectronic Circuits" (Cap. 1)

---

## 🎯 Preparazione Esercizi Successivi 🔮

### ES04 - Circuiti Serie/Parallelo 🔌
- Resistenze in serie: Req = R1 + R2 + R3 + ...
- Resistenze in parallelo: 1/Req = 1/R1 + 1/R2 + 1/R3 + ...
- Applicare legge di Ohm a circuiti complessi

### ES05 - Mezzi Trasmissivi 📡
- Attenuazione dipende da potenza iniziale
- Potenza = Tensione² / Impedanza
- Calcoli in dB: dB = 10 × log10(P_out/P_in)

### ES06+ - Circuiti AC e Impedenza ⚡
- Impedenza Z = R + j(ωL - 1/(ωC))
- Fattore di potenza cos(φ) = R/Z
- Potenza reattiva Q = V × I × sin(φ)

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi tutta la consegna
[ ] Comprendi legge di Ohm e potenza
[ ] Identifica i 3 step base

IMPLEMENTAZIONE:
[ ] Step 1: Conversioni unità
[ ] Step 2: Legge di Ohm base
[ ] Step 3: Potenza (3 metodi)
[ ] Step 4: Parametri globali
[ ] Step 5: Validazione
[ ] Step 6: Colori resistori
[ ] Step 7: Test (10 cases)
[ ] Step 8: Documentazione

VALIDAZIONE:
[ ] Tutti i test passano
[ ] Eccezioni corrette
[ ] Edge cases gestiti
[ ] Docstring presenti

BONUS:
[ ] Almeno 1 sfida bonus
[ ] Esempi pratici (lampadina, LED, sensore)
```

---

## 🎓 Conclusione

Hai imparato i **fondamenti dell'elettrotecnica** applicati a TLC:
- Legge di Ohm (la relazione base)
- Potenza (dissipazione calore)
- Validazione circuiti (coerenza fisica)

Questi concetti torneranno in OGNI esercizio successivo!

**Prossimo step:** ES04 - Circuiti più complessi con resistenze in serie/parallelo! 🔌

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS