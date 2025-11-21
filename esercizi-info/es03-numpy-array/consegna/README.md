# Es3: NumPy - Lavorare con Array Multidimensionali

## 📊 Informazioni Generali

**Livello:** 🟢 FACILE
**Durata stimata:** 3-4 ore
**Prerequisiti:** Es1-Es2 completati, liste, operazioni matematiche, cicli

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Utilizzare** la classe `ndarray` di NumPy per array efficienti
- ✅ **Creare** array con diversi metodi: `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
- ✅ **Operazioni vettoriali** (operazioni su interi array senza cicli)
- ✅ **Slicing e indexing** per accedere a elementi e sottoinsiemi
- ✅ **Metodi di manipolazione**: `reshape()`, `transpose()`, `flatten()`
- ✅ **Operazioni statistiche**: media, max, min, std (deviazione standard)
- ✅ **Velocità e efficienza** dei NumPy array vs liste Python

**Concetti fondamentali:**
- Classe `ndarray` di NumPy
- Vettorizzazione vs cicli Python
- Broadcasting (operazioni su array di forme diverse)
- Slicing multidimensionale
- Metodi di aggregazione

---

## 📖 Descrizione

NumPy è il fondamento della scienza dei dati in Python. Prima di usare librerie più avanzate (pandas, scikit-learn), devi capire **come funzionano gli array NumPy**.

**Perché NumPy?**

1. **Velocità** - Gli array NumPy sono 100x-1000x più veloci di liste Python
2. **Comodità** - Operazioni matematiche su interi array senza cicli
3. **Memoria** - Consumono molta meno memoria di liste Python
4. **Fondamentale** - Tutte le librerie scientifiche Python usano NumPy

**Confronto: Liste Python vs NumPy Array**

```python
# ❌ Python puro - LENTO
lista = [1, 2, 3, 4, 5]
risultato = [x ** 2 for x in lista]

