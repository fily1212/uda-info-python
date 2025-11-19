# Es3: Classe con Metodi - Contatore

## 📊 Informazioni Generali

**Livello:** 🟡 BASE
**Durata stimata:** 3-4 ore
**Prerequisiti:** Es1-2 completati, funzioni Python

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Creare** metodi che modificano lo stato dell'oggetto
- ✅ **Gestire** limiti e vincoli su attributi
- ✅ **Implementare** la logica di business in metodi
- ✅ **Gestire errori** con try/except
- ✅ **Usare** metodi che non ritornano nulla (void)
- ✅ **Capire** quando un metodo deve stampare vs ritornare

**Concetti fondamentali:**
- Metodi che modificano lo stato (self.attributo = ...)
- Validazione dei dati
- Gestione eccezioni (ValueError)
- Metodi accessori (getter, setter semplici)
- Stato mutevole di un oggetto

---

## 📖 Descrizione

Un **Contatore** è un oggetto che mantiene un valore intero e permette di modificarlo. È un esercizio perfetto per imparare:

1. **Come i metodi modificano lo stato** - ogni chiamata a incrementa() cambia il valore
2. **Vincoli e limiti** - non puoi andare sotto zero, non puoi superare il massimo
3. **Gestione degli errori** - cosa fare se qualcuno prova a fare un'operazione non valida?
4. **L'importanza della validazione** - controllare che i parametri siano sensati

Un contatore potrebbe essere usato per:
- Contare i click su un bottone in un'app
- Gestire la quantità di prodotto in un magazzino
- Tenere traccia dei tentativi di login
- Contare i visitatori di un sito

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Contatore Base

**Definisci una classe `Contatore` con:**

1. **Costruttore `__init__`** che riceve:
   - `valore_iniziale` (intero, default = 0)
   - `minimo` (intero, default = 0) - il contatore non può scendere sotto questo
   - `massimo` (intero, default = 100) - il contatore non può salire sopra questo

2. **Metodo `incrementa()`**
   - Aumenta il valore di 1
   - Se il valore supererebbe il massimo, stampa un avviso: "Limite massimo raggiunto: X"
   - Non incrementa se già al massimo

3. **Metodo `decrementa()`**
   - Diminuisce il valore di 1
   - Se il valore scendererebbe sotto il minimo, stampa un avviso: "Limite minimo raggiunto: X"
   - Non decrementa se già al minimo

4. **Metodo `reset()`**
   - Riporta il valore al valore iniziale che era stato passato a `__init__`
   - Stampa: "Contatore resettato a X"

5. **Metodo `valore()`**
   - Ritorna il valore corrente del contatore
   - Non stampa nulla

6. **Metodo `aggiungi(n)`**
   - Aggiunge n al valore attuale (come incrementa, ma di n unità)
   - Rispetta i limiti minimo e massimo
   - Se non riesce ad aggiungere tutto, stampa avviso

7. **Metodo `sottrai(n)`**
   - Sottrae n dal valore attuale
   - Rispetta i limiti
   - Se non riesce a sottrarre tutto, stampa avviso

### Parte 2: Miglioramenti e Validazione

1. **Validazione nel costruttore**
   - Se `minimo > massimo`, scambia i valori oppure solleva un'eccezione
   - Se `valore_iniziale` non è tra minimo e massimo, stampa avviso e correggi

2. **Metodo `info()`**
   - Ritorna una stringa con: "Contatore: X (min: Y, max: Z, iniziale: W)"
   - Es: "Contatore: 45 (min: 0, max: 100, iniziale: 50)"

3. **Metodo `percentuale()`**
   - Ritorna la percentuale tra minimo e massimo
   - Formula: (valore - minimo) / (massimo - minimo) * 100
   - Es: se valore=50, min=0, max=100, ritorna 50.0

4. **Metodo `è_al_minimo()` e `è_al_massimo()`**
   - Ritornano True se il contatore è al limite

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSE ============

class Contatore:
    """Un contatore con limiti minimo e massimo"""

    def __init__(self, valore_iniziale=0, minimo=0, massimo=100):
        """Inizializza il contatore con validazione"""
        # Validazione: se minimo > massimo, scambiali
        if minimo > massimo:
            minimo, massimo = massimo, minimo
            print(f"Attenzione: minimo e massimo scambiati -> min={minimo}, max={massimo}")

        self.minimo = minimo
        self.massimo = massimo
        self.valore_iniziale = valore_iniziale

        # Se valore_iniziale è fuori dai limiti, correggi
        if valore_iniziale < minimo or valore_iniziale > massimo:
            self.valore_iniziale = minimo
            print(f"Attenzione: valore_iniziale fuori limiti, impostato a {minimo}")

        self.valore_attuale = self.valore_iniziale

    def incrementa(self):
        """Incrementa di 1, rispettando il massimo"""
        if self.valore_attuale >= self.massimo:
            print(f"Limite massimo raggiunto: {self.massimo}")
        else:
            self.valore_attuale += 1

    def decrementa(self):
        """Decrementa di 1, rispettando il minimo"""
        if self.valore_attuale <= self.minimo:
            print(f"Limite minimo raggiunto: {self.minimo}")
        else:
            self.valore_attuale -= 1

    def reset(self):
        """Riporta il contatore al valore iniziale"""
        self.valore_attuale = self.valore_iniziale
        print(f"Contatore resettato a {self.valore_attuale}")

    def valore(self):
        """Ritorna il valore corrente"""
        return self.valore_attuale

    def aggiungi(self, n):
        """Aggiunge n, rispettando il massimo"""
        nuovo_valore = min(self.valore_attuale + n, self.massimo)
        if nuovo_valore != self.valore_attuale + n:
            print(f"Avviso: limite massimo raggiunto. Aggiunto solo {nuovo_valore - self.valore_attuale}")
        self.valore_attuale = nuovo_valore

    def sottrai(self, n):
        """Sottrae n, rispettando il minimo"""
        nuovo_valore = max(self.valore_attuale - n, self.minimo)
        if nuovo_valore != self.valore_attuale - n:
            print(f"Avviso: limite minimo raggiunto. Sottratto solo {self.valore_attuale - nuovo_valore}")
        self.valore_attuale = nuovo_valore

    def info(self):
        """Ritorna info sul contatore"""
        return f"Contatore: {self.valore_attuale} (min: {self.minimo}, max: {self.massimo}, iniziale: {self.valore_iniziale})"

    def percentuale(self):
        """Ritorna la percentuale tra minimo e massimo"""
        range_totale = self.massimo - self.minimo
        if range_totale == 0:
            return 100.0  # Se min == max, è sempre al 100%
        return ((self.valore_attuale - self.minimo) / range_totale) * 100

    def è_al_minimo(self):
        """Ritorna True se al minimo"""
        return self.valore_attuale == self.minimo

    def è_al_massimo(self):
        """Ritorna True se al massimo"""
        return self.valore_attuale == self.massimo


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    print("=== CREAZIONE CONTATORI ===\n")

    # Contatore semplice (0-100)
    c1 = Contatore(50, 0, 100)
    print(c1.info())

    print("\n=== TEST INCREMENTA ===")
    for i in range(5):
        c1.incrementa()
        print(f"Dopo incrementa: {c1.valore()}")

    print("\n=== TEST DECREMENTA ===")
    for i in range(6):
        c1.decrementa()
        print(f"Dopo decrementa: {c1.valore()}")

    print("\n=== TEST AGGIUNGI/SOTTRAI ===")
    c1.aggiungi(20)
    print(f"Dopo aggiungi(20): {c1.valore()}")

    c1.aggiungi(50)  # Prova a superare il max
    print(f"Dopo aggiungi(50): {c1.valore()}")

    c1.sottrai(60)  # Prova a scendere sotto il min
    print(f"Dopo sottrai(60): {c1.valore()}")

    print("\n=== TEST PERCENTUALE ===")
    print(f"Percentuale: {c1.percentuale():.1f}%")
    print(f"Al minimo? {c1.è_al_minimo()}")
    print(f"Al massimo? {c1.è_al_massimo()}")

    print("\n=== TEST RESET ===")
    c1.reset()
    print(c1.info())

    print("\n=== CONTATORE SPECIALE (10-20) ===")
    c2 = Contatore(15, 10, 20)
    print(c2.info())

    for i in range(8):
        c2.incrementa()

    print(f"Dopo 8 incrementi: {c2.valore()}")
    print(f"Percentuale: {c2.percentuale():.1f}%")

    print("\n=== CONTATORE CON VALIDAZIONE ERRATA ===")
    c3 = Contatore(150, 0, 100)  # valore_iniziale fuori limiti
    print(c3.info())

    c4 = Contatore(50, 100, 0)  # minimo > massimo
    print(c4.info())

