# Es4: Attributi di Classe vs Istanza

## 📊 Informazioni Generali

**Livello:** 🟡 BASE
**Durata stimata:** 4-5 ore
**Prerequisiti:** Es1-3 completati, classe Contatore

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Distinguere** attributi di classe vs attributi di istanza
- ✅ **Creare** attributi di classe che sono condivisi tra istanze
- ✅ **Creare** attributi di istanza specifici per ogni oggetto
- ✅ **Gestire** conti bancari con informazioni globali
- ✅ **Contare** il numero totale di conti/oggetti creati
- ✅ **Usare** attributi statici per tenere traccia di dati globali

**Concetti fondamentali:**
- Attributi di istanza (self.attributo)
- Attributi di classe (Class.attributo)
- Variabili locali di istanza
- Variabili condivise tra istanze
- Accesso agli attributi di classe

---

## 📖 Descrizione

Fino a ora, hai lavorato solo con **attributi di istanza** - dati specifici per ogni oggetto. Ora imparerai che le classi possono avere anche **attributi di classe** - dati **condivisi** da tutti gli oggetti della classe.

**Esempio intuitivo:**
```
Classe: Umano
Attributi di istanza: nome, cognome, età (diversi per ogni persona)
Attributi di classe: numero_braccia = 2 (uguale per tutti gli umani!)
```

**Caso pratico: Banca**
```python
class ContoCorrente:
    tasso_interesse = 0.05  # ATTRIBUTO DI CLASSE - uguale per tutti i conti!
    numero_conti = 0        # ATTRIBUTO DI CLASSE - conta quanti conti sono creati

    def __init__(self, titolare, saldo):
        self.titolare = titolare        # ATTRIBUTO DI ISTANZA - diverso per ogni conto
        self.saldo = saldo              # ATTRIBUTO DI ISTANZA - diverso per ogni conto
        ContoCorrente.numero_conti += 1 # Incrementa il contatore condiviso
```

**Perché è importante?**
1. Dati che devono essere **uguali per tutti** (tassi di interesse, numero conti)
2. **Contatori globali** (quanti oggetti sono stati creati)
3. **Configurazioni** condivise da tutte le istanze
4. **Effetto di rete** - quando una istanza modifica l'attributo di classe, tutte lo vedono

---

## 📝 Consegna Dettagliata

### Parte 1: Classe ContoCorrente Base

**Definisci una classe `ContoCorrente` con:**

1. **Attributi di Classe:**
   - `tasso_interesse = 0.05` (5% - uguale per tutti i conti)
   - `numero_conti = 0` (contatore di conti aperti, incrementato ad ogni __init__)

2. **Attributi di Istanza (nel costruttore):**
   - `titolare` (nome del proprietario)
   - `saldo` (importo iniziale)
   - `numero_conto` (generato automaticamente: partendo da 1001, 1002, 1003...)

3. **Metodi di Istanza:**
   - `deposita(importo)` - aumenta il saldo
   - `preleva(importo)` - diminuisce il saldo (check se c'è abbastanza saldo)
   - `info()` - ritorna stringa: "Conto 1001 (Marco Rossi): 1000.00€"
   - `saldo_attuale()` - ritorna il saldo

4. **Metodo per gli interessi:**
   - `applica_interesse()` - aumenta il saldo di (saldo * tasso_interesse)
   - Stampa: "Interesse applicato: +X.XX€"

### Parte 2: Tracciamento del Numero di Conti

**Aggiungi:**

1. **Metodo di classe `get_numero_conti()`** (o `numero_conti_aperti()`)
   - Ritorna quanti conti sono stati creati in totale
   - Usa `@classmethod` oppure accedi direttamente `ContoCorrente.numero_conti`

2. **Metodo di classe `modifica_tasso_interesse(nuovo_tasso)`**
   - Cambia il tasso per TUTTI i conti
   - Stampa avviso: "Tasso interesse cambiato a X%"
   - Tutti i conti vedranno il nuovo tasso

3. **Mostra la differenza** tra attributi di istanza e di classe:
   - Crea 3 conti
   - Modifica il tasso con il metodo di classe
   - Verifica che tutti vedono il nuovo tasso

### Parte 3: Operazioni Bancarie

**Aggiungi metodi utili:**

1. **`trasferisci(conto_destinatario, importo)`**
   - Preleva da questo conto
   - Deposita nel conto destinatario
   - Controlla se c'è abbastanza saldo
   - Stampa: "Trasferimento 100€ da 1001 a 1002"

2. **`calcola_saldo_con_interessi()`**
   - Ritorna quanto sarebbero i soldi DOPO aver applicato gli interessi
   - Non modifica il saldo, solo calcola

3. **Metodo di classe `conta_conti_ricchi(sogliaMinima)`** (Bonus)
   - Ritorna quanti conti hanno saldo > soglia
   - Nota: questo è complicato, vedi nel bonus

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSE ============

class ContoCorrente:
    """Rappresenta un conto corrente bancario"""

    # ATTRIBUTI DI CLASSE - condivisi da tutte le istanze
    tasso_interesse = 0.05  # 5%
    numero_conti = 0
    prossimo_numero_conto = 1001

    def __init__(self, titolare, saldo_iniziale):
        """Crea un nuovo conto corrente"""
        # Incrementa il contatore globale
        ContoCorrente.numero_conti += 1

        # ATTRIBUTI DI ISTANZA - specifici per ogni conto
        self.titolare = titolare
        self.saldo = saldo_iniziale
        self.numero_conto = ContoCorrente.prossimo_numero_conto
        ContoCorrente.prossimo_numero_conto += 1

        print(f"Conto creato: {self.numero_conto} ({titolare})")

    def deposita(self, importo):
        """Deposita soldi nel conto"""
        if importo <= 0:
            print("Errore: importo deve essere positivo")
            return False
        self.saldo += importo
        print(f"Depositato {importo}€. Nuovo saldo: {self.saldo}€")
        return True

    def preleva(self, importo):
        """Preleva soldi dal conto"""
        if importo <= 0:
            print("Errore: importo deve essere positivo")
            return False
        if importo > self.saldo:
            print(f"Errore: saldo insufficiente! (hai {self.saldo}€)")
            return False
        self.saldo -= importo
        print(f"Prelevato {importo}€. Nuovo saldo: {self.saldo}€")
        return True

    def info(self):
        """Ritorna informazioni sul conto"""
        return f"Conto {self.numero_conto} ({self.titolare}): {self.saldo:.2f}€"

    def saldo_attuale(self):
        """Ritorna il saldo attuale"""
        return self.saldo

    def applica_interesse(self):
        """Applica gli interessi al saldo"""
        interesse = self.saldo * ContoCorrente.tasso_interesse
        self.saldo += interesse
        print(f"Interesse applicato: +{interesse:.2f}€. Nuovo saldo: {self.saldo:.2f}€")

    def calcola_saldo_con_interessi(self):
        """Ritorna quanto sarebbero i soldi con gli interessi applicati"""
        return self.saldo * (1 + ContoCorrente.tasso_interesse)

    def trasferisci(self, conto_destinatario, importo):
        """Trasferisce soldi a un altro conto"""
        if self.preleva(importo):
            conto_destinatario.deposita(importo)
            print(f"Trasferimento {importo}€ da {self.numero_conto} a {conto_destinatario.numero_conto} completato")
            return True
        return False

    # METODO DI CLASSE - usa @classmethod
    @classmethod
    def get_numero_conti(cls):
        """Ritorna il numero totale di conti creati"""
        return cls.numero_conti

    @classmethod
    def modifica_tasso_interesse(cls, nuovo_tasso):
        """Modifica il tasso di interesse per TUTTI i conti"""
        cls.tasso_interesse = nuovo_tasso
        print(f"Tasso interesse modificato a {nuovo_tasso * 100}% per TUTTI i conti")


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    print("=== CREAZIONE CONTI ===\n")

    # Creiamo 3 conti
    c1 = ContoCorrente("Marco Rossi", 1000)
    c2 = ContoCorrente("Laura Verdi", 2000)
    c3 = ContoCorrente("Giovanni Bianchi", 500)

    print(f"\nConti creati: {ContoCorrente.get_numero_conti()}")
    print(f"Prossimo numero conto: {ContoCorrente.prossimo_numero_conto}")

    print("\n=== INFORMAZIONI CONTI ===")
    print(c1.info())
    print(c2.info())
    print(c3.info())

    print("\n=== OPERAZIONI BANCARIE ===")
    c1.deposita(500)
    c2.preleva(300)
    c3.preleva(1000)  # Fallisce - saldo insufficiente

    print("\n=== APPLICAZIONE INTERESSI ===")
    print(f"Tasso di interesse attuale: {ContoCorrente.tasso_interesse * 100}%")
    c1.applica_interesse()
    c2.applica_interesse()

    print("\n=== CAMBIO TASSO INTERESSE ===")
    print(f"Cambio il tasso per TUTTI i conti a 10%")
    ContoCorrente.modifica_tasso_interesse(0.10)

    print(f"Nuovo tasso: {ContoCorrente.tasso_interesse * 100}%")
    print(f"Saldo con nuovi interessi (c1): {c1.calcola_saldo_con_interessi():.2f}€")

    print("\n=== TRASFERIMENTI ===")
    c1.trasferisci(c2, 100)
    c3.trasferisci(c1, 50)

    print("\n=== SITUAZIONE FINALE ===")
    print(c1.info())
    print(c2.info())
    print(c3.info())
    print(f"Conti totali: {ContoCorrente.get_numero_conti()}")

# Output atteso:
# === CREAZIONE CONTI ===
# Conto creato: 1001 (Marco Rossi)
# Conto creato: 1002 (Laura Verdi)
# Conto creato: 1003 (Giovanni Bianchi)
# Conti creati: 3
# ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione e numero conto
```python
c1 = ContoCorrente("Marco", 1000)
c2 = ContoCorrente("Laura", 2000)
assert c1.numero_conto == 1001
assert c2.numero_conto == 1002
assert ContoCorrente.get_numero_conti() == 2
print("✓ Test 1 passato")
```

### Test 2: Attributi di istanza diversi
```python
c1 = ContoCorrente("Marco", 1000)
c2 = ContoCorrente("Laura", 2000)
assert c1.saldo == 1000
assert c2.saldo == 2000
assert c1.titolare != c2.titolare
print("✓ Test 2 passato")
```

### Test 3: Tasso di interesse condiviso
```python
c1 = ContoCorrente("Marco", 1000)
c2 = ContoCorrente("Laura", 2000)

# Inizialmente lo stesso
assert c1.tasso_interesse == c2.tasso_interesse

# Modifichiamo il tasso
ContoCorrente.modifica_tasso_interesse(0.10)

# Entrambi vedono il nuovo tasso!
assert c1.tasso_interesse == 0.10
assert c2.tasso_interesse == 0.10
print("✓ Test 3 passato")
```

### Test 4: Deposita e preleva
```python
c = ContoCorrente("Marco", 1000)
c.deposita(500)
assert c.saldo == 1500

c.preleva(300)
assert c.saldo == 1200

# Prova a prelevare più del saldo
assert c.preleva(2000) == False
assert c.saldo == 1200
print("✓ Test 4 passato")
```

### Test 5: Interessi
```python
ContoCorrente.modifica_tasso_interesse(0.05)  # 5%
c = ContoCorrente("Marco", 1000)
c.applica_interesse()
assert abs(c.saldo - 1050) < 0.01
print("✓ Test 5 passato")
```

### Test 6: Calcola saldo con interessi
```python
ContoCorrente.modifica_tasso_interesse(0.10)  # 10%
c = ContoCorrente("Marco", 1000)
saldo_con_interessi = c.calcola_saldo_con_interessi()
assert saldo_con_interessi == 1100
assert c.saldo == 1000  # Non modifica il saldo effettivo
print("✓ Test 6 passato")
```

### Test 7: Trasferisci
```python
c1 = ContoCorrente("Marco", 1000)
c2 = ContoCorrente("Laura", 500)
c1.trasferisci(c2, 200)
assert c1.saldo == 800
assert c2.saldo == 700
print("✓ Test 7 passato")
```

### Test 8: Numero conti incrementale
```python
ContoCorrente.numero_conti = 0  # Reset per il test
ContoCorrente.prossimo_numero_conto = 1001

c1 = ContoCorrente("A", 100)
c2 = ContoCorrente("B", 200)
c3 = ContoCorrente("C", 300)

assert c1.numero_conto == 1001
assert c2.numero_conto == 1002
assert c3.numero_conto == 1003
assert ContoCorrente.get_numero_conti() == 3
print("✓ Test 8 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Definisci gli attributi di classe
```python
class ContoCorrente:
    # ATTRIBUTI DI CLASSE (prima di __init__)
    tasso_interesse = 0.05
    numero_conti = 0
    prossimo_numero_conto = 1001
```

### Passo 2: Implementa `__init__` con incremento del contatore
```python
def __init__(self, titolare, saldo_iniziale):
    # Incrementa il contatore di classe
    ContoCorrente.numero_conti += 1

    # Attributi di istanza
    self.titolare = titolare
    self.saldo = saldo_iniziale
    self.numero_conto = ContoCorrente.prossimo_numero_conto
    ContoCorrente.prossimo_numero_conto += 1
```

**Importante:** Accedi agli attributi di classe con `ContoCorrente.attributo` o `self.__class__.attributo`

### Passo 3: Implementa metodi base
```python
def deposita(self, importo):
    if importo > 0:
        self.saldo += importo
        return True
    return False

def preleva(self, importo):
    if importo > 0 and importo <= self.saldo:
        self.saldo -= importo
        return True
    return False
```

### Passo 4: Implementa il metodo di classe
```python
@classmethod
def get_numero_conti(cls):
    """Ritorna quanti conti totali sono stati creati"""
    return cls.numero_conti

@classmethod
def modifica_tasso_interesse(cls, nuovo_tasso):
    """Modifica il tasso per TUTTI i conti"""
    cls.tasso_interesse = nuovo_tasso
```

**Nota:** nei metodi di classe, usi `cls` invece di `self` e `cls.attributo` per accedere agli attributi di classe

### Passo 5: Testa gli attributi di classe
```python
c1 = ContoCorrente("Marco", 1000)
c2 = ContoCorrente("Laura", 2000)

# Verifica che il numero conto è incrementale
assert c1.numero_conto == 1001
assert c2.numero_conto == 1002

# Verifica che il tasso è condiviso
print(c1.tasso_interesse)  # 0.05
ContoCorrente.modifica_tasso_interesse(0.10)
print(c1.tasso_interesse)  # 0.10 - cambiato!
```

### Passo 6: Implementa metodi di utilità
```python
def info(self):
    return f"Conto {self.numero_conto} ({self.titolare}): {self.saldo:.2f}€"

def applica_interesse(self):
    interesse = self.saldo * ContoCorrente.tasso_interesse
    self.saldo += interesse

def calcola_saldo_con_interessi(self):
    return self.saldo * (1 + ContoCorrente.tasso_interesse)
```

### Passo 7: Implementa trasferisci
```python
def trasferisci(self, conto_destinatario, importo):
    if self.preleva(importo):
        conto_destinatario.deposita(importo)
        return True
    return False
```

### Passo 8: Testa tutto insieme
```python
if __name__ == "__main__":
    c1 = ContoCorrente("Marco", 1000)
    c2 = ContoCorrente("Laura", 2000)

    print(c1.info())
    print(c2.info())

    c1.deposita(500)
    c1.trasferisci(c2, 200)
    ContoCorrente.modifica_tasso_interesse(0.10)
    c1.applica_interesse()

    print(c1.info())
```

---

## 💡 Trucchi e Best Practices

### ✅ Distingui chiaramente attributi di classe vs istanza
```python
class ContoCorrente:
    # CLASSE - definiti PRIMA di __init__
    tasso_interesse = 0.05
    numero_conti = 0

    def __init__(self, titolare, saldo):
        # ISTANZA - definiti dentro __init__
        self.titolare = titolare
        self.saldo = saldo
```

### ✅ Usa @classmethod per operazioni globali
```python
@classmethod
def modifica_tasso_interesse(cls, nuovo_tasso):
    """Modifica il tasso GLOBALE"""
    cls.tasso_interesse = nuovo_tasso

# Non farlo nei metodi normali!
# def modifica_tasso(self, nuovo_tasso):  # SBAGLIATO
#     self.tasso_interesse = nuovo_tasso
```

### ✅ Documenta chiaramente quali sono attributi di classe
```python
class ContoCorrente:
    """Conto corrente bancario

    Attributi di classe:
        tasso_interesse: float - tasso applicato a TUTTI i conti
        numero_conti: int - quanti conti sono stati creati
        prossimo_numero_conto: int - numero da assegnare al prossimo conto

    Attributi di istanza:
        titolare: str - nome del proprietario
        saldo: float - importo disponibile
        numero_conto: int - numero univoco del conto
    """
```

### ✅ Usa un metodo di classe factory se serve inizializzazione speciale
```python
@classmethod
def conto_vip(cls, titolare):
    """Factory method: crea un conto VIP con saldo iniziale maggiore"""
    return cls(titolare, 50000)

c_vip = ContoCorrente.conto_vip("Marco")  # Saldo = 50000
```

### ✅ Crea metodi di classe per statistiche globali
```python
@classmethod
def saldo_totale_tutti_conti(cls):
    """Ritorna il saldo totale di TUTTI i conti"""
    # Nota: questo è complicato senza una lista globale!
    # Vedi il bonus per come farlo
    pass
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Confondere attributi di classe e istanza
```python
# SBAGLIATO - accedi male agli attributi di classe
def modifica_tasso(self, nuovo_tasso):
    self.tasso_interesse = nuovo_tasso  # Crea attributo di ISTANZA, non modifica la classe!

# GIUSTO - accedi agli attributi di classe
def modifica_tasso(self, nuovo_tasso):
    ContoCorrente.tasso_interesse = nuovo_tasso  # Modifica l'attributo di CLASSE

# O meglio, usa @classmethod
@classmethod
def modifica_tasso(cls, nuovo_tasso):
    cls.tasso_interesse = nuovo_tasso
```

### ❌ Errore 2: Dimenticare di incrementare il contatore nel costruttore
```python
# SBAGLIATO
def __init__(self, titolare, saldo):
    # numero_conti non viene incrementato!
    self.titolare = titolare

# GIUSTO
def __init__(self, titolare, saldo):
    ContoCorrente.numero_conti += 1  # Incrementa il contatore
    self.titolare = titolare
```

### ❌ Errore 3: Usare lo stesso numero di conto per due conti
```python
# SBAGLIATO
def __init__(self, titolare, saldo):
    self.numero_conto = 1001  # Uguale per tutti!

# GIUSTO
def __init__(self, titolare, saldo):
    self.numero_conto = ContoCorrente.prossimo_numero_conto
    ContoCorrente.prossimo_numero_conto += 1
```

### ❌ Errore 4: Modificare un attributo di istanza quando volevi modificare quello di classe
```python
c1 = ContoCorrente("Marco", 1000)
c2 = ContoCorrente("Laura", 2000)

# SBAGLIATO - modifica solo c1
c1.tasso_interesse = 0.10
print(c2.tasso_interesse)  # Ancora 0.05! C1 ha il suo attributo privato

# GIUSTO - modifica la classe, quindi tutti vedono il cambio
ContoCorrente.tasso_interesse = 0.10
print(c2.tasso_interesse)  # 0.10
```

### ❌ Errore 5: Non validare gli importi
```python
# SBAGLIATO - permette importi negativi
def deposita(self, importo):
    self.saldo += importo

# GIUSTO - valida
def deposita(self, importo):
    if importo <= 0:
        return False
    self.saldo += importo
    return True
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Traccia i Conti Creati
Mantieni una lista di TUTTI i conti per poter fare statistiche:

```python
class ContoCorrente:
    # ...
    lista_conti = []  # NUOVO: lista di tutti i conti

    def __init__(self, titolare, saldo):
        ContoCorrente.numero_conti += 1
        # ...
        ContoCorrente.lista_conti.append(self)  # Aggiungi alla lista

    @classmethod
    def saldo_totale_tutti(cls):
        """Ritorna il saldo totale di TUTTI i conti"""
        return sum(c.saldo for c in cls.lista_conti)

    @classmethod
    def conto_piu_ricco(cls):
        """Ritorna il conto con il saldo maggiore"""
        return max(cls.lista_conti, key=lambda c: c.saldo)
```

### 🌟 Sfida 2: Commissioni Variabili
Aggiungi una commissione che cambia per tutti:

```python
class ContoCorrente:
    commissione_prelievo = 0.01  # 1% di commissione

    def preleva(self, importo):
        # Calcola commissione
        commissione = importo * ContoCorrente.commissione_prelievo
        totale = importo + commissione
        if totale > self.saldo:
            return False
        self.saldo -= totale
        return True

    @classmethod
    def modifica_commissione(cls, nuova_commissione):
        cls.commissione_prelievo = nuova_commissione
```

### 🌟 Sfida 3: Conto Bloccato
Aggiungi uno stato di blocco/sblocco:

```python
class ContoCorrente:
    def __init__(self, titolare, saldo):
        # ...
        self.bloccato = False

    def blocca_conto(self):
        """Blocca il conto - non si può prelevare"""
        self.bloccato = True

    def sblocca_conto(self):
        """Sblocca il conto"""
        self.bloccato = False

    def preleva(self, importo):
        if self.bloccato:
            print("Conto bloccato!")
            return False
        # ... resto del codice
```

### 🌟 Sfida 4: Sconto su Commissioni per VIP
I clienti VIP pagano meno commissioni:

```python
class ContoCorrente:
    commissione_standard = 0.01
    commissione_vip = 0.005

    def __init__(self, titolare, saldo, vip=False):
        # ...
        self.vip = vip

    @property
    def commissione(self):
        """Ritorna la commissione per questo conto"""
        return self.commissione_vip if self.vip else self.commissione_standard

    def preleva(self, importo):
        commissione = importo * self.commissione
        totale = importo + commissione
        if totale > self.saldo:
            return False
        self.saldo -= totale
        return True
```

### 🌟 Sfida 5: Limite di Prelievo Giornaliero
Aggiungi un limite che si resetta ogni giorno:

```python
from datetime import datetime, timedelta

class ContoCorrente:
    def __init__(self, titolare, saldo):
        # ...
        self.limite_prelievo_giorno = 1000  # Max 1000€ al giorno
        self.prelievi_oggi = 0
        self.ultimo_prelievo_giorno = datetime.now().date()

    def _reset_prelievi_se_nuovo_giorno(self):
        """Resetta i prelievi se è un nuovo giorno"""
        oggi = datetime.now().date()
        if oggi > self.ultimo_prelievo_giorno:
            self.prelievi_oggi = 0
            self.ultimo_prelievo_giorno = oggi

    def preleva(self, importo):
        self._reset_prelievi_se_nuovo_giorno()

        if self.prelievi_oggi + importo > self.limite_prelievo_giorno:
            print(f"Limite giornaliero superato!")
            return False

        if importo > self.saldo:
            return False

        self.saldo -= importo
        self.prelievi_oggi += importo
        return True
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Attributo di classe** | Condiviso da TUTTI gli oggetti | `tasso_interesse = 0.05` |
| **Attributo di istanza** | Specifico per ogni oggetto | `self.saldo = 1000` |
| **@classmethod** | Metodo che lavora sulla classe | `def modifica_tasso(cls)` |
| **cls** | Riferimento alla classe (come self per istanze) | `cls.numero_conti` |
| **Variabile globale** | Contatore o dato condiviso | `numero_conti = 0` |
| **Factory** | Metodo di classe che crea istanze speciali | `@classmethod def conto_vip()` |

---

## 🔗 Link Utili

### Documentazione
- [Python Class Attributes](https://docs.python.org/3/tutorial/classes.html#class-definition)
- [Class vs Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [@classmethod Decorator](https://docs.python.org/3/library/functions.html#classmethod)

### Tutorial
- [Real Python - Class Variables](https://realpython.com/class-variables-python/)
- [Real Python - @classmethod](https://realpython.com/instance-class-static-methods-explained/)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Nota come vengono usati gli attributi di classe
- Guarda come è implementato il metodo di classe
- Apprendi dall'uso di @classmethod vs metodi normali

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho definito gli attributi di classe (tasso_interesse, numero_conti)
- [ ] Il costruttore incrementa il numero di conti
- [ ] Ogni conto riceve un numero univoco
- [ ] Metodo deposita/preleva funziona correttamente
- [ ] Metodo applica_interesse usa il tasso di classe
- [ ] Metodo di classe modifica_tasso_interesse cambia il tasso per TUTTI
- [ ] Ho verificato che il tasso è condiviso (modifica su uno = modifica su tutti)
- [ ] Metodo trasferisci funziona correttamente
- [ ] Ho testato tutti i casi limite
- [ ] Ho aggiunto le estensioni (almeno una)

---

**Congratulazioni! Hai imparato la differenza cruciale tra attributi di classe e istanza! 🎉🐍**

*"Gli attributi di classe sono la chiave per tracciare informazioni globali in una gerarchia di oggetti."*
