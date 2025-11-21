# Es4: Pandas - Analizzare Dati con DataFrame

## 📊 Informazioni Generali

**Livello:** 🟡 BASE
**Durata stimata:** 4-5 ore
**Prerequisiti:** Es1-Es3 completati, NumPy, dizionari, CSV basico

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Utilizzare** la classe `DataFrame` di pandas per analizzare dati strutturati
- ✅ **Creare** DataFrame da diverse fonti: liste, dizionari, CSV, array NumPy
- ✅ **Esplorare** dati con metodi: `head()`, `tail()`, `info()`, `describe()`
- ✅ **Selezionare** dati con `loc[]`, `iloc[]`, filtraggio booleano
- ✅ **Manipolare** dati: `groupby()`, `sort_values()`, `apply()`
- ✅ **Pulire dati**: gestire valori mancanti (NaN), duplicati
- ✅ **Salvare** e caricare dati da CSV

**Concetti fondamentali:**
- Classe `DataFrame` (tabella OOP)
- Classe `Series` (colonna/riga)
- Index e colonne
- Operazioni pandasiane su dati tabulari
- Aggregazione e raggruppamento

---

## 📖 Descrizione

Pandas è la libreria **regina per l'analisi dati** in Python. Mentre NumPy lavora con array numerici, **pandas lavora con dati strutturati realistici** (tabelle, CSV, database).

**Perché pandas?**

1. **Tabelle come oggetti** - La classe `DataFrame` rappresenta dati tabulari nativamente
2. **Etichette per colonne** - Accedi con nomi, non solo indici numerici
3. **Operazioni intelligenti** - Aggregazioni, groupby, join di tabelle
4. **Integrazione dati** - Leggi/scrivi CSV, Excel, SQL, JSON
5. **Pulizia dati** - Gestione NaN, duplicati, conversioni tipo

**Confronto: NumPy vs Pandas**

```python
# ❌ NumPy - Matrix numerica senza contesto
import numpy as np
data = np.array([[25, 50000], [30, 60000], [35, 75000]])
print(data[0, 1])  # 50000 - cosa rappresenta?

# ✅ Pandas - Tabella strutturata con significato
import pandas as pd
df = pd.DataFrame({
    'Eta': [25, 30, 35],
    'Stipendio': [50000, 60000, 75000]
})
print(df['Stipendio'].mean())  # 61666.67 - significato chiaro!
```

---

## 📝 Consegna Dettagliata

### Parte 1: Creare DataFrame

**Crea un programma che:**

1. **Crea DataFrame da dizionario**
   - Dati studenti: nome, cognome, voto, materia
   - Dati vendite: prodotto, mese, quantità, prezzo
   - Dati temperature: giorno, temperatura_min, temperatura_max

2. **Crea DataFrame da liste**
   - Lista di liste (righe)
   - Specifica nomi colonne con `columns=`
   - Verifica forma con `.shape`

3. **Crea DataFrame da file CSV**
   - Leggi con `pd.read_csv()`
   - Specifica colonna indice con `index_col=`
   - Gestisci separatori diversi (`,`, `;`, `\t`)

4. **Crea DataFrame da NumPy array**
   - Converti array NumPy in DataFrame
   - Aggiungi nomi di colonna e indice

### Parte 2: Esplorare DataFrame

**Crea un programma che:**

1. **Ispeziona il DataFrame**
   - Visualizza prime righe: `.head(n)`
   - Visualizza ultime righe: `.tail(n)`
   - Forma del DataFrame: `.shape`
   - Info colonne: `.info()`
   - Statistiche descrittive: `.describe()`

2. **Accedi a colonne e righe**
   - Accedi singola colonna: `df['nome']`
   - Accedi singola riga: `df.loc[0]`
   - Accedi elemento: `df.loc[0, 'nome']`
   - Usa `.iloc[]` per posizioni numeriche