# Output atteso:
# Contatore: 50 (min: 0, max: 100, iniziale: 50)
# ...
# === TEST INCREMENTA ===
# Dopo incrementa: 51
# Dopo incrementa: 52
# ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione e valore iniziale
```python
c = Contatore(50, 0, 100)
assert c.valore() == 50
assert c.minimo == 0
assert c.massimo == 100
print("✓ Test 1 passato")
```

### Test 2: Incrementa
```python
c = Contatore(5, 0, 10)
c.incrementa()
assert c.valore() == 6
c.incrementa()
assert c.valore() == 7
print("✓ Test 2 passato")
```

### Test 3: Decrementa
```python
c = Contatore(5, 0, 10)
c.decrementa()
assert c.valore() == 4
c.decrementa()
assert c.valore() == 3
print("✓ Test 3 passato")
```

### Test 4: Limite massimo
```python
c = Contatore(10, 0, 10)
assert c.è_al_massimo() == True
c.incrementa()  # Non deve incrementare
assert c.valore() == 10
print("✓ Test 4 passato")
```

### Test 5: Limite minimo
```python
c = Contatore(0, 0, 10)
assert c.è_al_minimo() == True
c.decrementa()  # Non deve decrementare
assert c.valore() == 0
print("✓ Test 5 passato")
```

### Test 6: Reset
```python
c = Contatore(50, 0, 100)
c.incrementa()
c.incrementa()
c.reset()
assert c.valore() == 50
print("✓ Test 6 passato")
```

### Test 7: Aggiungi
```python
c = Contatore(50, 0, 100)
c.aggiungi(20)
assert c.valore() == 70
c.aggiungi(50)  # Supera massimo
assert c.valore() == 100  # Deve fermarsi a massimo
print("✓ Test 7 passato")
```

### Test 8: Sottrai
```python
c = Contatore(50, 0, 100)
c.sottrai(20)
assert c.valore() == 30
c.sottrai(50)  # Scende sotto minimo
assert c.valore() == 0  # Deve fermarsi a minimo
print("✓ Test 8 passato")
```

### Test 9: Percentuale
```python
c = Contatore(50, 0, 100)
assert c.percentuale() == 50.0

c = Contatore(75, 0, 100)
assert c.percentuale() == 75.0

c = Contatore(0, 0, 100)
assert c.percentuale() == 0.0

c = Contatore(100, 0, 100)
assert c.percentuale() == 100.0
print("✓ Test 9 passato")
```

