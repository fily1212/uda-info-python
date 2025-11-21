# Es5: Datetime Avanzato - Gestire Date e Ore come Oggetti

## 📊 Informazioni Generali

**Livello:** 🟡 BASE
**Durata stimata:** 3-4 ore
**Prerequisiti:** Es1-Es4 completati, concetti OOP base

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Utilizzare** le classi datetime: `datetime`, `date`, `time`, `timedelta`
- ✅ **Creare** oggetti data e ora con i costruttori appropriati
- ✅ **Parsing** stringhe in date: `strptime()` - conversione stringa → datetime
- ✅ **Formattare** date in stringhe: `strftime()` - conversione datetime → stringa
- ✅ **Operazioni** con date: somma, sottrazione, confronti
- ✅ **Calcoli pratici**: età, giorni tra date, scadenze, giorni lavorativi
- ✅ **Timezone** con pytz (opzionale ma utile)
- ✅ **Risolvere problemi reali**: gestione appuntamenti, promemoria, scadenze

**Concetti fondamentali:**
- Classi datetime: `datetime`, `date`, `time`, `timedelta`
- Parsing con `strptime()`
- Formattazione con `strftime()`
- Operazioni aritmetiche su date
- Timezone e UTC

---

## 📖 Descrizione

Datetime è una libreria **OOP per le date** che trasforma stringhe e numeri in oggetti intelligenti che capiscono il significato di "data".

**Perché usare datetime OOP?**

1. **Oggetti intelligenti** - Non trattare date come stringhe o numeri
2. **Operazioni native** - Somma/sottrazione di date è naturale
3. **Formattazione flessibile** - Converti date in qualsiasi formato
4. **Calcoli automatici** - Giorni tra date, settimane, anni
5. **Timezone** - Gestisci orari in diverse zone orarie

**Confronto: Stringhe vs Datetime**

```python
# ❌ Date come stringhe - FRAGILE
data1 = "2024-01-15"
data2 = "2024-02-20"
differenza = data2 - data1  # TypeError! Non puoi sottrarre stringhe!

# ✅ Datetime - ROBUSTO
from datetime import datetime
data1 = datetime(2024, 1, 15)
data2 = datetime(2024, 2, 20)
differenza = data2 - data1  # timedelta(36 days) - perfetto!
print(differenza.days)  # 36
```

---

## 📝 Consegna Dettagliata

### Parte 1: Creare Oggetti Data e Ora

**Crea un programma che:**

1. **Crea oggetti `datetime`**
   - Costruttore: `datetime(anno, mese, giorno, ora, minuto, secondo)`
   - Data odierna: `datetime.now()`
   - UTC: `datetime.utcnow()`
   - Dall'timestamp: `datetime.fromtimestamp()`

2. **Crea oggetti `date` (solo data)**
   - Costruttore: `date(anno, mese, giorno)`
   - Data odierna: `date.today()`
   - Estrai data da datetime: `datetime_obj.date()`

3. **Crea oggetti `time` (solo ora)**
   - Costruttore: `time(ora, minuto, secondo)`
   - Estrai ora da datetime: `datetime_obj.time()`

4. **Crea oggetti `timedelta` (intervalli)**
   - Differenza tra date: `datetime2 - datetime1`
   - Intervallo custom: `timedelta(days=5, hours=2, minutes=30)`
   - Proprietà: `.days`, `.seconds`, `.total_seconds()`

### Parte 2: Parsing e Formattazione

**Crea un programma che:**

1. **Parsing (stringa → datetime)**
   - Converti stringa in datetime: `datetime.strptime()`
   - Formati comuni: '%Y-%m-%d', '%d/%m/%Y', '%H:%M:%S'
   - Estrai componenti: `.year`, `.month`, `.day`, `.hour`, `.minute`

2. **Formattazione (datetime → stringa)**
   - Converti datetime in stringa: `.strftime()`
   - Formati comuni: '%d/%m/%Y', '%A, %d %B %Y' (con nome giorno/mese)
   - Nomi locali: giorni/mesi in italiano (con locale)

3. **Parsing di formati diversi**
   - ISO format: '2024-01-15T10:30:00'
   - Formato italiano: '15/01/2024'
   - Formato con giorno: 'Lunedi, 15 Gennaio 2024'

### Parte 3: Operazioni Aritmetiche con Date

**Crea un programma che:**

1. **Somma e sottrazione**
   - Aggiungi giorni: `data + timedelta(days=5)`
   - Aggiungi ore/minuti: `data + timedelta(hours=2)`
   - Sottrai date: `data2 - data1` → ottiene timedelta

2. **Confronti**
   - Quale data è precedente: `data1 < data2`
   - Quale data è successiva: `data1 > data2`
   - Sono uguali: `data1 == data2`

3. **Calcoli pratici**
   - Giorni tra due date
   - Settimane tra due date
   - Se una data è nel passato o nel futuro
   - Quanti giorni rimangono fino a una data

### Parte 4: Calcoli Pratici (Applicazioni Reali)

**Crea un programma che:**

1. **Calcolo dell'età**
   - Data di nascita → età in anni, mesi, giorni
   - Quando sarà il prossimo compleanno?
   - Quanto manca al compleanno?

2. **Gestione scadenze**
   - Data di creazione + durata → data di scadenza
   - Quanto tempo rimane prima della scadenza?
   - La scadenza è passata?

3. **Giorni lavorativi**
   - Conta giorni lavorativi (escludi weekday)
   - Conta weekend
   - Conto alla rovescia a data importante (ignorando weekend)

4. **Calendario custom**
   - Genera calendari personalizzati
   - Evidenzia festività
   - Conto dei giorni per mese

### Parte 5: Timezone (Opzionale ma Utile)

**Crea un programma che:**

1. **Installa pytz** (se non presente)
2. **Crea datetime con timezone**
3. **Converti tra timezone**
4. **Oro UTC vs locale**

### Parte 6: Esercizio Pratico Completo

**Sistema di gestione appuntamenti:**

1. **Crea lista appuntamenti**
   - Titolo, data, ora, durata
   - Salva in dizionario con datetime

2. **Funzioni di ricerca**
   - Appuntamenti di un giorno specifico
   - Appuntamenti della settimana
   - Appuntamenti per intervallo di date

3. **Promemoria**
   - Quali appuntamenti sono tra 7 giorni?
   - Quali appuntamenti sono scaduti?
   - Prossimo appuntamento?

4. **Analisi**
   - Giorni liberi nel mese
   - Giorni occupati
   - Statistiche su impegni

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ PARTE 1: CREARE OGGETTI ============

from datetime import datetime, date, time, timedelta
import calendar

print("=== CREAZIONE OGGETTI ===")

# datetime - data e ora
d1 = datetime(2024, 1, 15, 10, 30, 0)
print(f"DateTime specifico: {d1}")

# Data odierna
oggi = datetime.now()
print(f"Oggi: {oggi}")

# date - solo data
d2 = date(2024, 2, 20)
print(f"Solo data: {d2}")

# time - solo ora
t = time(14, 30, 45)
print(f"Solo ora: {t}")

# Combina date e time
dt = datetime.combine(d2, t)
print(f"Combinato: {dt}")

# ============ PARTE 2: PARSING E FORMATTAZIONE ============

print("\n=== PARSING E FORMATTAZIONE ===")

# Parsing (stringa → datetime)
stringa = "2024-03-15"
data_parsata = datetime.strptime(stringa, "%Y-%m-%d")
print(f"Parsato: {stringa} → {data_parsata}")

stringa_italiana = "15/03/2024"
data_it = datetime.strptime(stringa_italiana, "%d/%m/%Y")
print(f"Parsato italiano: {stringa_italiana} → {data_it}")

# Formattazione (datetime → stringa)
data = datetime(2024, 3, 15, 14, 30)
formattato1 = data.strftime("%d/%m/%Y")
print(f"Formato italiano: {formattato1}")

formattato2 = data.strftime("%A, %d %B %Y")  # Con nomi giorni
print(f"Formato esteso: {formattato2}")

formattato3 = data.strftime("%H:%M")
print(f"Solo ora: {formattato3}")

# Con locale italiano (richiede locale installato)
try:
    import locale
    locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')
    formattato4 = data.strftime("%A, %d %B %Y")
    print(f"Formato italiano (locale): {formattato4}")
except:
    print("Locale italiano non disponibile")

# ============ PARTE 3: OPERAZIONI ARITMETICHE ============

print("\n=== OPERAZIONI ARITMETICHE ===")

# Differenza tra date
data1 = datetime(2024, 1, 15)
data2 = datetime(2024, 2, 20)
differenza = data2 - data1
print(f"Differenza tra {data2.date()} e {data1.date()}:")
print(f"  Giorni: {differenza.days}")
print(f"  Secondi totali: {differenza.total_seconds()}")
print(f"  Settimane: {differenza.days // 7}")

# Somma di giorni
oggi = datetime.now()
domani = oggi + timedelta(days=1)
fra_una_settimana = oggi + timedelta(days=7)
fra_un_mese = oggi + timedelta(days=30)

print(f"\nDa oggi ({oggi.date()}):")
print(f"  Domani: {domani.date()}")
print(f"  Fra una settimana: {fra_una_settimana.date()}")
print(f"  Fra un mese: {fra_un_mese.date()}")

# Somma di ore
ora_now = datetime.now()
tra_2_ore = ora_now + timedelta(hours=2)
print(f"\nOra attuale: {ora_now.strftime('%H:%M')}")
print(f"Fra 2 ore: {tra_2_ore.strftime('%H:%M')}")

# Confronti
print(f"\nConf nti:")
print(f"data1 < data2: {data1 < data2}")
print(f"data1 == data2: {data1 == data2}")
print(f"data1 > data2: {data1 > data2}")

# ============ PARTE 4: CALCOLO ETA' ============

print("\n=== CALCOLO ETA' ===")

def calcola_eta(data_nascita):
    """Calcola età in anni, mesi, giorni"""
    oggi = date.today()

    # Calcolo base
    anni = oggi.year - data_nascita.year
    mesi = oggi.month - data_nascita.month
    giorni = oggi.day - data_nascita.day

    # Aggiustamenti
    if giorni < 0:
        mesi -= 1
        giorni += 30  # Approssimazione

    if mesi < 0:
        anni -= 1
        mesi += 12

    return anni, mesi, giorni

data_nascita = date(1990, 6, 15)
anni, mesi, giorni = calcola_eta(data_nascita)
print(f"Nato il {data_nascita}: {anni} anni, {mesi} mesi, {giorni} giorni")

# Quando sarà il prossimo compleanno?
oggi = date.today()
prossimo_compleanno = date(oggi.year, data_nascita.month, data_nascita.day)
if prossimo_compleanno < oggi:
    prossimo_compleanno = date(oggi.year + 1, data_nascita.month, data_nascita.day)

giorni_al_compleanno = (prossimo_compleanno - oggi).days
print(f"Prossimo compleanno: {prossimo_compleanno} ({giorni_al_compleanno} giorni)")

# ============ PARTE 5: GESTIONE SCADENZE ============

print("\n=== GESTIONE SCADENZE ===")

# Contratto creato oggi, durata 30 giorni
data_creazione = datetime.now()
durata = timedelta(days=30)
data_scadenza = data_creazione + durata

print(f"Contratto creato: {data_creazione.date()}")
print(f"Scadenza: {data_scadenza.date()}")

# Quanto tempo rimane?
tempo_rimasto = data_scadenza - datetime.now()
if tempo_rimasto.days >= 0:
    print(f"Giorni rimasti: {tempo_rimasto.days}")
    print(f"Scadenza tra: {tempo_rimasto.days} giorni")
else:
    print(f"SCADUTO! Da {abs(tempo_rimasto.days)} giorni!")

# ============ PARTE 6: GIORNI LAVORATIVI ============

print("\n=== GIORNI LAVORATIVI ============")

def conta_giorni_lavorativi(data_inizio, data_fine):
    """Conta giorni lavorativi (lun-ven) tra due date"""
    giorni_lav = 0
    data_corrente = data_inizio

    while data_corrente <= data_fine:
        # weekday(): 0=lunedi, 6=domenica
        if data_corrente.weekday() < 5:  # 0-4 sono lun-ven
            giorni_lav += 1
        data_corrente += timedelta(days=1)

    return giorni_lav

data_inizio = date(2024, 1, 1)
data_fine = date(2024, 1, 31)
gg_lav = conta_giorni_lavorativi(data_inizio, data_fine)
print(f"Giorni lavorativi gennaio 2024: {gg_lav}")

# Conta weekend
def conta_weekend(data_inizio, data_fine):
    """Conta giorni weekend (sab-dom)"""
    giorni_we = 0
    data_corrente = data_inizio

    while data_corrente <= data_fine:
        if data_corrente.weekday() >= 5:  # 5=sabato, 6=domenica
            giorni_we += 1
        data_corrente += timedelta(days=1)

    return giorni_we

gg_we = conta_weekend(data_inizio, data_fine)
print(f"Giorni weekend gennaio 2024: {gg_we}")

# ============ PARTE 7: CALENDARIO ============

print("\n=== CALENDARIO ===")

anno = 2024
mese = 3  # Marzo

print(f"\n{calendar.month_name[mese]} {anno}:")
print(calendar.month(anno, mese))

# Quanti giorni ha il mese?
num_giorni = calendar.monthrange(anno, mese)[1]
print(f"Giorni nel mese: {num_giorni}")

# ============ PARTE 8: SISTEMA APPUNTAMENTI ============

print(f"\n=== SISTEMA APPUNTAMENTI ===")

class Appuntamento:
    def __init__(self, titolo, data, ora, durata_minuti):
        self.titolo = titolo
        self.data_ora = datetime.combine(
            datetime.strptime(data, "%Y-%m-%d").date(),
            datetime.strptime(ora, "%H:%M").time()
        )
        self.durata = timedelta(minutes=durata_minuti)
        self.data_fine = self.data_ora + self.durata

    def __repr__(self):
        return f"{self.titolo} - {self.data_ora.strftime('%d/%m/%Y %H:%M')}"

    def e_scaduto(self):
        return self.data_ora < datetime.now()

    def giorni_rimanenti(self):
        return (self.data_ora.date() - date.today()).days

# Crea lista appuntamenti
appuntamenti = [
    Appuntamento("Riunione", "2024-01-20", "10:00", 60),
    Appuntamento("Pranzo", "2024-01-20", "12:30", 90),
    Appuntamento("Progetto", "2024-01-21", "15:00", 120),
    Appuntamento("Dentista", "2025-01-25", "09:00", 30),
]

print("Appuntamenti:")
for app in appuntamenti:
    print(f"  {app}")

# ============ PARTE 9: PROMEMORIA ============

print("\n=== PROMEMORIA ===")

def appuntamenti_della_settimana(appuntamenti):
    """Restituisce appuntamenti dei prossimi 7 giorni"""
    oggi = date.today()
    fra_7_giorni = oggi + timedelta(days=7)
    return [a for a in appuntamenti
            if oggi <= a.data_ora.date() <= fra_7_giorni]

def prossimo_appuntamento(appuntamenti):
    """Restituisce il prossimo appuntamento non scaduto"""
    non_scaduti = [a for a in appuntamenti if not a.e_scaduto()]
    return min(non_scaduti, key=lambda a: a.data_ora) if non_scaduti else None

print(f"Prossimi appuntamenti (7 giorni):")
per_settimana = appuntamenti_della_settimana(appuntamenti)
for app in per_settimana:
    print(f"  {app}")

prossimo = prossimo_appuntamento(appuntamenti)
if prossimo:
    print(f"\nProssimo appuntamento: {prossimo}")
    print(f"  Fra {prossimo.giorni_rimanenti()} giorni")
```

---

## 🔍 Casi di Prova (Test)

```python
# Test 1: Creazione datetime
def test_creazione():
    from datetime import datetime, date, time
    d = datetime(2024, 1, 15)
    assert d.year == 2024
    assert d.month == 1
    assert d.day == 15
    print("✓ Test 1 passato: Creazione datetime")

# Test 2: Parsing
def test_parsing():
    from datetime import datetime
    data_str = "2024-01-15"
    data = datetime.strptime(data_str, "%Y-%m-%d")
    assert data.year == 2024
    assert data.month == 1
    assert data.day == 15
    print("✓ Test 2 passato: Parsing")

# Test 3: Formattazione
def test_formattazione():
    from datetime import datetime
    d = datetime(2024, 1, 15, 14, 30)
    formattato = d.strftime("%d/%m/%Y")
    assert formattato == "15/01/2024"
    print("✓ Test 3 passato: Formattazione")

# Test 4: Differenza tra date
def test_differenza():
    from datetime import datetime
    d1 = datetime(2024, 1, 15)
    d2 = datetime(2024, 1, 20)
    diff = d2 - d1
    assert diff.days == 5
    print("✓ Test 4 passato: Differenza")

# Test 5: Somma di giorni
def test_somma():
    from datetime import datetime, timedelta
    d = datetime(2024, 1, 15)
    d_new = d + timedelta(days=5)
    assert d_new.day == 20
    print("✓ Test 5 passato: Somma giorni")

# Test 6: Confronti
def test_confronti():
    from datetime import datetime
    d1 = datetime(2024, 1, 15)
    d2 = datetime(2024, 1, 20)
    assert d1 < d2
    assert d2 > d1
    assert d1 != d2
    print("✓ Test 6 passato: Confronti")

# Test 7: Estrazione componenti
def test_componenti():
    from datetime import datetime
    d = datetime(2024, 1, 15, 14, 30, 45)
    assert d.year == 2024
    assert d.hour == 14
    assert d.minute == 30
    assert d.second == 45
    print("✓ Test 7 passato: Componenti")

# Test 8: Date vs Datetime
def test_date_datetime():
    from datetime import date, datetime
    d = date(2024, 1, 15)
    dt = datetime(2024, 1, 15, 14, 30)
    assert d.year == dt.year
    assert d.month == dt.month
    print("✓ Test 8 passato: Date vs Datetime")

# Test 9: Timedelta
def test_timedelta():
    from datetime import timedelta
    td = timedelta(days=5, hours=2)
    assert td.days == 5
    assert td.total_seconds() > 0
    print("✓ Test 9 passato: Timedelta")

# Test 10: Weekday
def test_weekday():
    from datetime import date
    d = date(2024, 1, 15)  # Lunedi
    assert d.weekday() == 0  # 0 = lunedi
    print("✓ Test 10 passato: Weekday")

if __name__ == "__main__":
    test_creazione()
    test_parsing()
    test_formattazione()
    test_differenza()
    test_somma()
    test_confronti()
    test_componenti()
    test_date_datetime()
    test_timedelta()
    test_weekday()
    print("\n✅ Tutti i test passati!")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Impara le classi base
```python
from datetime import datetime, date, time, timedelta

d = datetime(2024, 1, 15)
d2 = date.today()
t = time(14, 30)
```

### Passo 2: Esercitati con parsing
```python
s = "2024-01-15"
d = datetime.strptime(s, "%Y-%m-%d")
```

### Passo 3: Esercitati con formattazione
```python
d = datetime.now()
print(d.strftime("%d/%m/%Y %H:%M"))
```

### Passo 4: Fai operazioni aritmetiche
```python
d1 = datetime(2024, 1, 15)
d2 = datetime(2024, 1, 20)
print((d2 - d1).days)
```

### Passo 5: Crea funzioni custom
```python
def giorni_al_compleanno(data_nascita):
    ...
```

### Passo 6: Risolvi problemi pratici
```python
# Sistema appuntamenti, scadenze, etc
```

### Passo 7: Aggiungi timezone (opzionale)
```python
import pytz
# Lavora con timezone
```

---

## 💡 Trucchi e Best Practices

### ✅ Trucco 1: Scopri i formati con strftime()
```python
from datetime import datetime
d = datetime.now()
print(d.strftime("%Y"))  # Anno
print(d.strftime("%m"))  # Mese
print(d.strftime("%A"))  # Nome giorno
print(d.strftime("%B"))  # Nome mese
```

### ✅ Trucco 2: Usa weekday() per il giorno della settimana
```python
d = date(2024, 1, 15)
giorni = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']
print(giorni[d.weekday()])  # Lunedi
```

### ✅ Trucco 3: Converti tra date e datetime
```python
d = date.today()
dt = datetime.combine(d, time(14, 30))
d2 = dt.date()
```

### ✅ Trucco 4: Calcolo dell'età corretto
```python
def calcola_eta_precisa(data_nascita):
    oggi = date.today()
    eta = oggi.year - data_nascita.year
    if (oggi.month, oggi.day) < (data_nascita.month, data_nascita.day):
        eta -= 1
    return eta
```

### ✅ Trucco 5: Usa calendar per informazioni mese
```python
import calendar
num_giorni = calendar.monthrange(2024, 1)[1]  # Giorni in gennaio
nome_mese = calendar.month_name[1]  # "January"
```

### ✅ Trucco 6: Timezone con pytz
```python
import pytz
roma = pytz.timezone('Europe/Rome')
dt = datetime.now(roma)
```

### ✅ Trucco 7: Somme di mesi
```python
from dateutil.relativedelta import relativedelta
d = date(2024, 1, 15)
d_plus_3_mesi = d + relativedelta(months=3)
```

### ✅ Trucco 8: Confronti tra date
```python
d1 = date(2024, 1, 15)
d2 = date(2024, 1, 20)
if d1 < d2:
    print("d1 è precedente")
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Confondere ordine parametri
```python
# SBAGLIATO
d = datetime(15, 1, 2024)  # Che ordine è?

# GIUSTO
d = datetime(2024, 1, 15)  # Anno, mese, giorno (ISO standard)
```

### ❌ Errore 2: Usare formato sbagliato per strptime
```python
# SBAGLIATO
d = datetime.strptime("2024-01-15", "%d/%m/%Y")  # Mismatch!

# GIUSTO
d = datetime.strptime("2024-01-15", "%Y-%m-%d")
```

### ❌ Errore 3: Non gestire timezone
```python
# SBAGLIATO - confusion con ora locale vs UTC
d = datetime.now()
d_utc = datetime.utcnow()
# Sono diverse ma non è ovvio!

# GIUSTO - sii esplicito
from datetime import timezone
d_locale = datetime.now()
d_utc = datetime.now(timezone.utc)
```

### ❌ Errore 4: Usare stringhe per date
```python
# SBAGLIATO
scadenza = "2024-01-15"
if scadenza < "2024-01-20":  # Confronto stringa, non data!
    print("Scaduta")

# GIUSTO
scadenza = datetime(2024, 1, 15)
if scadenza < datetime(2024, 1, 20):  # Confronto data
    print("Scaduta")
```

### ❌ Errore 5: Dimenticare che months non esiste in timedelta
```python
# SBAGLIATO
from datetime import timedelta
d = date(2024, 1, 15)
d_new = d + timedelta(months=3)  # AttributeError!

# GIUSTO
from dateutil.relativedelta import relativedelta
d_new = d + relativedelta(months=3)
```

### ❌ Errore 6: Non considerare anni bisestili
```python
# SBAGLIATO - assumi 365 giorni sempre
giorni_anno = 365

# GIUSTO - usa le classi di datetime
import calendar
is_bisestile = calendar.isleap(2024)
```

### ❌ Errore 7: Confondere date() e today()
```python
# SBAGLIATO - quale usi?
d = date()  # ValueError! Date() richiede parametri

# GIUSTO
d = date.today()  # Oggi
d = date(2024, 1, 15)  # Data specifica
```

### ❌ Errore 8: NaiveDateTime vs AwareDateTime
```python
# SBAGLIATO - mix senza timezone
d1 = datetime.now()  # Naive (no timezone)
d2 = datetime.now(timezone.utc)  # Aware
d1 + d2  # TypeError!

# GIUSTO - sii consistente
from datetime import timezone
d1 = datetime.now(timezone.utc)
d2 = datetime.now(timezone.utc)
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Agenda Avanzata
- Sistema di gestione appuntamenti completo
- Ricorrenze (ogni giorno, settimana, mese)
- Conflitti di appuntamenti
- Export in iCal/Google Calendar

### 🌟 Sfida 2: Calcoli Astrali
- Calcola fasi lunari
- Stagioni astronomiche
- Giorni bisestili e loro storia

### 🌟 Sfida 3: Time Tracking App
- Registra inizio/fine attività
- Calcola tempo totale per categoria
- Rapporto settimanale/mensile

### 🌟 Sfida 4: Conversione Timezone Globale
- Converti ora tra 10 timezone
- Crea mappa del mondo con ore
- Gestisci daylight saving time

### 🌟 Sfida 5: Calendario Personalizzato
- Genera calendario HTML/PDF
- Evidenzia festività nazionali
- Segna appuntamenti custom
- Calcola giorni dedicati a progetto

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **datetime** | Oggetto data e ora | `datetime(2024, 1, 15, 14, 30)` |
| **date** | Solo data | `date(2024, 1, 15)` |
| **time** | Solo ora | `time(14, 30, 0)` |
| **timedelta** | Intervallo di tempo | `timedelta(days=5, hours=2)` |
| **strptime()** | Stringa → datetime | `datetime.strptime("2024-01-15", "%Y-%m-%d")` |
| **strftime()** | datetime → stringa | `d.strftime("%d/%m/%Y")` |
| **now()** | Data/ora attuale | `datetime.now()` |
| **today()** | Data odierna | `date.today()` |
| **weekday()** | Giorno della settimana (0-6) | `d.weekday()` → 0 = lunedi |
| **Operazioni** | Somma/sottrazione date | `d1 + timedelta(days=5)` |
| **Confronti** | Confronta date | `d1 < d2` |
| **timezone** | Fuso orario | `pytz.timezone('Europe/Rome')` |

---

## 🔗 Link Utili

### Documentazione Ufficiale
- [datetime - Python Docs](https://docs.python.org/3/library/datetime.html)
- [calendar - Python Docs](https://docs.python.org/3/library/calendar.html)
- [pytz - Timezone Database](https://pypi.org/project/pytz/)
- [dateutil - Extended Datetime](https://dateutil.readthedocs.io/)

### Tutorial Interattivi
- [Real Python - datetime](https://realpython.com/python-datetime/)
- [Real Python - Timezone](https://realpython.com/python-pytz/)
- [DataCamp - datetime Tutorial](https://www.datacamp.com/courses/working-with-dates-and-times-in-python)

### Cheat Sheet
- [datetime Cheat Sheet](https://www.datacamp.com/cheat-sheets/python-datetime)
- [strftime/strptime Codes](https://strftime.org/)

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

- [ ] Conosco le 4 classi: datetime, date, time, timedelta
- [ ] So creare oggetti datetime in vari modi
- [ ] So parsare stringhe con strptime()
- [ ] So formattare date con strftime()
- [ ] Riesco a fare operazioni aritmetiche tra date
- [ ] So calcolare l'età correttamente
- [ ] So contare giorni lavorativi vs weekend
- [ ] Capisco weekday() e il significato dei numeri 0-6
- [ ] Ho testato il codice con i casi di prova forniti
- [ ] Ho provato le sfide bonus
- [ ] Capisco che datetime è uno strumento fondamentale per applicazioni reali

---

**Buon lavoro! ⏰ Il tempo è un oggetto, non una stringa!**

*"Il tempo è l'unica cosa che non puoi comprare - imparalo a gestire bene con datetime."*
