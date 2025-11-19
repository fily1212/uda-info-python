# Es13: Ereditarietà Multipla - Sistema SmartHome

## 📊 Informazioni Generali

**Livello:** 🔴 AVANZATO
**Durata stimata:** 6-7 ore
**Prerequisiti:** Es1-12 completati, ereditarietà, composizione

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Implementare** ereditarietà multipla con mix-in
- ✅ **Capire** il MRO (Method Resolution Order)
- ✅ **Usare** super() in ereditarietà complessa
- ✅ **Progettare** mix-in riutilizzabili
- ✅ **Creare** una gerarchia di classi flexible
- ✅ **Evitare** il "diamond problem"
- ✅ **Implementare** un sistema SmartHome realistico

**Concetti fondamentali:**
- Ereditarietà singola vs multipla
- Mix-in = classi ausiliarie riutilizzabili
- MRO (Method Resolution Order) = ordine ricerca metodi
- super() = chiama metodo della classe padre
- Diamond problem = ambiguità in ereditarietà multipla
- Python usa C3 Linearization per MRO

---

## 📖 Descrizione

La **ereditarietà multipla** permette a una classe di ereditare da più classi padre.
I **mix-in** sono classi piccole che forniscono funzionalità specifiche.

Questo esercizio crea un **sistema SmartHome** con:
- **Elettrodomestici** base (Frigorifero, Lavatrice, Forno)
- **Mix-in Connettibile** per WiFi/Bluetooth
- **Mix-in Programmabile** per timer/automazione
- **Classe SmartHome** che gestisce tutti gli elettrodomestici
- **MRO** corretto e uso di super()

**Gerarchia:**
```
        Elettrodomestico (base)
              ↗    ↑    ↖
    Connettibile  |    Programmabile (mix-in)
              ↖    ↓    ↙
        Frigorifero, Lavatrice, Forno (combinazioni)
```

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Base Elettrodomestico

**Definisci una classe `Elettrodomestico` con:**

1. **Attributi:**
   - `nome` (str) - nome dell'elettrodomestico
   - `acceso` (bool) - se è acceso/spento
   - `consumo_watts` (int) - consumo energetico

2. **Metodi:**
   - `__init__(nome, consumo_watts)`
   - `accendi()` - accende l'apparecchio
   - `spegni()` - spegne l'apparecchio
   - `stato()` - ritorna lo stato
   - `__str__()` - rappresentazione

### Parte 2: Mix-in Connettibile

**Definisci un mix-in `Connettibile` con:**

1. **Attributi:**
   - `wifi_abilitato` (bool)
   - `bluetooth_abilitato` (bool)
   - `indirizzo_ip` (str) - None se non connesso

2. **Metodi:**
   - `abilita_wifi()` - attiva WiFi
   - `disabilita_wifi()` - disattiva WiFi
   - `abilita_bluetooth()` - attiva Bluetooth
   - `disabilita_bluetooth()` - disattiva Bluetooth
   - `connessione_info()` - ritorna info connessione

### Parte 3: Mix-in Programmabile

**Definisci un mix-in `Programmabile` con:**

1. **Attributi:**
   - `timer_attivo` (bool)
   - `tempo_programmato` (int) - minuti
   - `programmi` (list) - lista di programmi

2. **Metodi:**
   - `imposta_timer(minuti)` - imposta un timer
   - `annulla_timer()` - cancella il timer
   - `aggiungi_programma(nome_programma)` - aggiunge un programma
   - `lista_programmi()` - ritorna programmi disponibili
   - `esegui_programma(nome)` - avvia un programma

### Parte 4: Classi Concrete

**Implementa combinazioni di ereditarietà:**

1. **`Frigorifero`** (Elettrodomestico + Connettibile)
   - Controllabile via WiFi
   - Mantiene temperatura

2. **`Lavatrice`** (Elettrodomestico + Connettibile + Programmabile)
   - WiFi + timer + programmi di lavaggio

3. **`Forno`** (Elettrodomestico + Programmabile)
   - Timer + programmi di cottura
   - NO WiFi