3. **Controlli sui dati**
   - Conteggio non-null: `.count()`
   - Tipi di dati: `.dtypes`
   - Valori unici: `.nunique()`
   - Duplicati: `.duplicated()`

### Parte 3: Filtraggio e Selezione

**Crea un programma che:**

1. **Filtraggio booleano**
   - Seleziona righe dove stipendio > 50000
   - Seleziona studenti con voto >= 7
   - Filtri multipli: AND (`&`), OR (`|`), NOT (`~`)

2. **Selezione per colonne**
   - Singola colonna: `df['nome']`
   - Multiple colonne: `df[['nome', 'eta']]`
   - Intervallo di colonne: `df.loc[:, 'nome':'eta']`

3. **Selezione per posizione**
   - Righe 2-5: `df.iloc[2:5]`
   - Righe e colonne: `df.iloc[0:3, 1:3]`

### Parte 4: Manipolazione Dati

**Crea un programma che:**

1. **Ordinamento**
   - Ordina per colonna: `df.sort_values(by='age')`
   - Ordina decrescente: `ascending=False`
   - Ordina per multiple colonne

2. **Raggruppamento e aggregazione**
   - Raggruppa per categoria: `df.groupby('categoria')`
   - Calcola media per gruppo: `.mean()`
   - Calcola più aggregazioni: `.agg({'colonna': ['mean', 'sum']})`

3. **Operazioni su colonne**
   - Applica funzione: `.apply()`
   - Modifica valori: assegnazione diretta
   - Creare colonne calcolate

4. **Gestione valori mancanti**
   - Trova NaN: `.isna()`
   - Conta NaN: `.isna().sum()`
   - Riempi NaN: `.fillna()`
   - Elimina NaN: `.dropna()`

5. **Gestione duplicati**
   - Trova duplicati: `.duplicated()`
   - Elimina duplicati: `.drop_duplicates()`

### Parte 5: Esercizio Pratico Completo

**Dataset 1: Analisi Voti Studenti**

1. Crea DataFrame con 20 studenti, materie, voti
2. Calcola media voti per studente
3. Calcola media voti per materia
4. Identifica top 5 studenti
5. Identifica studenti che hanno bisogno di aiuto (voto < 6)

**Dataset 2: Analisi Vendite**

1. Crea DataFrame con prodotti, mesi, vendite, prezzo
2. Calcola ricavo totale per prodotto
3. Calcola ricavo per mese
4. Identifica prodotto più venduto
5. Crea report mensile

**Dataset 3: Analisi Temperatura**

1. Carica dati temperature città diverse
2. Calcola media, min, max per città
3. Confronta temperature tra città
4. Identifica giorno più caldo/freddo
5. Calcola trend (aumento/diminuzione)

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ PARTE 1: CREARE DATAFRAME ============

import pandas as pd
import numpy as np

# Da dizionario
dati_studenti = {
    'Nome': ['Marco', 'Laura', 'Giovanni', 'Anna', 'Paolo'],
    'Cognome': ['Rossi', 'Verdi', 'Bianchi', 'Neri', 'Gialli'],
    'Eta': [20, 21, 19, 20, 22],
    'Voto_Matematica': [8.5, 7.0, 9.0, 8.0, 7.5],
    'Voto_Italiano': [7.0, 8.5, 7.5, 9.0, 8.0]
}

df_studenti = pd.DataFrame(dati_studenti)
print("DataFrame Studenti:")
print(df_studenti)
print()

# ============ PARTE 2: ESPLORARE DATAFRAME ============

print("=== ESPLORAZIONE ===")
print(f"Forma: {df_studenti.shape}")  # (5, 5)
print(f"\nPrime 3 righe:")
print(df_studenti.head(3))

print(f"\nUltime 2 righe:")
print(df_studenti.tail(2))

print(f"\nInformazioni colonne:")
print(df_studenti.info())

print(f"\nStatistiche descrittive:")
print(df_studenti.describe())

