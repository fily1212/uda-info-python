# ES08 - Circuiti Combinatori ⚙️

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐⭐ INTERMEDIO |
| **Durata Stimata** | 4-5 ore |
| **Linguaggio** | Python 3.8+ |
| **Prerequisiti** | ES07 - Porte Logiche completato |
| **Argomento TLC** | Elaborazione Digitale: Circuiti Combinatori |

---

## 🎓 Concetti Fondamentali

### Che cos'è un Circuito Combinatorio? 🔌

Un **circuito combinatorio** è un circuito logico dove l'**output dipende SOLO dagli input attuali**, senza memoria di stati precedenti.

```
Circuito Combinatorio:
┌─────────────────────────────────────┐
│  Input A ─┐                         │
│  Input B ─┤─ [Logica] ─ Output Y   │
│  Input C ─┘                         │
│                                     │
│  Y(t) dipende SOLO da A,B,C al t   │
│  NON dipende da stati precedenti    │
└─────────────────────────────────────┘

Caratteristica:
• Nessuna memoria (no flip-flop)
• Nessuna retroazione
• Output immediato con input
```

**Contrasto: Circuito Sequenziale**
```
Circuito Sequenziale:
┌──────────────────────────┐
│ Input ─ [Logica] ┐      │
│                  │ Output
│         ┌────────┘      │
│         │ Memoria       │
│         └────────┬──────┘
│                  │
│          Feedback (retroazione)

Y(t) dipende da Input(t) E da stato precedente
```

**Applicazioni in TLC:**
- Sommatori (addizionamento)
- Comparatori (confronto numeri)
- Multiplexer (commutazione segnali)
- Decoder (selezione canale)
- Codificatori di parità

---

### Proprietà Circuiti Combinatori 📊

```
1. DETERMINISMO:
   Stesso input → Sempre stesso output
   (Prevedibile, senza casualità)

2. NO STATO:
   Non ricorda il passato
   (No memoria, no flip-flop)

3. TEMPO REALE:
   Output appare quasi istantaneamente
   (Ritardo solo propagazione logica)

4. TABELLA DI VERITÀ:
   Descrive completamente il circuito
   2^N righe per N ingressi
```

---

## 💻 Circuiti Combinatori Implementabili

### 1️⃣ Half Adder (Sommatore Mezzo)

**Funzione:** Somma 2 bit senza riporto in ingresso.

```
Ingressi: A (1 bit), B (1 bit)
Uscite: Sum (1 bit), Carry (1 bit)

Formula:
    Sum = A XOR B
    Carry = A AND B

Tabella di Verità:
┌───┬───┬─────┬───────┐
│ A │ B │ Sum │ Carry │
├───┼───┼─────┼───────┤
│ 0 │ 0 │  0  │   0   │
│ 0 │ 1 │  1  │   0   │
│ 1 │ 0 │  1  │   0   │
│ 1 │ 1 │  0  │   1   │ ← Overflow
└───┴───┴─────┴───────┘

Esempio:
  0 + 0 = 00 (sum=0, carry=0)
  1 + 1 = 10 (sum=0, carry=1) ← Riporto!
```

### 2️⃣ Full Adder (Sommatore Completo)

**Funzione:** Somma 2 bit + riporto in ingresso.

```
Ingressi: A, B, Carry_in
Uscite: Sum, Carry_out

Formula:
    Sum = A XOR B XOR Carry_in
    Carry_out = (A AND B) OR (Carry_in AND (A XOR B))

Tabella di Verità:
┌───┬───┬────────┬─────┬────────┐
│ A │ B │Carry_in│ Sum │Carry_o │
├───┼───┼────────┼─────┼────────┤
│ 0 │ 0 │   0    │  0  │   0    │
│ 0 │ 0 │   1    │  1  │   0    │
│ 0 │ 1 │   0    │  1  │   0    │
│ 0 │ 1 │   1    │  0  │   1    │
│ 1 │ 0 │   0    │  1  │   0    │
│ 1 │ 0 │   1    │  0  │   1    │
│ 1 │ 1 │   0    │  0  │   1    │
│ 1 │ 1 │   1    │  1  │   1    │
└───┴───┴────────┴─────┴────────┘

Catena di Full Adder:
   A3 B3       A2 B2       A1 B1       A0 B0
    │  │        │  │        │  │        │  │
    └──┤ FA  ┌──┴──┤ FA  ┌──┴──┤ FA  ┌──┴──┤ FA
       │   │  │       │  │       │  │       │
       └─C_o─┤ C_in  └─C_o─┤ C_in  └─C_o─┤ C_in
           └──────────────────────────────
```

