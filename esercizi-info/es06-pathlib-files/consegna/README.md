# Es6: Pathlib - Navigare il File System come Oggetti

## 📊 Informazioni Generali

**Livello:** 🟡 BASE
**Durata stimata:** 3-4 ore
**Prerequisiti:** Es1-Es5 completati, file I/O basico, os module

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Utilizzare** la classe `Path` di pathlib per file system OOP
- ✅ **Creare** oggetti Path da stringhe e componenti
- ✅ **Navigare** il file system: parent, name, stem, suffix
- ✅ **Verificare** file/directory: `exists()`, `is_file()`, `is_dir()`
- ✅ **Leggere/scrivere** file: `read_text()`, `write_text()`, `open()`
- ✅ **Creare/eliminare** file e directory: `mkdir()`, `rmdir()`, `unlink()`
- ✅ **Cercare file** con pattern glob: `glob()`, `rglob()`
- ✅ **Manipolare percorsi** in modo portable (Windows/Linux/Mac)
- ✅ **Creare applicazioni reali**: organizzatore file, backup, ricerca

**Concetti fondamentali:**
- Classe `Path` di pathlib
- Percorsi assoluti vs relativi
- Componenti di un percorso (parent, name, stem, suffix)
- Operazioni su file e directory
- Glob pattern matching
- Cross-platform compatibility

---

## 📖 Descrizione

Pathlib è un'interfaccia **OOP per il file system** che rende lavorare con file e directory **intuitivo e portable**.

**Perché usare pathlib?**

1. **Orientato agli oggetti** - Percorsi come oggetti, non stringhe
2. **Portable** - Stesso codice su Windows, Linux, macOS
3. **Intuitivo** - Metodi chiari: `exists()`, `is_file()`, `read_text()`
4. **Componibilità** - Combina percorsi con `/` (operatore overloadato)
5. **Pattern matching** - `glob()` per cercare file facilmente

**Confronto: os.path vs pathlib**

```python
# ❌ os.path - IMPERATIVO e FRAGILE
import os
file_path = os.path.join("cartella", "file.txt")
if os.path.exists(file_path):
    contenuto = open(file_path, 'r').read()

# ✅ pathlib - OOP e ELEGANTE
from pathlib import Path
file_path = Path("cartella") / "file.txt"  # Combina con /
if file_path.exists():
    contenuto = file_path.read_text()  # Metodo diretto!
```

---

## 📝 Consegna Dettagliata

### Parte 1: Creare e Navigare Path

**Crea un programma che:**

1. **Crea oggetti Path**
   - Da stringa: `Path("cartella/file.txt")`
   - Dalla directory attuale: `Path.cwd()`
   - Home directory: `Path.home()`
   - Directory temporanea: `Path("/tmp")`

2. **Combina percorsi**
   - Usa l'operatore `/`: `Path("cartella") / "file.txt"`
   - Non usa `os.path.join()`

3. **Accedi a componenti**
   - Nome file: `.name` → "file.txt"
   - Nome senza estensione: `.stem` → "file"
   - Estensione: `.suffix` → ".txt"
   - Directory padre: `.parent`
   - Percorso assoluto: `.absolute()`

### Parte 2: Verificare Esistenza e Tipo

**Crea un programma che:**

1. **Verifica file/directory**
   - Esiste: `.exists()`
   - È file: `.is_file()`
   - È directory: `.is_dir()`
   - È symlink: `.is_symlink()`
   - È file nascosto: `.name.startswith('.')`

2. **Ottieni informazioni**
   - Dimensione: `.stat().st_size`
   - Permessi: `.stat().st_mode`
   - Data modifica: `.stat().st_mtime`

### Parte 3: Operazioni su File

**Crea un programma che:**

1. **Leggi file**
   - Testo: `.read_text()`
   - Bytes: `.read_bytes()`
   - Riga per riga: `.open()` e ciclo

2. **Scrivi file**
   - Testo: `.write_text(contenuto)`
   - Bytes: `.write_bytes(dati)`
   - Append (aggiungi): `.open('a')` o `.write_text(append=True)` (con libreria)

3. **Operazioni di file**
   - Copia file: `shutil.copy()` con Path
   - Rinomina: `.rename(nuovo_nome)`
   - Elimina: `.unlink()`
   - Crea symlink: `.symlink_to()`