### Test 10: Validazione costruttore
```python
# Test minimo > massimo
c = Contatore(50, 100, 0)
assert c.minimo == 0
assert c.massimo == 100

# Test valore fuori limiti
c = Contatore(200, 0, 100)
assert c.valore() == 0
print("✓ Test 10 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Struttura di base
```python
class Contatore:
    def __init__(self, valore_iniziale=0, minimo=0, massimo=100):
        self.valore_attuale = valore_iniziale
        self.minimo = minimo
        self.massimo = massimo
        self.valore_iniziale = valore_iniziale

    def valore(self):
        return self.valore_attuale
```

### Passo 2: Aggiungi incrementa() e decrementa()
```python
def incrementa(self):
    if self.valore_attuale >= self.massimo:
        print(f"Limite massimo raggiunto: {self.massimo}")
    else:
        self.valore_attuale += 1

def decrementa(self):
    if self.valore_attuale <= self.minimo:
        print(f"Limite minimo raggiunto: {self.minimo}")
    else:
        self.valore_attuale -= 1
```

### Passo 3: Aggiungi reset()
```python
def reset(self):
    self.valore_attuale = self.valore_iniziale
    print(f"Contatore resettato a {self.valore_attuale}")
```

### Passo 4: Testa la parte base
```python
c = Contatore(50, 0, 100)
c.incrementa()
print(c.valore())  # Deve essere 51
c.reset()
print(c.valore())  # Deve essere 50
```

### Passo 5: Aggiungi aggiungi() e sottrai()
```python
def aggiungi(self, n):
    nuovo = min(self.valore_attuale + n, self.massimo)
    if nuovo != self.valore_attuale + n:
        print(f"Avviso: limite massimo raggiunto")
    self.valore_attuale = nuovo

def sottrai(self, n):
    nuovo = max(self.valore_attuale - n, self.minimo)
    if nuovo != self.valore_attuale - n:
        print(f"Avviso: limite minimo raggiunto")
    self.valore_attuale = nuovo
```

### Passo 6: Aggiungi metodi informativi
```python
def info(self):
    return f"Contatore: {self.valore_attuale} (min: {self.minimo}, max: {self.massimo})"

def percentuale(self):
    range_totale = self.massimo - self.minimo
    if range_totale == 0:
        return 100.0
    return ((self.valore_attuale - self.minimo) / range_totale) * 100

def è_al_minimo(self):
    return self.valore_attuale == self.minimo

def è_al_massimo(self):
    return self.valore_attuale == self.massimo
```

### Passo 7: Aggiungi validazione
```python
def __init__(self, valore_iniziale=0, minimo=0, massimo=100):
    # Valida e scambia se necessario
    if minimo > massimo:
        minimo, massimo = massimo, minimo
        print(f"Minimo e massimo scambiati")

    self.minimo = minimo
    self.massimo = massimo
    self.valore_iniziale = valore_iniziale

    # Correggi valore_iniziale se fuori limiti
    if valore_iniziale < minimo or valore_iniziale > massimo:
        self.valore_iniziale = minimo
        print(f"Valore iniziale corretto a {minimo}")

    self.valore_attuale = self.valore_iniziale
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa `min()` e `max()` per gestire i limiti elegantemente
```python
# Invece di scrivere if/else lunghi:
if self.valore_attuale + n > self.massimo:
    self.valore_attuale = self.massimo
else:
    self.valore_attuale += n

# Usa min/max:
self.valore_attuale = min(self.valore_attuale + n, self.massimo)
```

### ✅ Valida i dati nel costruttore
```python
# Non aspettare che il codice fallisca, valida subito
if minimo > massimo:
    minimo, massimo = massimo, minimo
    print("Avviso: limiti corretti")
```

### ✅ Aggiungi costanti di default significative
```python
class Contatore:
    DEFAULT_MINIMO = 0
    DEFAULT_MASSIMO = 100

    def __init__(self, valore_iniziale=0, minimo=None, massimo=None):
        if minimo is None:
            minimo = self.DEFAULT_MINIMO
        # ...
```

### ✅ Documenta il comportamento ai limiti
```python
def incrementa(self):
    """Incrementa di 1.

    Se al massimo, non incrementa e stampa un avviso.
    """
    if self.valore_attuale >= self.massimo:
        print(f"Limite massimo raggiunto: {self.massimo}")
    else:
        self.valore_attuale += 1
```

### ✅ Crea test unitari
```python
def test_contatore():
    """Testa la classe Contatore"""
    c = Contatore(50, 0, 100)

    # Test incrementa
    c.incrementa()
    assert c.valore() == 51, "Incrementa fallito"

    # Test al limite
    c.valore_attuale = 100
    c.incrementa()
    assert c.valore() == 100, "Non dovrebbe superare massimo"

    print("Tutti i test passati!")

if __name__ == "__main__":
    test_contatore()
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare di controllare i limiti
```python
# SBAGLIATO
def incrementa(self):
    self.valore_attuale += 1  # Che succede se saliamo oltre massimo?

# GIUSTO
def incrementa(self):
    if self.valore_attuale < self.massimo:
        self.valore_attuale += 1
```

### ❌ Errore 2: Non validare nel costruttore
```python
# SBAGLIATO
def __init__(self, valore, minimo, massimo):
    self.valore_attuale = valore  # Se valore > massimo, che succede?

# GIUSTO
def __init__(self, valore, minimo, massimo):
    if valore < minimo or valore > massimo:
        valore = minimo
    self.valore_attuale = valore
```

### ❌ Errore 3: Non rispettare il design: stampare vs ritornare
```python
# SBAGLIATO - info() stampa ma non ritorna
def info(self):
    print(f"Valore: {self.valore_attuale}")

# GIUSTO - info() ritorna una stringa
def info(self):
    return f"Valore: {self.valore_attuale}"
```

### ❌ Errore 4: Usare nomi di variabili confusi
```python
# CONFUSO
def __init__(self, v, mn, mx):  # Cosa significano v, mn, mx?

# CHIARO
def __init__(self, valore_iniziale, minimo, massimo):
    # I nomi spiegano il significato
```

### ❌ Errore 5: Non gestire casi limite nella percentuale
```python
# SBAGLIATO
def percentuale(self):
    return (self.valore_attuale - self.minimo) / (self.massimo - self.minimo) * 100
    # Se massimo == minimo, divisione per zero!

# GIUSTO
def percentuale(self):
    range_totale = self.massimo - self.minimo
    if range_totale == 0:
        return 100.0
    return ((self.valore_attuale - self.minimo) / range_totale) * 100
```

### ❌ Errore 6: Mutare gli attributi da fuori la classe
```python
# SBAGLIATO - chiunque può fare questo
c = Contatore(50, 0, 100)
c.valore_attuale = 9999  # Ignora i limiti!

# GIUSTO - usa metodi che validano
c.aggiungi(9999)  # aggiungi valida i limiti
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Contatore con Storico
Registra ogni cambio di valore:
- Aggiungi attributo `storico = []`
- Quando il valore cambia, registra: (nuovo_valore, timestamp)
- Metodo `mostra_storico()` - stampa tutti i cambiamenti
- Metodo `numero_cambiamenti()` - ritorna quante volte è cambiato

```python
from datetime import datetime

def incrementa(self):
    if self.valore_attuale < self.massimo:
        self.valore_attuale += 1
        self.storico.append((self.valore_attuale, datetime.now()))
```

### 🌟 Sfida 2: Contatore Circolare
Un contatore che "torna indietro" al minimo quando raggiunge il massimo:
- Metodo `incrementa_circolare()` - se al massimo, torna a minimo
- Es: Contatore(0-10) → 9, 10, 0, 1, 2...

```python
def incrementa_circolare(self):
    if self.valore_attuale >= self.massimo:
        self.valore_attuale = self.minimo
    else:
        self.valore_attuale += 1
```

### 🌟 Sfida 3: Contatore con Callback
Quando si raggiunge il massimo/minimo, chiama una funzione:
- Parametri nel costruttore: `callback_minimo=None`, `callback_massimo=None`
- Quando raggiungi il limite, chiama la funzione: `callback_minimo()`

```python
def __init__(self, valore=0, minimo=0, massimo=100,
             callback_minimo=None, callback_massimo=None):
    # ...
    self.callback_minimo = callback_minimo
    self.callback_massimo = callback_massimo

def decrementa(self):
    if self.valore_attuale <= self.minimo:
        if self.callback_minimo:
            self.callback_minimo()
    else:
        self.valore_attuale -= 1
```

### 🌟 Sfida 4: Contatore con Moltiplicazione/Divisione
Aggiungi operazioni più complesse:
- `moltiplica(fattore)` - moltiplica il valore (rispettando limiti)
- `dividi(divisore)` - divide il valore (arrotonda)
- `quadrato()` - eleva al quadrato
- `radice_quadrata()` - radice quadrata

```python
import math

def quadrato(self):
    nuovo = min(self.valore_attuale ** 2, self.massimo)
    print(f"Quadrato: {self.valore_attuale}² = {nuovo}")
    self.valore_attuale = nuovo
```

### 🌟 Sfida 5: Comparazione tra Contatori
Aggiungi metodi per confrontare due contatori:
- `è_uguale(altro_contatore)` - stessi valori e limiti
- `è_maggiore_di(altro_contatore)` - questo > altro
- `è_minore_di(altro_contatore)` - questo < altro
- `somma_con(altro_contatore)` - crea nuovo contatore con somma dei valori

```python
def è_uguale(self, altro):
    return (self.valore_attuale == altro.valore_attuale and
            self.minimo == altro.minimo and
            self.massimo == altro.massimo)

def è_maggiore_di(self, altro):
    return self.valore_attuale > altro.valore_attuale
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Stato** | Il valore attuale dell'oggetto | `valore_attuale = 50` |
| **Mutazione** | Cambiamento dello stato | `incrementa()` cambia il valore |
| **Validazione** | Controllare che i dati siano validi | Controllare min <= valore <= max |
| **Limite** | Vincolo su quanto può variare il valore | minimo e massimo |
| **Reset** | Tornare allo stato iniziale | `reset()` |
| **Getter** | Metodo che ritorna un valore | `valore()` ritorna il valore attuale |
| **Info** | Metodo che mostra informazioni | `info()` ritorna una stringa descrittiva |

---

## 🔗 Link Utili

### Documentazione
- [Python Methods](https://docs.python.org/3/tutorial/classes.html#method-objects)
- [Built-in Functions - min, max](https://docs.python.org/3/library/functions.html#min)

### Concetti
- [Mutability in Python](https://realpython.com/python-mutable-immutable-objects/)
- [State in OOP](https://www.programiz.com/python-programming/object-oriented-programming)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Leggi il tuo codice prima di guardare la soluzione
- Nota come gestiscono i limiti
- Apprendi dai metodi di validazione
- Valuta se ci sono approcci più eleganti

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho definito correttamente la classe `Contatore`
- [ ] Il costruttore valida i dati
- [ ] Metodo `incrementa()` rispetta il massimo
- [ ] Metodo `decrementa()` rispetta il minimo
- [ ] Metodo `reset()` funziona correttamente
- [ ] Metodi `aggiungi()` e `sottrai()` rispettano i limiti
- [ ] Metodo `valore()` ritorna il valore
- [ ] Metodo `percentuale()` calcola correttamente
- [ ] Metodi `è_al_minimo()` e `è_al_massimo()` funzionano
- [ ] Ho testato tutti i casi limite
- [ ] Ho aggiunto le estensioni (almeno una)

---

**Congratulazioni! Hai implementato un sistema con stato e vincoli! 🎉🐍**

*"Un buon design di classe anticipare i problemi e gestirli gracefully."*