### 3️⃣ Multiplexer (Mux) 🔀

**Funzione:** Seleziona quale input mandare all'output.

```
MUX 2:1 (2 input, 1 select)
┌──────────────────┐
│ I0 ─┐            │
│     ├─ Output    │
│ I1 ─┤            │
│ S ──┘            │
└──────────────────┘

Select = 0 → Output = I0
Select = 1 → Output = I1

MUX 4:1 (4 input, 2 select)
┌────────────────────┐
│ I0 ─┐              │
│ I1 ─┤              │
│ I2 ─┼─ Output      │
│ I3 ─┤              │
│ S1 S0 ─┘           │
└────────────────────┘

S1 S0 → Output
00    → I0
01    → I1
10    → I2
11    → I3

Tabella:
┌────┬────┬────────┐
│ S1 │ S0 │ Output │
├────┼────┼────────┤
│ 0  │ 0  │  I0    │
│ 0  │ 1  │  I1    │
│ 1  │ 0  │  I2    │
│ 1  │ 1  │  I3    │
└────┴────┴────────┘
```

### 4️⃣ Decoder 🔓

**Funzione:** Attiva una sola linea di output in base all'input.

```
DECODER 2-to-4
┌──────────────┐
│ A ─┐         │
│    ├─ Y0    │
│ B ─┘ Y1     │
│    Y2     │
│    Y3     │
└──────────────┘

Input AB → Output attivo
00 → Y0=1, Y1=0, Y2=0, Y3=0
01 → Y0=0, Y1=1, Y2=0, Y3=0
10 → Y0=0, Y1=0, Y2=1, Y3=0
11 → Y0=0, Y1=0, Y2=0, Y3=1

Tabella:
┌───┬───┬────┬────┬────┬────┐
│ A │ B │ Y0 │ Y1 │ Y2 │ Y3 │
├───┼───┼────┼────┼────┼────┤
│ 0 │ 0 │ 1  │ 0  │ 0  │ 0  │
│ 0 │ 1 │ 0  │ 1  │ 0  │ 0  │
│ 1 │ 0 │ 0  │ 0  │ 1  │ 0  │
│ 1 │ 1 │ 0  │ 0  │ 0  │ 1  │
└───┴───┴────┴────┴────┴────┘
```

### 5️⃣ Codificatore di Parità 🔢

**Funzione:** Aggiungi bit di parità per rilevare errori.

```
PARITÀ PARI (Even Parity):
Aggiungere bit pari se numero 1 è pari

Numero:    101 (due 1)
Parità:    0 (aggiungi 0 → due 1 rimangono pari)
Output:    1010

PARITÀ DISPARI (Odd Parity):
Aggiungere bit se numero 1 è dispari

Numero:    101 (due 1)
Parità:    1 (aggiungi 1 → tre 1 sono dispari)
Output:    1011
```

---

## 💻 Funzioni Python da Implementare

### Livello 1: Sommatori ✅

