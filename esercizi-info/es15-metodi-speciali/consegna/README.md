# Es10: Metodi Speciali (Dunder Methods) - Punti 2D

## 📊 Informazioni Generali

**Livello:** 🟡 INTERMEDIO
**Durata stimata:** 4-5 ore
**Prerequisiti:** Es1-9 completati, comprensione delle classi

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Usare** metodi speciali (dunder methods) con doppio underscore
- ✅ **Implementare** `__init__`, `__str__`, `__repr__`
- ✅ **Creare** operatori personalizzati (`__add__`, `__sub__`, `__mul__`)
- ✅ **Confrontare** oggetti (`__eq__`, `__lt__`, `__le__`)
- ✅ **Rappresentare** lunghezza e indici (`__len__`, `__getitem__`, `__setitem__`)
- ✅ **Rendere** le classi "simili a tipi nativi"
- ✅ **Usare** magia Python attraverso metodi speciali

**Concetti fondamentali:**
- Dunder methods = metodi con `__` prima e dopo
- `__init__` = costruttore (inizializzazione)
- `__str__` = rappresentazione leggibile
- `__repr__` = rappresentazione tecnica
- Operatori = metodi speciali (`+`, `-`, `*`, `==`, `<`, ecc.)
- Magic methods = rendono le classi "magiche" e intuitive

---

## 📖 Descrizione

Python ti permette di rendere le tue classi **intuitive come tipi nativi**. Quando scrivi:

```python
x = [1, 2, 3]
print(x)          # Chiama x.__str__()
len(x)            # Chiama x.__len__()
x[0]              # Chiama x.__getitem__(0)
x == [1, 2, 3]    # Chiama x.__eq__([1, 2, 3])
```

Puoi fare lo stesso con le tue classi! Questo esercizio crea una classe `Punto2D` che:
- Si stampa come "(x, y)"
- Supporta operazioni: `+`, `-`, `*`, `/`
- Supporta comparazioni: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Supporta `len()` e accesso per indice
- Si comporta come un tipo nativo

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Punto2D Base

**Definisci una classe `Punto2D` con:**

1. **Attributi:**
   - `x` (float) - coordinata x
   - `y` (float) - coordinata y

2. **Metodi speciali di rappresentazione:**
   - `__init__(x, y)` - costruttore
   - `__str__()` - ritorna "(x, y)" leggibile per print
   - `__repr__()` - ritorna "Punto2D(x, y)" per debugging
   - `__info__()` - ritorna info dettagliata

### Parte 2: Operatori Aritmetici

**Implementa operatori che restituiscono nuovi Punto2D:**

1. **`__add__(altro)`** - somma di due punti
   - `p1 + p2` → Punto2D(p1.x + p2.x, p1.y + p2.y)

2. **`__sub__(altro)`** - sottrazione di due punti
   - `p1 - p2` → Punto2D(p1.x - p2.x, p1.y - p2.y)

3. **`__mul__(scalare)`** - moltiplicazione per scalare
   - `p * 2` → Punto2D(p.x * 2, p.y * 2)
   - `2 * p` → (implementa `__rmul__`)

4. **`__truediv__(scalare)`** - divisione per scalare
   - `p / 2` → Punto2D(p.x / 2, p.y / 2)
   - Solleva ValueError se scalare == 0

5. **`__neg__()`** - negazione (opposto)
   - `-p` → Punto2D(-p.x, -p.y)

### Parte 3: Operatori di Comparazione

**Implementa comparazioni:**

1. **`__eq__(altro)`** - uguaglianza
   - `p1 == p2` → True se x e y uguali

2. **`__ne__(altro)`** - disuguaglianza (autogenerato da `!=`)

3. **`__lt__(altro)`** - minore (ordinamento per distanza da origine)
   - `p1 < p2` → True se distanza(p1) < distanza(p2)

4. **`__le__(altro)`** - minore o uguale
5. **`__gt__(altro)`** - maggiore
6. **`__ge__(altro)`** - maggiore o uguale

