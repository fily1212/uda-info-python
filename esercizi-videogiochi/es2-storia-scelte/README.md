# Es2: Storia a Scelte Multiple 📖

**Livello:** BASE
**Durata stimata:** 4-5 ore

## Descrizione

Scrivi una storia interattiva dove ogni scelta del giocatore influenza la trama e porta a finali diversi. Un'avventura "choose your own adventure" in stile librogame.

## Obiettivi

### Competenze Italiano
- Scrivere una trama coerente con inizio, sviluppo e conclusione
- Creare bivi narrativi significativi
- Sviluppare personaggi e dialoghi
- Mantenere coerenza tra scelte e conseguenze
- Creare almeno 3 finali diversi

### Competenze Informatica
- Strutture dati per albero decisionale
- Logica condizionale complessa
- Tracking delle scelte del giocatore
- Funzioni ricorsive o iterative per navigare la storia
- Gestione dello stato del gioco

## Consegna

Creare una storia interattiva con:

### 1. Struttura Narrativa
- **Inizio comune**: tutti i giocatori partono dallo stesso punto
- **Almeno 10 scene/nodi**: momenti decisionali
- **Almeno 3 finali distinti**: diversi esiti della storia
- **Scelte significative**: che impattano realmente sulla trama

### 2. Meccaniche di Gioco
- Ad ogni bivio, presentare 2-3 opzioni
- Le scelte passate influenzano quelle future (opzionale ma consigliato)
- Tracking variabili (es. coraggio, intelligenza, relazioni)
- Possibilità di game over/morte

### 3. Tematiche (Scegli Una)
- 🕵️ **Giallo**: risolvi un mistero
- 🏰 **Fantasy**: quest epica
- 🚀 **Fantascienza**: esplorazione spaziale
- 😱 **Horror**: sopravvivi al terrore
- 💕 **Romantico**: storia d'amore
- 🎓 **Storico**: rivi eventi del passato

## Esempio di Utilizzo

```
=== IL MISTERO DEL FARO ===

Sei un investigatore chiamato a indagare sulla scomparsa
del guardiano del faro sull'Isola Nera. Arriva al faro
una notte tempestosa. La porta è socchiusa.

Cosa fai?
1. Entri immediatamente
2. Chiami prima la polizia
3. Esplori l'esterno del faro

Scelta: 1

Entri nel faro. L'interno è buio e silenzioso. Vedi una
scala a chiocciola che sale e una porta sotto la scala.

Cosa fai?
1. Sali le scale
2. Apri la porta sotto la scala
3. Accendi la tua torcia ed esplori il piano terra

Scelta: 2

[La storia continua...]

=== FINALE: LA VERITÀ SEPOLTA ===

Scopri che il guardiano non è scomparso, ma si nascondeva
dai contrabbandieri. Lo salvi e diventi un eroe locale.

Punteggio: 85/100
Finali scoperti: 1/3
```

## Suggerimenti di Codice

### Struttura a Dizionario

```python
storia = {
    "inizio": {
        "testo": "Sei un investigatore chiamato a indagare...",
        "scelte": {
            "1": {"testo": "Entri immediatamente", "prossima": "dentro_faro"},
            "2": {"testo": "Chiami prima la polizia", "prossima": "chiama_polizia"},
            "3": {"testo": "Esplori l'esterno", "prossima": "esplora_esterno"}
        }
    },
    "dentro_faro": {
        "testo": "Entri nel faro. L'interno è buio...",
        "scelte": {
            "1": {"testo": "Sali le scale", "prossima": "scale"},
            "2": {"testo": "Porta sotto scala", "prossima": "cantina"},
            "3": {"testo": "Esplori piano terra", "prossima": "piano_terra"}
        }
    },
    "cantina": {
        "testo": "Scopri che il guardiano si nascondeva dai contrabbandieri...",
        "finale": "LA VERITÀ SEPOLTA",
        "scelte": {}  # Nessuna scelta = finale
    },
    # ... altre scene
}
```

### Engine di Gioco

```python
def gioca_storia():
    scena_corrente = "inizio"
    stats = {"coraggio": 50, "intelligenza": 50}

    print("=== IL MISTERO DEL FARO ===\n")

    while True:
        scena = storia[scena_corrente]

        # Mostra testo scena
        print(scena["testo"])
        print()

        # Controlla se è un finale
        if "finale" in scena:
            print(f"=== FINALE: {scena['finale']} ===")
            break

        # Mostra scelte
        for numero, scelta in scena["scelte"].items():
            print(f"{numero}. {scelta['testo']}")

        # Input giocatore
        scelta_input = input("\nScelta: ")

        if scelta_input in scena["scelte"]:
            scena_corrente = scena["scelte"][scelta_input]["prossima"]
            print("\n" + "="*50 + "\n")
        else:
            print("Scelta non valida!")

gioca_storia()
```

### Con Tracking Stats (Avanzato)

```python
def mostra_scena_con_stats(scena_id, stats):
    scena = storia[scena_id]

    # Alcune scene possono richiedere stats minime
    if "requisiti" in scena:
        if stats["coraggio"] < scena["requisiti"].get("coraggio", 0):
            return "game_over_paura"

    # Modificare stats in base alla scelta
    if "modifica_stats" in scena:
        for stat, valore in scena["modifica_stats"].items():
            stats[stat] += valore

    return scena_id
```

## Struttura Mappa Storia (Esempio)

```
            [Inizio]
               |
       +-------+-------+
       |       |       |
   [Entra] [Chiama] [Esplora]
       |       |       |
       |       |    [Trova indizio]
       |       |       |
   [Scale] [Polizia] [Entra preparato]
       |       |       |
    +--+--+    |    +--+--+
    |     |    |    |     |
[Sopra][Sotto]|[Piano][Sopra]
    |     |    |    |     |
[Fine1][Fine2][Fine3][Fine1]
```

## Consigli per la Storia

1. **Inizia semplice**: 5-7 scene, 2 finali
2. **Espandi gradualmente**: aggiungi rami e complessità
3. **Ogni scelta conta**: evita scelte "finte"
4. **Bilancia i finali**: non troppo facili o difficili da raggiungere
5. **Testa tutti i percorsi**: assicurati che ogni ramo funzioni

## Tracciare le Scelte

```python
# Tenere registro delle decisioni
scelte_fatte = []

def registra_scelta(scelta_id, scelta_testo):
    scelte_fatte.append({"id": scelta_id, "testo": scelta_testo})

def mostra_recap():
    print("\n=== RECAP DELLE TUE SCELTE ===")
    for i, scelta in enumerate(scelte_fatte, 1):
        print(f"{i}. {scelta['testo']}")
```

## Estensioni

- Sistema di inventario semplice
- Relazioni con personaggi che cambiano
- Mini-puzzle o enigmi
- Salvataggio/caricamento partita
- Statistiche finali (scelte, finali scoperti)
- Achievements/trofei

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 📖✨**
