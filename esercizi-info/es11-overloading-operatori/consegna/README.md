# Es11: Overloading Operatori - Classe Frazione

## 📊 Informazioni Generali

**Livello:** 🔴 AVANZATO
**Durata stimata:** 6-7 ore
**Prerequisiti:** Es1-10 completati, metodi speciali, operatori

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Implementare** overloading operatori aritmetici avanzati
- ✅ **Gestire** operazioni con numeri razionali (frazioni)
- ✅ **Semplificare** automaticamente con MCD (Massimo Comun Divisore)
- ✅ **Implementare** operatori matematici (+, -, *, /)
- ✅ **Creare** operatori di comparazione con tolleranza
- ✅ **Gestire** eccezioni (divisione per zero)
- ✅ **Padroneggiare** le migliori pratiche di operator overloading

**Concetti fondamentali:**
- Numeratore e denominatore per frazioni
- MCD (Massimo Comun Divisore) per semplificazione
- Operatori aritmetici con __add__, __sub__, __mul__, __truediv__
- Operatori di comparazione con __eq__, __lt__, __gt__
- Rappresentazione con __str__ e __repr__
- Gestione di edge case (frazioni negative, divisione per zero)

---

## 📖 Descrizione

Una **frazione** (numero razionale) è rappresentata da:
- **Numeratore**: numero sopra la linea
- **Denominatore**: numero sotto la linea

Esempio: 3/4 = 0.75, 1/2 = 0.5, 5/10 = 1/2 (semplificata)

Questo esercizio crea una classe `Frazione` che:
- Rappresenta numeri razionali
- Supporta operazioni aritmetiche (+, -, *, /)
- Supporta comparazioni (==, <, >, <=, >=)
- **Semplifica automaticamente** usando MCD
- Gestisce errori (divisione per zero)
- Si stampa come "3/4" o "1/2" (semplificata)

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Frazione Base

**Definisci una classe `Frazione` con:**

1. **Attributi:**
   - `numeratore` (int) - numeratore
   - `denominatore` (int) - denominatore (non può essere 0)

2. **Metodi di Inizializzazione:**
   - `__init__(numeratore, denominatore)` - costruttore
   - **Semplificare automaticamente** (3/6 → 1/2)
   - Gestire segni: 3/-4 → -3/4, -3/-4 → 3/4
   - Solleva ValueError se denominatore == 0

### Parte 2: Operatori Aritmetici

**Implementa operazioni con frazioni:**

1. **`__add__(altra)`** - somma di frazioni
   - (1/2) + (1/3) = (5/6)

2. **`__sub__(altra)`** - sottrazione di frazioni
   - (3/4) - (1/4) = (1/2)

3. **`__mul__(altra)`** - moltiplicazione di frazioni
   - (1/2) * (3/4) = (3/8)

4. **`__truediv__(altra)`** - divisione di frazioni
   - (1/2) / (1/3) = (3/2)
   - Solleva ValueError se altra == 0

### Parte 3: Operatori di Comparazione

**Implementa comparazioni:**

1. **`__eq__(altra)`** - uguaglianza
   - (1/2) == (2/4) → True (entrambe semplificate)

2. **`__lt__(altra)`** - minore
   - (1/2) < (3/4) → True

3. **`__le__`, `__gt__`, `__ge__`** - altre comparazioni

### Parte 4: Rappresentazione

1. **`__str__()`** - output leggibile
   - (1/2) → "1/2"

2. **`__repr__()`** - output tecnico
   - (1/2) → "Frazione(1, 2)"

3. **`__float__()`** - conversione a float
   - float(Frazione(1, 2)) → 0.5

4. **`__int__()`** - conversione a int (arrotonda)
   - int(Frazione(3, 2)) → 1 (arrotondamento)

### Parte 5: Metodi Utili

1. **`semplifica()`** - semplifica la frazione
2. **`inverti()`** - ritorna l'inverso (1/2 → 2/1)
3. **`valore_float()`** - calcola il valore decimale
4. **`è_intera()`** - True se denominatore == 1
5. **`mcd(a, b)`** - metodo statico per calcolare MCD

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ FUNZIONE AUSILIARIA ============