### Parte 4: Operazioni su Directory

**Crea un programma che:**

1. **Crea directory**
   - Crea singola: `.mkdir()`
   - Crea genitori se necessario: `.mkdir(parents=True)`

2. **Naviga directory**
   - Elenca contenuto: `.iterdir()`
   - Elenca ricorsivamente: `.rglob('*')`
   - Conta file: `len(list(path.iterdir()))`

3. **Elimina directory**
   - Vuota: `.rmdir()`
   - Ricorsivamente: `shutil.rmtree()`

### Parte 5: Cercare File con Glob

**Crea un programma che:**

1. **Glob semplice**
   - Tutti i .txt: `path.glob('*.txt')`
   - Pattern specifico: `path.glob('file_*.txt')`
   - Cartelle specifiche: `path.glob('*/file.txt')`

2. **Glob ricorsivo**
   - Tutti i file ricorsivamente: `path.rglob('*')`
   - Tutti i .py ricorsivamente: `path.rglob('*.py')`

3. **Filtraggio risultati**
   - Solo file: `[p for p in path.rglob('*') if p.is_file()]`
   - Solo directory: `[p for p in path.rglob('*') if p.is_dir()]`

### Parte 6: Esercizio Pratico Completo

**Progetto 1: Organizzatore File**

1. Crea struttura di cartelle:
   - Documenti / (PDF, DOCX, TXT)
   - Immagini / (JPG, PNG, GIF)
   - Video / (MP4, AVI)
   - Audio / (MP3, WAV)

2. Creai script che:
   - Raccoglie file da cartella mixed
   - Li organizza per tipo
   - Rinomina per coerenza

**Progetto 2: Backup Automatico**

1. Crea script che:
   - Scansiona cartella source
   - Copia in cartella backup
   - Mantiene struttura directory
   - Registra operazioni in log

**Progetto 3: Ricerca Avanzata**

1. Ricerca file per:
   - Nome esatto
   - Pattern (glob)
   - Estensione
   - Dimensione
   - Data modifica

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ PARTE 1: CREARE E NAVIGARE PATH ============

from pathlib import Path
import shutil
from datetime import datetime

print("=== NAVIGAZIONE PATH ===")

# Crea Path da stringa
p = Path("file.txt")
print(f"Path relativo: {p}")

# Directory attuale
cwd = Path.cwd()
print(f"Directory attuale: {cwd}")

# Home directory
home = Path.home()
print(f"Home directory: {home}")

# Combina percorsi con / (non os.path.join!)
cartella = Path("documenti")
file = cartella / "report.pdf"
print(f"Percorso combinato: {file}")

# Componenti
print(f"\nComponenti di '{file}':")
print(f"  Nome completo: {file.name}")      # report.pdf
print(f"  Nome senza estensione: {file.stem}")  # report
print(f"  Estensione: {file.suffix}")       # .pdf
print(f"  Directory padre: {file.parent}")  # documenti
print(f"  Path assoluto: {file.absolute()}")

# ============ PARTE 2: VERIFICARE ESISTENZA ============

print(f"\n=== VERIFICAZIONE ===")

# Crea una cartella di test
test_dir = Path("test_pathlib")
test_file = test_dir / "file.txt"

# Verifica
print(f"Esiste '{test_dir}'? {test_dir.exists()}")

# Crea cartella
test_dir.mkdir(exist_ok=True)
print(f"Dopo mkdir: esiste '{test_dir}'? {test_dir.exists()}")
print(f"È una directory? {test_dir.is_dir()}")

# Crea file
test_file.write_text("Contenuto di prova\n")
print(f"\nEsiste '{test_file}'? {test_file.exists()}")
print(f"È un file? {test_file.is_file()}")

# ============ PARTE 3: LEGGERE/SCRIVERE FILE ============

print(f"\n=== LETTURA/SCRITTURA ===")

# Scrivi testo
file_path = test_dir / "dati.txt"
contenuto = "Linea 1\nLinea 2\nLinea 3\n"
file_path.write_text(contenuto)
print(f"Scritto: {file_path}")

# Leggi testo
testo_letto = file_path.read_text()
print(f"Contenuto letto:\n{testo_letto}")

