# Es4: Inventario e Sistema di Oggetti 🎒

**Livello:** INTERMEDIO
**Durata stimata:** 5-6 ore

## Descrizione

Crea un sistema completo di inventario con oggetti raccoglibili, utilizzabili e combinabili, tipico dei giochi d'avventura.

## Obiettivi

### Competenze Italiano
- Descrivere oggetti in modo evocativo
- Creare oggetti con significato narrativo
- Scrivere messaggi di feedback chiari
- Progettare puzzle basati sugli oggetti

### Competenze Informatica
- Classi e oggetti (OOP)
- Liste e dizionari per gestire collezioni
- Logica di combinazione oggetti
- Stati degli oggetti (usabile, combinabile, chiave)
- Gestione peso/limiti inventario

## Consegna

Implementare un sistema di inventario con:

### 1. Oggetti
- Almeno 10 oggetti diversi nel gioco
- Ogni oggetto ha:
  - Nome
  - Descrizione
  - Peso (opzionale)
  - Proprietà (usabile, combinabile, quest item)

### 2. Comandi Inventario
- **prendi [oggetto]**: raccogliere oggetto dalla stanza
- **lascia [oggetto]**: lasciare oggetto nella stanza
- **inventario** (o **i**): vedere oggetti posseduti
- **esamina [oggetto]**: descrizione dettagliata
- **usa [oggetto]**: utilizzare un oggetto
- **combina [oggetto1] con [oggetto2]**: creare nuovo oggetto

### 3. Meccaniche
- Limite di peso o numero oggetti (opzionale)
- Oggetti "chiave" necessari per proseguire
- Combinazioni logiche (es. fiammiferi + candela = candela accesa)
- Oggetti a uso singolo vs riutilizzabili
- Feedback descrittivo per ogni azione

### 4. Integrazione con Stanze
- Oggetti posizionati nelle stanze
- Oggetti nascosti (scopribili con azioni speciali)
- Oggetti fissi (non raccoglibili ma esaminabili)

## Esempio di Utilizzo

```
=== AVVENTURA CON INVENTARIO ===

Ti trovi in: Biblioteca Polverosa

Vedi qui:
- una chiave arrugginita
- un vecchio libro

> prendi chiave
Hai raccolto la chiave arrugginita.

> prendi libro
Hai raccolto il vecchio libro.

> inventario
Stai trasportando:
1. Chiave arrugginita (0.1 kg)
2. Vecchio libro (0.5 kg)

Peso totale: 0.6 / 10.0 kg

> esamina libro
Un antico tomo rilegato in pelle. Sulle pagine ingiallite
noti un enigma scritto a mano: "Solo il fuoco rivela la verità"

> vai nord

Ti trovi in: Studio del Professore

Vedi qui:
- candela spenta
- scatola di fiammiferi

> prendi candela
Hai raccolto la candela spenta.

> prendi fiammiferi
Hai raccolto la scatola di fiammiferi.

> combina fiammiferi con candela
Hai acceso la candela! Ora la fiamma illumina la stanza.

[Nuovo oggetto: "candela accesa" creato]

> usa candela accesa
Avvicini la candela accesa alle pagine del libro. Lentamente,
appare una scritta invisibile: "La chiave apre la porta est"

> vai est

C'è una porta chiusa a chiave.

> usa chiave
Usi la chiave arrugginita. La porta cigola aprendosi!
```

## Suggerimenti di Codice

### Classe Oggetto

```python
class Oggetto:
    def __init__(self, nome, descrizione, peso=0, usabile=False, combinabile=False):
        self.nome = nome
        self.descrizione = descrizione
        self.peso = peso
        self.usabile = usabile
        self.combinabile = combinabile
        self.usato = False

    def esamina(self):
        return self.descrizione

    def usa(self):
        if not self.usabile:
            return f"Non puoi usare {self.nome}."
        if self.usato:
            return f"{self.nome} è già stato usato."
        self.usato = True
        return f"Hai usato {self.nome}."

# Creazione oggetti
chiave = Oggetto(
    "chiave arrugginita",
    "Una vecchia chiave di ferro, arrugginita dal tempo.",
    peso=0.1,
    usabile=True
)

libro = Oggetto(
    "vecchio libro",
    "Un antico tomo rilegato in pelle con pagine ingiallite.",
    peso=0.5
)
```

### Sistema Inventario

```python
class Inventario:
    def __init__(self, peso_max=10.0):
        self.oggetti = []
        self.peso_max = peso_max

    def peso_attuale(self):
        return sum(obj.peso for obj in self.oggetti)

    def aggiungi(self, oggetto):
        if self.peso_attuale() + oggetto.peso > self.peso_max:
            return False, "Inventario pieno!"
        self.oggetti.append(oggetto)
        return True, f"Hai raccolto {oggetto.nome}."

    def rimuovi(self, nome_oggetto):
        for obj in self.oggetti:
            if obj.nome.lower() == nome_oggetto.lower():
                self.oggetti.remove(obj)
                return True, obj
        return False, None

    def contiene(self, nome_oggetto):
        return any(obj.nome.lower() == nome_oggetto.lower()
                   for obj in self.oggetti)

    def mostra(self):
        if not self.oggetti:
            return "L'inventario è vuoto."

        output = "Stai trasportando:\n"
        for i, obj in enumerate(self.oggetti, 1):
            output += f"{i}. {obj.nome} ({obj.peso} kg)\n"
        output += f"\nPeso totale: {self.peso_attuale():.1f} / {self.peso_max} kg"
        return output

# Uso
inventario = Inventario(peso_max=10.0)
successo, msg = inventario.aggiungi(chiave)
print(msg)
```

### Sistema Combinazioni

```python
combinazioni = {
    ("fiammiferi", "candela"): {
        "risultato": Oggetto(
            "candela accesa",
            "Una candela che brucia con una fiamma costante.",
            peso=0.3,
            usabile=True
        ),
        "messaggio": "Hai acceso la candela! Ora la fiamma illumina la stanza.",
        "rimuovi": ["fiammiferi", "candela"]
    },
    ("chiave", "porta"): {
        "messaggio": "Hai aperto la porta!",
        "azione": "apri_porta_est"
    }
}

def combina_oggetti(obj1_nome, obj2_nome, inventario):
    """Combina due oggetti se possibile"""
    chiave = tuple(sorted([obj1_nome.lower(), obj2_nome.lower()]))

    if chiave in combinazioni:
        combo = combinazioni[chiave]

        # Rimuovi oggetti usati
        if "rimuovi" in combo:
            for nome in combo["rimuovi"]:
                inventario.rimuovi(nome)

        # Aggiungi risultato
        if "risultato" in combo:
            inventario.aggiungi(combo["risultato"])

        return True, combo["messaggio"]

    return False, "Non puoi combinare questi oggetti."
```

### Integrazione con Stanze

```python
stanze = {
    "biblioteca": {
        "nome": "Biblioteca Polverosa",
        "descrizione": "Scaffali pieni di libri antichi...",
        "oggetti": [chiave, libro],
        "nord": "studio"
    },
    "studio": {
        "nome": "Studio del Professore",
        "descrizione": "Una scrivania ingombra di carte...",
        "oggetti": [candela, fiammiferi],
        "sud": "biblioteca"
    }
}

def prendi_oggetto(nome_oggetto, stanza_corrente, inventario):
    """Prende un oggetto dalla stanza"""
    stanza = stanze[stanza_corrente]

    for obj in stanza["oggetti"]:
        if obj.nome.lower() == nome_oggetto.lower():
            successo, msg = inventario.aggiungi(obj)
            if successo:
                stanza["oggetti"].remove(obj)
            return msg

    return f"Non vedo nessun '{nome_oggetto}' qui."
```

## Oggetti di Esempio

### Chiavi e Serrature
- Chiave arrugginita → Apre porta biblioteca
- Chiave d'oro → Apre cassaforte
- Chiave scheletro → Apre tutte le porte

### Oggetti Illuminanti
- Candela + Fiammiferi → Candela accesa
- Torcia + Batterie → Torcia funzionante
- Lanterna + Olio → Lanterna accesa

### Oggetti Puzzle
- Lente d'ingrandimento → Rivela scritte nascoste
- Mappa → Mostra percorso segreto
- Codice → Sblocca cassaforte

### Oggetti Quest
- Lettera → Avvia missione
- Foto → Indizio per enigma
- Amuleto → Necessario per finale

## Meccaniche Avanzate

### Peso e Ingombro
```python
# Oggetti pesanti limitano movimento
if inventario.peso_attuale() > 8.0:
    velocita_movimento = "lento"
else:
    velocita_movimento = "normale"
```

### Oggetti Deteriorabili
```python
class OggettoDeteriorabile(Oggetto):
    def __init__(self, nome, descrizione, durata):
        super().__init__(nome, descrizione, usabile=True)
        self.durata = durata

    def usa(self):
        self.durata -= 1
        if self.durata <= 0:
            return f"{self.nome} si è consumato completamente!"
        return f"Hai usato {self.nome}. Usi rimanenti: {self.durata}"

# Esempio: Torcia con batterie limitate
torcia = OggettoDeteriorabile("torcia", "Una torcia a pile.", durata=5)
```

## Estensioni

- Crafting system complesso (più ingredienti)
- Oggetti equipaggiabili (armi, armature)
- Durabilità oggetti
- Oggetti consumabili (pozioni)
- Container (borse, casse) per più spazio
- Trading con NPC
- Oggetti unici vs stackabili (monete, frecce)

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🎒✨**
