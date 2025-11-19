# Es1: Usare Classi Esistenti

## 📊 Informazioni Generali

**Livello:** 🟢 FACILE
**Durata stimata:** 2-3 ore
**Prerequisiti:** Funzioni Python, liste, dizionari, import moduli

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Utilizzare** classi già pronte dalle librerie Python standard
- ✅ **Leggere** la documentazione ufficiale di Python
- ✅ **Creare oggetti** (istanze) da classi esistenti
- ✅ **Usare metodi** forniti dalle classi
- ✅ **Lavorare con** datetime, collections.Counter, namedtuple
- ✅ **Risolvere problemi reali** senza dover programmare le classi da zero

**Concetti fondamentali:**
- Classe vs oggetto (istanza)
- Metodi di un oggetto
- Attributi di un oggetto
- Importare e usare moduli

---

## 📖 Descrizione

Prima di **imparare a scrivere classi**, devi capire come **usarle**. Python mette a disposizione tante classi già pronte nelle sue librerie standard. Questo esercizio ti insegna a:

1. Usare la classe `datetime` per calcolare date, ore e giorni
2. Usare `collections.Counter` per contare frequenze
3. Usare `namedtuple` per creare oggetti strutturati
4. Esplorare la documentazione per scoprire i metodi disponibili

Iniziando con classi già pronte, capirai i **principi fondamentali** prima di crearne di tue.

---

## 📝 Consegna Dettagliata

### Parte 1: Lavorare con `datetime`

La classe `datetime` permette di lavorare con date, ore e intervalli di tempo.

**Crea un programma che:**

1. **Calcola l'età di una persona**
   - Prendi la data di nascita (come stringa o come oggetto datetime)
   - Usa `datetime.now()` per ottenere la data odierna
   - Calcola la differenza in anni (e mesi/giorni se possibile)
   - Stampa "Hai X anni, Y mesi, Z giorni"

2. **Calcola i giorni rimanenti fino a una data importante**
   - Data di riferimento: il tuo compleanno, capodanno, o una data a scelta
   - Calcola quanti giorni rimangono
   - Mostra il numero di settimane

3. **Analizza una serie di date**
   - Crea una lista di almeno 5 date importanti (date di storiche, eventi, etc.)
   - Ordina le date (usa il metodo di sorting)
   - Mostra quale è la più vecchia e quale la più recente
   - Mostra gli intervalli tra date consecutive

### Parte 2: Contare Frequenze con `Counter`

La classe `Counter` (da `collections`) conta quante volte appare ogni elemento in una collezione.

**Crea un programma che:**

1. **Analizza la frequenza di parole**
   - Prendi un testo (può essere una frase, un paragrafo, una riga di codice)
   - Usa `Counter` per contare quante volte appare ogni parola
   - Mostra le 5 parole più frequenti
   - Ignora maiuscole/minuscole (trasforma tutto in minuscolo)

2. **Analizza frequenza di caratteri**
   - Prendi una stringa (es: "programmazione")
   - Conta quante volte appare ogni lettera
   - Mostra le lettere in ordine di frequenza
   - Calcola la percentuale di ogni lettera

3. **Conta elementi in una lista**
   - Crea una lista di numeri (con ripetizioni: [1,2,2,3,3,3,4,4,4,4,...])
   - Usa Counter per contare frequenze
   - Mostra i dati in modo leggibile

### Parte 3: Oggetti Strutturati con `namedtuple`

`namedtuple` crea oggetti con attributi nominati (più leggibili rispetto a tuple normali).

**Crea un programma che:**

1. **Definisci una namedtuple `Persona`**
   - Campi: nome, cognome, età, città
   - Crea almeno 5 oggetti Persona
   - Stampa i dati in modo formattato

2. **Definisci una namedtuple `Voto`**
   - Campi: materia, voto, data
   - Crea una lista di almeno 10 voti
   - Mostra i voti in ordine di data
   - Calcola la media per materia

3. **Combina namedtuple con altre classi**
   - Crea una namedtuple `Punto` (x, y)
   - Calcola la distanza tra due punti usando la formula: √((x2-x1)² + (y2-y1)²)
   - Usa `math.sqrt` o `**0.5`

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ PARTE 1: DATETIME ============

from datetime import datetime, timedelta