print(f"\nTipi di dati:")
print(df_studenti.dtypes)

# ============ PARTE 3: ACCEDERE AI DATI ============

print("\n=== ACCESSO DATI ===")
print(f"Colonna 'Nome': {df_studenti['Nome'].tolist()}")
print(f"\nPrimo studente (riga 0):")
print(df_studenti.loc[0])

print(f"\nNome e Eta del primo studente:")
print(df_studenti.loc[0, ['Nome', 'Eta']])

print(f"\nVoti di Marco:")
print(f"Matematica: {df_studenti.loc[0, 'Voto_Matematica']}")
print(f"Italiano: {df_studenti.loc[0, 'Voto_Italiano']}")

# ============ PARTE 4: FILTRAGGIO ============

print("\n=== FILTRAGGIO ===")

# Studenti con voto matematica >= 8
bravi_matematica = df_studenti[df_studenti['Voto_Matematica'] >= 8]
print(f"Studenti bravi in matematica (voto >= 8):")
print(bravi_matematica[['Nome', 'Voto_Matematica']])

# Studenti minorenni (eta < 21)
minorenni = df_studenti[df_studenti['Eta'] < 21]
print(f"\nStudenti minorenni (eta < 21):")
print(minorenni[['Nome', 'Eta']])

# Studenti bravi in entrambe le materie
eccellenti = df_studenti[(df_studenti['Voto_Matematica'] >= 8) &
                         (df_studenti['Voto_Italiano'] >= 8)]
print(f"\nStudenti eccellenti (voti >= 8 in entrambe):")
print(eccellenti[['Nome', 'Voto_Matematica', 'Voto_Italiano']])

# ============ PARTE 5: ORDINAMENTO ============

print("\n=== ORDINAMENTO ===")

# Ordina per voto matematica decrescente
ordinati = df_studenti.sort_values('Voto_Matematica', ascending=False)
print(f"Ordinati per voto matematica (decrescente):")
print(ordinati[['Nome', 'Voto_Matematica']])

# Ordina per eta, poi nome
ordinati2 = df_studenti.sort_values(['Eta', 'Nome'])
print(f"\nOrdinati per eta e nome:")
print(ordinati2[['Nome', 'Eta']])

# ============ PARTE 6: MANIPOLAZIONE ============

print("\n=== MANIPOLAZIONE ===")

# Crea colonna con media voti
df_studenti['Media_Voti'] = (df_studenti['Voto_Matematica'] +
                              df_studenti['Voto_Italiano']) / 2
print(f"DataFrame con media voti:")
print(df_studenti[['Nome', 'Voto_Matematica', 'Voto_Italiano', 'Media_Voti']])

# Calcola statistiche per colonna
print(f"\nMedia matematica: {df_studenti['Voto_Matematica'].mean():.2f}")
print(f"Max italiano: {df_studenti['Voto_Italiano'].max():.2f}")
print(f"Min matematica: {df_studenti['Voto_Matematica'].min():.2f}")

# ============ PARTE 7: AGGREGAZIONE (GROUPBY) ============

# Dataset vendite
vendite = {
    'Prodotto': ['A', 'B', 'A', 'B', 'C', 'A', 'B', 'C', 'C', 'A'],
    'Mese': ['Gen', 'Gen', 'Feb', 'Feb', 'Gen', 'Mar', 'Mar', 'Feb', 'Mar', 'Feb'],
    'Quantita': [10, 15, 8, 12, 20, 5, 18, 7, 14, 11],
    'Prezzo': [100, 150, 100, 150, 200, 100, 150, 200, 200, 100]
}

df_vendite = pd.DataFrame(vendite)
print(f"\n=== DATASET VENDITE ===")
print(df_vendite)

# Raggruppa per prodotto
print(f"\nVendite totali per prodotto:")
per_prodotto = df_vendite.groupby('Prodotto')['Quantita'].sum()
print(per_prodotto)

