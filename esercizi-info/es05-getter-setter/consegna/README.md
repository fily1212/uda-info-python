# Es5: Getter e Setter - Rettangolo

## 📊 Informazioni Generali

**Livello:** 🟡 BASE
**Durata stimata:** 3-4 ore
**Prerequisiti:** Es1-4 completati, class ContoCorrente

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Creare** getter e setter per controllare l'accesso agli attributi
- ✅ **Validare** i dati in ingresso (no valori negativi)
- ✅ **Proteggere** gli attributi da modifiche non valide
- ✅ **Implementare** metodi di calcolo (area, perimetro, diagonale)
- ✅ **Capire** l'encapsulamento e la proprietà privata
- ✅ **Usare** convenzioni Python per attributi privati (_attributo, __attributo)

**Concetti fondamentali:**
- Attributi privati (convenzione _nome e __nome)
- Metodi getter (get_attributo o @property)
- Metodi setter (set_attributo o @attributo.setter)
- Validazione nei setter
- Calcoli basati su attributi protetti

---

## 📖 Descrizione

Finora hai permetteva chiunque di modificare direttamente gli attributi di un oggetto:

```python
rettangolo = Rettangolo(10, 5)
rettangolo.base = -100  # Questo non dovrebbe essere permesso!
rettangolo.altezza = "pippo"  # Neanche questo!
```

I **getter e setter** ti permettono di **controllare come** gli attributi vengono modificati:

```python
class Rettangolo:
    def __init__(self, base, altezza):
        self._base = base      # Attributo privato (per convenzione)
        self._altezza = altezza

    def set_base(self, nuova_base):
        """Setter - controlla il valore prima di assegnarlo"""
        if nuova_base <= 0:
            print("Errore: base deve essere positiva!")
            return False
        self._base = nuova_base
        return True

    def get_base(self):
        """Getter - ritorna il valore"""
        return self._base

rettangolo = Rettangolo(10, 5)
rettangolo.set_base(-100)  # Stampa errore, non assegna!
rettangolo.set_base(15)    # Funziona!
```

**Perché è importante?**
1. **Validazione** - assicuri che i dati siano sensati
2. **Incapsulamento** - nascondi i dettagli interni
3. **Calcoli automatici** - il setter può fare cose aggiuntive
4. **Manutenibilità** - se cambi la logica, cambi solo il setter

Un **Rettangolo** è perfetto per imparare questo perché:
- Ha attributi sensibili (base, altezza) che devono essere > 0
- Ha calcoli utili (area, perimetro, diagonale)
- È facile capire cosa sia "corretto" e cosa "sbagliato"

---

## 📝 Consegna Dettagliata

### Parte 1: Attributi Privati e Setter/Getter Base

**Definisci una classe `Rettangolo` con:**

1. **Attributi privati:**
   - `_base` (float, privato)
   - `_altezza` (float, privato)

2. **Metodi Getter:**
   - `get_base()` - ritorna la base
   - `get_altezza()` - ritorna l'altezza

3. **Metodi Setter con Validazione:**
   - `set_base(valore)` - assegna base solo se > 0
   - `set_altezza(valore)` - assegna altezza solo se > 0
   - Se il valore non è valido, stampa errore e NON assegna
   - Ritorna True se riuscito, False se fallito

4. **Costruttore `__init__`:**
   - Riceve base e altezza
   - Usa i setter per assegnare (così valida subito!)
   - Se non sono validi, assegna un valore di default (es: 1.0)

### Parte 2: Metodi di Calcolo

**Aggiungi metodi per calcolare:**

1. **`area()`**
   - Ritorna: base * altezza

2. **`perimetro()`**
   - Ritorna: 2 * (base + altezza)

3. **`diagonale()`**
   - Usa il teorema di Pitagora: √(base² + altezza²)
   - Importa `math.sqrt` o usa `**0.5`
   - Ritorna il valore con 2 decimali

4. **`è_quadrato()`**
   - Ritorna True se base == altezza, False altrimenti

5. **`scala(fattore)`**
   - Moltiplica base e altezza per fattore
   - Es: scala(2) raddoppia le dimensioni
   - Usa i setter (così valida i nuovi valori!)