# ✅ NumPy - VELOCE (e più leggibile)
import numpy as np
array = np.array([1, 2, 3, 4, 5])
risultato = array ** 2  # Vettorizzazione!
```

NumPy fa in una riga quello che Python puro farebbe con un ciclo. Inoltre, l'operazione è **molto più veloce**!

---

## 📝 Consegna Dettagliata

### Parte 1: Creare Array

**Crea un programma che:**

1. **Crea array con diversi metodi**
   - `np.array()`: da lista Python
   - `np.zeros()`: array di zeri
   - `np.ones()`: array di uni
   - `np.arange()`: sequenza di numeri (come range())
   - `np.linspace()`: N numeri distribuiti uniformemente
   - `np.random.rand()`: numeri casuali tra 0 e 1
   - `np.random.randint()`: numeri interi casuali

2. **Crea array multidimensionali (matrici)**
   - Array 1D: `np.array([1, 2, 3])`
   - Array 2D: `np.array([[1, 2], [3, 4]])`
   - Array 3D: per esperimento (difficile visualizzare)
   - Verifica forma con `.shape`
   - Conta elementi con `.size`

3. **Verifica proprietà degli array**
   - Tipo di dati: `.dtype`
   - Numero di dimensioni: `.ndim`
   - Dimensioni: `.shape`
   - Numero totale elementi: `.size`

### Parte 2: Operazioni Vettoriali (Vettorizzazione)

**Crea un programma che:**

1. **Operazioni matematiche elemento-per-elemento**
   - Somma, sottrazione, moltiplicazione, divisione
   - Potenze: `array ** 2`
   - Radice quadrata: `np.sqrt(array)`
   - Funzioni trigonometriche: `np.sin()`, `np.cos()`
   - Logaritmo: `np.log()`

2. **Broadcasting (magia di NumPy)**
   - Somma array con scalare: `array + 5`
   - Somma array 1D a array 2D: `matrix + array`
   - Moltiplicazione di matrici: `np.dot()` o `@`

3. **Confronto elemento-per-elemento**
   - Quali elementi sono > 10?
   - Crea array booleano con `array > 10`
   - Filtra elementi: `array[array > 10]`

### Parte 3: Slicing e Indexing

**Crea un programma che:**

1. **Indexing semplice**
   - Accedi a singoli elementi: `array[0]`, `matrix[0, 1]`
   - Accedi agli ultimi elementi: `array[-1]`
   - Accedi in ordine inverso: `array[::-1]`

2. **Slicing (sottoinsiemi)**
   - Primi N elementi: `array[:5]`
   - Elementi da indice a indice: `array[2:7]`
   - Ogni N-esimo elemento: `array[::2]`
   - Slicing 2D: `matrix[0:2, 1:3]`

3. **Fancy Indexing**
   - Accedi a elementi specifici: `array[[0, 2, 4]]`
   - Usa array booleano: `array[array > 5]`
   - Filtraggio condizionale

### Parte 4: Manipolazione Array

**Crea un programma che:**

1. **Reshape (cambia forma)**
   - Converti 1D array 12 elementi in array 3x4
   - Converti 3x4 in 4x3
   - Converti in 1D con `flatten()`
   - Copia con `copy()` vs vista con slicing

2. **Transpose (trasponi)**
   - Trasponi una matrice 2x3 in 3x2
   - Usa `.T` o `np.transpose()`
   - Verifica che elemento [0,1] diventa [1,0]

3. **Concatenazione e Stack**
   - Unisci array orizzontalmente: `np.hstack()`
   - Unisci array verticalmente: `np.vstack()`
   - Unisci array su nuovo asse: `np.stack()`

### Parte 5: Operazioni Statistiche

**Crea un programma che:**

1. **Aggregazioni semplici**
   - Media: `.mean()`
   - Somma: `.sum()`
   - Massimo: `.max()`
   - Minimo: `.min()`

2. **Statistiche avanzate**
   - Deviazione standard: `.std()`
   - Varianza: `.var()`
   - Mediana: `np.median()`
   - Quartili: `np.percentile()`

3. **Operazioni su assi (per righe/colonne)**
   - Media per riga: `.mean(axis=1)`
   - Media per colonna: `.mean(axis=0)`
   - Somma per colonna: `.sum(axis=0)`

### Parte 6: Esercizio Pratico Completo

**Analisi di dati voti/temperature/vendite:**

1. **Carica i dati**
   - 30 voti di studenti (valori 0-100)
   - Calcola: media, mediana, min, max, std
   - Conta quanti hanno voto >= 70

2. **Temperature settimanali**
   - 7 giorni, 3 misurazioni per giorno
   - Array 7x3 (giorni x misurazioni)
   - Calcola media per giorno
   - Calcola media complessiva
   - Trova giorno più caldo/freddo

3. **Vendite per negozio**
   - 5 negozi, 12 mesi di vendite (array 5x12)
   - Calcola vendite totali per negozio
   - Calcola vendite medie per mese
   - Trova negozio migliore/peggiore

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ PARTE 1: CREARE ARRAY ============

import numpy as np

# Creare array da lista Python
arr1 = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr1}")
print(f"Tipo: {type(arr1)}")  # <class 'numpy.ndarray'>

# Creare array di zeri e uni
zeros = np.zeros(5)
print(f"Zeri: {zeros}")  # [0. 0. 0. 0. 0.]

ones = np.ones((3, 4))  # Matrice 3x4 di uni
print(f"Uni (forma {ones.shape}): \n{ones}")

# Sequenze di numeri
arange_arr = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8
print(f"Arange (0-10, step 2): {arange_arr}")

linspace_arr = np.linspace(0, 10, 5)  # 5 numeri da 0 a 10
print(f"Linspace (5 numeri 0-10): {linspace_arr}")

# Array casuali
random_arr = np.random.rand(5)  # 5 numeri casuali [0, 1)
print(f"Casuali: {random_arr}")

random_int = np.random.randint(1, 100, 10)  # 10 interi [1, 100)
print(f"Interi casuali: {random_int}")

# ============ PARTE 2: PROPRIETÀ ARRAY ============

matrice = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nMatrice:\n{matrice}")
print(f"Forma (shape): {matrice.shape}")  # (2, 3)
print(f"Numero dimensioni: {matrice.ndim}")  # 2
print(f"Numero totale elementi: {matrice.size}")  # 6
print(f"Tipo di dati: {matrice.dtype}")  # int64

# ============ PARTE 3: OPERAZIONI VETTORIALI ============

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Operazioni elemento-per-elemento
print(f"\nOperazioni Vettoriali:")
print(f"{a} + {b} = {a + b}")  # [11 22 33 44 55]
print(f"{a} * 2 = {a * 2}")  # [2 4 6 8 10]
print(f"{a} ** 2 = {a ** 2}")  # [1 4 9 16 25]

# Funzioni matematiche
print(f"sqrt({a}) = {np.sqrt(a.astype(float))}")
print(f"sin({a}) = {np.sin(a)}")

# Confronti
print(f"{a} > 2 = {a > 2}")  # [False False True True True]
filtered = a[a > 2]  # Filtra elementi > 2
print(f"Elementi > 2: {filtered}")  # [3 4 5]

# ============ PARTE 4: SLICING E INDEXING ============

arr = np.arange(0, 20, 2)  # [0, 2, 4, 6, ..., 18]
print(f"\nArray: {arr}")

print(f"Primo elemento: {arr[0]}")  # 0
print(f"Ultimo elemento: {arr[-1]}")  # 18
print(f"Primi 5: {arr[:5]}")  # [0 2 4 6 8]
print(f"Da indice 2 a 7: {arr[2:7]}")  # [4 6 8 10 12]
print(f"Ogni 2 elementi: {arr[::2]}")  # [0 4 8 12 16]
print(f"Inverso: {arr[::-1]}")  # [18 16 14 ... 2 0]

# Indexing 2D
matrix2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatrice 2D:\n{matrix2d}")
print(f"Elemento [0, 1]: {matrix2d[0, 1]}")  # 2
print(f"Prima riga: {matrix2d[0]}")  # [1 2 3]
print(f"Seconda colonna: {matrix2d[:, 1]}")  # [2 5 8]
print(f"Sottomatrice [0:2, 1:3]:\n{matrix2d[0:2, 1:3]}")

# ============ PARTE 5: RESHAPE E TRANSPOSE ============

# Reshape
arr_flat = np.arange(12)  # [0, 1, 2, ..., 11]
arr_2d = arr_flat.reshape(3, 4)
print(f"\nArray 1D (12 elementi):\n{arr_flat}")
print(f"Array 2D (3x4):\n{arr_2d}")

arr_3d = arr_flat.reshape(2, 2, 3)
print(f"Array 3D (2x2x3):\n{arr_3d}")

# Flatten
unraveled = arr_3d.flatten()
print(f"Flattened: {unraveled}")

# Transpose
print(f"\nMatrice originale (3x4):\n{arr_2d}")
print(f"Trasposata (4x3):\n{arr_2d.T}")

# ============ PARTE 6: STATISTICHE ============

voti = np.array([65, 72, 85, 88, 92, 78, 95, 87, 73, 81,
                 79, 86, 77, 91, 84, 80, 88, 75, 93, 82,
                 76, 89, 85, 74, 90, 83, 87, 79, 88, 86])

print(f"\n=== ANALISI VOTI ({len(voti)} studenti) ===")
print(f"Media: {voti.mean():.2f}")
print(f"Mediana: {np.median(voti):.2f}")
print(f"Minimo: {voti.min()}")
print(f"Massimo: {voti.max()}")
print(f"Deviazione Standard: {voti.std():.2f}")
print(f"Varianza: {voti.var():.2f}")

# Conteggi
passed = (voti >= 70).sum()
failed = (voti < 70).sum()
print(f"Promossi (>= 70): {passed}")
print(f"Bocciati (< 70): {failed}")

# Percentili
p25 = np.percentile(voti, 25)
p75 = np.percentile(voti, 75)
print(f"25° percentile (Q1): {p25}")
print(f"75° percentile (Q3): {p75}")

# ============ PARTE 7: OPERAZIONI MULTI-DIMENSIONALI ============

# Dati temperatura: 7 giorni, 3 misurazioni per giorno
temperature = np.array([
    [15, 16, 14],  # Lunedi
    [16, 17, 15],  # Martedi
    [18, 19, 17],  # Mercoledi
    [20, 21, 19],  # Giovedi
    [22, 23, 21],  # Venerdi
    [21, 22, 20],  # Sabato
    [19, 20, 18],  # Domenica
])

print(f"\n=== ANALISI TEMPERATURE ===")
print(f"Forma: {temperature.shape}")  # (7, 3)

# Media per giorno (lungo colonne)
giorni = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']
media_per_giorno = temperature.mean(axis=1)
print(f"\nMedia temperatura per giorno:")
for giorno, media in zip(giorni, media_per_giorno):
    print(f"  {giorno}: {media:.1f}°C")

# Media per misura (lungo righe)
media_per_misura = temperature.mean(axis=0)
print(f"\nMedia per misura (mattina, pomeriggio, sera):")
print(f"  {media_per_misura}")

# Media complessiva
media_totale = temperature.mean()
print(f"Media complessiva: {media_totale:.1f}°C")

# Min/Max per giorno
print(f"\nGiorno più caldo (media): {giorni[media_per_giorno.argmax()]} ({media_per_giorno.max():.1f}°C)")
print(f"Giorno più freddo (media): {giorni[media_per_giorno.argmin()]} ({media_per_giorno.min():.1f}°C)")

# ============ PARTE 8: CONCATENAZIONE ============

arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

# Concatena orizzontalmente
print(f"\n=== CONCATENAZIONE ===")
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"hstack (fianco): {np.hstack([arr_a, arr_b])}")

# Concatena verticalmente
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
print(f"\nvstack (sopra-sotto):\n{np.vstack([mat_a, mat_b])}")
```

