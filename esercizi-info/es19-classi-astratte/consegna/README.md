# Es14: Classi Astratte - Forme Geometriche

## 📊 Informazioni Generali

**Livello:** 🔴 AVANZATO
**Durata stimata:** 6-7 ore
**Prerequisiti:** Es1-13 completati, ABC, metodi astratti

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Usare** il modulo `abc` (Abstract Base Classes)
- ✅ **Definire** metodi astratti obbligatori
- ✅ **Impedire** istanziazione di classi astratte
- ✅ **Forzare** implementazione in sottoclassi
- ✅ **Creare** gerarchie di classi ben definite
- ✅ **Implementare** contratti (interfacce) Python
- ✅ **Applicare** polimorfismo attraverso ABC

**Concetti fondamentali:**
- ABC = Abstract Base Class
- @abstractmethod = metodo che deve essere implementato
- Non puoi istanziare una classe astratta
- Sottoclassi DEVONO implementare tutti i metodi astratti
- ABC garantisce contratto tra classi
- Polimorfismo attraverso interfaccia comune

---

## 📖 Descrizione

Una **forma geometrica** ha proprietà comuni:
- Perimetro e area
- Calcoli basati su dimensioni

Questo esercizio crea una **gerarchia di forme** con:
- **Classe astratta `Forma`** che definisce l'interfaccia
- **Metodi astratti** area() e perimetro()
- **Classi concrete** Cerchio, Rettangolo, Triangolo, Quadrato
- **Validazione** dimensioni positive
- **Polimorfismo** per calcoli su collezioni di forme
- **Proprietà calcolate** (area, perimetro)

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Astratta Forma

**Definisci una classe astratta `Forma` con:**

1. **Metodi astratti:**
   - `area()` - calcola l'area
   - `perimetro()` - calcola il perimetro
   - `descrizione()` - descrizione della forma

2. **Metodi concreti:**
   - `è_valida()` - True se dimensioni sono valide (> 0)
   - `__str__()` - stampa area e perimetro
   - `__repr__()` - rappresentazione tecnica

3. **Proprietà:**
   - Non permette istanziazione diretta

### Parte 2: Classe Cerchio

**Implementa una classe `Cerchio(Forma)` con:**

1. **Attributi:**
   - `raggio` (float) - raggio del cerchio

2. **Metodi astratti implementati:**
   - `area()` - π × r²
   - `perimetro()` - 2 × π × r
   - `descrizione()` - "Cerchio con raggio..."

3. **Metodi aggiuntivi:**
   - `diametro()` - 2 × raggio
   - `cambia_raggio(nuovo_raggio)` - modifica raggio

### Parte 3: Classe Rettangolo

**Implementa una classe `Rettangolo(Forma)` con:**

1. **Attributi:**
   - `larghezza` (float)
   - `altezza` (float)

2. **Metodi astratti implementati:**
   - `area()` - larghezza × altezza
   - `perimetro()` - 2 × (larghezza + altezza)
   - `descrizione()` - "Rettangolo..."

3. **Metodi aggiuntivi:**
   - `diagonale()` - √(l² + h²)
   - `è_quadrato()` - True se larghezza == altezza

### Parte 4: Classe Triangolo

**Implementa una classe `Triangolo(Forma)` con:**

1. **Attributi:**
   - `lato1, lato2, lato3` (float) - tre lati

2. **Metodi astratti implementati:**
   - `area()` - formula di Erone: √(s(s-a)(s-b)(s-c)), s = semiperimetro
   - `perimetro()` - lato1 + lato2 + lato3
   - `descrizione()` - "Triangolo..."

3. **Metodi aggiuntivi:**
   - `è_valido()` - verifica diseguaglianza triangolare
   - `tipo_triangolo()` - equilatero, isoscele, scaleno
   - `è_rettangolo()` - verifica teorema di Pitagora

### Parte 5: Classe Quadrato

**Implementa una classe `Quadrato(Rettangolo)` con:**

1. **Attributi:**
   - `lato` (float) - un solo lato (eredita larghezza=altezza=lato)

2. **Override se necessario**

3. **Metodi aggiuntivi:**
   - Specificità del quadrato (semplice, un solo parametro)