# Raggruppa per mese
print(f"\nVendite medie per mese:")
per_mese = df_vendite.groupby('Mese')['Quantita'].mean()
print(per_mese)

# Aggregazioni multiple
print(f"\nAggregazioni per prodotto:")
aggregato = df_vendite.groupby('Prodotto').agg({
    'Quantita': ['sum', 'mean', 'count'],
    'Prezzo': ['mean']
})
print(aggregato)

# ============ PARTE 8: RICAVO TOTALE ============

print(f"\n=== CALCOLI AVANZATI ===")

# Calcola ricavo per riga
df_vendite['Ricavo'] = df_vendite['Quantita'] * df_vendite['Prezzo']
print(f"DataFrame con ricavo:")
print(df_vendite)

# Ricavo totale
ricavo_totale = df_vendite['Ricavo'].sum()
print(f"\nRicavo totale: {ricavo_totale}")

# Ricavo per prodotto
ricavo_prodotto = df_vendite.groupby('Prodotto')['Ricavo'].sum()
print(f"\nRicavo per prodotto:")
print(ricavo_prodotto)

# ============ PARTE 9: GESTIONE VALORI MANCANTI ============

print(f"\n=== VALORI MANCANTI ===")

# Crea DataFrame con NaN
dati_con_nan = {
    'Nome': ['Marco', 'Laura', None, 'Anna'],
    'Voto': [8.5, np.nan, 7.5, 9.0]
}

df_nan = pd.DataFrame(dati_con_nan)
print(f"DataFrame con valori mancanti:")
print(df_nan)

print(f"\nValori mancanti per colonna:")
print(df_nan.isna().sum())

print(f"\nRighe senza valori mancanti:")
print(df_nan.dropna())

print(f"\nRiempi NaN con valore fisso:")
df_filled = df_nan.fillna({'Voto': 0, 'Nome': 'Sconosciuto'})
print(df_filled)

# ============ PARTE 10: SAVE/LOAD CSV ============

print(f"\n=== SALVA/CARICA CSV ===")

# Salva su CSV
df_studenti.to_csv('studenti.csv', index=False)
print("Salvato 'studenti.csv'")

# Carica da CSV
df_caricato = pd.read_csv('studenti.csv')
print(f"\nCaricato da CSV:")
print(df_caricato.head())

# ============ PARTE 11: ANALISI TEMPERATURE ============

print(f"\n=== ANALISI TEMPERATURE ===")

temp_data = {
    'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano', 'Napoli'],
    'Data': ['01/01', '01/01', '02/01', '01/01', '02/01', '02/01'],
    'Temperatura': [15, 5, 16, 18, 6, 19]
}

df_temp = pd.DataFrame(temp_data)
print(df_temp)

print(f"\nTemperatura media per città:")
print(df_temp.groupby('Città')['Temperatura'].mean())

print(f"\nTemperatura max per città:")
print(df_temp.groupby('Città')['Temperatura'].max())

print(f"\nCittà più calda (media): {df_temp.groupby('Città')['Temperatura'].mean().idxmax()}")
print(f"Città più fredda (media): {df_temp.groupby('Città')['Temperatura'].mean().idxmin()}")
```

---

## 🔍 Casi di Prova (Test)

```python
# Test 1: Creazione DataFrame
def test_creazione():
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert df.shape == (3, 2)
    assert list(df.columns) == ['A', 'B']
    print("✓ Test 1 passato: Creazione DataFrame")

# Test 2: Accesso elementi
def test_accesso():
    import pandas as pd
    df = pd.DataFrame({'Nome': ['Marco', 'Laura'], 'Eta': [25, 28]})
    assert df.loc[0, 'Nome'] == 'Marco'
    assert df.loc[1, 'Eta'] == 28
    print("✓ Test 2 passato: Accesso elementi")

