# Es9: Composizione - Biblioteca Digitale

## 📊 Informazioni Generali

**Livello:** 🟡 INTERMEDIO
**Durata stimata:** 5-6 ore
**Prerequisiti:** Es1-8 completati, classi e attributi

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Distinguere** tra ereditarietà e composizione
- ✅ **Implementare** relazioni "has-a" (ha un/una)
- ✅ **Creare** classi che contengono altre classi
- ✅ **Progettare** una Biblioteca con Libri
- ✅ **Gestire** liste di oggetti dentro altri oggetti
- ✅ **Implementare** ricerca, filtro e statistica
- ✅ **Capire** quando usare composizione vs ereditarietà

**Concetti fondamentali:**
- Composizione = relazione "has-a" (la Biblioteca ha Libri)
- Ereditarietà = relazione "is-a" (il Cane è un Animale)
- Delega = un oggetto chiede a un altro di fare qualcosa
- Aggregazione = collezione di oggetti

---

## 📖 Descrizione

Nel precedente esercizio hai imparato **l'ereditarietà** (relazione "is-a"). Questo esercizio insegna **la composizione** (relazione "has-a"):

```
Ereditarietà:
Cane is-a Animale (Cane è un tipo di Animale)

Composizione:
Biblioteca has-a Libro (Biblioteca contiene Libri)
```

Questo esercizio crea una **biblioteca digitale** dove:
- `Libro` contiene titolo, autore, ISBN, anno, stato di prestito
- `Biblioteca` contiene molti `Libro` (composizione!)
- La biblioteca può prestare e restituire libri
- Statistiche su libri, autori, anni di pubblicazione

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Libro

**Definisci una classe `Libro` con:**

1. **Attributi:**
   - `titolo` (str) - titolo del libro
   - `autore` (str) - autore principale
   - `isbn` (str) - codice ISBN univoco
   - `anno` (int) - anno di pubblicazione
   - `pagine` (int) - numero di pagine
   - `disponibile` (bool) - se è disponibile per il prestito
   - `prestato_a` (str) - nome di chi lo ha in prestito (None se disponibile)
   - `data_prestito` (datetime) - quando è stato prestato

2. **Metodi:**
   - `__init__(titolo, autore, isbn, anno, pagine)` - costruttore
   - `presta_a(nome_persona)` - marca come prestato
   - `restituisci()` - marca come disponibile
   - `info()` - ritorna stringa con dettagli
   - `è_disponibile()` - True se disponibile
   - `eta_pubblicazione()` - quanti anni dalla pubblicazione
   - `è_classico()` - True se pubblicato più di 50 anni fa

### Parte 2: Classe Biblioteca

**Definisci una classe `Biblioteca` con:**

1. **Attributi:**
   - `nome` (str) - nome della biblioteca
   - `libri` (list) - lista di Libro
   - `indirizzo` (str) - indirizzo fisico

2. **Metodi di Gestione:**
   - `aggiungi_libro(libro)` - aggiunge un libro
   - `rimuovi_libro(isbn)` - rimuove per ISBN
   - `numero_libri()` - quanti libri totali
   - `numero_libri_disponibili()` - quanti si possono prendere
   - `numero_libri_prestati()` - quanti sono in prestito

3. **Metodi di Ricerca:**
   - `cerca_per_titolo(titolo)` - ritorna lista (contiene il titolo)
   - `cerca_per_autore(autore)` - ritorna lista di libri di quell'autore
   - `cerca_per_isbn(isbn)` - ritorna un Libro o None
   - `cerca_per_anno(anno)` - libri pubblicati in quell'anno
   - `libri_di_autore_ordinati(autore)` - libri di autore ordinati per anno

4. **Metodi di Prestito:**
   - `presta_libro(isbn, nome_persona)` - presta un libro disponibile
   - `restituisci_libro(isbn)` - restituisce un libro prestato
   - `libri_prestati_a(nome_persona)` - quali libri ha una persona

