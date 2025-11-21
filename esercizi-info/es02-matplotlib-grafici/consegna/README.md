# Es2: Matplotlib - Creare Grafici con Classi Esistenti

## 📊 Informazioni Generali

**Livello:** 🟢 FACILE
**Durata stimata:** 3-4 ore
**Prerequisiti:** Es1 completato, liste, dizionari, funzioni, numpy base

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Utilizzare** la libreria matplotlib per creare grafici
- ✅ **Creare oggetti** Figure, Axes, Subplot dalle classi matplotlib
- ✅ **Usare metodi** delle classi: `plot()`, `bar()`, `scatter()`, `hist()`, `set_title()`, `set_xlabel()`
- ✅ **Personalizzare** grafici: colori, legende, griglie, stili
- ✅ **Salvare** grafici in file con `savefig()`
- ✅ **Leggere** la documentazione ufficiale di matplotlib
- ✅ **Risolvere problemi reali** visualizzando dati

**Concetti fondamentali:**
- Classi matplotlib: `Figure`, `Axes`, `pyplot`
- Creazione di grafici con oggetti (OOP) vs funzioni imperative
- Attributi e metodi degli oggetti grafico
- Layout e personalizzazione

---

## 📖 Descrizione

Matplotlib è una libreria **orientata agli oggetti** per creare grafici professionali. Prima di imparare a scrivere le tue classi, è fondamentale capire come usare quelle già pronte.

**Perché imparare matplotlib OOP?**

1. **Migliore controllo** - I metodi delle classi ti permettono di personalizzare ogni aspetto
2. **Riusabilità** - Puoi salvare grafici e usarli in programmi più grandi
3. **Fondamenta OOP** - Matplotlib usa classi `Figure`, `Axes`, `Subplot`
4. **Professionale** - I grafici creati sono di qualità da pubblicazione

**Approccio Procedurale (Funzionale):**
```python
# Vecchio modo: usa pyplot direttamente
import matplotlib.pyplot as plt
plt.plot([1,2,3], [1,4,9])
plt.title("Titolo")
plt.show()
```

**Approccio OOP (quello che imparerai):**
```python
# Nuovo modo: crea oggetti e chiama metodi
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3], [1,4,9])
ax.set_title("Titolo")
plt.show()
```

Il secondo approccio è **più potente e flessibile**!

---

## 📝 Consegna Dettagliata

### Parte 1: Grafici Semplici con Figure e Axes

**Crea un programma che:**

1. **Importa le classi corrette**
   - `from matplotlib.figure import Figure`
   - `from matplotlib.axes import Axes`
   - `import matplotlib.pyplot as plt`

2. **Crea un grafico a linee**
   - Usa `fig, ax = plt.subplots()` per creare Figure e Axes
   - Traccia una linea con dati x=[0,1,2,3,4] e y=[0,1,4,9,16] (quadrati)
   - Usa il metodo `ax.plot()` della classe Axes
   - Aggiungi titolo con `ax.set_title("Quadrati")`
   - Aggiungi etichette assi con `ax.set_xlabel()` e `ax.set_ylabel()`
   - Mostra il grafico con `plt.show()`

3. **Personalizza il grafico**
   - Cambia colore della linea: `ax.plot(..., color='red')`
   - Cambia stile linea: `ax.plot(..., linestyle='--')`
   - Aggiungi griglia: `ax.grid(True)`
   - Aggiungi legenda: `ax.legend(['Quadrati'])`

### Parte 2: Grafici a Barre e Scatter

**Crea un programma che:**

1. **Grafico a barre** (vendite per mese)
   - Dati: mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag']
   - Vendite = [100, 150, 120, 180, 200]
   - Usa il metodo `ax.bar()` della classe Axes
   - Personalizza con colori diversi: `ax.bar(..., color='green')`
   - Aggiungi titolo e etichette

2. **Grafico scatter** (relazione peso-altezza)
   - Crea dati casuali o realistici
   - Usa il metodo `ax.scatter()` della classe Axes
   - Personalizza con dimensione punti: `s=100`
   - Usa trasparenza: `alpha=0.6`
   - Aggiungi colori per categorie

