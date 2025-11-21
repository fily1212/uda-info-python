# Es6: Ereditarietà - Gli Animali dello Zoo

## 📊 Informazioni Generali

**Livello:** 🟡 INTERMEDIO
**Durata stimata:** 4-5 ore
**Prerequisiti:** Es1-5 completati, classi con metodi e getter/setter

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Creare** una classe base (superclasse) con attributi e metodi comuni
- ✅ **Ereditare** da una classe base usando `class Figlio(Base):`
- ✅ **Definire** attributi comuni a tutte le sottoclassi
- ✅ **Override** dei metodi per comportamenti specifici
- ✅ **Usare** `super()` per richiamare i metodi della classe base
- ✅ **Progettare** gerarchie di classi logiche e riutilizzabili
- ✅ **Applicare** l'ereditarietà a problemi reali

**Concetti fondamentali:**
- Classe base (superclasse/parent class)
- Sottoclasse (derived class/child class)
- Override (sovrascrittura di metodi)
- Polimorfismo (stesso metodo, comportamenti diversi)
- Relazione "is-a" (il Cane *è un* Animale)

---

## 📖 Descrizione

Finora hai creato classi indipendenti. Ma spesso scoprirai che molte classi condividono codice comune. Ad esempio:

```
Cane, Gatto, Uccello, Pesce → Tutti sono Animali!
  ↓
  Hanno attributi comuni: nome, età, peso
  Hanno metodi comuni: mangia(), dormi(), info()
  Ma comportamenti specifici: abbaia(), miagola(), vola()
```

L'**ereditarietà** ti permette di:
1. **Scrivere una volta** il codice comune (classe `Animale`)
2. **Riutilizzarlo** in sottoclassi specifiche (`Cane`, `Gatto`, `Uccello`)
3. **Specializzare** il comportamento dove serve

Questo esercizio crea uno **zoo virtuale** dove:
- `Animale` è la classe base con metodi comuni
- `Cane`, `Gatto`, `Uccello` ereditano da `Animale`
- Ogni animale ha il suo verso caratteristico
- Lo zoo contiene una lista di animali che fanno cose diverse

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Base Animale

**Definisci una classe `Animale` con:**

1. **Attributi:**
   - `nome` (str) - nome dell'animale
   - `eta` (int) - anni di vita
   - `peso` (float) - kilogrammi
   - `specie` (str) - tipo di animale (privato con default in costruttore)

2. **Metodi:**
   - `__init__(nome, eta, peso)` - costruttore
   - `mangia()` - stampa "Animale {nome} sta mangiando"
   - `dormi()` - stampa "Animale {nome} sta dormendo"
   - `info()` - ritorna stringa con nome, eta, peso
   - `invecchia()` - incrementa eta di 1
   - `cresce(kg)` - aumenta peso di kg

### Parte 2: Sottoclassi - Gli Animali

**Crea tre sottoclassi che ereditano da `Animale`:**

#### 2a. Classe `Cane(Animale)`
- **Attributo aggiuntivo:** `razza` (str)
- **Metodi:**
  - `__init__(nome, eta, peso, razza)` - usa `super().__init__(...)` per gli attributi della classe base
  - `abbaia()` - stampa "BBBAU BBBAU!"
  - `info()` - override: ritorna info base + razza

#### 2b. Classe `Gatto(Animale)`
- **Attributo aggiuntivo:** `colore` (str)
- **Metodi:**
  - `__init__(nome, eta, peso, colore)` - usa `super().__init__(...)`
  - `miagola()` - stampa "Miao miao miao!"
  - `info()` - override: ritorna info base + colore

#### 2c. Classe `Uccello(Animale)`
- **Attributo aggiuntivo:** `apertura_ali` (float, in cm)
- **Metodi:**
  - `__init__(nome, eta, peso, apertura_ali)` - usa `super().__init__(...)`
  - `vola()` - stampa "L'uccello sta volando in cielo!"
  - `canta()` - stampa "Cip cip cip!" (o melodia a scelta)
  - `info()` - override: ritorna info base + apertura ali

### Parte 3: La Classe Zoo

**Definisci una classe `Zoo` con:**

1. **Attributi:**
   - `nome` (str) - nome dello zoo
   - `animali` (lista) - contiene gli animali dello zoo
   - `budget` (float) - soldi disponibili

2. **Metodi:**
   - `aggiungi_animale(animale)` - aggiunge un animale alla lista
   - `rimuovi_animale(nome)` - rimuove un animale per nome
   - `numero_animali()` - ritorna quanti animali ci sono
   - `tutti_dormono()` - tutti gli animali dormono (chiama dormi() per ognuno)
   - `tutti_mangiano()` - tutti gli animali mangiano (chiama mangia() per ognuno)
   - `elenca_animali()` - stampa info di tutti gli animali
   - `animali_per_tipo(tipo)` - ritorna lista di animali di quel tipo (es: "Cane")
   - `cani_abbaiano()` - solo i cani abbaiano
   - `gatti_miagolano()` - solo i gatti miagolano
   - `uccelli_volano()` - solo gli uccelli volano
   - `spettacolo()` - tutti gli animali fanno il loro verso caratteristico

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSI ============

class Animale:
    """Classe base per tutti gli animali"""

    def __init__(self, nome, eta, peso):
        self.nome = nome
        self.eta = eta
        self.peso = peso

    def mangia(self):
        print(f"Animale {self.nome} sta mangiando")

    def dormi(self):
        print(f"Animale {self.nome} sta dormendo")

    def info(self):
        return f"{self.nome}, {self.eta} anni, {self.peso} kg"

    def invecchia(self):
        self.eta += 1
        print(f"{self.nome} è invecchiato. Ora ha {self.eta} anni")

    def cresce(self, kg):
        self.peso += kg
        print(f"{self.nome} è cresciuto di {kg} kg. Ora pesa {self.peso} kg")


class Cane(Animale):
    """Un cane - sottoclasse di Animale"""

    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, eta, peso)  # Chiama il costruttore della classe base
        self.razza = razza

    def abbaia(self):
        print(f"{self.nome} abbaia: BBBAU BBBAU!")

    def info(self):
        return f"{super().info()} - Cane ({self.razza})"


class Gatto(Animale):
    """Un gatto - sottoclasse di Animale"""

    def __init__(self, nome, eta, peso, colore):
        super().__init__(nome, eta, peso)
        self.colore = colore

    def miagola(self):
        print(f"{self.nome} miagola: Miao miao miao!")

    def info(self):
        return f"{super().info()} - Gatto ({self.colore})"


class Uccello(Animale):
    """Un uccello - sottoclasse di Animale"""

    def __init__(self, nome, eta, peso, apertura_ali):
        super().__init__(nome, eta, peso)
        self.apertura_ali = apertura_ali

    def vola(self):
        print(f"{self.nome} sta volando in cielo!")

    def canta(self):
        print(f"{self.nome} canta: Cip cip cip!")

    def info(self):
        return f"{super().info()} - Uccello (ali: {self.apertura_ali} cm)"


class Zoo:
    """Uno zoo con molti animali"""

    def __init__(self, nome, budget=10000):
        self.nome = nome
        self.animali = []
        self.budget = budget

    def aggiungi_animale(self, animale):
        self.animali.append(animale)
        print(f"Aggiunto {animale.nome} allo zoo {self.nome}")

    def rimuovi_animale(self, nome):
        self.animali = [a for a in self.animali if a.nome != nome]
        print(f"Rimosso {nome} dallo zoo")

    def numero_animali(self):
        return len(self.animali)

    def tutti_mangiano(self):
        print("\n=== Ora della Pappa ===")
        for animale in self.animali:
            animale.mangia()

    def tutti_dormono(self):
        print("\n=== Ora della Nanna ===")
        for animale in self.animali:
            animale.dormi()

    def elenca_animali(self):
        print(f"\n=== Animali del {self.nome} ===")
        for animale in self.animali:
            print(f"  - {animale.info()}")

    def animali_per_tipo(self, tipo):
        """Ritorna lista di animali di un tipo specifico"""
        return [a for a in self.animali if type(a).__name__ == tipo]

    def cani_abbaiano(self):
        print("\n=== I Cani Abbaiano ===")
        for animale in self.animali_per_tipo("Cane"):
            animale.abbaia()

    def gatti_miagolano(self):
        print("\n=== I Gatti Miagolano ===")
        for animale in self.animali_per_tipo("Gatto"):
            animale.miagola()

    def uccelli_volano(self):
        print("\n=== Gli Uccelli Volano ===")
        for animale in self.animali_per_tipo("Uccello"):
            animale.vola()

    def spettacolo(self):
        """Tutti gli animali fanno il loro verso!"""
        print(f"\n=== GRANDE SPETTACOLO AL {self.nome.upper()} ===")
        self.cani_abbaiano()
        self.gatti_miagolano()
        self.uccelli_volano()
        print(f"\nSpettacolo terminato! Grazie per la visita al {self.nome}!\n")


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    # Creare lo zoo
    zoo = Zoo("Zoo Italia", budget=50000)

    # Creare gli animali
    cane1 = Cane("Rex", 5, 30, "Pastore Tedesco")
    cane2 = Cane("Fido", 3, 15, "Barboncino")

    gatto1 = Gatto("Micia", 4, 4.5, "Grigio")
    gatto2 = Gatto("Fluffy", 2, 3.8, "Bianco")

    uccello1 = Uccello("Pippo", 1, 0.2, 25)
    uccello2 = Uccello("Cip", 2, 0.15, 20)

    # Aggiungere animali allo zoo
    for animale in [cane1, cane2, gatto1, gatto2, uccello1, uccello2]:
        zoo.aggiungi_animale(animale)

    # Mostrare gli animali
    zoo.elenca_animali()
    print(f"\nTotale animali: {zoo.numero_animali()}")

    # Test metodi comuni
    print("\n=== TEST METODI COMUNI ===")
    zoo.tutti_mangiano()
    zoo.tutti_dormono()

    # Test metodi specifici
    zoo.spettacolo()

    # Test animali per tipo
    print("=== CANI NELLO ZOO ===")
    for cane in zoo.animali_per_tipo("Cane"):
        print(f"  - {cane.info()}")

    # Test invecchiamento e crescita
    print("\n=== CAMBIO NEL TEMPO ===")
    cane1.invecchia()
    cane1.cresce(2)
    print(f"Info aggiornata: {cane1.info()}")

    # Output atteso:
    # Aggiunto Rex allo zoo Zoo Italia
    # Aggiunto Fido allo zoo Zoo Italia
    # ...
    # === Animali del Zoo Italia ===
    #   - Rex, 5 anni, 30 kg - Cane (Pastore Tedesco)
    # ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione animali
```python
animale = Animale("Generico", 3, 10)
assert animale.nome == "Generico"
assert animale.eta == 3
assert animale.peso == 10
print("✓ Test 1 passato")
```

### Test 2: Ereditarietà - Cane
```python
cane = Cane("Rex", 5, 30, "Pastore Tedesco")
assert cane.nome == "Rex"
assert cane.eta == 5
assert cane.peso == 30
assert cane.razza == "Pastore Tedesco"
assert "Cane" in cane.info()
print("✓ Test 2 passato")
```

### Test 3: Ereditarietà - Gatto
```python
gatto = Gatto("Micia", 4, 4.5, "Grigio")
assert gatto.nome == "Micia"
assert gatto.colore == "Grigio"
assert "Gatto" in gatto.info()
print("✓ Test 3 passato")
```

### Test 4: Ereditarietà - Uccello
```python
uccello = Uccello("Pippo", 1, 0.2, 25)
assert uccello.nome == "Pippo"
assert uccello.apertura_ali == 25
assert "Uccello" in uccello.info()
print("✓ Test 4 passato")
```

### Test 5: Metodi comuni (invecchia)
```python
cane = Cane("Rex", 5, 30, "Pastore")
cane.invecchia()
assert cane.eta == 6
cane.invecchia()
assert cane.eta == 7
print("✓ Test 5 passato")
```

### Test 6: Metodi comuni (cresce)
```python
cane = Cane("Rex", 5, 30, "Pastore")
cane.cresce(5)
assert cane.peso == 35
cane.cresce(-2)  # Può anche dimagrire
assert cane.peso == 33
print("✓ Test 6 passato")
```

### Test 7: Zoo - aggiunta e rimozione
```python
zoo = Zoo("Zoo Test")
cane = Cane("Rex", 5, 30, "Pastore")
gatto = Gatto("Micia", 4, 4.5, "Grigio")

zoo.aggiungi_animale(cane)
zoo.aggiungi_animale(gatto)
assert zoo.numero_animali() == 2

zoo.rimuovi_animale("Rex")
assert zoo.numero_animali() == 1
print("✓ Test 7 passato")
```

### Test 8: Zoo - animali per tipo
```python
zoo = Zoo("Zoo Test")
cane1 = Cane("Rex", 5, 30, "Pastore")
cane2 = Cane("Fido", 3, 15, "Barboncino")
gatto = Gatto("Micia", 4, 4.5, "Grigio")

zoo.aggiungi_animale(cane1)
zoo.aggiungi_animale(cane2)
zoo.aggiungi_animale(gatto)

cani = zoo.animali_per_tipo("Cane")
assert len(cani) == 2
assert cani[0].nome == "Rex"

gatti = zoo.animali_per_tipo("Gatto")
assert len(gatti) == 1
print("✓ Test 8 passato")
```

### Test 9: Override di metodi
```python
cane = Cane("Rex", 5, 30, "Pastore")
gatto = Gatto("Micia", 4, 4.5, "Grigio")
uccello = Uccello("Pippo", 1, 0.2, 25)

info_cane = cane.info()
info_gatto = gatto.info()
info_uccello = uccello.info()

assert "Cane" in info_cane
assert "Gatto" in info_gatto
assert "Uccello" in info_uccello
assert "Pastore" in info_cane
assert "Grigio" in info_gatto
print("✓ Test 9 passato")
```

### Test 10: Polimorfismo
```python
# Tutti gli animali possono essere in una lista
animali = [
    Cane("Rex", 5, 30, "Pastore"),
    Gatto("Micia", 4, 4.5, "Grigio"),
    Uccello("Pippo", 1, 0.2, 25)
]

# Tutti hanno i metodi comuni
for animale in animali:
    animale.mangia()  # Lavora per tutti!
    assert hasattr(animale, "dormi")
    assert hasattr(animale, "invecchia")

print("✓ Test 10 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Crea la classe base Animale
```python
class Animale:
    def __init__(self, nome, eta, peso):
        self.nome = nome
        self.eta = eta
        self.peso = peso

    def mangia(self):
        print(f"{self.nome} sta mangiando")

    def dormi(self):
        print(f"{self.nome} sta dormendo")

    def info(self):
        return f"{self.nome}, {self.eta} anni, {self.peso} kg"
```

### Passo 2: Aggiungi metodi comuni in Animale
```python
def invecchia(self):
    self.eta += 1
    print(f"{self.nome} è invecchiato di 1 anno")

def cresce(self, kg):
    self.peso += kg
    print(f"{self.nome} è cresciuto di {kg} kg")
```

### Passo 3: Crea la prima sottoclasse - Cane
```python
class Cane(Animale):  # Eredita da Animale
    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, eta, peso)  # Chiama il costruttore della classe base
        self.razza = razza

    def abbaia(self):
        print(f"{self.nome} abbaia: BBBAU BBBAU!")

    def info(self):
        # Chiama il metodo info della classe base e aggiungi il tuo
        return f"{super().info()} - Cane ({self.razza})"
```

### Passo 4: Crea le altre sottoclassi - Gatto e Uccello
Stessa logica del Cane, ma con attributi e metodi specifici.

### Passo 5: Crea la classe Zoo
```python
class Zoo:
    def __init__(self, nome, budget=10000):
        self.nome = nome
        self.animali = []
        self.budget = budget

    def aggiungi_animale(self, animale):
        self.animali.append(animale)

    def numero_animali(self):
        return len(self.animali)
```

### Passo 6: Aggiungi metodi di comportamento al Zoo
```python
def tutti_mangiano(self):
    for animale in self.animali:
        animale.mangia()

def tutti_dormono(self):
    for animale in self.animali:
        animale.dormi()

def elenca_animali(self):
    for animale in self.animali:
        print(animale.info())
```

### Passo 7: Aggiungi metodi specifici al Zoo
```python
def animali_per_tipo(self, tipo):
    return [a for a in self.animali if type(a).__name__ == tipo]

def cani_abbaiano(self):
    for cane in self.animali_per_tipo("Cane"):
        cane.abbaia()

def gatti_miagolano(self):
    for gatto in self.animali_per_tipo("Gatto"):
        gatto.miagola()

def uccelli_volano(self):
    for uccello in self.animali_per_tipo("Uccello"):
        uccello.vola()
```

### Passo 8: Testa il codice
```python
zoo = Zoo("Zoo Italia")
zoo.aggiungi_animale(Cane("Rex", 5, 30, "Pastore"))
zoo.aggiungi_animale(Gatto("Micia", 4, 4.5, "Grigio"))
zoo.aggiungi_animale(Uccello("Pippo", 1, 0.2, 25))

zoo.elenca_animali()
zoo.spettacolo()
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa `super()` per accedere ai metodi della classe base
```python
class Cane(Animale):
    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, eta, peso)  # Buono!
        self.razza = razza

    def info(self):
        return f"{super().info()} - Cane ({self.razza})"
```

### ✅ Non ripetere il codice - usa l'ereditarietà!
```python
# CATTIVO - ripetizione
class Cane:
    def __init__(self, nome, eta, peso, razza):
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.razza = razza

# BUONO - ereditarietà
class Cane(Animale):
    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, eta, peso)
        self.razza = razza
```

### ✅ Override significa "specializzare", non "eliminare"
```python
# BUONO - specializza il metodo
class Cane(Animale):
    def info(self):
        # Usa la classe base E aggiungi informazioni specifiche
        return f"{super().info()} - Cane ({self.razza})"

# CATTIVO - ignora completamente la classe base
class Cane(Animale):
    def info(self):
        return f"{self.razza}"  # Perdi informazioni!
```

### ✅ Verifica il tipo di un oggetto con `isinstance()`
```python
cane = Cane("Rex", 5, 30, "Pastore")
print(isinstance(cane, Cane))     # True
print(isinstance(cane, Animale))  # True (eredita da Animale!)
print(isinstance(cane, Gatto))    # False
```

### ✅ Ottieni il tipo con `type().__name__`
```python
cane = Cane("Rex", 5, 30, "Pastore")
print(type(cane).__name__)  # "Cane"

# Utile nel Zoo
def animali_per_tipo(self, tipo):
    return [a for a in self.animali if type(a).__name__ == tipo]
```

### ✅ Crea un metodo factory per creare animali
```python
class Zoo:
    def crea_cane(self, nome, eta, peso, razza):
        cane = Cane(nome, eta, peso, razza)
        self.aggiungi_animale(cane)
        return cane
```

### ✅ Documenta la gerarchia
```python
"""
Gerarchia di ereditarietà:

        Animale (classe base)
           /   |   \
          /    |    \
       Cane  Gatto  Uccello (sottoclassi)

Animale definisce:
  - Attributi comuni: nome, eta, peso
  - Metodi comuni: mangia(), dormi(), info(), invecchia(), cresce()

Cane aggiunge:
  - Attributo: razza
  - Metodo: abbaia()

Gatto aggiunge:
  - Attributo: colore
  - Metodo: miagola()

Uccello aggiunge:
  - Attributo: apertura_ali
  - Metodi: vola(), canta()
"""
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare `super().__init__()` nel costruttore
```python
# SBAGLIATO - attributi della classe base non vengono inizializzati
class Cane(Animale):
    def __init__(self, nome, eta, peso, razza):
        self.razza = razza  # Dimentica super!
        # Risultato: self.nome, self.eta, self.peso non esistono!

# GIUSTO
class Cane(Animale):
    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, eta, peso)  # Sempre prima!
        self.razza = razza
```

### ❌ Errore 2: Non fare override correttamente
```python
# SBAGLIATO - non chiama il metodo della classe base
class Cane(Animale):
    def info(self):
        return f"{self.razza}"  # Perde info della classe base!

# GIUSTO - usa super() per includerlo
class Cane(Animale):
    def info(self):
        return f"{super().info()} - Cane ({self.razza})"
```

### ❌ Errore 3: Confondere ereditarietà con composizione
```python
# SBAGLIATO - composizione quando dovrebbe essere ereditarietà
class Cane:
    def __init__(self, nome):
        self.animale = Animale(nome)  # Non è ereditarietà!
        self.razza = "Pastore"

# GIUSTO - ereditarietà
class Cane(Animale):
    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, eta, peso)
        self.razza = razza
```

### ❌ Errore 4: Accedere a `self` senza inizializzare gli attributi
```python
# SBAGLIATO
class Gatto(Animale):
    def miagola(self):
        print(f"{self.colore} miagola")  # self.colore potrebbe non esistere!

# GIUSTO - assicurati che il costruttore sia chiamato
class Gatto(Animale):
    def __init__(self, nome, eta, peso, colore):
        super().__init__(nome, eta, peso)
        self.colore = colore  # Inizializza prima di usare!
```

### ❌ Errore 5: Usare `type()` quando vuoi il nome
```python
# MEDIOCRE
cane = Cane("Rex", 5, 30, "Pastore")
print(type(cane))  # <class '__main__.Cane'>

# MIGLIORE
print(type(cane).__name__)  # "Cane"
print(type(cane).__name__ == "Cane")  # True per confronti
```

### ❌ Errore 6: Gerarchia di ereditarietà troppo profonda
```python
# MEDIOCRE - troppi livelli
class Animale: pass
class Vertebrato(Animale): pass
class Mammifero(Vertebrato): pass
class Carnivoro(Mammifero): pass
class Cane(Carnivoro): pass  # Troppi livelli!

# MIGLIORE - semplice
class Animale: pass
class Cane(Animale): pass
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Aggiungi Altre Specie di Animali
```python
class Pesce(Animale):
    def __init__(self, nome, eta, peso, tipo_pesce):
        super().__init__(nome, eta, peso)
        self.tipo_pesce = tipo_pesce

    def nuota(self):
        print(f"{self.nome} sta nuotando sott'acqua!")

class Elefante(Animale):
    def __init__(self, nome, eta, peso, lunghezza_proboscide):
        super().__init__(nome, eta, peso)
        self.lunghezza_proboscide = lunghezza_proboscide

    def sputa_acqua(self):
        print(f"{self.nome} sputa acqua con la proboscide!")
```

### 🌟 Sfida 2: Metodo `verso()` Polimorfo
Crea un metodo `verso()` nella classe base Animale che ritorna il verso specifico:

```python
class Animale:
    def verso(self):
        """Sovrascritto in ogni sottoclasse"""
        return "..."

class Cane(Animale):
    def verso(self):
        return "BBBAU BBBAU!"

class Gatto(Animale):
    def verso(self):
        return "Miao miao miao!"

# Nel Zoo:
def tutti_verso(self):
    for animale in self.animali:
        print(f"{animale.nome}: {animale.verso()}")
```

### 🌟 Sfida 3: Statistiche dello Zoo
```python
class Zoo:
    def eta_media_animali(self):
        if not self.animali:
            return 0
        return sum(a.eta for a in self.animali) / len(self.animali)

    def peso_totale_animali(self):
        return sum(a.peso for a in self.animali)

    def animale_piu_vecchio(self):
        if not self.animali:
            return None
        return max(self.animali, key=lambda a: a.eta)

    def animale_piu_pesante(self):
        if not self.animali:
            return None
        return max(self.animali, key=lambda a: a.peso)

    def numero_cani(self):
        return len(self.animali_per_tipo("Cane"))

    def numero_gatti(self):
        return len(self.animali_per_tipo("Gatto"))

    def numero_uccelli(self):
        return len(self.animali_per_tipo("Uccello"))
```

### 🌟 Sfida 4: Alimentazione Specifica
```python
class Animale:
    def mangia(self):
        return self.cibo_preferito()

    def cibo_preferito(self):
        """Sovrascritto in ogni sottoclasse"""
        return "cibo generico"

class Cane(Animale):
    def cibo_preferito(self):
        return "croquette"

class Gatto(Animale):
    def cibo_preferito(self):
        return "pesce"

class Uccello(Animale):
    def cibo_preferito(self):
        return "semi"

# Nel Zoo:
def elenca_alimentazione(self):
    for animale in self.animali:
        print(f"{animale.nome} mangia {animale.cibo_preferito()}")
```

### 🌟 Sfida 5: Habitat e Comfort
```python
class Animale:
    def __init__(self, nome, eta, peso, habitat):
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.habitat = habitat

    def habitat_ideale(self):
        """Sovrascritto in ogni sottoclasse"""
        return self.habitat

class Cane(Animale):
    def habitat_ideale(self):
        return "parco/casa"

class Gatto(Animale):
    def habitat_ideale(self):
        return "casa"

class Uccello(Animale):
    def habitat_ideale(self):
        return "voliera/albero"

# Nel Zoo:
def verifica_habitat(self):
    for animale in self.animali:
        match = animale.habitat == animale.habitat_ideale()
        status = "✓" if match else "✗"
        print(f"{status} {animale.nome}: {animale.habitat} (ideale: {animale.habitat_ideale()})")
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Ereditarietà** | Una classe eredita da un'altra | `class Cane(Animale):` |
| **Classe Base** | La classe da cui si eredita | `class Animale:` |
| **Sottoclasse** | La classe che eredita | `class Cane(Animale):` |
| **super()** | Accede ai metodi della classe base | `super().__init__(...)` |
| **Override** | Sovrascrittura di metodo | `def info(self): return super().info() + "extra"` |
| **Polimorfismo** | Stesso metodo, comportamenti diversi | `cane.verso() != gatto.verso()` |
| **isinstance()** | Verifica se è istanza di una classe | `isinstance(cane, Cane)` |
| **Relazione is-a** | Una sottoclasse *è un* tipo di classe base | `Cane is-a Animale` |

---

## 🔗 Link Utili

### Documentazione
- [Python Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [super() function](https://docs.python.org/3/library/functions.html#super)
- [isinstance() function](https://docs.python.org/3/library/functions.html#isinstance)

### Tutorial
- [Real Python - Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- [Real Python - super()](https://realpython.com/python-super/)
- [OOP in Python - Inheritance](https://www.geeksforgeeks.org/inheritance-in-python/)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Guarda come è strutturata la gerarchia di ereditarietà
- Nota come vengono usati super() e override
- Osserva come il Zoo gestisce animali di tipi diversi
- Apprendi dai pattern di polimorfismo

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho creato la classe base `Animale` con attributi comuni
- [ ] Ho creato sottoclassi `Cane`, `Gatto`, `Uccello`
- [ ] Ogni sottoclasse usa `super().__init__()` nel costruttore
- [ ] Ho aggiunto attributi specifici a ogni sottoclasse
- [ ] Ho implementato metodi specifici (abbaia, miagola, vola)
- [ ] Ho fatto override del metodo `info()` in ogni sottoclasse
- [ ] Ho creato la classe `Zoo` con lista di animali
- [ ] Il Zoo può aggiungere e rimuovere animali
- [ ] Il Zoo può fare attività comuni (mangia, dormi)
- [ ] Il Zoo può filtrare per tipo di animale
- [ ] Ho testato il polimorfismo (stessi metodi, comportamenti diversi)
- [ ] Ho testato con almeno 6 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai imparato l'ereditarietà! 🎉🦁**

*"L'ereditarietà è il modo di Python di dire: 'questi oggetti hanno molto in comune'"*