### Parte 3: Metodi Informativi

1. **`info()`**
   - Ritorna stringa: "Rettangolo 10x5 - Area: 50, Perimetro: 30"

2. **`dettagli()`**
   - Ritorna info completa con diagonale:
   - "Base: 10, Altezza: 5"
   - "Area: 50, Perimetro: 30, Diagonale: 11.18"

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSE ============

import math

class Rettangolo:
    """Rappresenta un rettangolo con base e altezza"""

    def __init__(self, base, altezza):
        """Crea un rettangolo con validazione"""
        self._base = 1.0
        self._altezza = 1.0

        # Usa i setter per validare
        if not self.set_base(base):
            print(f"Attenzione: base invalida, impostata a 1.0")

        if not self.set_altezza(altezza):
            print(f"Attenzione: altezza invalida, impostata a 1.0")

    # ===== GETTER =====

    def get_base(self):
        """Ritorna la base"""
        return self._base

    def get_altezza(self):
        """Ritorna l'altezza"""
        return self._altezza

    # ===== SETTER =====

    def set_base(self, nuova_base):
        """Imposta la base se valida (> 0)"""
        try:
            nuova_base = float(nuova_base)
            if nuova_base <= 0:
                print(f"Errore: base deve essere positiva (ricevuto {nuova_base})")
                return False
            self._base = nuova_base
            return True
        except (ValueError, TypeError):
            print(f"Errore: base deve essere un numero")
            return False

    def set_altezza(self, nuova_altezza):
        """Imposta l'altezza se valida (> 0)"""
        try:
            nuova_altezza = float(nuova_altezza)
            if nuova_altezza <= 0:
                print(f"Errore: altezza deve essere positiva (ricevuto {nuova_altezza})")
                return False
            self._altezza = nuova_altezza
            return True
        except (ValueError, TypeError):
            print(f"Errore: altezza deve essere un numero")
            return False

    # ===== METODI DI CALCOLO =====

    def area(self):
        """Calcola l'area"""
        return self._base * self._altezza

    def perimetro(self):
        """Calcola il perimetro"""
        return 2 * (self._base + self._altezza)

    def diagonale(self):
        """Calcola la diagonale (teorema di Pitagora)"""
        diag = math.sqrt(self._base**2 + self._altezza**2)
        return round(diag, 2)

    def è_quadrato(self):
        """Ritorna True se è un quadrato"""
        return abs(self._base - self._altezza) < 0.001  # Tollera piccole differenze

    def scala(self, fattore):
        """Scala il rettangolo per un fattore"""
        if fattore <= 0:
            print("Errore: fattore di scala deve essere positivo")
            return False

        # Calcola i nuovi valori
        nuova_base = self._base * fattore
        nuova_altezza = self._altezza * fattore

        # Usa i setter (così valida automaticamente)
        self.set_base(nuova_base)
        self.set_altezza(nuova_altezza)
        return True

    # ===== METODI INFORMATIVI =====

    def info(self):
        """Ritorna info compatta"""
        return f"Rettangolo {self._base}x{self._altezza} - Area: {self.area()}, Perimetro: {self.perimetro()}"

    def dettagli(self):
        """Ritorna info dettagliata"""
        ritorno = f"Base: {self._base}, Altezza: {self._altezza}\n"
        ritorno += f"Area: {self.area()}, Perimetro: {self.perimetro()}, Diagonale: {self.diagonale()}\n"
        if self.è_quadrato():
            ritorno += "Forma: Quadrato"
        else:
            ritorno += "Forma: Rettangolo"
        return ritorno


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    print("=== CREAZIONE RETTANGOLI ===\n")

    # Rettangolo valido
    r1 = Rettangolo(10, 5)
    print(r1.info())
    print(r1.dettagli())

    # Rettangolo con valori invalidi (corregge automaticamente)
    print("\n=== RETTANGOLO CON VALORI INVALIDI ===")
    r2 = Rettangolo(-5, 0)
    print(r2.info())

    # Test setter
    print("\n=== TEST SETTER ===")
    print("Provo a impostare base = -10:")
    r1.set_base(-10)  # Fallisce
    print(f"Base rimane: {r1.get_base()}")

    print("\nProvo a impostare base = 15:")
    r1.set_base(15)  # Funziona
    print(f"Nuova base: {r1.get_base()}")
    print(r1.info())

    # Test quadrato
    print("\n=== TEST QUADRATO ===")
    r3 = Rettangolo(5, 5)
    print(f"È quadrato? {r3.è_quadrato()}")
    print(r3.dettagli())

    # Test scala
    print("\n=== TEST SCALA ===")
    r1.scala(2)  # Raddoppia
    print("Dopo scala(2):")
    print(r1.dettagli())

    r1.scala(0.5)  # Dimezza
    print("\nDopo scala(0.5):")
    print(r1.dettagli())

    # Test calcoli
    print("\n=== CALCOLI VARI ===")
    rettangoli = [
        Rettangolo(3, 4),
        Rettangolo(5, 12),
        Rettangolo(10, 10),
    ]

    for i, r in enumerate(rettangoli, 1):
        print(f"\nRettangolo {i}: {r.info()}")
        print(f"  Diagonale: {r.diagonale()}")
        print(f"  È quadrato? {r.è_quadrato()}")