### Parte 3: Istogrammi e Subplot

**Crea un programma che:**

1. **Istogramma** (distribuzione voti studenti)
   - Voti = [7.5, 8.0, 6.5, 7.0, 8.5, 6.0, 9.0, 7.5, 8.0, 6.5]
   - Usa il metodo `ax.hist()` della classe Axes
   - Personalizza numero bin: `bins=5`
   - Aggiungi colore e etichette

2. **Multipli grafici** (subplot)
   - Crea 2x2 subfigure: `fig, axes = plt.subplots(2, 2)`
   - Fai un grafico diverso in ogni subplot
   - Usa ogni elemento di `axes` per disegnare
   - Aggiungi titolo diverso a ogni subplot
   - Usa `fig.suptitle()` per titolo generale

### Parte 4: Salvare Grafici in File

**Crea un programma che:**

1. **Salva grafici in formati diversi**
   - Crea un grafico
   - Salva con `fig.savefig('grafico.png')`
   - Salva anche in formato PDF: `fig.savefig('grafico.pdf')`
   - Salva in formato SVG (vettoriale): `fig.savefig('grafico.svg')`

2. **Personalizza il salvataggio**
   - Usa DPI alto per immagini nitide: `dpi=300`
   - Usa bbox_inches='tight' per evitare margini
   - Prova transparent=True per sfondo trasparente

### Parte 5: Esercizio Pratico Completo

**Crea un programma che analizza dati reali:**

1. **Dati di temperatura** giornaliera per una settimana
   - Crea array con temperature: [15, 16, 18, 20, 22, 21, 19]
   - Crea grafico a linee con personalizzazioni
   - Aggiungi una linea orizzontale per la media (usa `ax.axhline()`)
   - Colora aree sopra/sotto media diversamente

2. **Dati di vendite** per trimestre
   - Crea grafico a barre con 3 prodotti
   - Usa sub-barre per mostrare diversi trimestri
   - Aggiungi legenda e griglia

3. **Dati di voti studenti**
   - Crea scatter con nome studente, voto, presenze
   - Usa colore per materia
   - Usa grandezza punto per presenze
   - Aggiungi labels per studenti migliori/peggiori

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ PARTE 1: GRAFICO A LINEE ============

import matplotlib.pyplot as plt
import numpy as np

# Crea dati
x = np.array([0, 1, 2, 3, 4])
y = x ** 2  # Quadrati

# APPROCCIO OOP: Crea oggetti Figure e Axes
fig, ax = plt.subplots(figsize=(8, 6))

# Usa metodo della classe Axes
ax.plot(x, y, color='red', linestyle='-', linewidth=2, label='y = x²')

# Personalizza con metodi
ax.set_title('Grafico Quadrati', fontsize=16, fontweight='bold')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3)  # Griglia leggera
ax.legend()  # Mostra legenda

# Salva il grafico
fig.savefig('quadrati.png', dpi=150, bbox_inches='tight')
plt.show()

# ============ PARTE 2: GRAFICO A BARRE ============

# Dati vendite
mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio']
vendite = [100, 150, 120, 180, 200]

# Crea Figure e Axes
fig, ax = plt.subplots(figsize=(10, 6))

# Usa metodo bar() della classe Axes
colori = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
ax.bar(mesi, vendite, color=colori, alpha=0.8, edgecolor='black')

# Personalizza
ax.set_title('Vendite Mensili', fontsize=16, fontweight='bold')
ax.set_xlabel('Mese', fontsize=12)
ax.set_ylabel('Vendite (€)', fontsize=12)
ax.grid(True, axis='y', alpha=0.3)

# Aggiungi valori sulle barre
for i, v in enumerate(vendite):
    ax.text(i, v + 5, str(v), ha='center', fontweight='bold')

fig.savefig('vendite.png', dpi=150, bbox_inches='tight')
plt.show()

# ============ PARTE 3: SCATTER PLOT ============

# Dati altezza e peso
altezze = [160, 165, 170, 175, 180, 165, 172, 178]
pesi = [55, 60, 65, 70, 75, 58, 68, 76]
genere = [0, 1, 0, 1, 0, 1, 0, 1]  # 0=F, 1=M

