# ES07 - Porte Logiche 🔧

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐⭐ INTERMEDIO |
| **Durata Stimata** | 3-4 ore |
| **Linguaggio** | Python 3.8+ |
| **Prerequisiti** | ES01-ES06 completati, Algebra booleana base |
| **Argomento TLC** | Elaborazione Digitale: Porte Logiche e Algebra Booleana |

---

## 🎓 Concetti Fondamentali

### Bit e Segnali Digitali 🔢

Un **bit** (Binary Digit) è l'unità minima di informazione digitale:

```
Bit = 2 stati possibili:
    0 (FALSE, LOW, OFF)  ← Assenza di segnale
    1 (TRUE, HIGH, ON)   ← Presenza di segnale
```

**Rappresentazione in circuiti:**

```
Logica POSITIVA (standard):
    0 → 0V (GND, Ground)
    1 → 5V (VCC, Alimentazione)

Logica NEGATIVA (raro):
    0 → 5V
    1 → 0V

Segnale digitale nel tempo:
    V
    5│   ┌─┐   ┌─┐
    │   │ │   │ │
    0│   │ └───┘ └─   (bit: 1, 0, 1, 1, 0)
      └──────────────
```

**Applicazioni in TLC:**
- Trasmissione dati (ethernet, WiFi)
- Cellulari (4G, 5G)
- Memoria computer (RAM, SSD)
- Codifica segnali audio/video

---

### Algebra Booleana 🧮

L'**algebra booleana** è matematica con 2 soli valori: **TRUE/FALSE** oppure **1/0**.

**Operazioni fondamentali:**

```
1. AND (e logico)
   Risultato = 1 solo se ENTRAMBI gli input sono 1
   Simbolo: & oppure ·

2. OR (o logico)
   Risultato = 1 se ALMENO UNO degli input è 1
   Simbolo: | oppure +

3. NOT (negazione)
   Inverte il valore: 0→1, 1→0
   Simbolo: ¯ (barra sopra)

4. NAND (NOT AND)
   Opposto di AND

5. NOR (NOT OR)
   Opposto di OR

6. XOR (OR esclusivo)
   Risultato = 1 se input sono DIVERSI
   Simbolo: ⊕

7. XNOR (equivalenza)
   Risultato = 1 se input sono UGUALI
```

---

### Porte Logiche Fondamentali 🚪

Una **porta logica** è un circuito che implementa un'operazione booleana:

#### 1️⃣ Porta AND

```
    A ──┐
        ├─ Y = A AND B
    B ──┤ (Y=1 solo se A=1 E B=1)
        │

Simbolo:        Tabella di Verità:
      ┌─────┐   A  B  Y
    A─┤ &   │   0  0  0
      │     ├─Y  0  1  0
    B─┤     │   1  0  0
      └─────┘   1  1  1
```

#### 2️⃣ Porta OR

```
    A ──┐
        ├─ Y = A OR B
    B ──┤ (Y=1 se A=1 O B=1)
        │

Tabella di Verità:
  A  B  Y
  0  0  0
  0  1  1
  1  0  1
  1  1  1
```

#### 3️⃣ Porta NOT

```
    A ────Y = NOT A
        (Y = opposto di A)

Tabella di Verità:
  A  Y
  0  1
  1  0
```

#### 4️⃣ Porta NAND

```
    A ──┐
        ├─ Y = NOT(A AND B)
    B ──┤

Tabella di Verità:
  A  B  Y
  0  0  1
  0  1  1
  1  0  1
  1  1  0  ← Unica differenza da AND
```

#### 5️⃣ Porta NOR

```
    A ──┐
        ├─ Y = NOT(A OR B)
    B ──┤

Tabella di Verità:
  A  B  Y
  0  0  1  ← Unica differenza da OR
  0  1  0
  1  0  0
  1  1  0
```

#### 6️⃣ Porta XOR (OR Esclusivo)

```
    A ──┐
        ├─ Y = A XOR B
    B ──┤ (Y=1 se A≠B)

Tabella di Verità:
  A  B  Y
  0  0  0
  0  1  1  ← Diversi
  1  0  1  ← Diversi
  1  1  0
```

#### 7️⃣ Porta XNOR (Equivalenza)

```
    A ──┐
        ├─ Y = A XNOR B
    B ──┤ (Y=1 se A=B)

Tabella di Verità:
  A  B  Y
  0  0  1  ← Uguali
  0  1  0
  1  0  0
  1  1  1  ← Uguali
```