---

## 🔍 Casi di Prova (Test)

```python
# Test 1: Creazione array
def test_creazione():
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    assert len(arr) == 5
    assert arr[0] == 1
    assert arr[-1] == 5
    print("✓ Test 1 passato: Creazione array")

# Test 2: Operazioni vettoriali
def test_operazioni():
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    risultato = a + b
    assert np.array_equal(risultato, np.array([5, 7, 9]))
    print("✓ Test 2 passato: Operazioni vettoriali")

# Test 3: Slicing
def test_slicing():
    import numpy as np
    arr = np.arange(10)
    assert np.array_equal(arr[2:5], np.array([2, 3, 4]))
    assert np.array_equal(arr[::2], np.array([0, 2, 4, 6, 8]))
    print("✓ Test 3 passato: Slicing")

# Test 4: Shape e Reshape
def test_reshape():
    import numpy as np
    arr = np.arange(12)
    reshaped = arr.reshape(3, 4)
    assert reshaped.shape == (3, 4)
    assert reshaped[0, 0] == 0
    assert reshaped[2, 3] == 11
    print("✓ Test 4 passato: Reshape")

# Test 5: Transpose
def test_transpose():
    import numpy as np
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    transposed = mat.T
    assert transposed.shape == (3, 2)
    assert transposed[0, 1] == 4
    print("✓ Test 5 passato: Transpose")

# Test 6: Statistiche
def test_statistiche():
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    assert arr.mean() == 3
    assert arr.sum() == 15
    assert arr.min() == 1
    assert arr.max() == 5
    print("✓ Test 6 passato: Statistiche")

# Test 7: Filtraggio
def test_filtraggio():
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    filtered = arr[arr > 5]
    assert np.array_equal(filtered, np.array([6, 7, 8, 9, 10]))
    print("✓ Test 7 passato: Filtraggio")

# Test 8: Broadcasting
def test_broadcasting():
    import numpy as np
    a = np.array([1, 2, 3])
    risultato = a + 10
    assert np.array_equal(risultato, np.array([11, 12, 13]))
    print("✓ Test 8 passato: Broadcasting")

# Test 9: Concatenazione
def test_concatenazione():
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = np.hstack([a, b])
    assert len(result) == 6
    assert result[3] == 4
    print("✓ Test 9 passato: Concatenazione")

# Test 10: Operazioni 2D
def test_2d():
    import numpy as np
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    assert mat.shape == (2, 3)
    assert mat[0, 1] == 2
    assert np.array_equal(mat[1], np.array([4, 5, 6]))
    print("✓ Test 10 passato: Operazioni 2D")

if __name__ == "__main__":
    test_creazione()
    test_operazioni()
    test_slicing()
    test_reshape()
    test_transpose()
    test_statistiche()
    test_filtraggio()
    test_broadcasting()
    test_concatenazione()
    test_2d()
    print("\n✅ Tutti i test passati!")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Installa NumPy
```bash
pip install numpy
```

### Passo 2: Impara a creare array
```python
import numpy as np
arr = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
zeros = np.zeros((3, 3))
```

### Passo 3: Sperimenta operazioni vettoriali
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)   # [5 7 9]
print(a * 2)   # [2 4 6]
print(a ** 2)  # [1 4 9]
```