```python
def half_adder(a, b):
    """
    Sommatore mezzo (2 bit).

    Args:
        a, b (int): Bit da sommare (0 o 1)

    Returns:
        tuple: (sum_bit, carry)

    Formule:
        sum = a XOR b
        carry = a AND b

    Esempio:
        >>> half_adder(1, 1)
        (0, 1)  # 1+1=10 (sum=0, carry=1)
    """

def full_adder(a, b, carry_in):
    """
    Sommatore completo (2 bit + carry_in).

    Returns:
        tuple: (sum_bit, carry_out)

    Formule:
        sum = a XOR b XOR carry_in
        carry_out = (a AND b) OR (carry_in AND (a XOR b))
    """

def somma_n_bit(lista_a, lista_b, carry_in=0):
    """
    Somma due numeri di N bit usando catena Full Adder.

    Args:
        lista_a: [a3, a2, a1, a0] (MSB a sinistra)
        lista_b: [b3, b2, b1, b0]
        carry_in: Riporto iniziale (default 0)

    Returns:
        tuple: (carry_out, somma)
               somma = [s3, s2, s1, s0]

    Esempio:
        >>> somma_n_bit([0,1,0,1], [0,0,1,1])  # 5 + 3
        (0, [1,0,0,0])  # Risultato = 8 (01000)
    """
```

### Livello 2: Multiplexer 🔀

```python
def mux_2to1(i0, i1, sel):
    """
    Multiplexer 2:1.

    Args:
        i0, i1 (int): Input dati
        sel (int): Bit di selezione (0 o 1)

    Returns:
        int: i0 se sel=0, i1 se sel=1

    Esempio:
        >>> mux_2to1(5, 10, 0)
        5
        >>> mux_2to1(5, 10, 1)
        10
    """

def mux_4to1(i0, i1, i2, i3, sel1, sel0):
    """
    Multiplexer 4:1.

    Args:
        i0, i1, i2, i3: 4 input
        sel1, sel0: 2 bit di selezione

    Returns:
        Output selezionato
    """

def mux_8to1(inputs_list, sel2, sel1, sel0):
    """
    Multiplexer 8:1.

    Args:
        inputs_list: [i0, i1, ..., i7] (8 input)
        sel2, sel1, sel0: 3 bit di selezione

    Returns:
        Input selezionato
    """
```

### Livello 3: Decoder 🔓

```python
def decoder_2to4(a, b):
    """
    Decoder 2-to-4.

    Args:
        a, b: 2 bit di input

    Returns:
        tuple: (y0, y1, y2, y3)
               Solo uno è 1, gli altri 0

    Tabella:
        ab → y0 y1 y2 y3
        00 → 1  0  0  0
        01 → 0  1  0  0
        10 → 0  0  1  0
        11 → 0  0  0  1
    """

def decoder_3to8(a, b, c):
    """
    Decoder 3-to-8 (8 linee di output).

    Returns:
        tuple: (y0, y1, ..., y7)
    """

def decoder_with_enable(a, b, enable):
    """
    Decoder con enable. Output attivo solo se enable=1.

    Returns:
        tuple: (y0, y1, y2, y3)
               Se enable=0, tutti 0
    """
```

### Livello 4: Codificatori e Parità 🔢

```python
def calcola_parità_pari(bits):
    """
    Calcola bit di parità pari.

    Args:
        bits (list): Lista di bit [b0, b1, ...]

    Returns:
        int: Bit di parità (0 o 1)

    Parità PARI: numero totale di 1 (incluso parità) deve essere PARI
    Se numero di 1 è dispari, parità=1 (aggiungi 1)
    Se numero di 1 è pari, parità=0 (non aggiungi)

    Esempio:
        >>> calcola_parità_pari([1, 0, 1])  # 2 uno (pari)
        0  # Non aggiungi
        >>> calcola_parità_pari([1, 0, 0])  # 1 uno (dispari)
        1  # Aggiungi 1
    """

def calcola_parità_dispari(bits):
    """
    Calcola bit di parità dispari.

    Parità DISPARI: numero totale di 1 deve essere DISPARI
    """

def encoder_4to2(y3, y2, y1, y0):
    """
    Encoder 4-to-2: inverso del decoder.

    Args:
        y3, y2, y1, y0: 4 linee di input

    Returns:
        tuple: (a, b) numero della linea attiva

    Solo una linea può essere attiva.
    Se y2=1 → (a,b) = (1,0)
    """

def rilevatore_errore_parità(data_bits, parity_bit, tipo='pari'):
    """
    Rileva se c'è errore usando parità.

    Args:
        data_bits: Dati ricevuti
        parity_bit: Bit di parità ricevuto
        tipo: 'pari' o 'dispari'

    Returns:
        bool: True se errore rilevato, False se OK
    """
```