### Parte 6: Funzioni Polimorfiche

**Implementa funzioni che lavorano con qualunque forma:**

1. `area_totale(forme)` - somma aree
2. `perimetro_massimo(forme)` - forma con perimetro più grande
3. `forma_piu_compatta(forme)` - forma con area/perimetro massimo
4. `classifica_per_area(forme)` - ordina per area
5. `rapporto_forme(forme)` - statistiche

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ CLASSI ASTRATTE ============

from abc import ABC, abstractmethod
import math


class Forma(ABC):
    """Classe astratta per forme geometriche"""

    @abstractmethod
    def area(self):
        """Calcola l'area della forma"""
        pass

    @abstractmethod
    def perimetro(self):
        """Calcola il perimetro della forma"""
        pass

    @abstractmethod
    def descrizione(self):
        """Descrizione della forma"""
        pass

    def è_valida(self):
        """Controlla se la forma è valida"""
        return True  # Override se necessario

    def __str__(self):
        """Stampa area e perimetro"""
        return (
            f"{self.descrizione()}\n"
            f"  Area: {self.area():.2f}\n"
            f"  Perimetro: {self.perimetro():.2f}"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}(...)"


# ============ CLASSE CERCHIO ============

class Cerchio(Forma):
    """Un cerchio definito dal raggio"""

    def __init__(self, raggio):
        if raggio <= 0:
            raise ValueError("Il raggio deve essere positivo")
        self.raggio = float(raggio)

    def area(self):
        """Area: π × r²"""
        return math.pi * self.raggio ** 2

    def perimetro(self):
        """Perimetro (circonferenza): 2 × π × r"""
        return 2 * math.pi * self.raggio

    def descrizione(self):
        return f"Cerchio con raggio {self.raggio:.2f}"

    def diametro(self):
        """Diametro = 2 × raggio"""
        return 2 * self.raggio

    def cambia_raggio(self, nuovo_raggio):
        """Modifica il raggio"""
        if nuovo_raggio <= 0:
            raise ValueError("Il raggio deve essere positivo")
        self.raggio = float(nuovo_raggio)


# ============ CLASSE RETTANGOLO ============

class Rettangolo(Forma):
    """Un rettangolo definito da larghezza e altezza"""

    def __init__(self, larghezza, altezza):
        if larghezza <= 0 or altezza <= 0:
            raise ValueError("Larghezza e altezza devono essere positive")
        self.larghezza = float(larghezza)
        self.altezza = float(altezza)

    def area(self):
        """Area: larghezza × altezza"""
        return self.larghezza * self.altezza

    def perimetro(self):
        """Perimetro: 2 × (larghezza + altezza)"""
        return 2 * (self.larghezza + self.altezza)

    def descrizione(self):
        return f"Rettangolo {self.larghezza:.2f}×{self.altezza:.2f}"

    def diagonale(self):
        """Diagonale: √(l² + h²)"""
        return math.sqrt(self.larghezza ** 2 + self.altezza ** 2)

    def è_quadrato(self):
        """True se larghezza == altezza"""
        return abs(self.larghezza - self.altezza) < 1e-9


# ============ CLASSE TRIANGOLO ============