# Output atteso:
# === CREAZIONE RETTANGOLI ===
# Rettangolo 10x5 - Area: 50, Perimetro: 30
# Base: 10, Altezza: 5
# Area: 50, Perimetro: 30, Diagonale: 11.18
# Forma: Rettangolo
# ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione e getter
```python
r = Rettangolo(10, 5)
assert r.get_base() == 10
assert r.get_altezza() == 5
print("✓ Test 1 passato")
```

### Test 2: Setter valido
```python
r = Rettangolo(10, 5)
assert r.set_base(15) == True
assert r.get_base() == 15
print("✓ Test 2 passato")
```

### Test 3: Setter invalido (negativo)
```python
r = Rettangolo(10, 5)
assert r.set_base(-5) == False
assert r.get_base() == 10  # Non cambia
print("✓ Test 3 passato")
```

### Test 4: Setter invalido (zero)
```python
r = Rettangolo(10, 5)
assert r.set_altezza(0) == False
assert r.get_altezza() == 5  # Non cambia
print("✓ Test 4 passato")
```

### Test 5: Area
```python
r = Rettangolo(10, 5)
assert r.area() == 50
r.set_base(3)
r.set_altezza(4)
assert r.area() == 12
print("✓ Test 5 passato")
```

### Test 6: Perimetro
```python
r = Rettangolo(10, 5)
assert r.perimetro() == 30
r.set_base(6)
r.set_altezza(4)
assert r.perimetro() == 20
print("✓ Test 6 passato")
```

### Test 7: Diagonale (Pitagora)
```python
r = Rettangolo(3, 4)  # Triangolo 3-4-5
assert r.diagonale() == 5.0

r = Rettangolo(5, 12)  # Triangolo 5-12-13
assert r.diagonale() == 13.0

r = Rettangolo(1, 1)
assert abs(r.diagonale() - 1.41) < 0.01
print("✓ Test 7 passato")
```

### Test 8: Quadrato
```python
r1 = Rettangolo(5, 5)
assert r1.è_quadrato() == True

r2 = Rettangolo(5, 6)
assert r2.è_quadrato() == False

r3 = Rettangolo(7.5, 7.5)
assert r3.è_quadrato() == True
print("✓ Test 8 passato")
```

### Test 9: Scala
```python
r = Rettangolo(10, 5)
r.scala(2)
assert r.get_base() == 20
assert r.get_altezza() == 10
assert r.area() == 200  # (10*2) * (5*2) = 20 * 10 = 200

r.scala(0.5)
assert r.get_base() == 10
assert r.get_altezza() == 5
print("✓ Test 9 passato")
```

### Test 10: Validazione nel costruttore
```python
r = Rettangolo(-5, 10)
# Dovrebbe impostare valori di default o correggere
assert r.get_base() > 0
assert r.get_altezza() > 0
print("✓ Test 10 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Definisci attributi privati e getter
```python
class Rettangolo:
    def __init__(self, base, altezza):
        self._base = base
        self._altezza = altezza

    def get_base(self):
        return self._base

    def get_altezza(self):
        return self._altezza