### Parte 4: Metodi Speciali di Accesso

**Implementa accesso simile a sequenze:**

1. **`__len__()`** - distanza da origine (arrotondata a int)
   - `len(p)` → √(x² + y²)

2. **`__getitem__(indice)`** - accesso per indice
   - `p[0]` → x
   - `p[1]` → y
   - Solleva IndexError per altri indici

3. **`__setitem__(indice, valore)`** - modifica per indice
   - `p[0] = 5` → modifica x
   - `p[1] = 10` → modifica y

### Parte 5: Metodi Utili

1. **`distanza()`** - distanza da origine
2. **`distanza_da(altro)`** - distanza da un altro punto
3. **`modulo()`** - alias per distanza
4. **`hash()`** - per uso in set/dict (implementa `__hash__`)

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSE ============

import math

class Punto2D:
    """Un punto in uno spazio 2D con metodi speciali"""

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # ===== RAPPRESENTAZIONE =====

    def __str__(self):
        """Rappresentazione per print - leggibile"""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Rappresentazione per debugging - tecnica"""
        return f"Punto2D({self.x}, {self.y})"

    # ===== OPERATORI ARITMETICI =====

    def __add__(self, altro):
        """Somma di due punti"""
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return Punto2D(self.x + altro.x, self.y + altro.y)

    def __sub__(self, altro):
        """Sottrazione di due punti"""
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return Punto2D(self.x - altro.x, self.y - altro.y)

    def __mul__(self, scalare):
        """Moltiplicazione per scalare"""
        if isinstance(scalare, Punto2D):
            return NotImplemented
        return Punto2D(self.x * scalare, self.y * scalare)

    def __rmul__(self, scalare):
        """Moltiplicazione da sinistra (scalare * punto)"""
        return self.__mul__(scalare)

    def __truediv__(self, scalare):
        """Divisione per scalare"""
        if scalare == 0:
            raise ValueError("Non puoi dividere per zero!")
        return Punto2D(self.x / scalare, self.y / scalare)

    def __neg__(self):
        """Negazione - opposto del punto"""
        return Punto2D(-self.x, -self.y)

    # ===== COMPARAZIONI =====

    def __eq__(self, altro):
        """Uguaglianza - punti sono uguali se x e y uguali"""
        if not isinstance(altro, Punto2D):
            return False
        return abs(self.x - altro.x) < 1e-9 and abs(self.y - altro.y) < 1e-9

    def __ne__(self, altro):
        """Disuguaglianza (Python genera da __eq__)"""
        return not self.__eq__(altro)

    def __lt__(self, altro):
        """Minore - basato su distanza da origine"""
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return self.distanza() < altro.distanza()

    def __le__(self, altro):
        """Minore o uguale"""
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return self.distanza() <= altro.distanza()

    def __gt__(self, altro):
        """Maggiore"""
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return self.distanza() > altro.distanza()

    def __ge__(self, altro):
        """Maggiore o uguale"""
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return self.distanza() >= altro.distanza()

    # ===== ACCESSO COME SEQUENZA =====

    def __len__(self):
        """Lunghezza - distanza da origine (arrotondata)"""
        return int(round(self.distanza()))

    def __getitem__(self, indice):
        """Accesso per indice"""
        if indice == 0:
            return self.x
        elif indice == 1:
            return self.y
        elif indice == -1:
            return self.y
        elif indice == -2:
            return self.x
        else:
            raise IndexError(f"Indice {indice} fuori range")

    def __setitem__(self, indice, valore):
        """Modifica per indice"""
        if indice == 0 or indice == -2:
            self.x = float(valore)
        elif indice == 1 or indice == -1:
            self.y = float(valore)
        else:
            raise IndexError(f"Indice {indice} fuori range")

    # ===== METODI UTILI =====

    def distanza(self):
        """Distanza da origine (0, 0)"""
        return math.sqrt(self.x**2 + self.y**2)

    def distanza_da(self, altro):
        """Distanza da un altro punto"""
        if not isinstance(altro, Punto2D):
            raise TypeError("Deve essere un Punto2D")
        dx = self.x - altro.x
        dy = self.y - altro.y
        return math.sqrt(dx**2 + dy**2)

    def modulo(self):
        """Alias per distanza da origine"""
        return self.distanza()

    def __hash__(self):
        """Hash per uso in set/dict"""
        return hash((round(self.x, 10), round(self.y, 10)))

    def __bool__(self):
        """Un punto è True se non è l'origine"""
        return self.x != 0 or self.y != 0


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    # Creare punti
    p1 = Punto2D(3, 4)
    p2 = Punto2D(1, 2)
    origine = Punto2D(0, 0)

    print("=== RAPPRESENTAZIONE ===")
    print(f"str(p1): {p1}")  # (3.0, 4.0)
    print(f"repr(p1): {repr(p1)}")  # Punto2D(3.0, 4.0)

    print("\n=== OPERATORI ARITMETICI ===")
    p3 = p1 + p2
    print(f"p1 + p2 = {p3}")  # (4.0, 6.0)

    p4 = p1 - p2
    print(f"p1 - p2 = {p4}")  # (2.0, 2.0)

    p5 = p1 * 2
    print(f"p1 * 2 = {p5}")  # (6.0, 8.0)

    p6 = 3 * p2
    print(f"3 * p2 = {p6}")  # (3.0, 6.0)

    p7 = p1 / 2
    print(f"p1 / 2 = {p7}")  # (1.5, 2.0)

    p8 = -p1
    print(f"-p1 = {p8}")  # (-3.0, -4.0)

    print("\n=== COMPARAZIONI ===")
    print(f"p1 == Punto2D(3, 4): {p1 == Punto2D(3, 4)}")  # True
    print(f"p1 != p2: {p1 != p2}")  # True

    # Ordinamento per distanza da origine
    punti = [Punto2D(5, 0), Punto2D(3, 4), Punto2D(1, 1), Punto2D(0, 10)]
    print(f"\nPunti ordinati per distanza:")
    for p in sorted(punti):
        print(f"  {p} - distanza: {p.distanza():.2f}")

    print("\n=== ACCESSO COME SEQUENZA ===")
    p = Punto2D(7, 9)
    print(f"p = {p}")
    print(f"len(p) = {len(p)}")  # Distanza da origine
    print(f"p[0] = {p[0]}")  # x = 7
    print(f"p[1] = {p[1]}")  # y = 9

    p[0] = 5
    print(f"Dopo p[0] = 5: {p}")  # (5.0, 9.0)

    print("\n=== DISTANZE =====")
    p1 = Punto2D(0, 0)
    p2 = Punto2D(3, 4)
    p3 = Punto2D(6, 8)

    print(f"p1: {p1} - distanza da origine: {p1.distanza():.2f}")
    print(f"p2: {p2} - distanza da origine: {p2.distanza():.2f}")
    print(f"p3: {p3} - distanza da p2: {p3.distanza_da(p2):.2f}")

    print("\n=== USO IN SET E DICT ===")
    punti_unici = {Punto2D(1, 2), Punto2D(1, 2), Punto2D(3, 4)}
    print(f"Punti unici: {len(punti_unici)}")  # 2 (uno duplicato)

    dizionario = {
        Punto2D(0, 0): "origine",
        Punto2D(1, 0): "asse x",
        Punto2D(0, 1): "asse y"
    }
    print(f"Dizionario: {dizionario}")

    # Output atteso:
    # === RAPPRESENTAZIONE ===
    # str(p1): (3.0, 4.0)
    # repr(p1): Punto2D(3.0, 4.0)
    # ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione e rappresentazione
