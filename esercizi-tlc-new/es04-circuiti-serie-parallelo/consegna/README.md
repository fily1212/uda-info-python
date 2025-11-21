# ES04 - Circuiti in Serie e Parallelo 🔌

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐⭐ BASE |
| **Durata Stimata** | 3-4 ore |
| **Linguaggio** | Python 3.8+ |
| **Prerequisiti** | ES03 Legge di Ohm completato |
| **Argomento TLC** | Circuiti: analisi serie/parallelo, tensione efficace AC |

---

## 🎓 Concetti Fondamentali

### Topologia Circuiti: Serie vs Parallelo 🔗

#### Collegamento in SERIE 📏
**Definizione:** Componenti collegati uno dopo l'altro. La stessa corrente attraversa tutti.

```
Circuito serie:
      Vin
      │
      ├─ R1 ─┬─ R2 ─┬─ R3 ─┐
             │      │      │
             │      │      │
    ─────────┴──────┴──────┴─────
             GND (Massa)

Caratteristiche:
- Stessa corrente I attraversa tutti
- Tensione si divide: V_tot = V1 + V2 + V3 + ...
- Resistenza equivalente: R_eq = R1 + R2 + R3 + ...
```

**Vantaggi/Svantaggi:**
```
✓ Semplice da analizzare
✓ Stessa corrente ovunque
✗ Fallingazione: se un componente si rompe, tutto si ferma
✗ Tensione bassa su ogni resistore (se molte)
```

**Esempio pratico:** Luci di Natale vecchie (tutte in serie - se una si brucia, tutte si spengono)

#### Collegamento in PARALLELO ↔️
**Definizione:** Componenti collegati fra gli stessi due punti. Stessa tensione su tutti.

```
Circuito parallelo:
         Vin
          │
     ┌────┴────┐
     │    │    │
    R1   R2   R3
     │    │    │
     └────┬────┘
          │
        GND

Caratteristiche:
- Stessa tensione V su tutti
- Corrente si divide: I_tot = I1 + I2 + I3 + ...
- Resistenza equivalente: 1/R_eq = 1/R1 + 1/R2 + 1/R3 + ...
```

**Vantaggi/Svantaggi:**
```
✓ Ridondanza: se un componente muore, altri funzionano
✓ Tensione uguale su tutti (resistori uguali)
✗ Corrente totale alta (dissipazione)
✗ Resistenza equivalente MINORE
```

**Esempio pratico:** Prese elettriche in casa (tutte in parallelo - accendere una lampada non spegne le altre)

---

## 📐 Formule Fondamentali

### Resistenze in SERIE 📏

```
R_eq = R1 + R2 + R3 + ... + Rn

Generico:
R_eq = Σ Ri  (i = 1 a n)

Proprietà:
- R_eq > max(Ri)
- R_eq cresce con ogni resistenza aggiunta
```

**Esempio:**
```
R1 = 100 Ω
R2 = 150 Ω
R3 = 50 Ω

R_eq = 100 + 150 + 50 = 300 Ω
```

### Resistenze in PARALLELO ↔️

```
1/R_eq = 1/R1 + 1/R2 + 1/R3 + ... + 1/Rn

Oppure (caso 2 resistenze):
R_eq = (R1 × R2) / (R1 + R2)

Proprietà:
- R_eq < min(Ri)
- R_eq diminuisce aggiungendo resistenze
```

**Esempio:**
```
R1 = 100 Ω
R2 = 100 Ω
R3 = 100 Ω (3 × 100Ω in parallelo)

1/R_eq = 1/100 + 1/100 + 1/100 = 3/100
R_eq = 100/3 ≈ 33.3 Ω
```

**Caso speciale:** n resistenze uguali (R) in parallelo:
```
R_eq = R / n
```

### Divisore di Tensione (Serie) ⚖️

Quando resistenze sono in serie, la tensione si divide in proporzione alle resistenze:

```
Circuito:
    V_in ─┬─ R1 ─┬─ R2 ─┬
          │      │      │
          └──────┴──────┘
                GND

Tensione su R2:
V2 = V_in × R2 / (R1 + R2)

Formula generale:
Vi = V_in × Ri / R_eq
```

**Applicazione TLC:** Attenuatori, sensori di livello, partitori per ADC