```

### Passo 2: Aggiungi i setter con validazione
```python
def set_base(self, nuova_base):
    """Setter con validazione"""
    if nuova_base <= 0:
        print(f"Errore: base deve essere > 0")
        return False
    self._base = nuova_base
    return True

def set_altezza(self, nuova_altezza):
    """Setter con validazione"""
    if nuova_altezza <= 0:
        print(f"Errore: altezza deve essere > 0")
        return False
    self._altezza = nuova_altezza
    return True
```

### Passo 3: Modifica il costruttore per usare i setter
```python
def __init__(self, base, altezza):
    self._base = 1.0  # Default
    self._altezza = 1.0  # Default

    # Usa i setter per validare
    if not self.set_base(base):
        print("Base invalida, usato default 1.0")

    if not self.set_altezza(altezza):
        print("Altezza invalida, usato default 1.0")
```

### Passo 4: Implementa i metodi di calcolo
```python
import math

def area(self):
    return self._base * self._altezza

def perimetro(self):
    return 2 * (self._base + self._altezza)

def diagonale(self):
    d = math.sqrt(self._base**2 + self._altezza**2)
    return round(d, 2)

def è_quadrato(self):
    return self._base == self._altezza
```

### Passo 5: Implementa scala
```python
def scala(self, fattore):
    """Scala il rettangolo"""
    if fattore <= 0:
        return False

    # Calcola nuovi valori
    nuova_base = self._base * fattore
    nuova_altezza = self._altezza * fattore

    # Usa i setter (valida automaticamente)
    self.set_base(nuova_base)
    self.set_altezza(nuova_altezza)
    return True
```

### Passo 6: Aggiungi metodi informativi
```python
def info(self):
    return f"Rettangolo {self._base}x{self._altezza} - Area: {self.area()}, Perimetro: {self.perimetro()}"

def dettagli(self):
    s = f"Base: {self._base}, Altezza: {self._altezza}\n"
    s += f"Area: {self.area()}, Perimetro: {self.perimetro()}, Diagonale: {self.diagonale()}"
    return s
```

### Passo 7: Testa la classe
```python
r = Rettangolo(10, 5)
print(r.info())
r.set_base(15)
print(f"Area: {r.area()}")
print(f"Quadrato? {r.è_quadrato()}")
r.scala(2)
print(r.dettagli())
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa il prefisso `_` per indicare attributi privati
```python
class Rettangolo:
    def __init__(self, base, altezza):
        self._base = base  # Privato (per convenzione)
        self._altezza = altezza

# Non fai così (pubblico):
# self.base = base
```

### ✅ Valida sempre nei setter
```python
# BUONO - valida il tipo e il valore
def set_base(self, valore):
    try:
        valore = float(valore)
        if valore <= 0:
            raise ValueError("Deve essere positivo")
        self._base = valore
        return True
    except:
        return False

# CATTIVO - non valida
def set_base(self, valore):
    self._base = valore
```

### ✅ Usa i setter nel costruttore
```python
# BUONO - valida nel costruttore
def __init__(self, base, altezza):
    self._base = 1.0
    self._altezza = 1.0
    self.set_base(base)
    self.set_altezza(altezza)

# MENO BUONO - non valida
def __init__(self, base, altezza):
    self._base = base
    self._altezza = altezza
```

### ✅ Documenta cosa è privato e cosa pubblico
```python
class Rettangolo:
    """Rettangolo con getter/setter

    Attributi privati:
        _base: float - la base
        _altezza: float - l'altezza

    Metodi pubblici:
        area() - calcola l'area
        perimetro() - calcola il perimetro
    """
```

### ✅ Usa `math.sqrt` per la radice
```python
import math

def diagonale(self):
    return math.sqrt(self._base**2 + self._altezza**2)

# Oppure usa **0.5 (più compatto)
def diagonale(self):
    return (self._base**2 + self._altezza**2)**0.5
```