# Leggi riga per riga
print("Riga per riga:")
for i, linea in enumerate(file_path.read_text().split('\n'), 1):
    if linea:
        print(f"  {i}: {linea}")

# Append (aggiungi)
file_path.write_text(file_path.read_text() + "Linea 4\n")
print(f"Aggiunto testo a {file_path}")

# Statistiche file
stat = file_path.stat()
print(f"\nStatistiche '{file_path}':")
print(f"  Dimensione: {stat.st_size} bytes")
print(f"  Modificato: {datetime.fromtimestamp(stat.st_mtime)}")

# ============ PARTE 4: OPERAZIONI FILE ============

print(f"\n=== OPERAZIONI FILE ===")

# Rinomina
nuovo_nome = test_dir / "dati_rinominato.txt"
file_path.rename(nuovo_nome)
print(f"Rinominato: {file_path} → {nuovo_nome}")

# Copia
file_copia = test_dir / "copia.txt"
shutil.copy(nuovo_nome, file_copia)
print(f"Copiato: {nuovo_nome} → {file_copia}")

# Elenca file nella directory
print(f"\nFile in '{test_dir}':")
for file in test_dir.iterdir():
    print(f"  {file.name} ({file.stat().st_size} bytes)")

# ============ PARTE 5: GLOB PATTERNS ============

print(f"\n=== GLOB PATTERNS ===")

# Crea alcuni file di test
(test_dir / "doc1.txt").write_text("Doc 1")
(test_dir / "doc2.txt").write_text("Doc 2")
(test_dir / "image.png").write_text("PNG")
(test_dir / "data.csv").write_text("CSV")

# Glob: tutti i .txt
txt_files = list(test_dir.glob("*.txt"))
print(f"File .txt: {[f.name for f in txt_files]}")

# Glob: pattern specifico
pattern = list(test_dir.glob("doc*.txt"))
print(f"File doc*.txt: {[f.name for f in pattern]}")

# Glob: tutti i file
all_files = list(test_dir.glob("*"))
print(f"Tutti i file: {[f.name for f in all_files]}")

# ============ PARTE 6: ORGANIZZATORE FILE ============

print(f"\n=== ORGANIZZATORE FILE ===")

def organizza_per_estensione(cartella_source):
    """Organizza file in sottocartelle per estensione"""
    source = Path(cartella_source)

    # Raggruppa per estensione
    file_per_ext = {}
    for file in source.glob("*"):
        if file.is_file():
            ext = file.suffix.lstrip('.')  # Rimuovi il punto
            if ext not in file_per_ext:
                file_per_ext[ext] = []
            file_per_ext[ext].append(file)

    # Crea cartelle e sposta file
    for ext, files in file_per_ext.items():
        folder = source / ext
        folder.mkdir(exist_ok=True)

        for file in files:
            destinazione = folder / file.name
            shutil.move(str(file), str(destinazione))
            print(f"  Spostato: {file.name} → {folder.name}/")

    return file_per_ext

# Organizza
print(f"Organizzazione file in '{test_dir}':")
risultato = organizza_per_estensione(test_dir)

# Mostra struttura
print(f"\nStruttura dopo organizzazione:")
for item in test_dir.rglob("*"):
    indent = "  " * (len(item.relative_to(test_dir).parts) - 1)
    if item.is_file():
        print(f"{indent}├─ {item.name}")
    else:
        print(f"{indent}├─ {item.name}/")

# ============ PARTE 7: RICERCA AVANZATA ============

print(f"\n=== RICERCA AVANZATA ===")

def cerca_file(cartella, pattern=None, estensione=None, min_size=0):
    """Cerca file con vari criteri"""
    path = Path(cartella)
    risultati = []

    for file in path.rglob("*"):
        if not file.is_file():
            continue

        # Filtra per pattern
        if pattern and pattern not in file.name:
            continue

        # Filtra per estensione
        if estensione and not file.name.endswith(estensione):
            continue

        # Filtra per dimensione minima
        if file.stat().st_size < min_size:
            continue

        risultati.append(file)

    return risultati

# Cerca file .txt
print("File .txt:")
txt = cerca_file(test_dir, estensione='.txt')
for f in txt:
    print(f"  {f.relative_to(test_dir)} ({f.stat().st_size} bytes)")