**Esempio:**
```
V_in = 10 V
R1 = 90 Ω (attenuatore)
R2 = 10 Ω (carico)

V2 = 10 × 10 / (90 + 10) = 10 × 10 / 100 = 1 V
Attenuazione: 10:1
```

### Divisore di Corrente (Parallelo) 🌀

Quando resistenze sono in parallelo, la corrente si divide inversamente alle resistenze:

```
Circuito:
    I_in ─┬─ R1 ─┬
          │      │
          ┼─ R2 ─┤
          │      │
          ┴──────┘
           GND

Corrente per R2:
I2 = I_in × R1 / (R1 + R2)  (Si invertono!)

Oppure:
I2 = I_in × (R_eq / R2)

Proprietà:
- Corrente maggiore passa per resistenza minore!
```

**Esempio:**
```
I_in = 10 A
R1 = 100 Ω (resistenza bassa)
R2 = 1000 Ω (resistenza alta)

I1 = 10 × 1000 / (100 + 1000) = 10 × 1000/1100 = 9.09 A (più del 90%)
I2 = 10 × 100 / (100 + 1000) = 10 × 100/1100 = 0.91 A (solo 9%)
```

---

## 🔄 Tensione Efficace (RMS) in AC 🌊

In telecomunicazioni, i segnali sono spesso **alternati sinusoidali**.

```
Segnale AC sinusoidale:
v(t) = V_picco × sin(2πft)

Dove:
- V_picco = ampiezza massima (tensione di picco)
- f = frequenza
```

### Valore RMS (Root Mean Square)

```
V_rms = V_picco / √2  ≈ 0.707 × V_picco

Oppure:
V_picco = V_rms × √2  ≈ 1.414 × V_rms
```

**Significato fisico:**
```
Potenza dissipata su R:
- DC (continua): P = V² / R
- AC sinusoidale: P = V_rms² / R  (non V_picco!)
```

**Esempio pratico - Elettricità domestica:**
```
Tensione AC Europa: 230 V RMS (valore efficace)
Tensione picco: 230 × √2 ≈ 325 V
Quando lampadina 60W @ 230V brillà:
P = 230² / R
60 = 52900 / R
R ≈ 882 Ω (resistenza a regime termico)
```

### Conversione Picco ↔ RMS

```
V_rms = V_picco / √2
V_picco = V_rms × √2

Fattore di conversione: 1/√2 ≈ 0.7071
```

---

## 💻 Funzioni Python da Implementare

### Livello 1: Resistenze in Serie 📏

```python
def resistenza_serie(resistenze_lista):
    """
    Calcola resistenza equivalente per resistenze in serie.

    Formula: R_eq = R1 + R2 + R3 + ...

    Args:
        resistenze_lista (list): Lista di resistenze [R1, R2, ..., Rn] in Ohm

    Returns:
        float: Resistenza equivalente in Ohm

    Raises:
        ValueError: se lista vuota o valori negativi

    Esempio:
        >>> resistenza_serie([100, 150, 50])
        300.0
    """
    # Sommare tutti gli elementi della lista


def resistenza_parallelo(resistenze_lista):
    """
    Calcola resistenza equivalente per resistenze in parallelo.

    Formula: 1/R_eq = 1/R1 + 1/R2 + 1/R3 + ...

    Args:
        resistenze_lista (list): Lista di resistenze [R1, R2, ..., Rn] in Ohm

    Returns:
        float: Resistenza equivalente in Ohm

    Raises:
        ValueError: se lista vuota, valori zero/negativi

    Esempio:
        >>> resistenza_parallelo([100, 100, 100])
        33.333...
    """
    # 1. Verificare nessuno zero
    # 2. Calcolare somma reciproci
    # 3. Ritornare inverso


def resistenza_parallelo_due(r1, r2):
    """
    Formula semplificata per due resistenze in parallelo.

    Formula: R_eq = (R1 × R2) / (R1 + R2)

    Più veloce del caso generale.

    Args:
        r1 (float): Prima resistenza [Ω]
        r2 (float): Seconda resistenza [Ω]

    Returns:
        float: Resistenza equivalente [Ω]
    """
    # Usare formula semplificata
```

### Livello 2: Analisi Circuito Serie/Parallelo 🔍