# Test 3: Filtraggio
def test_filtraggio():
    import pandas as pd
    df = pd.DataFrame({'Voto': [6, 7, 8, 9, 10]})
    filtrato = df[df['Voto'] >= 8]
    assert len(filtrato) == 3
    print("✓ Test 3 passato: Filtraggio")

# Test 4: Ordinamento
def test_ordinamento():
    import pandas as pd
    df = pd.DataFrame({'Nome': ['C', 'A', 'B'], 'Voto': [7, 9, 8]})
    ordinato = df.sort_values('Voto', ascending=False)
    assert ordinato.iloc[0]['Voto'] == 9
    print("✓ Test 4 passato: Ordinamento")

# Test 5: Groupby
def test_groupby():
    import pandas as pd
    df = pd.DataFrame({'Categoria': ['A', 'B', 'A', 'B'], 'Valore': [10, 20, 15, 25]})
    gruppo = df.groupby('Categoria')['Valore'].sum()
    assert gruppo['A'] == 25
    assert gruppo['B'] == 45
    print("✓ Test 5 passato: Groupby")

# Test 6: Statistiche
def test_statistiche():
    import pandas as pd
    df = pd.DataFrame({'Voto': [6, 7, 8, 9, 10]})
    assert df['Voto'].mean() == 8.0
    assert df['Voto'].min() == 6
    assert df['Voto'].max() == 10
    print("✓ Test 6 passato: Statistiche")

# Test 7: Colonne nuove
def test_colonne_nuove():
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df['C'] = df['A'] + df['B']
    assert list(df['C']) == [5, 7, 9]
    print("✓ Test 7 passato: Colonne nuove")

# Test 8: Valori mancanti
def test_nan():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({'A': [1, np.nan, 3]})
    assert df['A'].isna().sum() == 1
    print("✓ Test 8 passato: Valori mancanti")

# Test 9: Head/Tail
def test_head_tail():
    import pandas as pd
    df = pd.DataFrame({'A': range(10)})
    assert len(df.head(3)) == 3
    assert len(df.tail(2)) == 2
    print("✓ Test 9 passato: Head/Tail")

# Test 10: Shape
def test_shape():
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    assert df.shape == (3, 3)
    print("✓ Test 10 passato: Shape")

if __name__ == "__main__":
    test_creazione()
    test_accesso()
    test_filtraggio()
    test_ordinamento()
    test_groupby()
    test_statistiche()
    test_colonne_nuove()
    test_nan()
    test_head_tail()
    test_shape()
    print("\n✅ Tutti i test passati!")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Installa pandas
```bash
pip install pandas
```

### Passo 2: Crea il tuo primo DataFrame
```python
import pandas as pd
df = pd.DataFrame({'Nome': ['Marco', 'Laura'],
                   'Eta': [25, 28]})
print(df)
```

### Passo 3: Esplora il DataFrame
```python
print(df.head())      # Prime righe
print(df.shape)       # Forma
print(df.info())      # Info colonne
print(df.describe())  # Statistiche
```

### Passo 4: Accedi ai dati
```python
print(df['Nome'])     # Colonna
print(df.loc[0])      # Riga
print(df.loc[0, 'Eta'])  # Elemento
```

### Passo 5: Filtra i dati
```python
filtrato = df[df['Eta'] >= 25]
```

### Passo 6: Manipola i dati
```python
df['Categoria'] = df['Eta'].apply(lambda x: 'Giovane' if x < 30 else 'Adulto')
```

### Passo 7: Aggrega i dati
```python
df.groupby('Categoria').agg({'Eta': ['mean', 'count']})
```

### Passo 8: Salva e carica
```python
df.to_csv('file.csv')
df2 = pd.read_csv('file.csv')
```

---

## 💡 Trucchi e Best Practices

### ✅ Trucco 1: Scopri metodi con dir() e help()
```python
df = pd.DataFrame({'A': [1, 2, 3]})
print(dir(df))  # Tutti i metodi
help(df.groupby)  # Aiuto specifico
```