4. **`ForninoSmart`** (Forno + Connettibile)
   - Combina forno con WiFi

### Parte 5: Classe SmartHome

**Definisci una classe `SmartHome` che:**

1. **Gestisce** una collezione di elettrodomestici
2. **Consente** accensione/spegnimento multipli
3. **Calcola** consumo totale
4. **Ricerca** per tipo
5. **Automazione** base (accendi tutto, spegni tutto)

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ CLASSE BASE ============

class Elettrodomestico:
    """Base per tutti gli elettrodomestici"""

    def __init__(self, nome, consumo_watts):
        self.nome = nome
        self.acceso = False
        self.consumo_watts = consumo_watts

    def accendi(self):
        """Accende l'apparecchio"""
        self.acceso = True
        print(f"✓ {self.nome} acceso")

    def spegni(self):
        """Spegne l'apparecchio"""
        self.acceso = False
        print(f"✓ {self.nome} spento")

    def stato(self):
        """Stato attuale"""
        stato = "ACCESO" if self.acceso else "SPENTO"
        return f"{self.nome}: {stato} ({self.consumo_watts}W)"

    def __str__(self):
        return self.stato()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.nome}', {self.consumo_watts}W)"


# ============ MIX-IN CONNETTIBILE ============

class Connettibile:
    """Mix-in per apparecchi con connettività WiFi/Bluetooth"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Catena MRO
        self.wifi_abilitato = False
        self.bluetooth_abilitato = False
        self.indirizzo_ip = None

    def abilita_wifi(self):
        """Attiva WiFi"""
        self.wifi_abilitato = True
        self.indirizzo_ip = "192.168.1.100"  # Simulato
        print(f"  ✓ WiFi abilitato per {self.nome}")

    def disabilita_wifi(self):
        """Disattiva WiFi"""
        self.wifi_abilitato = False
        self.indirizzo_ip = None
        print(f"  ✓ WiFi disabilitato per {self.nome}")

    def abilita_bluetooth(self):
        """Attiva Bluetooth"""
        self.bluetooth_abilitato = True
        print(f"  ✓ Bluetooth abilitato per {self.nome}")

    def disabilita_bluetooth(self):
        """Disattiva Bluetooth"""
        self.bluetooth_abilitato = False
        print(f"  ✓ Bluetooth disabilitato per {self.nome}")

    def connessione_info(self):
        """Informazioni sulla connettività"""
        info = f"{self.nome} - "
        if self.wifi_abilitato:
            info += f"WiFi ({self.indirizzo_ip}) "
        if self.bluetooth_abilitato:
            info += "Bluetooth "
        if not self.wifi_abilitato and not self.bluetooth_abilitato:
            info += "Offline"
        return info


# ============ MIX-IN PROGRAMMABILE ============

class Programmabile:
    """Mix-in per apparecchi con timer e programmi"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Catena MRO
        self.timer_attivo = False
        self.tempo_programmato = 0
        self.programmi = []
        self.programma_attivo = None

    def imposta_timer(self, minuti):
        """Imposta un timer"""
        if minuti <= 0:
            print(f"  ✗ Timer deve essere > 0")
            return False
        self.tempo_programmato = minuti
        self.timer_attivo = True
        print(f"  ✓ Timer impostato: {minuti} minuti per {self.nome}")
        return True

    def annulla_timer(self):
        """Annulla il timer"""
        self.timer_attivo = False
        self.tempo_programmato = 0
        print(f"  ✓ Timer annullato per {self.nome}")
        return True

    def aggiungi_programma(self, nome_programma):
        """Aggiunge un programma disponibile"""
        if nome_programma not in self.programmi:
            self.programmi.append(nome_programma)
            print(f"  ✓ Programma aggiunto: {nome_programma}")
        return True

    def lista_programmi(self):
        """Ritorna lista di programmi"""
        return self.programmi

    def esegui_programma(self, nome):
        """Esegui un programma"""
        if nome not in self.programmi:
            print(f"  ✗ Programma '{nome}' non trovato")
            return False
        self.programma_attivo = nome
        self.accendi()
        print(f"  ✓ Programma '{nome}' avviato su {self.nome}")
        return True

    def timer_info(self):
        """Informazioni sul timer"""
        if self.timer_attivo:
            return f"Timer: {self.tempo_programmato} min (attivo)"
        return "Timer: nessuno"


# ============ CLASSI CONCRETE ============

class Frigorifero(Connettibile, Elettrodomestico):
    """Frigorifero smart con WiFi"""

    def __init__(self, nome="Frigorifero", consumo_watts=200):
        super().__init__(nome, consumo_watts)
        self.temperatura = 4  # gradi Celsius

    def imposta_temperatura(self, temp):
        """Imposta la temperatura interna"""
        if -20 <= temp <= 10:
            self.temperatura = temp
            print(f"  ✓ Temperatura {self.nome} impostata a {temp}°C")
        else:
            print(f"  ✗ Temperatura fuori range")

    def __str__(self):
        base = super().__str__()
        return f"{base} | Temp: {self.temperatura}°C | Connessione: {self.connessione_info()}"


class Lavatrice(Connettibile, Programmabile, Elettrodomestico):
    """Lavatrice smart con WiFi e programmi"""

    def __init__(self, nome="Lavatrice", consumo_watts=2000):
        super().__init__(nome, consumo_watts)
        # Aggiungi programmi standard
        self.aggiungi_programma("Cotone 60°C")
        self.aggiungi_programma("Delicati 30°C")
        self.aggiungi_programma("Veloce 30min")

    def __str__(self):
        base = Elettrodomestico.__str__(self)
        return (
            f"{base}\n"
            f"    Programmi: {', '.join(self.lista_programmi())}\n"
            f"    {self.timer_info()}\n"
            f"    {self.connessione_info()}"
        )


class Forno(Programmabile, Elettrodomestico):
    """Forno con timer e programmi (NO WiFi)"""

    def __init__(self, nome="Forno", consumo_watts=3000):
        super().__init__(nome, consumo_watts)
        self.temperatura_interna = 20
        # Aggiungi programmi standard
        self.aggiungi_programma("Pizze 250°C")
        self.aggiungi_programma("Pane 220°C")
        self.aggiungi_programma("Dolci 180°C")

    def imposta_temperatura(self, temp):
        """Imposta temperatura forno"""
        if 50 <= temp <= 300:
            self.temperatura_interna = temp
            print(f"  ✓ Forno {self.nome} riscaldato a {temp}°C")
        else:
            print(f"  ✗ Temperatura fuori range (50-300°C)")

    def __str__(self):
        base = Elettrodomestico.__str__(self)
        return (
            f"{base} | Temp: {self.temperatura_interna}°C\n"
            f"    Programmi: {', '.join(self.lista_programmi())}\n"
            f"    {self.timer_info()}"
        )


class ForninoSmart(Connettibile, Forno):
    """Forno smart con WiFi"""

    def __init__(self, nome="Fornino Smart", consumo_watts=2500):
        super().__init__(nome, consumo_watts)

    def __str__(self):
        base = Forno.__str__(self)
        return f"{base}\n    WiFi: {self.connessione_info()}"


# ============ CLASSE SMARTHOME ============