def mcd(a, b):
    """Massimo Comun Divisore - Algoritmo di Euclide"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


# ============ DEFINIZIONE CLASSE ============

class Frazione:
    """Un numero razionale (frazione) con semplificazione automatica"""

    def __init__(self, numeratore, denominatore):
        if denominatore == 0:
            raise ValueError("Il denominatore non può essere zero!")

        # Semplificare automaticamente
        divisore = mcd(abs(numeratore), abs(denominatore))
        self.numeratore = numeratore // divisore
        self.denominatore = denominatore // divisore

        # Normalizzare il segno (sempre nel numeratore)
        if self.denominatore < 0:
            self.numeratore = -self.numeratore
            self.denominatore = -self.denominatore

    # ===== RAPPRESENTAZIONE =====

    def __str__(self):
        """Rappresentazione leggibile"""
        if self.denominatore == 1:
            return str(self.numeratore)  # 3/1 → "3"
        return f"{self.numeratore}/{self.denominatore}"

    def __repr__(self):
        """Rappresentazione tecnica"""
        return f"Frazione({self.numeratore}, {self.denominatore})"

    # ===== CONVERSIONI =====

    def __float__(self):
        """Converti a float"""
        return self.numeratore / self.denominatore

    def __int__(self):
        """Converti a int (con arrotondamento)"""
        return round(self.numeratore / self.denominatore)

    # ===== OPERATORI ARITMETICI =====

    def __add__(self, altra):
        """Somma di frazioni: a/b + c/d = (ad + bc) / bd"""
        if not isinstance(altra, Frazione):
            return NotImplemented

        numeratore = self.numeratore * altra.denominatore + self.denominatore * altra.numeratore
        denominatore = self.denominatore * altra.denominatore
        return Frazione(numeratore, denominatore)

    def __sub__(self, altra):
        """Sottrazione: a/b - c/d = (ad - bc) / bd"""
        if not isinstance(altra, Frazione):
            return NotImplemented

        numeratore = self.numeratore * altra.denominatore - self.denominatore * altra.numeratore
        denominatore = self.denominatore * altra.denominatore
        return Frazione(numeratore, denominatore)

    def __mul__(self, altra):
        """Moltiplicazione: (a/b) * (c/d) = (ac) / (bd)"""
        if not isinstance(altra, Frazione):
            return NotImplemented

        return Frazione(
            self.numeratore * altra.numeratore,
            self.denominatore * altra.denominatore
        )

    def __rmul__(self, altra):
        """Moltiplicazione da sinistra"""
        return self.__mul__(altra)

    def __truediv__(self, altra):
        """Divisione: (a/b) / (c/d) = (a/b) * (d/c) = (ad) / (bc)"""
        if not isinstance(altra, Frazione):
            return NotImplemented

        if altra.numeratore == 0:
            raise ValueError("Non puoi dividere per una frazione zero!")

        # Diviso un frazione = moltiplicato per il suo inverso
        return Frazione(
            self.numeratore * altra.denominatore,
            self.denominatore * altra.numeratore
        )

    def __neg__(self):
        """Negazione: -(a/b) = -a/b"""
        return Frazione(-self.numeratore, self.denominatore)

    def __pos__(self):
        """Positivo: +(a/b) = a/b"""
        return Frazione(self.numeratore, self.denominatore)

    def __abs__(self):
        """Valore assoluto"""
        return Frazione(abs(self.numeratore), self.denominatore)

    # ===== COMPARAZIONI =====

    def __eq__(self, altra):
        """Uguaglianza (frazioni semplificate)"""
        if not isinstance(altra, Frazione):
            return NotImplemented
        # Entrambe semplificate, quindi basta confrontare num e denom
        return self.numeratore == altra.numeratore and self.denominatore == altra.denominatore

    def __ne__(self, altra):
        """Disuguaglianza"""
        if not isinstance(altra, Frazione):
            return NotImplemented
        return not self.__eq__(altra)

    def __lt__(self, altra):
        """Minore: a/b < c/d ⟺ ad < bc"""
        if not isinstance(altra, Frazione):
            return NotImplemented
        return self.numeratore * altra.denominatore < self.denominatore * altra.numeratore

    def __le__(self, altra):
        """Minore o uguale"""
        if not isinstance(altra, Frazione):
            return NotImplemented
        return self.__eq__(altra) or self.__lt__(altra)

    def __gt__(self, altra):
        """Maggiore"""
        if not isinstance(altra, Frazione):
            return NotImplemented
        return not self.__le__(altra)

    def __ge__(self, altra):
        """Maggiore o uguale"""
        if not isinstance(altra, Frazione):
            return NotImplemented
        return not self.__lt__(altra)

    # ===== METODI UTILI =====

    def semplifica(self):
        """Semplifica la frazione (già fatto in __init__)"""
        return self

    def inverti(self):
        """Ritorna l'inverso (1/2 → 2/1)"""
        if self.numeratore == 0:
            raise ValueError("Non puoi invertire zero!")
        return Frazione(self.denominatore, self.numeratore)

    def valore_float(self):
        """Valore decimale"""
        return float(self)

    def è_intera(self):
        """True se è un numero intero (denominatore == 1)"""
        return self.denominatore == 1

    @staticmethod
    def mcd(a, b):
        """Massimo Comun Divisore (Algoritmo di Euclide)"""
        a, b = abs(a), abs(b)
        while b != 0:
            a, b = b, a % b
        return a


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    print("=== CREAZIONE E RAPPRESENTAZIONE ===")
    f1 = Frazione(3, 4)
    f2 = Frazione(1, 2)
    f3 = Frazione(6, 9)  # Semplificata a 2/3

    print(f"f1 = {f1}")        # 3/4
    print(f"f2 = {f2}")        # 1/2
    print(f"f3 = {f3}")        # 2/3 (semplificata da 6/9)
    print(f"repr(f1) = {repr(f1)}")

    print("\n=== CONVERSIONI ===")
    print(f"float(f1) = {float(f1)}")  # 0.75
    print(f"int(f1) = {int(f1)}")      # 1 (arrotondato)

    print("\n=== OPERATORI ARITMETICI ===")
    f4 = f1 + f2
    print(f"{f1} + {f2} = {f4}")  # 3/4 + 1/2 = 5/4

    f5 = f1 - f2
    print(f"{f1} - {f2} = {f5}")  # 3/4 - 1/2 = 1/4

    f6 = f1 * f2
    print(f"{f1} * {f2} = {f6}")  # 3/4 * 1/2 = 3/8

    f7 = f1 / f2
    print(f"{f1} / {f2} = {f7}")  # 3/4 / 1/2 = 3/2

    print("\n=== NEGAZIONE E VALORE ASSOLUTO ===")
    f_neg = -f1
    print(f"-{f1} = {f_neg}")     # -3/4

    f_abs = abs(Frazione(-3, 4))
    print(f"abs(-3/4) = {f_abs}") # 3/4

    print("\n=== COMPARAZIONI ===")
    f8 = Frazione(2, 4)  # Semplificata a 1/2
    print(f"{f2} == {f8}: {f2 == f8}")  # True (entrambe 1/2)
    print(f"{f1} > {f2}: {f1 > f2}")    # True (3/4 > 1/2)
    print(f"{f1} < {f2}: {f1 < f2}")    # False

    print("\n=== ORDINAMENTO ===")
    frazioni = [Frazione(3, 4), Frazione(1, 2), Frazione(5, 6), Frazione(1, 3)]
    frazioni_ordinate = sorted(frazioni)
    print(f"Ordinato: {[str(f) for f in frazioni_ordinate]}")

    print("\n=== METODI UTILI ===")
    f = Frazione(3, 4)
    print(f"{f}.inverti() = {f.inverti()}")       # 4/3
    print(f"{f}.valore_float() = {f.valore_float()}")  # 0.75
    print(f"{f}.è_intera() = {f.è_intera()}")    # False
    print(f"{Frazione(5, 1)}.è_intera() = {Frazione(5, 1).è_intera()}")  # True

    print("\n=== GESTIONE ERRORI ===")
    try:
        f_zero = Frazione(0, 5) / Frazione(0, 1)
    except ValueError as e:
        print(f"Errore atteso: {e}")

    try:
        f_error = Frazione(5, 0)
    except ValueError as e:
        print(f"Errore atteso: {e}")

    print("\n=== OPERAZIONI COMPLESSE ===")
    # (1/2 + 1/3) * (3/4 - 1/6)
    risultato = (Frazione(1, 2) + Frazione(1, 3)) * (Frazione(3, 4) - Frazione(1, 6))
    print(f"(1/2 + 1/3) * (3/4 - 1/6) = {risultato}")
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione e semplificazione
```python
f1 = Frazione(6, 9)
assert f1.numeratore == 2
assert f1.denominatore == 3
assert str(f1) == "2/3"
print("✓ Test 1 passato")
```