---

### Tabelle di Verità 📋

Una **tabella di verità** mostra tutti i risultati possibili per ogni combinazione di input:

```
Porta con N ingressi:
- 2^N righe (combinazioni)
- 1 colonna output

Esempio: 2 ingressi (A, B)
→ 2² = 4 righe

Esempio: 3 ingressi (A, B, C)
→ 2³ = 8 righe
```

---

## 💻 Funzioni Python da Implementare

### Livello 1: Porte Basilari ✅

```python
def and_gate(a, b):
    """
    Porta AND - Output 1 solo se entrambi input sono 1.

    Args:
        a (int): Input A (0 o 1)
        b (int): Input B (0 o 1)

    Returns:
        int: Risultato (0 o 1)

    Tabella:
        A  B  Y
        0  0  0
        0  1  0
        1  0  0
        1  1  1

    Esempio:
        >>> and_gate(1, 1)
        1
        >>> and_gate(1, 0)
        0
    """

def or_gate(a, b):
    """Porta OR - Output 1 se almeno un input è 1."""

def not_gate(a):
    """Porta NOT - Inverte input (0→1, 1→0)."""

def nand_gate(a, b):
    """Porta NAND - NOT(AND)."""

def nor_gate(a, b):
    """Porta NOR - NOT(OR)."""

def xor_gate(a, b):
    """Porta XOR - Output 1 se input diversi."""

def xnor_gate(a, b):
    """Porta XNOR - Output 1 se input uguali."""
```

### Livello 2: Classe PortaLogica 🎯

```python
class PortaLogica:
    """
    Rappresenta una porta logica generica.

    Attributi:
        nome (str): Nome porta (AND, OR, NOT, etc)
        n_ingressi (int): Numero ingressi (1 o 2)
        tabella_verita (list): Lista di tuple (input, output)
    """

    def __init__(self, nome, n_ingressi=2):
        """
        Inizializza porta logica.

        Args:
            nome (str): 'AND', 'OR', 'NOT', 'NAND', 'NOR', 'XOR', 'XNOR'
            n_ingressi (int): 1 per NOT, 2 per altre
        """

    def valuta(self, *inputs):
        """
        Calcola output della porta.

        Args:
            *inputs: Valori input (1 o 2 a seconda porta)

        Returns:
            int: Output della porta (0 o 1)
        """

    def genera_tabella_verita(self):
        """
        Genera e ritorna tabella di verità.

        Returns:
            list: Lista di dict {'input_a': ..., 'input_b': ..., 'output': ...}
        """

    def stampa_tabella(self):
        """Stampa tabella di verità in formato leggibile."""

    def __repr__(self):
        """Rappresentazione stringa: 'Porta AND (2 ingressi)'"""
```

### Livello 3: Circuiti Combinatori Semplici 🔌

```python
def half_adder(a, b):
    """
    Half Adder: somma 2 bit.

    Returns:
        tuple: (sum_bit, carry_bit)
               sum = a XOR b
               carry = a AND b

    Esempio:
        >>> half_adder(0, 1)
        (1, 0)  # 0 + 1 = 1 (no riporto)
        >>> half_adder(1, 1)
        (0, 1)  # 1 + 1 = 10 (riporto 1)
    """

def full_adder(a, b, carry_in):
    """
    Full Adder: somma 2 bit + riporto in ingresso.

    Args:
        a, b: Bit da sommare
        carry_in: Riporto da stadio precedente

    Returns:
        tuple: (sum_bit, carry_out)
    """

def multiplexer_2to1(a, b, select):
    """
    Multiplexer 2:1 - Sceglie tra 2 input.

    Args:
        a, b: Input dati
        select: Bit di selezione (0→a, 1→b)

    Returns:
        int: Input selezionato
    """

def multiplexer_4to1(a, b, c, d, select):
    """
    Multiplexer 4:1 - Sceglie tra 4 input.

    Args:
        select: 2 bit di selezione (00, 01, 10, 11)
    """

def decoder_2to4(a, b):
    """
    Decoder 2-to-4: attiva 1 di 4 output basato su input.

    Args:
        a, b: Input bit (00, 01, 10, 11)

    Returns:
        tuple: (y0, y1, y2, y3) - Solo uno è 1
    """
```

### Livello 4: Verifica e Visualizzazione 📊

