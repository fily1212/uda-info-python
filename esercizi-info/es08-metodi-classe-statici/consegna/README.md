# Es8: Metodi di Classe e Statici - Catalogo Prodotti

## 📊 Informazioni Generali

**Livello:** 🟡 INTERMEDIO
**Durata stimata:** 5-6 ore
**Prerequisiti:** Es1-7 completati, classi e ereditarietà

---

## 🎯 Cosa Imparerai

In questo esercizio imparerai a:
- ✅ **Distinguere** tra metodi di istanza, metodi di classe e metodi statici
- ✅ **Usare** `@staticmethod` per funzioni pure senza stato
- ✅ **Usare** `@classmethod` per logica a livello di classe
- ✅ **Creare** factory methods con `@classmethod`
- ✅ **Gestire** attributi di classe condivisi tra istanze
- ✅ **Implementare** logica di validazione globale
- ✅ **Contare** istanze di una classe

**Concetti fondamentali:**
- Metodo di istanza: accede a `self` (dati dell'oggetto)
- Metodo di classe: accede a `cls` (dati della classe)
- Metodo statico: nessun accesso a `self` o `cls` (funzione pura)
- Attributo di classe: condiviso tra tutte le istanze
- Factory method: metodo per creare oggetti specializzati

---

## 📖 Descrizione

Finora hai creato metodi che accedevano agli attributi dell'istanza (`self`). Ma a volte devi:

1. **Metodi statici** - funzioni pure non legate all'istanza (es: validare un codice)
2. **Metodi di classe** - logica che riguarda la classe nel complesso (es: contare quante istanze)
3. **Attributi di classe** - dati condivisi tra tutte le istanze (es: IVA standard)

Questo esercizio crea un **catalogo di prodotti** dove:
- Ogni prodotto traccia il numero di istanze create
- Metodi statici validano codici e calcolano sconti
- Metodi di classe leggono da dizionari e contano prodotti
- Attributi di classe sono condivisi (IVA, contatori)

---

## 📝 Consegna Dettagliata

### Parte 1: Classe Prodotto Base

**Definisci una classe `Prodotto` con:**

1. **Attributi di classe (condivisi):**
   - `contatore_prodotti` (int) - numero totale di istanze create
   - `iva_default` (float) - 0.22 (22% IVA standard)
   - `sconto_quantita` (dict) - `{10: 0.05, 50: 0.10, 100: 0.20}` (5% da 10 pezzi, 10% da 50, ecc.)

2. **Attributi di istanza:**
   - `codice` (str) - identificativo unico (es: "PROD001")
   - `nome` (str) - nome del prodotto
   - `prezzo` (float) - prezzo in euro
   - `quantita` (int) - quantità in magazzino
   - `descrizione` (str) - descrizione breve

3. **Metodo `__init__`:**
   - Incrementa `contatore_prodotti`
   - Inizializza gli attributi
   - Valida il codice con `@staticmethod valida_codice()`

### Parte 2: Metodi Statici

**Implementa metodi con `@staticmethod`:**

1. **`valida_codice(codice)`**
   - Ritorna True se è stringa di forma "PROD" + 3 cifre (es: "PROD001")
   - Ritorna False altrimenti
   - Non accede a `self` né `cls`

2. **`calcola_sconto(quantita, prezzo)`**
   - Riceve quantità e prezzo
   - Ritorna il prezzo scontato in base a quantità
   - Usa le soglie in `sconto_quantita`
   - Es: 50 pezzi da 10€ = sconto 10% → 450€

3. **`formatta_prezzo(prezzo)`**
   - Ritorna stringa formattata: "€ 49.99"
   - Con 2 decimali, simbolo €

4. **`valida_email(email)`**
   - Ritorna True se email contiene "@" e "."
   - Ritorna False altrimenti

### Parte 3: Metodi di Classe

**Implementa metodi con `@classmethod`:**

1. **`crea_da_dict(cls, dati)`** - Factory method
   - Riceve dizionario con chiavi: codice, nome, prezzo, quantita, descrizione
   - Crea e ritorna un'istanza di Prodotto
   - Utile per caricare da file JSON

2. **`crea_da_csv(cls, riga_csv)`** - Factory method
   - Riceve stringa CSV: "PROD001,Mela,5.50,100,Frutta fresca"
   - Splitta, crea Prodotto, ritorna istanza

3. **`conta_prodotti(cls)`**
   - Ritorna il numero totale di Prodotto creati
   - Accede a `cls.contatore_prodotti`

4. **`cambia_iva(cls, nuova_iva)`**
   - Cambia l'IVA globale per tutti i prodotti
   - Es: `Prodotto.cambia_iva(0.10)` per 10%

5. **`aggiungi_soglia_sconto(cls, quantita, percentuale)`**
   - Aggiunge una nuova soglia di sconto
   - Es: `Prodotto.aggiungi_soglia_sconto(200, 0.25)` per 25% da 200 pezzi

### Parte 4: Metodi di Istanza

1. **`info()`** - ritorna stringa con dettagli
2. **`prezzo_con_iva()`** - prezzo * (1 + IVA)
3. **`prezzo_scontato(quantita)`** - prezzo scontato per quella quantità
4. **`valore_magazzino()`** - prezzo * quantita
5. **`aumenta_quantita(n)`** - aggiunge n pezzi
6. **`diminuisci_quantita(n)`** - rimuove n pezzi (min 0)

### Parte 5: Catalogo

**Crea una classe `Catalogo` per gestire prodotti:**

1. **Attributi:**
   - `nome` (str) - nome del catalogo
   - `prodotti` (dict) - `{codice: Prodotto, ...}`

2. **Metodi:**
   - `aggiungi_prodotto(prodotto)` - aggiunge al catalogo
   - `cerca_per_codice(codice)` - ritorna Prodotto o None
   - `cerca_per_nome(nome)` - ritorna lista di Prodotti che contengono nome
   - `valore_totale_magazzino()` - somma di valore_magazzino() di tutti
   - `prodotto_piu_caro()` - quale costa di più
   - `prodotto_piu_economico()` - quale costa di meno
   - `numero_tipi_prodotti()` - quanti tipi (ma non quantità)
   - `numero_pezzi_totali()` - somma di tutte le quantità
   - `applica_sconto_globale(percentuale)` - sconta tutti di una %

---

## 💻 Esempio di Utilizzo Completo

```python
# ============ DEFINIZIONE CLASSI ============

class Prodotto:
    """Catalogo di prodotti con metodi statici e di classe"""

    # ATTRIBUTI DI CLASSE
    contatore_prodotti = 0
    iva_default = 0.22  # 22% IVA
    sconto_quantita = {10: 0.05, 50: 0.10, 100: 0.20}

    def __init__(self, codice, nome, prezzo, quantita, descrizione=""):
        # Valida il codice
        if not Prodotto.valida_codice(codice):
            raise ValueError(f"Codice invalido: {codice}")

        # Attributi di istanza
        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        self.descrizione = descrizione

        # Incrementa il contatore
        Prodotto.contatore_prodotti += 1

    # ===== METODI STATICI (@staticmethod) =====

    @staticmethod
    def valida_codice(codice):
        """Valida formato codice PRODXXX"""
        if not isinstance(codice, str):
            return False
        if len(codice) != 7:
            return False
        if not codice.startswith("PROD"):
            return False
        return codice[4:].isdigit()

    @staticmethod
    def calcola_sconto(quantita, prezzo):
        """Calcola prezzo scontato in base a quantità"""
        sconto = 0
        for soglia in sorted(Prodotto.sconto_quantita.keys()):
            if quantita >= soglia:
                sconto = Prodotto.sconto_quantita[soglia]
        return prezzo * quantita * (1 - sconto)

    @staticmethod
    def formatta_prezzo(prezzo):
        """Formatta prezzo con simbolo euro"""
        return f"€ {prezzo:.2f}"

    @staticmethod
    def valida_email(email):
        """Valida se è un'email"""
        return "@" in email and "." in email

    # ===== METODI DI CLASSE (@classmethod) =====

    @classmethod
    def crea_da_dict(cls, dati):
        """Factory method - crea da dizionario"""
        return cls(
            dati["codice"],
            dati["nome"],
            dati["prezzo"],
            dati["quantita"],
            dati.get("descrizione", "")
        )

    @classmethod
    def crea_da_csv(cls, riga_csv):
        """Factory method - crea da stringa CSV"""
        parti = riga_csv.split(",")
        return cls(
            parti[0].strip(),
            parti[1].strip(),
            float(parti[2].strip()),
            int(parti[3].strip()),
            parti[4].strip() if len(parti) > 4 else ""
        )

    @classmethod
    def conta_prodotti(cls):
        """Ritorna numero totale di prodotti creati"""
        return cls.contatore_prodotti

    @classmethod
    def cambia_iva(cls, nuova_iva):
        """Cambia l'IVA globale"""
        cls.iva_default = nuova_iva
        print(f"IVA cambiata a {nuova_iva*100}%")

    @classmethod
    def aggiungi_soglia_sconto(cls, quantita, percentuale):
        """Aggiunge una nuova soglia di sconto"""
        cls.sconto_quantita[quantita] = percentuale
        print(f"Aggiunta soglia: {quantita} pezzi → {percentuale*100}% sconto")

    # ===== METODI DI ISTANZA =====

    def info(self):
        """Informazioni sul prodotto"""
        return (
            f"[{self.codice}] {self.nome}\n"
            f"  Prezzo: {Prodotto.formatta_prezzo(self.prezzo)}\n"
            f"  Quantità: {self.quantita}\n"
            f"  Descrizione: {self.descrizione}"
        )

    def prezzo_con_iva(self):
        """Prezzo comprensivo di IVA"""
        return self.prezzo * (1 + Prodotto.iva_default)

    def prezzo_scontato(self, quantita):
        """Prezzo per una certa quantità con sconto"""
        return Prodotto.calcola_sconto(quantita, self.prezzo)

    def valore_magazzino(self):
        """Valore totale del prodotto in magazzino"""
        return self.prezzo * self.quantita

    def aumenta_quantita(self, n):
        """Aggiunge pezzi"""
        if n < 0:
            return False
        self.quantita += n
        return True

    def diminuisci_quantita(self, n):
        """Rimuove pezzi"""
        if n < 0:
            return False
        self.quantita = max(0, self.quantita - n)
        return True


class Catalogo:
    """Catalogo di prodotti"""

    def __init__(self, nome):
        self.nome = nome
        self.prodotti = {}  # {codice: Prodotto}

    def aggiungi_prodotto(self, prodotto):
        """Aggiunge un prodotto al catalogo"""
        self.prodotti[prodotto.codice] = prodotto

    def cerca_per_codice(self, codice):
        """Cerca un prodotto per codice"""
        return self.prodotti.get(codice)

    def cerca_per_nome(self, nome):
        """Cerca prodotti per nome (contains)"""
        return [p for p in self.prodotti.values() if nome.lower() in p.nome.lower()]

    def valore_totale_magazzino(self):
        """Valore totale di tutto il magazzino"""
        return sum(p.valore_magazzino() for p in self.prodotti.values())

    def prodotto_piu_caro(self):
        """Prodotto con prezzo più alto"""
        if not self.prodotti:
            return None
        return max(self.prodotti.values(), key=lambda p: p.prezzo)

    def prodotto_piu_economico(self):
        """Prodotto con prezzo più basso"""
        if not self.prodotti:
            return None
        return min(self.prodotti.values(), key=lambda p: p.prezzo)

    def numero_tipi_prodotti(self):
        """Numero di tipi (righe) di prodotti"""
        return len(self.prodotti)

    def numero_pezzi_totali(self):
        """Numero totale di pezzi"""
        return sum(p.quantita for p in self.prodotti.values())

    def applica_sconto_globale(self, percentuale):
        """Sconta tutti i prodotti di una percentuale"""
        for prodotto in self.prodotti.values():
            prodotto.prezzo *= (1 - percentuale)
        print(f"Sconto del {percentuale*100}% applicato a tutti i prodotti")

    def info_catalogo(self):
        """Informazioni sul catalogo"""
        return (
            f"\n=== Catalogo {self.nome} ===\n"
            f"Tipi di prodotto: {self.numero_tipi_prodotti()}\n"
            f"Pezzi totali: {self.numero_pezzi_totali()}\n"
            f"Valore magazzino: {Prodotto.formatta_prezzo(self.valore_totale_magazzino())}\n"
        )


# ============ PROGRAMMA PRINCIPALE ============

if __name__ == "__main__":
    # Creare alcuni prodotti
    p1 = Prodotto("PROD001", "Mela", 0.50, 100, "Frutta fresca")
    p2 = Prodotto("PROD002", "Pane", 2.50, 50, "Pane integrale")
    p3 = Prodotto("PROD003", "Latte", 1.50, 80, "Latte intero")

    # Usando factory method da dizionario
    p4 = Prodotto.crea_da_dict({
        "codice": "PROD004",
        "nome": "Formaggio",
        "prezzo": 5.00,
        "quantita": 30,
        "descrizione": "Parmigiano"
    })

    # Usando factory method da CSV
    p5 = Prodotto.crea_da_csv("PROD005,Uova,0.15,200,Uova fresche")

    print("=== METODI STATICI ===")
    print(f"Valida 'PROD001': {Prodotto.valida_codice('PROD001')}")
    print(f"Valida 'INVALIDO': {Prodotto.valida_codice('INVALIDO')}")
    print(f"Prezzo formattato: {Prodotto.formatta_prezzo(10.5)}")
    print(f"Sconto 50 pezzi da €0.50: {Prodotto.formatta_prezzo(Prodotto.calcola_sconto(50, 0.50))}")

    print("\n=== METODI DI CLASSE ===")
    print(f"Numero prodotti creati: {Prodotto.conta_prodotti()}")
    print(f"IVA attuale: {Prodotto.iva_default*100}%")

    print("\n=== CATALOGO ===")
    catalogo = Catalogo("Negozio di Frutta e Verdura")
    for p in [p1, p2, p3, p4, p5]:
        catalogo.aggiungi_prodotto(p)

    print(catalogo.info_catalogo())

    print("Prodotto più caro:", catalogo.prodotto_piu_caro().nome, "-", Prodotto.formatta_prezzo(catalogo.prodotto_piu_caro().prezzo))
    print("Prodotto più economico:", catalogo.prodotto_piu_economico().nome, "-", Prodotto.formatta_prezzo(catalogo.prodotto_piu_economico().prezzo))

    print("\n=== RICERCA ===")
    cerca_mela = catalogo.cerca_per_nome("Mela")
    print(f"Trovati {len(cerca_mela)} prodotti con 'Mela'")

    # Output atteso:
    # === METODI STATICI ===
    # Valida 'PROD001': True
    # Valida 'INVALIDO': False
    # Prezzo formattato: € 10.50
    # Sconto 50 pezzi da €0.50: € 22.50
    # ...
```

---

## 🔍 Casi di Prova (Test)

### Test 1: Metodo statico - Validazione codice
```python
assert Prodotto.valida_codice("PROD001") == True
assert Prodotto.valida_codice("PROD999") == True
assert Prodotto.valida_codice("INVALID") == False
assert Prodotto.valida_codice("PROD00A") == False
assert Prodotto.valida_codice(123) == False
print("✓ Test 1 passato")
```

### Test 2: Metodo statico - Formatta prezzo
```python
assert Prodotto.formatta_prezzo(10) == "€ 10.00"
assert Prodotto.formatta_prezzo(10.5) == "€ 10.50"
assert Prodotto.formatta_prezzo(0.1) == "€ 0.10"
print("✓ Test 2 passato")
```

### Test 3: Metodo statico - Calcola sconto
```python
# Sconto 10% da 50 pezzi: 50 * 10 * 0.9 = 450
prezzo_scontato = Prodotto.calcola_sconto(50, 10)
assert prezzo_scontato == 450
# Sconto 5% da 20 pezzi: 20 * 10 * 0.95 = 190
prezzo_scontato = Prodotto.calcola_sconto(20, 10)
assert prezzo_scontato == 190
print("✓ Test 3 passato")
```

### Test 4: Metodo di classe - Contatore
```python
# Resetta il contatore per il test
Prodotto.contatore_prodotti = 0
p1 = Prodotto("PROD001", "Mela", 0.50, 100)
assert Prodotto.conta_prodotti() == 1
p2 = Prodotto("PROD002", "Pane", 2.50, 50)
assert Prodotto.conta_prodotti() == 2
print("✓ Test 4 passato")
```

### Test 5: Factory method - Da dizionario
```python
dati = {
    "codice": "PROD001",
    "nome": "Mela",
    "prezzo": 0.50,
    "quantita": 100,
    "descrizione": "Frutta"
}
p = Prodotto.crea_da_dict(dati)
assert p.codice == "PROD001"
assert p.nome == "Mela"
assert p.prezzo == 0.50
assert p.quantita == 100
print("✓ Test 5 passato")
```

### Test 6: Factory method - Da CSV
```python
p = Prodotto.crea_da_csv("PROD001,Mela,0.50,100,Frutta")
assert p.codice == "PROD001"
assert p.nome == "Mela"
assert p.prezzo == 0.50
assert p.quantita == 100
assert p.descrizione == "Frutta"
print("✓ Test 6 passato")
```

### Test 7: Metodo di istanza - Prezzo con IVA
```python
Prodotto.iva_default = 0.22
p = Prodotto("PROD001", "Mela", 10.0, 100)
prezzo_iva = p.prezzo_con_iva()
assert abs(prezzo_iva - 12.2) < 0.01  # 10 * 1.22 = 12.2
print("✓ Test 7 passato")
```

### Test 8: Metodo di istanza - Valore magazzino
```python
p = Prodotto("PROD001", "Mela", 0.50, 100)
assert p.valore_magazzino() == 50.0
p.aumenta_quantita(50)
assert p.valore_magazzino() == 75.0
print("✓ Test 8 passato")
```

### Test 9: Catalogo - Ricerca
```python
catalogo = Catalogo("Test")
p1 = Prodotto("PROD001", "Mela Rossa", 0.50, 100)
p2 = Prodotto("PROD002", "Mela Verde", 0.60, 50)
p3 = Prodotto("PROD003", "Pane", 2.50, 50)

catalogo.aggiungi_prodotto(p1)
catalogo.aggiungi_prodotto(p2)
catalogo.aggiungi_prodotto(p3)

mele = catalogo.cerca_per_nome("Mela")
assert len(mele) == 2
print("✓ Test 9 passato")
```

### Test 10: Metodo di classe - Cambia IVA
```python
Prodotto.iva_default = 0.22
Prodotto.cambia_iva(0.10)
assert Prodotto.iva_default == 0.10

p = Prodotto("PROD001", "Mela", 10.0, 100)
assert p.prezzo_con_iva() == 11.0  # 10 * 1.10
print("✓ Test 10 passato")
```

---

## 📚 Suggerimenti Implementazione Passo-Passo

### Passo 1: Crea attributi di classe
```python
class Prodotto:
    # Attributi di CLASSE (condivisi)
    contatore_prodotti = 0
    iva_default = 0.22
    sconto_quantita = {10: 0.05, 50: 0.10, 100: 0.20}
```

### Passo 2: Implementa metodi statici per validazione
```python
@staticmethod
def valida_codice(codice):
    """Metodo statico - nessun self né cls"""
    if not isinstance(codice, str):
        return False
    if len(codice) != 7:
        return False
    return codice.startswith("PROD") and codice[4:].isdigit()
```

### Passo 3: Implementa metodi statici di utilità
```python
@staticmethod
def formatta_prezzo(prezzo):
    """Funzione pura - non dipende da stato"""
    return f"€ {prezzo:.2f}"

@staticmethod
def calcola_sconto(quantita, prezzo):
    """Usa attributi di classe ma non modifica stato"""
    sconto = 0
    for soglia in sorted(Prodotto.sconto_quantita.keys()):
        if quantita >= soglia:
            sconto = Prodotto.sconto_quantita[soglia]
    return prezzo * quantita * (1 - sconto)
```

### Passo 4: Implementa il costruttore con contatore
```python
def __init__(self, codice, nome, prezzo, quantita):
    if not Prodotto.valida_codice(codice):
        raise ValueError(f"Codice invalido")

    self.codice = codice
    self.nome = nome
    self.prezzo = prezzo
    self.quantita = quantita

    # Incrementa il contatore di classe
    Prodotto.contatore_prodotti += 1
```

### Passo 5: Implementa factory methods
```python
@classmethod
def crea_da_dict(cls, dati):
    """Factory - crea da dizionario"""
    return cls(
        dati["codice"],
        dati["nome"],
        dati["prezzo"],
        dati["quantita"]
    )

@classmethod
def crea_da_csv(cls, riga_csv):
    """Factory - crea da CSV"""
    parti = riga_csv.split(",")
    return cls(
        parti[0].strip(),
        parti[1].strip(),
        float(parti[2].strip()),
        int(parti[3].strip())
    )
```

### Passo 6: Implementa metodi di classe di logica
```python
@classmethod
def conta_prodotti(cls):
    """Accede all'attributo di classe"""
    return cls.contatore_prodotti

@classmethod
def cambia_iva(cls, nuova_iva):
    """Modifica attributo di classe"""
    cls.iva_default = nuova_iva
```

### Passo 7: Implementa metodi di istanza
```python
def prezzo_con_iva(self):
    """Metodo di istanza - accede a self e attributi di classe"""
    return self.prezzo * (1 + Prodotto.iva_default)

def valore_magazzino(self):
    return self.prezzo * self.quantita
```

### Passo 8: Crea il Catalogo e testa
```python
catalogo = Catalogo("Negozio")
p1 = Prodotto("PROD001", "Mela", 0.50, 100)
p2 = Prodotto.crea_da_dict({...})
p3 = Prodotto.crea_da_csv("PROD003,...")

catalogo.aggiungi_prodotto(p1)
catalogo.aggiungi_prodotto(p2)

print(f"Prodotti: {Prodotto.conta_prodotti()}")
print(f"Valore: {catalogo.valore_totale_magazzino()}")
```

---

## 💡 Trucchi e Best Practices

### ✅ Usa @staticmethod per funzioni pure
```python
# BUONO - metodo statico per logica pura
@staticmethod
def formatta_prezzo(prezzo):
    return f"€ {prezzo:.2f}"

# CATTIVO - metodo di istanza per logica che non usa self
def formatta_prezzo(self, prezzo):
    return f"€ {prezzo:.2f}"
    # Perché self non viene usato?
```

### ✅ Usa @classmethod per factory methods
```python
# BUONO - factory method
@classmethod
def crea_da_dict(cls, dati):
    return cls(dati["codice"], dati["nome"], dati["prezzo"])

# Uso:
p = Prodotto.crea_da_dict({"codice": "PROD001", ...})
```

### ✅ Usa attributi di classe per dati globali
```python
# BUONO - dati condivisi in attributo di classe
class Prodotto:
    iva_default = 0.22  # Condiviso

    @classmethod
    def cambia_iva(cls, nuova_iva):
        cls.iva_default = nuova_iva  # Cambia per TUTTI

# CATTIVO - copia l'IVA in ogni istanza
class Prodotto:
    def __init__(self, ...):
        self.iva = 0.22  # Non è condiviso!
```

### ✅ Incrementa contatori in __init__
```python
class Prodotto:
    contatore_prodotti = 0

    def __init__(self, ...):
        # ... attributi di istanza ...
        Prodotto.contatore_prodotti += 1  # Incrementa quando crei
```

### ✅ Usa isinstance() per validare tipo
```python
@staticmethod
def valida_codice(codice):
    if not isinstance(codice, str):  # Verifica tipo
        return False
    if len(codice) != 7:
        return False
    return True
```

### ✅ Usa get() per accedere a dizionari con default
```python
@classmethod
def crea_da_dict(cls, dati):
    return cls(
        dati["codice"],
        dati["nome"],
        dati["prezzo"],
        dati["quantita"],
        dati.get("descrizione", "")  # Default se non esiste
    )
```

---

## ❌ Errori Comuni da Evitare

### ❌ Errore 1: Usare metodo di istanza come statico
```python
# SBAGLIATO - usa self quando non serve
class Prodotto:
    @staticmethod
    def formatta_prezzo(self, prezzo):  # self in @staticmethod?
        return f"€ {prezzo:.2f}"

# GIUSTO - nessun self in @staticmethod
@staticmethod
def formatta_prezzo(prezzo):
    return f"€ {prezzo:.2f}"
```

### ❌ Errore 2: Dimenticare che attributi di classe sono condivisi
```python
# SBAGLIATO - contatore non si incrementa
class Prodotto:
    contatore_prodotti = 0

    def __init__(self, ...):
        # self.contatore_prodotti += 1  # Crea ISTANZA invece!
        # Adesso ogni istanza ha la sua copia, non condivisa

# GIUSTO - modifica l'attributo di classe
def __init__(self, ...):
    Prodotto.contatore_prodotti += 1  # Modifica la classe
```

### ❌ Errore 3: Usare @classmethod quando serve @staticmethod
```python
# SBAGLIATO - riceve cls ma non lo usa
class Prodotto:
    @classmethod
    def formatta_prezzo(cls, prezzo):  # cls non serve!
        return f"€ {prezzo:.2f}"

# GIUSTO
@staticmethod
def formatta_prezzo(prezzo):
    return f"€ {prezzo:.2f}"
```

### ❌ Errore 4: Factory method non ritorna l'istanza
```python
# SBAGLIATO
@classmethod
def crea_da_dict(cls, dati):
    cls(dati["codice"], ...)  # Non ritorna!

# GIUSTO
@classmethod
def crea_da_dict(cls, dati):
    return cls(dati["codice"], ...)  # Ritorna istanza
```

### ❌ Errore 5: Accedere a self in metodo statico
```python
# SBAGLIATO
@staticmethod
def formatta_prezzo(prezzo):
    return f"€ {self.prezzo:.2f}"  # self non esiste!

# GIUSTO
@staticmethod
def formatta_prezzo(prezzo):
    return f"€ {prezzo:.2f}"  # Usa il parametro
```

### ❌ Errore 6: CSV parsing senza error handling
```python
# SBAGLIATO - fallisce se formato sbagliato
@classmethod
def crea_da_csv(cls, riga_csv):
    parti = riga_csv.split(",")
    return cls(parti[0], parti[1], float(parti[2]), int(parti[3]))

# MIGLIORE - con validazione
@classmethod
def crea_da_csv(cls, riga_csv):
    try:
        parti = riga_csv.split(",")
        if len(parti) < 4:
            raise ValueError("CSV incompleto")
        return cls(
            parti[0].strip(),
            parti[1].strip(),
            float(parti[2].strip()),
            int(parti[3].strip())
        )
    except (ValueError, IndexError) as e:
        print(f"Errore parsing CSV: {e}")
        return None
```

---

## 🚀 Estensioni e Sfide Bonus

### 🌟 Sfida 1: Persistenza - Salva e Carica da JSON
```python
import json

class Catalogo:
    def salva_json(self, nome_file):
        """Salva il catalogo in JSON"""
        dati = {
            "nome": self.nome,
            "prodotti": [
                {
                    "codice": p.codice,
                    "nome": p.nome,
                    "prezzo": p.prezzo,
                    "quantita": p.quantita,
                    "descrizione": p.descrizione
                }
                for p in self.prodotti.values()
            ]
        }
        with open(nome_file, 'w') as f:
            json.dump(dati, f, indent=2)

    @classmethod
    def carica_json(cls, nome_file):
        """Carica il catalogo da JSON"""
        with open(nome_file, 'r') as f:
            dati = json.load(f)

        catalogo = cls(dati["nome"])
        for p_data in dati["prodotti"]:
            p = Prodotto.crea_da_dict(p_data)
            catalogo.aggiungi_prodotto(p)
        return catalogo
```

### 🌟 Sfida 2: Gestione degli ID Auto-Incrementali
```python
class Prodotto:
    contatore_prodotti = 0
    id_prodotti = 1000  # ID auto-incrementale

    @classmethod
    def prossimo_id(cls):
        cls.id_prodotti += 1
        return cls.id_prodotti

    @classmethod
    def auto_crea_da_dict(cls, dati):
        """Factory che genera automaticamente codice"""
        codice = f"AUTO{cls.prossimo_id()}"
        return cls(
            codice,
            dati["nome"],
            dati["prezzo"],
            dati["quantita"]
        )
```

### 🌟 Sfida 3: Reporting Avanzato
```python
class Catalogo:
    def rapporto_valore_per_categoria(self):
        """Raggruppa per categoria e mostra valore"""
        categorie = {}
        for p in self.prodotti.values():
            cat = p.categoria if hasattr(p, 'categoria') else "Varia"
            if cat not in categorie:
                categorie[cat] = 0
            categorie[cat] += p.valore_magazzino()

        for cat, valore in sorted(categorie.items()):
            print(f"{cat}: {Prodotto.formatta_prezzo(valore)}")

    def prodotti_sotto_soglia(self, soglia_quantita):
        """Identifica prodotti con quantità bassa"""
        return [p for p in self.prodotti.values() if p.quantita < soglia_quantita]
```

### 🌟 Sfida 4: Validazione Avanzata
```python
class Prodotto:
    @staticmethod
    def valida_prezzo(prezzo):
        return isinstance(prezzo, (int, float)) and prezzo > 0

    @staticmethod
    def valida_quantita(quantita):
        return isinstance(quantita, int) and quantita >= 0

    @staticmethod
    def valida_email(email):
        return "@" in email and "." in email and len(email) > 5

    def __init__(self, codice, nome, prezzo, quantita):
        if not Prodotto.valida_codice(codice):
            raise ValueError(f"Codice invalido: {codice}")
        if not Prodotto.valida_prezzo(prezzo):
            raise ValueError(f"Prezzo invalido: {prezzo}")
        if not Prodotto.valida_quantita(quantita):
            raise ValueError(f"Quantita invalida: {quantita}")

        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        Prodotto.contatore_prodotti += 1
```

### 🌟 Sfida 5: Sistema di Licenze e Versioni
```python
class Prodotto:
    versione = "1.0"
    licenza = "GPL"

    @classmethod
    def aggiorna_versione(cls, nuova_versione):
        cls.versione = nuova_versione

    @classmethod
    def aggiorna_licenza(cls, nuova_licenza):
        cls.licenza = nuova_licenza

    def info_sistema(self):
        return (
            f"{self.nome}\n"
            f"Versione: {Prodotto.versione}\n"
            f"Licenza: {Prodotto.licenza}"
        )
```

---

## 📖 Riassunto Concetti Importanti

| Concetto | Spiegazione | Accede a | Usa |
|----------|-------------|----------|-----|
| **Metodo istanza** | Lavora su singoli oggetti | `self` | Dati dell'istanza |
| **Metodo classe** | Lavora a livello di classe | `cls` | Attributi di classe |
| **Metodo statico** | Funzione pura indipendente | Nessuno | Logica generica |
| **Attributo istanza** | Dati di un singolo oggetto | - | `self.attributo` |
| **Attributo classe** | Dati condivisi | - | `cls.attributo` |
| **Factory method** | Crea istanze specializzate | - | `@classmethod` |
| **Contatore** | Traccia istanze create | - | In `__init__` |

---

## 🔗 Link Utili

### Documentazione
- [@staticmethod Decorator](https://docs.python.org/3/library/functions.html#staticmethod)
- [@classmethod Decorator](https://docs.python.org/3/library/functions.html#classmethod)
- [Class and Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)

### Tutorial
- [Real Python - Static Methods](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Real Python - Class Methods](https://realpython.com/course/static-class-methods/)
- [GeeksforGeeks - Static vs Class Methods](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)

---

## 📂 Soluzione

Quando hai terminato, confronta il tuo codice con la soluzione ufficiale:

📁 **[Soluzione Ufficiale](../soluzione/)**

**Consigli per il confronto:**
- Osserva come sono usati @staticmethod e @classmethod
- Guarda come sono gestiti gli attributi di classe
- Nota i factory methods e come sono implementati
- Apprendi dai pattern di validazione

---

## ✅ Checklist Finale

Prima di dire che hai finito, verifica:

- [ ] Ho creato attributi di classe (contatore, IVA, sconto)
- [ ] Ho implementato @staticmethod per validazione codice
- [ ] Ho implementato @staticmethod per calcoli (sconto, formato)
- [ ] Ho implementato @classmethod per contare prodotti
- [ ] Ho implementato @classmethod per cambiare IVA
- [ ] Ho creato factory methods da_dict() e da_csv()
- [ ] Il costruttore incrementa il contatore
- [ ] Ho implementato metodi di istanza (prezzo_con_iva, valore_magazzino)
- [ ] Ho creato la classe Catalogo
- [ ] Il Catalogo può aggiungere, cercare, e filtrare prodotti
- [ ] Ho testato con almeno 8 casi di prova
- [ ] Ho implementato almeno una sfida bonus
- [ ] Il codice è commentato e leggibile

---

**Congratulazioni! Hai padroneggiato metodi statici e di classe! 🎉💼**

*"I metodi statici e di classe sono la chiave per organizzare logica riutilizzabile nel tuo codice."*