### Passo 4: Impara slicing e indexing
```python
arr = np.arange(10)
print(arr[0])      # 0
print(arr[2:5])    # [2 3 4]
print(arr[::2])    # [0 2 4 6 8]
```

### Passo 5: Esplora reshape e transpose
```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)
print(matrix.shape)
print(matrix.T)
```

### Passo 6: Calcola statistiche
```python
dati = np.array([1, 2, 3, 4, 5])
print(dati.mean())
print(dati.std())
print(dati.max())
```

### Passo 7: Risolvi problemi pratici
```python
# Analizza dati reali con le competenze acquisite
```

---

## 💡 Trucchi e Best Practices

### ✅ Trucco 1: Scopri i metodi di un array
```python
import numpy as np
arr = np.array([1, 2, 3])
print(dir(arr))  # Tutti i metodi disponibili
help(arr.mean)   # Aiuto su metodo specifico
```

### ✅ Trucco 2: Usa astype() per cambiare tipo
```python
arr = np.array([1, 2, 3])
arr_float = arr.astype(float)
arr_str = arr.astype(str)
```

### ✅ Trucco 3: Usa `.copy()` vs `.view()`
```python
arr = np.array([1, 2, 3])
copia = arr.copy()  # Copia vera
vista = arr[:]      # Vista (modifiche condivise)
```