class SmartHome:
    """Sistema di controllo per casa intelligente"""

    def __init__(self, nome_casa="La Mia Casa"):
        self.nome_casa = nome_casa
        self.elettrodomestici = []

    def aggiungi_elettrodomestico(self, apparecchio):
        """Aggiunge un'appliance alla casa"""
        self.elettrodomestici.append(apparecchio)
        print(f"✓ {apparecchio.nome} aggiunto a {self.nome_casa}")

    def rimuovi_elettrodomestico(self, nome):
        """Rimuove un'appliance"""
        for app in self.elettrodomestici:
            if app.nome == nome:
                self.elettrodomestici.remove(app)
                print(f"✓ {nome} rimosso da {self.nome_casa}")
                return True
        return False

    def accendi_tutto(self):
        """Accende tutti gli apparecchi"""
        print(f"\n🏠 Accensione generale di {self.nome_casa}")
        for app in self.elettrodomestici:
            app.accendi()

    def spegni_tutto(self):
        """Spegne tutti gli apparecchi"""
        print(f"\n🏠 Spegnimento generale di {self.nome_casa}")
        for app in self.elettrodomestici:
            app.spegni()

    def consumo_totale(self):
        """Calcola consumo totale in Watts"""
        return sum(app.consumo_watts for app in self.elettrodomestici if app.acceso)

    def trova_per_tipo(self, tipo):
        """Trova apparecchi di un tipo specifico"""
        return [app for app in self.elettrodomestici if isinstance(app, tipo)]

    def apparecchi_connessi(self):
        """Ritorna apparecchi con WiFi attivo"""
        return [
            app for app in self.elettrodomestici
            if isinstance(app, Connettibile) and app.wifi_abilitato
        ]

    def rapporto_stato(self):
        """Stampa lo stato completo della casa"""
        print(f"\n{'='*60}")
        print(f"📋 RAPPORTO: {self.nome_casa}")
        print(f"{'='*60}")

        for app in self.elettrodomestici:
            print(f"\n{app}")

        print(f"\n{'─'*60}")
        print(f"Apparecchi accesi: {sum(1 for a in self.elettrodomestici if a.acceso)}/{len(self.elettrodomestici)}")
        print(f"Consumo totale: {self.consumo_totale()} W")
        print(f"Apparecchi connessi: {len(self.apparecchi_connessi())}")
        print(f"{'='*60}\n")

    def __str__(self):
        return f"SmartHome: {self.nome_casa} ({len(self.elettrodomestici)} apparecchi)"


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    print("=== CREAZIONE SMARTHOME ===")
    casa = SmartHome("Casa Intelligente")

    print("\n=== CREAZIONE APPARECCHI ===")
    frigo = Frigorifero()
    lavatrice = Lavatrice()
    forno = Forno()
    fornino = ForninoSmart("Fornino Combo")

    casa.aggiungi_elettrodomestico(frigo)
    casa.aggiungi_elettrodomestico(lavatrice)
    casa.aggiungi_elettrodomestico(forno)
    casa.aggiungi_elettrodomestico(fornino)

    print("\n=== STATO INIZIALE ===")
    casa.rapporto_stato()

    print("=== ABILITAZIONE WIFI ===")
    frigo.abilita_wifi()
    lavatrice.abilita_wifi()
    fornino.abilita_wifi()

    print("\n=== PROGRAMMAZIONE LAVATRICE ===")
    lavatrice.esegui_programma("Cotone 60°C")
    lavatrice.imposta_timer(60)

    print("\n=== PROGRAMMAZIONE FORNO ===")
    forno.accendi()
    forno.esegui_programma("Pizze 250°C")
    forno.imposta_temperature(250)
    forno.imposta_timer(30)

    print("\n=== STATO DOPO PROGRAMMAZIONE ===")
    casa.rapporto_stato()

    print("=== ACCENSIONE GENERALE ===")
    casa.accendi_tutto()

    print("\n=== CONSUMO TOTALE ===")
    print(f"Consumo attuale: {casa.consumo_totale()} W")

    print("\n=== APPARECCHI CONNESSI ===")
    for app in casa.apparecchi_connessi():
        print(f"  - {app.nome}: {app.indirizzo_ip}")

    print("\n=== APPARECCHI PER TIPO ===")
    frigoriferi = casa.trova_per_tipo(Frigorifero)
    print(f"Frigoriferi: {[f.nome for f in frigoriferi]}")

    print("\n=== SPEGNIMENTO GENERALE ===")
    casa.spegni_tutto()

    print("\n=== STATO FINALE ===")
    casa.rapporto_stato()
```

---

## 🔍 Casi di Prova (Test)

### Test 1: MRO (Method Resolution Order)
```python
lavatrice = Lavatrice()
# MRO è: Lavatrice → Connettibile → Programmabile → Elettrodomestico → object
# Verifica che tutti i metodi sono accessibili
assert hasattr(lavatrice, 'accendi')  # Da Elettrodomestico
assert hasattr(lavatrice, 'abilita_wifi')  # Da Connettibile
assert hasattr(lavatrice, 'imposta_timer')  # Da Programmabile
print("✓ Test 1 passato")
```

### Test 2: Ereditarietà Frigorifero
```python
frigo = Frigorifero("Frigo", 200)
assert isinstance(frigo, Connettibile)
assert isinstance(frigo, Elettrodomestico)
assert frigo.consumo_watts == 200
print("✓ Test 2 passato")
```

### Test 3: Accensione/Spegnimento
```python
app = Frigorifero()
assert app.acceso == False
app.accendi()
assert app.acceso == True
app.spegni()
assert app.acceso == False
print("✓ Test 3 passato")
```

### Test 4: Connettibilità WiFi
```python
frigo = Frigorifero()
assert frigo.wifi_abilitato == False

frigo.abilita_wifi()
assert frigo.wifi_abilitato == True
assert frigo.indirizzo_ip == "192.168.1.100"

frigo.disabilita_wifi()
assert frigo.wifi_abilitato == False
assert frigo.indirizzo_ip == None
print("✓ Test 4 passato")
```

### Test 5: Timer Programmabile
```python
lavatrice = Lavatrice()
assert lavatrice.timer_attivo == False

lavatrice.imposta_timer(60)
assert lavatrice.timer_attivo == True
assert lavatrice.tempo_programmato == 60

lavatrice.annulla_timer()
assert lavatrice.timer_attivo == False
print("✓ Test 5 passato")
```

### Test 6: Programmi
```python
lavatrice = Lavatrice()
programmi = lavatrice.lista_programmi()
assert "Cotone 60°C" in programmi
assert "Delicati 30°C" in programmi

lavatrice.aggiungi_programma("Ultra veloce")
assert "Ultra veloce" in lavatrice.lista_programmi()
print("✓ Test 6 passato")
```

### Test 7: Esecuzione programma
```python
forno = Forno()
assert forno.acceso == False

forno.esegui_programma("Pizze 250°C")
assert forno.acceso == True
assert forno.programma_attivo == "Pizze 250°C"
print("✓ Test 7 passato")
```

### Test 8: SmartHome - Gestione apparecchi
```python
casa = SmartHome("Casa Test")
assert len(casa.elettrodomestici) == 0

frigo = Frigorifero()
casa.aggiungi_elettrodomestico(frigo)
assert len(casa.elettrodomestici) == 1

casa.rimuovi_elettrodomestico("Frigorifero")
assert len(casa.elettrodomestici) == 0
print("✓ Test 8 passato")
```

### Test 9: SmartHome - Accensione collettiva
```python
casa = SmartHome("Casa Test")
casa.aggiungi_elettrodomestico(Frigorifero())
casa.aggiungi_elettrodomestico(Lavatrice())

for app in casa.elettrodomestici:
    assert app.acceso == False

casa.accendi_tutto()
for app in casa.elettrodomestici:
    assert app.acceso == True
print("✓ Test 9 passato")
```

### Test 10: SmartHome - Consumo
```python
casa = SmartHome("Casa Test")
casa.aggiungi_elettrodomestico(Frigorifero("Frigo1", 200))
casa.aggiungi_elettrodomestico(Lavatrice("Lavatr1", 2000))

casa.accendi_tutto()
assert casa.consumo_totale() == 2200
print("✓ Test 10 passato")
```

### Test 11: SmartHome - Ricerca per tipo
```python
casa = SmartHome("Casa Test")
casa.aggiungi_elettrodomestico(Frigorifero())
casa.aggiungi_elettrodomestico(Frigorifero("Frigo2"))
casa.aggiungi_elettrodomestico(Lavatrice())

frigoriferi = casa.trova_per_tipo(Frigorifero)
assert len(frigoriferi) == 2
print("✓ Test 11 passato")
```

### Test 12: ForninoSmart - Ereditarietà multipla
```python
fornino = ForninoSmart()
# Deve avere metodi da Connettibile
assert hasattr(fornino, 'abilita_wifi')
# Deve avere metodi da Forno (che eredita da Programmabile)
assert hasattr(fornino, 'imposta_timer')
assert hasattr(fornino, 'esegui_programma')