### ✅ Trucco 2: Usa `.copy()` per evitare modifiche inattese
```python
df_copy = df.copy()  # Copia vera
df_view = df         # Riferimento - modifiche condivise
```

### ✅ Trucco 3: Usa `.loc[]` vs `.iloc[]`
```python
df.loc[0, 'Nome']     # Per etichette
df.iloc[0, 0]         # Per posizioni numeriche
```

### ✅ Trucco 4: Filtri booleani multipli
```python
# AND
df[(df['Eta'] > 25) & (df['Voto'] >= 8)]

# OR
df[(df['Eta'] < 20) | (df['Voto'] >= 9)]

# NOT
df[~(df['Eta'] > 25)]
```

### ✅ Trucco 5: Aggrega con più funzioni
```python
df.groupby('Categoria').agg({
    'Valore': ['sum', 'mean', 'count'],
    'Prezzo': ['mean', 'max']
})
```

### ✅ Trucco 6: Usa `.apply()` per operazioni custom
```python
df['Categoria'] = df['Voto'].apply(lambda x: 'Bravo' if x >= 7 else 'Scarso')
```

### ✅ Trucco 7: Rinomina colonne facilmente
```python
df.rename(columns={'old_name': 'new_name'})
```

### ✅ Trucco 8: Usa `.drop()` per righe/colonne
```python
df.drop('Nome', axis=1)  # Elimina colonna
df.drop(0)               # Elimina riga 0
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Confondere `.iloc[]` e `.loc[]`
```python
# SBAGLIATO - confusione
print(df.loc[1])  # Potrebbe non essere la 2ª riga se indice non è 0,1,2,...
print(df.iloc[1]) # Sempre la 2ª riga per posizione

# GIUSTO - sii consapevole
print(df.iloc[1])  # Per indice numerico
print(df.loc['A'])  # Per etichetta
```

### ❌ Errore 2: Dimenticare parentesi per filtri multipli
```python
# SBAGLIATO
df[df['A'] > 5 and df['B'] < 10]  # Errore!

# GIUSTO
df[(df['A'] > 5) & (df['B'] < 10)]  # & not and
```

### ❌ Errore 3: Modificare DataFrame senza chain
```python
# SBAGLIATO - warning (SettingWithCopyWarning)
df[df['A'] > 5]['B'] = 100  # Potrebbe non modificare

# GIUSTO - assegna completamente
df.loc[df['A'] > 5, 'B'] = 100
```

### ❌ Errore 4: Non controllare NaN
```python
# SBAGLIATO - NaN causa problemi
media = df['Voto'].mean()  # Ignora NaN di default (OK)
totale = df['Voto'].sum()  # Ignora NaN (potrebbe essere un problema)

# GIUSTO - sii consapevole
print(df.isna().sum())  # Conta NaN
df.dropna()             # Elimina righe con NaN
```

### ❌ Errore 5: Usare `==` per NaN
```python
# SBAGLIATO
df[df['Voto'] == np.nan]  # Non funziona! NaN != NaN

# GIUSTO
df[df['Voto'].isna()]
```

### ❌ Errore 6: Non specificare indice con groupby
```python
# SBAGLIATO - risultato confuso
df.groupby('Categoria')  # Cosa ottieni?

# GIUSTO - specifica aggregazione
df.groupby('Categoria')['Valore'].sum()
df.groupby('Categoria')[['Valore', 'Prezzo']].mean()
```

### ❌ Errore 7: Dimenticare il reset_index() con groupby
```python
# SBAGLIATO - risultato è Series
risultato = df.groupby('Categoria')['Valore'].sum()
print(risultato)  # Index strano

# GIUSTO - converti se vuoi DataFrame
risultato = df.groupby('Categoria')['Valore'].sum().reset_index()
```

### ❌ Errore 8: Non gestire colonne di tipo sbagliato
```python
# SBAGLIATO
df['Data'] = '01/01/2024'
df[df['Data'] > '2024-01-01']  # Confronto stringa, non data!