```python
def valida_tabella_verita(tabella, porta_nome):
    """
    Verifica se tabella è corretta per quella porta.

    Returns:
        (bool, list): (è_valida, errori)
    """

def confronta_porte(porta1, porta2):
    """
    Confronta due porte: stesse tabelle di verità?

    Returns:
        bool: True se identiche
    """

def stampa_tabella_verita_formattata(porta):
    """
    Stampa tabella in formato bello ASCII art.

    Output:
        ┌─────┬─────┬────┐
        │  A  │  B  │ AND│
        ├─────┼─────┼────┤
        │  0  │  0  │ 0  │
        │  0  │  1  │ 0  │
        │  1  │  0  │ 0  │
        │  1  │  1  │ 1  │
        └─────┴─────┴────┘
    """
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### Decoder (Selezione Canale) 📻

```python
# Decodificare numero canale WiFi
def seleziona_canale_wifi(bit_canale_0, bit_canale_1):
    """
    WiFi 2.4 GHz ha 14 canali (numerati 1-14).
    Decodificare con 4 bit (16 possibili valori).
    """
    y0, y1, y2, y3 = decoder_2to4(bit_canale_0, bit_canale_1)
    return [y0, y1, y2, y3]
```

### Multiplexer (Commutazione Segnali) 🔄

```python
# Selezionare quale antenna trasmettere
def seleziona_antenna(segnale1, segnale2, segnale3, segnale4, numero_antenna):
    """
    Multiplexer 4:1 seleziona quale antenna trasmettere.
    numero_antenna: 00=1, 01=2, 10=3, 11=4
    """
```

### Comparatore (Controllo Errori) ✓

```python
# Verificare se due bit ricevuti sono uguali
def verifica_parità(bit1, bit2):
    """
    XNOR: ritorna 1 se bit sono uguali (no errore).
    """
    return xnor_gate(bit1, bit2)
```

### Sommatore Binario 🔢

```python
# Sommare numeri in binario
def somma_binaria_4bit(a3, a2, a1, a0, b3, b2, b1, b0):
    """
    Somma due numeri di 4 bit usando Full Adder.
    Ritorna 5 bit: (carry_finale, s3, s2, s1, s0)
    """
```

---

## 🧪 Test Cases (8-10 casi)

```python
# TEST 1: Porta AND
assert and_gate(0, 0) == 0
assert and_gate(0, 1) == 0
assert and_gate(1, 0) == 0
assert and_gate(1, 1) == 1
print("✓ Porta AND")

# TEST 2: Porta OR
assert or_gate(0, 0) == 0
assert or_gate(0, 1) == 1
assert or_gate(1, 0) == 1
assert or_gate(1, 1) == 1
print("✓ Porta OR")

# TEST 3: Porta NOT
assert not_gate(0) == 1
assert not_gate(1) == 0
print("✓ Porta NOT")

# TEST 4: Porta XOR
assert xor_gate(0, 0) == 0
assert xor_gate(0, 1) == 1
assert xor_gate(1, 0) == 1
assert xor_gate(1, 1) == 0
print("✓ Porta XOR")

# TEST 5: Porta XNOR
assert xnor_gate(0, 0) == 1
assert xnor_gate(0, 1) == 0
assert xnor_gate(1, 0) == 0
assert xnor_gate(1, 1) == 1
print("✓ Porta XNOR")

# TEST 6: Half Adder
assert half_adder(0, 0) == (0, 0)  # 0+0=0, no carry
assert half_adder(0, 1) == (1, 0)  # 0+1=1, no carry
assert half_adder(1, 0) == (1, 0)  # 1+0=1, no carry
assert half_adder(1, 1) == (0, 1)  # 1+1=10 (carry 1)
print("✓ Half Adder")

# TEST 7: Full Adder
assert full_adder(0, 0, 0) == (0, 0)
assert full_adder(1, 1, 1) == (1, 1)  # 1+1+1=11
assert full_adder(0, 1, 1) == (0, 1)  # 0+1+1=10
print("✓ Full Adder")

# TEST 8: Decoder 2-to-4
y0, y1, y2, y3 = decoder_2to4(0, 0)
assert (y0, y1, y2, y3) == (1, 0, 0, 0)  # Input 00 → attiva y0
y0, y1, y2, y3 = decoder_2to4(1, 0)
assert (y0, y1, y2, y3) == (0, 1, 0, 0)  # Input 10 → attiva y1
print("✓ Decoder 2-to-4")

# TEST 9: Multiplexer 2-to-1
assert multiplexer_2to1(5, 10, 0) == 5   # select=0 → a
assert multiplexer_2to1(5, 10, 1) == 10  # select=1 → b
print("✓ Multiplexer 2-to-1")

