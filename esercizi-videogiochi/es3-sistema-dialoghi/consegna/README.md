# Es3: Parser Testuale Avanzato (stile Inform6)

## Obiettivi
- **Italiano**: Scrittura descrizioni evocative, dialoghi naturali
- **Informatica**: Parsing linguaggio naturale, pattern matching, NLP base

## Descrizione

Crea un vero **parser testuale** come nei classici giochi Infocom/Inform6, dove i giocatori scrivono comandi in linguaggio naturale invece di scegliere da menu!

## Differenza con Es1-2

### Esercizio 1 (Motore Base):
```
> 1. Vai a nord
> 2. Prendi chiave
> 3. Esamina porta
```
✅ Facile, ma limitato

### Esercizio 3 (Parser):
```
> prendi la chiave dorata dal tavolo
> esamina attentamente la porta misteriosa
> parla con il mago della profezia
> usa la chiave sulla porta
```
✅ Immersivo, libero, naturale!

## Comandi Supportati

Il parser deve riconoscere:

### Movimento
- `vai nord`, `va a est`, `muovi sud`
- `nord`, `n`, `su`, `giù` (diretto)
- `entra`, `esci`, `sali`, `scendi`

### Osservazione
- `guarda`, `look`, `l`
- `esamina [oggetto]`, `ispeziona [oggetto]`
- `guarda [oggetto]`, `osserva [personaggio]`

### Manipolazione
- `prendi [oggetto]`, `raccogli [oggetto]`, `afferra [oggetto]`
- `lascia [oggetto]`, `posa [oggetto]`, `drop [oggetto]`
- `usa [oggetto]`, `utilizza [oggetto]`
- `apri [oggetto]`, `chiudi [oggetto]`

### Interazione
- `parla con [NPC]`, `dialoga con [NPC]`
- `chiedi di [argomento]`, `domanda su [argomento]`

## Caratteristiche Chiave

### 1. Sinonimi
```python
VERBI = {
    'prendi': ['prendi', 'raccogli', 'afferra', 'take', 'get'],
    'guarda': ['guarda', 'esamina', 'osserva', 'look', 'x'],
}
```

### 2. Articoli Ignorabili
```python
"prendi la chiave dorata" = "prendi chiave dorata"
```

### 3. Pattern Matching
```python
# Riconosce:
"parla con il mago di magia"
# Come:
verbo: parla
oggetto: mago
argomento: magia
```

### 4. Stati Dinamici
```python
oggetto.stato = {
    'aperto': True,
    'acceso': False,
    'rotto': False
}
```

## Implementazione

### Classe Oggetto
```python
class Oggetto:
    def __init__(self, nome, sinonimi, descrizione):
        self.nome = nome
        self.sinonimi = ['spada', 'lama', 'arma']
        self.descrizione = "..."
        self.raccoglibile = True
        self.stato = {}

    def corrisponde(self, parola):
        return parola in self.sinonimi
```

### Classe Parser
```python
class Parser:
    def parse(self, comando):
        # 1. Pulisci input (rimuovi articoli)
        # 2. Identifica verbo
        # 3. Identifica oggetto/i
        # 4. Esegui azione
        pass
```

## Esercizio per Gli Studenti

### Parte 1: Scrittura Storia
Scrivi un'avventura testuale con:
- Almeno 5 stanze
- 8 oggetti interattivi
- 2 NPC con dialoghi
- 3 puzzle da risolvere

### Parte 2: Implementazione Parser
Estendi il parser per supportare:
- Nuovi verbi (`leggi`, `rompi`, `mangia`)
- Combinazioni oggetti (`metti X su Y`)
- Condizioni complesse

### Parte 3: Testing
Testa con amici/compagni che:
- I comandi siano intuitivi
- Le descrizioni siano chiare
- I puzzle siano risolvibili

## Esempi di Comandi Avanzati

### Combinazioni
```
> metti la gemma sull'altare
> colpisci la porta con l'ascia
> da la pozione al cavaliere
```

### Condizioni
```python
if giocatore.ha('spada') and stanza.ha('drago'):
    return "Combatti il drago!"
```

### Puzzle
```python
# Puzzle: Aprire porta magica
if 'runa rossa' in inventario and 'runa blu' in inventario:
    if comando == "usa rune su porta":
        porta.apri()
```

## Risorse

### Parser Classici
- **Zork** (Infocom, 1980)
- **Colossal Cave Adventure** (1976)
- **Inform 7** - linguaggio moderno per IF

### Librerie Python
- `nltk` - Natural Language Toolkit (avanzato)
- `spacy` - NLP moderno
- Regex per pattern matching

## Valutazione

| Aspetto | Peso |
|---------|------|
| Ricchezza vocabolario parser | 25% |
| Qualità descrizioni | 25% |
| Logica puzzle | 20% |
| Dialoghi NPC | 15% |
| Gestione errori utente | 15% |

## Esempio Sessione di Gioco

```
La Cripta del Mago Aldrin
═══════════════════════════════════

> guarda
Sei all'ingresso di una cripta antica. Muri di pietra,
aria fredda. Una scala scende a nord.

Vedi: torcia

> prendi torcia
✅ Preso: torcia

> nord
Corridoio Buio
È buio pesto. Non vedi nulla.

> usa torcia
🔥 Accendi la torcia. La luce illumina l'oscurità!

> guarda
Un corridoio stretto illuminato dalla tua torcia...

> nord
Sala delle Statue
Quattro statue ti circondano...

> esamina statua
Una statua di guerriero. Alla base brilla qualcosa!

> prendi chiave dalla statua
✅ Preso: chiave d'oro

> est
Biblioteca del Mago
Scaffali polverosi...

C'è: Fantasma del Mago Aldrin

> parla con fantasma
Fantasma: "Benvenuto nella mia dimora..."

> chiedi di tesoro
Fantasma: "Il tesoro è protetto. Serve luce e chiave..."
```

**Questo è il potere di un parser testuale!** 🎮✨