```python
p = Punto2D(3, 4)
assert p.x == 3
assert p.y == 4
assert str(p) == "(3.0, 4.0)"
assert "Punto2D" in repr(p)
print("✓ Test 1 passato")
```

### Test 2: Operatore __add__
```python
p1 = Punto2D(1, 2)
p2 = Punto2D(3, 4)
p3 = p1 + p2
assert p3.x == 4
assert p3.y == 6
assert isinstance(p3, Punto2D)
print("✓ Test 2 passato")
```

### Test 3: Operatore __sub__
```python
p1 = Punto2D(5, 7)
p2 = Punto2D(2, 3)
p3 = p1 - p2
assert p3.x == 3
assert p3.y == 4
print("✓ Test 3 passato")
```

### Test 4: Operatore __mul__ e __rmul__
```python
p = Punto2D(2, 3)
p2 = p * 3
assert p2.x == 6
assert p2.y == 9

p3 = 2 * p
assert p3.x == 4
assert p3.y == 6
print("✓ Test 4 passato")
```

### Test 5: Operatore __truediv__
```python
p = Punto2D(6, 8)
p2 = p / 2
assert p2.x == 3
assert p2.y == 4

try:
    p / 0  # Deve sollevare ValueError
    assert False
except ValueError:
    pass
print("✓ Test 5 passato")
```