5. **Metodi di Statistica:**
   - `anno_pubblicazione_piu_antico()` - anno min
   - `anno_pubblicazione_piu_recente()` - anno max
   - `anno_medio_pubblicazione()` - media degli anni
   - `numero_autori_diversi()` - quanti autori unici
   - `autori_ordine_alfabetico()` - lista di autori ordinata
   - `libro_piu_lungo()` - quale ha più pagine
   - `libro_piu_corto()` - quale ha meno pagine
   - `numero_pagine_totale()` - somma di tutte le pagine
   - `libri_classici()` - ritorna libri pubblicati >50 anni fa

6. **Metodi Informativi:**
   - `elenca_libri()` - stampa info di tutti i libri
   - `info_biblioteca()` - stampa statistiche generali
   - `rapporto_prestiti()` - stampa libri in prestito e a chi

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSI ============

from datetime import datetime

class Libro:
    """Un libro in una biblioteca"""

    def __init__(self, titolo, autore, isbn, anno, pagine):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        self.anno = anno
        self.pagine = pagine
        self.disponibile = True
        self.prestato_a = None
        self.data_prestito = None

    def presta_a(self, nome_persona):
        """Presta il libro a una persona"""
        if not self.disponibile:
            print(f"Errore: {self.titolo} è già prestato a {self.prestato_a}")
            return False

        self.disponibile = False
        self.prestato_a = nome_persona
        self.data_prestito = datetime.now()
        print(f"✓ {self.titolo} prestato a {nome_persona}")
        return True

    def restituisci(self):
        """Restituisce il libro"""
        if self.disponibile:
            print(f"Errore: {self.titolo} non è prestato")
            return False

        self.disponibile = True
        self.prestato_a = None
        self.data_prestito = None
        print(f"✓ {self.titolo} restituito")
        return True

    def info(self):
        """Informazioni sul libro"""
        status = "Disponibile" if self.disponibile else f"Prestato a {self.prestato_a}"
        return (
            f"[{self.isbn}] {self.titolo}\n"
            f"  Autore: {self.autore}\n"
            f"  Anno: {self.anno} ({self.eta_pubblicazione()} anni fa)\n"
            f"  Pagine: {self.pagine}\n"
            f"  Status: {status}"
        )

    def è_disponibile(self):
        return self.disponibile

    def eta_pubblicazione(self):
        """Quanti anni dalla pubblicazione"""
        anno_attuale = datetime.now().year
        return anno_attuale - self.anno

    def è_classico(self):
        """True se pubblicato più di 50 anni fa"""
        return self.eta_pubblicazione() > 50


