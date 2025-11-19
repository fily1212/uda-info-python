# Es8: Grafici di Funzioni Base

**Livello:** FACILE
**Durata stimata:** 2-3 ore

## Descrizione

Programma per graficare e studiare funzioni matematiche elementari: lineari, quadratiche, cubiche, esponenziali, logaritmiche, trigonometriche.

## Obiettivi

### Competenze Matematica
- Comprendere forme e caratteristiche delle funzioni base
- Identificare dominio, codominio, intersezioni
- Studiare crescenza, decrescenza, massimi, minimi
- Trasformazioni di funzioni (traslazioni, dilatazioni)

### Competenze Informatica
- Numpy per array e valutazioni
- Matplotlib per grafici
- Funzioni lambda
- Gestione assi e range

## Consegna

Il programma deve graficare:

### 1. Funzioni Lineari
- y = mx + q
- Parametri: m (coefficiente angolare), q (intercetta)
- Esempi: y = 2x + 1, y = -x + 3

### 2. Funzioni Quadratiche
- y = ax² + bx + c
- Parabola con vertice e intersezioni
- Esempi: y = x², y = -x² + 4

### 3. Funzioni Cubiche
- y = ax³ + bx² + cx + d
- Esempi: y = x³, y = x³ - 3x

### 4. Funzioni Esponenziali
- y = a^x
- Esempi: y = 2^x, y = e^x, y = 0.5^x

### 5. Funzioni Logaritmiche
- y = log(x), y = ln(x)
- Dominio: x > 0

### 6. Funzioni Trigonometriche
- y = sin(x), y = cos(x), y = tan(x)
- Mostrare periodicità

### 7. Funzioni Composte (opzionale)
- Combinazioni: y = sin(x²), y = e^(-x²)

## Esempio di Utilizzo

```
=== VISUALIZZATORE FUNZIONI ===

Scegli la funzione da graficare:
1. Lineare (y = mx + q)
2. Quadratica (y = ax² + bx + c)
3. Cubica (y = x³)
4. Esponenziale (y = a^x)
5. Logaritmica (y = log(x))
6. Trigonometriche (sin, cos, tan)
7. Confronta più funzioni

Scelta: 2

Inserisci a: 1
Inserisci b: 0
Inserisci c: -4

Funzione: y = x² - 4

Caratteristiche:
- Vertice: (0, -4)
- Asse di simmetria: x = 0
- Intersezioni x: x = -2, x = 2
- Intersezione y: y = -4
- Concavità: verso l'alto (a > 0)

[Mostra grafico]
```

## Suggerimenti di Codice

```python
import numpy as np
import matplotlib.pyplot as plt

def grafica_funzione(f, x_min=-10, x_max=10, label='f(x)'):
    """
    Grafica una funzione f nel range [x_min, x_max]

    Args:
        f: funzione Python (es. lambda x: x**2)
        x_min, x_max: range dell'asse x
        label: etichetta per legenda
    """
    x = np.linspace(x_min, x_max, 1000)
    y = f(x)

    plt.plot(x, y, label=label)
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(f'Grafico di {label}')
    plt.show()

# Esempi
grafica_funzione(lambda x: x**2, -5, 5, 'y = x²')
grafica_funzione(lambda x: np.sin(x), -2*np.pi, 2*np.pi, 'y = sin(x)')
```

### Funzione Quadratica Completa
```python
def quadratica(a, b, c):
    """Studia e grafica y = ax² + bx + c"""
    # Vertice
    x_v = -b / (2 * a)
    y_v = a * x_v**2 + b * x_v + c

    # Delta e intersezioni x
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b + np.sqrt(delta)) / (2*a)
        x2 = (-b - np.sqrt(delta)) / (2*a)

    # Grafico
    x = np.linspace(x_v - 5, x_v + 5, 1000)
    y = a * x**2 + b * x + c

    plt.plot(x, y)
    plt.plot(x_v, y_v, 'ro', label=f'Vertice ({x_v:.2f}, {y_v:.2f})')
    plt.axhline(0, color='k', linewidth=0.5)
    plt.axvline(0, color='k', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()
```

### Confrontare Più Funzioni
```python
x = np.linspace(-5, 5, 1000)

plt.plot(x, x, label='y = x')
plt.plot(x, x**2, label='y = x²')
plt.plot(x, x**3, label='y = x³')
plt.plot(x, 2**x, label='y = 2^x')

plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Confronto Funzioni')
plt.ylim(-10, 10)
plt.show()
```

## Funzioni da Implementare

### Lineari
- y = x
- y = 2x + 3
- y = -0.5x + 1

### Quadratiche
- y = x²
- y = -x² + 4
- y = 2x² - 4x + 1

### Esponenziali
- y = 2^x
- y = e^x
- y = (1/2)^x

### Logaritmiche
- y = log₁₀(x)
- y = ln(x)
- y = log₂(x)

### Trigonometriche
- y = sin(x)
- y = cos(x)
- y = tan(x) [attenzione alle asintote!]

## Estensioni

- Calcolare derivate numericamente
- Trovare zeri con metodi numerici
- Calcolare integrali definiti
- Animare trasformazioni (traslazioni, dilatazioni)
- Funzioni a tratti
- Funzioni parametriche

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 📉📈**