### Test 6: Operatore __neg__
```python
p = Punto2D(3, -4)
p_neg = -p
assert p_neg.x == -3
assert p_neg.y == 4
print("✓ Test 6 passato")
```

### Test 7: Operatore __eq__
```python
p1 = Punto2D(3, 4)
p2 = Punto2D(3, 4)
p3 = Punto2D(1, 2)

assert p1 == p2
assert not (p1 == p3)
assert p1 != p3
print("✓ Test 7 passato")
```

### Test 8: Operatori di comparazione
```python
p1 = Punto2D(1, 1)  # distanza = sqrt(2) ≈ 1.41
p2 = Punto2D(2, 0)  # distanza = 2
p3 = Punto2D(3, 4)  # distanza = 5

assert p1 < p2 < p3
assert p3 > p2 > p1
assert p1 <= p2 <= p3
print("✓ Test 8 passato")
```

### Test 9: Accesso per indice
```python
p = Punto2D(7, 9)
assert p[0] == 7
assert p[1] == 9
assert p[-1] == 9
assert p[-2] == 7

p[0] = 5
assert p.x == 5
p[1] = 10
assert p.y == 10

try:
    p[2]  # Deve sollevare IndexError
    assert False
except IndexError:
    pass
print("✓ Test 9 passato")
```

### Test 10: Distanza e len()
```python
p = Punto2D(3, 4)
assert p.distanza() == 5.0
assert len(p) == 5  # Arrotondato a int

p1 = Punto2D(0, 0)
p2 = Punto2D(3, 4)
distanza = p2.distanza_da(p1)
assert distanza == 5.0
print("✓ Test 10 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Costruttore e rappresentazione
```python
class Punto2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Punto2D({self.x}, {self.y})"
```

### Passo 2: Operatori aritmetici
```python
def __add__(self, altro):
    if not isinstance(altro, Punto2D):
        return NotImplemented
    return Punto2D(self.x + altro.x, self.y + altro.y)

def __sub__(self, altro):
    if not isinstance(altro, Punto2D):
        return NotImplemented
    return Punto2D(self.x - altro.x, self.y - altro.y)

def __mul__(self, scalare):
    if isinstance(scalare, Punto2D):
        return NotImplemented
    return Punto2D(self.x * scalare, self.y * scalare)

def __rmul__(self, scalare):
    return self.__mul__(scalare)
```

### Passo 3: Divisione e negazione
```python
def __truediv__(self, scalare):
    if scalare == 0:
        raise ValueError("Non puoi dividere per zero!")
    return Punto2D(self.x / scalare, self.y / scalare)

def __neg__(self):
    return Punto2D(-self.x, -self.y)
```

### Passo 4: Comparazioni
```python
def __eq__(self, altro):
    if not isinstance(altro, Punto2D):
        return False
    return abs(self.x - altro.x) < 1e-9 and abs(self.y - altro.y) < 1e-9