class Biblioteca:
    """Una biblioteca con molti libri (composizione)"""

    def __init__(self, nome, indirizzo=""):
        self.nome = nome
        self.indirizzo = indirizzo
        self.libri = []  # La Biblioteca CONTIENE Libri (composizione!)

    # ===== GESTIONE LIBRI =====

    def aggiungi_libro(self, libro):
        """Aggiunge un libro alla biblioteca"""
        if self.cerca_per_isbn(libro.isbn):
            print(f"Errore: Libro {libro.isbn} già presente")
            return False
        self.libri.append(libro)
        print(f"✓ Aggiunto {libro.titolo}")
        return True

    def rimuovi_libro(self, isbn):
        """Rimuove un libro per ISBN"""
        libro = self.cerca_per_isbn(isbn)
        if not libro:
            print(f"Errore: Libro {isbn} non trovato")
            return False
        self.libri.remove(libro)
        print(f"✓ Rimosso {libro.titolo}")
        return True

    def numero_libri(self):
        return len(self.libri)

    def numero_libri_disponibili(self):
        return sum(1 for l in self.libri if l.disponibile)

    def numero_libri_prestati(self):
        return sum(1 for l in self.libri if not l.disponibile)

    # ===== RICERCA =====

    def cerca_per_titolo(self, titolo):
        """Cerca libri per titolo (contiene)"""
        return [l for l in self.libri if titolo.lower() in l.titolo.lower()]

    def cerca_per_autore(self, autore):
        """Cerca tutti i libri di un autore"""
        return [l for l in self.libri if l.autore.lower() == autore.lower()]

    def cerca_per_isbn(self, isbn):
        """Cerca un libro per ISBN"""
        for l in self.libri:
            if l.isbn == isbn:
                return l
        return None

    def cerca_per_anno(self, anno):
        """Cerca libri di un anno"""
        return [l for l in self.libri if l.anno == anno]

    def libri_di_autore_ordinati(self, autore):
        """Libri di un autore ordinati per anno"""
        return sorted(self.cerca_per_autore(autore), key=lambda l: l.anno)

    # ===== PRESTITI =====

    def presta_libro(self, isbn, nome_persona):
        """Presta un libro disponibile"""
        libro = self.cerca_per_isbn(isbn)
        if not libro:
            print(f"Errore: Libro {isbn} non trovato")
            return False
        return libro.presta_a(nome_persona)

    def restituisci_libro(self, isbn):
        """Restituisce un libro"""
        libro = self.cerca_per_isbn(isbn)
        if not libro:
            print(f"Errore: Libro {isbn} non trovato")
            return False
        return libro.restituisci()

    def libri_prestati_a(self, nome_persona):
        """Quali libri ha una persona"""
        return [l for l in self.libri if l.prestato_a == nome_persona]

    # ===== STATISTICHE =====

    def anno_pubblicazione_piu_antico(self):
        if not self.libri:
            return None
        return min(l.anno for l in self.libri)

    def anno_pubblicazione_piu_recente(self):
        if not self.libri:
            return None
        return max(l.anno for l in self.libri)

    def anno_medio_pubblicazione(self):
        if not self.libri:
            return 0
        return sum(l.anno for l in self.libri) / len(self.libri)

    def numero_autori_diversi(self):
        autori = set(l.autore for l in self.libri)
        return len(autori)

    def autori_ordine_alfabetico(self):
        autori = sorted(set(l.autore for l in self.libri))
        return autori

    def libro_piu_lungo(self):
        if not self.libri:
            return None
        return max(self.libri, key=lambda l: l.pagine)

    def libro_piu_corto(self):
        if not self.libri:
            return None
        return min(self.libri, key=lambda l: l.pagine)

    def numero_pagine_totale(self):
        return sum(l.pagine for l in self.libri)

    def libri_classici(self):
        """Libri pubblicati più di 50 anni fa"""
        return [l for l in self.libri if l.è_classico()]

    # ===== INFORMAZIONI =====

    def elenca_libri(self):
        """Stampa info di tutti i libri"""
        print(f"\n=== Libri della {self.nome} ===\n")
        for libro in sorted(self.libri, key=lambda l: l.titolo):
            print(libro.info())
            print()

    def info_biblioteca(self):
        """Statistiche generali"""
        return (
            f"\n=== Biblioteca {self.nome} ===\n"
            f"Indirizzo: {self.indirizzo}\n"
            f"Totale libri: {self.numero_libri()}\n"
            f"Disponibili: {self.numero_libri_disponibili()}\n"
            f"Prestati: {self.numero_libri_prestati()}\n"
            f"Autori diversi: {self.numero_autori_diversi()}\n"
            f"Anni pubblicazione: {self.anno_pubblicazione_piu_antico()}-{self.anno_pubblicazione_piu_recente()}\n"
            f"Media anno pubblicazione: {self.anno_medio_pubblicazione():.0f}\n"
            f"Pagine totali: {self.numero_pagine_totale()}\n"
        )

    def rapporto_prestiti(self):
        """Libri in prestito e a chi"""
        print(f"\n=== Rapporto Prestiti {self.nome} ===\n")
        if self.numero_libri_prestati() == 0:
            print("Nessun libro in prestito!\n")
            return

        persone = set(l.prestato_a for l in self.libri if not l.disponibile)
        for persona in sorted(persone):
            libri = self.libri_prestati_a(persona)
            print(f"{persona}:")
            for libro in libri:
                giorni = (datetime.now() - libro.data_prestito).days
                print(f"  - {libro.titolo} ({giorni} giorni)")
            print()


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    # Creare una biblioteca
    biblioteca = Biblioteca("Biblioteca Centrale", "Via Roma 1")

    # Aggiungere libri
    libri_da_aggiungere = [
        Libro("Don Chisciotte", "Miguel de Cervantes", "ISBN001", 1605, 1072),
        Libro("1984", "George Orwell", "ISBN002", 1949, 328),
        Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "ISBN003", 1954, 1178),
        Libro("Orgoglio e Pregiudizio", "Jane Austen", "ISBN004", 1813, 432),
        Libro("Il Grande Gatsby", "F. Scott Fitzgerald", "ISBN005", 1925, 180),
        Libro("La Fattoria degli Animali", "George Orwell", "ISBN006", 1945, 141),
        Libro("Cento Anni di Solitudine", "Gabriel García Márquez", "ISBN007", 1967, 417),
        Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling", "ISBN008", 1998, 309),
    ]

    for libro in libri_da_aggiungere:
        biblioteca.aggiungi_libro(libro)

    # Mostrare la biblioteca
    print(biblioteca.info_biblioteca())

    # Test ricerca
    print("=== RICERCA PER AUTORE (Orwell) ===")
    orwell = biblioteca.cerca_per_autore("George Orwell")
    for libro in orwell:
        print(f"  - {libro.titolo} ({libro.anno})")

    # Test prestiti
    print("\n=== TEST PRESTITI ===")
    biblioteca.presta_libro("ISBN001", "Marco")
    biblioteca.presta_libro("ISBN003", "Marco")
    biblioteca.presta_libro("ISBN005", "Laura")

    # Mostrare prestiti
    biblioteca.rapporto_prestiti()

    # Test statistiche
    print("=== STATISTICHE ===")
    print(f"Libro più lungo: {biblioteca.libro_piu_lungo().titolo} ({biblioteca.libro_piu_lungo().pagine} pagine)")
    print(f"Libro più corto: {biblioteca.libro_piu_corto().titolo} ({biblioteca.libro_piu_corto().pagine} pagine)")
    print(f"Libri classici (>50 anni): {len(biblioteca.libri_classici())}")
    print(f"Autori: {', '.join(biblioteca.autori_ordine_alfabetico())}")

    # Output atteso:
    # === Biblioteca Centrale ===
    # Indirizzo: Via Roma 1
    # Totale libri: 8
    # Disponibili: 5
    # Prestati: 3
    # ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Creazione Libro