# TEST 10: Classe PortaLogica
porta_and = PortaLogica('AND')
assert porta_and.valuta(1, 1) == 1
tabella = porta_and.genera_tabella_verita()
assert len(tabella) == 4  # 2² righe
print("✓ Classe PortaLogica")
```

---

## 🛠️ Step Implementazione (7-10 passaggi)

### STEP 1: Setup e Funzioni Basilari ✅
- [ ] Creare file `soluzione.py`
- [ ] Implementare le 7 porte basilari (AND, OR, NOT, NAND, NOR, XOR, XNOR)
- [ ] Testare con 2-3 esempi

```python
def and_gate(a, b):
    return 1 if (a == 1 and b == 1) else 0

def or_gate(a, b):
    return 1 if (a == 1 or b == 1) else 0

def not_gate(a):
    return 1 if a == 0 else 0
```

### STEP 2: Validazione Input 🔍
- [ ] Aggiungere controlli che a, b siano 0 o 1
- [ ] Lanciare ValueError se non validi
- [ ] Testare con input invalido

```python
def and_gate(a, b):
    if a not in [0, 1] or b not in [0, 1]:
        raise ValueError("Input deve essere 0 o 1")
    return 1 if (a == 1 and b == 1) else 0
```

### STEP 3: Implementare Porte Composite ⚡
- [ ] Implementare NAND, NOR usando porte basilari
- [ ] Implementare XOR, XNOR
- [ ] Testare che risultati siano corretti

```python
def nand_gate(a, b):
    return not_gate(and_gate(a, b))

def xor_gate(a, b):
    # XOR = (a OR b) AND (NOT(a AND b))
    return and_gate(or_gate(a, b), nand_gate(a, b))
```

### STEP 4: Tabelle di Verità Automatiche 📋
- [ ] Implementare `genera_tabella_verita()` per 2 ingressi
- [ ] Testare che generi 4 righe
- [ ] Testare con più porte

```python
def genera_tabella_verita(porta_func):
    """
    Data una funzione porta, genera tabella.
    """
    tabella = []
    for a in [0, 1]:
        for b in [0, 1]:
            output = porta_func(a, b)
            tabella.append({'a': a, 'b': b, 'output': output})
    return tabella