class Triangolo(Forma):
    """Un triangolo definito dai tre lati"""

    def __init__(self, lato1, lato2, lato3):
        if lato1 <= 0 or lato2 <= 0 or lato3 <= 0:
            raise ValueError("Tutti i lati devono essere positivi")

        # Verifica diseguaglianza triangolare
        if not (lato1 + lato2 > lato3 and lato1 + lato3 > lato2 and lato2 + lato3 > lato1):
            raise ValueError("I lati non formano un triangolo valido")

        self.lato1 = float(lato1)
        self.lato2 = float(lato2)
        self.lato3 = float(lato3)

    def perimetro(self):
        """Perimetro: lato1 + lato2 + lato3"""
        return self.lato1 + self.lato2 + self.lato3

    def area(self):
        """Area: formula di Erone"""
        s = self.perimetro() / 2  # semiperimetro
        area_quadrata = s * (s - self.lato1) * (s - self.lato2) * (s - self.lato3)
        if area_quadrata < 0:
            return 0
        return math.sqrt(area_quadrata)

    def descrizione(self):
        tipo = self.tipo_triangolo()
        return f"Triangolo {tipo} ({self.lato1:.2f}, {self.lato2:.2f}, {self.lato3:.2f})"

    def è_valido(self):
        """Verifica diseguaglianza triangolare"""
        return (
            self.lato1 + self.lato2 > self.lato3 and
            self.lato1 + self.lato3 > self.lato2 and
            self.lato2 + self.lato3 > self.lato1
        )

    def tipo_triangolo(self):
        """Ritorna il tipo di triangolo"""
        lati = sorted([self.lato1, self.lato2, self.lato3])
        tolleranza = 1e-9

        # Equilatero
        if abs(lati[0] - lati[1]) < tolleranza and abs(lati[1] - lati[2]) < tolleranza:
            return "equilatero"
        # Isoscele
        elif (abs(lati[0] - lati[1]) < tolleranza or
              abs(lati[1] - lati[2]) < tolleranza):
            return "isoscele"
        # Scaleno
        else:
            return "scaleno"

    def è_rettangolo(self):
        """Verifica se è rettangolo (Pitagora)"""
        lati = sorted([self.lato1, self.lato2, self.lato3])
        a, b, c = lati[0], lati[1], lati[2]
        return abs(a**2 + b**2 - c**2) < 1e-9


# ============ CLASSE QUADRATO ============

class Quadrato(Rettangolo):
    """Un quadrato (caso speciale di rettangolo)"""

    def __init__(self, lato):
        if lato <= 0:
            raise ValueError("Il lato deve essere positivo")
        super().__init__(lato, lato)
        self.lato = float(lato)

    def descrizione(self):
        return f"Quadrato con lato {self.lato:.2f}"

    def cambia_lato(self, nuovo_lato):
        """Modifica il lato"""
        if nuovo_lato <= 0:
            raise ValueError("Il lato deve essere positivo")
        self.lato = float(nuovo_lato)
        self.larghezza = self.lato
        self.altezza = self.lato


# ============ FUNZIONI POLIMORFICHE ============

def area_totale(forme):
    """Calcola l'area totale di una collezione di forme"""
    return sum(forma.area() for forma in forme)


def perimetro_massimo(forme):
    """Ritorna la forma con il perimetro più grande"""
    if not forme:
        return None
    return max(forme, key=lambda f: f.perimetro())


def forma_piu_compatta(forme):
    """Ritorna la forma con il rapporto area/perimetro massimo"""
    if not forme:
        return None

    def compattezza(forma):
        p = forma.perimetro()
        return forma.area() / p if p > 0 else 0

    return max(forme, key=compattezza)


def classifica_per_area(forme):
    """Ordina le forme per area (crescente)"""
    return sorted(forme, key=lambda f: f.area())