```python
libro = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
assert libro.titolo == "1984"
assert libro.autore == "George Orwell"
assert libro.è_disponibile() == True
print("✓ Test 1 passato")
```

### Test 2: Prestito Libro
```python
libro = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
assert libro.presta_a("Marco") == True
assert libro.è_disponibile() == False
assert libro.prestato_a == "Marco"
assert libro.presta_a("Laura") == False  # È già prestato!
print("✓ Test 2 passato")
```

### Test 3: Restituzione Libro
```python
libro = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
libro.presta_a("Marco")
assert libro.restituisci() == True
assert libro.è_disponibile() == True
assert libro.prestato_a == None
print("✓ Test 3 passato")
```

### Test 4: Composizione - Biblioteca contiene Libri
```python
biblioteca = Biblioteca("Test Library")
libro1 = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
libro2 = Libro("Dune", "Frank Herbert", "ISBN002", 1965, 688)

assert biblioteca.numero_libri() == 0
biblioteca.aggiungi_libro(libro1)
assert biblioteca.numero_libri() == 1
biblioteca.aggiungi_libro(libro2)
assert biblioteca.numero_libri() == 2
print("✓ Test 4 passato")
```

### Test 5: Ricerca per ISBN
```python
biblioteca = Biblioteca("Test Library")
libro = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
biblioteca.aggiungi_libro(libro)

trovato = biblioteca.cerca_per_isbn("ISBN001")
assert trovato == libro
assert trovato.titolo == "1984"

non_trovato = biblioteca.cerca_per_isbn("ISBN999")
assert non_trovato == None
print("✓ Test 5 passato")
```

### Test 6: Ricerca per Autore
```python
biblioteca = Biblioteca("Test Library")
libro1 = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
libro2 = Libro("La Fattoria degli Animali", "George Orwell", "ISBN002", 1945, 141)
libro3 = Libro("Dune", "Frank Herbert", "ISBN003", 1965, 688)

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)

orwell = biblioteca.cerca_per_autore("George Orwell")
assert len(orwell) == 2
assert libro1 in orwell
assert libro2 in orwell
print("✓ Test 6 passato")
```

### Test 7: Prestito da Biblioteca
```python
biblioteca = Biblioteca("Test Library")
libro = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
biblioteca.aggiungi_libro(libro)

assert biblioteca.numero_libri_disponibili() == 1
assert biblioteca.numero_libri_prestati() == 0

biblioteca.presta_libro("ISBN001", "Marco")
assert biblioteca.numero_libri_disponibili() == 0
assert biblioteca.numero_libri_prestati() == 1
print("✓ Test 7 passato")
```

### Test 8: Libri prestati a una persona
```python
biblioteca = Biblioteca("Test Library")
libro1 = Libro("1984", "George Orwell", "ISBN001", 1949, 328)
libro2 = Libro("Dune", "Frank Herbert", "ISBN002", 1965, 688)
libro3 = Libro("Harry Potter", "J.K. Rowling", "ISBN003", 1998, 309)

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)

biblioteca.presta_libro("ISBN001", "Marco")
biblioteca.presta_libro("ISBN002", "Marco")
biblioteca.presta_libro("ISBN003", "Laura")

marco_libri = biblioteca.libri_prestati_a("Marco")
assert len(marco_libri) == 2
assert libro1 in marco_libri
assert libro2 in marco_libri
print("✓ Test 8 passato")
```

### Test 9: Statistiche
```python
biblioteca = Biblioteca("Test Library")
libro1 = Libro("Antico", "Autore1", "ISBN001", 1900, 300)
libro2 = Libro("Recente", "Autore2", "ISBN002", 2020, 400)
libro3 = Libro("Medio", "Autore3", "ISBN003", 1950, 500)

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)

assert biblioteca.anno_pubblicazione_piu_antico() == 1900
assert biblioteca.anno_pubblicazione_piu_recente() == 2020
assert biblioteca.numero_autori_diversi() == 3
assert biblioteca.numero_pagine_totale() == 1200
print("✓ Test 9 passato")
```

### Test 10: Libri classici
```python
from datetime import datetime

anno_attuale = datetime.now().year
biblioteca = Biblioteca("Test Library")
libro1 = Libro("Classico", "Autore1", "ISBN001", anno_attuale - 60, 300)
libro2 = Libro("Recente", "Autore2", "ISBN002", anno_attuale - 5, 400)

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)

classici = biblioteca.libri_classici()
assert len(classici) == 1
assert libro1 in classici
print("✓ Test 10 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Crea la classe Libro
```python
class Libro:
    def __init__(self, titolo, autore, isbn, anno, pagine):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        self.anno = anno
        self.pagine = pagine
        self.disponibile = True
        self.prestato_a = None
```

### Passo 2: Aggiungi metodi di prestito a Libro
```python
def presta_a(self, nome_persona):
    if not self.disponibile:
        return False
    self.disponibile = False
    self.prestato_a = nome_persona
    return True

def restituisci(self):
    if self.disponibile:
        return False
    self.disponibile = True
    self.prestato_a = None
    return True
```

### Passo 3: Aggiungi metodi di utilità a Libro
```python
def è_disponibile(self):
    return self.disponibile

def eta_pubblicazione(self):
    return datetime.now().year - self.anno

def è_classico(self):
    return self.eta_pubblicazione() > 50
```

### Passo 4: Crea la classe Biblioteca
```python
class Biblioteca:
    def __init__(self, nome, indirizzo=""):
        self.nome = nome
        self.indirizzo = indirizzo
        self.libri = []  # Contiene Libri (composizione!)
```

### Passo 5: Aggiungi metodi di gestione libri
```python
def aggiungi_libro(self, libro):
    if self.cerca_per_isbn(libro.isbn):
        return False
    self.libri.append(libro)
    return True

def numero_libri(self):
    return len(self.libri)

def numero_libri_disponibili(self):
    return sum(1 for l in self.libri if l.disponibile)
```

### Passo 6: Aggiungi metodi di ricerca
```python
def cerca_per_isbn(self, isbn):
    for l in self.libri:
        if l.isbn == isbn:
            return l
    return None

def cerca_per_autore(self, autore):
    return [l for l in self.libri if l.autore == autore]

def cerca_per_titolo(self, titolo):
    return [l for l in self.libri if titolo in l.titolo]
```

### Passo 7: Aggiungi metodi di prestito
```python
def presta_libro(self, isbn, nome_persona):
    libro = self.cerca_per_isbn(isbn)
    if not libro:
        return False
    return libro.presta_a(nome_persona)

def restituisci_libro(self, isbn):
    libro = self.cerca_per_isbn(isbn)
    if not libro:
        return False
    return libro.restituisci()
```

### Passo 8: Aggiungi metodi di statistica
```python
def numero_autori_diversi(self):
    return len(set(l.autore for l in self.libri))

def anno_medio_pubblicazione(self):
    return sum(l.anno for l in self.libri) / len(self.libri)

def libri_classici(self):
    return [l for l in self.libri if l.è_classico()]
```

---

## 💡 Trucchi e Best Practices

### ✅ Composizione vs Ereditarietà
```python
# COMPOSIZIONE (has-a): Biblioteca HA Libri
class Biblioteca:
    def __init__(self):
        self.libri = []  # Contiene oggetti Libro

# Non dovresti fare:
# class Biblioteca(Libro):  # Biblioteca è un Libro? NO!
#     pass

# EREDITARIETÀ (is-a): Cane è un Animale
class Animale: pass
class Cane(Animale):  # Cane è un tipo di Animale
    pass
```

### ✅ Delega a oggetti contenuti
```python
# BUONO - la Biblioteca delega al Libro
class Biblioteca:
    def presta_libro(self, isbn, persona):
        libro = self.cerca_per_isbn(isbn)
        return libro.presta_a(persona)  # Delega!

# CATTIVO - duplica il codice
class Biblioteca:
    def presta_libro(self, isbn, persona):
        libro = self.cerca_per_isbn(isbn)
        if not libro.disponibile:
            return False
        libro.disponibile = False
        libro.prestato_a = persona
        # Ripete il codice che è già in Libro.presta_a()
```

### ✅ Usa `datetime` per tracciare tempo
```python
from datetime import datetime

class Libro:
    def __init__(self, ...):
        self.data_prestito = None

    def presta_a(self, persona):
        self.data_prestito = datetime.now()
        # Ora puoi calcolare:
        # giorni = (datetime.now() - self.data_prestito).days
```

### ✅ Ricerca con list comprehension
```python
# BUONO - conciso e leggibile
def cerca_per_autore(self, autore):
    return [l for l in self.libri if l.autore == autore]

# CATTIVO - più verboso
def cerca_per_autore(self, autore):
    risultati = []
    for libro in self.libri:
        if libro.autore == autore:
            risultati.append(libro)
    return risultati
```

### ✅ Usa `max()` e `min()` con `key`
```python
# BUONO - conciso
piu_lungo = max(self.libri, key=lambda l: l.pagine)
piu_corto = min(self.libri, key=lambda l: l.pagine)

# CATTIVO - più verboso
piu_lungo = None
for l in self.libri:
    if piu_lungo is None or l.pagine > piu_lungo.pagine:
        piu_lungo = l
```

### ✅ Ricerca singola vs multipla
```python
# Singola istanza (ritorna Libro o None)
def cerca_per_isbn(self, isbn):
    for l in self.libri:
        if l.isbn == isbn:
            return l
    return None

# Multipli (ritorna lista)
def cerca_per_autore(self, autore):
    return [l for l in self.libri if l.autore == autore]
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Usare ereditarietà quando serve composizione
```python
# SBAGLIATO - Biblioteca non è un tipo di Libro
class Biblioteca(Libro):
    def __init__(self, nome):
        super().__init__("Biblioteca", "", "", 0, 0)
        self.libri = []

# GIUSTO - Biblioteca contiene Libri
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []  # Composizione!
```

### ❌ Errore 2: Dimenticare che lista contiene riferimenti
```python
# SBAGLIATO - il libro fuori dalla lista non è aggiornato
libro = Libro("1984", "Orwell", "ISBN001", 1949, 328)
biblioteca.aggiungi_libro(libro)
# Se modifico `libro`, anche nella biblioteca è modificato!
libro.disponibile = False
# Ora in biblioteca è falso anche se non è nel prestito della biblioteca

# GIUSTO - questo comportamento è corretto in Python!
# Perché biblioteca contiene un riferimento allo stesso oggetto
# Se vuoi una copia indipendente, fai deepcopy:
import copy
libro_copia = copy.deepcopy(libro)
```

### ❌ Errore 3: Ricerca che ritorna elemento invece di lista
```python
# SBAGLIATO - inconsistente
def cerca_per_titolo(self, titolo):
    for l in self.libri:
        if titolo in l.titolo:
            return l  # Ritorna un elemento!

# GIUSTO - sempre list comprehension per ricerche multiple
def cerca_per_titolo(self, titolo):
    return [l for l in self.libri if titolo in l.titolo]  # Lista!
```

### ❌ Errore 4: Non gestire il caso vuoto
```python
# SBAGLIATO - crash se lista vuota
def libro_piu_lungo(self):
    return max(self.libri, key=lambda l: l.pagine)  # IndexError se vuota!

# GIUSTO - controlla se vuota
def libro_piu_lungo(self):
    if not self.libri:
        return None
    return max(self.libri, key=lambda l: l.pagine)
```

### ❌ Errore 5: Confronto di stringhe case-sensitive
```python
# SBAGLIATO - "George Orwell" != "george orwell"
def cerca_per_autore(self, autore):
    return [l for l in self.libri if l.autore == autore]

# GIUSTO - lowercase per entrambi
def cerca_per_autore(self, autore):
    return [l for l in self.libri if l.autore.lower() == autore.lower()]
```

### ❌ Errore 6: Modificare lista mentre la iteriamo
```python
# SBAGLIATO - modifica lista mentre iteriamo
for libro in self.libri:
    if libro.è_classico():
        self.libri.remove(libro)  # Modifica durante iterazione!

# GIUSTO - creiamo una nuova lista
def rimuovi_classici(self):
    self.libri = [l for l in self.libri if not l.è_classico()]
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Sistema di Prenotazioni
```python
class Libro:
    def __init__(self, ...):
        self.prenotazioni = []  # Lista di nomi che prenotano

    def prenota(self, nome_persona):
        """Prenota un libro per quando disponibile"""
        self.prenotazioni.append(nome_persona)
        return True

    def avvisa_prenotante(self):
        """Ritorna il prossimo che lo ha prenotato"""
        if self.prenotazioni:
            return self.prenotazioni.pop(0)
        return None

class Biblioteca:
    def prenota_libro(self, isbn, nome_persona):
        libro = self.cerca_per_isbn(isbn)
        if not libro:
            return False
        return libro.prenota(nome_persona)
```

### 🌟 Sfida 2: Storico Prestiti
```python
from datetime import datetime

class Libro:
    def __init__(self, ...):
        self.storico_prestiti = []  # [(persona, data_inizio, data_fine), ...]

    def presta_a(self, nome_persona):
        if not self.disponibile:
            return False
        self.disponibile = False
        self.prestato_a = nome_persona
        self.data_prestito = datetime.now()
        return True

    def restituisci(self):
        if self.disponibile:
            return False
        # Aggiungi al storico
        self.storico_prestiti.append((
            self.prestato_a,
            self.data_prestito,
            datetime.now()
        ))
        self.disponibile = True
        self.prestato_a = None
        self.data_prestito = None
        return True

    def numero_volte_prestato(self):
        return len(self.storico_prestiti)
```

### 🌟 Sfida 3: Rating e Recensioni
```python
class Libro:
    def __init__(self, ...):
        self.rating = 0
        self.numero_voti = 0
        self.recensioni = []

    def aggiungi_rating(self, voto):
        """Voto da 1 a 5"""
        if 1 <= voto <= 5:
            self.rating = (self.rating * self.numero_voti + voto) / (self.numero_voti + 1)
            self.numero_voti += 1
            return True
        return False

    def aggiungi_recensione(self, testo):
        self.recensioni.append(testo)

    def rating_medio(self):
        return round(self.rating, 1)
```

### 🌟 Sfida 4: Generi e Tag
```python
class Libro:
    def __init__(self, ..., genere="Fiction"):
        self.genere = genere
        self.tag = []  # ["fantasy", "avventura", ...]

    def aggiungi_tag(self, tag):
        if tag not in self.tag:
            self.tag.append(tag)

class Biblioteca:
    def cerca_per_genere(self, genere):
        return [l for l in self.libri if l.genere == genere]

    def cerca_per_tag(self, tag):
        return [l for l in self.libri if tag in l.tag]

    def libri_correlati(self, isbn):
        """Suggerimenti basati su genere e tag"""
        libro = self.cerca_per_isbn(isbn)
        if not libro:
            return []
        return [
            l for l in self.libri
            if l.isbn != isbn and (l.genere == libro.genere or any(t in l.tag for t in libro.tag))
        ]
```

### 🌟 Sfida 5: Esportazione Dati
```python
import json
from datetime import datetime

class Biblioteca:
    def esporta_json(self, nome_file):
        """Salva la biblioteca in JSON"""
        dati = {
            "nome": self.nome,
            "indirizzo": self.indirizzo,
            "libri": [
                {
                    "titolo": l.titolo,
                    "autore": l.autore,
                    "isbn": l.isbn,
                    "anno": l.anno,
                    "pagine": l.pagine,
                    "disponibile": l.disponibile,
                    "prestato_a": l.prestato_a
                }
                for l in self.libri
            ]
        }
        with open(nome_file, 'w', encoding='utf-8') as f:
            json.dump(dati, f, indent=2, ensure_ascii=False)

    @classmethod
    def carica_json(cls, nome_file):
        """Carica una biblioteca da JSON"""
        with open(nome_file, 'r', encoding='utf-8') as f:
            dati = json.load(f)

        biblioteca = cls(dati["nome"], dati.get("indirizzo", ""))
        for l_data in dati.get("libri", []):
            libro = Libro(
                l_data["titolo"],
                l_data["autore"],
                l_data["isbn"],
                l_data["anno"],
                l_data["pagine"]
            )
            if not l_data.get("disponibile", True):
                libro.disponibile = False
                libro.prestato_a = l_data.get("prestato_a")
            biblioteca.aggiungi_libro(libro)
        return biblioteca
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Esempio |
|----------|-------------|---------|
| **Composizione** | Relazione "has-a" (contiene) | Biblioteca ha Libri |
| **Ereditarietà** | Relazione "is-a" (tipo di) | Cane è un Animale |
| **Delega** | Un oggetto chiede a un altro di fare | Biblioteca → Libro |
| **Aggregazione** | Collezione di oggetti | Lista di Libri |
| **Ricerca singola** | Ritorna un oggetto o None | cerca_per_isbn() |
| **Ricerca multipla** | Ritorna una lista | cerca_per_autore() |
| **Statistica** | Calcoli su intera collezione | numero_autori_diversi() |

---

## 🔗 Link Utili

### Documentazione
- [Python Collections](https://docs.python.org/3/library/collections.html)
- [datetime Module](https://docs.python.org/3/library/datetime.html)
- [json Module](https://docs.python.org/3/library/json.html)

### Tutorial
- [Real Python - Composition vs Inheritance](https://realpython.com/inheritance-composition-python/)
- [OOP Design Patterns](https://www.geeksforgeeks.org/design-patterns-in-python/)
- [Data Structures in Python](https://docs.python.org/3/tutorial/datastructures.html)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Osserva come sono implementati i metodi di ricerca
- Guarda come sono gestite le liste di oggetti
- Nota i pattern di statistica e aggregazione
- Apprendi dall'uso di datetime e date tracking

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho creato la classe `Libro` con tutti gli attributi
- [ ] Ho implementato metodi di prestito in Libro
- [ ] Ho implementato metodi di utilità in Libro (eta, è_classico)
- [ ] Ho creato la classe `Biblioteca` (composizione!)
- [ ] La Biblioteca contiene una lista di Libri
- [ ] Ho implementato metodi di gestione (aggiungi, rimuovi)
- [ ] Ho implementato ricerca per ISBN (singola)
- [ ] Ho implementato ricerca per autore (multipla)
- [ ] Ho implementato ricerca per titolo (multipla)
- [ ] Ho implementato metodi di prestito nella Biblioteca
- [ ] Ho implementato metodi di statistica
- [ ] Ho implementato libri_classici()
- [ ] Ho testato con almeno 8 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai padroneggiato la composizione! 🎉📚**

*"La composizione è come dire: 'Questa classe ha una relazione con un'altra classe, non ne è un tipo'"*