fornino.abilita_wifi()
assert fornino.wifi_abilitato == True
fornino.imposta_timer(45)
assert fornino.timer_attivo == True
print("✓ Test 12 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Classe base Elettrodomestico
```python
class Elettrodomestico:
    def __init__(self, nome, consumo_watts):
        self.nome = nome
        self.acceso = False
        self.consumo_watts = consumo_watts

    def accendi(self):
        self.acceso = True

    def spegni(self):
        self.acceso = False
```

### Passo 2: Mix-in Connettibile
```python
class Connettibile:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wifi_abilitato = False
        self.indirizzo_ip = None

    def abilita_wifi(self):
        self.wifi_abilitato = True
        self.indirizzo_ip = "192.168.1.100"
```

### Passo 3: Mix-in Programmabile
```python
class Programmabile:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer_attivo = False
        self.programmi = []

    def imposta_timer(self, minuti):
        self.timer_attivo = True
        self.tempo_programmato = minuti
```

### Passo 4: Classe Frigorifero (semplice)
```python
class Frigorifero(Connettibile, Elettrodomestico):
    def __init__(self, nome="Frigorifero", consumo_watts=200):
        super().__init__(nome, consumo_watts)
        self.temperatura = 4
```

### Passo 5: Classe Lavatrice (complessa)
```python
class Lavatrice(Connettibile, Programmabile, Elettrodomestico):
    def __init__(self, nome="Lavatrice", consumo_watts=2000):
        super().__init__(nome, consumo_watts)
        self.aggiungi_programma("Cotone 60°C")
```

### Passo 6: Classe Forno
```python
class Forno(Programmabile, Elettrodomestico):
    def __init__(self, nome="Forno", consumo_watts=3000):
        super().__init__(nome, consumo_watts)
        self.temperatura_interna = 20
```

### Passo 7: ForninoSmart (eredita da Connettibile + Forno)
```python
class ForninoSmart(Connettibile, Forno):
    def __init__(self, nome="Fornino Smart", consumo_watts=2500):
        super().__init__(nome, consumo_watts)
```

### Passo 8: Classe SmartHome
```python
class SmartHome:
    def __init__(self, nome_casa="Casa"):
        self.nome_casa = nome_casa
        self.elettrodomestici = []

    def aggiungi_elettrodomestico(self, app):
        self.elettrodomestici.append(app)

    def accendi_tutto(self):
        for app in self.elettrodomestici:
            app.accendi()
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa super() per catena MRO
```python
# BUONO - super() segue MRO
class Lavatrice(Connettibile, Programmabile, Elettrodomestico):
    def __init__(self, nome, consumo):
        super().__init__(nome, consumo)  # Segue MRO

# CATTIVO - chiama diretto, salta classi
class Lavatrice(Connettibile, Programmabile, Elettrodomestico):
    def __init__(self, nome, consumo):
        Elettrodomestico.__init__(self, nome, consumo)  # Salta Connettibile!
```

### ✅ Ogni mix-in chiama super().__init__
```python
# BUONO - catena MRO
class Connettibile:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Passa a prossima classe
        self.wifi_abilitato = False

class Programmabile:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Passa a prossima classe
        self.timer_attivo = False
```

### ✅ Verifica MRO durante sviluppo
```python
# Utile per debugging
lavatrice = Lavatrice()
print(lavatrice.__class__.__mro__)
# Output: (<class 'Lavatrice'>, <class 'Connettibile'>,
#          <class 'Programmabile'>, <class 'Elettrodomestico'>, <class 'object'>)
```

### ✅ Usa isinstance() per verificare tipo
```python
# Verifica capacità
if isinstance(app, Connettibile):
    app.abilita_wifi()

if isinstance(app, Programmabile):
    app.imposta_timer(30)
```

### ✅ Ordine ereditarietà importa (sinistra→destra)
```python
# BUONO - ordine logico
class Lavatrice(Connettibile, Programmabile, Elettrodomestico):
    pass
# MRO: Lavatrice → Connettibile → Programmabile → Elettrodomestico

# CATTIVO - ordine confuso
class Lavatrice(Programmabile, Connettibile, Elettrodomestico):
    pass
# MRO: Lavatrice → Programmabile → Connettibile → Elettrodomestico
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare super() in mix-in
```python
# SBAGLIATO - __init__ non catena
class Connettibile:
    def __init__(self):
        self.wifi = False
        # Manca super()!

# Allora Programmabile.__init__ non è mai chiamato!

# GIUSTO
class Connettibile:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wifi = False
```

### ❌ Errore 2: Ordine ereditarietà sbagliato
```python
# SBAGLIATO - Lavatrice non ha metodi da Programmabile
class Lavatrice(Elettrodomestico, Programmabile, Connettibile):
    pass

# GIUSTO - specifiche prima, base dopo
class Lavatrice(Connettibile, Programmabile, Elettrodomestico):
    pass
```

### ❌ Errore 3: Usare __init__ diretto invece di super()
```python
# SBAGLIATO - salta classi
class ForninoSmart(Connettibile, Forno):
    def __init__(self, nome, consumo):
        Forno.__init__(self, nome, consumo)  # Salta Connettibile!

# GIUSTO
class ForninoSmart(Connettibile, Forno):
    def __init__(self, nome, consumo):
        super().__init__(nome, consumo)  # Segue MRO
```

### ❌ Errore 4: Diamond problem non gestito
```python
# SBAGLIATO - "diamond problem"
# Entrambi Connettibile e Programmabile ereditano da Elettrodomestico
# __init__ potrebbe essere chiamato due volte!

# GIUSTO - usa super() con *args, **kwargs
class Connettibile:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

### ❌ Errore 5: Apparecchio senza __init__ corretto
```python
# SBAGLIATO - non passa parametri a super()
class Frigorifero(Connettibile, Elettrodomestico):
    def __init__(self):
        Connettibile.__init__(self)  # Quale nome/consumo?

# GIUSTO
class Frigorifero(Connettibile, Elettrodomestico):
    def __init__(self, nome="Frigorifero", consumo_watts=200):
        super().__init__(nome, consumo_watts)
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Automazione (spegni se non in uso)
```python
class Frigorifero(Connettibile, Elettrodomestico):
    def __init__(self, ...):
        super().__init__(...)
        self.ultima_apertura = None
        self.spegnimento_automatico = True

    def apri_porta(self):
        """Registra apertura porta"""
        from datetime import datetime
        self.ultima_apertura = datetime.now()
        if not self.acceso:
            self.accendi()

    def controlla_inattivita(self, minuti_soglia=30):
        """Spegni se non aperto da troppo tempo"""
        from datetime import datetime, timedelta
        if self.ultima_apertura:
            delta = datetime.now() - self.ultima_apertura
            if delta > timedelta(minutes=minuti_soglia) and self.spegnimento_automatico:
                self.spegni()
```

### 🌟 Sfida 2: Scenario di automazione
```python
class SmartHome:
    def scenario_buonanotte(self):
        """Scenario che prepara la casa per la notte"""
        print("\n🌙 Scenario: Buonanotte")
        # Spegni tutto tranne il frigorifero
        for app in self.elettrodomestici:
            if not isinstance(app, Frigorifero):
                app.spegni()
        # Disabilita WiFi
        for app in self.apparecchi_connessi():
            app.disabilita_wifi()

    def scenario_mattino(self):
        """Scenario mattino"""
        print("\n☀️ Scenario: Buongiorno")
        # Accendi frigorifero e forno per fare colazione
        for app in self.elettrodomestici:
            if isinstance(app, (Frigorifero, Forno)):
                app.accendi()
```

### 🌟 Sfida 3: Storico accensioni
```python
from datetime import datetime

class Elettrodomestico:
    def __init__(self, nome, consumo_watts):
        # ... altri attributi
        self.storico_accensioni = []

    def accendi(self):
        self.acceso = True
        self.storico_accensioni.append(("acceso", datetime.now()))

    def spegni(self):
        self.acceso = False
        self.storico_accensioni.append(("spento", datetime.now()))

    def ore_di_utilizzo(self):
        """Calcola ore totali di utilizzo"""
        # Implementa logica di calcolo
        pass
```

### 🌟 Sfida 4: Monitoraggio consumi
```python
class SmartHome:
    def __init__(self, nome_casa):
        self.nome_casa = nome_casa
        self.elettrodomestici = []
        self.storico_consumi = []

    def registra_consumo(self):
        """Registra consumo attuale"""
        from datetime import datetime
        consumo = self.consumo_totale()
        self.storico_consumi.append((datetime.now(), consumo))

    def consumo_medio_giornaliero(self):
        """Calcola media consumi"""
        if self.storico_consumi:
            return sum(c[1] for c in self.storico_consumi) / len(self.storico_consumi)
        return 0
```

### 🌟 Sfida 5: Geolocalizzazione (allontana/avvicina)
```python
class SmartHome:
    def __init__(self, nome_casa):
        # ... altri attributi
        self.utenti_presenti = True

    def utenti_assenti(self):
        """Attivato quando utenti escono"""
        print("\n👋 Casa svuotata")
        self.spegni_tutto()
        # Attiva sensori antifurto
        for app in self.apparecchi_connessi():
            print(f"  📡 {app.nome} in standby")

    def utenti_tornano(self):
        """Attivato quando utenti rientrano"""
        print("\n👋 Bentornato!")
        # Accendi luci/riscaldamento
        for app in self.elettrodomestici:
            if app.nome in ["Luci", "Riscaldamento"]:
                app.accendi()
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Mix-in** | Classe ausiliaria riutilizzabile | Connettibile, Programmabile |
| **MRO** | Method Resolution Order | Lavatrice → Connettibile → ... |
| **super()** | Chiama metodo della classe seguente in MRO | super().__init__() |
| **Ereditarietà multipla** | Eredita da più classi | class X(A, B, C) |
| **Diamond problem** | Ambiguità in ereditarietà | Evitato con super() |
| **isinstance()** | Verifica tipo/capacità | isinstance(app, Connettibile) |
| ***args, **kwargs** | Parametri variabili | Passare a super() |

---

## 🔗 Link Utili

### Documentazione
- [Python MRO (Method Resolution Order)](https://docs.python.org/3/glossary.html#term-method-resolution-order)
- [super() Function](https://docs.python.org/3/library/functions.html#super)
- [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)

### Tutorial
- [Real Python - Multiple Inheritance](https://realpython.com/python-multiple-inheritance/)
- [C3 Linearization](https://en.wikipedia.org/wiki/C3_linearization)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Osserva come è implementato MRO
- Guarda come super() è usato nella catena
- Nota come sono progettati i mix-in
- Apprendi i pattern di ereditarietà multipla

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho creato la classe base `Elettrodomestico`
- [ ] Ho creato il mix-in `Connettibile` con WiFi/Bluetooth
- [ ] Ho creato il mix-in `Programmabile` con timer/programmi
- [ ] Ho implementato `Frigorifero` (Connettibile + Elettrodomestico)
- [ ] Ho implementato `Lavatrice` (Connettibile + Programmabile + Elettrodomestico)
- [ ] Ho implementato `Forno` (Programmabile + Elettrodomestico)
- [ ] Ho implementato `ForninoSmart` (Connettibile + Forno)
- [ ] Tutti i __init__ usano super() correttamente
- [ ] Ho creato la classe `SmartHome` per gestione
- [ ] SmartHome può accendere/spegnere tutto
- [ ] SmartHome calcola consumo totale
- [ ] SmartHome ricerca per tipo
- [ ] Ho testato con almeno 12 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile
- [ ] Ho stampato MRO per verificare

---

**Congratulazioni! Hai padroneggiato l'ereditarietà multipla! 🎉🏠**

*"L'ereditarietà multipla e i mix-in permettono di creare gerarchie di classi flessibili e riutilizzabili!"*