def __lt__(self, altro):
    if not isinstance(altro, Punto2D):
        return NotImplemented
    return self.distanza() < altro.distanza()

# Implementa __le__, __gt__, __ge__ similmente
```

### Passo 5: Accesso per indice
```python
def __len__(self):
    return int(round(self.distanza()))

def __getitem__(self, indice):
    if indice == 0 or indice == -2:
        return self.x
    elif indice == 1 or indice == -1:
        return self.y
    else:
        raise IndexError(f"Indice fuori range")

def __setitem__(self, indice, valore):
    if indice == 0 or indice == -2:
        self.x = float(valore)
    elif indice == 1 or indice == -1:
        self.y = float(valore)
    else:
        raise IndexError(f"Indice fuori range")
```

### Passo 6: Metodi di utilità
```python
import math

def distanza(self):
    return math.sqrt(self.x**2 + self.y**2)

def distanza_da(self, altro):
    if not isinstance(altro, Punto2D):
        raise TypeError("Deve essere un Punto2D")
    dx = self.x - altro.x
    dy = self.y - altro.y
    return math.sqrt(dx**2 + dy**2)
```

### Passo 7: Hash e bool
```python
def __hash__(self):
    return hash((round(self.x, 10), round(self.y, 10)))

def __bool__(self):
    return self.x != 0 or self.y != 0
```

### Passo 8: Testa tutto
```python
p1 = Punto2D(3, 4)
p2 = Punto2D(1, 2)
print(p1)
print(p1 + p2)
print(sorted([p2, p1]))
print(p1[0])
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa `NotImplemented` per operatori non supportati
```python
# BUONO - ritorna NotImplemented
def __add__(self, altro):
    if not isinstance(altro, Punto2D):
        return NotImplemented  # Python proverà altro.__radd__(self)
    return Punto2D(self.x + altro.x, self.y + altro.y)

# CATTIVO - solleva TypeError
def __add__(self, altro):
    if not isinstance(altro, Punto2D):
        raise TypeError("Deve essere un Punto2D")
```

### ✅ Implementa sia `__mul__` che `__rmul__`
```python
# BUONO - funziona sia p * 2 che 2 * p
def __mul__(self, scalare):
    return Punto2D(self.x * scalare, self.y * scalare)

def __rmul__(self, scalare):
    return self.__mul__(scalare)  # Delega a __mul__

# CATTIVO - solo p * 2 funziona
def __mul__(self, scalare):
    return Punto2D(self.x * scalare, self.y * scalare)
# 2 * p fallisce perché non c'è __rmul__
```

### ✅ Usa tolleranza per comparazioni di float
```python
# BUONO - tolleranza per imprecisioni
def __eq__(self, altro):
    return abs(self.x - altro.x) < 1e-9 and abs(self.y - altro.y) < 1e-9

# CATTIVO - float esatti non sono affidabili
def __eq__(self, altro):
    return self.x == altro.x and self.y == altro.y
```

### ✅ Implementa `__repr__` come codice Python
```python
# BUONO - è valido Python
def __repr__(self):
    return f"Punto2D({self.x}, {self.y})"
# eval(repr(p)) crea un nuovo punto uguale

# ACCETTABILE - solo descrittivo
def __repr__(self):
    return f"<Punto2D at {hex(id(self))}>"
```

### ✅ Gestisci IndexError in __getitem__
```python
# BUONO - solleva IndexError
def __getitem__(self, indice):
    if indice == 0:
        return self.x
    elif indice == 1:
        return self.y
    else:
        raise IndexError(f"Indice {indice} fuori range")

# CATTIVO - non gestisce indici invalidi
def __getitem__(self, indice):
    return [self.x, self.y][indice]  # Funziona ma poco controllato
```