### Test 2: Normalizzazione segni
```python
f1 = Frazione(3, -4)
assert f1.numeratore == -3
assert f1.denominatore == 4

f2 = Frazione(-3, -4)
assert f2.numeratore == 3
assert f2.denominatore == 4
print("✓ Test 2 passato")
```

### Test 3: Operatore __add__
```python
f1 = Frazione(1, 2)
f2 = Frazione(1, 3)
f3 = f1 + f2
assert f3.numeratore == 5
assert f3.denominatore == 6
print("✓ Test 3 passato")
```

### Test 4: Operatore __sub__
```python
f1 = Frazione(3, 4)
f2 = Frazione(1, 4)
f3 = f1 - f2
assert f3.numeratore == 1
assert f3.denominatore == 2
print("✓ Test 4 passato")
```

### Test 5: Operatore __mul__
```python
f1 = Frazione(2, 3)
f2 = Frazione(3, 4)
f3 = f1 * f2
assert f3.numeratore == 1
assert f3.denominatore == 2  # (2*3)/(3*4) = 6/12 → 1/2
print("✓ Test 5 passato")
```

### Test 6: Operatore __truediv__
```python
f1 = Frazione(1, 2)
f2 = Frazione(1, 3)
f3 = f1 / f2
assert f3.numeratore == 3
assert f3.denominatore == 2  # (1/2) / (1/3) = (1*3)/(2*1) = 3/2
print("✓ Test 6 passato")
```