### Livello 5: Classe CircuitoCombinatorio 🎯

```python
class CircuitoCombinatorio:
    """
    Rappresenta un circuito combinatorio generico.

    Attributi:
        nome (str): Nome circuito (es: 'Full Adder')
        n_ingressi (int): Numero ingressi
        n_uscite (int): Numero uscite
        tabella_verita (list): Tabella completa
    """

    def __init__(self, nome, n_ingressi, n_uscite, tabella=None):
        """
        Inizializza circuito.

        Args:
            nome: Nome descrittivo
            n_ingressi: Numero ingressi
            n_uscite: Numero uscite
            tabella: Tabella di verità (opzionale)
        """

    def valuta(self, *inputs):
        """
        Calcola output dato input.

        Returns:
            Output (int, tuple, o list dipende da n_uscite)
        """

    def genera_tabella_verita(self, funzione):
        """
        Genera tabella di verità automaticamente.

        Args:
            funzione: Funzione che implementa circuito

        Returns:
            list: Tabella di verità completa
        """

    def stampa_tabella(self):
        """Stampa tabella formattata ASCII art."""

    def valida_input(self, *inputs):
        """Verifica che input siano validi (0 o 1)."""

    def visualizza_ascii_art(self):
        """Disegna circuito in ASCII art."""
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### Sommatore per Calcolo Potenza 🔢

```python
# Calcolare 5 + 3 in binario con Full Adder
#   0101  (5)
# + 0011  (3)
# ------
#   1000  (8)

a = [0, 1, 0, 1]
b = [0, 0, 1, 1]
carry_out, risultato = somma_n_bit(a, b)
print(f"{a} + {b} = {risultato}")  # [1, 0, 0, 0] = 8
```

### Selezione Canale WiFi 📶

```python
# WiFi: 14 canali, selezionare con decoder
canale = 5  # Canale 5 (binario: 00101)
a = (canale >> 2) & 1  # Bit 2
b = (canale >> 1) & 1  # Bit 1
c = canale & 1         # Bit 0

y0, y1, y2, y3, y4, y5, y6, y7 = decoder_3to8(a, b, c)
print(f"Canale {canale} attivo")
```

### Controllo Errori di Trasmissione ✓

```python
# Trasmettere 101 con bit di parità
dati = [1, 0, 1]
parity = calcola_parità_pari(dati)  # 1 (numero dispari di 1)
pacchetto = dati + [parity]  # [1, 0, 1, 1]

# In ricezione:
dati_ricevuti = [1, 0, 1, 1]
errore = rilevatore_errore_parità(
    dati_ricevuti[:-1],
    dati_ricevuti[-1],
    'pari'
)
print(f"Errore rilevato: {errore}")  # False (OK)
```

### Multiplexer per Commutazione Segnali 🔄

```python
# Selezionare quale antenna trasmettere
segnale_antenna1 = 1.2  # Voltaggio antenna 1
segnale_antenna2 = 0.8  # Voltaggio antenna 2
segnale_antenna3 = 1.0  # Voltaggio antenna 3
segnale_antenna4 = 0.5  # Voltaggio antenna 4

antenna_selezionata = 2  # Codificato come bit
sel1 = (antenna_selezionata >> 1) & 1
sel0 = antenna_selezionata & 1

uscita = mux_4to1(
    segnale_antenna1, segnale_antenna2,
    segnale_antenna3, segnale_antenna4,
    sel1, sel0
)
print(f"Antenna {antenna_selezionata}: {uscita} V")
```

---

## 🧪 Test Cases (8-10 casi)

```python
# TEST 1: Half Adder
assert half_adder(0, 0) == (0, 0)
assert half_adder(1, 1) == (0, 1)
print("✓ Half Adder")

# TEST 2: Full Adder
assert full_adder(0, 0, 0) == (0, 0)
assert full_adder(1, 1, 1) == (1, 1)  # 1+1+1=11
assert full_adder(1, 0, 1) == (0, 1)  # 1+0+1=10
print("✓ Full Adder")

