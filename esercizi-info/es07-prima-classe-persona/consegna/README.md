# Es2: Prima Classe - Persona

## 📊 Informazioni Generali

**Livello:** 🟢 FACILE
**Durata stimata:** 3-4 ore
**Prerequisiti:** Es1 completato, funzioni Python, dizionari

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Creare** la tua prima classe personalizzata
- ✅ **Definire** il costruttore `__init__` con attributi
- ✅ **Scrivere** metodi di istanza (self)
- ✅ **Istanziare** oggetti e usarli
- ✅ **Organizzare** dati e comportamenti insieme
- ✅ **Capire** la differenza tra classe e oggetto

**Concetti fondamentali:**
- Classe come "modello" per creare oggetti
- `self` - il riferimento all'oggetto corrente
- `__init__` - il costruttore (inizializzatore)
- Attributi di istanza
- Metodi di istanza

---

## 📖 Descrizione

Sei pronto per **creare la tua prima classe**! Una classe `Persona` è il perfetto punto di partenza perché:

1. È semplice ma utile nella vita reale
2. Ha chiari attributi (nome, cognome, età)
3. Ha comportamenti logici (presentarsi, controllare maggiore età)
4. Ti farà capire come organizzare dati e funzioni insieme

Una classe **raggruppa dati e funzioni** che lavorano su quei dati. Invece di avere:
```python
nome = "Marco"
cognome = "Rossi"
eta = 25

def saluta_marco():
    print(f"Ciao, mi chiamo Marco Rossi")
```

Puoi avere:
```python
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} {self.cognome}")

marco = Persona("Marco", "Rossi", 25)
marco.saluta()  # Molto più elegante!
```

---

## 📝 Consegna Dettagliata

### Parte 1: Creare la Classe Base

**Definisci una classe `Persona` con:**

1. **Costruttore `__init__`** che riceve:
   - `nome` (stringa)
   - `cognome` (stringa)
   - `eta` (intero, anni)
   - Salva questi attributi nell'oggetto

2. **Metodo `saluta()`**
   - Stampa un saluto informale: "Ciao, mi chiamo {nome} {cognome}!"
   - Esempio: "Ciao, mi chiamo Marco Rossi!"

3. **Metodo `info()`**
   - Ritorna una stringa con le informazioni complete
   - Formato: "{nome} {cognome}, {eta} anni"
   - Esempio: "Marco Rossi, 25 anni"
   - Nota: `ritorna` (return) il risultato, non stamparlo!

4. **Metodo `è_maggiorenne()`** (o `is_maggiorenne()`)
   - Ritorna `True` se eta >= 18, altrimenti `False`
   - Non stampa nulla, solo ritorna il risultato

### Parte 2: Usare la Classe

**Scrivi un programma main che:**

1. **Crea almeno 5 oggetti Persona**
   - Usa nomi e eta diversi
   - Almeno 2 devono essere minorenni (eta < 18)
   - Almeno 2 devono essere maggiorenni

2. **Usa i metodi su ogni Persona**
   - Chiama `saluta()` su ogni persona
   - Stampa `info()` di ogni persona
   - Controlla se sono maggiorenni

3. **Crea una lista di persone**
   - Metti tutte le persone in una lista
   - Itera la lista stampando nome, cognome, eta, maggiorenne sì/no

4. **Operazioni su lista**
   - Trova la persona più giovane (min per eta)
   - Trova la persona più anziana (max per eta)
   - Calcola l'eta media
   - Conta quanti sono maggiorenni

### Parte 3: Estensioni (Opzionali ma Consigliate)

1. **Aggiungere il luogo di nascita**
   - Modifica `__init__` per aggiungere parametro `luogo`
   - Aggiorna il metodo `info()`

2. **Aggiungere un metodo per augurare buon compleanno**
   - Metodo `auguri_compleanno()`
   - Aumenta automaticamente l'eta di 1
   - Stampa un messaggio festoso
   - Esempio: "Auguri Marco! Ora hai 26 anni!"