def rapporto_forme(forme):
    """Stampa statistiche sulle forme"""
    if not forme:
        print("Nessuna forma")
        return

    print(f"\n{'='*60}")
    print(f"📊 RAPPORTO FORME ({len(forme)} forme)")
    print(f"{'='*60}")

    area_tot = area_totale(forme)
    perim_max = perimetro_massimo(forme)
    compatta = forma_piu_compatta(forme)

    print(f"Area totale: {area_tot:.2f}")
    print(f"Perimetro massimo: {perim_max.perimetro():.2f} ({perim_max.descrizione()})")
    print(f"Forma più compatta: {compatta.descrizione()}")

    print(f"\n{'─'*60}")
    print("Forme ordinate per area:")
    for i, forma in enumerate(classifica_per_area(forme), 1):
        print(f"  {i}. {forma.descrizione()}: area={forma.area():.2f}")

    print(f"{'='*60}\n")


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    print("=== CREAZIONE FORME ===\n")

    # Non puoi fare questo:
    # forma = Forma()  # ✗ TypeError: Can't instantiate abstract class Forma

    # Creare istanze di forme concrete
    c1 = Cerchio(5)
    print(f"✓ {c1.descrizione()}")

    r1 = Rettangolo(4, 6)
    print(f"✓ {r1.descrizione()}")

    q1 = Quadrato(5)
    print(f"✓ {q1.descrizione()}")

    t1 = Triangolo(3, 4, 5)
    print(f"✓ {t1.descrizione()}")

    print("\n=== PROPRIETÀ FORME ===\n")
    print(c1)
    print()
    print(r1)
    print()
    print(q1)
    print()
    print(t1)

    print("\n=== METODI SPECIFICI ===\n")
    print(f"Cerchio - diametro: {c1.diametro():.2f}")
    print(f"Rettangolo - diagonale: {r1.diagonale():.2f}")
    print(f"Rettangolo - è quadrato? {r1.è_quadrato()}")
    print(f"Quadrato - è quadrato? {q1.è_quadrato()}")
    print(f"Triangolo - tipo: {t1.tipo_triangolo()}")
    print(f"Triangolo (3,4,5) - è rettangolo? {t1.è_rettangolo()}")

    print("\n=== COLLEZIONE DI FORME ===\n")
    forme = [
        Cerchio(3),
        Rettangolo(4, 5),
        Quadrato(4),
        Triangolo(5, 5, 6),
        Cerchio(2)
    ]

    # Usa funzioni polimorfiche
    rapporto_forme(forme)

    print("=== ORDINAMENTO ===\n")
    ordinate = classifica_per_area(forme)
    for forma in ordinate:
        print(f"  {forma.descrizione()}: area={forma.area():.2f}")

    print("\n=== POLIMORFISMO ===\n")
    # Cicla su tutti, indipendentemente dal tipo
    for forma in forme:
        print(f"{forma.descrizione()}: area={forma.area():.2f}, perim={forma.perimetro():.2f}")

    print("\n=== GESTIONE ERRORI ===\n")
    try:
        c_invalid = Cerchio(-5)
    except ValueError as e:
        print(f"✗ Errore Cerchio: {e}")

    try:
        t_invalid = Triangolo(1, 2, 10)  # Non forma un triangolo
    except ValueError as e:
        print(f"✗ Errore Triangolo: {e}")

    try:
        forma_astratta = Forma()
    except TypeError as e:
        print(f"✗ Errore Forma astratta: Non puoi istanziare una classe astratta")
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Non puoi istanziare classe astratta
```python
try:
    forma = Forma()
    assert False  # Non dovrebbe arrivare qui
except TypeError:
    pass  # Atteso
print("✓ Test 1 passato")
```

### Test 2: Cerchio - area e perimetro
```python
c = Cerchio(5)
assert abs(c.area() - math.pi * 25) < 0.01
assert abs(c.perimetro() - 2 * math.pi * 5) < 0.01
assert c.diametro() == 10
print("✓ Test 2 passato")
```

### Test 3: Rettangolo - area e perimetro
```python
r = Rettangolo(4, 6)
assert r.area() == 24
assert r.perimetro() == 20
assert abs(r.diagonale() - math.sqrt(52)) < 0.01
assert r.è_quadrato() == False
print("✓ Test 3 passato")
```

### Test 4: Quadrato - specializzazione
```python
q = Quadrato(5)
assert q.area() == 25
assert q.perimetro() == 20
assert q.è_quadrato() == True
assert q.diagonale() == math.sqrt(50)
print("✓ Test 4 passato")
```

### Test 5: Triangolo - area con Erone
```python
t = Triangolo(3, 4, 5)  # Triangolo rettangolo
assert abs(t.area() - 6.0) < 0.01  # (3×4)/2 = 6
assert t.perimetro() == 12
print("✓ Test 5 passato")
```

### Test 6: Triangolo - tipo
```python
t_eq = Triangolo(5, 5, 5)
assert t_eq.tipo_triangolo() == "equilatero"

t_iso = Triangolo(5, 5, 6)
assert t_iso.tipo_triangolo() == "isoscele"

t_sc = Triangolo(3, 4, 5)
assert t_sc.tipo_triangolo() == "scaleno"
print("✓ Test 6 passato")
```