fig, ax = plt.subplots(figsize=(8, 6))

# Usa scatter() per punti
colori_genere = ['pink' if g == 0 else 'lightblue' for g in genere]
ax.scatter(altezze, pesi, s=100, c=colori_genere, alpha=0.6, edgecolor='black')

ax.set_title('Relazione Altezza-Peso', fontsize=14, fontweight='bold')
ax.set_xlabel('Altezza (cm)', fontsize=12)
ax.set_ylabel('Peso (kg)', fontsize=12)
ax.grid(True, alpha=0.3)

fig.savefig('scatter.png', dpi=150, bbox_inches='tight')
plt.show()

# ============ PARTE 4: ISTOGRAMMA ============

# Dati voti
voti = [6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 7.0, 6.5, 8.0, 7.5]

fig, ax = plt.subplots(figsize=(8, 6))

# Usa hist() per istogramma
ax.hist(voti, bins=5, color='skyblue', edgecolor='black', alpha=0.7)

ax.set_title('Distribuzione Voti Studenti', fontsize=14, fontweight='bold')
ax.set_xlabel('Voto', fontsize=12)
ax.set_ylabel('Frequenza', fontsize=12)
ax.grid(True, axis='y', alpha=0.3)

fig.savefig('istogramma.png', dpi=150, bbox_inches='tight')
plt.show()

# ============ PARTE 5: SUBPLOT (Multipli Grafici) ============

# Crea figura con 2x2 subfigure
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Dashboard Analisi Dati', fontsize=16, fontweight='bold')

# Subplot 1: Linee
axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3], marker='o', color='red')
axes[0, 0].set_title('Grafico Linee')
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: Barre
axes[0, 1].bar(['A', 'B', 'C'], [10, 20, 15], color='green', alpha=0.7)
axes[0, 1].set_title('Grafico Barre')
axes[0, 1].grid(True, axis='y', alpha=0.3)

# Subplot 3: Scatter
axes[1, 0].scatter([1, 2, 3, 4], [2, 3, 1, 4], s=100, color='blue', alpha=0.6)
axes[1, 0].set_title('Scatter Plot')
axes[1, 0].grid(True, alpha=0.3)

# Subplot 4: Istogramma
axes[1, 1].hist([1, 1, 2, 2, 2, 3, 3, 3, 3], bins=3, color='orange', alpha=0.7)
axes[1, 1].set_title('Istogramma')
axes[1, 1].grid(True, axis='y', alpha=0.3)