### ✅ Trucco 4: Broadcasting automatico
```python
a = np.array([1, 2, 3])      # Shape (3,)
b = np.array([[1], [2], [3]]) # Shape (3, 1)
risultato = a + b            # Shape (3, 3) - broadcasting!
```

### ✅ Trucco 5: Usa np.where() per condizioni
```python
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 2, arr, 0)  # Sostituisci
# [0, 0, 3, 4, 5]
```

### ✅ Trucco 6: Usa `argmax()` e `argmin()`
```python
arr = np.array([3, 1, 4, 1, 5, 9])
print(arr.argmax())  # Indice del max (5)
print(arr.argmin())  # Indice del min (1)
```

### ✅ Trucco 7: Usa `unique()` per elementi unici
```python
arr = np.array([1, 2, 2, 3, 3, 3])
print(np.unique(arr))  # [1, 2, 3]
unique, counts = np.unique(arr, return_counts=True)
# counts = [1, 2, 3]
```

### ✅ Trucco 8: Operazioni con NaN
```python
arr = np.array([1, 2, np.nan, 4])
print(np.nanmean(arr))  # Media ignorando NaN
print(np.nansum(arr))   # Somma ignorando NaN
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Confondere shape di array diversi
```python
# SBAGLIATO
a = np.array([1, 2, 3])  # Shape (3,)
b = np.array([[1, 2, 3]])  # Shape (1, 3)
print(a + b)  # Broadcasting non intuitivo

# GIUSTO - sii consapevole delle forme
print(f"Shape di a: {a.shape}")
print(f"Shape di b: {b.shape}")
```

### ❌ Errore 2: Modificare array "per sbaglio"
```python
# SBAGLIATO - fai vista, non copia
original = np.array([1, 2, 3])
subset = original[:]
subset[0] = 999
print(original)  # [999, 2, 3] - modificato!

# GIUSTO - usa copy() se vuoi indipendenza
subset = original.copy()
subset[0] = 999
print(original)  # [1, 2, 3] - intatto
```

### ❌ Errore 3: Confondere axis 0 e axis 1
```python
# SBAGLIATO - quale asse?
matrix = np.array([[1, 2, 3], [4, 5, 6]])
media = matrix.mean()  # Media totale

# GIUSTO - specifica asse
media_righe = matrix.mean(axis=1)  # Per riga
media_colonne = matrix.mean(axis=0)  # Per colonna
```

### ❌ Errore 4: Non gestire operazioni tra forme diverse
```python
# SBAGLIATO
a = np.array([[1, 2], [3, 4]])  # 2x2
b = np.array([1, 2, 3])  # 3 elementi
print(a + b)  # ValueError!

# GIUSTO - verifica forme prima
print(a.shape, b.shape)
```

### ❌ Errore 5: Usare loop Python quando hai vettorizzazione
```python
# SBAGLIATO - LENTO
arr = np.arange(1000000)
for i in range(len(arr)):
    arr[i] = arr[i] ** 2

# GIUSTO - VELOCE
arr = arr ** 2
```

### ❌ Errore 6: Dimenticare parentesi per shape con tuple
```python
# SBAGLIATO
zeros = np.zeros(3, 4)  # Errore!