```

### STEP 5: Classe PortaLogica 🎯
- [ ] Implementare __init__, valuta(), genera_tabella_verita()
- [ ] Aggiungere stampa tabella formattata
- [ ] Testare con varie porte

### STEP 6: Circuiti Combinatori - Half Adder ⚙️
- [ ] Implementare Half Adder (somma 2 bit)
- [ ] Formula: sum = A XOR B, carry = A AND B
- [ ] Testare con 4 combinazioni

### STEP 7: Full Adder e Multiplexer 🔌
- [ ] Implementare Full Adder (somma + carry_in)
- [ ] Implementare Multiplexer 2:1 e 4:1
- [ ] Implementare Decoder 2-to-4
- [ ] Testare tutti

### STEP 8: Visualizzazione ASCII Art 📊
- [ ] Implementare `stampa_tabella_formattata()` con box drawing
- [ ] Output leggibile con bordi
- [ ] Testare con varia porte

### STEP 9: Test Completo ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare gestione eccezioni
- [ ] Testare edge cases

### STEP 10: Documentazione 📚
- [ ] Aggiungere docstring complete
- [ ] Creare file `esempi.py`
- [ ] Commentare trucchi booleani

---

## 💡 Trucchi Python & TLC 🎯

### Trucchi Python 🐍

1. **Operatori logici Python:**
   ```python
   # AND
   risultato = a and b
   risultato = int(a and b)  # Forza 0 o 1

   # OR
   risultato = a or b

   # NOT
   risultato = not a
   risultato = int(not a)  # Forza 0 o 1
   ```

2. **Operatori bitwise (per numeri):**
   ```python
   # AND bit a bit: &
   5 & 3 = 0b101 & 0b011 = 0b001 = 1

   # OR bit a bit: |
   5 | 3 = 0b101 | 0b011 = 0b111 = 7

   # XOR: ^
   5 ^ 3 = 0b101 ^ 0b011 = 0b110 = 6

   # NOT: ~
   ~5 = NOT 0b101 = ... (attenzione: complimento a 2)
   ```

3. **Ternario condizionale:**
   ```python
   # if x else y
   risultato = 1 if (a and b) else 0
   ```

4. **Generare tabella con loop annidati:**
   ```python
   for a in [0, 1]:
       for b in [0, 1]:
           y = and_gate(a, b)
           print(f"{a} AND {b} = {y}")
   ```

5. **Dictionary per mappare funzioni:**
   ```python
   PORTE = {
       'AND': and_gate,
       'OR': or_gate,
       'NOT': not_gate
   }
   risultato = PORTE['AND'](1, 1)  # 1
   ```

### Trucchi TLC 📡

1. **De Morgan's Laws:**
   ```
   NOT(A AND B) = NOT(A) OR NOT(B)
   NOT(A OR B) = NOT(A) AND NOT(B)

   Utile per semplificare circuiti!
   ```

2. **XOR è "somma modulo 2":**
   ```
   XOR = somma binaria senza riporto
   0 + 0 = 0 (no carry)
   0 + 1 = 1 (no carry)
   1 + 0 = 1 (no carry)
   1 + 1 = 0 (carry 1)  ← Solo questo è diverso!
   ```

3. **Half Adder vs Full Adder:**
   ```
   Half Adder:   somma 2 bit
   Full Adder:   somma 2 bit + riporto in ingresso
   Full = Half + logica per carry_in
   ```

4. **Decoder vs Multiplexer:**
   ```
   Decoder:      Input → seleziona quale output attivare
   Mux:          Input → seleziona quale input leggere
   Opposti!
   ```

5. **Numeri binari con Python:**
   ```python
   0b1010 = 10 in decimale
   bin(5) = '0b101'
   int('1010', 2) = 10
   ```

---

## ⚠️ Errori Comuni (Fisici + Codice) 🐛

### Errori Fisici 📉

1. **Confondere AND e OR**
   ```
   ❌ AND output 1 se "almeno uno" → SBAGLIATO!
   ✅ AND output 1 se "ENTRAMBI"

   ❌ OR output 1 se "uno solo" → SBAGLIATO!
   ✅ OR output 1 se "almeno uno"
   ```

2. **Dimenticare che NOT ha 1 solo ingresso**
   ```
   ❌ not_gate(1, 0)  → 2 ingressi!
   ✅ not_gate(1)     → 1 ingresso
   ```

3. **Confondere le porte inverse**
   ```
   ❌ NAND = NOR → SBAGLIATO!
   ✅ NAND = NOT(AND)
   ✅ NOR = NOT(OR)
   ```

4. **Interpretare tabelle male**
   ```
   ❌ XOR: "1 e 1 = 1" → SBAGLIATO!
   ✅ XOR: "1 e 1 = 0" (diversi → 0)
   ```

### Errori di Codice 💻

1. **Input non validato**
   ```python
   ❌ def and_gate(a, b):
        return a and b  # Crash con input strano!

   ✅ def and_gate(a, b):
        if a not in [0, 1] or b not in [0, 1]:
            raise ValueError(...)
        return 1 if (a == 1 and b == 1) else 0
   ```

2. **Logica booleana confusa in Python**
   ```python
   ❌ a and b  # Ritorna a o b, non 0/1!
      print(a and b)  # Stampa: True oppure False

   ✅ int(a and b)  # Forza a 0 o 1
      1 if (a and b) else 0
   ```

3. **Tabella di verità incompleta**
   ```python
   ❌ for a in [0, 1]:
        for b in [0, 1]:
            print(a, b)  # Stampa solo input!

   ✅ for a in [0, 1]:
        for b in [0, 1]:
            y = porta(a, b)
            print(f"{a} {b} {y}")  # Include output
   ```

4. **Decoder con output sbagliato**
   ```python
   ❌ def decoder_2to4(a, b):
        if a == 0 and b == 0:
            return (1, 0, 0, 0)  # Memoria: y0, y1, y2, y3
        else:
            return (0, 0, 0, 0)  # Dove vanno altri?

   ✅ Implementare TUTTE le 4 combinazioni
   ```

5. **Half Adder: dimenticare il carry**
   ```python
   ❌ def half_adder(a, b):
        return (xor_gate(a, b))  # MANCA il carry!

   ✅ def half_adder(a, b):
        sum_bit = xor_gate(a, b)
        carry = and_gate(a, b)
        return (sum_bit, carry)
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Circuito Sommatore 4-bit ⭐

Creare funzione che somma due numeri di 4 bit:

```python
def somma_4bit(a3, a2, a1, a0, b3, b2, b1, b0):
    """
    Somma due numeri 4-bit usando catena di Full Adder.

    Returns:
        tuple: (carry_out, s3, s2, s1, s0)

    Esempio:
        somma_4bit(0,1,0,1, 0,0,1,1)  # 5 + 3 = 8
        → (0, 1, 0, 0, 0)  # 01000 = 8
    """
```

### Sfida 2: Comparatore 2-bit ⭐

Implementare circuito che compara due numeri:

```python
def comparatore(a1, a0, b1, b0):
    """
    Ritorna:
        (a_minore_b, a_uguale_b, a_maggiore_b)

    Esempio:
        comparatore(0, 1, 0, 0)  # 1 vs 0
        → (0, 0, 1)  # 1 > 0
    """
```

### Sfida 3: Encoder Priorità ⭐⭐

```python
def encoder_4to2(y3, y2, y1, y0):
    """
    Encoder con priorità: trova il bit attivo più alto.

    Se più di uno attivo, priorità al più alto indice.

    Returns:
        (a, b): Numero della linea attiva in binario
    """
```

### Sfida 4: Simulatore Circuito Interattivo ⭐⭐

```python
def simulatore_interattivo():
    """
    Menu interattivo:
    1. Scegli porta (AND, OR, NOT, etc)
    2. Inserisci input
    3. Visualizza output e tabella
    4. Aggiungi più porte in cascata

    Stato: ricorda output porte precedenti per input prossime
    """
```

### Sfida 5: Verifica Equivalenza Circuiti ⭐⭐⭐

```python
def circuiti_equivalenti(circuito1, circuito2):
    """
    Verifica se due circuiti (liste di porte) sono equivalenti.

    circuito1 = [
        ('AND', 0, [0, 1]),      # Porta AND con input 0, 1
        ('NOT', 1, [OUTPUT_PORTA_1])
    ]

    Genera tabelle verità per entrambi e confronta.
    """
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione Python
- [Python boolean operators](https://docs.python.org/3/tutorial/datastructures.html)
- [Bitwise operators](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)

### TLC - Logica Digitale
- [Wikipedia: Logic gate](https://en.wikipedia.org/wiki/Logic_gate)
- [Wikipedia: Adder (electronics)](https://en.wikipedia.org/wiki/Adder_(electronics))
- [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra)

### Video Tutorial
- [Crash Course: Boolean Logic](https://www.youtube.com/watch?v=gI-qXk7XojA)
- [Logic Gates Explained](https://www.youtube.com/watch?v=gI-qXk7XojA)

### Simulatori Online
- [Logic.ly - Circuiti logici online](https://logic.ly/)
- [CircuitVerse - Simulatore circuiti](https://circuitverse.org/)

---

## 🎯 Preparazione Esercizi Successivi 🔮

Questo esercizio prepara:

1. **ES08 - Circuiti Combinatori** ⚙️
   - Sommatori, multiplexer, decoder
   - Combinazioni di porte logiche

2. **ES09 - Simulatore Circuiti Web** 💻
   - Visualizzare porte graficamente
   - Simulare circuiti in tempo reale

3. **Informatica - Architettura Computer** 💾
   - ALU (Arithmetic Logic Unit)
   - Processore

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi tabelle di verità
[ ] Capisci AND, OR, NOT, XOR
[ ] Conosci Half/Full Adder
[ ] Capisci Decoder/Mux

IMPLEMENTAZIONE:
[ ] Step 1: 7 porte basilari
[ ] Step 2: Validazione input
[ ] Step 3: Porte composite (NAND, NOR, XOR, XNOR)
[ ] Step 4: Tabelle di verità automatiche
[ ] Step 5: Classe PortaLogica
[ ] Step 6: Half Adder
[ ] Step 7: Full Adder + Mux + Decoder
[ ] Step 8: Visualizzazione ASCII
[ ] Step 9: Test (almeno 10)

VALIDAZIONE:
[ ] Tutti i test passano
[ ] Funzioni hanno docstring
[ ] Eccezioni per input invalidi
[ ] Nessun crash

BONUS:
[ ] 1-2 sfide bonus completate
[ ] File esempi.py con casi reali
```

---

## 🎓 Conclusione

Hai imparato i **fondamenti della logica digitale** che sono il cuore dei computer e tutti i dispositivi digitali moderni. Una smartphone è milioni di porte logiche!

**Prossimo step:** ES08 - Circuiti Combinatori (combinazioni avanzate di porte) ⚙️

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS
