# Es6: Statistica Descrittiva

**Livello:** BASE
**Durata stimata:** 3-4 ore

## Descrizione

Programma per calcolare e visualizzare le principali misure statistiche descrittive: media, mediana, moda, varianza, deviazione standard, con grafici (istogrammi, boxplot).

## Obiettivi

### Competenze Matematica
- Misure di tendenza centrale (media, mediana, moda)
- Misure di dispersione (range, varianza, deviazione standard)
- Quartili e percentili
- Interpretazione di boxplot e istogrammi

### Competenze Informatica
- Liste e operazioni su dataset
- Ordinamento e ricerca
- Librerie: `statistics` o `numpy`
- Matplotlib per visualizzazioni

## Consegna

Il programma deve:

### 1. Inserimento Dati
- Permettere inserimento manuale di una lista di numeri
- Oppure leggere da file CSV
- Oppure generare dati casuali per test

### 2. Calcolare Statistiche

**Tendenza Centrale:**
- **Media aritmetica**: somma / n
- **Mediana**: valore centrale ordinato
- **Moda**: valore più frequente

**Dispersione:**
- **Range**: max - min
- **Varianza**: media degli scarti quadratici
- **Deviazione standard**: radice quadrata della varianza
- **Coefficiente di variazione**: (dev.std / media) × 100

**Posizione:**
- **Quartili**: Q1 (25%), Q2 (50%), Q3 (75%)
- **Range interquartile (IQR)**: Q3 - Q1

### 3. Visualizzazioni
- **Istogramma**: distribuzione dei valori
- **Boxplot**: quartili e outlier
- **Grafico lineare**: andamento valori (se ha senso)

## Esempio di Utilizzo

```
=== STATISTICA DESCRITTIVA ===

Inserisci i dati (separati da spazio):
12 15 18 20 22 22 25 28 30 35

Analisi dei dati:
Numero di valori: 10

TENDENZA CENTRALE:
Media: 22.7
Mediana: 22.0
Moda: 22

DISPERSIONE:
Range: 23 (min: 12, max: 35)
Varianza: 46.01
Deviazione standard: 6.78
Coefficiente di variazione: 29.87%

QUARTILI:
Q1 (25%): 17.25
Q2 (50%): 22.0 (mediana)
Q3 (75%): 27.25
IQR: 10.0

[Mostra istogramma e boxplot]
```

## Suggerimenti di Codice

### Usando il modulo `statistics`
```python
import statistics

dati = [12, 15, 18, 20, 22, 22, 25, 28, 30, 35]

media = statistics.mean(dati)
mediana = statistics.median(dati)
try:
    moda = statistics.mode(dati)
except:
    moda = "Nessuna moda unica"

varianza = statistics.variance(dati)
dev_std = statistics.stdev(dati)
```

### Quartili Manualmente
```python
def calcola_quartili(dati):
    dati_ordinati = sorted(dati)
    n = len(dati_ordinati)

    q2 = statistics.median(dati_ordinati)  # Mediana
    q1 = statistics.median(dati_ordinati[:n//2])
    q3 = statistics.median(dati_ordinati[(n+1)//2:])

    return q1, q2, q3
```

### Visualizzazione
```python
import matplotlib.pyplot as plt

# Istogramma
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(dati, bins=10, edgecolor='black')
plt.xlabel('Valore')
plt.ylabel('Frequenza')
plt.title('Istogramma')

# Boxplot
plt.subplot(1, 2, 2)
plt.boxplot(dati)
plt.ylabel('Valore')
plt.title('Boxplot')

plt.tight_layout()
plt.show()
```

## Formule

```
Media: μ = (Σ xi) / n

Mediana: valore centrale se n dispari,
         media dei due centrali se n pari

Varianza: σ² = Σ(xi - μ)² / n

Deviazione Standard: σ = √(varianza)

Coefficiente di Variazione: CV = (σ / μ) × 100
```

## Dataset di Esempio

**Voti studenti:** 18, 20, 22, 24, 25, 26, 27, 28, 28, 30

**Temperature (°C):** 15, 17, 18, 20, 22, 23, 25, 26, 28, 30

**Stipendi (k€):** 25, 28, 30, 32, 35, 38, 40, 45, 50, 80

## Estensioni

- Leggere dati da file CSV
- Confrontare più dataset
- Calcolare asimmetria (skewness) e curtosi
- Identificare outlier con metodo IQR
- Normalizzazione dei dati (z-score)

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 📈📊**