# TEST 3: Somma 4-bit
carry, somma = somma_n_bit([0,1,0,1], [0,0,1,1])  # 5+3
assert somma == [1,0,0,0] and carry == 0  # 8
print("✓ Somma 4-bit")

# TEST 4: Mux 2-to-1
assert mux_2to1(5, 10, 0) == 5
assert mux_2to1(5, 10, 1) == 10
print("✓ Mux 2-to-1")

# TEST 5: Mux 4-to-1
assert mux_4to1(1, 2, 3, 4, 0, 0) == 1  # sel=00
assert mux_4to1(1, 2, 3, 4, 1, 0) == 3  # sel=10
print("✓ Mux 4-to-1")

# TEST 6: Decoder 2-to-4
y0, y1, y2, y3 = decoder_2to4(0, 0)
assert (y0, y1, y2, y3) == (1, 0, 0, 0)
y0, y1, y2, y3 = decoder_2to4(1, 1)
assert (y0, y1, y2, y3) == (0, 0, 0, 1)
print("✓ Decoder 2-to-4")

# TEST 7: Parità Pari
assert calcola_parità_pari([0, 0, 0]) == 0  # 0 uno (pari)
assert calcola_parità_pari([1, 0, 0]) == 1  # 1 uno (dispari)
assert calcola_parità_pari([1, 1, 0]) == 0  # 2 uno (pari)
print("✓ Parità Pari")

# TEST 8: Parità Dispari
assert calcola_parità_dispari([0, 0, 0]) == 1  # 0 uno (pari)
assert calcola_parità_dispari([1, 0, 0]) == 0  # 1 uno (dispari)
print("✓ Parità Dispari")

# TEST 9: Encoder 4-to-2
assert encoder_4to2(0, 0, 1, 0) == (0, 1)  # y2=1
assert encoder_4to2(1, 0, 0, 0) == (1, 1)  # y3=1
print("✓ Encoder 4-to-2")

# TEST 10: Classe CircuitoCombinatorio
circuito = CircuitoCombinatorio('Half Adder', 2, 2)
assert circuito.valuta(1, 1) == (0, 1)
tabella = circuito.genera_tabella_verita(half_adder)
assert len(tabella) == 4  # 2² righe
print("✓ Classe CircuitoCombinatorio")
```

---

## 🛠️ Step Implementazione (7-10 passaggi)

### STEP 1: Setup e Half Adder ✅
- [ ] Creare file `soluzione.py`
- [ ] Implementare `half_adder()`
- [ ] Testare con 4 combinazioni

```python
def half_adder(a, b):
    if a not in [0, 1] or b not in [0, 1]:
        raise ValueError("Input deve essere 0 o 1")
    sum_bit = a ^ b      # XOR
    carry = a & b        # AND
    return (sum_bit, carry)
```

### STEP 2: Full Adder 🔄
- [ ] Implementare `full_adder()`
- [ ] Formula: sum = a XOR b XOR carry_in
- [ ] Carry_out = (a AND b) OR (carry_in AND (a XOR b))
- [ ] Testare con 8 combinazioni

### STEP 3: Somma N-bit ⚙️
- [ ] Implementare `somma_n_bit()` usando catena Full Adder
- [ ] Iterare su bit da destra a sinistra (LSB → MSB)
- [ ] Gestire carry tra stadi
- [ ] Testare somme: 5+3=8, 7+7=14, 0+15=15

### STEP 4: Multiplexer 🔀
- [ ] Implementare `mux_2to1()`, `mux_4to1()`, `mux_8to1()`
- [ ] Usare shifter di bit per decodificare select
- [ ] Testare con vari input

```python
def mux_4to1(i0, i1, i2, i3, sel1, sel0):
    sel = (sel1 << 1) | sel0  # Convertire 2 bit in numero
    inputs = [i0, i1, i2, i3]
    return inputs[sel]
