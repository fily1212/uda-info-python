# Es8: Convertitore di Unità di Misura

**Livello:** FACILE
**Durata stimata:** 2-3 ore

## Descrizione

Programma che converte tra diverse unità di misura fisiche: lunghezza, massa, velocità, temperatura, tempo, energia.

## Obiettivi

### Competenze Fisica
- Comprendere le unità di misura del Sistema Internazionale
- Conoscere i fattori di conversione tra unità
- Applicare conversioni in contesti pratici

### Competenze Informatica
- Dizionari per memorizzare fattori di conversione
- Funzioni per operazioni ripetute
- Menu interattivo
- Validazione input

## Consegna

Il programma deve convertire tra le seguenti unità:

### 1. Lunghezza
- Metri (m), chilometri (km), centimetri (cm), millimetri (mm)
- Miglia, piedi, pollici
- Anni luce

### 2. Massa
- Kilogrammi (kg), grammi (g), tonnellate (t)
- Libbre (lb), once (oz)

### 3. Velocità
- m/s, km/h, mph (miglia/ora)
- Nodi

### 4. Temperatura
- Celsius, Fahrenheit, Kelvin
- Formule: °F = °C × 9/5 + 32, K = °C + 273.15

### 5. Tempo
- Secondi, minuti, ore, giorni, anni

### 6. Energia (opzionale)
- Joule, calorie, kilowattora

## Esempio di Utilizzo

```
=== CONVERTITORE UNITÀ DI MISURA ===

Scegli la categoria:
1. Lunghezza
2. Massa
3. Velocità
4. Temperatura
5. Tempo
6. Esci

Scelta: 1

Unità di partenza:
1. Metri (m)
2. Chilometri (km)
3. Centimetri (cm)
4. Miglia (mi)

Scelta: 2

Unità di arrivo:
1. Metri (m)
2. Chilometri (km)
3. Centimetri (cm)
4. Miglia (mi)

Scelta: 4

Inserisci valore: 100

Risultato: 100 km = 62.137 miglia
```

## Suggerimenti

- Usa dizionari per i fattori di conversione
- Esempio: `{'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}`
- Per convertire: valore_base = valore * fattore_partenza
- Poi: valore_finale = valore_base / fattore_arrivo
- Temperatura richiede formule diverse!
- Crea una funzione per ogni categoria

## Esempio di Codice Struttura

```python
# Dizionario lunghezze (in metri)
lunghezze = {
    'm': 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
    'mi': 1609.34,  # miglio
    'ft': 0.3048,   # piede
}

def converti_lunghezza(valore, da, a):
    # Converti in metri
    metri = valore * lunghezze[da]
    # Converti nell'unità richiesta
    risultato = metri / lunghezze[a]
    return risultato
```

## Fattori di Conversione Utili

- 1 km = 1000 m
- 1 miglio = 1.60934 km
- 1 lb = 0.453592 kg
- 1 m/s = 3.6 km/h
- 1 nodo = 1.852 km/h

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🔄📏**