# Calcolare l'età
data_nascita = datetime(1995, 3, 15)  # 15 marzo 1995
oggi = datetime.now()

eta_giorni = (oggi - data_nascita).days
eta_anni = eta_giorni // 365
eta_mesi = (eta_giorni % 365) // 30

print(f"Sei nato il: {data_nascita.strftime('%d/%m/%Y')}")
print(f"Eta: {eta_anni} anni e {eta_mesi} mesi")
print(f"Totale giorni: {eta_giorni}")

# Giorni fino a Natale
natale = datetime(2024, 12, 25)
giorni_natale = (natale - oggi).days
print(f"\nGiorni fino a Natale: {giorni_natale}")

# ============ PARTE 2: COUNTER ============

from collections import Counter

# Contare parole in un testo
testo = "Python è fantastico. Python è potente. Python è usato dappertutto."
parole = testo.lower().split()
contatore = Counter(parole)

print(f"\nFrequenza parole:")
for parola, freq in contatore.most_common(5):
    print(f"  {parola}: {freq} volte")

# Contare caratteri
stringa = "programmazione"
freq_lettere = Counter(stringa)
print(f"\nFrequenza lettere in '{stringa}':")
for lettera, freq in freq_lettere.most_common():
    print(f"  {lettera}: {freq}")

# ============ PARTE 3: NAMEDTUPLE ============

from collections import namedtuple

# Creare una namedtuple
Persona = namedtuple('Persona', ['nome', 'cognome', 'eta', 'citta'])

# Creare oggetti
persone = [
    Persona('Marco', 'Rossi', 25, 'Roma'),
    Persona('Laura', 'Verdi', 28, 'Milano'),
    Persona('Giovanni', 'Bianchi', 22, 'Napoli'),
]

print(f"\nPersone:")
for p in persone:
    print(f"  {p.nome} {p.cognome}, {p.eta} anni, da {p.citta}")

# Calcolare media età
eta_media = sum(p.eta for p in persone) / len(persone)
print(f"Eta media: {eta_media:.1f} anni")

# Namedtuple Voto
Voto = namedtuple('Voto', ['materia', 'voto', 'data'])

voti = [
    Voto('Matematica', 8.5, datetime(2024, 10, 15)),
    Voto('Italiano', 7.0, datetime(2024, 10, 20)),
    Voto('Matematica', 9.0, datetime(2024, 11, 5)),
    Voto('Inglese', 8.0, datetime(2024, 11, 10)),
]

print(f"\nVoti:")
for v in sorted(voti, key=lambda x: x.data):
    print(f"  {v.materia}: {v.voto} ({v.data.strftime('%d/%m/%Y')})")

# Media per materia
materie = Counter(v.materia for v in voti)
for materia in materie:
    media = sum(v.voto for v in voti if v.materia == materia) / materie[materia]
    print(f"Media {materia}: {media:.2f}")

# Punti e distanza
import math
Punto = namedtuple('Punto', ['x', 'y'])

p1 = Punto(0, 0)
p2 = Punto(3, 4)

distanza = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
print(f"\nDistanza tra {p1} e {p2}: {distanza}")
```

---

## 🔍 Casi di Prova (Test)

Prova il tuo codice con questi casi:

### Test datetime
```python
# Test 1: Calcolo edad
data = datetime(2000, 1, 1)
# Verifica che il calcolo sia corretto

# Test 2: Giorni tra date
d1 = datetime(2024, 1, 1)
d2 = datetime(2024, 1, 8)
# Deve essere 7 giorni

# Test 3: Ordinamento date
date = [datetime(2024, 12, 25), datetime(2024, 1, 1), datetime(2024, 6, 15)]
sorted_dates = sorted(date)
# Verifica l'ordine
```

### Test Counter
```python
# Test 1: Parole duplicate
testo = "a b a c a d a"
c = Counter(testo.split())
assert c['a'] == 4
assert c['b'] == 1

# Test 2: Caratteri
c = Counter("aabbccddddee")
assert c['d'] == 4
assert c['a'] == 2

# Test 3: Numeri
numeri = [1,1,1,2,2,3,4,4,4,4,4]
c = Counter(numeri)
assert c[4] == 5
assert c.most_common(1) == [(4, 5)]
```

### Test namedtuple
```python
# Test 1: Creazione
Persona = namedtuple('Persona', ['nome', 'eta'])
p = Persona('Marco', 25)
assert p.nome == 'Marco'
assert p.eta == 25

# Test 2: Iterazione
persone = [Persona('A', 20), Persona('B', 30), Persona('C', 25)]
assert len(persone) == 3

# Test 3: Accesso attributi
p = Persona('Laura', 28)
assert p[0] == 'Laura'  # Per indice come tuple
assert p.nome == 'Laura'  # Per nome
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Importa i moduli necessari
```python
from datetime import datetime, timedelta
from collections import Counter, namedtuple
import math
```

### Passo 2: Scrivi una funzione per calcolare l'età
```python
def calcola_eta(data_nascita):
    """Calcola età in anni e mesi"""
    oggi = datetime.now()
    eta_giorni = (oggi - data_nascita).days
    anni = eta_giorni // 365
    mesi = (eta_giorni % 365) // 30
    return anni, mesi, eta_giorni
```

### Passo 3: Scrivi una funzione per contare parole
```python
def analizza_testo(testo):
    """Conta frequenza parole e ritorna Counter"""
    parole = testo.lower().split()
    return Counter(parole)
```

### Passo 4: Crea namedtuple e usale
```python
# Definisci il tipo
Persona = namedtuple('Persona', ['nome', 'cognome', 'eta'])

# Crea oggetti
p1 = Persona('Marco', 'Rossi', 25)
p2 = Persona('Laura', 'Verdi', 28)

# Usa gli attributi
print(f"{p1.nome} ha {p1.eta} anni")
```

### Passo 5: Testa ogni parte prima di continuare
```python
# Dopo ogni sezione, testa il codice
if __name__ == "__main__":
    # Test datetime
    print("=== Test DateTime ===")
    # ... test code ...

    # Test Counter
    print("=== Test Counter ===")
    # ... test code ...

    # Test namedtuple
    print("=== Test namedtuple ===")
    # ... test code ...
```

---

## 💡 Trucchi e Best Practices

### ✅ Come leggere la documentazione
1. Apri la documentazione Python ufficiale
2. Cerca il modulo (es: `datetime`)
3. Leggi la sezione "Example"
4. Prova gli esempi nel REPL interattivo (`python -i` o Jupyter)

### ✅ Usa `dir()` e `help()` per esplorare
```python
from datetime import datetime
import inspect

# Scopri tutti i metodi di datetime
print(dir(datetime))

# Leggi la documentazione di un metodo
help(datetime.strftime)

# Prova nel REPL
d = datetime.now()
d.  # Premi Tab per auto-completamento
```

### ✅ Formatta le date con `strftime`
```python
d = datetime(2024, 11, 19)
print(d.strftime("%d/%m/%Y"))  # 19/11/2024
print(d.strftime("%A, %d %B %Y"))  # Tuesday, 19 November 2024
```

### ✅ Counter può contare direttamente liste
```python
from collections import Counter

numeri = [1, 2, 2, 3, 3, 3]
c = Counter(numeri)  # Basta passare la lista!
```

### ✅ Ordina namedtuple facilmente
```python
persone = [...]
# Per nome
ordinati = sorted(persone, key=lambda p: p.nome)
# Per eta
ordinati = sorted(persone, key=lambda p: p.eta, reverse=True)
```

### ✅ Usa `.most_common()` per i top elementi
```python
from collections import Counter

testo = "programmazione in python"
parole = Counter(testo.split())
top_5 = parole.most_common(5)  # Ritorna lista di tuple
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare di importare il modulo
```python
# SBAGLIATO - ModuleNotFoundError
Counter([1,2,2,3])  # Counter non è definito

# GIUSTO
from collections import Counter
Counter([1,2,2,3])
```

### ❌ Errore 2: Confrontare date non dello stesso tipo
```python
# SBAGLIATO
data = "2024-11-19"
oggi = datetime.now()
differenza = oggi - data  # TypeError!

# GIUSTO
data = datetime(2024, 11, 19)
oggi = datetime.now()
differenza = oggi - data  # Funziona!
```

### ❌ Errore 3: Dimenticare che Counter ritorna un Counter, non una lista
```python
# SBAGLIATO
risultato = Counter("aabbcc")[0]  # Prova ad accedere come lista

# GIUSTO
risultato = Counter("aabbcc")  # È un Counter (tipo dizionario)
a_count = risultato['a']  # Accedi con la chiave
```

### ❌ Errore 4: Modificare una namedtuple (immutabile)
```python
# SBAGLIATO
Persona = namedtuple('Persona', ['nome', 'eta'])
p = Persona('Marco', 25)
p.eta = 26  # AttributeError! namedtuple è immutabile

# GIUSTO - crea un nuovo oggetto
p = Persona('Marco', 26)  # Crea nuovo oggetto
# Oppure converti in dizionario, modifica, ricrea
p_dict = p._asdict()
p_dict['eta'] = 26
p = Persona(**p_dict)
```

### ❌ Errore 5: Usare `split()` senza considerare punteggiatura
```python
# SBAGLIATO
testo = "Python, python. PYTHON!"
parole = Counter(testo.split())
# Risultato: Counter(['Python,', 'python.', 'PYTHON!'])  # Diverse!

# GIUSTO - normalizza il testo
import string
testo = "Python, python. PYTHON!"
testo_pulito = testo.lower()
for p in string.punctuation:
    testo_pulito = testo_pulito.replace(p, '')
parole = Counter(testo_pulito.split())
# Risultato: Counter({'python': 3})
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Analizzatore di File di Testo
- Leggi un file .txt reale (scarica dal web)
- Analizza frequenza parole, lettere, lunghezza media parole
- Mostra le 20 parole più comuni (escludi le "stop words" come "il", "di", "che")

### 🌟 Sfida 2: Generatore Calendario
- Usa `calendar` module
- Genera un calendario per un mese intero
- Evidenzia i weekend
- Segna le date importanti

### 🌟 Sfida 3: Statistiche Avanzate
- Dato un dataset di temperature (liste di numeri)
- Usa `datetime` per date
- Crea una namedtuple `Rilevamento` (data, temperatura, umidita)
- Calcola: massima, minima, media per mese
- Mostra trend

### 🌟 Sfida 4: Generatore di Riepiloghi
- Prendi testi lunghi
- Conta frequenza parole
- Estrai le N parole più importanti (ignora stop words)
- Usa per creare "tag cloud"

### 🌟 Sfida 5: Sistema di Gestione Contatti
- Crea namedtuple per `Contatto` (nome, email, telefono, data_ultimo_contatto)
- Carica una lista di contatti
- Ordina per data ultimo contatto
- Identifica contatti con cui non parli da più di X giorni

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Classe** | Blueprint per creare oggetti | `datetime` |
| **Oggetto/Istanza** | Copia concreta di una classe | `datetime.now()` |
| **Metodo** | Funzione appartenente a una classe | `d.strftime('%d/%m/%Y')` |
| **Attributo** | Dato contenuto in un oggetto | `d.year`, `d.month` |
| **Import** | Porta una classe nel tuo codice | `from datetime import datetime` |
| **Counter** | Conta occorrenze elementi | `Counter([1,1,2,3,3,3])` |
| **namedtuple** | Tuple con campi nominati | `Persona('Marco', 25)` |

---

## 🔗 Link Utili

### Documentazione Ufficiale
- [datetime - Python Docs](https://docs.python.org/3/library/datetime.html)
- [collections - Python Docs](https://docs.python.org/3/library/collections.html)
- [collections.namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)

### Tutorial Interattivi
- [Real Python - Python datetime](https://realpython.com/python-datetime/)
- [Real Python - Counter](https://realpython.com/python-counter/)

### Strumenti
- [Python REPL Online](https://repl.it/languages/python3)
- [Python Tutor](http://pythontutor.com/) - Visualizza l'esecuzione

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Leggi il tuo codice prima di guardare la soluzione
- Nota le differenze di stile e approccio
- Apprendi dalle scelte implementative
- Non copiare direttamente - usa come riferimento!

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho importato correttamente tutti i moduli
- [ ] Parte datetime funziona (calcolo età, giorni, ordinamento)
- [ ] Parte Counter funziona (parole, caratteri, numeri)
- [ ] Parte namedtuple funziona (creazione, accesso, iterazione)
- [ ] Ho testato con i casi di prova forniti
- [ ] Il codice è commentato e leggibile
- [ ] Ho provato le sfide bonus

---

**Buon lavoro! 🚀 Ricorda: il primo passo per creare classi è imparare a usarle!**

*"Non puoi fare una torta senza imparare prima a usare gli utensili."*