```python
def analizza_circuito_serie(V_totale, resistenze_lista):
    """
    Analizza circuito resistivo in serie.

    Args:
        V_totale (float): Tensione totale [V]
        resistenze_lista (list): Resistenze [R1, R2, ..., Rn] [Ω]

    Returns:
        dict: {
            'R_eq': resistenza equivalente,
            'I_totale': corrente totale,
            'V_lista': [V1, V2, ...],  # Tensioni su ogni R
            'P_lista': [P1, P2, ...],  # Potenze su ogni R
            'P_totale': potenza totale
        }
    """
    # 1. Calcolare R_eq
    # 2. Calcolare I_totale = V / R_eq
    # 3. Per ogni R: Vi = I × Ri, Pi = I² × Ri
    # 4. Ritornare dizionario


def analizza_circuito_parallelo(V_totale, resistenze_lista):
    """
    Analizza circuito resistivo in parallelo.

    Args:
        V_totale (float): Tensione totale [V]
        resistenze_lista (list): Resistenze [R1, R2, ..., Rn] [Ω]

    Returns:
        dict: {
            'R_eq': resistenza equivalente,
            'I_totale': corrente totale,
            'I_lista': [I1, I2, ...],  # Correnti su ogni R
            'P_lista': [P1, P2, ...],  # Potenze su ogni R
            'P_totale': potenza totale
        }
    """
    # 1. Calcolare R_eq
    # 2. Per ogni R: Ii = V / Ri, Pi = V² / Ri
    # 3. Calcolare I_totale = somma Ii
    # 4. Ritornare dizionario
```

### Livello 3: Divisore di Tensione e Corrente ⚖️

```python
def divisore_tensione(V_in, r1, r2):
    """
    Calcola tensione su R2 in divisore di tensione.

    Circuito: V_in ─┬─ R1 ─┬─ R2 ─┐
                    │      │      │
                    └──────┴──────┘

    Formula: V2 = V_in × R2 / (R1 + R2)

    Args:
        V_in (float): Tensione ingresso [V]
        r1 (float): Prima resistenza (serie) [Ω]
        r2 (float): Seconda resistenza (serie) [Ω]

    Returns:
        tuple: (V_r1, V_r2) tensioni su R1 e R2

    Esempio:
        >>> V1, V2 = divisore_tensione(10, 90, 10)
        >>> V2
        1.0
    """
    # Applicare formula divisore
    # Restituire (V1, V2)


def divisore_corrente(I_in, r1, r2):
    """
    Calcola corrente su ogni R in divisore di corrente.

    Circuito in parallelo con sorgente corrente I_in.

    Formula: I2 = I_in × R1 / (R1 + R2)  (invertito!)

    Args:
        I_in (float): Corrente ingresso [A]
        r1 (float): Prima resistenza (parallelo) [Ω]
        r2 (float): Seconda resistenza (parallelo) [Ω]

    Returns:
        tuple: (I_r1, I_r2) correnti su R1 e R2

    Nota: Corrente MINORE passa per resistenza MAGGIORE
    """
    # Applicare formula divisore corrente (reciproca!)
```

### Livello 4: Tensione RMS e AC 🌊

```python
def rms_da_picco(v_picco):
    """
    Converte tensione di picco a RMS.

    Formula: V_rms = V_picco / √2

    Args:
        v_picco (float): Tensione picco [V]

    Returns:
        float: Tensione RMS [V]

    Esempio:
        >>> rms_da_picco(325)
        230.0  (approssimativamente)
    """


def picco_da_rms(v_rms):
    """
    Converte tensione RMS a picco.

    Formula: V_picco = V_rms × √2

    Args:
        v_rms (float): Tensione RMS [V]

    Returns:
        float: Tensione picco [V]

    Esempio:
        >>> picco_da_rms(230)
        325.27...
    """


def potenza_ac(v_rms, resistenza):
    """
    Calcola potenza dissipata in AC sinusoidale.

    Nota IMPORTANTE:
    P = V_rms² / R  (NON V_picco!)

    Args:
        v_rms (float): Tensione RMS [V]
        resistenza (float): Resistenza [Ω]

    Returns:
        float: Potenza [W]

    Esempio:
        >>> potenza_ac(230, 883)
        60.0  (lampadina)
    """
```

### Livello 5: Visualizzazione ASCII 🎨