### Test 7: Triangolo - è rettangolo
```python
t = Triangolo(3, 4, 5)
assert t.è_rettangolo() == True

t2 = Triangolo(5, 5, 5)
assert t2.è_rettangolo() == False
print("✓ Test 7 passato")
```

### Test 8: Triangolo - diseguaglianza
```python
try:
    t_invalid = Triangolo(1, 2, 10)
    assert False
except ValueError:
    pass
print("✓ Test 8 passato")
```

### Test 9: Polimorfismo - area_totale
```python
forme = [
    Cerchio(2),
    Quadrato(4),
    Rettangolo(3, 5)
]
tot = area_totale(forme)
atteso = math.pi * 4 + 16 + 15
assert abs(tot - atteso) < 0.01
print("✓ Test 9 passato")
```

### Test 10: Polimorfismo - perimetro_massimo
```python
forme = [
    Cerchio(1),
    Quadrato(2),
    Rettangolo(2, 2)
]
max_forma = perimetro_massimo(forme)
assert isinstance(max_forma, (Cerchio, Quadrato, Rettangolo))
print("✓ Test 10 passato")
```

### Test 11: Classifica per area
```python
forme = [
    Cerchio(5),
    Quadrato(2),
    Rettangolo(2, 3)
]
ordinate = classifica_per_area(forme)
for i in range(len(ordinate) - 1):
    assert ordinate[i].area() <= ordinate[i+1].area()
print("✓ Test 11 passato")
```

### Test 12: isinstance - verifica tipo
```python
c = Cerchio(5)
r = Rettangolo(4, 6)
q = Quadrato(5)
t = Triangolo(3, 4, 5)

assert isinstance(c, Forma)
assert isinstance(r, Forma)
assert isinstance(q, Forma)
assert isinstance(q, Rettangolo)  # Eredita da Rettangolo
assert isinstance(t, Forma)
print("✓ Test 12 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Definire classe astratta
```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def descrizione(self):
        pass
```

### Passo 2: Implementare Cerchio
```python
class Cerchio(Forma):
    def __init__(self, raggio):
        if raggio <= 0:
            raise ValueError("Raggio positivo")
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raggio

    def descrizione(self):
        return f"Cerchio raggio={self.raggio}"
```

### Passo 3: Implementare Rettangolo
```python
class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        if larghezza <= 0 or altezza <= 0:
            raise ValueError("Positivi")
        self.larghezza = larghezza
        self.altezza = altezza

    def area(self):
        return self.larghezza * self.altezza

    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)

    def descrizione(self):
        return f"Rettangolo {self.larghezza}×{self.altezza}"
```

### Passo 4: Implementare Triangolo
```python
class Triangolo(Forma):
    def __init__(self, l1, l2, l3):
        if not (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
            raise ValueError("Non è triangolo")
        self.lato1, self.lato2, self.lato3 = l1, l2, l3

    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s-self.lato1) * (s-self.lato2) * (s-self.lato3))

    def descrizione(self):
        return f"Triangolo ({self.lato1}, {self.lato2}, {self.lato3})"
```

### Passo 5: Implementare Quadrato
```python
class Quadrato(Rettangolo):
    def __init__(self, lato):
        if lato <= 0:
            raise ValueError("Positivo")
        super().__init__(lato, lato)
        self.lato = lato

    def descrizione(self):
        return f"Quadrato lato={self.lato}"
```

### Passo 6: Funzioni polimorfiche
```python
def area_totale(forme):
    return sum(f.area() for f in forme)

def perimetro_massimo(forme):
    return max(forme, key=lambda f: f.perimetro())

def classifica_per_area(forme):
    return sorted(forme, key=lambda f: f.area())
```

### Passo 7: Testa polimorfismo
```python
forme = [Cerchio(3), Rettangolo(4, 5), Triangolo(3, 4, 5)]
print(area_totale(forme))
for f in forme:
    print(f.descrizione())
```

### Passo 8: Aggiungi rapporto completo
```python
def rapporto_forme(forme):
    # Stampa statistiche dettagliate
    for forma in forme:
        print(forma)
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa ABC per contrati di interfaccia
```python
# BUONO - ABC garantisce contratto
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

# Allora tutte le sottoclassi DEVONO implementare area()

# CATTIVO - no ABC
class Forma:
    def area(self):
        raise NotImplementedError()
# Sottoclassi potrebbero "dimenticare"
```

### ✅ @abstractmethod per obbligare implementazione
```python
# BUONO - metodi astratti
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

# Se non implementi, TypeError al __init__

# CATTIVO - solo eccezione
class Forma:
    def area(self):
        raise NotImplementedError()
# Potrebbe non essere implementato
```

### ✅ Valida in __init__ delle sottoclassi
```python
# BUONO - valida subito
class Cerchio(Forma):
    def __init__(self, raggio):
        if raggio <= 0:
            raise ValueError("Raggio > 0")
        self.raggio = raggio

# CATTIVO - valida in area()
def area(self):
    if self.raggio <= 0:
        raise ValueError()
    return math.pi * self.raggio ** 2
```

### ✅ Usa isinstance() per tipo checking
```python
# BUONO
if isinstance(forma, Cerchio):
    print(forma.raggio)

# CATTIVO
if type(forma) == Cerchio:  # Non include sottoclassi
    pass
```

### ✅ Polimorfismo senza type checking
```python
# BUONO - lavora con qualunque Forma
def print_forme(forme):
    for f in forme:
        print(f.area())  # Funziona per tutti!

# CATTIVO - type checking
def print_forme(forme):
    for f in forme:
        if isinstance(f, Cerchio):
            print(f.area())
        elif isinstance(f, Rettangolo):
            print(f.area())
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare @abstractmethod
```python
# SBAGLIATO - puoi istanziare Forma!
class Forma(ABC):
    def area(self):  # Manca @abstractmethod
        pass

f = Forma()  # Funziona! Sbagliato

# GIUSTO
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

f = Forma()  # TypeError
```

### ❌ Errore 2: Non implementare metodo astratto
```python
# SBAGLIATO - manca implementazione
class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio
    # Manca area()!

c = Cerchio(5)  # TypeError: area() not implemented

# GIUSTO - implementa tutti i metodi astratti
class Cerchio(Forma):
    def area(self):
        return math.pi * self.raggio ** 2
```

### ❌ Errore 3: Usare type() invece di isinstance()
```python
# SBAGLIATO - non funziona con ereditarietà
q = Quadrato(5)
if type(q) == Rettangolo:  # False! Quadrato != Rettangolo
    pass

# GIUSTO - isinstance verifica anche ereditarietà
if isinstance(q, Rettangolo):  # True! Quadrato è-un Rettangolo
    pass
```

### ❌ Errore 4: Non validare in __init__
```python
# SBAGLIATO - valida in area()
class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio  # Potrebbe essere negativo!

    def area(self):
        if self.raggio < 0:
            raise ValueError()

# GIUSTO - valida in __init__
def __init__(self, raggio):
    if raggio <= 0:
        raise ValueError("Raggio > 0")
    self.raggio = raggio
```

### ❌ Errore 5: Erone mal implementato
```python
# SBAGLIATO - formula sbagliata
def area(self):
    s = self.perimetro() / 2
    return math.sqrt(s * (s-self.lato1) * (s-self.lato2))  # Manca lato3!

# GIUSTO
def area(self):
    s = self.perimetro() / 2
    return math.sqrt(s * (s-self.lato1) * (s-self.lato2) * (s-self.lato3))
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Ellisse
```python
class Ellisse(Forma):
    """Ellisse con due semiassi"""
    def __init__(self, semi_asse_a, semi_asse_b):
        if semi_asse_a <= 0 or semi_asse_b <= 0:
            raise ValueError("Semiassi positivi")
        self.a = semi_asse_a
        self.b = semi_asse_b

    def area(self):
        return math.pi * self.a * self.b

    def perimetro(self):
        # Approssimazione di Ramanujan
        h = ((self.a - self.b)**2) / ((self.a + self.b)**2)
        return math.pi * (self.a + self.b) * (1 + 3*h / (10 + math.sqrt(4 - 3*h)))

    def descrizione(self):
        return f"Ellisse {self.a}×{self.b}"
```

### 🌟 Sfida 2: Pentagono regolare
```python
class PentagonoRegolare(Forma):
    """Pentagono con 5 lati uguali"""
    def __init__(self, lato):
        if lato <= 0:
            raise ValueError("Lato > 0")
        self.lato = lato

    def area(self):
        return (self.lato**2 * math.sqrt(25 + 10*math.sqrt(5))) / 4

    def perimetro(self):
        return 5 * self.lato

    def descrizione(self):
        return f"Pentagono regolare lato={self.lato}"
```

### 🌟 Sfida 3: Forma 3D (volume)
```python
class Forma3D(ABC):
    """Classe astratta per forme 3D"""
    @abstractmethod
    def area_superficie(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Sfera(Forma3D):
    def __init__(self, raggio):
        self.raggio = raggio

    def area_superficie(self):
        return 4 * math.pi * self.raggio**2

    def volume(self):
        return 4/3 * math.pi * self.raggio**3
```

### 🌟 Sfida 4: Trasformazioni geometriche
```python
class Forma(ABC):
    # ... metodi originali ...

    def scala(self, fattore):
        """Scala la forma"""
        raise NotImplementedError()

    def ruota(self, gradi):
        """Ruota la forma"""
        raise NotImplementedError()

class Cerchio(Forma):
    def scala(self, fattore):
        self.raggio *= fattore

    def ruota(self, gradi):
        pass  # Un cerchio ruotato è identico
```

### 🌟 Sfida 5: Forma con colore
```python
class Forma(ABC):
    def __init__(self, colore="rosso"):
        self.colore = colore

    # ... metodi astratti ...

    def cambia_colore(self, nuovo_colore):
        self.colore = nuovo_colore

# Tutte le sottoclassi ereditano colore!
c = Cerchio(5, colore="blu")
c.cambia_colore("verde")
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **ABC** | Abstract Base Class | from abc import ABC |
| **@abstractmethod** | Metodo che deve essere implementato | @abstractmethod def area() |
| **Contratto** | Interfaccia garantita | Tutte le forme hanno area() |
| **Polimorfismo** | Stesso metodo, comportamento diverso | f.area() su qualunque forma |
| **isinstance()** | Verifica tipo incluso ereditarietà | isinstance(q, Rettangolo) |
| **Specializzazione** | Sottoclasse di sottoclasse | Quadrato(Rettangolo) |
| **Erone** | Formula area triangolo | √(s(s-a)(s-b)(s-c)) |

---

## 🔗 Link Utili

### Documentazione
- [Python ABC Module](https://docs.python.org/3/library/abc.html)
- [Abstract Base Classes](https://docs.python.org/3/glossary.html#term-abstract-base-class)
- [Geometric Formulas](https://en.wikipedia.org/wiki/Heron%27s_formula)

### Tutorial
- [Real Python - ABC](https://realpython.com/python-abc/)
- [Polymorphism in Python](https://www.geeksforgeeks.org/polymorphism-in-python/)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Osserva come è definita la classe astratta
- Guarda come sono implementati i metodi astratti
- Nota come funziona il polimorfismo
- Apprendi i pattern di specializzazione

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho importato ABC e abstractmethod
- [ ] Ho creato classe astratta `Forma`
- [ ] Ho definito metodi astratti: area(), perimetro(), descrizione()
- [ ] Non riesco a istanziare Forma (TypeError)
- [ ] Ho implementato `Cerchio` con area e perimetro corretti
- [ ] Ho implementato `Rettangolo` con area e perimetro corretti
- [ ] Ho implementato `Triangolo` con formula di Erone
- [ ] Ho validato triangolo (diseguaglianza triangolare)
- [ ] Ho implementato `Quadrato` come specializzazione
- [ ] Ho implementato funzioni polimorfiche (area_totale, ecc.)
- [ ] area_totale funziona su collezione eterogenea
- [ ] perimetro_massimo ritorna forma corretta
- [ ] classifica_per_area ordina correttamente
- [ ] Ho testato con almeno 12 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai padroneggiato le classi astratte! 🎉📐**

*"Le classi astratte permettono di definire contratti e forzare implementazioni, rendendo il codice più robusto e manutenibile!"*