### ✅ Usa `isinstance()` per validare tipi
```python
# BUONO - verifica esplicita
def __add__(self, altro):
    if not isinstance(altro, Punto2D):
        return NotImplemented

# CATTIVO - assume il tipo
def __add__(self, altro):
    return Punto2D(self.x + altro.x, self.y + altro.y)  # Crash se non è Punto2D
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare __rmul__
```python
# SBAGLIATO - solo p * 2 funziona
class Punto2D:
    def __mul__(self, scalare):
        return Punto2D(self.x * scalare, self.y * scalare)

p = Punto2D(1, 2)
p * 2      # Funziona
2 * p      # Fallisce! AttributeError: int non ha __mul__ per Punto2D
```

### ❌ Errore 2: Usare == invece di __eq__
```python
# SBAGLIATO - istanze diverse sono sempre diverse
p1 = Punto2D(3, 4)
p2 = Punto2D(3, 4)
print(p1 == p2)  # False! (senza __eq__)
print(p1 is p2)  # False (diverse istanze)

# GIUSTO - implementa __eq__
def __eq__(self, altro):
    return self.x == altro.x and self.y == altro.y
print(p1 == p2)  # True!
```

### ❌ Errore 3: Modificare self in operatori
```python
# SBAGLIATO - __add__ non deve modificare
def __add__(self, altro):
    self.x += altro.x  # Non modificare self!
    self.y += altro.y
    return self

# GIUSTO - crea un nuovo oggetto
def __add__(self, altro):
    return Punto2D(self.x + altro.x, self.y + altro.y)
```

### ❌ Errore 4: Confrontare float esatti
```python
# SBAGLIATO
def __eq__(self, altro):
    return self.x == altro.x  # 0.1 + 0.2 != 0.3!

# GIUSTO - tolleranza
def __eq__(self, altro):
    return abs(self.x - altro.x) < 1e-9
```

### ❌ Errore 5: __len__ ritorna float
```python
# SBAGLIATO - __len__ deve ritornare int
def __len__(self):
    return self.distanza()  # Float!

# GIUSTO
def __len__(self):
    return int(self.distanza())  # O arrotonda
```

### ❌ Errore 6: Non gestire None in comparazioni
```python
# SBAGLIATO - crash se confronti con None
def __lt__(self, altro):
    return self.distanza() < altro.distanza()  # AttributeError se altro è None

# GIUSTO - verifica il tipo
def __lt__(self, altro):
    if not isinstance(altro, Punto2D):
        return NotImplemented
    return self.distanza() < altro.distanza()
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Punto3D
```python
class Punto3D:
    """Estensione a 3D"""

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, altro):
        if not isinstance(altro, Punto3D):
            return NotImplemented
        return Punto3D(self.x + altro.x, self.y + altro.y, self.z + altro.z)

    def distanza(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def prodotto_scalare(self, altro):
        """Dot product"""
        return self.x * altro.x + self.y * altro.y + self.z * altro.z

    def prodotto_vettoriale(self, altro):
        """Cross product"""
        x = self.y * altro.z - self.z * altro.y
        y = self.z * altro.x - self.x * altro.z
        z = self.x * altro.y - self.y * altro.x
        return Punto3D(x, y, z)
```

### 🌟 Sfida 2: Operatore // (floor division)
```python
class Punto2D:
    def __floordiv__(self, scalare):
        """Divisione intera"""
        if scalare == 0:
            raise ValueError("Divisione per zero")
        return Punto2D(self.x // scalare, self.y // scalare)

    def __mod__(self, scalare):
        """Modulo"""
        if scalare == 0:
            raise ValueError("Divisione per zero")
        return Punto2D(self.x % scalare, self.y % scalare)

    def __pow__(self, potenza):
        """Elevazione a potenza"""
        return Punto2D(self.x ** potenza, self.y ** potenza)
```

### 🌟 Sfida 3: Iterazione
```python
class Punto2D:
    def __iter__(self):
        """Rendi il punto iterabile"""
        return iter([self.x, self.y])

    def __next__(self):
        """Per for loops"""
        # Questo è già fatto da __iter__

# Uso:
p = Punto2D(3, 4)
x, y = p  # Unpacking!
for coord in p:
    print(coord)
```