```

### STEP 5: Decoder 🔓
- [ ] Implementare `decoder_2to4()`, `decoder_3to8()`
- [ ] Generare output tuple con soli 0 e 1
- [ ] Testare tutte le combinazioni

### STEP 6: Parità e Encoding 🔢
- [ ] Implementare `calcola_parità_pari()` e `calcola_parità_dispari()`
- [ ] Contare numero di 1 negli input
- [ ] Implementare `encoder_4to2()`
- [ ] Implementare `rilevatore_errore_parità()`

### STEP 7: Classe CircuitoCombinatorio 🎯
- [ ] Creare classe con __init__, valuta()
- [ ] Implementare `genera_tabella_verita()`
- [ ] Implementare `stampa_tabella()` formattata

### STEP 8: ASCII Art Visualizzazione 📊
- [ ] Creare funzione per disegnare circuito
- [ ] Mostrare ingressi, uscite, logica
- [ ] Includere tabella di verità

### STEP 9: Test Completo ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare edge cases
- [ ] Testare gestione errori

### STEP 10: Documentazione 📚
- [ ] Aggiungere docstring complete
- [ ] Creare file `esempi.py` con casi reali
- [ ] Documentare assunzioni

---

## 💡 Trucchi Python & TLC 🎯

### Trucchi Python 🐍

1. **Operatori bitwise veloci:**
   ```python
   # XOR veloce
   risultato = a ^ b

   # AND veloce
   risultato = a & b

   # OR veloce
   risultato = a | b

   # NOT veloce (attenzione: complemento a 2)
   risultato = ~a  # NOT puro
   risultato = 1 - a  # Inverso per bit (0/1)
   ```

2. **Shift per selezione bit:**
   ```python
   sel = (sel1 << 1) | sel0  # Combinare 2 bit in numero
   # sel1=1, sel0=0 → sel = (1<<1) | 0 = 2 | 0 = 2

   bit = (numero >> posizione) & 1  # Leggere bit a posizione
   # numero=5=0b101, posizione=2 → (5>>2)&1 = 1
   ```

3. **Loop su liste di bit:**
   ```python
   for i, bit in enumerate([1, 0, 1, 1]):
       if bit == 1:
           print(f"Bit {i} attivo")
   ```

4. **Generare tutte le combinazioni:**
   ```python
   from itertools import product

   for combo in product([0, 1], repeat=3):  # 2³=8 combinazioni
       a, b, c = combo
       print(a, b, c)
   ```

5. **Validare 0/1 veloce:**
   ```python
   if not all(bit in [0, 1] for bit in [a, b, c]):
       raise ValueError("...")
   ```

### Trucchi TLC 📡

1. **Catena di Full Adder:**
   ```
   Visione corretta:
   ┌─────────────┬─────────────┬─────────────┬─────────────┐
   │   FA (bit3) │   FA (bit2) │   FA (bit1) │   FA (bit0) │
   │  carry      │  carry      │  carry      │  carry      │
   │    out──────→in carry───→in carry───→in carry───→in=0 │
   └─────────────┴─────────────┴─────────────┴─────────────┘

   Il carry fluisce da destra a sinistra!
   ```

2. **Decoder attiva solo una linea:**
   ```
   Input 2-bit → esattamente 1 output = 1, altri = 0
   Sempre 2^N output per N bit
   ```

3. **Multiplexer seleziona input:**
   ```
   Inverso del Decoder
   Input: quale selezionare (numero)
   Output: quel valore
   ```

4. **Parità per rilevare errori:**
   ```
   Pari:   numero totale 1 (incluso parity bit) PARI
   Dispari: numero totale 1 (incluso parity bit) DISPARI

   Rileva 1 errore (numero 1 cambia da pari↔dispari)
   Non rileva 2 errori (numero 1 rimane pari/dispari)
   ```

5. **Dimensione circuito cresce esponenzialmente:**
   ```
   N ingressi → 2^N combinazioni in tabella
   3 ingressi → 8 righe
   4 ingressi → 16 righe
   5 ingressi → 32 righe ← Già complesso!
   ```

---

## ⚠️ Errori Comuni (Fisici + Codice) 🐛

### Errori Fisici 📉

1. **Dimenticare il carry tra stadi**
   ```
   ❌ Usare Half Adder per ogni bit
      (perde il carry!)
   ✅ Usare Full Adder con catena di carry
   ```

2. **Decoder vs Encoder confusi**
   ```
   ❌ Decoder: Input → quale output attivare
   ❌ Encoder: quale input attivo → numero
   (Inversi!)
   ```

3. **Parità sbagliata**
   ```
   ❌ Parità pari = "numero 1 è pari"
   ✅ Parità pari = "numero totale 1 (incluso parità) PARI"

   Se 101 (2 uno), parità_pari = 0
   Se 1010 (2 uno), numero totale = 2 (pari!) ✓
   ```

4. **Ordine bit sbagliato (MSB vs LSB)**
   ```
   MSB = Most Significant Bit (bit più a sinistra)
   LSB = Least Significant Bit (bit più a destra)

   5 = [0, 1, 0, 1]  dove [MSB=0, ..., LSB=1]
   ```

### Errori di Codice 💻

1. **Sommatore che ignora carry_out**
   ```python
   ❌ def somma_n_bit(a, b):
        # Ritorna solo somma, perde overflow
        return somma

   ✅ def somma_n_bit(a, b):
        # Ritorna carry_out e somma
        return (carry_out, somma)
   ```

2. **Decoder che ritorna numero invece di tuple**
   ```python
   ❌ def decoder_2to4(a, b):
        linea = (a << 1) | b
        return linea  # Sbagliato!

   ✅ def decoder_2to4(a, b):
        y0 = 1 if (a==0 and b==0) else 0
        y1 = 1 if (a==0 and b==1) else 0
        # ...
        return (y0, y1, y2, y3)
   ```

3. **Multiplexer con selezione sbagliata**
   ```python
   ❌ inputs = [i0, i1, i2, i3]
        # sel1 sel0 → indice
        # 00 → 0 ✓
        # 01 → 1 ✓
        # 10 → 2 ✓
        # 11 → 3 ✓
      return inputs[sel]  # OK se codificato bene

   ✅ sel = (sel1 << 1) | sel0  # Correggere se necessario
   ```

4. **Parità non conteggia il bit di parità**
   ```python
   ❌ def calcola_parità_pari(bits):
        # Conta solo input, non il risultato
        numero_uno = sum(bits)
        return numero_uno % 2

      # Ma il BIT DI PARITÀ è parte della somma totale!

   ✅ # Inversione semplice:
      numero_uno = sum(bits)
      # Se pari, parità=0; se dispari, parità=1
      return numero_uno % 2

      # Dopo aggiunta di parità:
      # numero_totale = numero_uno + 1 (se parità=1)
      # numero_totale deve essere PARI
   ```

5. **Indice sbagliato su liste**
   ```python
   ❌ somma = [s3, s2, s1, s0]
      print(somma[0])  # Stampa s3 (MSB)

   ✅ Ricordare che Python usa indici 0-based
      somma[0] è il PRIMO elemento (MSB)
      somma[3] è l'ULTIMO elemento (LSB)
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Comparatore 4-bit ⭐