```python
def disegna_circuito_serie(resistenze_lista, V_totale):
    """
    Disegna circuito serie in ASCII art.

    Output:
    ```
    V_in=10V
      │
      ├─ R1=100Ω (V=6.67V, I=0.067A, P=0.44W)
      ├─ R2=150Ω (V=10V, I=0.067A, P=0.44W)
      ├─ R3=50Ω (V=3.33V, I=0.067A, P=0.22W)
      │
      ├─ R_eq=300Ω
      ├─ I_tot=0.033A
      ├─ P_tot=1.1W
      │
      GND
    ```
    """


def disegna_circuito_parallelo(resistenze_lista, V_totale):
    """
    Disegna circuito parallelo in ASCII art.

    Output:
    ```
      V_in=10V
        │
      ┌─┴─┐
      │   │     │      │
     R1  R2    R3
     100Ω 100Ω 100Ω
    (0.1A) (0.1A) (0.1A)
      │     │      │
      └─┬─┘
        │
        ├─ R_eq≈33.3Ω
        ├─ I_tot=0.3A
        ├─ P_tot=3W
        │
        GND
    ```
    """
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### Esempio 1: Circuito AC Domestico 🏠
```
Sistema europeo:
- Tensione: 230V RMS (efficace)
- Frequenza: 50 Hz
- Prese in parallelo

Calcolo:
- Tensione picco: 230 × √2 ≈ 325V
- Lampadina 60W @ 230V: R ≈ 883Ω
- Corrente picco: I_picco = 325 / 883 ≈ 0.368A
- Corrente RMS: I_rms = 0.368 / √2 ≈ 0.26A
```

### Esempio 2: Partitore di Tensione (Sensore) 📊
```
Sensore di temperatura con ADC:

       5V
        │
       10kΩ (R_pull-up)
        │
        ├──── Vin (→ ADC 0-5V)
        │
     NTC (resistenza variabile)
       5-50kΩ
        │
       GND

Analisi:
- A 25°C: R_ntc = 10kΩ → V_in = 5 × 10/(10+10) = 2.5V
- A 35°C: R_ntc ≈ 6.5kΩ → V_in = 5 × 6.5/(10+6.5) ≈ 2V
- Sensibilità: 50mV/°C
```

### Esempio 3: Bilanciamento Carico in Parallelo 🔌
```
Due LED con resistori di limitazione (corrente):

LED1: V_f=2V, I_f=20mA
LED2: V_f=2V, I_f=20mA
V_alim = 5V

Problema: Se collegati in parallelo senza resistori diversi,
uno prende più corrente dell'altro (variazione VF).

Soluzione: Usare resistori di limitazione calcoli su resistenza:
V_resistore = 5 - 2 = 3V
Necessario: I = 10mA (per affidabilità)
R = 3 / 0.01 = 300Ω

Con R=300Ω su entrambi, la corrente è bilanciata (entro tolleranza).
```

### Esempio 4: Stub Matching in RF 📡
```
Adattamento impedenza in linea di trasmissione (80Ω):

Carico: Z_L = 50Ω (non adattato)

Stub: Lunghezza linea cortocircuitata aggiunta in parallelo
Calcolo stub richiede: Diagramma Smith, numero di stubs, distanza.

Semplificato: Due valori di impedenza in parallelo:
Z_eq = (Z1 × Z2) / (Z1 + Z2)
Risolvere per Z_eq = 80Ω con Z_L = 50Ω.
```

### Esempio 5: Attenuatore Sfasatore 🎚️
```
Attenuatore π (pad):

      ┌─ R_serie ─┐
      │           │
   Vin ├─ R_par ─ ├ Vout
      │           │
      └─ R_par ─┘
         (parallelo)

Attenuazione desiderata: 10 dB
Impedenza adattata: 50Ω

Calcoli:
- Rapporto attenuazione: 10^(10/20) = √10 ≈ 3.16
- R_serie, R_par calcolati da impedenza e attenuazione
```

---

## 🧪 Test Cases (8-10 casi)

```python
# TEST 1: Resistenze serie - somma semplice
assert abs(resistenza_serie([100, 150, 50]) - 300) < 1e-9

# TEST 2: Resistenze parallelo - formula
assert abs(resistenza_parallelo([100, 100, 100]) - 33.333) < 0.01

# TEST 3: Due resistenze parallelo - formula semplificata
assert abs(resistenza_parallelo_due(100, 100) - 50) < 1e-9

# TEST 4: Parallelo - R_eq < min(Ri)
r_eq = resistenza_parallelo([100, 200, 300])
assert r_eq < 100