# Adatta layout
fig.tight_layout()
fig.savefig('dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

# ============ PARTE 6: ANALISI TEMPERATURA ============

# Dati realistici
giorni = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']
temperature = [15, 16, 18, 20, 22, 21, 19]
temp_media = sum(temperature) / len(temperature)

fig, ax = plt.subplots(figsize=(10, 6))

# Grafico a linee con marker
ax.plot(giorni, temperature, marker='o', linewidth=2, markersize=8,
        color='red', label='Temperatura')

# Linea media
ax.axhline(y=temp_media, color='blue', linestyle='--', linewidth=2,
           label=f'Media: {temp_media:.1f}°C')

# Riempi area sopra media
ax.fill_between(range(len(giorni)), temperature, temp_media,
                where=[t >= temp_media for t in temperature],
                alpha=0.2, color='red', label='Sopra media')

ax.set_title('Temperatura Settimanale', fontsize=14, fontweight='bold')
ax.set_xlabel('Giorno', fontsize=12)
ax.set_ylabel('Temperatura (°C)', fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)

fig.savefig('temperatura.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 🔍 Casi di Prova (Test)

Prova il tuo codice con questi casi:

```python
# Test 1: Grafico a linee semplice
def test_grafico_linee():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    assert ax is not None
    plt.close(fig)
    print("✓ Test 1 passato: Grafico linee creato")

# Test 2: Personalizzazione colori
def test_colori():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3], color='red', label='Test')
    ax.legend()
    assert len(ax.lines) == 1
    plt.close(fig)
    print("✓ Test 2 passato: Colori funzionano")

# Test 3: Grafico a barre
def test_barre():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.bar(['A', 'B', 'C'], [10, 20, 15])
    assert len(ax.patches) == 3
    plt.close(fig)
    print("✓ Test 3 passato: Grafico barre creato")

# Test 4: Scatter plot
def test_scatter():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    assert len(ax.collections) > 0
    plt.close(fig)
    print("✓ Test 4 passato: Scatter plot creato")

# Test 5: Istogramma
def test_istogramma():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.hist([1, 1, 2, 2, 2, 3], bins=3)
    assert len(ax.patches) > 0
    plt.close(fig)
    print("✓ Test 5 passato: Istogramma creato")

# Test 6: Titoli e etichette
def test_titoli():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title("Titolo Test")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    assert ax.get_title() == "Titolo Test"
    plt.close(fig)
    print("✓ Test 6 passato: Titoli e etichette funzionano")

# Test 7: Salvataggio file
def test_salvataggio():
    import matplotlib.pyplot as plt
    import os
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    fig.savefig('test_grafico.png')
    assert os.path.exists('test_grafico.png')
    os.remove('test_grafico.png')
    plt.close(fig)
    print("✓ Test 7 passato: Salvataggio file funziona")

# Test 8: Subplot
def test_subplot():
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 2)
    assert len(axes.flat) == 4
    plt.close(fig)
    print("✓ Test 8 passato: Subplot creati")

# Test 9: Griglia
def test_griglia():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.grid(True)
    plt.close(fig)
    print("✓ Test 9 passato: Griglia aggiunta")

# Test 10: Legenda
def test_legenda():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], label='Test')
    ax.legend()
    plt.close(fig)
    print("✓ Test 10 passato: Legenda aggiunta")

if __name__ == "__main__":
    test_grafico_linee()
    test_colori()
    test_barre()
    test_scatter()
    test_istogramma()
    test_titoli()
    test_salvataggio()
    test_subplot()
    test_griglia()
    test_legenda()
    print("\n✅ Tutti i test passati!")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Installa matplotlib (se non presente)
```bash
pip install matplotlib
```

### Passo 2: Impara la struttura OOP di matplotlib
```python
import matplotlib.pyplot as plt

# Il modo OOP (quello che userai):
fig, ax = plt.subplots()  # Crea Figure e Axes
ax.plot([1,2,3], [1,2,3])  # Chiama metodo su Axes
plt.show()
```

### Passo 3: Crea il tuo primo grafico a linee
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
ax.set_title("Primo Grafico")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
```

### Passo 4: Aggiungi personalizzazioni
```python
ax.plot([0, 1, 2, 3], [0, 1, 4, 9], color='red', linewidth=2, label='Dati')
ax.grid(True, alpha=0.3)
ax.legend()
```

### Passo 5: Crea grafici diversi (barre, scatter, istogramma)
```python
# Barre
ax.bar(['A', 'B', 'C'], [10, 20, 15])

# Scatter
ax.scatter(x_data, y_data)

# Istogramma
ax.hist(data, bins=5)
```

### Passo 6: Usa subplot per multipli grafici
```python
fig, axes = plt.subplots(2, 2)  # 2x2 griglia
axes[0, 0].plot([1, 2, 3])
axes[0, 1].bar(['A', 'B'], [10, 20])
axes[1, 0].scatter([1, 2], [1, 2])
axes[1, 1].hist([1, 1, 2, 2, 2, 3])
```

### Passo 7: Salva i grafici
```python
fig.savefig('grafico.png', dpi=300, bbox_inches='tight')
```

---

## 💡 Trucchi e Best Practices

### ✅ Trucco 1: Scopri gli attributi di Axes
```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3])

# Scopri cosa puoi fare con `ax`
print(dir(ax))  # Tutti i metodi disponibili
help(ax.plot)   # Documentazione di un metodo
```

### ✅ Trucco 2: Personalizza colori facilmente
```python
# Usa nomi colori
ax.plot(x, y, color='red')
ax.bar(categories, values, color='blue')

# Usa codici esadecimali
ax.plot(x, y, color='#FF6B6B')

# Usa RGB
ax.plot(x, y, color=(0.5, 0.2, 0.8))

# Usa palette di colori
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
```

### ✅ Trucco 3: Figsize per dimensioni personalizzate
```python
# Grafico piccolo
fig, ax = plt.subplots(figsize=(6, 4))

# Grafico grande
fig, ax = plt.subplots(figsize=(14, 10))

# Formato predefinito
fig, ax = plt.subplots(figsize=(12, 8))
```

### ✅ Trucco 4: Usa fontsize per testi leggibili
```python
ax.set_title("Titolo", fontsize=16, fontweight='bold')
ax.set_xlabel("Asse X", fontsize=12)
ax.set_ylabel("Asse Y", fontsize=12)
ax.tick_params(labelsize=10)
```

### ✅ Trucco 5: tight_layout() per evitare sovrapposizioni
```python
fig, axes = plt.subplots(2, 2)
# ... aggiungi dati ...
fig.tight_layout()  # Adatta automaticamente lo spazio
plt.show()
```

### ✅ Trucco 6: fill_between() per aree colorate
```python
ax.plot(x, y1, label='Linea 1')
ax.fill_between(x, y1, y2, alpha=0.2, color='blue')
```

### ✅ Trucco 7: Stili di linea
```python
ax.plot(x, y, linestyle='-')    # Linea continua
ax.plot(x, y, linestyle='--')   # Trattini
ax.plot(x, y, linestyle=':')    # Puntini
ax.plot(x, y, linestyle='-.')   # Linea-punto
```

### ✅ Trucco 8: Marker per punti
```python
ax.plot(x, y, marker='o')       # Cerchi
ax.plot(x, y, marker='s')       # Quadrati
ax.plot(x, y, marker='^')       # Triangoli
ax.plot(x, y, marker='*')       # Stelle
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Dimenticare di creare Figure e Axes
```python
# SBAGLIATO
plt.plot([1, 2, 3])  # Funziona ma non è OOP
plt.title("Titolo")

# GIUSTO
fig, ax = plt.subplots()
ax.plot([1, 2, 3])
ax.set_title("Titolo")
```

### ❌ Errore 2: Confondere pyplot e oggetti
```python
# SBAGLIATO - mescolare approcci
fig, ax = plt.subplots()
ax.plot([1, 2, 3])
plt.title("Titolo")  # Usa pyplot direttamente - inconsistente!

# GIUSTO - usa solo OOP
fig, ax = plt.subplots()
ax.plot([1, 2, 3])
ax.set_title("Titolo")  # Usa metodo di ax
```

### ❌ Errore 3: Non salvare prima di plt.show()
```python
# SBAGLIATO
fig.savefig('grafico.png')
plt.show()  # Potrebbe cancellare il grafico
plt.close(fig)

# GIUSTO - salva prima di mostrare
fig.savefig('grafico.png')
plt.show()
```

### ❌ Errore 4: Dimenticare di chiudere i grafici
```python
# SBAGLIATO - consuma memoria
for i in range(100):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    plt.show()

# GIUSTO - chiudi ogni volta
for i in range(100):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    plt.show()
    plt.close(fig)
```

### ❌ Errore 5: Usare set_title() invece di title()
```python
# SBAGLIATO
ax.title("Titolo")  # Questo metodo non esiste!

# GIUSTO
ax.set_title("Titolo")  # Metodo della classe Axes
```

### ❌ Errore 6: Dimenticare che scatter non accetta colore come stringa
```python
# SBAGLIATO
ax.scatter(x, y, color='red')  # Potrebbe non funzionare come previsto

# GIUSTO
ax.scatter(x, y, c='red')  # Usa 'c' non 'color'
```

### ❌ Errore 7: Non normalizzare dati prima di istogramma
```python
# SBAGLIATO - dati troppo spread
ax.hist([1, 2, 100, 3, 4], bins=10)  # Bins grandi e vuoti

# GIUSTO - scegli bins appropriato
ax.hist([1, 2, 3, 4, 5], bins=5)
```

### ❌ Errore 8: Ignorare figsize
```python
# SBAGLIATO - grafico piccolissimo e illeggibile
fig, ax = plt.subplots()
ax.plot(data_complessa)

# GIUSTO - scegli dimensioni appropriate
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(data_complessa)
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Grafico Interattivo con Bottoni
- Crea un programma con matplotlib e ipywidgets
- Aggiungi bottoni per cambiare il tipo di grafico
- Cambia colori, stili, scale interattivamente

### 🌟 Sfida 2: Dashboard Completo
- Crea una dashboard con 6-8 grafici diversi
- Usa dati realistici (CSV o API)
- Personalizza colori e stili coerentemente
- Salva come HTML/PNG per condividere

### 🌟 Sfida 3: Animazione Grafici
- Usa `matplotlib.animation` per animare grafici
- Crea animazione di crescita lineare
- Crea animazione di scatter plot dinamico

### 🌟 Sfida 4: Heatmap e Contorno
- Crea heatmap con dati 2D (matrice)
- Crea contour plots per visualizzare funzioni
- Usa diverse colormap

### 🌟 Sfida 5: Esportazione Multiformat
- Crea una funzione che salva grafico in 5 formati (PNG, PDF, SVG, EPS, JPG)
- Ottimizza DPI per ogni formato
- Confronta file size

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Figure** | Contenitore principale per il grafico | `fig, ax = plt.subplots()` |
| **Axes** | Area dove si disegna il grafico | `ax.plot(...)` |
| **plot()** | Metodo per linee | `ax.plot(x, y, color='red')` |
| **bar()** | Metodo per barre | `ax.bar(['A', 'B'], [10, 20])` |
| **scatter()** | Metodo per punti | `ax.scatter(x, y)` |
| **hist()** | Metodo per istogrammi | `ax.hist(data, bins=5)` |
| **set_title()** | Aggiunge titolo | `ax.set_title("Titolo")` |
| **set_xlabel()** | Etichetta asse X | `ax.set_xlabel("X")` |
| **set_ylabel()** | Etichetta asse Y | `ax.set_ylabel("Y")` |
| **legend()** | Mostra legenda | `ax.legend()` |
| **grid()** | Aggiunge griglia | `ax.grid(True)` |
| **savefig()** | Salva il grafico | `fig.savefig('file.png')` |
| **subplots()** | Crea multipli grafici | `fig, axes = plt.subplots(2, 2)` |

---

## 🔗 Link Utili

### Documentazione Ufficiale
- [Matplotlib Official Documentation](https://matplotlib.org/)
- [Matplotlib API Reference](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html)
- [Axes Methods Reference](https://matplotlib.org/stable/api/axes_api.html)
- [pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

### Tutorial Interattivi
- [Real Python - Matplotlib](https://realpython.com/python-matplotlib-guide/)
- [DataCamp - Matplotlib Tutorial](https://www.datacamp.com/courses/introduction-to-data-visualization-with-matplotlib)
- [W3Schools - Matplotlib](https://www.w3schools.com/python/matplotlib_intro.asp)

### Cheat Sheet
- [Matplotlib Cheat Sheet](https://github.com/rougier/matplotlib-cheatsheet)
- [DataCamp Cheat Sheet](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1579378308/Matplotlib_Cheat_Sheet_5bcc1c7a16_03efcc6b50.pdf)

### Colori e Stili
- [Named Colors](https://matplotlib.org/stable/gallery/color/named_colors.html)
- [Colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
- [Line Styles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)

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

- [ ] Ho importato correttamente matplotlib
- [ ] Conosco la differenza tra Figure e Axes
- [ ] Riesco a creare grafici a linee, barre, scatter, istogrammi
- [ ] So come personalizzare: colori, etichette, titoli, legende
- [ ] So come usare subplot per multipli grafici
- [ ] Riesco a salvare grafici in file (PNG, PDF, SVG)
- [ ] Ho testato il codice con i casi di prova forniti
- [ ] Il codice è commentato e leggibile
- [ ] Ho provato le sfide bonus
- [ ] Capisco come matplotlib usa classi (Figure, Axes) per un'interfaccia OOP

---

**Buon lavoro! 🎨 Matplotlib è il primo passo per visualizzare dati come un professionista!**

*"Un'immagine vale mille parole. Un grafico ben fatto vale mille fogli di numeri."*