```python
def comparatore_4bit(a3, a2, a1, a0, b3, b2, b1, b0):
    """
    Compara due numeri di 4 bit.

    Returns:
        (a_minore, a_uguale, a_maggiore)

    Logica:
    - Confronta MSB prima
    - Se MSB diversi, determina risultato
    - Se MSB uguali, confronta bit successivo
    """
```

### Sfida 2: Generatore Parità Programmabile ⭐

```python
def aggiungi_parità(dati, tipo='pari'):
    """
    Aggiunge bit di parità a dati.

    Args:
        dati: Lista di bit
        tipo: 'pari' o 'dispari'

    Returns:
        dati + [parità_bit]
    """
```

### Sfida 3: Conversione Binario ↔ Altro ⭐⭐

```python
def convertitore_base(numero, da_base, a_base):
    """
    Converte numero tra basi diverse.

    Basi supportate: 2 (binario), 8 (ottale), 10 (decimale), 16 (esadecimale)

    Interno: sempre attraverso binario
    """
```

### Sfida 4: Simulatore Sommatore Visuale ⭐⭐

```python
def simula_somma_visuale(a, b):
    """
    Mostra passo-passo la somma di due numeri.

    Output:
        ```
        Somma: 0101 + 0011 = ?

        Bit 0: 1 + 1 = 10 (sum=0, carry=1)
        Bit 1: 0 + 1 + 1 = 10 (sum=0, carry=1)
        Bit 2: 1 + 0 + 1 = 10 (sum=0, carry=1)
        Bit 3: 0 + 0 + 1 = 1 (sum=1, carry=0)

        Risultato: 1000
        ```
    """
```

