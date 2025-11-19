# Es1: Motore Base Avventura Testuale 🎮

**Livello:** FACILE
**Durata stimata:** 3-4 ore

## Descrizione

Crea il motore fondamentale per un'avventura testuale: sistema di stanze, movimenti tra le stanze, descrizioni e comandi testuali base.

## Obiettivi

### Competenze Italiano
- Scrivere descrizioni evocative dei luoghi
- Dare nomi significativi alle location
- Creare coerenza geografica
- Storytelling ambientale

### Competenze Informatica
- Dizionari per rappresentare stanze e connessioni
- Gestione stato del gioco
- Parser di comandi semplice
- Loop di gioco (game loop)
- Funzioni e organizzazione codice

## Consegna

Implementare un motore base con:

### 1. Sistema di Stanze
- Almeno 5 stanze interconnesse
- Ogni stanza ha:
  - Nome
  - Descrizione
  - Connessioni (nord, sud, est, ovest)

### 2. Comandi Supportati
- **vai [direzione]**: muoversi tra stanze
- **guarda**: vedere descrizione stanza attuale
- **aiuto**: mostrare comandi disponibili
- **esci**: terminare il gioco

### 3. Meccaniche
- Tracking della posizione corrente
- Impossibile andare in direzioni non valide
- Messaggi di errore chiari
- Descrizione automatica quando si entra in una nuova stanza

## Esempio di Utilizzo

```
=== LA TUA AVVENTURA ===

Ti trovi in: Ingresso della Villa

Sei nell'ingresso di una villa abbandonata. La polvere copre
ogni superficie. A nord vedi una scala che sale al piano
superiore, a est c'è una porta socchiusa, a ovest senti un
ticchettio di orologio.

> vai nord

Ti trovi in: Corridoio Superiore

Un lungo corridoio buio con porte su entrambi i lati.
Uscite disponibili: sud, est, ovest

> vai est

Ti trovi in: Camera da Letto

Una camera da letto polverosa con un letto disfatto.
Uscite disponibili: ovest

> vai nord
Non puoi andare in quella direzione!

> aiuto
Comandi disponibili:
- vai [direzione]: muoviti (nord/sud/est/ovest)
- guarda: osserva la stanza
- aiuto: mostra questo messaggio
- esci: esci dal gioco
```

## Suggerimenti di Codice

### Struttura Dati Stanze

```python
stanze = {
    "ingresso": {
        "nome": "Ingresso della Villa",
        "descrizione": "Sei nell'ingresso di una villa abbandonata...",
        "nord": "corridoio_superiore",
        "est": "salone",
        "ovest": "biblioteca"
    },
    "corridoio_superiore": {
        "nome": "Corridoio Superiore",
        "descrizione": "Un lungo corridoio buio...",
        "sud": "ingresso",
        "est": "camera",
        "ovest": "studio"
    },
    # ... altre stanze
}
```

### Game Loop Base

```python
def gioca():
    stanza_corrente = "ingresso"

    print("=== LA TUA AVVENTURA ===\n")
    mostra_stanza(stanza_corrente)

    while True:
        comando = input("\n> ").lower().strip()

        if comando == "esci":
            print("Grazie per aver giocato!")
            break
        elif comando == "guarda":
            mostra_stanza(stanza_corrente)
        elif comando.startswith("vai "):
            direzione = comando.split()[1]
            stanza_corrente = muovi(stanza_corrente, direzione)
        elif comando == "aiuto":
            mostra_aiuto()
        else:
            print("Comando non riconosciuto. Digita 'aiuto' per i comandi.")

def mostra_stanza(nome_stanza):
    stanza = stanze[nome_stanza]
    print(f"\nTi trovi in: {stanza['nome']}\n")
    print(stanza['descrizione'])

    # Mostra uscite
    uscite = [dir for dir in ['nord', 'sud', 'est', 'ovest']
              if dir in stanza]
    print(f"\nUscite disponibili: {', '.join(uscite)}")

def muovi(stanza_corrente, direzione):
    stanza = stanze[stanza_corrente]

    if direzione in stanza:
        nuova_stanza = stanza[direzione]
        print(f"\nVai verso {direzione}...\n")
        mostra_stanza(nuova_stanza)
        return nuova_stanza
    else:
        print("Non puoi andare in quella direzione!")
        return stanza_corrente

# Avvia il gioco
gioca()
```

## Mappa di Esempio

```
        [Studio]
            |
         (ovest)
            |
[Camera] - [Corridoio Superiore]
   |              |
 (est)         (sud)
   |              |
[Biblioteca] - [Ingresso] - [Salone]
              (ovest)      (est)
```

## Estensioni

Una volta completato il motore base, puoi aggiungere:

- Descrizioni diverse per prima visita vs rivisita
- Sinonimi per direzioni (n, s, e, o)
- Comando "mappa" per vedere dove sei
- Stanze che si sbloccano con eventi
- Descrizioni dinamiche (ora del giorno, eventi)

## Cosa Imparai

- Rappresentare un mondo di gioco con dizionari
- Gestire lo stato del programma
- Creare un'interfaccia testuale interattiva
- Loop principale di un videogioco
- Parsing semplice di comandi utente

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🎮📖**
