# Es12: Property Decorator - Classe Temperatura

## 📊 Informazioni Generali

**Livello:** 🔴 AVANZATO
**Durata stimata:** 5-6 ore
**Prerequisiti:** Es1-11 completati, decorator, property

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Usare** il decorator @property per getter e setter
- ✅ **Implementare** conversioni automatiche tra scale di temperatura
- ✅ **Validare** i dati con setter personalizzati
- ✅ **Gestire** proprietà calcolate con @property
- ✅ **Capire** la differenza tra attributi e property
- ✅ **Applicare** encapsulation con underscore privato
- ✅ **Creare** interfacce fluide e intuitive

**Concetti fondamentali:**
- @property = getter (accesso lecito)
- @property.setter = setter (modifica controllata)
- Validazione nel setter
- Conversione tra scale: Celsius ↔ Fahrenheit ↔ Kelvin
- Attributi privati con _ prefisso
- Proprietà calcolate (sola lettura)

---

## 📖 Descrizione

La **temperatura** può essere espressa in tre scale:
- **Celsius (°C)**: scala comune, 0°C = punto di congelamento acqua
- **Fahrenheit (°F)**: scala USA, (C × 9/5) + 32
- **Kelvin (K)**: scala assoluta, C + 273.15, non può essere < 0

Questo esercizio crea una classe `Temperatura` che:
- Immagazzina il valore interno in **Celsius** (preferito)
- Fornisce accesso tramite @property in tutte e tre le scale
- Converte **automaticamente** tra scale
- **Valida** i valori (Kelvin ≥ 0, cioè ≥ -273.15°C)
- Permette modifica tramite @property.setter in qualsiasi scala
- Implementa metodi di confronto

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Temperatura Base

**Definisci una classe `Temperatura` con:**

1. **Attributo privato:**
   - `_celsius` (float) - valore interno in Celsius

2. **Costruttore:**
   - `__init__(valore=0, scala="celsius")` - accetta valore in qualunque scala
   - Valida il valore (Kelvin non può essere < 0)
   - Converte in Celsius internamente

### Parte 2: Properties per le Scale

**Implementa @property e @property.setter per:**

1. **`celsius`** - accesso in gradi Celsius
   - getter: ritorna _celsius
   - setter: valida e imposta _celsius

2. **`fahrenheit`** - accesso in gradi Fahrenheit
   - getter: converte Celsius a Fahrenheit
   - setter: converte Fahrenheit a Celsius e imposta

3. **`kelvin`** - accesso in Kelvin (scala assoluta)
   - getter: converte Celsius a Kelvin
   - setter: valida (>= 0), converte e imposta
   - **IMPORTANTE**: solleva ValueError se kelvin < 0

### Parte 3: Validazione e Conversione

**Implementa metodi privati:**

1. **`_valida_temperatura(valore, scala)`** - valida il valore
   - Kelvin deve essere >= 0
   - Celsius deve essere >= -273.15
   - Fahrenheit deve essere >= -459.67

2. **`_celsius_da_fahrenheit(f)`** - conversione F→C
3. **`_celsius_da_kelvin(k)`** - conversione K→C
4. **`_fahrenheit_da_celsius(c)`** - conversione C→F
5. **`_kelvin_da_celsius(c)`** - conversione C→K

### Parte 4: Metodi di Confronto

1. **`è_piu_calda_di(altra)`** - True se self > altra
2. **`è_piu_fredda_di(altra)`** - True se self < altra
3. **`è_uguale_a(altra)`** - True se self == altra (con tolleranza)
4. **Implementa `__eq__`, `__lt__`, `__gt__`, `__le__`, `__ge__`**

### Parte 5: Rappresentazione

1. **`__str__()`** - output leggibile
   - "20.0°C" o "68.0°F" (a seconda della scala di default)

2. **`__repr__()`** - output tecnico
   - "Temperatura(20.0, 'celsius')"

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSE ============

class Temperatura:
    """Una temperatura con conversione automatica tra scale"""

    def __init__(self, valore=0, scala="celsius"):
        """Inizializza la temperatura in qualunque scala"""
        self._scala_default = scala
        self._celsius = 0

        # Usa il setter appropriato per convertire e validare
        if scala.lower() == "celsius":
            self.celsius = valore
        elif scala.lower() == "fahrenheit":
            self.fahrenheit = valore
        elif scala.lower() == "kelvin":
            self.kelvin = valore
        else:
            raise ValueError(f"Scala sconosciuta: {scala}")

    # ===== VALIDAZIONE =====

    def _valida_temperatura(self, valore, scala):
        """Valida una temperatura in una scala"""
        scala = scala.lower()
        if scala == "kelvin":
            if valore < 0:
                raise ValueError(f"Kelvin non può essere negativo: {valore} K")
        elif scala == "celsius":
            if valore < -273.15:
                raise ValueError(f"Temperatura sotto zero assoluto: {valore}°C")
        elif scala == "fahrenheit":
            if valore < -459.67:
                raise ValueError(f"Temperatura sotto zero assoluto: {valore}°F")
        else:
            raise ValueError(f"Scala sconosciuta: {scala}")

    # ===== CONVERSIONI PRIVATE =====

    @staticmethod
    def _celsius_da_fahrenheit(fahrenheit):
        """Converte Fahrenheit a Celsius"""
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def _celsius_da_kelvin(kelvin):
        """Converte Kelvin a Celsius"""
        return kelvin - 273.15

    @staticmethod
    def _fahrenheit_da_celsius(celsius):
        """Converte Celsius a Fahrenheit"""
        return celsius * 9 / 5 + 32

    @staticmethod
    def _kelvin_da_celsius(celsius):
        """Converte Celsius a Kelvin"""
        return celsius + 273.15

    # ===== PROPERTY CELSIUS =====

    @property
    def celsius(self):
        """Accesso in gradi Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, valore):
        """Imposta la temperatura in gradi Celsius"""
        self._valida_temperatura(valore, "celsius")
        self._celsius = float(valore)

    # ===== PROPERTY FAHRENHEIT =====

    @property
    def fahrenheit(self):
        """Accesso in gradi Fahrenheit"""
        return self._fahrenheit_da_celsius(self._celsius)

    @fahrenheit.setter
    def fahrenheit(self, valore):
        """Imposta la temperatura in gradi Fahrenheit"""
        self._valida_temperatura(valore, "fahrenheit")
        self._celsius = self._celsius_da_fahrenheit(valore)

    # ===== PROPERTY KELVIN =====

    @property
    def kelvin(self):
        """Accesso in Kelvin (scala assoluta)"""
        return self._kelvin_da_celsius(self._celsius)

    @kelvin.setter
    def kelvin(self, valore):
        """Imposta la temperatura in Kelvin"""
        self._valida_temperatura(valore, "kelvin")
        self._celsius = self._celsius_da_kelvin(valore)

    # ===== RAPPRESENTAZIONE =====

    def __str__(self):
        """Rappresentazione leggibile"""
        if self._scala_default.lower() == "fahrenheit":
            return f"{self.fahrenheit:.1f}°F"
        elif self._scala_default.lower() == "kelvin":
            return f"{self.kelvin:.1f} K"
        else:
            return f"{self.celsius:.1f}°C"

    def __repr__(self):
        """Rappresentazione tecnica"""
        return f"Temperatura({self._celsius:.2f}, 'celsius')"

    # ===== COMPARAZIONI =====

    def __eq__(self, altra):
        """Uguaglianza (tolleranza 0.01)"""
        if not isinstance(altra, Temperatura):
            return NotImplemented
        return abs(self._celsius - altra._celsius) < 0.01

    def __lt__(self, altra):
        """Minore (più fredda)"""
        if not isinstance(altra, Temperatura):
            return NotImplemented
        return self._celsius < altra._celsius

    def __le__(self, altra):
        """Minore o uguale"""
        if not isinstance(altra, Temperatura):
            return NotImplemented
        return self._celsius <= altra._celsius

    def __gt__(self, altra):
        """Maggiore (più calda)"""
        if not isinstance(altra, Temperatura):
            return NotImplemented
        return self._celsius > altra._celsius

    def __ge__(self, altra):
        """Maggiore o uguale"""
        if not isinstance(altra, Temperatura):
            return NotImplemented
        return self._celsius >= altra._celsius

    def __ne__(self, altra):
        """Disuguaglianza"""
        if not isinstance(altra, Temperatura):
            return NotImplemented
        return not self.__eq__(altra)

    # ===== METODI DI CONFRONTO =====

    def è_piu_calda_di(self, altra):
        """True se questa temperatura è più alta"""
        if not isinstance(altra, Temperatura):
            raise TypeError("Deve essere una Temperatura")
        return self._celsius > altra._celsius

    def è_piu_fredda_di(self, altra):
        """True se questa temperatura è più bassa"""
        if not isinstance(altra, Temperatura):
            raise TypeError("Deve essere una Temperatura")
        return self._celsius < altra._celsius

    def è_uguale_a(self, altra):
        """True se le temperature sono uguali (tolleranza 0.01)"""
        if not isinstance(altra, Temperatura):
            raise TypeError("Deve essere una Temperatura")
        return abs(self._celsius - altra._celsius) < 0.01

    # ===== METODI UTILI =====

    def differenza(self, altra):
        """Differenza di temperatura in Celsius"""
        if not isinstance(altra, Temperatura):
            raise TypeError("Deve essere una Temperatura")
        return abs(self._celsius - altra._celsius)

    def converti_in(self, scala):
        """Ritorna il valore nella scala richiesta"""
        scala = scala.lower()
        if scala == "celsius":
            return self.celsius
        elif scala == "fahrenheit":
            return self.fahrenheit
        elif scala == "kelvin":
            return self.kelvin
        else:
            raise ValueError(f"Scala sconosciuta: {scala}")

    def copia(self):
        """Crea una copia di questa temperatura"""
        return Temperatura(self._celsius, "celsius")


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    print("=== CREAZIONE E CONVERSIONE ===")
    t1 = Temperatura(20, "celsius")
    print(f"t1 creata con 20°C: {t1}")
    print(f"In Fahrenheit: {t1.fahrenheit:.1f}°F")
    print(f"In Kelvin: {t1.kelvin:.1f} K")

    print("\n=== CREAZIONE CON DIVERSE SCALE ===")
    t2 = Temperatura(68, "fahrenheit")
    print(f"t2 creata con 68°F: {t2}")
    print(f"In Celsius: {t2.celsius:.1f}°C")
    print(f"In Kelvin: {t2.kelvin:.1f} K")

    t3 = Temperatura(293.15, "kelvin")
    print(f"t3 creata con 293.15 K: {t3}")

    print("\n=== MODIFICA CON PROPERTY SETTER ===")
    t = Temperatura(0, "celsius")
    print(f"Iniziale: {t}")

    t.celsius = 25
    print(f"Dopo t.celsius = 25: {t} (F: {t.fahrenheit:.1f}°F)")

    t.fahrenheit = 86
    print(f"Dopo t.fahrenheit = 86: {t} (C: {t.celsius:.1f}°C)")

    t.kelvin = 300
    print(f"Dopo t.kelvin = 300: {t}")

    print("\n=== COMPARAZIONI ===")
    t_freddo = Temperatura(-10, "celsius")
    t_caldo = Temperatura(30, "celsius")
    t_medio = Temperatura(20, "celsius")

    print(f"Freddo: {t_freddo}")
    print(f"Medio: {t_medio}")
    print(f"Caldo: {t_caldo}")

    print(f"\n{t_caldo} è più calda di {t_freddo}? {t_caldo.è_piu_calda_di(t_freddo)}")
    print(f"{t_freddo} è più fredda di {t_caldo}? {t_freddo.è_piu_fredda_di(t_caldo)}")
    print(f"{t_medio} è uguale a {Temperatura(20, 'celsius')}? {t_medio.è_uguale_a(Temperatura(20, 'celsius'))}")

    print("\n=== OPERATORI DI COMPARAZIONE ===")
    print(f"{t_caldo} > {t_freddo}: {t_caldo > t_freddo}")
    print(f"{t_freddo} < {t_caldo}: {t_freddo < t_caldo}")
    print(f"{t_medio} == {Temperatura(20, 'celsius')}: {t_medio == Temperatura(20, 'celsius')}")

    print("\n=== ORDINAMENTO ===")
    temperature = [
        Temperatura(30, "celsius"),
        Temperatura(10, "celsius"),
        Temperatura(20, "celsius"),
        Temperatura(0, "celsius")
    ]
    temperature_ordinate = sorted(temperature)
    print("Temperature ordinate (da fredda a calda):")
    for t in temperature_ordinate:
        print(f"  {t}")

    print("\n=== DIFFERENZA TRA TEMPERATURE ===")
    t1 = Temperatura(25, "celsius")
    t2 = Temperatura(10, "celsius")
    diff = t1.differenza(t2)
    print(f"Differenza tra {t1} e {t2}: {diff:.1f}°C")

    print("\n=== GESTIONE ERRORI ===")
    try:
        t_zero = Temperatura(-300, "kelvin")
    except ValueError as e:
        print(f"Errore atteso: {e}")

    try:
        t = Temperatura(20, "celsius")
        t.kelvin = -50  # Sotto zero assoluto
    except ValueError as e:
        print(f"Errore atteso: {e}")

    try:
        t = Temperatura(20, "scala_sconosciuta")
    except ValueError as e:
        print(f"Errore atteso: {e}")

    print("\n=== METODO CONVERTI_IN ===")
    t = Temperatura(100, "celsius")
    print(f"100°C in diverse scale:")
    print(f"  Celsius: {t.converti_in('celsius'):.1f}°C")
    print(f"  Fahrenheit: {t.converti_in('fahrenheit'):.1f}°F")
    print(f"  Kelvin: {t.converti_in('kelvin'):.1f} K")
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione in Celsius
```python
t = Temperatura(20, "celsius")
assert t.celsius == 20
assert abs(t.fahrenheit - 68.0) < 0.01
assert abs(t.kelvin - 293.15) < 0.01
print("✓ Test 1 passato")
```

### Test 2: Creazione in Fahrenheit
```python
t = Temperatura(32, "fahrenheit")
assert abs(t.celsius - 0.0) < 0.01  # Punto di congelamento acqua
assert abs(t.fahrenheit - 32.0) < 0.01
assert abs(t.kelvin - 273.15) < 0.01
print("✓ Test 2 passato")
```

### Test 3: Creazione in Kelvin
```python
t = Temperatura(273.15, "kelvin")
assert abs(t.celsius - 0.0) < 0.01
assert abs(t.fahrenheit - 32.0) < 0.01
assert abs(t.kelvin - 273.15) < 0.01
print("✓ Test 3 passato")
```

### Test 4: Setter Celsius
```python
t = Temperatura(0, "celsius")
t.celsius = 100  # Punto di ebollizione acqua
assert t.celsius == 100
assert abs(t.fahrenheit - 212.0) < 0.01
assert abs(t.kelvin - 373.15) < 0.01
print("✓ Test 4 passato")
```

### Test 5: Setter Fahrenheit
```python
t = Temperatura(0, "celsius")
t.fahrenheit = 98.6  # Temperatura corporea
assert abs(t.celsius - 37.0) < 0.1
assert abs(t.fahrenheit - 98.6) < 0.01
print("✓ Test 5 passato")
```

### Test 6: Setter Kelvin
```python
t = Temperatura(0, "celsius")
t.kelvin = 300  # ~27°C
assert abs(t.celsius - 26.85) < 0.1
assert abs(t.kelvin - 300.0) < 0.01
print("✓ Test 6 passato")
```

### Test 7: Validazione Kelvin (non negativo)
```python
try:
    t = Temperatura(-50, "kelvin")
    assert False  # Non dovrebbe arrivare qui
except ValueError:
    pass  # Atteso

try:
    t = Temperatura(0, "celsius")
    t.kelvin = -10  # Tenta di impostare negativo
    assert False
except ValueError:
    pass  # Atteso
print("✓ Test 7 passato")
```

### Test 8: Comparazioni
```python
t1 = Temperatura(20, "celsius")
t2 = Temperatura(25, "celsius")
t3 = Temperatura(20, "celsius")

assert t1 < t2
assert t2 > t1
assert t1 == t3
assert t1 <= t2
assert t2 >= t1
assert t1 != t2
print("✓ Test 8 passato")
```

### Test 9: Metodi di confronto
```python
t_caldo = Temperatura(30, "celsius")
t_freddo = Temperatura(10, "celsius")
t_uguale = Temperatura(30, "celsius")

assert t_caldo.è_piu_calda_di(t_freddo)
assert t_freddo.è_piu_fredda_di(t_caldo)
assert t_caldo.è_uguale_a(t_uguale)
print("✓ Test 9 passato")
```

### Test 10: Differenza tra temperature
```python
t1 = Temperatura(30, "celsius")
t2 = Temperatura(20, "celsius")
diff = t1.differenza(t2)
assert abs(diff - 10.0) < 0.01
print("✓ Test 10 passato")
```

### Test 11: Conversione tra scale
```python
t = Temperatura(0, "celsius")
assert abs(t.converti_in("celsius") - 0.0) < 0.01
assert abs(t.converti_in("fahrenheit") - 32.0) < 0.01
assert abs(t.converti_in("kelvin") - 273.15) < 0.01
print("✓ Test 11 passato")
```

### Test 12: Ordinamento di temperature
```python
temperature = [
    Temperatura(30, "celsius"),
    Temperatura(10, "celsius"),
    Temperatura(20, "celsius")
]
ordinate = sorted(temperature)
assert ordinate[0].celsius < ordinate[1].celsius < ordinate[2].celsius
print("✓ Test 12 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Metodi di conversione statici
```python
@staticmethod
def _celsius_da_fahrenheit(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

@staticmethod
def _fahrenheit_da_celsius(celsius):
    return celsius * 9 / 5 + 32

@staticmethod
def _celsius_da_kelvin(kelvin):
    return kelvin - 273.15

@staticmethod
def _kelvin_da_celsius(celsius):
    return celsius + 273.15
```

### Passo 2: Validazione
```python
def _valida_temperatura(self, valore, scala):
    scala = scala.lower()
    if scala == "kelvin" and valore < 0:
        raise ValueError(f"Kelvin non può essere negativo: {valore}")
    elif scala == "celsius" and valore < -273.15:
        raise ValueError(f"Sotto zero assoluto: {valore}")
```

### Passo 3: Costruttore
```python
def __init__(self, valore=0, scala="celsius"):
    self._scala_default = scala
    self._celsius = 0

    if scala.lower() == "celsius":
        self.celsius = valore
    elif scala.lower() == "fahrenheit":
        self.fahrenheit = valore
    elif scala.lower() == "kelvin":
        self.kelvin = valore
```

### Passo 4: Property Celsius
```python
@property
def celsius(self):
    return self._celsius

@celsius.setter
def celsius(self, valore):
    self._valida_temperatura(valore, "celsius")
    self._celsius = float(valore)
```

### Passo 5: Property Fahrenheit
```python
@property
def fahrenheit(self):
    return self._fahrenheit_da_celsius(self._celsius)

@fahrenheit.setter
def fahrenheit(self, valore):
    self._valida_temperatura(valore, "fahrenheit")
    self._celsius = self._celsius_da_fahrenheit(valore)
```

### Passo 6: Property Kelvin
```python
@property
def kelvin(self):
    return self._kelvin_da_celsius(self._celsius)

@kelvin.setter
def kelvin(self, valore):
    self._valida_temperatura(valore, "kelvin")
    self._celsius = self._celsius_da_kelvin(valore)
```

### Passo 7: Comparazioni
```python
def __eq__(self, altra):
    if not isinstance(altra, Temperatura):
        return NotImplemented
    return abs(self._celsius - altra._celsius) < 0.01

def __lt__(self, altra):
    if not isinstance(altra, Temperatura):
        return NotImplemented
    return self._celsius < altra._celsius
```

### Passo 8: Metodi di confronto e utilità
```python
def è_piu_calda_di(self, altra):
    return self._celsius > altra._celsius

def è_piu_fredda_di(self, altra):
    return self._celsius < altra._celsius

def differenza(self, altra):
    return abs(self._celsius - altra._celsius)
```

---

## 💡 Trucchi e Best Practices

### ✅ Immagazzina sempre in una scala interna
```python
# BUONO - immagazzina in Celsius, converti per accesso
class Temperatura:
    def __init__(self, valore, scala):
        self._celsius = ...  # Sempre Celsius internamente

# Allora conversioni sono sempre consistenti
```

### ✅ Valida nel setter, non nel getter
```python
# BUONO - valida solo se assegni
@kelvin.setter
def kelvin(self, valore):
    self._valida_temperatura(valore, "kelvin")  # Valida qui
    self._celsius = self._celsius_da_kelvin(valore)

@property
def kelvin(self):
    return self._kelvin_da_celsius(self._celsius)  # Niente validazione
```

### ✅ Usa metodi di conversione statici
```python
# BUONO - metodi statici riutilizzabili
@staticmethod
def _fahrenheit_da_celsius(celsius):
    return celsius * 9 / 5 + 32

# Puoi usarli anche senza istanza
celsius = Temperatura._celsius_da_fahrenheit(68)
```

### ✅ Tolleranza in comparazioni di float
```python
# BUONO - tolleranza 0.01
def __eq__(self, altra):
    return abs(self._celsius - altra._celsius) < 0.01

# CATTIVO - esatto, può fallire
def __eq__(self, altra):
    return self._celsius == altra._celsius
```

### ✅ Usa @property per interfaccia pulita
```python
# BUONO - interfaccia come attributo
t.celsius = 25  # Chiaro, semplice

# CATTIVO - trop verboso
t.imposta_celsius(25)
t.ottieni_celsius()
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Validare nel getter
```python
# SBAGLIATO - getter non dovrebbe validare
@property
def kelvin(self):
    if ... < 0:  # NO!
        raise ValueError()

# GIUSTO - valida solo nel setter
@kelvin.setter
def kelvin(self, valore):
    if valore < 0:
        raise ValueError()
```

### ❌ Errore 2: Dimenticare di normalizzare il segno
```python
# SBAGLIATO - t1 e t2 sono diverse internally
t1 = Temperatura(20, "celsius")
t2 = Temperatura(68, "fahrenheit")  # Stesso valore!
print(t1 == t2)  # False se non converte correttamente

# GIUSTO - assicurati che le conversioni siano precise
```

### ❌ Errore 3: Non documentare scale
```python
# SBAGLIATO - confuso quale scala usa
t = Temperatura(100)  # È Celsius? Fahrenheit? Kelvin?

# GIUSTO - specifica sempre
t = Temperatura(100, "celsius")
t = Temperatura(100, "fahrenheit")
```

### ❌ Errore 4: Verificare kelvin < -273.15 anziché < 0
```python
# SBAGLIATO - confonde K e C
if kelvin < -273.15:  # Kelvin non è mai negativo!
    raise ValueError()

# GIUSTO
if kelvin < 0:
    raise ValueError("Kelvin non può essere negativo")
```

### ❌ Errore 5: Non usare tolleranza nei confronti
```python
# SBAGLIATO - float non è preciso
t1.celsius = 20.0
t2.celsius = 20.0000000001
assert t1 == t2  # False! Imprecisione float

# GIUSTO - tolleranza
assert abs(t1.celsius - t2.celsius) < 0.01
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Scala Rankine
```python
class Temperatura:
    # Rankine = Fahrenheit + 459.67 (come Kelvin per Celsius)
    @staticmethod
    def _rankine_da_celsius(celsius):
        return (celsius + 273.15) * 9 / 5

    @staticmethod
    def _celsius_da_rankine(rankine):
        return rankine * 5 / 9 - 273.15

    @property
    def rankine(self):
        return self._rankine_da_celsius(self._celsius)

    @rankine.setter
    def rankine(self, valore):
        if valore < 0:
            raise ValueError("Rankine non può essere negativo")
        self._celsius = self._celsius_da_rankine(valore)
```

### 🌟 Sfida 2: Operatori aritmetici
```python
class Temperatura:
    def __add__(self, altra):
        """Somma di temperature"""
        if isinstance(altra, Temperatura):
            return Temperatura(self.celsius + altra.celsius, "celsius")
        elif isinstance(altra, (int, float)):
            return Temperatura(self.celsius + altra, "celsius")
        return NotImplemented

    def __sub__(self, altra):
        """Differenza di temperature"""
        if isinstance(altra, Temperatura):
            return Temperatura(self.celsius - altra.celsius, "celsius")
        return NotImplemented

# Uso:
t = Temperatura(20, "celsius")
t_piu_calda = t + Temperatura(10, "celsius")  # 30°C
```

### 🌟 Sfida 3: Descrizione dettagliata
```python
class Temperatura:
    def descrivi(self):
        """Descrizione della temperatura"""
        c = self.celsius
        if c < -50:
            return "Freddo estremo"
        elif c < 0:
            return "Sotto zero"
        elif c < 15:
            return "Freddo"
        elif c < 25:
            return "Mite"
        elif c < 35:
            return "Caldo"
        else:
            return "Molto caldo"

    def è_sotto_congelamento(self):
        return self.celsius < 0

    def è_sopra_ebollizione(self):
        return self.celsius > 100
```

### 🌟 Sfida 4: Media di temperature
```python
@staticmethod
def media(temperature):
    """Calcola la media di più temperature"""
    if not temperature:
        return None
    total = sum(t.celsius for t in temperature)
    return Temperatura(total / len(temperature), "celsius")

# Uso:
temperature = [
    Temperatura(20, "celsius"),
    Temperatura(25, "celsius"),
    Temperatura(30, "celsius")
]
media = Temperatura.media(temperature)  # 25°C
```

### 🌟 Sfida 5: Intervallo di temperature
```python
class IntervaloTemperature:
    """Un intervallo con min e max"""
    def __init__(self, minima, massima):
        if minima > massima:
            minima, massima = massima, minima
        self.minima = minima
        self.massima = massima

    def è_dentro(self, t):
        return self.minima <= t <= self.massima

    def ampiezza(self):
        return self.massima.differenza(self.minima)

# Uso:
intervallo = IntervaloTemperature(
    Temperatura(20, "celsius"),
    Temperatura(30, "celsius")
)
print(intervallo.è_dentro(Temperatura(25, "celsius")))  # True
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **@property** | Getter per attributo | @property def celsius(self): |
| **@property.setter** | Setter per attributo | @celsius.setter |
| **Conversione** | Formule tra scale | C = (F - 32) × 5/9 |
| **Validazione** | Controllo valori | kelvin >= 0 |
| **Scala interna** | Rappresentazione unica | Sempre Celsius |
| **Tolleranza** | Imprecisione float | abs(a - b) < 0.01 |
| **Interfaccia fluida** | Accesso naturale | t.celsius = 25 |

---

## 🔗 Link Utili

### Documentazione
- [Python @property Decorator](https://docs.python.org/3/library/functions.html#property)
- [Properties - Official Docs](https://docs.python.org/3/glossary.html#term-property)
- [Temperatura - Wikipedia](https://it.wikipedia.org/wiki/Temperatura)

### Tutorial
- [Real Python - Python Property](https://realpython.com/python-property/)
- [GeeksforGeeks - @property Decorator](https://www.geeksforgeeks.org/python-property-decorator-property/)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Osserva come sono implementate le conversioni
- Guarda come è organizzata la validazione
- Nota come sono usati i setter e getter
- Apprendi dai metodi di confronto

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho implementato i metodi di conversione statici
- [ ] Ho creato il constructor con supporto di diverse scale
- [ ] Ho implementato _valida_temperatura
- [ ] Ho implementato @property celsius con setter
- [ ] Ho implementato @property fahrenheit con setter
- [ ] Ho implementato @property kelvin con setter
- [ ] Kelvin solleva errore se < 0
- [ ] Ho implementato __eq__, __lt__, __le__, __gt__, __ge__
- [ ] Ho implementato è_piu_calda_di, è_piu_fredda_di, è_uguale_a
- [ ] Ho implementato differenza() e converti_in()
- [ ] Ho testato con almeno 12 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai padroneggiato le proprietà Python! 🎉🌡️**

*"Le proprietà rendono il tuo codice più pulito, sicuro e intuitivo come i tipi nativi di Python!"*