### 🌟 Sfida 4: Operatori di assegnamento aumentato
```python
class Punto2D:
    def __iadd__(self, altro):
        """+="""
        self.x += altro.x
        self.y += altro.y
        return self

    def __isub__(self, altro):
        """-="""
        self.x -= altro.x
        self.y -= altro.y
        return self

    def __imul__(self, scalare):
        """*="""
        self.x *= scalare
        self.y *= scalare
        return self

# Uso:
p = Punto2D(1, 2)
p += Punto2D(3, 4)  # p diventa (4, 6)
p *= 2              # p diventa (8, 12)
```

### 🌟 Sfida 5: Conversione di tipo e chiamabilità
```python
class Punto2D:
    def __int__(self):
        """Converti in int - somma delle coordinate"""
        return int(self.x + self.y)

    def __float__(self):
        """Converti in float - distanza"""
        return self.distanza()

    def __call__(self, scalare):
        """Rendi il punto "chiamabile""""
        return Punto2D(self.x * scalare, self.y * scalare)

# Uso:
p = Punto2D(3, 4)
print(int(p))      # 7 (3 + 4)
print(float(p))    # 5.0 (distanza)
p_scaled = p(2)    # (6, 8)
```

---

## 📖 Riassunto Concetti Importanti

| Metodo | Uso | Esempio |
|--------|-----|---------|
| `__init__` | Costruttore | `Punto2D(3, 4)` |
| `__str__` | Per print | `str(p)` |
| `__repr__` | Per repr | `repr(p)` |
| `__add__` | Operatore `+` | `p1 + p2` |
| `__sub__` | Operatore `-` | `p1 - p2` |
| `__mul__` | Operatore `*` | `p * 2` |
| `__rmul__` | Operatore `*` da destra | `2 * p` |
| `__truediv__` | Operatore `/` | `p / 2` |
| `__eq__` | Operatore `==` | `p1 == p2` |
| `__lt__` | Operatore `<` | `p1 < p2` |
| `__len__` | Funzione `len()` | `len(p)` |
| `__getitem__` | Accesso `[]` | `p[0]` |
| `__setitem__` | Modifica `[]` | `p[0] = 5` |
| `__hash__` | Per set/dict | `{p1, p2}` |
| `__bool__` | Per `if` | `if p:` |

---

## 🔗 Link Utili

### Documentazione
- [Data Model - Python Docs](https://docs.python.org/3/reference/datamodel.html)
- [Magic Methods - Python Docs](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [math Module](https://docs.python.org/3/library/math.html)

### Tutorial
- [Real Python - Magic Methods](https://realpython.com/operator-and-function-overloading-in-python/)
- [GeeksforGeeks - Dunder Methods](https://www.geeksforgeeks.org/dunder-magic-methods-python/)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Osserva come sono implementati gli operatori
- Guarda come sono gestite le comparazioni
- Nota come si implementa l'accesso per indice
- Apprendi dai metodi di utilità

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho implementato `__init__`, `__str__`, `__repr__`
- [ ] Ho implementato operatori aritmetici (`__add__`, `__sub__`, `__mul__`, `__rmul__`, `__truediv__`)
- [ ] Ho implementato negazione (`__neg__`)
- [ ] Ho implementato operatori di comparazione (`__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`)
- [ ] Ho implementato accesso per indice (`__getitem__`, `__setitem__`)
- [ ] Ho implementato `__len__`
- [ ] Ho implementato `__hash__` e `__bool__`
- [ ] Ho implementato metodi di utilità (distanza, distanza_da)
- [ ] Gli operatori ritornano nuovi oggetti (non modificano self)
- [ ] Uso tolleranza per comparazioni di float
- [ ] Ho testato con almeno 8 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai sbloccato la magia di Python! 🎉✨**

*"I metodi speciali rendono le tue classi intuitive come i tipi built-in di Python"*
