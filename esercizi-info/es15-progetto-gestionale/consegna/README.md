# Es15: Progetto Finale - Sistema Gestionale Scuola

## 📊 Informazioni Generali

**Livello:** 🔴 AVANZATO (PROGETTO FINALE)
**Durata stimata:** 10-12 ore
**Prerequisiti:** Es1-14 completati, OOP avanzata

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Progettare** da zero un sistema complesso
- ✅ **Integrare** tutti i concetti OOP appresi (11-14)
- ✅ **Creare** gerarchie di classi con ereditarietà
- ✅ **Gestire** relazioni tra entità (composizione)
- ✅ **Implementare** persistenza dati (JSON/CSV)
- ✅ **Sviluppare** menu interattivo completo
- ✅ **Applicare** validazione e gestione errori
- ✅ **Documentare** e testare il codice

**Concetti usati:**
- Ereditarietà (Persona → Studente, Docente)
- Composizione (Scuola contiene Studenti, Corsi)
- Polimorfismo (metodi comuni)
- Proprietà e validazione
- Persistenza dati (JSON)
- Menu interattivo
- Gestione eccezioni
- Statistica e calcoli

---

## 📖 Descrizione Generale

Un **sistema gestionale per scuola** gestisce:
- **Persone**: Studenti e Docenti con dati anagrafici
- **Corsi**: Lezioni con docente, studenti iscritti
- **Voti**: Registrazione voti per studenti in corsi
- **Medie**: Calcolo automatico di medie per studente
- **Report**: Statistiche e export dati
- **Persistenza**: Salva/carica da JSON
- **Menu**: Interfaccia interattiva

**Questa è una applicazione VERA, non un semplice esercizio!**

---

## 📝 Diagramma UML Testuale

```
┌─────────────────────────────────────────────────────────────┐
│                        Scuola                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ nome: str                                             │   │
│  │ studenti: List[Studente]                              │   │
│  │ docenti: List[Docente]                                │   │
│  │ corsi: List[Corso]                                    │   │
│  │ iscrizioni: List[Iscrizione]                          │   │
│  │ voti: List[Voto]                                      │   │
│  └──────────────────────────────────────────────────────┘   │
│  - aggiungi_studente()                                      │
│  - aggiungi_docente()                                       │
│  - crea_corso()                                             │
│  - iscrivi_studente()                                       │
│  - registra_voto()                                          │
│  - statistiche()                                            │
│  - salva() / carica()                                       │
└─────────────────────────────────────────────────────────────┘
         │
         ├──────────┬─────────────┬──────────────┐
         ▼          ▼             ▼              ▼
      ┌─────────┐ ┌──────────┐ ┌────────┐  ┌──────────────┐
      │ Persona │ │Studente  │ │Docente │  │  Corso       │
      ├─────────┤ ├──────────┤ ├────────┤  ├──────────────┤
      │ nome    │ │ matricola│ │ badge  │  │ nome         │
      │ cognome │ │ data_iscr│ │ materia│  │ docente      │
      │ email   │ │ media    │ │ salary │  │ studenti[]   │
      │ data    │ │ corsi[]  │ │        │  │ anno         │
      │_________|_│__________│_│________|  │ max_studenti │
                                            └──────────────┘
      ┌──────────────────┐
      │   Iscrizione     │
      ├──────────────────┤
      │ studente         │
      │ corso            │
      │ data_iscrizione  │
      └──────────────────┘

      ┌──────────────────┐
      │   Voto           │
      ├──────────────────┤
      │ studente         │
      │ corso            │
      │ voto (1-10)      │
      │ data             │
      │ tipo (verifiche) │
      └──────────────────┘
```

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Base Persona

**Definisci una classe `Persona` astratta con:**

1. **Attributi:**
   - `nome` (str) - nome della persona
   - `cognome` (str) - cognome
   - `email` (str) - email univoca
   - `data_nascita` (date) - data di nascita

2. **Metodi astratti:**
   - `descrizione()` - descrizione persona
   - `tipo()` - "Studente", "Docente", ecc.

3. **Metodi concreti:**
   - `eta()` - calcola età in anni
   - `nome_completo()` - "Nome Cognome"
   - `è_maggiorenne()` - True se >= 18
   - `__str__()`, `__eq__()`, `__hash__()`

### Parte 2: Classe Studente

**Definisci una classe `Studente(Persona)` con:**

1. **Attributi aggiuntivi:**
   - `matricola` (str) - numero univoco
   - `data_iscrizione` (date) - quando si è iscritto
   - `corsi` (list) - corsi seguiti
   - `voti` (list) - voti ottenuti

2. **Metodi:**
   - `iscrivi_corso(corso)` - aggiunge corso
   - `abbandona_corso(corso)` - rimuove corso
   - `media_voti()` - calcola media
   - `media_corso(corso)` - media in un corso
   - `voti_corso(corso)` - ritorna voti di un corso
   - `numero_corsi()` - quanti corsi segue
   - `è_promosso()` - True se media >= 6
   - `descrizione()` - output leggibile

### Parte 3: Classe Docente

**Definisci una classe `Docente(Persona)` con:**

1. **Attributi aggiuntivi:**
   - `badge` (str) - identificativo docente
   - `materia` (str) - materia insegnata
   - `corsi_insegnati` (list) - corsi
   - `stipendio` (float) - stipendio

2. **Metodi:**
   - `assegna_corso(corso)` - aggiunge corso
   - `numero_studenti()` - quanti studenti insegna
   - `corsi_insegnati()` - ritorna corsi
   - `registra_voto(studente, corso, voto)` - registra voto
   - `descrizione()` - output leggibile

### Parte 4: Classe Corso

**Definisci una classe `Corso` con:**

1. **Attributi:**
   - `nome` (str) - nome corso
   - `docente` (Docente) - insegnante
   - `anno` (int) - anno scolastico
   - `studenti` (list) - studenti iscritti
   - `max_studenti` (int) - capienza massima
   - `voti` (dict) - {studente → [voti]}

2. **Metodi:**
   - `iscrivi_studente(studente)` - aggiunge studente
   - `rimuovi_studente(studente)` - rimuove
   - `numero_studenti()` - quanti iscritti
   - `è_pieno()` - True se raggiunto max
   - `registra_voto(studente, voto)` - aggiunge voto
   - `media_corso()` - media di tutti voti
   - `lista_studenti()` - ritorna studenti
   - `rapporto()` - statistiche del corso

### Parte 5: Classe Iscrizione

**Definisci una classe `Iscrizione` per tracciare iscrizioni:**

1. **Attributi:**
   - `studente` (Studente)
   - `corso` (Corso)
   - `data_iscrizione` (date)
   - `data_abbandono` (date) - None se ancora iscritto

2. **Metodi:**
   - `abbandona()` - registra abbandono
   - `è_attiva()` - True se non abbandonato
   - `giorni_iscritto()` - quanti giorni

### Parte 6: Classe Voto

**Definisci una classe `Voto` per tracciare voti:**

1. **Attributi:**
   - `studente` (Studente)
   - `corso` (Corso)
   - `voto` (float) - 1-10
   - `data` (date)
   - `tipo` (str) - "Verifica", "Esame", "Progetto"

2. **Metodi:**
   - `è_sufficiente()` - True se >= 6
   - `è_eccellente()` - True se >= 9
   - `descrizione()` - output leggibile

### Parte 7: Classe Scuola

**Definisci la classe `Scuola` che gestisce tutto:**

1. **Attributi:**
   - `nome` (str)
   - `indirizzo` (str)
   - `studenti` (list)
   - `docenti` (list)
   - `corsi` (list)
   - `iscrizioni` (list)
   - `voti` (list)

2. **Metodi di Gestione Persone:**
   - `aggiungi_studente(nome, cognome, email, data_nascita)`
   - `aggiungi_docente(nome, cognome, email, materia)`
   - `rimuovi_studente(matricola)`
   - `rimuovi_docente(badge)`

3. **Metodi di Gestione Corsi:**
   - `crea_corso(nome, docente, anno)`
   - `iscrivi_studente_corso(matricola, corso_id)`
   - `rimuovi_studente_corso(matricola, corso_id)`

4. **Metodi di Gestione Voti:**
   - `registra_voto(matricola, corso_id, voto, tipo)`
   - `media_studente(matricola)` - media totale
   - `media_studente_corso(matricola, corso_id)`
   - `studenti_promossi()` - > 6
   - `studenti_insufficienti()` - < 6

5. **Metodi di Ricerca:**
   - `trova_studente(matricola)`
   - `trova_docente(badge)`
   - `trova_corso(corso_id)`
   - `studenti_corso(corso_id)` - lista studenti
   - `corsi_studente(matricola)` - corsi di uno studente

6. **Metodi di Statistiche:**
   - `numero_studenti()`, `numero_docenti()`, `numero_corsi()`
   - `media_generale()` - media di tutti voti
   - `corso_piu_affollato()` - con più studenti
   - `docente_con_piu_studenti()`
   - `studente_con_migliore_media()`

7. **Metodi di Persistenza:**
   - `salva(filename)` - salva in JSON
   - `carica(filename)` - carica da JSON
   - `esporta_csv(filename)` - esporta studenti

8. **Metodi di Report:**
   - `rapporto_completo()` - stampa tutto
   - `rapporto_studenti()` - elenco studenti
   - `rapporto_corsi()` - elenco corsi
   - `rapporto_voti(matricola)` - voti di uno studente

### Parte 8: Menu Interattivo

**Crea un sistema di menu con:**

1. **Menu principale:**
   - 1. Gestione Studenti
   - 2. Gestione Docenti
   - 3. Gestione Corsi
   - 4. Registrazione Voti
   - 5. Statistiche e Report
   - 6. Carica/Salva Dati
   - 0. Esci

2. **Sottomenu Studenti:**
   - Aggiungi studente
   - Rimuovi studente
   - Visualizza studenti
   - Iscrivere a corso
   - Visualizza voti

3. **Sottomenu Corsi:**
   - Crea corso
   - Visualizza corsi
   - Iscrivere studente
   - Visualizza iscritti

4. **Sottomenu Voti:**
   - Registra voto
   - Visualizza voti studente
   - Visualizza media

5. **Sottomenu Statistiche:**
   - Media generale
   - Studenti promossi/insufficienti
   - Corso più affollato
   - Classifica studenti per media

---

## 💻 Esempio di Utilizzo Base

```python
# ============ ESECUZIONE BASE ============

from datetime import date
from scuola import Scuola, Studente, Docente, Corso

# Crea scuola
scuola = Scuola("Liceo Classico", "Via Roma 1")

# Aggiungi docenti
scuola.aggiungi_docente("Marco", "Rossi", "m.rossi@liceo.it", "Matematica", 2000)
scuola.aggiungi_docente("Laura", "Verdi", "l.verdi@liceo.it", "Italiano", 1900)

# Aggiungi studenti
scuola.aggiungi_studente("Giovanni", "Bianchi", "g.bianchi@student.it", date(2005, 3, 15))
scuola.aggiungi_studente("Maria", "Neri", "m.neri@student.it", date(2004, 7, 20))
scuola.aggiungi_studente("Paolo", "Rossi", "p.rossi@student.it", date(2005, 1, 10))

# Crea corsi
docente_rossi = scuola.docenti[0]
docente_verdi = scuola.docenti[1]

scuola.crea_corso("Matematica 1A", docente_rossi, 2024)
scuola.crea_corso("Italiano 1A", docente_verdi, 2024)

# Iscrivi studenti a corsi
scuola.iscrivi_studente_corso(scuola.studenti[0].matricola, 0)
scuola.iscrivi_studente_corso(scuola.studenti[0].matricola, 1)
scuola.iscrivi_studente_corso(scuola.studenti[1].matricola, 0)
scuola.iscrivi_studente_corso(scuola.studenti[2].matricola, 1)

# Registra voti
scuola.registra_voto(scuola.studenti[0].matricola, 0, 8.5, "Verifica")
scuola.registra_voto(scuola.studenti[0].matricola, 0, 7.0, "Esame")
scuola.registra_voto(scuola.studenti[0].matricola, 1, 9.0, "Tema")
scuola.registra_voto(scuola.studenti[1].matricola, 0, 5.0, "Verifica")

# Visualizza statistiche
print(scuola.rapporto_completo())

# Salva dati
scuola.salva("scuola.json")
```

---

## 🔍 Requisiti Funzionali

### RF1: Gestione Studenti
- [ ] Aggiungere nuovo studente con dati anagrafici
- [ ] Assegnare matricola univoca automaticamente
- [ ] Rimuovere studente dal sistema
- [ ] Modificare dati studente
- [ ] Visualizzare lista studenti ordinata

### RF2: Gestione Docenti
- [ ] Aggiungere docente con badge univoco
- [ ] Assegnare materia insegnata
- [ ] Registrare stipendio
- [ ] Visualizzare docenti per materia
- [ ] Calcolare numero studenti per docente

### RF3: Gestione Corsi
- [ ] Creare nuovo corso
- [ ] Assegnare docente responsabile
- [ ] Impostare capienza massima
- [ ] Iscrivere studenti (con limite capienza)
- [ ] Rimuovere iscrizioni

### RF4: Registrazione Voti
- [ ] Registrare voto per studente in corso
- [ ] Voto deve essere 1-10
- [ ] Registrare tipo voto (Verifica, Esame, Progetto)
- [ ] Calcolare media voti per studente
- [ ] Calcolare media voti per corso

### RF5: Statistiche
- [ ] Media generale della scuola
- [ ] Studenti promossi (media >= 6)
- [ ] Studenti insufficienti (media < 6)
- [ ] Classifica studenti per media
- [ ] Corso più affollato
- [ ] Docente con più studenti

### RF6: Persistenza Dati
- [ ] Salvare dati in JSON
- [ ] Caricare dati da JSON
- [ ] Esportare studenti in CSV
- [ ] Importare dati da file esterno

### RF7: Menu Interattivo
- [ ] Menu principale con opzioni
- [ ] Sottomenu per ogni sezione
- [ ] Validazione input
- [ ] Messaggi di errore chiari
- [ ] Possibilità di tornare indietro

---

## 👥 User Stories

### User Story 1: Preside
```
Come Preside,
voglio visualizzare tutte le statistiche della scuola,
in modo da avere una visione d'insieme sulla qualità educativa.

Accettazione:
- Posso vedere media generale della scuola
- Posso vedere numero totale di studenti/docenti/corsi
- Posso identificare corsi sovraffollati
- Posso esportare report in CSV
```

### User Story 2: Docente
```
Come Docente,
voglio registrare voti agli studenti dei miei corsi,
in modo da tenere traccia del loro progresso.

Accettazione:
- Posso visualizzare lista studenti del mio corso
- Posso registrare voto con tipo (Verifica, Esame, Progetto)
- Posso visualizzare media voti del corso
- Posso identificare studenti in difficoltà
```

### User Story 3: Studente
```
Come Studente,
voglio visualizzare i miei voti e media,
in modo da monitorare il mio andamento scolastico.

Accettazione:
- Posso visualizzare tutti i miei voti
- Posso vedere la media generale
- Posso vedere media per corso
- Posso verificare se sono promosso
```

### User Story 4: Segretaria
```
Come Segretaria,
voglio gestire iscrizioni e dati studenti,
in modo da mantenere l'anagrafe scolastica aggiornata.

Accettazione:
- Posso aggiungere/rimuovere studenti
- Posso iscrivere studenti ai corsi
- Posso salvare/caricare i dati da file
- Ricevo errore se matric ola è duplicata
```

---

## ✅ Criteri di Valutazione Progetto

### Completezza (30%)
- [ ] Tutte le 7 parti implementate
- [ ] Metodi base per ogni classe
- [ ] Menu funzionante
- [ ] Persistenza dati

### Correttezza OOP (25%)
- [ ] Ereditarietà implementata correttamente
- [ ] Composizione usata appropriatamente
- [ ] Polimorfismo applicato
- [ ] Validazione e gestione errori

### Qualità Codice (20%)
- [ ] Codice leggibile e commentato
- [ ] Nomi significativi per variabili/metodi
- [ ] Funzioni ben dimensionate
- [ ] DRY (Don't Repeat Yourself)

### Funzionalità Menu (15%)
- [ ] Menu intuitivo e facile da usare
- [ ] Input validation robusto
- [ ] Messaggi di errore chiari
- [ ] Opzione Esci funzionante

### Test e Documentazione (10%)
- [ ] Almeno 10 test case
- [ ] Docstring per metodi importanti
- [ ] README con istruzioni
- [ ] Esempi di utilizzo

---

## 📚 Suggerimenti Architetturali

### Struttura File Consigliata
```
progetto/
├── main.py           # Menu e esecuzione
├── scuola.py         # Classe Scuola
├── persona.py        # Persona, Studente, Docente
├── corso.py          # Corso, Iscrizione
├── voto.py           # Voto
├── utils.py          # Funzioni di utilità
├── scuola.json       # Dati salvati
└── README.md         # Documentazione
```

### Pattern Consigliati

#### 1. Factory Pattern per Studenti
```python
class Scuola:
    def aggiungi_studente(self, nome, cognome, email, data):
        # Crea automaticamente matricola unica
        matricola = f"STD{len(self.studenti)+1:04d}"
        studente = Studente(matricola, nome, cognome, email, data)
        self.studenti.append(studente)
        return studente
```

#### 2. Repository Pattern
```python
class Scuola:
    def trova_studente(self, matricola):
        """Repository per studenti"""
        for s in self.studenti:
            if s.matricola == matricola:
                return s
        return None
```

#### 3. Service Pattern
```python
class GestoreVoti:
    """Service per voti"""
    def __init__(self, scuola):
        self.scuola = scuola

    def registra_voto(self, matricola, corso_id, voto, tipo):
        # Logica di registrazione voti
        pass
```

### Gestione Errori Consigliata
```python
class StudenteNonTrovatoError(Exception):
    pass

class CorsoGiaPienoError(Exception):
    pass

class VotoNonValidoError(Exception):
    pass

# Uso
def registra_voto(self, matricola, corso_id, voto, tipo):
    if not 1 <= voto <= 10:
        raise VotoNonValidoError("Voto deve essere 1-10")
    # ...
```

### Validazione Consigliata
```python
def aggiungi_studente(self, nome, cognome, email, data_nascita):
    if not nome or not cognome:
        raise ValueError("Nome e cognome obbligatori")
    if "@" not in email:
        raise ValueError("Email non valida")
    if date.today() < data_nascita:
        raise ValueError("Data nascita futura")
    if not self._email_unica(email):
        raise ValueError("Email già in uso")
    # ...
```

### Persistenza JSON
```python
import json
from datetime import date, datetime

class Scuola:
    def salva(self, filename):
        dati = {
            "nome": self.nome,
            "indirizzo": self.indirizzo,
            "studenti": [...],  # JSON-serializable
            "docenti": [...],
            "corsi": [...]
        }
        with open(filename, 'w') as f:
            json.dump(dati, f, indent=2, default=str)
```

---

## 📊 Test Case Suggeriti

```python
# Test 1: Creazione studente
studente = Studente("STD001", "Giovanni", "Rossi", "g.rossi@mail.it", date(2005, 1, 1))
assert studente.nome == "Giovanni"
assert studente.eta() == 19

# Test 2: Media studente
# Aggiungi voti e verifica media calcolata

# Test 3: Iscrizione a corso
# Iscrivi studente e verifica se è in lista studenti del corso

# Test 4: Validazione voto
# Tenta registrazione voto invalido (> 10), deve sollevare errore

# Test 5: Capienza corso
# Aggiungi max_studenti e tenta iscrizione extra

# Test 6: Salvataggio/Caricamento
# Salva scuola, ricarica, verifica uguaglianza

# Test 7: Statistiche
# Registra voti, calcola media generale

# Test 8: Ricerca
# Trova studente per matricola

# Test 9: Rimozione
# Rimuovi studente, verifica che non sia più nella lista

# Test 10: Unicità
# Tenta aggiungere email duplicata
```

---

## 🚀 Funzionalità Bonus (Extra Points)

### 🌟 Bonus 1: Autenticazione
```python
class Utente:
    def __init__(self, username, password, ruolo):
        self.username = username
        self.password = self._hash_password(password)
        self.ruolo = ruolo  # admin, docente, studente

# Menu iniziale con login
```

### 🌟 Bonus 2: Sistema di Classi
```python
class Classe:
    def __init__(self, nome, anno):
        self.nome = nome  # "1A", "2B"
        self.anno = anno
        self.studenti = []
```

### 🌟 Bonus 3: Assenze e Giustificazioni
```python
class Assenza:
    def __init__(self, studente, data, giustificata):
        self.studente = studente
        self.data = data
        self.giustificata = giustificata
```

### 🌟 Bonus 4: Sistema di Comunicazioni
```python
class Messaggio:
    def __init__(self, mittente, destinatario, testo):
        self.mittente = mittente
        self.destinatario = destinatario
        self.testo = testo
        self.data = datetime.now()
```

### 🌟 Bonus 5: Esportazione Report PDF
```python
def esporta_pdf(self, filename):
    """Esporta report completo in PDF"""
    from reportlab.lib.pagesizes import letter
    # Implementa esportazione
```

---

## 📖 Riassunto Checklist Implementazione

### Fase 1: Classi Base (Ore 2-3)
- [ ] Classe Persona (astratta)
- [ ] Classe Studente
- [ ] Classe Docente
- [ ] Test base per persone

### Fase 2: Gestione Corsi e Voti (Ore 2-3)
- [ ] Classe Corso
- [ ] Classe Iscrizione
- [ ] Classe Voto
- [ ] Registrazione voti

### Fase 3: Classe Scuola (Ore 2)
- [ ] Creazione classe Scuola
- [ ] Metodi di gestione
- [ ] Metodi di ricerca
- [ ] Metodi di statistiche

### Fase 4: Persistenza Dati (Ore 1)
- [ ] Serializzazione JSON
- [ ] Salvataggio e caricamento
- [ ] Export CSV

### Fase 5: Menu Interattivo (Ore 2-3)
- [ ] Menu principale
- [ ] Sottomenu
- [ ] Validazione input
- [ ] Gestione errori

### Fase 6: Test e Documentazione (Ore 1-2)
- [ ] Almeno 10 test case
- [ ] Docstring
- [ ] README.md
- [ ] Revisione codice

---

## 💾 Template di Salvataggio JSON

```json
{
  "nome": "Liceo Classico",
  "indirizzo": "Via Roma 1",
  "studenti": [
    {
      "matricola": "STD0001",
      "nome": "Giovanni",
      "cognome": "Rossi",
      "email": "g.rossi@student.it",
      "data_nascita": "2005-03-15",
      "data_iscrizione": "2023-09-01"
    }
  ],
  "docenti": [
    {
      "badge": "DOC001",
      "nome": "Marco",
      "cognome": "Verdi",
      "email": "m.verdi@liceo.it",
      "materia": "Matematica",
      "stipendio": 2000
    }
  ],
  "corsi": [
    {
      "id": "COR001",
      "nome": "Matematica 1A",
      "docente_badge": "DOC001",
      "anno": 2024,
      "max_studenti": 25
    }
  ],
  "voti": [
    {
      "studente_matricola": "STD0001",
      "corso_id": "COR001",
      "voto": 8.5,
      "data": "2024-01-15",
      "tipo": "Verifica"
    }
  ]
}
```

---

## 🔗 Link Utili

### Documentazione
- [Python datetime](https://docs.python.org/3/library/datetime.html)
- [Python json](https://docs.python.org/3/library/json.html)
- [Python CSV](https://docs.python.org/3/library/csv.html)

### OOP Patterns
- [Design Patterns - Refactoring.Guru](https://refactoring.guru/design-patterns)
- [Factory Pattern](https://refactoring.guru/design-patterns/factory-method)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

---

## ✅ Checklist Finale Completa

Prima di presentare il progetto:

**Implementazione:**
- [ ] Classe Persona (astratta) con metodi base
- [ ] Classe Studente con tutti i metodi
- [ ] Classe Docente con tutti i metodi
- [ ] Classe Corso con iscrizioni
- [ ] Classe Iscrizione
- [ ] Classe Voto
- [ ] Classe Scuola con tutti i metodi

**Funzionalità:**
- [ ] Aggiungere/rimuovere studenti
- [ ] Aggiungere/rimuovere docenti
- [ ] Creare corsi
- [ ] Iscrivere studenti a corsi
- [ ] Registrare voti
- [ ] Calcolare medie
- [ ] Statistiche (promossi, insufficienti, ecc.)

**Persistenza:**
- [ ] Salva in JSON
- [ ] Carica da JSON
- [ ] Esporta CSV

**Menu:**
- [ ] Menu principale funzionante
- [ ] Sottomenu per ogni sezione
- [ ] Input validation
- [ ] Gestione errori

**Qualità:**
- [ ] Codice commentato
- [ ] Nomi significativi
- [ ] DRY principle applicato
- [ ] Error handling robusto

**Test:**
- [ ] Almeno 10 test case
- [ ] Test di integrazione

**Documentazione:**
- [ ] README.md completo
- [ ] Istruzioni di utilizzo
- [ ] Docstring per metodi
- [ ] Diagrammi (se necessario)

---

**Congratulazioni! Hai completato il progetto finale! 🎉🎓**

*"Questo progetto integra tutto quello che hai imparato in 15 esercizi. È un vero sistema gestionale!"*

**Prossimi passi:**
- Aggiungi le funzionalità bonus
- Implementa un'interfaccia grafica (tkinter/PyQt)
- Deployer su web con Flask/Django
- Condividi su GitHub!