# GIUSTO
zeros = np.zeros((3, 4))  # Tupla (3, 4)
```

### ❌ Errore 7: Dividere per zero
```python
# SBAGLIATO - avviso (divide by zero)
arr = np.array([1, 2, 3])
result = arr / 0  # Produce inf/nan

# GIUSTO - gestisci
with np.errstate(divide='ignore', invalid='ignore'):
    result = arr / 0
```

### ❌ Errore 8: Non capire flatten() vs ravel()
```python
# SBAGLIATO - confusion
arr = np.arange(6).reshape(2, 3)
flat1 = arr.flatten()  # Copia
flat2 = arr.ravel()    # Vista
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Matrice di Correlazione
- Carica dati 2D (es. altezza, peso, età)
- Calcola correlazione tra variabili
- Visualizza come heatmap

### 🌟 Sfida 2: Algebra Lineare
- Moltiplicazione matriciale con `np.dot()`
- Calcolo determinante con `np.linalg.det()`
- Inversa matrice con `np.linalg.inv()`
- Autovalori/autovettori con `np.linalg.eig()`

### 🌟 Sfida 3: Decomposizione SVD
- Usa SVD (Singular Value Decomposition)
- Comprimi immagini usando SVD
- Ricostruisci approssimativamente

### 🌟 Sfida 4: Problemi Statistici Avanzati
- Calcola distribuzione gaussiana
- Monte Carlo simulation
- Bootstrap per intervalli di confidenza

### 🌟 Sfida 5: Performance Benchmark
- Confronta velocità: loop Python vs NumPy
- Uso memoria: liste vs array
- Profila codice con `timeit` o `cProfile`

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **ndarray** | Classe NumPy per array multidimensionali | `np.array([1, 2, 3])` |
| **shape** | Forma (dimensioni) dell'array | `.shape` → (3, 4) |
| **dtype** | Tipo di dati elemento | `.dtype` → int64, float64 |
| **Vettorizzazione** | Operazioni su interi array senza cicli | `arr ** 2` |
| **Broadcasting** | Operazioni su array di forme diverse | `arr + 5` |
| **Slicing** | Estrai parti di array | `arr[1:4]` |
| **Reshape** | Cambia forma senza perdere dati | `.reshape(3, 4)` |
| **Transpose** | Scambia righe e colonne | `.T` |
| **Axis** | Dimensione lungo cui operare | `axis=0` (righe), `axis=1` (colonne) |
| **Aggregazione** | Operazioni su gruppi di elementi | `.sum()`, `.mean()`, `.max()` |

---

## 🔗 Link Utili

### Documentazione Ufficiale
- [NumPy Official Documentation](https://numpy.org/doc/stable/)
- [NumPy API Reference](https://numpy.org/doc/stable/reference/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)

### Tutorial Interattivi
- [Real Python - NumPy](https://realpython.com/numpy-tutorial/)
- [DataCamp - NumPy Tutorial](https://www.datacamp.com/courses/introduction-to-numpy)
- [W3Schools - NumPy](https://www.w3schools.com/python/numpy/default.asp)

### Cheat Sheet
- [NumPy Cheat Sheet (DataCamp)](https://assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
- [NumPy Quick Reference](https://numpy.org/doc/stable/user/basics.html)

### Visualizzazione
- [NumPy Broadcasting Rules](https://numpy.org/doc/stable/user/basics.broadcasting.html)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Leggi il tuo codice prima di guardare la soluzione
- Nota le differenze di stile e approccio
- Apprendi dalle scelte implementative
- Non copiare direttamente - usa come riferimento!

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] So creare array con diversi metodi (np.array, np.zeros, np.arange, ecc.)
- [ ] Capisco la forma (shape) e le dimensioni degli array
- [ ] Riesco a fare operazioni vettoriali senza cicli
- [ ] Capisco slicing e indexing (1D e 2D)
- [ ] So reshape, transpose, flatten
- [ ] Riesco a calcolare statistiche (media, max, min, std)
- [ ] Capisco il concetto di axis (0 = righe, 1 = colonne)
- [ ] So filtrare array con condizioni booleane
- [ ] Ho testato il codice con i casi di prova forniti
- [ ] Ho provato le sfide bonus
- [ ] Capisco che NumPy è fondamentale per data science

---

**Buon lavoro! 🚀 NumPy è il superpotere di Python per scienza dei dati!**

*"NumPy non è solo più veloce di Python - è ordini di grandezza più efficiente."*
