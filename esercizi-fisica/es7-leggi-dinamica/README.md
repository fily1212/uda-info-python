# Es7: Leggi della Dinamica

**Livello:** FACILE
**Durata stimata:** 2-3 ore

## Descrizione

Programma che applica le leggi della dinamica di Newton per risolvere problemi pratici di fisica.

## Obiettivi

### Competenze Fisica
- Applicare la seconda legge di Newton (F = ma)
- Calcolare peso, forza normale, attrito
- Risolvere problemi del piano inclinato
- Comprendere le relazioni tra forza, massa e accelerazione

### Competenze Informatica
- Funzioni matematiche in Python
- Modulo math per operazioni trigonometriche
- Validazione e gestione input utente
- Formattazione output

## Consegna

Il programma deve risolvere i seguenti problemi:

1. **Seconda Legge di Newton**
   - Calcolare F = m × a
   - Date 2 grandezze, trovare la terza

2. **Peso e Forza Normale**
   - Calcolare peso: P = m × g
   - Forza normale su piano orizzontale e inclinato

3. **Forza di Attrito**
   - Attrito statico: Fs = μs × N
   - Attrito dinamico: Fd = μd × N

4. **Piano Inclinato**
   - Componenti della forza peso
   - Forza parallela al piano: F∥ = mg sin(θ)
   - Forza perpendicolare: F⊥ = mg cos(θ)
   - Accelerazione su piano inclinato senza attrito

## Esempio di Utilizzo

```
=== CALCOLATORE DINAMICA ===

Scegli il tipo di problema:
1. Seconda legge di Newton (F = ma)
2. Calcolo peso
3. Forza di attrito
4. Piano inclinato

Scelta: 4

Inserisci massa (kg): 10
Inserisci angolo del piano (gradi): 30

Risultati:
Peso: 98.1 N
Componente parallela: 49.05 N
Componente perpendicolare: 84.87 N
Accelerazione: 4.905 m/s²
```

## Suggerimenti

- Usa `math.sin()` e `math.cos()` (ricorda di convertire gradi in radianti!)
- Usa `math.radians()` per convertire gradi in radianti
- g = 9.81 m/s²
- Crea funzioni separate per ogni tipo di calcolo
- Valida che massa e angoli siano positivi

## Formule Utili

```python
import math

# Conversione gradi -> radianti
radianti = math.radians(gradi)

# Peso
P = m * g  # g = 9.81

# Piano inclinato
F_parallela = m * g * math.sin(math.radians(theta))
F_perpendicolare = m * g * math.cos(math.radians(theta))
a = g * math.sin(math.radians(theta))
```

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! ⚙️📐**