### ✅ Tolleranza per comparazioni di float
```python
# SBAGLIATO - float non sono mai esattamente uguali
def è_quadrato(self):
    return self._base == self._altezza

# GIUSTO - tolleranza di piccola differenza
def è_quadrato(self):
    return abs(self._base - self._altezza) < 0.001
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Accedere direttamente agli attributi privati
```python
# SBAGLIATO - ignora la validazione
r = Rettangolo(10, 5)
r._base = -100  # Cambia senza validare!

# GIUSTO - usa il setter
r.set_base(-100)  # Stampa errore, non cambia
```

### ❌ Errore 2: Dimenticare di validare nei setter
```python
# SBAGLIATO - non valida
def set_base(self, valore):
    self._base = valore

# GIUSTO - valida
def set_base(self, valore):
    if valore <= 0:
        return False
    self._base = valore
    return True
```

### ❌ Errore 3: Non usare i setter nel costruttore
```python
# SBAGLIATO - il costruttore non valida
def __init__(self, base, altezza):
    self._base = base
    self._altezza = altezza
    # Se qualcuno passa -5, viene accettato!

# GIUSTO - il costruttore usa i setter
def __init__(self, base, altezza):
    self._base = 1.0
    self._altezza = 1.0
    self.set_base(base)  # Valida
    self.set_altezza(altezza)  # Valida
```

### ❌ Errore 4: Confondere area con perimetro
```python
# SBAGLIATO
def area(self):
    return 2 * (self._base + self._altezza)  # Questo è il perimetro!

# GIUSTO
def area(self):
    return self._base * self._altezza

def perimetro(self):
    return 2 * (self._base + self._altezza)
```

### ❌ Errore 5: Non gestire divisione per zero nella diagonale
```python
# Normalmente non è un problema con dimensioni > 0, ma...
# BUONO - usare math.sqrt
import math
def diagonale(self):
    return math.sqrt(self._base**2 + self._altezza**2)

# ANCHE BUONO - usare **0.5
def diagonale(self):
    return (self._base**2 + self._altezza**2)**0.5
```

### ❌ Errore 6: Stampare dentro il setter
```python
# MEDIOCRE - stampa al setter
def set_base(self, valore):
    if valore <= 0:
        print("Errore!")  # Brutto per unit test
        return False

# MIGLIORE - solo ritorna False, lascia al chiamante di stampare
def set_base(self, valore):
    if valore <= 0:
        return False  # Solo ritorna
    self._base = valore
    return True
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: @property Decorator (Python Advanced)
Usa `@property` per fare sembrare i getter come attributi:

```python
class Rettangolo:
    # ...

    @property
    def base(self):
        """Accedi come r.base invece di r.get_base()"""
        return self._base

    @base.setter
    def base(self, valore):
        """Assegna come r.base = 15 invece di r.set_base(15)"""
        if valore <= 0:
            raise ValueError("Base deve essere > 0")
        self._base = valore

# Uso:
r = Rettangolo(10, 5)
print(r.base)  # 10 - sembra un attributo!
r.base = 15    # Usa il setter!
r.base = -5    # Solleva ValueError
```

### 🌟 Sfida 2: Confronto Tra Rettangoli
Aggiungi metodi per confrontare:

```python
def ha_stessa_area(self, altro):
    """Ritorna True se hanno la stessa area"""
    return abs(self.area() - altro.area()) < 0.001

def ha_maggiore_area(self, altro):
    """Ritorna True se questo ha area maggiore"""
    return self.area() > altro.area()

def hanno_stesso_perimetro(self, altro):
    """Ritorna True se hanno lo stesso perimetro"""
    return abs(self.perimetro() - altro.perimetro()) < 0.001

# Uso:
r1 = Rettangolo(10, 5)
r2 = Rettangolo(5, 10)  # Stessa area!
print(r1.ha_stessa_area(r2))  # True
```

### 🌟 Sfida 3: Rettangolo come Griglia
Usa il rettangolo per rappresentare una griglia:

```python
class Rettangolo:
    # ...

    def numero_quadrati_unitari(self):
        """Quanti quadrati 1x1 entrano?"""
        return int(self._base) * int(self._altezza)

    def numero_celle(self, largezza_cella, altezza_cella):
        """Quante celle di una certa dimensione entrano?"""
        return int(self._base / largezza_cella) * int(self._altezza / altezza_cella)

    def stampa_griglia(self, simbolo="*"):
        """Stampa una rappresentazione ASCII del rettangolo"""
        larghezza = int(self._base)
        altezza = int(self._altezza)
        for i in range(altezza):
            print(simbolo * larghezza)
```

### 🌟 Sfida 4: Rettangolo come Coordinate
Assegna al rettangolo una posizione:

```python
class Rettangolo:
    def __init__(self, base, altezza, x=0, y=0):
        self._base = base
        self._altezza = altezza
        self._x = x  # Posizione top-left
        self._y = y

    def contiene_punto(self, px, py):
        """Ritorna True se il punto (px, py) è dentro il rettangolo"""
        return (self._x <= px <= self._x + self._base and
                self._y <= py <= self._y + self._altezza)

    def si_sovrappone_con(self, altro):
        """Ritorna True se questo rettangolo si sovrappone con un altro"""
        return not (self._x + self._base < altro._x or
                   altro._x + altro._base < self._x or
                   self._y + self._altezza < altro._y or
                   altro._y + altro._altezza < self._y)
```

### 🌟 Sfida 5: Rettangolo come Framing
Aggiungi margini/bordo:

```python
class Rettangolo:
    # ...

    def aggiungi_margine(self, margine):
        """Aggiunge margine esterno"""
        self.scala(1 + margine / min(self._base, self._altezza))

    def crea_rettangolo_interno(self, margine):
        """Ritorna un nuovo rettangolo più piccolo di margine"""
        nuova_base = self._base - 2 * margine
        nuova_altezza = self._altezza - 2 * margine
        if nuova_base <= 0 or nuova_altezza <= 0:
            return None
        return Rettangolo(nuova_base, nuova_altezza)

    def percentuale_riempimento(self, oggetto_interno):
        """Percentuale di area occupata dall'oggetto"""
        if self.area() == 0:
            return 0
        return (oggetto_interno.area() / self.area()) * 100
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Attributo privato** | Nascosto (per convenzione _) | `self._base` |
| **Getter** | Metodo che ritorna un attributo | `get_base()` |
| **Setter** | Metodo che assegna con validazione | `set_base(valore)` |
| **Validazione** | Controllare che il valore sia corretto | `if valore <= 0: return False` |
| **Encapsulamento** | Nascondere dettagli interni | Usare getter/setter |
| **@property** | Decorator per fare getter/setter trasparenti | `@property def base(self)` |
| **Tolleranza float** | Piccola differenza per comparazioni | `abs(a - b) < 0.001` |

---

## 🔗 Link Utili

### Documentazione
- [Python Getter and Setter](https://docs.python.org/3/tutorial/classes.html)
- [@property Decorator](https://docs.python.org/3/library/functions.html#property)
- [Math Module](https://docs.python.org/3/library/math.html)

### Tutorial
- [Real Python - @property](https://realpython.com/python-property/)
- [Encapsulation in Python](https://www.geeksforgeeks.org/encapsulation-in-python/)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Nota come sono implementati i getter e setter
- Guarda come viene fatta la validazione
- Apprendi dal design degli attributi privati
- Valuta se la soluzione usa @property

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho definito attributi privati (_base, _altezza)
- [ ] Ho implementato getter e setter per base e altezza
- [ ] I setter validano che i valori siano > 0
- [ ] Il costruttore usa i setter per validare
- [ ] Metodo area() calcola correttamente
- [ ] Metodo perimetro() calcola correttamente
- [ ] Metodo diagonale() usa Pitagora correttamente
- [ ] Metodo è_quadrato() funziona
- [ ] Metodo scala() cambia entrambe le dimensioni
- [ ] Metodi info() e dettagli() stampa i dati
- [ ] Ho testato tutti i casi limite
- [ ] Ho testato con valori invalidi
- [ ] Ho aggiunto le estensioni (almeno una)

---

**Congratulazioni! Hai implementato l'encapsulamento con getter e setter! 🎉🐍**

*"Proteggere i dati con getter e setter è il primo passo verso un buon design orientato agli oggetti."*