# GIUSTO
df['Data'] = pd.to_datetime(df['Data'])
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Merge e Join
- Unisci due DataFrame con `merge()` e `join()`
- Pratica inner/outer/left/right joins
- Lavora con chiavi multiple

### 🌟 Sfida 2: Pivot Table
- Crea pivot table con dati multidimensionali
- Aggrega in modo intelligente
- Crea tabelle incrociate

### 🌟 Sfida 3: Time Series
- Lavora con serie temporali (`pd.to_datetime()`)
- Resample dati (giornaliero → mensile)
- Calcola rolling mean

### 🌟 Sfida 4: Analisi Esplorativa (EDA)
- Carica dataset reale (es. Titanic, Iris)
- Pulisci e prepara i dati
- Crea report di analisi

### 🌟 Sfida 5: Export Avanzato
- Esporta in Excel con `to_excel()`
- Crea fogli multipli
- Formatta celle e colonne
- Esporta in SQL

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **DataFrame** | Tabella 2D (righe + colonne) | `pd.DataFrame({'A': [1,2,3]})` |
| **Series** | Vettore 1D (una colonna) | `df['Nome']` |
| **Index** | Etichette di righe | `.index` |
| **Colonne** | Etichette di colonne | `.columns` |
| **loc[]** | Accedi per etichetta | `df.loc[0, 'Nome']` |
| **iloc[]** | Accedi per posizione | `df.iloc[0, 0]` |
| **head()** | Prime N righe | `.head(5)` |
| **tail()** | Ultime N righe | `.tail(3)` |
| **groupby()** | Raggruppa per categoria | `.groupby('Categoria')` |
| **agg()** | Aggrega con funzioni | `.agg({'col': ['sum', 'mean']})` |
| **sort_values()** | Ordina DataFrame | `.sort_values('Voto', ascending=False)` |
| **apply()** | Applica funzione custom | `.apply(lambda x: x*2)` |
| **fillna()** | Riempi valori mancanti | `.fillna(0)` |
| **dropna()** | Elimina NaN | `.dropna()` |
| **to_csv()** | Salva in CSV | `.to_csv('file.csv')` |
| **read_csv()** | Carica da CSV | `pd.read_csv('file.csv')` |

---

## 🔗 Link Utili

### Documentazione Ufficiale
- [Pandas Official Documentation](https://pandas.pydata.org/)
- [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

### Tutorial Interattivi
- [Real Python - Pandas](https://realpython.com/learning-paths/pandas-data-science/)
- [DataCamp - Pandas Tutorial](https://www.datacamp.com/courses/data-manipulation-with-pandas)
- [W3Schools - Pandas](https://www.w3schools.com/python/pandas/default.asp)

### Cheat Sheet
- [Pandas Cheat Sheet (DataCamp)](https://assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf)
- [Pandas Cheat Sheet (GitHub)](https://github.com/pandas-dev/pandas/blob/main/doc/source/user_guide/basics.rst)

### Dataset di Esempio
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

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

- [ ] So creare DataFrame da diverse fonti (dizionario, lista, CSV)
- [ ] Conosco head(), tail(), info(), describe()
- [ ] So accedere ai dati con loc[], iloc[]
- [ ] Riesco a filtrare con condizioni booleane
- [ ] So usare sort_values() e ordinare DataFrame
- [ ] Capisco groupby() e aggregazioni
- [ ] So creare colonne calcolate
- [ ] So gestire valori mancanti (NaN)
- [ ] So salvare e caricare CSV
- [ ] Ho testato il codice con i casi di prova forniti
- [ ] Ho provato le sfide bonus
- [ ] Capisco che pandas è lo standard per data analysis Python

---

**Buon lavoro! 📊 Pandas è il cuore dell'analisi dati in Python!**

*"I dati sono il nuovo petrolio - pandas ti insegna come raffinarli."*