# Cerca per pattern
print("\nFile contenenti 'doc':")
doc = cerca_file(test_dir, pattern='doc')
for f in doc:
    print(f"  {f.relative_to(test_dir)}")

# ============ PARTE 8: BACKUP AUTOMATICO ============

print(f"\n=== BACKUP AUTOMATICO ===")

def backup_directory(source, backup_name="backup"):
    """Crea backup di una directory"""
    source = Path(source)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = source.parent / f"{source.name}_{backup_name}_{timestamp}"

    backup.mkdir(parents=True, exist_ok=True)

    # Copia ricorsivamente
    copiati = 0
    for file in source.rglob("*"):
        if file.is_file():
            relative_path = file.relative_to(source)
            destinazione = backup / relative_path
            destinazione.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, destinazione)
            copiati += 1

    print(f"Backup creato: {backup}")
    print(f"File copiati: {copiati}")
    return backup

# Crea backup
backup_path = backup_directory(test_dir)

# ============ PARTE 9: CLEANUP ============

print(f"\n=== CLEANUP ===")

# Elimina directory ricorsivamente
shutil.rmtree(test_dir)
shutil.rmtree(backup_path)
print(f"Eliminate directory di test")
```

---

## 🔍 Casi di Prova (Test)

```python
# Test 1: Creazione Path
def test_path_creazione():
    from pathlib import Path
    p = Path("test.txt")
    assert str(p) == "test.txt"
    print("✓ Test 1 passato: Creazione Path")

# Test 2: Combinazione percorsi
def test_path_combinazione():
    from pathlib import Path
    p = Path("cartella") / "file.txt"
    assert "cartella" in str(p) and "file.txt" in str(p)
    print("✓ Test 2 passato: Combinazione")

# Test 3: Componenti
def test_path_componenti():
    from pathlib import Path
    p = Path("cartella/report.pdf")
    assert p.name == "report.pdf"
    assert p.stem == "report"
    assert p.suffix == ".pdf"
    print("✓ Test 3 passato: Componenti")

# Test 4: Crea e verifica file
def test_file_operazioni():
    from pathlib import Path
    p = Path("test_file.txt")
    p.write_text("test")
    assert p.exists()
    assert p.is_file()
    assert p.read_text() == "test"
    p.unlink()
    print("✓ Test 4 passato: Operazioni file")

# Test 5: Crea e verifica directory
def test_dir_operazioni():
    from pathlib import Path
    p = Path("test_dir")
    p.mkdir(exist_ok=True)
    assert p.exists()
    assert p.is_dir()
    p.rmdir()
    print("✓ Test 5 passato: Operazioni directory")

# Test 6: Glob
def test_glob():
    from pathlib import Path
    p = Path(".")
    py_files = list(p.glob("*.py"))
    assert isinstance(py_files, list)
    print("✓ Test 6 passato: Glob")

# Test 7: Parent
def test_parent():
    from pathlib import Path
    p = Path("cartella/file.txt")
    assert p.parent == Path("cartella")
    print("✓ Test 7 passato: Parent")

# Test 8: Absolute
def test_absolute():
    from pathlib import Path
    p = Path("file.txt")
    abs_p = p.absolute()
    assert abs_p.is_absolute()
    print("✓ Test 8 passato: Absolute")

# Test 9: Iterdir
def test_iterdir():
    from pathlib import Path
    p = Path(".")
    items = list(p.iterdir())
    assert isinstance(items, list)
    assert all(isinstance(i, Path) for i in items)
    print("✓ Test 9 passato: Iterdir")

# Test 10: Stat
def test_stat():
    from pathlib import Path
    p = Path(".")
    stat = p.stat()
    assert hasattr(stat, 'st_size')
    assert hasattr(stat, 'st_mtime')
    print("✓ Test 10 passato: Stat")

if __name__ == "__main__":
    test_path_creazione()
    test_path_combinazione()
    test_path_componenti()
    test_file_operazioni()
    test_dir_operazioni()
    test_glob()
    test_parent()
    test_absolute()
    test_iterdir()
    test_stat()
    print("\n✅ Tutti i test passati!")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Crea Path base
```python
from pathlib import Path
p = Path("file.txt")
```

### Passo 2: Combina percorsi
```python
p = Path("cartella") / "file.txt"
```

### Passo 3: Accedi a componenti
```python
print(p.name)   # file.txt
print(p.stem)   # file
print(p.suffix) # .txt
```

### Passo 4: Leggi e scrivi file
```python
p.write_text("contenuto")
contenuto = p.read_text()
```

### Passo 5: Verifica file/directory
```python
if p.exists() and p.is_file():
    print("File esiste")
```

### Passo 6: Naviga directory
```python
for file in Path(".").iterdir():
    print(file.name)
```

### Passo 7: Usa glob
```python
python_files = Path(".").glob("*.py")
```

---

## 💡 Trucchi e Best Practices

### ✅ Trucco 1: Usa `/` per combinare percorsi
```python
# SBAGLIATO - vecchio stile
path = os.path.join("cartella", "file.txt")

# GIUSTO - pathlib
path = Path("cartella") / "file.txt"
```

### ✅ Trucco 2: Converti Path in stringa se necessario
```python
p = Path("file.txt")
stringa = str(p)  # Converti se necessario per funzioni legacy
```

### ✅ Trucco 3: Usa .relative_to() per percorsi relativi
```python
base = Path("/home/utente")
file = Path("/home/utente/documenti/file.txt")
relativo = file.relative_to(base)  # documenti/file.txt
```

### ✅ Trucco 4: Usa exist_ok per operazioni sicure
```python
cartella.mkdir(exist_ok=True)  # Non errore se esiste
```

### ✅ Trucko 5: Usa stat() per informazioni file
```python
stat = file.stat()
size = stat.st_size
mtime = stat.st_mtime
mode = stat.st_mode
```

### ✅ Trucco 6: Usa rglob() per ricerca ricorsiva
```python
# Tutti i .py ricorsivamente
python_files = Path(".").rglob("*.py")
```

### ✅ Trucco 7: Usa parts per accedere a componenti
```python
p = Path("cartella/sottocartella/file.txt")
print(p.parts)  # ('cartella', 'sottocartella', 'file.txt')
```

### ✅ Trucco 8: Usa match() per pattern matching
```python
p = Path("documento.txt")
if p.match("*.txt"):
    print("È un file txt")
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Usare stringhe invece di Path
```python
# SBAGLIATO
file = "cartella/file.txt"
if os.path.exists(file):  # Vecchio stile
    with open(file) as f:
        contenuto = f.read()

# GIUSTO
file = Path("cartella/file.txt")
if file.exists():
    contenuto = file.read_text()
```

### ❌ Errore 2: Confondere / e os.path.join()
```python
# SBAGLIATO - mix di stili
path = Path("cartella") + "/file.txt"  # Potrebbe fallire!

# GIUSTO
path = Path("cartella") / "file.txt"
```

### ❌ Errore 3: Non usare exist_ok
```python
# SBAGLIATO - errore se esiste
cartella.mkdir()

# GIUSTO - no errore
cartella.mkdir(exist_ok=True)
```

### ❌ Errore 4: Usare open() quando puoi usare metodi Path
```python
# SBAGLIATO - più verboso
with open(file, 'r') as f:
    contenuto = f.read()

# GIUSTO - conciso
contenuto = file.read_text()
```

### ❌ Errore 5: Eliminare directory non vuota con rmdir()
```python
# SBAGLIATO - errore se non vuota
cartella.rmdir()

# GIUSTO - usa shutil.rmtree()
import shutil
shutil.rmtree(cartella)
```

### ❌ Errore 6: Usare glob() quando intendi rglob()
```python
# SBAGLIATO - solo livello attuale
files = Path(".").glob("*.py")

# GIUSTO - ricorsivo
files = Path(".").rglob("*.py")
```

### ❌ Errore 7: Non gestire percorsi Windows
```python
# SBAGLIATO - hardcoded separatore
path = Path("cartella\\file.txt")  # Funziona solo Windows!

# GIUSTO - pathlib gestisce automaticamente
path = Path("cartella") / "file.txt"  # Funziona ovunque
```

### ❌ Errore 8: Confondere .name e .stem
```python
p = Path("file.tar.gz")
print(p.name)    # file.tar.gz
print(p.stem)    # file.tar
print(p.suffix)  # .gz
# Solo il suffisso ULTIMO!
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: File Explorer Avanzato
- Crea un'interfaccia per navigare cartelle
- Mostra informazioni file (dimensione, data, permessi)
- Cerca file con pattern
- Crea visualizzazione ad albero

### 🌟 Sfida 2: Sincronizzatore Cartelle
- Sincronizza due cartelle
- Identifica file nuovo/modificato/eliminato
- Copia solo file nuovi/modificati
- Log delle operazioni

### 🌟 Sfida 3: Organizzatore Intelligente
- Analizza estensioni file
- Organizza per tipo (immagini, video, documenti)
- Rinomina automaticamente per data
- Unisci file duplicati

### 🌟 Sfida 4: Analizzatore Disco
- Calcola spazio usato per cartella
- Trova file grandi
- Visualizza grafico di utilizzo
- Suggerisci file da eliminare

### 🌟 Sfida 5: Gestire Archivi
- Estrai ZIP/TAR
- Crea archivi da cartelle
- Analizza contenuto archivi
- Verifica integrità

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Path** | Oggetto percorso file/directory | `Path("file.txt")` |
| **cwd()** | Directory attuale | `Path.cwd()` |
| **home()** | Directory home utente | `Path.home()` |
| **/**  | Combinazione percorsi | `Path("dir") / "file.txt"` |
| **.name** | Nome completo file | `path.name` → "file.txt" |
| **.stem** | Nome senza estensione | `path.stem` → "file" |
| **.suffix** | Estensione | `path.suffix` → ".txt" |
| **.parent** | Directory padre | `path.parent` |
| **.exists()** | Controlla esistenza | `path.exists()` → bool |
| **.is_file()** | È file? | `path.is_file()` → bool |
| **.is_dir()** | È directory? | `path.is_dir()` → bool |
| **.read_text()** | Leggi testo | `contenuto = path.read_text()` |
| **.write_text()** | Scrivi testo | `path.write_text("...")` |
| **.mkdir()** | Crea directory | `path.mkdir(parents=True)` |
| **.iterdir()** | Elenca contenuto | `for f in path.iterdir()` |
| **.glob()** | Pattern matching | `path.glob("*.txt")` |
| **.rglob()** | Ricerca ricorsiva | `path.rglob("*.py")` |
| **.stat()** | Informazioni file | `size = path.stat().st_size` |
| **.rename()** | Rinomina | `path.rename("nuovo_nome")` |
| **.unlink()** | Elimina file | `path.unlink()` |
| **.rmdir()** | Elimina directory | `path.rmdir()` |

---

## 🔗 Link Utili

### Documentazione Ufficiale
- [pathlib - Python Docs](https://docs.python.org/3/library/pathlib.html)
- [pathlib Guide](https://docs.python.org/3/library/pathlib.html#concrete-paths)
- [os.path Comparison](https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module)

### Tutorial Interattivi
- [Real Python - pathlib](https://realpython.com/python-pathlib/)
- [DataCamp - File System Navigation](https://www.datacamp.com/courses/working-with-the-file-system-in-python)
- [GeeksforGeeks - pathlib](https://www.geeksforgeeks.org/pathlib-module-in-python/)

### Cheat Sheet
- [pathlib Cheat Sheet](https://github.com/chris1610/pbpython/blob/master/notebooks/Pathlib-Cheatsheet.ipynb)
- [Path Methods Reference](https://docs.python.org/3/library/pathlib.html#pure-paths)

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

- [ ] So creare Path da stringhe e directory speciali (home, cwd)
- [ ] So combinare percorsi con l'operatore `/`
- [ ] So accedere ai componenti (name, stem, suffix, parent)
- [ ] So verificare file/directory con exists(), is_file(), is_dir()
- [ ] So leggere/scrivere file con read_text() e write_text()
- [ ] So creare/eliminare directory
- [ ] So navigare directory con iterdir()
- [ ] So cercare file con glob() e rglob()
- [ ] So ottenere informazioni file con stat()
- [ ] Ho testato il codice con i casi di prova forniti
- [ ] Ho provato le sfide bonus
- [ ] Capisco che pathlib è il modo moderno di lavorare con file system

---

**Buon lavoro! 📁 Pathlib rende il file system un oggetto elegante!**

*"Non usare os.path - pathlib è il futuro di Python per la gestione file."*