### Sfida 5: Costruttore Circuito Automatico ⭐⭐⭐

```python
def crea_sommatore_n_bit(n):
    """
    Crea oggetto CircuitoCombinatorio per sommatore N-bit.

    Automazione:
    - N ingressi: [a0, ..., a_{n-1}, b0, ..., b_{n-1}]
    - N+1 uscite: [carry_out, s0, ..., s_{n-1}]
    - Genera tabella di verità automatica (2^(2N) righe!)

    Nota: N > 4 diventa computazionalmente pesante
    """
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione Python
- [Bitwise operators](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)
- [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product)

### TLC - Circuiti Combinatori
- [Wikipedia: Adder (electronics)](https://en.wikipedia.org/wiki/Adder_(electronics))
- [Wikipedia: Multiplexer](https://en.wikipedia.org/wiki/Multiplexer)
- [Wikipedia: Decoder (digital)](https://en.wikipedia.org/wiki/Decoder)
- [Parity check](https://en.wikipedia.org/wiki/Parity_bit)

### Simulatori Online
- [Logic.ly](https://logic.ly/) - Disegna circuiti interattivi
- [CircuitVerse](https://circuitverse.org/) - Simulazione circuiti digitali
- [All About Circuits](https://www.allaboutcircuits.com/) - Tutorials dettagliati

### Letture Consigliate
1. Hambley, "Electronics" (Cap 10-12)
2. Katz & Borriello, "Contemporary Logic Design"
3. Patterson & Hennessy, "Computer Organization and Design"

---

## 🎯 Preparazione Esercizi Successivi 🔮

Questo esercizio prepara:

1. **ES09 - Simulatore Circuiti Web** 💻
   - Disegnare circuiti visualmente
   - Simulare circuiti combinatori in HTML5 Canvas

2. **Informatica - Progettazione CPU** 💾
   - ALU (Arithmetic Logic Unit)
   - Datapath e control unit

3. **Telecomunicazioni Avanzate**
   - Codificatori di canale (channel encoder)
   - Rilevamento e correzione errori (FEC)

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi circuiti fondamentali (HA, FA, Mux, Dec)
[ ] Comprendi tabelle di verità
[ ] Conosci formula Full Adder
[ ] Capisci concatenamento carry

IMPLEMENTAZIONE:
[ ] Step 1: Half Adder
[ ] Step 2: Full Adder
[ ] Step 3: Somma N-bit con catena
[ ] Step 4: Multiplexer 2-1, 4-1, 8-1
[ ] Step 5: Decoder 2-to-4, 3-to-8
[ ] Step 6: Parità, Encoder, Controllo errori
[ ] Step 7: Classe CircuitoCombinatorio
[ ] Step 8: Visualizzazione ASCII
[ ] Step 9: Test (almeno 10)

VALIDAZIONE:
[ ] Tutti i test passano
[ ] Funzioni hanno docstring
[ ] Somma N-bit funziona correttamente
[ ] Decoder attiva solo una linea
[ ] Parità rileva errori

BONUS:
[ ] 1-2 sfide bonus completate
[ ] File esempi.py con somme, decoder, mux
[ ] Visualizzazione circuito ASCII art
```

---

## 🎓 Conclusione

Hai imparato i **circuiti combinatori fondamentali** che sono il cuore dell'elaborazione digitale. Un processore moderno è composto da milioni di questi circuiti combinati insieme!

Dalla somma di numeri al routing di segnali, tutto si basa su questi principi semplici di logica booleana.

**Prossimo step:** ES09 - Simulatore Circuiti Web (visualizzare questi circuiti interattivamente!) 💻

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS
