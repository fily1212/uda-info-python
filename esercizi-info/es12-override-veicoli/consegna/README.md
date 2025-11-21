# Es7: Override di Metodi - I Veicoli

## 📊 Informazioni Generali

**Livello:** 🟡 INTERMEDIO
**Durata stimata:** 4-5 ore
**Prerequisiti:** Es6 completato, comprensione dell'ereditarietà

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Sovrascrivere** metodi della classe base con comportamenti specifici
- ✅ **Usare** `super()` per richiamare il metodo della classe base E aggiungere codice
- ✅ **Progettare** comportamenti polimorfi dove ogni tipo si comporta diversamente
- ✅ **Gestire** attributi specifici (cilindrata, marce, carburante)
- ✅ **Applicare** il polimorfismo in liste eterogenee di oggetti
- ✅ **Capire** quando usare override vs nuovi metodi

**Concetti fondamentali:**
- Override = Sovrascrittura di metodi
- Polimorfismo = Stesso metodo, comportamenti diversi
- `super()` = Accesso ai metodi della classe base
- Metodo polimorfo = Un metodo che si comporta diversamente per ogni sottoclasse

---

## 📖 Descrizione

L'esercizio precedente ti ha insegnato l'ereditarietà. Questo esercizio va oltre: **l'override** è quando una sottoclasse **sovrascrive** completamente il comportamento di un metodo ereditato.

```
Veicolo.muovi() → metodo generico (base)
  ↓
Auto.muovi() → motore acceso, accelero su strada (override specifico)
Moto.muovi() → moto veloce e leggera (override specifico)
Bicicletta.muovi() → pedalo manualmente (override specifico)
```

Questo esercizio crea un **sistema di trasporto** dove:
- `Veicolo` è la classe base
- `Auto`, `Moto`, `Bicicletta` ereditano da `Veicolo`
- Ognuno ha il proprio modo di muoversi
- Tutti possono essere in una lista e chiamare `muovi()` polimorficamente

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Base Veicolo

**Definisci una classe `Veicolo` con:**

1. **Attributi:**
   - `marca` (str) - marca del veicolo (es: "Toyota", "Fiat")
   - `modello` (str) - modello (es: "Prius", "500")
   - `anno` (int) - anno di fabbricazione
   - `velocita_attuale` (float) - km/h, default 0
   - `velocita_massima` (float) - km/h massima possibile

2. **Metodi:**
   - `__init__(marca, modello, anno, velocita_massima)` - costruttore
   - `muovi()` - metodo che sarà sovrascritto (stampa info generica)
   - `accellera(incremente)` - aumenta velocità (max velocita_massima)
   - `frena(decremento)` - diminuisce velocità (min 0)
   - `ferma()` - porta velocità a 0
   - `info()` - ritorna info del veicolo
   - `velocita_attuale_str()` - ritorna velocità come stringa

### Parte 2: Sottoclassi - I Veicoli

#### 2a. Classe `Auto(Veicolo)`
- **Attributi aggiuntivi:**
  - `cilindrata` (int) - in cc (es: 1200, 2000)
  - `num_marce` (int) - numero di marce (es: 5, 6)
  - `marcia_attuale` (int) - da 0 a num_marce (0 = parcheggio)

- **Metodi:**
  - `__init__(marca, modello, anno, velocita_max, cilindrata, num_marce)` - usa super()
  - `muovi()` - override: stampa "Accendo il motore da {cilindrata}cc. Vroom vroom!"
  - `cambia_marcia(nuova_marcia)` - cambia marcia con validazione
  - `info()` - override: include cilindrata e marce
  - `accelera(incremente)` - override: muove anche la marcia se necessario

#### 2b. Classe `Moto(Veicolo)`
- **Attributi aggiuntivi:**
  - `cilindrata` (int) - in cc
  - `tipo` (str) - es: "sport", "cruiser", "touring"

- **Metodi:**
  - `__init__(marca, modello, anno, velocita_max, cilindrata, tipo)` - usa super()
  - `muovi()` - override: stampa "Moto in movimento! Vrroooom! Tipo: {tipo}"
  - `impennata()` - stampa "La moto fa un'impennata!"
  - `info()` - override: include cilindrata e tipo
  - `accellera(incremente)` - override: accelerazione +50% più veloce

#### 2c. Classe `Bicicletta(Veicolo)`
- **Attributi aggiuntivi:**
  - `tipo_cambio` (str) - es: "none", "manual", "automatic"
  - `numero_marce` (int) - 1 per fisso, 18 per cambio manual

- **Metodi:**
  - `__init__(marca, modello, anno, velocita_max, tipo_cambio, numero_marce)` - usa super()
  - `muovi()` - override: stampa "Pedalo manualmente! Puff puff!"
  - `pedala()` - stampa "Pedalando velocemente!"
  - `frena(decremento)` - override: frena più velocemente (x 1.5)
  - `info()` - override: include tipo cambio e numero marce

### Parte 3: Garaggio

**Definisci una classe `Garaggio` con:**

1. **Attributi:**
   - `nome` (str)
   - `veicoli` (lista) - i veicoli nel garaggio
   - `posti` (int) - numero massimo di veicoli

2. **Metodi:**
   - `aggiungi_veicolo(veicolo)` - aggiunge se c'è spazio
   - `numero_veicoli()` - quanti veicoli
   - `posti_disponibili()` - quanti posti liberi
   - `tutti_si_muovono()` - tutti i veicoli fanno muovi() (polimorfismo!)
   - `veicoli_per_tipo(tipo)` - filtra per tipo
   - `acceleration_test()` - testa accelerazione di tutti
   - `ordina_per_velocita_max()` - ordina i veicoli
   - `veicolo_piu_veloce()` - qual è il più veloce
   - `info_garaggio()` - stampa info di tutti i veicoli

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSI ============

class Veicolo:
    """Classe base per tutti i veicoli"""

    def __init__(self, marca, modello, anno, velocita_massima):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocita_attuale = 0
        self.velocita_massima = velocita_massima

    def muovi(self):
        print(f"Il veicolo {self.marca} {self.modello} si muove")

    def accellera(self, incremento):
        self.velocita_attuale = min(
            self.velocita_attuale + incremento, self.velocita_massima
        )
        print(f"Accelero. Velocità: {self.velocita_attuale} km/h")

    def frena(self, decremento):
        self.velocita_attuale = max(self.velocita_attuale - decremento, 0)
        print(f"Freno. Velocità: {self.velocita_attuale} km/h")

    def ferma(self):
        self.velocita_attuale = 0
        print(f"{self.marca} {self.modello} è fermo")

    def info(self):
        return f"{self.marca} {self.modello} ({self.anno}) - V.Max: {self.velocita_massima} km/h"

    def velocita_str(self):
        return f"{self.velocita_attuale}/{self.velocita_massima} km/h"


class Auto(Veicolo):
    """Un'auto - sottoclasse di Veicolo"""

    def __init__(self, marca, modello, anno, velocita_max, cilindrata, num_marce):
        super().__init__(marca, modello, anno, velocita_max)
        self.cilindrata = cilindrata
        self.num_marce = num_marce
        self.marcia_attuale = 0

    def muovi(self):
        # Override del metodo muovi
        print(f"Accendo il motore {self.cilindrata}cc da {self.marca}. Vroom vroom!")
        self.accellera(10)

    def cambia_marcia(self, nuova_marcia):
        if 0 <= nuova_marcia <= self.num_marce:
            self.marcia_attuale = nuova_marcia
            print(f"Ho inserito la marcia {nuova_marcia}")
            return True
        else:
            print(f"Errore: marcia non valida (0-{self.num_marce})")
            return False

    def accellera(self, incremento):
        # Override: accelerazione accelera in base alla marcia
        if self.marcia_attuale > 0:
            super().accellera(incremento)
        else:
            print("Errore: Devo inserire una marcia!")

    def info(self):
        # Override usando super()
        info_base = super().info()
        return f"{info_base}, {self.cilindrata}cc, {self.num_marce} marce"


class Moto(Veicolo):
    """Una moto - sottoclasse di Veicolo"""

    def __init__(self, marca, modello, anno, velocita_max, cilindrata, tipo):
        super().__init__(marca, modello, anno, velocita_max)
        self.cilindrata = cilindrata
        self.tipo = tipo

    def muovi(self):
        # Override del metodo muovi
        print(f"Moto {self.tipo} in movimento! Vrroooom!")

    def impennata(self):
        if self.velocita_attuale > 20:
            print("La moto fa un'impennata! Wow!")
        else:
            print("Troppo lento per fare un'impennata")

    def accellera(self, incremento):
        # Override: moto accelera più velocemente
        super().accellera(incremento * 1.5)  # 50% più veloce

    def info(self):
        info_base = super().info()
        return f"{info_base}, {self.cilindrata}cc, Tipo: {self.tipo}"


class Bicicletta(Veicolo):
    """Una bicicletta - sottoclasse di Veicolo"""

    def __init__(self, marca, modello, anno, velocita_max, tipo_cambio, numero_marce):
        super().__init__(marca, modello, anno, velocita_max)
        self.tipo_cambio = tipo_cambio
        self.numero_marce = numero_marce

    def muovi(self):
        # Override del metodo muovi
        print(f"Pedalo manualmente! Puff puff! 🚴")

    def pedala(self):
        print("Pedalando velocemente!")

    def frena(self, decremento):
        # Override: frena più velocemente
        super().frena(decremento * 1.5)

    def info(self):
        info_base = super().info()
        return f"{info_base}, Cambio: {self.tipo_cambio}, {self.numero_marce} marce"


class Garaggio:
    """Un garaggio con vari veicoli"""

    def __init__(self, nome, posti=10):
        self.nome = nome
        self.veicoli = []
        self.posti = posti

    def aggiungi_veicolo(self, veicolo):
        if len(self.veicoli) < self.posti:
            self.veicoli.append(veicolo)
            print(f"Aggiunto {veicolo.marca} {veicolo.modello} al garaggio")
            return True
        else:
            print(f"Garaggio pieno! Non riesco ad aggiungere {veicolo.marca}")
            return False

    def numero_veicoli(self):
        return len(self.veicoli)

    def posti_disponibili(self):
        return self.posti - len(self.veicoli)

    def tutti_si_muovono(self):
        """POLIMORFISMO - ogni veicolo muove a modo suo!"""
        print(f"\n=== Tutti i veicoli del {self.nome} si muovono ===")
        for veicolo in self.veicoli:
            veicolo.muovi()  # Chiama il muovi() specifico di ogni tipo!

    def veicoli_per_tipo(self, tipo):
        """Filtra per tipo di veicolo"""
        return [v for v in self.veicoli if type(v).__name__ == tipo]

    def acceleration_test(self):
        """Test di accelerazione"""
        print(f"\n=== Acceleration Test al {self.nome} ===")
        for veicolo in self.veicoli:
            print(f"\nTest di {veicolo.marca} {veicolo.modello}:")
            for i in range(3):
                veicolo.accellera(10)
            veicolo.ferma()

    def ordina_per_velocita_max(self):
        """Ritorna veicoli ordinati per velocità massima"""
        return sorted(self.veicoli, key=lambda v: v.velocita_massima, reverse=True)

    def veicolo_piu_veloce(self):
        """Ritorna il veicolo con velocità massima più alta"""
        if not self.veicoli:
            return None
        return max(self.veicoli, key=lambda v: v.velocita_massima)

    def info_garaggio(self):
        print(f"\n=== Garaggio {self.nome} ===")
        print(f"Posti: {self.numero_veicoli()}/{self.posti}")
        for veicolo in self.veicoli:
            print(f"  - {veicolo.info()}")


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    # Creare un garaggio
    garaggio = Garaggio("Garage Rossi", posti=10)

    # Creare veicoli diversi
    auto1 = Auto("Toyota", "Prius", 2020, 180, 1500, 6)
    auto2 = Auto("Fiat", "500", 2022, 160, 1200, 5)

    moto1 = Moto("Ducati", "Monster", 2021, 220, 937, "sport")
    moto2 = Moto("Harley-Davidson", "Street 750", 2020, 200, 750, "cruiser")

    bici1 = Bicicletta("Decathlon", "B'Twin", 2023, 40, "manual", 18)
    bici2 = Bicicletta("Specialized", "Allez", 2023, 50, "automatic", 21)

    # Aggiungere veicoli al garaggio
    for veicolo in [auto1, auto2, moto1, moto2, bici1, bici2]:
        garaggio.aggiungi_veicolo(veicolo)

    # Mostrare il garaggio
    garaggio.info_garaggio()

    # POLIMORFISMO - il momento magico!
    # Ogni veicolo muove a modo suo, ma usiamo lo stesso metodo muovi()
    garaggio.tutti_si_muovono()

    # Test di accelerazione
    garaggio.acceleration_test()

    # Ordina per velocità
    print("\n=== Veicoli ordinati per velocità massima ===")
    for veicolo in garaggio.ordina_per_velocita_max():
        print(f"  - {veicolo.info()}")

    # Veicolo più veloce
    piu_veloce = garaggio.veicolo_piu_veloce()
    print(f"\nVeicolo più veloce: {piu_veloce.info()}")

    # Filtra per tipo
    print("\n=== Solo Auto ===")
    for auto in garaggio.veicoli_per_tipo("Auto"):
        print(f"  - {auto.info()}")

    print("\n=== Solo Moto ===")
    for moto in garaggio.veicoli_per_tipo("Moto"):
        print(f"  - {moto.info()}")

    # Output atteso:
    # === Garaggio Garage Rossi ===
    # Posti: 6/10
    #   - Toyota Prius (2020) - V.Max: 180 km/h, 1500cc, 6 marce
    # ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Veicolo base
```python
v = Veicolo("Generic", "Model", 2020, 200)
assert v.marca == "Generic"
assert v.velocita_attuale == 0
assert v.velocita_massima == 200
print("✓ Test 1 passato")
```

### Test 2: Auto - creazione e info
```python
auto = Auto("Toyota", "Prius", 2020, 180, 1500, 6)
assert auto.marca == "Toyota"
assert auto.cilindrata == 1500
assert auto.num_marce == 6
assert "1500cc" in auto.info()
print("✓ Test 2 passato")
```

### Test 3: Auto - cambio marcia
```python
auto = Auto("Toyota", "Prius", 2020, 180, 1500, 6)
assert auto.cambia_marcia(3) == True
assert auto.marcia_attuale == 3
assert auto.cambia_marcia(10) == False  # Invalido
assert auto.marcia_attuale == 3  # Non cambia
print("✓ Test 3 passato")
```

### Test 4: Moto - ereditarietà e accelerazione
```python
moto = Moto("Ducati", "Monster", 2021, 220, 937, "sport")
assert moto.marca == "Ducati"
assert moto.tipo == "sport"
assert "937cc" in moto.info()
moto.accellera(10)
# Moto accelera più veloce (x1.5), quindi >10
assert moto.velocita_attuale > 10
print("✓ Test 4 passato")
```

### Test 5: Bicicletta - override di frena
```python
bici = Bicicletta("Decathlon", "B'Twin", 2023, 40, "manual", 18)
bici.velocita_attuale = 30
bici.frena(10)
# Bicicletta frena più veloce (x1.5), quindi più di 10
assert bici.velocita_attuale < 20
print("✓ Test 5 passato")
```

### Test 6: Polimorfismo - lista di veicoli
```python
veicoli = [
    Auto("Toyota", "Prius", 2020, 180, 1500, 6),
    Moto("Ducati", "Monster", 2021, 220, 937, "sport"),
    Bicicletta("Decathlon", "B'Twin", 2023, 40, "manual", 18)
]

# Tutti hanno i metodi comuni
for v in veicoli:
    assert hasattr(v, "muovi")
    assert hasattr(v, "accellera")
    assert hasattr(v, "frena")

# Ma muovi() si comporta diversamente!
# (In un test reale potresti catturare l'output)
print("✓ Test 6 passato")
```

### Test 7: Garaggio - aggiunta veicoli
```python
garaggio = Garaggio("Test", posti=3)
auto = Auto("Toyota", "Prius", 2020, 180, 1500, 6)
moto = Moto("Ducati", "Monster", 2021, 220, 937, "sport")

assert garaggio.aggiungi_veicolo(auto) == True
assert garaggio.numero_veicoli() == 1
assert garaggio.posti_disponibili() == 2

assert garaggio.aggiungi_veicolo(moto) == True
assert garaggio.numero_veicoli() == 2
print("✓ Test 7 passato")
```

### Test 8: Garaggio - filtro per tipo
```python
garaggio = Garaggio("Test", posti=10)
auto1 = Auto("Toyota", "Prius", 2020, 180, 1500, 6)
auto2 = Auto("Fiat", "500", 2022, 160, 1200, 5)
moto = Moto("Ducati", "Monster", 2021, 220, 937, "sport")

garaggio.aggiungi_veicolo(auto1)
garaggio.aggiungi_veicolo(auto2)
garaggio.aggiungi_veicolo(moto)

auto_list = garaggio.veicoli_per_tipo("Auto")
assert len(auto_list) == 2

moto_list = garaggio.veicoli_per_tipo("Moto")
assert len(moto_list) == 1
print("✓ Test 8 passato")
```

### Test 9: Garaggio - veicolo più veloce
```python
garaggio = Garaggio("Test", posti=10)
auto = Auto("Toyota", "Prius", 2020, 180, 1500, 6)  # 180
moto = Moto("Ducati", "Monster", 2021, 220, 937, "sport")  # 220
bici = Bicicletta("Decathlon", "B'Twin", 2023, 40, "manual", 18)  # 40

garaggio.aggiungi_veicolo(auto)
garaggio.aggiungi_veicolo(moto)
garaggio.aggiungi_veicolo(bici)

piu_veloce = garaggio.veicolo_piu_veloce()
assert piu_veloce.velocita_massima == 220
assert type(piu_veloce).__name__ == "Moto"
print("✓ Test 9 passato")
```

### Test 10: Super() - info con ereditarietà
```python
auto = Auto("Toyota", "Prius", 2020, 180, 1500, 6)
info = auto.info()

# Contiene info della classe base
assert "Toyota" in info
assert "Prius" in info
assert "2020" in info
assert "180" in info

# Contiene info specifica di Auto
assert "1500cc" in info
assert "6 marce" in info
print("✓ Test 10 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Crea la classe base Veicolo
```python
class Veicolo:
    def __init__(self, marca, modello, anno, velocita_massima):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocita_attuale = 0
        self.velocita_massima = velocita_massima

    def muovi(self):
        print(f"{self.marca} {self.modello} si muove")

    def accellera(self, incremento):
        self.velocita_attuale = min(
            self.velocita_attuale + incremento, self.velocita_massima
        )

    def frena(self, decremento):
        self.velocita_attuale = max(self.velocita_attuale - decremento, 0)
```

### Passo 2: Aggiungi metodi comuni in Veicolo
```python
def ferma(self):
    self.velocita_attuale = 0

def info(self):
    return f"{self.marca} {self.modello} ({self.anno}) - V.Max: {self.velocita_massima} km/h"
```

### Passo 3: Crea Auto con super()
```python
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, velocita_max, cilindrata, num_marce):
        super().__init__(marca, modello, anno, velocita_max)
        self.cilindrata = cilindrata
        self.num_marce = num_marce

    def muovi(self):
        print(f"Accendo il motore {self.cilindrata}cc. Vroom vroom!")
```

### Passo 4: Override del metodo info in Auto
```python
def info(self):
    # Chiama super().info() per ottenere le info base
    # poi aggiungi info specifiche
    info_base = super().info()
    return f"{info_base}, {self.cilindrata}cc, {self.num_marce} marce"
```

### Passo 5: Crea Moto e Bicicletta similmente
```python
class Moto(Veicolo):
    # Simile ad Auto

class Bicicletta(Veicolo):
    # Simile ad Auto
```

### Passo 6: Crea il Garaggio
```python
class Garaggio:
    def __init__(self, nome, posti=10):
        self.nome = nome
        self.veicoli = []
        self.posti = posti

    def aggiungi_veicolo(self, veicolo):
        if len(self.veicoli) < self.posti:
            self.veicoli.append(veicolo)
            return True
        return False
```

### Passo 7: Aggiungi POLIMORFISMO al Garaggio
```python
def tutti_si_muovono(self):
    """Questo è POLIMORFISMO - ogni veicolo muove a modo suo!"""
    for veicolo in self.veicoli:
        veicolo.muovi()  # Chiama il muovi() specifico!
```

### Passo 8: Testa il polimorfismo
```python
garaggio = Garaggio("Garage", posti=10)
garaggio.aggiungi_veicolo(Auto("Toyota", "Prius", 2020, 180, 1500, 6))
garaggio.aggiungi_veicolo(Moto("Ducati", "Monster", 2021, 220, 937, "sport"))
garaggio.tutti_si_muovono()  # Ogni veicolo muove diversamente!
```

---

## 💡 Trucchi e Best Practices

### ✅ Override con super() per riutilizzare codice
```python
# BUONO - riutilizza il codice base
class Auto(Veicolo):
    def info(self):
        return f"{super().info()}, {self.cilindrata}cc"

# CATTIVO - duplica il codice
class Auto(Veicolo):
    def info(self):
        return f"{self.marca} {self.modello} ({self.anno}), {self.cilindrata}cc"
```

### ✅ Polimorfismo = diversi comportamenti stesso nome
```python
# Tutti hanno muovi(), ma si comportano diversamente
auto.muovi()      # "Accendo il motore..."
moto.muovi()      # "Moto in movimento!..."
bici.muovi()      # "Pedalo manualmente!..."

# Perfetto per liste eterogenee
for veicolo in [auto, moto, bici]:
    veicolo.muovi()  # Chiama il giusto muovi()!
```

### ✅ Usa `type().__name__` per filtrare
```python
def veicoli_per_tipo(self, tipo):
    return [v for v in self.veicoli if type(v).__name__ == tipo]

# Uso:
auto_list = garaggio.veicoli_per_tipo("Auto")
```

### ✅ Override aggiunti = metodi specifici
```python
# Auto ha questo metodo (specifico di Auto)
class Auto(Veicolo):
    def cambia_marcia(self, nuova_marcia):
        # Non esiste in Moto o Bicicletta!
        self.marcia_attuale = nuova_marcia

# Moto ha questo metodo (specifico di Moto)
class Moto(Veicolo):
    def impennata(self):
        # Non esiste in Auto o Bicicletta!
        print("Impennata!")
```

### ✅ Chiama super() PRIMA di aggiungere codice
```python
# BUONO - chiama super() e poi aggiunge
class Moto(Veicolo):
    def accellera(self, incremento):
        super().accellera(incremento * 1.5)  # Base + modifica

# CATTIVO - ignora il super()
class Moto(Veicolo):
    def accellera(self, incremento):
        self.velocita_attuale = min(self.velocita_attuale + incremento * 1.5, self.velocita_massima)
        # Ripete codice inutilmente
```

### ✅ Usa lambda per sorting polimorfo
```python
# Ordina veicoli per velocità massima
ordinati = sorted(self.veicoli, key=lambda v: v.velocita_massima)

# Ordina per marca
ordinati = sorted(self.veicoli, key=lambda v: v.marca)

# Ordina per tipo (classe)
ordinati = sorted(self.veicoli, key=lambda v: type(v).__name__)
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare super().__init__()
```python
# SBAGLIATO - attributi della classe base non vengono inizializzati
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, velocita_max, cilindrata):
        self.cilindrata = cilindrata
        # Dimentica super()! self.marca, self.velocita_attuale non esistono!

# GIUSTO
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, velocita_max, cilindrata):
        super().__init__(marca, modello, anno, velocita_max)
        self.cilindrata = cilindrata
```

### ❌ Errore 2: Override completo invece di parziale
```python
# SBAGLIATO - reimplementa tutto, codice duplicato
class Moto(Veicolo):
    def accellera(self, incremento):
        self.velocita_attuale = min(
            self.velocita_attuale + incremento * 1.5, self.velocita_massima
        )
        print(f"Accelero. Velocità: {self.velocita_attuale}")

# GIUSTO - usa super() e modifica
class Moto(Veicolo):
    def accellera(self, incremento):
        super().accellera(incremento * 1.5)  # Delega la logica
```

### ❌ Errore 3: Confondere override con nuovi metodi
```python
# Nuovo metodo (va bene)
class Auto(Veicolo):
    def cambia_marcia(self, marcia):
        self.marcia_attuale = marcia

# Override (sovrascrive un metodo ereditato)
class Auto(Veicolo):
    def info(self):
        # Sovrascrive Veicolo.info()
        return super().info() + f", {self.cilindrata}cc"
```

### ❌ Errore 4: Polimorfismo con condizionali
```python
# SBAGLIATO - polimorfismo rovinato
class Garaggio:
    def tutti_si_muovono(self):
        for veicolo in self.veicoli:
            if type(veicolo).__name__ == "Auto":
                print("Accendo il motore...")
            elif type(veicolo).__name__ == "Moto":
                print("Moto in movimento...")
            # Questo non è polimorfismo!

# GIUSTO - polimorfismo
class Garaggio:
    def tutti_si_muovono(self):
        for veicolo in self.veicoli:
            veicolo.muovi()  # Chiama il muovi() specifico
```

### ❌ Errore 5: Non validare nei setter
```python
# SBAGLIATO - può accettare valori invalidi
class Auto(Veicolo):
    def cambia_marcia(self, nuova_marcia):
        self.marcia_attuale = nuova_marcia  # Se è 100?

# GIUSTO - valida
class Auto(Veicolo):
    def cambia_marcia(self, nuova_marcia):
        if 0 <= nuova_marcia <= self.num_marce:
            self.marcia_attuale = nuova_marcia
            return True
        return False
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Camion e Autobus
```python
class Camion(Veicolo):
    def __init__(self, marca, modello, anno, velocita_max, portata):
        super().__init__(marca, modello, anno, velocita_max)
        self.portata = portata  # in tonnellate
        self.carico_attuale = 0

    def carica(self, peso):
        if self.carico_attuale + peso <= self.portata:
            self.carico_attuale += peso
            return True
        return False

    def muovi(self):
        print(f"Camion pesante caricato ({self.carico_attuale}t) si muove lentamente")

class Autobus(Veicolo):
    def __init__(self, marca, modello, anno, velocita_max, posti):
        super().__init__(marca, modello, anno, velocita_max)
        self.posti = posti
        self.passeggeri = 0

    def sali_passeggeri(self, num):
        if self.passeggeri + num <= self.posti:
            self.passeggeri += num
            return True
        return False

    def muovi(self):
        print(f"Autobus con {self.passeggeri} passeggeri in movimento")
```

### 🌟 Sfida 2: Metodo muovi() con distanza
```python
class Veicolo:
    # ...
    def muovi(self, distanza):
        """Muovi il veicolo per una data distanza (in km)"""
        tempo_ore = distanza / self.velocita_massima
        print(f"Viaggio di {distanza}km impiegherebbe {tempo_ore:.1f} ore")

# Ogni sottoclasse overrida con tempo specifico
class Moto(Veicolo):
    def muovi(self, distanza):
        tempo_ore = distanza / self.velocita_massima * 0.8  # Più veloce
        print(f"Moto percorre {distanza}km in {tempo_ore:.1f} ore")
```

### 🌟 Sfida 3: Consumo di carburante
```python
class Veicolo:
    def __init__(self, marca, modello, anno, velocita_max, consumi_kmh):
        super().__init__(marca, modello, anno, velocita_max)
        self.consumi_kmh = consumi_kmh
        self.carburante = 50  # litri

    def percorri(self, km):
        consumo = km / self.consumi_kmh
        if self.carburante >= consumo:
            self.carburante -= consumo
            return True
        return False

# Ogni tipo ha consumi diversi
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, velocita_max, cilindrata, num_marce):
        super().__init__(marca, modello, anno, velocita_max, 10)  # 10 km/litro
        # ...

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, velocita_max, cilindrata, tipo):
        super().__init__(marca, modello, anno, velocita_max, 20)  # 20 km/litro
        # ...
```

### 🌟 Sfida 4: Costo di manutenzione
```python
class Veicolo:
    def costo_manutenzione_anno(self):
        """Sovrascritto in ogni sottoclasse"""
        return 500  # Default

class Auto(Veicolo):
    def costo_manutenzione_anno(self):
        return 800 + (self.cilindrata / 100)

class Moto(Veicolo):
    def costo_manutenzione_anno(self):
        return 600 + (self.cilindrata / 100)

class Bicicletta(Veicolo):
    def costo_manutenzione_anno(self):
        return 50  # Quasi gratis!
```

### 🌟 Sfida 5: Sistema di Parcheggio
```python
class Garaggio:
    def __init__(self, nome, posti_auto=20, posti_moto=30, posti_bici=50):
        self.nome = nome
        self.posti_auto = posti_auto
        self.posti_moto = posti_moto
        self.posti_bici = posti_bici
        self.auto_parcheggiate = []
        self.moto_parcheggiate = []
        self.bici_parcheggiate = []

    def parcheggia(self, veicolo):
        if type(veicolo).__name__ == "Auto":
            if len(self.auto_parcheggiate) < self.posti_auto:
                self.auto_parcheggiate.append(veicolo)
                return True
        elif type(veicolo).__name__ == "Moto":
            if len(self.moto_parcheggiate) < self.posti_moto:
                self.moto_parcheggiate.append(veicolo)
                return True
        elif type(veicolo).__name__ == "Bicicletta":
            if len(self.bici_parcheggiate) < self.posti_bici:
                self.bici_parcheggiate.append(veicolo)
                return True
        return False
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Override** | Sovrascrittura di un metodo ereditato | `def muovi(self): ...` in Auto |
| **Polimorfismo** | Stesso metodo, comportamenti diversi | `auto.muovi() != moto.muovi()` |
| **super()** | Accesso ai metodi della classe base | `super().__init__(...)` |
| **Relazione is-a** | Una sottoclasse *è un* tipo di superclasse | `Auto is-a Veicolo` |
| **Metodo polimorfo** | Metodo che si comporta diversamente per sottoclasse | `muovi()` in ogni veicolo |
| **Filtro per tipo** | Selezionare oggetti di un tipo specifico | `type(v).__name__ == "Auto"` |

---

## 🔗 Link Utili

### Documentazione
- [Python Method Override](https://docs.python.org/3/tutorial/classes.html#method-objects)
- [Polymorphism in Python](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [super() documentation](https://docs.python.org/3/library/functions.html#super)

### Tutorial
- [Real Python - Polymorphism](https://realpython.com/python-polymorphism/)
- [Method Overriding](https://www.geeksforgeeks.org/method-overriding-in-python/)
- [Polymorphism Example](https://www.tutorialspoint.com/python/python_polymorphism.htm)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Nota come sono implementati gli override
- Guarda come super() è usato
- Osserva il polimorfismo nella lista di veicoli
- Apprendi dai pattern di filtro e sorting

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho creato la classe base `Veicolo` con attributi comuni
- [ ] Ho creato sottoclassi `Auto`, `Moto`, `Bicicletta`
- [ ] Ogni sottoclasse usa `super().__init__()` nel costruttore
- [ ] Ho overridato il metodo `muovi()` in ogni sottoclasse
- [ ] Ho overridato il metodo `info()` usando `super().info()`
- [ ] Ho implementato metodi specifici (cambia_marcia, impennata, ecc.)
- [ ] Ho creato la classe `Garaggio` con lista di veicoli
- [ ] Il Garaggio usa polimorfismo in `tutti_si_muovono()`
- [ ] Ho testato il polimorfismo (stessi metodi, diversi comportamenti)
- [ ] Ho implementato filtro per tipo di veicolo
- [ ] Ho testato con almeno 8 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai padroneggiato l'override e il polimorfismo! 🎉🏎️**

*"L'override è il modo di Python di dire: 'I want to do this my way'"*