3. **Verificare se due persone hanno la stessa eta**
   - Metodo `stessa_eta(altra_persona)`
   - Ritorna `True` se hanno la stessa eta, altrimenti `False`

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSE ============

class Persona:
    """Rappresenta una persona con nome, cognome e eta"""

    def __init__(self, nome, cognome, eta):
        """Inizializza una persona con i dati forniti"""
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        print(f"Persona creata: {nome} {cognome}")

    def saluta(self):
        """Stampa un saluto informale"""
        print(f"Ciao, mi chiamo {self.nome} {self.cognome}!")

    def info(self):
        """Ritorna una stringa con le informazioni"""
        return f"{self.nome} {self.cognome}, {self.eta} anni"

    def è_maggiorenne(self):
        """Ritorna True se è maggiorenne (>= 18)"""
        return self.eta >= 18

    # Estensioni
    def auguri_compleanno(self):
        """Augura il compleanno e aumenta l'eta"""
        self.eta += 1
        print(f"🎂 Auguri {self.nome}! Ora hai {self.eta} anni!")

    def stessa_eta(self, altra_persona):
        """Controlla se ha la stessa eta di un'altra persona"""
        return self.eta == altra_persona.eta


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    # Creare le persone
    print("=== CREAZIONE PERSONE ===")
    p1 = Persona("Marco", "Rossi", 25)
    p2 = Persona("Laura", "Verdi", 28)
    p3 = Persona("Giovanni", "Bianchi", 17)
    p4 = Persona("Alice", "Neri", 16)
    p5 = Persona("Andrea", "Blu", 30)

    # Lista di persone
    persone = [p1, p2, p3, p4, p5]

    # Usare i metodi
    print("\n=== SALUTI ===")
    for p in persone:
        p.saluta()

    print("\n=== INFORMAZIONI ===")
    for p in persone:
        print(p.info())

    print("\n=== CONTROLLO MAGGIORENNE ===")
    for p in persone:
        status = "maggiorenne" if p.è_maggiorenne() else "minorenne"
        print(f"{p.info()} - {status}")

    # Operazioni su lista
    print("\n=== STATISTICHE ===")

    # Persona più giovane
    piu_giovane = min(persone, key=lambda p: p.eta)
    print(f"Più giovane: {piu_giovane.info()}")

    # Persona più anziana
    piu_anziana = max(persone, key=lambda p: p.eta)
    print(f"Più anziana: {piu_anziana.info()}")

    # Eta media
    eta_media = sum(p.eta for p in persone) / len(persone)
    print(f"Eta media: {eta_media:.1f} anni")

    # Conta maggiorenni
    maggiorenni = sum(1 for p in persone if p.è_maggiorenne())
    print(f"Maggiorenni: {maggiorenni} su {len(persone)}")

    # Test estensioni
    print("\n=== ESTENSIONI ===")
    p1.auguri_compleanno()

    if p1.stessa_eta(p5):
        print(f"{p1.nome} e {p5.nome} hanno la stessa eta")
    else:
        print(f"{p1.nome} ({p1.eta}) e {p5.nome} ({p5.eta}) hanno eta diverse")

# Output atteso:
# Persona creata: Marco Rossi
# Persona creata: Laura Verdi
# ...
# === SALUTI ===
# Ciao, mi chiamo Marco Rossi!
# Ciao, mi chiamo Laura Verdi!
# ...
# === INFORMAZIONI ===
# Marco Rossi, 25 anni
# Laura Verdi, 28 anni
# ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione di una Persona
```python
p = Persona("Marco", "Rossi", 25)
assert p.nome == "Marco"
assert p.cognome == "Rossi"
assert p.eta == 25
print("✓ Test 1 passato")
```

### Test 2: Metodo info()
```python
p = Persona("Laura", "Verdi", 28)
info = p.info()
assert info == "Laura Verdi, 28 anni"
print("✓ Test 2 passato")
```

### Test 3: Metodo è_maggiorenne()
```python
p1 = Persona("Marco", "Rossi", 25)
p2 = Persona("Giovanni", "Bianchi", 17)
assert p1.è_maggiorenne() == True
assert p2.è_maggiorenne() == False
print("✓ Test 3 passato")
```

### Test 4: Operazioni su lista
```python
persone = [
    Persona("A", "X", 20),
    Persona("B", "Y", 30),
    Persona("C", "Z", 15),
]

# Test min (più giovane)
piu_giovane = min(persone, key=lambda p: p.eta)
assert piu_giovane.eta == 15

# Test max (più anziana)
piu_anziana = max(persone, key=lambda p: p.eta)
assert piu_anziana.eta == 30

# Test media
media = sum(p.eta for p in persone) / len(persone)
assert media == 21.66 or abs(media - 65/3) < 0.01

print("✓ Test 4 passato")
```

### Test 5: Auguri compleanno
```python
p = Persona("Marco", "Rossi", 25)
eta_prima = p.eta
p.auguri_compleanno()
assert p.eta == eta_prima + 1
print("✓ Test 5 passato")
```

### Test 6: Stessa eta
```python
p1 = Persona("Marco", "Rossi", 25)
p2 = Persona("Laura", "Verdi", 25)
p3 = Persona("Giovanni", "Bianchi", 30)

assert p1.stessa_eta(p2) == True
assert p1.stessa_eta(p3) == False
print("✓ Test 6 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Scrivi la struttura di base
```python
class Persona:
    def __init__(self, nome, cognome, eta):
        # Qui inizializza gli attributi
        pass

    def saluta(self):
        # Qui implementa il metodo
        pass
```

### Passo 2: Implementa `__init__`
```python
def __init__(self, nome, cognome, eta):
    self.nome = nome
    self.cognome = cognome
    self.eta = eta
```

**Cosa succede:**
- `self` rappresenta l'oggetto che stai creando
- `self.nome = nome` crea un attributo `nome` sull'oggetto
- Quando fai `p = Persona("Marco", "Rossi", 25)`, Python:
  1. Crea un nuovo oggetto Persona
  2. Chiama `__init__` automaticamente
  3. Passa "Marco", "Rossi", 25 come parametri

### Passo 3: Implementa `saluta()`
```python
def saluta(self):
    print(f"Ciao, mi chiamo {self.nome} {self.cognome}!")
```

**Nota:** non hai parametri aggiuntivi! Python passa `self` automaticamente.

### Passo 4: Implementa `info()`
```python
def info(self):
    return f"{self.nome} {self.cognome}, {self.eta} anni"
```

**Importante:** usa `return`, non `print`!

### Passo 5: Implementa `è_maggiorenne()`
```python
def è_maggiorenne(self):
    return self.eta >= 18
```

### Passo 6: Testa con poche persone
```python
# Prima di creare molti test, prova con uno
p = Persona("Marco", "Rossi", 25)
p.saluta()
print(p.info())
print(f"Maggiorenne: {p.è_maggiorenne()}")
```

### Passo 7: Aggiungi le estensioni
Una volta che la parte base funziona, aggiungi:
```python
def auguri_compleanno(self):
    self.eta += 1
    print(f"Auguri!")

def stessa_eta(self, altra_persona):
    return self.eta == altra_persona.eta
```

### Passo 8: Scrivi il programma principale
```python
if __name__ == "__main__":
    # Crea le persone
    p1 = Persona(...)
    p2 = Persona(...)

    # Testa i metodi
    # ...
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa docstring per spiegare la classe
```python
class Persona:
    """Rappresenta una persona con nome, cognome e eta.

    Attributi:
        nome (str): Nome della persona
        cognome (str): Cognome della persona
        eta (int): Eta in anni
    """
```

### ✅ Aggiungi docstring ai metodi
```python
def è_maggiorenne(self):
    """Controlla se la persona è maggiorenne.

    Returns:
        bool: True se eta >= 18, False altrimenti
    """
    return self.eta >= 18
```

### ✅ Crea un metodo `__str__()` per una stampa pulita
```python
def __str__(self):
    """Ritorna una rappresentazione leggibile dell'oggetto"""
    return f"{self.nome} {self.cognome}, {self.eta} anni"

# Ora puoi fare:
p = Persona("Marco", "Rossi", 25)
print(p)  # Stampa: Marco Rossi, 25 anni
```

### ✅ Usa type hints per chiarezza
```python
class Persona:
    def __init__(self, nome: str, cognome: str, eta: int) -> None:
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def è_maggiorenne(self) -> bool:
        return self.eta >= 18
```

### ✅ Valida i dati nel costruttore
```python
def __init__(self, nome: str, cognome: str, eta: int):
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("Nome deve essere una stringa non vuota")
    if eta < 0 or eta > 150:
        raise ValueError("Eta deve essere tra 0 e 150")

    self.nome = nome
    self.cognome = cognome
    self.eta = eta
```

### ✅ Usa f-string per formattazione elegante
```python
# BUONO
print(f"{self.nome} {self.cognome}")

# MENO BUONO
print(self.nome + " " + self.cognome)

# ANCORA MENO BUONO
print("{} {}".format(self.nome, self.cognome))
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare `self` come primo parametro
```python
# SBAGLIATO
class Persona:
    def saluta(nome, cognome):  # Manca self!
        print(f"Ciao {nome} {cognome}")

# GIUSTO
class Persona:
    def saluta(self):
        print(f"Ciao {self.nome} {self.cognome}")
```

### ❌ Errore 2: Usare `self.` come se fosse una variabile globale
```python
# SBAGLIATO
def info(self):
    nome = self.nome
    cognome = self.cognome
    eta = self.eta
    return nome + " " + cognome + ", " + str(eta) + " anni"

# GIUSTO - usa direttamente self.
def info(self):
    return f"{self.nome} {self.cognome}, {self.eta} anni"
```

### ❌ Errore 3: Non creare attributi in `__init__`
```python
# SBAGLIATO
class Persona:
    def __init__(self, nome):
        # Se non assegni qui, l'attributo non esiste!
        pass

    def saluta(self):
        print(self.nome)  # AttributeError!

# GIUSTO
class Persona:
    def __init__(self, nome):
        self.nome = nome  # Crea l'attributo

    def saluta(self):
        print(self.nome)  # Funziona!
```

### ❌ Errore 4: Confondere `print()` e `return`
```python
# SBAGLIATO
def info(self):
    print(f"{self.nome} {self.cognome}")  # Non ritorna nulla!

# Poi quando fai:
resultado = p.info()
print(resultado)  # None! L'output è stampato sopra

# GIUSTO
def info(self):
    return f"{self.nome} {self.cognome}"

resultado = p.info()
print(resultado)  # Stampa correttamente
```

### ❌ Errore 5: Modificare direttamente `self.eta` in operazioni
```python
# SBAGLIATO - modifica direttamente
p.eta = p.eta + 1  # Funziona ma non elegante

# GIUSTO - usa un metodo
def auguri_compleanno(self):
    self.eta += 1
    print(f"Auguri! Ora hai {self.eta} anni")

p.auguri_compleanno()
```

### ❌ Errore 6: Dimenticare le parentesi quando chiami un metodo
```python
# SBAGLIATO
p.saluta  # Ritorna il metodo, non lo esegue

# GIUSTO
p.saluta()  # Esegue il metodo
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Classe Famiglia
Crea una classe `Famiglia` che:
- Ha un attributo `nome_famiglia` (es: "Rossi")
- Ha una lista `membri` di Persona
- Metodo `aggiungi_membro(persona)` - aggiunge una persona
- Metodo `eta_media()` - calcola eta media della famiglia
- Metodo `elenca_membri()` - stampa tutti i membri

```python
class Famiglia:
    def __init__(self, nome_famiglia):
        self.nome_famiglia = nome_famiglia
        self.membri = []

    def aggiungi_membro(self, persona):
        self.membri.append(persona)

    # ... altri metodi ...

f = Famiglia("Rossi")
f.aggiungi_membro(Persona("Marco", "Rossi", 25))
f.aggiungi_membro(Persona("Laura", "Rossi", 28))
```

### 🌟 Sfida 2: Generazione Password Sicura
Aggiungi alla classe Persona:
- Metodo `genera_email(dominio="example.com")`
  - Ritorna: nome.cognome@dominio
  - Tutto minuscolo
  - Es: "marco.rossi@example.com"

```python
def genera_email(self, dominio="example.com"):
    return f"{self.nome.lower()}.{self.cognome.lower()}@{dominio}"
```

### 🌟 Sfida 3: Ordinare Persone per Criteri
Ordina una lista di persone per:
1. Eta (crescente e decrescente)
2. Nome (alfabetico)
3. Cognome (alfabetico)

```python
persone = [...]

# Per eta crescente
ordinati = sorted(persone, key=lambda p: p.eta)

# Per eta decrescente
ordinati = sorted(persone, key=lambda p: p.eta, reverse=True)

# Per nome
ordinati = sorted(persone, key=lambda p: p.nome)
```

### 🌟 Sfida 4: Relazioni tra Persone
Aggiungi metodi per relazioni:
- `è_più_giovane(altra_persona)` - ritorna True se self è più giovane
- `differenza_eta(altra_persona)` - ritorna la differenza di anni
- `è_adulto()` - True se > 21 anni (differente da maggiorenne)

```python
def è_più_giovane(self, altra_persona):
    return self.eta < altra_persona.eta

def differenza_eta(self, altra_persona):
    return abs(self.eta - altra_persona.eta)
```

### 🌟 Sfida 5: Generazione Automatica ID
Aggiungi un sistema di ID automatici:
- Ogni Persona riceve un ID unico incrementale
- Usa un attributo di classe `contatore_id`
- Ogni nuova Persona incrementa il contatore

```python
class Persona:
    contatore_id = 0  # Attributo di classe

    def __init__(self, nome, cognome, eta):
        Persona.contatore_id += 1
        self.id = Persona.contatore_id
        # ... rest ...

p1 = Persona("Marco", "Rossi", 25)  # id = 1
p2 = Persona("Laura", "Verdi", 28)  # id = 2
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **self** | Riferimento all'oggetto corrente | `self.nome = "Marco"` |
| **__init__** | Costruttore, inizializza l'oggetto | `def __init__(self, nome, eta)` |
| **Attributo** | Dato contenuto nell'oggetto | `self.nome`, `self.eta` |
| **Metodo** | Funzione dentro una classe | `def saluta(self)` |
| **Istanza** | Copia concreta di una classe | `p = Persona("Marco", 25)` |
| **Parametro** | Dato che il metodo riceve | `def __init__(self, nome)` |
| **return** | Ritorna un risultato dal metodo | `return f"{self.nome}"` |

---

## 🔗 Link Utili

### Documentazione Ufficiale
- [Python Classes - Docs](https://docs.python.org/3/tutorial/classes.html)
- [Python Class Objects](https://docs.python.org/3/tutorial/classes.html#class-objects)

### Tutorial
- [Real Python - Classes and Objects](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools - Python Classes](https://www.w3schools.com/python/python_classes.asp)

### Strumenti
- [Python Tutor](http://pythontutor.com/) - Visualizza come vengono creati gli oggetti
- [Visualizzatore classi online](https://gashimov.dev/python-visualizer/)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Leggi il tuo codice prima di guardare la soluzione
- Nota se hai usato nomi diversi per metodi/attributi
- Apprendi dai docstring e dai commenti
- Valuta se la tua implementazione è più semplice o più complessa
- Non copiare - usa come riferimento per migliorare!

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho definito correttamente la classe `Persona`
- [ ] Il costruttore `__init__` funziona correttamente
- [ ] Metodo `saluta()` stampa correttamente
- [ ] Metodo `info()` ritorna una stringa
- [ ] Metodo `è_maggiorenne()` ritorna un booleano
- [ ] Ho creato almeno 5 oggetti Persona
- [ ] Ho testato tutti i metodi
- [ ] Ho aggiunto le estensioni (almeno una)
- [ ] Il codice ha commenti/docstring
- [ ] Ho provato i casi di prova forniti

---

**Congratulazioni! Hai creato la tua prima classe! 🎉🐍**

*"Una classe ben progettata è il fondamento di un codice robusto e elegante."*