### Test 7: Comparazioni
```python
f1 = Frazione(1, 2)
f2 = Frazione(2, 4)
f3 = Frazione(3, 4)

assert f1 == f2  # Entrambe semplificate a 1/2
assert f1 < f3
assert f3 > f1
assert f1 <= f2
print("✓ Test 7 passato")
```

### Test 8: Conversioni
```python
f = Frazione(3, 4)
assert float(f) == 0.75
assert int(f) == 1  # Arrotondato
print("✓ Test 8 passato")
```

### Test 9: Negazione e valore assoluto
```python
f = Frazione(3, 4)
f_neg = -f
assert f_neg.numeratore == -3
assert f_neg.denominatore == 4

f_abs = abs(f_neg)
assert f_abs.numeratore == 3
print("✓ Test 9 passato")
```

### Test 10: Inversi
```python
f = Frazione(3, 4)
f_inv = f.inverti()
assert f_inv.numeratore == 4
assert f_inv.denominatore == 3
print("✓ Test 10 passato")
```

### Test 11: Frazione intera
```python
f1 = Frazione(5, 1)
f2 = Frazione(3, 4)

assert f1.è_intera() == True
assert f2.è_intera() == False
print("✓ Test 11 passato")
```

### Test 12: Divisione per zero
```python
f1 = Frazione(1, 2)
f2 = Frazione(0, 1)

try:
    f1 / f2
    assert False
except ValueError:
    pass
print("✓ Test 12 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Funzione MCD
```python
def mcd(a, b):
    """Massimo Comun Divisore"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

# Test:
assert mcd(12, 8) == 4
assert mcd(7, 3) == 1
```

### Passo 2: Costruttore con semplificazione
```python
class Frazione:
    def __init__(self, numeratore, denominatore):
        if denominatore == 0:
            raise ValueError("Denominatore non può essere zero!")

        # Semplificare
        divisore = mcd(abs(numeratore), abs(denominatore))
        self.numeratore = numeratore // divisore
        self.denominatore = denominatore // divisore

        # Normalizzare segni
        if self.denominatore < 0:
            self.numeratore = -self.numeratore
            self.denominatore = -self.denominatore
```

### Passo 3: Rappresentazione
```python
def __str__(self):
    if self.denominatore == 1:
        return str(self.numeratore)
    return f"{self.numeratore}/{self.denominatore}"

def __repr__(self):
    return f"Frazione({self.numeratore}, {self.denominatore})"
```

### Passo 4: Operatori aritmetici
```python
def __add__(self, altra):
    if not isinstance(altra, Frazione):
        return NotImplemented
    num = self.numeratore * altra.denominatore + self.denominatore * altra.numeratore
    den = self.denominatore * altra.denominatore
    return Frazione(num, den)

def __mul__(self, altra):
    if not isinstance(altra, Frazione):
        return NotImplemented
    return Frazione(self.numeratore * altra.numeratore,
                    self.denominatore * altra.denominatore)
```

### Passo 5: Divisione
```python
def __truediv__(self, altra):
    if not isinstance(altra, Frazione):
        return NotImplemented
    if altra.numeratore == 0:
        raise ValueError("Non puoi dividere per zero!")
    return Frazione(self.numeratore * altra.denominatore,
                    self.denominatore * altra.numeratore)
```

### Passo 6: Comparazioni
```python
def __eq__(self, altra):
    if not isinstance(altra, Frazione):
        return NotImplemented
    return (self.numeratore == altra.numeratore and
            self.denominatore == altra.denominatore)

def __lt__(self, altra):
    if not isinstance(altra, Frazione):
        return NotImplemented
    return self.numeratore * altra.denominatore < self.denominatore * altra.numeratore
```

### Passo 7: Negazione e conversioni
```python
def __neg__(self):
    return Frazione(-self.numeratore, self.denominatore)

def __float__(self):
    return self.numeratore / self.denominatore

def __int__(self):
    return round(self.numeratore / self.denominatore)
```

### Passo 8: Metodi utili
```python
def inverti(self):
    if self.numeratore == 0:
        raise ValueError("Non puoi invertire zero!")
    return Frazione(self.denominatore, self.numeratore)

def è_intera(self):
    return self.denominatore == 1
```

---

## 💡 Trucchi e Best Practices

### ✅ Semplificare in __init__
```python
# BUONO - semplifica automaticamente
def __init__(self, numeratore, denominatore):
    divisore = mcd(abs(numeratore), abs(denominatore))
    self.numeratore = numeratore // divisore
    self.denominatore = denominatore // divisore

# Allora Frazione(6, 9) == Frazione(2, 3) automaticamente
```

### ✅ Normalizzare segni
```python
# BUONO - segno sempre nel numeratore
if self.denominatore < 0:
    self.numeratore = -self.numeratore
    self.denominatore = -self.denominatore

# Allora Frazione(3, -4) diventa Frazione(-3, 4)
```

### ✅ Verificare tipo in operatori
```python
# BUONO - verifica tipo e ritorna NotImplemented
def __add__(self, altra):
    if not isinstance(altra, Frazione):
        return NotImplemented
    # Continua...
```

### ✅ Comparazioni accurate
```python
# BUONO - moltiplicazione incrociata
def __lt__(self, altra):
    return self.numeratore * altra.denominatore < self.denominatore * altra.numeratore

# CATTIVO - divisione può avere errori di float
def __lt__(self, altra):
    return float(self) < float(altra)  # Impreciso!
```

### ✅ __str__ per numeri interi
```python
# BUONO - 5/1 si stampa come "5"
def __str__(self):
    if self.denominatore == 1:
        return str(self.numeratore)
    return f"{self.numeratore}/{self.denominatore}"
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare MCD
```python
# SBAGLIATO - non semplifica
f1 = Frazione(6, 9)
f2 = Frazione(2, 3)
print(f1 == f2)  # False! (diversi dopo semplificazione)

# GIUSTO - implementa MCD in __init__
```

### ❌ Errore 2: Non normalizzare segni
```python
# SBAGLIATO - segni inconsistenti
f1 = Frazione(3, -4)  # Rimane 3/-4
f2 = Frazione(-3, 4)  # Diventa -3/4
print(f1 == f2)  # False! (ma dovrebbe essere True)

# GIUSTO - normalizza in __init__
```

### ❌ Errore 3: Usare float in comparazioni
```python
# SBAGLIATO - impreciso
def __eq__(self, altra):
    return float(self) == float(altra)  # 0.1 + 0.2 != 0.3!

# GIUSTO - moltiplicazione incrociata
def __eq__(self, altra):
    return self.numeratore == altra.numeratore and \
           self.denominatore == altra.denominatore
```

### ❌ Errore 4: Divisione per zero non controllata
```python
# SBAGLIATO - no check
f = Frazione(1, 2)
f / Frazione(0, 1)  # ZeroDivisionError!

# GIUSTO
def __truediv__(self, altra):
    if altra.numeratore == 0:
        raise ValueError("Divisione per zero!")
```

### ❌ Errore 5: Non invertire correttamente
```python
# SBAGLIATO - non controlla zero
def inverti(self):
    return Frazione(self.denominatore, self.numeratore)

# Frazione(0, 1).inverti() = Frazione(1, 0) → ValueError!

# GIUSTO
def inverti(self):
    if self.numeratore == 0:
        raise ValueError("Non puoi invertire zero!")
    return Frazione(self.denominatore, self.numeratore)
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Operatori di assegnamento
```python
class Frazione:
    def __iadd__(self, altra):
        """+="""
        risultato = self + altra
        self.numeratore = risultato.numeratore
        self.denominatore = risultato.denominatore
        return self

    def __isub__(self, altra):
        """-="""
        risultato = self - altra
        self.numeratore = risultato.numeratore
        self.denominatore = risultato.denominatore
        return self

# Uso:
f = Frazione(1, 2)
f += Frazione(1, 4)  # f diventa 3/4
```

### 🌟 Sfida 2: Operatori con numeri interi
```python
class Frazione:
    def __add__(self, altra):
        if isinstance(altra, int):
            altra = Frazione(altra, 1)
        if not isinstance(altra, Frazione):
            return NotImplemented
        # Continua...

# Uso:
f = Frazione(1, 2)
f + 2  # Frazione(1, 2) + Frazione(2, 1) = Frazione(5, 2)
```

### 🌟 Sfida 3: Somma di lista di frazioni
```python
def somma_frazioni(lista):
    """Somma una lista di frazioni"""
    if not lista:
        return Frazione(0, 1)
    risultato = lista[0]
    for f in lista[1:]:
        risultato = risultato + f
    return risultato

# Uso:
frazioni = [Frazione(1, 2), Frazione(1, 3), Frazione(1, 6)]
print(somma_frazioni(frazioni))  # 1
```

### 🌟 Sfida 4: MCD di lista e riduzione
```python
class Frazione:
    @staticmethod
    def riduzione_frazione(lista_frazioni):
        """Riduce frazioni a denominatore comune"""
        if not lista_frazioni:
            return []

        # Trova il denominatore comune
        denominatori = [f.denominatore for f in lista_frazioni]
        mcm = denominatori[0]
        for d in denominatori[1:]:
            mcm = mcm * d // Frazione.mcd(mcm, d)

        # Converte tutte le frazioni
        risultato = []
        for f in lista_frazioni:
            fattore = mcm // f.denominatore
            risultato.append(Frazione(f.numeratore * fattore, mcm))
        return risultato
```

### 🌟 Sfida 5: Iterazione e unpacking
```python
class Frazione:
    def __iter__(self):
        """Rendi la frazione iterabile"""
        return iter([self.numeratore, self.denominatore])

# Uso:
f = Frazione(3, 4)
num, den = f  # Unpacking!
print(num, den)  # 3 4

for valore in f:
    print(valore)  # Stampa 3, poi 4
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **MCD** | Massimo Comun Divisore | mcd(12, 8) = 4 |
| **Semplificazione** | Ridurre a forma minima | 6/9 → 2/3 |
| **Normalizzazione** | Segno sempre nel numeratore | 3/-4 → -3/4 |
| **Operazione** | Somma: (ad+bc)/(bd) | 1/2 + 1/3 = 5/6 |
| **Divisione** | (a/b)/(c/d) = (ad)/(bc) | (1/2)/(1/3) = 3/2 |
| **Comparazione** | ad < bc (no float) | 1/2 < 3/4 |
| **Inversione** | Swap numeratore/denominatore | (3/4).inverti() = 4/3 |

---

## 🔗 Link Utili

### Documentazione
- [fractions Module - Python Docs](https://docs.python.org/3/library/fractions.html)
- [Rational Numbers](https://en.wikipedia.org/wiki/Rational_number)
- [Euclidean Algorithm - MCD](https://en.wikipedia.org/wiki/Euclidean_algorithm)

### Tutorial
- [Real Python - Operator Overloading](https://realpython.com/operator-and-function-overloading-in-python/)
- [Data Model - Special Methods](https://docs.python.org/3/reference/datamodel.html)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Osserva come è implementato MCD
- Guarda la semplificazione in __init__
- Nota come sono implementate le operazioni aritmetiche
- Apprendi le migliori pratiche di operator overloading

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho implementato la funzione MCD (Algoritmo di Euclide)
- [ ] Ho semplificato automaticamente in __init__
- [ ] Ho normalizzato i segni (sempre nel numeratore)
- [ ] Ho implementato __str__ e __repr__
- [ ] Ho implementato __float__ e __int__
- [ ] Ho implementato __add__, __sub__, __mul__, __truediv__
- [ ] Ho implementato __neg__, __pos__, __abs__
- [ ] Ho implementato __eq__, __lt__, __le__, __gt__, __ge__
- [ ] Ho gestito la divisione per zero
- [ ] Ho implementato inverti() e è_intera()
- [ ] Ho testato con almeno 12 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai padroneggiato l'overloading degli operatori! 🎉🔢**

*"Le frazioni sono la base dei numeri razionali, e gli operatori sovraccaricati le rendono naturali e intuitive!"*
