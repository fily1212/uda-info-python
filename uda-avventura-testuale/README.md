# UDA Avventure Testuali - Narrativa e Parser

## Creare Avventure Testuali Interattive con Parser di Linguaggio Naturale

Unità Didattica di Apprendimento che combina **scrittura creativa**, **progettazione narrativa** e **programmazione** per creare avventure testuali complete con parser di linguaggio naturale in stile Inform6/Zork.

---

## Descrizione

Gli studenti progetteranno e implementeranno un'**avventura testuale completa** con:
- Sistema di parsing di comandi in linguaggio naturale
- Mappa di stanze interconnesse
- Oggetti interattivi con azioni multiple
- NPC con dialoghi e comportamenti
- Sistema di eventi e puzzle
- Trama con colpi di scena ed enigmi

**Approccio:** Viene fornito un motore completo (`text_adventure_engine`). Gli studenti si concentrano su:
- **Parte Italiano:** Progettazione narrativa, worldbuilding, dialoghi, enigmi
- **Parte Informatica:** Implementazione della storia usando il motore

---

## Obiettivi

### Competenze Italiano (50%)
- **Progettazione narrativa:** struttura della storia, arco narrativo, colpi di scena
- **Worldbuilding:** creazione ambientazioni coerenti e atmosferiche
- **Scrittura descrittiva:** descrizioni evocative di luoghi, oggetti, personaggi
- **Dialoghi:** conversazioni realistiche e funzionali alla trama
- **Enigmi e puzzle:** progettare sfide logiche integrate nella narrazione
- **Stile narrativo:** tono, registro, atmosfera

### Competenze Informatica (50%)
- Utilizzo di librerie e API
- Programmazione orientata agli oggetti
- Strutture dati (dizionari, liste, classi)
- Debugging e testing
- Organizzazione del codice
- Documentazione tecnica

---

## Struttura UDA

### FASE 1: Progettazione (Italiano)
**Consegne:**
1. Concept e tema dell'avventura
2. Mappa narrativa (grafo delle stanze)
3. Documento di progettazione completo (stile, trama, personaggi, enigmi)

### FASE 2: Implementazione Progressiva (Informatica + Italiano)
**Esercizi incrementali:**
1. Mappa e sistema di movimento
2. Descrizioni ambientali e atmosfera
3. Oggetti osservabili e interattivi
4. Sistema di puzzle ed eventi
5. NPC e dialoghi
6. Integrazione finale e testing

### FASE 3: Rifinitura e Presentazione
**Consegne:**
1. Playtest e correzioni
2. Documentazione finale
3. Presentazione del lavoro

---

## Esercizi Dettagliati

### 📝 Es0: Introduzione al Motore (DEMO - NON VALUTATO)
**Obiettivo:** Familiarizzare con il motore fornito.

**Attività:**
- Giocare alle avventure d'esempio:
  - "Il Mistero della Villa Abbandonata" (giallo/investigativo)
  - "Le Idi di Marzo" (storico - Roma antica con finali multipli)
- Analizzare il codice sorgente degli esempi
- Comprendere come funziona il parser
- Sperimentare con i comandi in linguaggio naturale

**Tempo:** 3-4 ore

---

### 🗺️ Es1: Mappa e Movimento (ITALIANO 30% + INFORMATICA 70%)

**Parte Italiano (3-5 ore):**
- Disegnare la mappa del mondo di gioco (almeno 8 stanze)
- Scrivere un paragrafo di ambientazione generale
- Dare nomi evocativi ai luoghi
- Pianificare i collegamenti logici tra le stanze

**Consegna:** Documento con mappa disegnata e giustificazione delle scelte narrative.

**Parte Informatica (5-7 ore):**
- Implementare le stanze usando la classe `Room`
- Definire le connessioni (nord, sud, est, ovest, su, giù)
- Scrivere descrizioni brevi per ogni stanza
- Testare il movimento

**Consegna:** File Python funzionante con mappa esplorabile.

**Esempio fornito:** Vedi `esempio_es1_mappa.py`

**Valutazione (10% del totale):**
| Criterio | Peso |
|----------|------|
| Coerenza geografica della mappa (ITA) | 30% |
| Nomi evocativi e atmosfera (ITA) | 20% |
| Implementazione corretta (INFO) | 40% |
| Descrizioni chiare (ITA+INFO) | 10% |

---

### 📖 Es2: Descrizioni Ambientali e Atmosfera (ITALIANO 70% + INFORMATICA 30%)

**Parte Italiano (6-8 ore):**
- Scrivere descrizioni dettagliate per ogni stanza (100-200 parole)
- Creare atmosfera attraverso dettagli sensoriali
- Usare tecniche narrative (show don't tell, metafore, similitudini)
- Mantenere coerenza di stile e tono

**Consegna:** Documento con tutte le descrizioni + analisi dello stile scelto.

**Parte Informatica (2-3 ore):**
- Integrare le descrizioni lunghe nelle stanze
- Aggiungere descrizioni alternative (es. al buio, dopo eventi)
- Testare la visualizzazione

**Consegna:** Aggiornamento del file Python con descrizioni complete.

**Esempio fornito:** Vedi `esempio_es2_descrizioni.py`

**Valutazione (15% del totale):**
| Criterio | Peso |
|----------|------|
| Qualità letteraria (ITA) | 40% |
| Coerenza stile e tono (ITA) | 30% |
| Implementazione tecnica (INFO) | 20% |
| Integrazione funzionale (INFO) | 10% |

---

### 🔍 Es3: Oggetti Osservabili e Interattivi (ITALIANO 40% + INFORMATICA 60%)

**Parte Italiano (4-6 ore):**
- Progettare 10-15 oggetti significativi per la storia
- Scrivere descrizioni dettagliate per ciascuno
- Definire azioni speciali per oggetti chiave
- Pianificare oggetti come indizi per enigmi

**Consegna:** Documento con lista oggetti, descrizioni, funzioni narrative.

**Parte Informatica (6-8 ore):**
- Implementare oggetti usando la classe `Item`
- Definire azioni custom (oltre a osserva, prendi, usa)
- Gestire oggetti fissi vs raccoglibili
- Posizionare oggetti nelle stanze appropriate

**Consegna:** Aggiornamento Python con oggetti funzionanti.

**Esempio fornito:** Vedi `esempio_es3_oggetti.py`

**Valutazione (15% del totale):**
| Criterio | Peso |
|----------|------|
| Rilevanza narrativa oggetti (ITA) | 30% |
| Qualità descrizioni (ITA) | 20% |
| Implementazione azioni (INFO) | 35% |
| Testing e funzionalità (INFO) | 15% |

---

### 🧩 Es4: Puzzle ed Eventi (ITALIANO 50% + INFORMATICA 50%)

**Parte Italiano (5-7 ore):**
- Progettare 3-5 enigmi integrati nella trama
- Scrivere la logica narrativa di ogni puzzle
- Creare indizi disseminati nel mondo
- Bilanciare difficoltà e soddisfazione

**Consegna:** Documento di progettazione puzzle con soluzioni e indizi.

**Parte Informatica (5-7 ore):**
- Implementare sistema di eventi
- Codificare la logica dei puzzle
- Gestire stati del gioco (es. porta aperta/chiusa)
- Implementare feedback al giocatore

**Consegna:** Aggiornamento Python con puzzle funzionanti.

**Esempio fornito:** Vedi `esempio_es4_puzzle.py`

**Valutazione (20% del totale):**
| Criterio | Peso |
|----------|------|
| Originalità e creatività puzzle (ITA) | 30% |
| Integrazione narrativa (ITA) | 20% |
| Logica implementazione (INFO) | 35% |
| Usabilità e feedback (INFO) | 15% |

---

### 💬 Es5: NPC e Dialoghi (ITALIANO 60% + INFORMATICA 40%)

**Parte Italiano (6-8 ore):**
- Creare 3-5 NPC caratterizzati
- Scrivere background e personalità
- Progettare alberi di dialogo
- Integrare NPC nella trama (forniscono indizi, oggetti, aprono percorsi)

**Consegna:** Documento personaggi + script dialoghi completi.

**Parte Informatica (4-6 ore):**
- Implementare NPC usando la classe `NPC`
- Codificare dialoghi e risposte
- Gestire dialoghi che attivano eventi
- Implementare stati dell'NPC (es. amichevole/ostile)

**Consegna:** Aggiornamento Python con NPC funzionanti.

**Esempio fornito:** Vedi `esempio_es5_npc.py`

**Valutazione (15% del totale):**
| Criterio | Peso |
|----------|------|
| Caratterizzazione personaggi (ITA) | 35% |
| Qualità dialoghi (ITA) | 25% |
| Implementazione tecnica (INFO) | 30% |
| Integrazione eventi (INFO) | 10% |

---

### 🎯 Es6: Progetto Finale - Avventura Completa (ITALIANO 50% + INFORMATICA 50%)

**Requisiti:**

**Italiano:**
- Trama completa con inizio, sviluppo, climax, conclusione
- Almeno 2 colpi di scena
- 8-12 stanze con descrizioni dettagliate
- 3-5 enigmi integrati
- 3-5 NPC caratterizzati
- Documento di progettazione narrativa completo

**Informatica:**
- Codice funzionante e senza bug critici
- Tutte le funzionalità implementate
- Almeno 15 oggetti interattivi
- Sistema di eventi complesso
- Codice commentato e organizzato
- README con istruzioni

**Presentazione:**
- Demo giocabile (10-15 minuti)
- Presentazione delle scelte narrative
- Analisi tecnica dell'implementazione

**Valutazione (25% del totale):**
| Criterio | Peso |
|----------|------|
| Qualità narrativa complessiva (ITA) | 25% |
| Originalità e creatività (ITA) | 15% |
| Funzionalità tecnica (INFO) | 25% |
| Qualità del codice (INFO) | 15% |
| Completezza | 10% |
| Presentazione | 10% |

---

## Il Motore: `text_adventure_engine`

### Caratteristiche Principali

**Parser di Linguaggio Naturale:**
- Comprende frasi in italiano naturale
- Riconosce sinonimi e varianti
- Gestisce articoli, preposizioni, pronomi
- Comandi supportati: vai, prendi, lascia, osserva, usa, parla, inventario, aiuto, etc.

**Sistema di Stanze:**
- Navigazione multi-direzionale (N, S, E, O, SU, GIÙ)
- Descrizioni brevi e lunghe
- Visibilità condizionale

**Sistema Oggetti:**
- Proprietà customizzabili
- Azioni base + azioni custom
- Stati (prendibile, contenitore, nascosto, etc.)
- Combinazioni tra oggetti

**Sistema NPC:**
- Dialoghi strutturati
- Stati e comportamenti
- Eventi attivabili

**Sistema Eventi:**
- Trigger basati su condizioni
- Modifica dello stato del mondo
- Catene di eventi

### Utilizzo Base

```python
from text_adventure_engine import Game, Room, Item, NPC

# Creare il gioco
game = Game(
    title="La Mia Avventura",
    author="Nome Studente",
    intro="Testo introduttivo..."
)

# Creare stanze
sala = Room(
    name="Sala Grande",
    description="Una vasta sala con soffitti altissimi...",
    short_desc="Sala Grande"
)

# Aggiungere oggetti
chiave = Item(
    name="chiave",
    description="Una chiave arrugginita...",
    can_take=True
)
sala.add_item(chiave)

# Creare NPC
custode = NPC(
    name="custode",
    description="Un vecchio custode...",
    dialogue={
        "default": "Buongiorno, posso aiutarti?"
    }
)
sala.add_npc(custode)

# Connettere stanze
game.add_room("sala", sala)
game.set_start("sala")
game.connect_rooms("sala", "north", "biblioteca")

# Avviare il gioco
game.start()
```

---

## Pianificazione Temporale

| Fase | Attività | Ore |
|------|----------|-----|
| **Settimana 1-2** | Es0 + Es1 | 12h |
| **Settimana 3-4** | Es2 + Es3 | 16h |
| **Settimana 5-6** | Es4 + Es5 | 18h |
| **Settimana 7-10** | Es6 (Progetto Finale) | 25h |
| **Settimana 11** | Presentazioni | 4h |

**TOTALE: 75 ore** (ideale per un quadrimestre con 2h/settimana ITA + 3h/settimana INFO)

---

## Valutazione Finale

### Peso Esercizi
- Es1: 10%
- Es2: 15%
- Es3: 15%
- Es4: 20%
- Es5: 15%
- Es6: 25%

### Suddivisione Discipline
- **Italiano:** 50% (progettazione, scrittura, narrativa)
- **Informatica:** 50% (implementazione, debugging, organizzazione codice)

### Griglia Valutazione Progetto Finale

**Eccellente (9-10):**
- Trama originale con colpi di scena efficaci
- Stile narrativo maturo e coerente
- Enigmi creativi e ben integrati
- Codice pulito, funzionante, senza bug
- Implementazione completa di tutte le features

**Buono (7-8):**
- Trama interessante con sviluppo adeguato
- Descrizioni di buona qualità
- Enigmi funzionali
- Codice funzionante con qualche bug minore
- Maggior parte delle features implementate

**Sufficiente (6):**
- Trama basilare ma completa
- Descrizioni essenziali
- Almeno un enigma funzionante
- Codice con alcuni bug ma giocabile
- Features principali implementate

**Insufficiente (<6):**
- Trama incompleta o incoerente
- Descrizioni scarse o assenti
- Nessun enigma o non funzionanti
- Codice non funzionante o troppi bug
- Features mancanti o non implementate

---

## Esempi e Risorse

### File Forniti
- `text_adventure_engine.py` - Il motore completo
- `esempio_villa_misteriosa.py` - **Avventura 1: Il Mistero della Villa Abbandonata** (Giallo/Investigativo)
- `esempio_idi_di_marzo.py` - **Avventura 2: Le Idi di Marzo** (Storico - Roma Antica, 44 a.C.)
- `esempio_es1_mappa.py` - Esempio esercizio 1
- `esempio_es2_descrizioni.py` - Esempio esercizio 2
- `esempio_es3_oggetti.py` - Esempio esercizio 3
- `esempio_es4_puzzle.py` - Esempio esercizio 4
- `esempio_es5_npc.py` - Esempio esercizio 5

### Avventure Complete d'Esempio

#### 🏚️ **Il Mistero della Villa Abbandonata**
- **File:** `esempio_villa_misteriosa.py`
- **Genere:** Giallo/Investigativo
- **Ambientazione:** Villa vittoriana abbandonata, epoca contemporanea
- **Durata:** 20-30 minuti
- **Difficoltà:** Media
- **Trama:** Detective chiamato a investigare la scomparsa del Professor Blackwood. 12 stanze da esplorare, puzzle a catena, laboratorio segreto, colpo di scena finale.
- **Didattica:** Perfetto per mostrare struttura investigativa, raccolta indizi, atmosfera gotica/noir.

#### 🏛️ **Le Idi di Marzo - Un Complotto a Roma**
- **File:** `esempio_idi_di_marzo.py`
- **Genere:** Storico/Thriller Politico
- **Ambientazione:** Antica Roma, 14-15 marzo 44 a.C.
- **Durata:** 25-35 minuti
- **Difficoltà:** Media-Alta
- **Trama:** Sei Marcus Verus, scriba che scopre il complotto per uccidere Giulio Cesare. Devi decidere: avvertire Cesare, rimanere in silenzio, o avvertire i veterani. **3 finali multipli** basati sulle tue scelte.
- **Didattica:**
  - Storia romana (personaggi reali: Bruto, Cassio, Calpurnia)
  - Cultura romana (domus, Foro, terme, oggetti d'epoca)
  - Puzzle storici (cifra di Cesare)
  - Dilemmi morali e scelte con conseguenze
  - Riferimenti storici accurati per scopo educativo

### Generi Consigliati
- 🕵️ **Giallo/Investigativo:** Risolvere un mistero
- 🏛️ **Storico:** Rivivere un evento storico
- 🌌 **Fantascientifico:** Esplorazione spaziale
- 🏰 **Fantasy:** Quest in mondi magici
- 😱 **Horror:** Atmosfere inquietanti
- 🎭 **Drammatico:** Storie a forte impatto emotivo

### Risorse Esterne
- [Interactive Fiction Database](https://ifdb.org/) - Database di avventure testuali
- [Zork](https://en.wikipedia.org/wiki/Zork) - Classico delle avventure testuali
- [Inform 7](http://inform7.com/) - Linguaggio per IF moderno
- Giocare avventure testuali classiche per ispirazione

---

## Consigli per Studenti

### Per la Parte Italiano
1. **Pianifica prima di scrivere:** Fai schemi, mappe mentali, scalette
2. **Show, don't tell:** Mostra attraverso dettagli, non dire direttamente
3. **Coerenza è fondamentale:** Mantieni tono e stile uniformi
4. **Ogni elemento serve:** Non mettere oggetti/NPC inutili
5. **Testa la tua storia:** Falla leggere ad altri per feedback

### Per la Parte Informatica
1. **Leggi la documentazione:** Il motore è ben commentato
2. **Testa frequentemente:** Non aspettare la fine per testare
3. **Usa print() per debugging:** Controlla cosa succede nel codice
4. **Chiedi aiuto:** Il codice è complesso, è normale avere dubbi
5. **Commenta il tuo codice:** Ti aiuterà a ricordare cosa fa

### Per Entrambe
1. **Lavora incrementalmente:** Fai un pezzo alla volta
2. **Backup frequenti:** Salva spesso il tuo lavoro
3. **Chiedi feedback:** Dai da giocare la tua avventura ad altri
4. **Sii creativo:** Questa è la tua storia, rendila unica
5. **Divertiti:** Se ti diverti tu, si divertiranno anche i giocatori

---

## FAQ

**D: Posso lavorare in gruppo?**
R: Sì, gruppi di 2-3 persone. Deve essere chiaro chi ha fatto cosa.

**D: Posso modificare il motore?**
R: No per gli esercizi base. Sì per il progetto finale se documentate le modifiche.

**D: Quanto deve essere lunga l'avventura?**
R: Circa 15-30 minuti di gioco per un giocatore che risolve gli enigmi.

**D: Posso usare AI per scrivere?**
R: No. La scrittura deve essere completamente vostra. L'originalità è valutata.

**D: Come testo se funziona tutto?**
R: Gioca alla tua avventura! Prova tutti i percorsi possibili.

**D: E se trovo un bug nel motore?**
R: Segnalalo al docente, verrà corretto per tutti.

---

**Buona creazione delle vostre avventure testuali! 🎮📚✨**