# TEST 5: Divisore di tensione - partizione
V1, V2 = divisore_tensione(10, 90, 10)
assert abs(V1 - 9) < 1e-9
assert abs(V2 - 1) < 1e-9

# TEST 6: Divisore tensione - somma V
V1, V2 = divisore_tensione(100, 60, 40)
assert abs((V1 + V2) - 100) < 1e-9

# TEST 7: RMS da picco - AC domestico
V_rms = rms_da_picco(325)
assert abs(V_rms - 230) < 1  # Circa 230V

# TEST 8: Picco da RMS - inverso
V_picco = picco_da_rms(230)
assert abs(V_picco - 325) < 1

# TEST 9: Potenza AC - lampadina
# 60W @ 230V RMS in R=883Ω
P = potenza_ac(230, 883)
assert abs(P - 60) < 1

# TEST 10: Circuito parallelo - corrente totale
analisi = analizza_circuito_parallelo(10, [100, 100, 100])
assert abs(analisi['I_totale'] - 0.3) < 0.01  # 10V / 33.3Ω ≈ 0.3A
```

---

## 🛠️ Step Implementazione (7-8 passaggi)

### STEP 1: Resistenze in Serie e Parallelo ✅
- [ ] Implementare `resistenza_serie()` - somma semplice
- [ ] Implementare `resistenza_parallelo()` - formula reciproci
- [ ] Implementare `resistenza_parallelo_due()` - caso ottimizzato
- [ ] Testare con valori tipici:
  - Serie: [100, 200, 300] → 600Ω
  - Parallelo: [100, 100, 100] → 33.3Ω

### STEP 2: Analisi Circuito Serie 📏
- [ ] Implementare `analizza_circuito_serie()`
- [ ] Calcolare: R_eq, I_totale, V su ogni R, P su ogni R
- [ ] Verificare: Somma V = V_totale, Somma P = P_totale
- [ ] Testare con 2-3 resistenze

### STEP 3: Analisi Circuito Parallelo ↔️
- [ ] Implementare `analizza_circuito_parallelo()`
- [ ] Calcolare: R_eq, I su ogni R, P su ogni R
- [ ] Verificare: V uguale su tutti, Somma I = I_totale
- [ ] Testare con 2-3 resistenze

### STEP 4: Divisore di Tensione e Corrente ⚖️
- [ ] Implementare `divisore_tensione()`
- [ ] Implementare `divisore_corrente()` (formula inversa!)
- [ ] Testare:
  - Tensione: 10V su [90Ω, 10Ω] → [9V, 1V]
  - Corrente: 10A su [100Ω, 1000Ω] → [9.09A, 0.91A]

### STEP 5: Tensione AC e RMS 🌊
- [ ] Implementare `rms_da_picco()` - dividi per √2
- [ ] Implementare `picco_da_rms()` - moltiplica per √2
- [ ] Implementare `potenza_ac()` - usa V_rms!
- [ ] Testare: 230V RMS → 325V picco, lampadina 60W @ 230V

### STEP 6: Visualizzazione ASCII 🎨
- [ ] Implementare `disegna_circuito_serie()`
- [ ] Implementare `disegna_circuito_parallelo()`
- [ ] Output leggibile con parametri
- [ ] Testare con piccoli circuiti (2-3 R)

### STEP 7: Test Completo ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare coerenza (serie + parallelo)
- [ ] Testare edge cases (1 resistenza, resistenze uguali)

### STEP 8: Documentazione e Esempi 📚
- [ ] Creare file `esempi.py` con:
  - Circuito domestico 230V
  - Sensore con partitore tensione
  - LED con resistore
- [ ] Aggiungere docstring complete

---

## 💡 Trucchi Python & TLC 🎯

### Trucchi Python 🐍
1. **Somma lista efficiente:**
   ```python
   R_eq = sum(resistenze_lista)  # Già fatto!
   ```

2. **Reciproci:**
   ```python
   inversi = [1/R for R in resistenze_lista]
   R_eq = 1 / sum(inversi)
   ```

3. **Radice quadrata:**
   ```python
   import math
   rad_due = math.sqrt(2)  # ≈ 1.414
   V_picco = V_rms * rad_due
   ```

4. **Dizionario per risultati complessi:**
   ```python
   risultato = {
       'R_eq': R_eq,
       'I_lista': [I1, I2, I3],
       'P_lista': [P1, P2, P3],
       'verifiche': {'sum_V': V1+V2, 'sum_P': P1+P2}
   }
   ```

5. **List comprehension per calcoli:**
   ```python
   V_lista = [calcola_tensione(R, I_tot) for R in R_lista]
   ```

### Trucchi TLC 📡
1. **Serie aumenta resistenza, parallelo la diminuisce:**
   ```
   Serie: R_eq > max(Ri)
   Parallelo: R_eq < min(Ri)
   ```

2. **Potenza RMS vs Picco (IMPORTANTE!):**
   ```
   DC: P = V² / R
   AC: P = V_rms² / R  ← NON V_picco!

   Errore comune:
   ❌ P = 325² / R  = 105625 / R  (Sbagliato!)
   ✅ P = 230² / R  = 52900 / R   (Giusto!)
   ```

3. **Divisore tensione - Formula mnemonica:**
   ```
   V_out è proporzionale alla R_out:
   V_out = V_in × R_out / (R_in + R_out)
   ```

4. **Divisore corrente - Reciproco:**
   ```
   I_out è INVERSAMENTE proporzionale a R_out:
   I_out = I_in × R_in / (R_in + R_out)
   (Attenzione: nel numeratore va l'ALTRA R!)
   ```

5. **Attenuatore 10:1 (pratico):**
   ```
   Per dimezzare la tensione: R_in = R_out
   Per attenuare 10×: R_in = 9 × R_out
   Per attenuare 100×: R_in = 99 × R_out
   ```

---

## ⚠️ Errori Comuni 🐛

### Errori Fisici 📉

1. **Confondere serie e parallelo**
   ```
   ❌ "Due resistenze in serie: 1/R_eq = 1/R1 + 1/R2"
   ✅ "Due resistenze in serie: R_eq = R1 + R2"
   ```

2. **Usare V_picco per potenza AC**
   ```
   ❌ P = V_picco² / R = 325² / 883 ≈ 120W (SBAGLIATO!)
   ✅ P = V_rms² / R = 230² / 883 ≈ 60W (GIUSTO!)
   ```

3. **Dimenticare che tensione è uguale in parallelo**
   ```
   ❌ "In parallelo, ogni R ha tensione diversa"
   ✅ "In parallelo, ogni R ha STESSA tensione V"
   ```

4. **Dimenticare che corrente è uguale in serie**
   ```
   ❌ "In serie, ogni R ha corrente diversa"
   ✅ "In serie, ogni R ha STESSA corrente I"
   ```

5. **Resistenza negativa?**
   ```
   ❌ Consentire resistenze negative
   ✅ Lanciare ValueError se R < 0
   ```

### Errori di Codice 💻

1. **Divisione per zero in parallelo**
   ```python
   ❌ R_eq = 1 / sum([1/R for R in lista])
       # Crash se uno zero nella lista

   ✅ for R in lista:
       if R == 0:
           raise ValueError("Resistenza zero")
   ```

2. **Confondere formule semplicate**
   ```python
   ❌ R_parallelo_due = (r1 + r2) / (r1 * r2)  # SBAGLIATO!
   ✅ R_parallelo_due = (r1 * r2) / (r1 + r2)  # GIUSTO!
   ```

3. **RMS da picco - dimenticare √2**
   ```python
   ❌ V_rms = V_picco / 2  # Sbagliato!
   ✅ V_rms = V_picco / math.sqrt(2)  # Giusto!
   ```

4. **Confronto esatto di float**
   ```python
   ❌ if V1 + V2 == V_totale:  # Potrebbe fallire!
   ✅ if abs((V1 + V2) - V_totale) < 1e-9:
   ```

5. **Indice lista errato**
   ```python
   ❌ P_lista[3] su lista di 3 elementi (IndexError)
   ✅ Sempre iterare: for i, P in enumerate(P_lista)
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Circuito Misto (Serie-Parallelo) ⭐
```python
def analizza_circuito_misto(V_in, config):
    """
    Analizza circuiti combinati serie-parallelo.

    Config: {'tipo': 'serie', 'elementi': [R1, R2, {...}]}

    Ricorsivo per circuiti complessi:
    - R1 in serie con (R2 || R3)
    - (R1 || R2) in serie con R3
    """
```

### Sfida 2: Wheatstone Bridge (Ponte) ⭐⭐
```python
def analizza_ponte_wheatstone(r1, r2, r3, r4, V_alim):
    """
    Analizza circuito ponte Wheatstone.

    Uso: Sensori di precisione (strain gauge, NTC)

    V_out = V_alim × (r2/(r1+r2) - r4/(r3+r4))

    Quando equilibrato:
    r1 × r4 = r2 × r3  → V_out = 0
    """
```

### Sfida 3: Distribuzione Corrente in Parallelo ⭐
```python
def verifica_bilanciamento_parallelo(resistenze_lista, tolleranza_perc=5):
    """
    Verifica se correnti sono bilanciate.

    In un circuito parallelo ideale, resistenze uguali
    dovrebbero avere correnti uguali.

    Ritorna: Percentuale scostamento massimo
    Avviso: Se > tolleranza
    """
```

### Sfida 4: Ottimizzazione Partitore Tensione ⭐⭐
```python
def progetta_partitore_tensione(V_in, V_out_desiderato, Z_ingresso=1e6):
    """
    Calcola R1, R2 per partitore.

    Vincoli:
    - V_out = V_in × R2 / (R1 + R2) = V_out_desiderato
    - Impedenza d'ingresso Z ≈ R1 + R2 = Z_desiderato

    Ricavare R1 e R2.
    """
```

### Sfida 5: Circuito AC con Impedenza Complessa ⭐⭐⭐
```python
def impedenza_rl_serie(r_ohm, l_henry, frequenza_hz):
    """
    Calcola impedenza totale serie RL.

    Z = R + jωL
    ω = 2πf

    |Z| = √(R² + (ωL)²)
    φ = arctan(ωL / R)
    """
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione Python
- [math.sqrt()](https://docs.python.org/3/library/math.html#math.sqrt)
- [List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

### Teoria Circuiti
- [Wikipedia: Series Circuit](https://en.wikipedia.org/wiki/Series_circuit)
- [Wikipedia: Parallel Circuit](https://en.wikipedia.org/wiki/Parallel_circuit)
- [Wikipedia: Voltage Divider](https://en.wikipedia.org/wiki/Voltage_divider)

### TLC Applicazioni
- [Wheatstone Bridge](https://en.wikipedia.org/wiki/Wheatstone_bridge)
- [RF Matching Network](https://en.wikipedia.org/wiki/Impedance_matching)

### Letture Consigliate
1. Nilsson & Riedel, "Electric Circuits" (Cap. 2-3)
2. Robbins & Miller, "Circuit Analysis: Theory and Practice" (Cap. 3)

---

## 🎯 Preparazione Esercizi Successivi 🔮

### ES05 - Mezzi Trasmissivi 📡
- Attenuazione dipende dalla potenza iniziale
- Rapporto potenze in dB: dB = 10 × log10(P_out/P_in)
- Divisore di tensione usato in sensori RF

### ES06+ - Filtri e Impedenza ⚡
- Circuiti RC (passa-basso): f_c = 1/(2πRC)
- Circuiti RL (passa-alto): f_c = R/(2πL)
- Impedenza dipende da frequenza

### ES07 - Trasmissione AC 🌊
- Trasformatori: rapporto spire determina rapporto tensione
- Adattamento impedenza su linee di trasmissione
- Stub matching (parallelo di linee)

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi tutta la consegna
[ ] Comprendi serie vs parallelo
[ ] Capire formule divisore
[ ] Comprendi RMS vs Picco

IMPLEMENTAZIONE:
[ ] Step 1: Serie e parallelo
[ ] Step 2: Analisi serie
[ ] Step 3: Analisi parallelo
[ ] Step 4: Divisori (V e I)
[ ] Step 5: AC e RMS
[ ] Step 6: Visualizzazione ASCII
[ ] Step 7: Test (10 cases)
[ ] Step 8: Documentazione

VALIDAZIONE:
[ ] Tutti i test passano
[ ] Somme di tensioni/correnti corrette
[ ] RMS calcolato correttamente
[ ] Nessun crash edge cases

BONUS:
[ ] Almeno 1 sfida bonus
[ ] Esempi con circuiti reali
```

---

## 🎓 Conclusione

Hai imparato come **analizzare circuiti reali** con serie e parallelo. Questi concetti sono usati OVUNQUE:
- Distribuzioni potenza
- Sensori e trasduttori
- Circuiti di adattamento impedenza
- Filtri e reti di correzione

**Prossimo step:** ES05 - Mezzi trasmissivi e attenuazione del segnale! 📡

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS