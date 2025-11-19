# Es4: Simulatore di Dadi

**Livello:** FACILE
**Durata stimata:** 2-3 ore

## Descrizione

Simula il lancio di dadi e confronta i risultati empirici con la teoria della probabilità, visualizzando le distribuzioni con grafici.

## Obiettivi

### Competenze Matematica
- Probabilità uniforme discreta
- Distribuzione di frequenze
- Confronto teoria vs pratica
- Legge dei grandi numeri

### Competenze Informatica
- Modulo `random` per numeri casuali
- Liste e dizionari per conteggi
- Matplotlib per grafici
- Cicli e statistiche

## Consegna

Il programma deve:

1. **Lancio Singolo/Multiplo**
   - Simulare lancio di 1 o più dadi a 6 facce
   - Mostrare risultati individuali e somma

2. **Distribuzione Frequenze**
   - Lanciare N volte (es. 1000, 10000)
   - Contare quante volte esce ogni faccia
   - Calcolare frequenze relative

3. **Confronto con Teoria**
   - Probabilità teorica: 1/6 per ogni faccia
   - Confrontare frequenze empiriche vs teoriche
   - Mostrare differenze percentuali

4. **Visualizzazione**
   - Grafico a barre delle frequenze
   - Linea orizzontale per probabilità teorica (1/6 = 16.67%)

## Esempio di Utilizzo

```
=== SIMULATORE DADI ===

Quanti dadi vuoi lanciare? 2
Quante volte? 10000

Simulazione in corso...

Risultati per somma dei due dadi:
Somma 2: 281 volte (2.81%) - teorico: 2.78%
Somma 3: 548 volte (5.48%) - teorico: 5.56%
Somma 4: 828 volte (8.28%) - teorico: 8.33%
...
Somma 7: 1667 volte (16.67%) - teorico: 16.67%
...
Somma 12: 276 volte (2.76%) - teorico: 2.78%

[Mostra grafico con matplotlib]
```

## Suggerimenti

### Lancio Dadi
```python
import random

def lancia_dado():
    return random.randint(1, 6)

def lancia_n_dadi(n):
    return [lancia_dado() for _ in range(n)]
```

### Conteggio Frequenze
```python
def simula_lanci(num_lanci, num_dadi=1):
    risultati = {}
    for _ in range(num_lanci):
        lancio = sum(lancia_n_dadi(num_dadi))
        risultati[lancio] = risultati.get(lancio, 0) + 1
    return risultati
```

### Grafico
```python
import matplotlib.pyplot as plt

plt.bar(risultati.keys(), risultati.values())
plt.axhline(y=num_lanci/6, color='r', linestyle='--', label='Teorico')
plt.xlabel('Faccia del dado')
plt.ylabel('Frequenza')
plt.title('Distribuzione lanci di dadi')
plt.legend()
plt.show()
```

## Probabilità Teoriche

### 1 Dado (6 facce)
- Ogni faccia: 1/6 ≈ 16.67%

### 2 Dadi (somma)
- Somma 2: 1/36 ≈ 2.78%
- Somma 3: 2/36 ≈ 5.56%
- Somma 4: 3/36 ≈ 8.33%
- Somma 7: 6/36 ≈ 16.67% (più probabile!)
- Somma 12: 1/36 ≈ 2.78%

## Estensioni

- Dadi con facce diverse (d4, d8, d12, d20)
- Simulazione giochi (es. Monopoly)
- Calcolare media e deviazione standard
- Confrontare diverse quantità di lanci

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🎲📊**
