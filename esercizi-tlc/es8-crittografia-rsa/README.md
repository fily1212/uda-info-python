# Es8: Crittografia RSA

**Livello:** AVANZATO
**Durata stimata:** 6-7 ore

## Descrizione

Implementazione completa dell'algoritmo RSA per crittografia asimmetrica: generazione di chiavi pubbliche/private, cifratura, decifratura e firma digitale. Analisi della sicurezza e fattorizzazione di numeri semi-primi.

## Obiettivi

### Competenze TLC
- Comprendere la crittografia a chiave pubblica
- Implementare l'algoritmo RSA (Rivest-Shamir-Adleman)
- Generare numeri primi grandi
- Calcolare parametri RSA (e, d, n, φ)
- Implementare firma digitale e verificazione

### Competenze Informatica
- Test di primalità (Miller-Rabin)
- Algoritmo di Euclide esteso (EGCD)
- Elevamento a potenza modulare veloce
- Gestione di numeri grandi (Python big integers)
- Crittografia e decrittografia di messaggi
- Hash e firma digitale

## Consegna

Il programma deve:

1. **Generare chiavi RSA:**
   - Scegli due numeri primi grandi p e q
   - Calcola n = p*q (modulo)
   - Calcola φ(n) = (p-1)*(q-1)
   - Scegli e: gcd(e, φ) = 1, tipicamente e=65537
   - Calcola d: e*d ≡ 1 (mod φ)
   - Chiave pubblica: (e, n)
   - Chiave privata: (d, n)

2. **Cifratura e decifratura:**
   - Cifratura: C = M^e mod n
   - Decifratura: M = C^d mod n
   - Gestione di messaggi lunghi (block cipher)

3. **Firma digitale:**
   - Hash del messaggio: h = SHA256(messaggio)
   - Firma: σ = h^d mod n
   - Verificazione: h' = σ^e mod n, verifica h == h'

4. **Utility crittografiche:**
   - Test di primalità robusto (Miller-Rabin)
   - Generatore di numeri primi casuali
   - Algoritmo EGCD per calcolo chiave privata
   - Padding di messaggi

5. **Analisi e attacchi:**
   - Fattorizzazione (Pollard rho, per chiavi deboli)
   - Analisi della forza della chiave
   - Timing attacks awareness

## Esempio di Utilizzo

```
=== SISTEMA RSA ===

Generazione chiavi RSA:
1. Genera nuova coppia di chiavi
2. Carica chiavi da file
3. Esci

Scelta: 1

Inserisci bit-length chiavi (512, 1024, 2048, 4096): 1024

Generando numeri primi da 512 bit...
├─ Primo p: 17959898...(512 bit)
├─ Primo q: 18439872...(512 bit)
├─ Modulo n (1024 bit): 33156...(1024 bit)
├─ Phi(n) = (p-1)*(q-1): 33155...
├─ Esponente pubblico e: 65537
├─ Esponente privato d: 49823...(1024 bit)
└─ Chiavi generate in 2.34 sec ✓

Chiave pubblica:
-----BEGIN RSA PUBLIC KEY-----
e: 65537
n: 33156...
-----END RSA PUBLIC KEY-----

Chiave privata (PROTEGGERE!):
-----BEGIN RSA PRIVATE KEY-----
d: 49823...
n: 33156...
-----END RSA PRIVATE KEY-----

--- MENU PRINCIPALE ---
1. Cifra messaggio
2. Decifra messaggio
3. Firma digitale
4. Verifica firma
5. Analizza chiave
6. Esci

Scelta: 1

Inserisci messaggio: "Ciao, questo è segreto!"

Messaggio (plaintext): Ciao, questo è segreto!
Lunghezza: 28 caratteri

Messaggi cifrati (blocks):
Block 1: 15823...
Block 2: 24917...
Block 3: ...

Ciphertext completo (hex): 3f8a9b2e...

--- DECIFRAZIONE ---

Ciphertext: 3f8a9b2e...

Messaggi decifrati:
Block 1: Ciao, q
Block 2: uesto
Block 3: è seg
...

Plaintext: Ciao, questo è segreto! ✓

--- FIRMA DIGITALE ---

Messaggio: "Documento importante"
SHA256 hash: a3f9e2c...

Firma generata: 8f2a4d...

Dimensione firma: 1024 bit
Algoritmo: RSA + SHA256
```

## Suggerimenti

- Usa Python's `random` e `sympy.ntheory` per numeri primi
- Implementa Miller-Rabin per test di primalità veloce
- Usa algoritmo di Euclide esteso per calcolo modulo inverso
- Implementa pow(base, exp, mod) per elevamento veloce
- Gestisci messaggi lunghi dividendoli in blocchi
- Aggiungi padding OAEP o PKCS#1 v1.5 per sicurezza
- Usa `hashlib.sha256()` per hash crittografico
- Valida la forza della chiave (min 1024 bit, meglio 2048+)

## Esempio di Codice Struttura

```python
import random
import math
from hashlib import sha256

class RSA:
    def __init__(self, key_size=1024):
        self.key_size = key_size
        self.p = None
        self.q = None
        self.n = None
        self.e = None
        self.d = None
        self.phi = None

    def is_prime(self, num, k=40):
        """Test di primalità Miller-Rabin"""
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False

        # Scrivi num-1 come 2^r * d
        r, d = 0, num - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        # Test k volte
        for _ in range(k):
            a = random.randrange(2, num - 1)
            x = pow(a, d, num)

            if x == 1 or x == num - 1:
                continue

            for _ in range(r - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False

        return True

    def genera_primo(self, bit_length):
        """Genera numero primo casuale di bit_length bit"""
        while True:
            num = random.getrandbits(bit_length)
            num |= (1 << bit_length - 1) | 1  # Assicura bit_length bit e dispari

            if self.is_prime(num):
                return num

    def egcd(self, a, b):
        """Algoritmo di Euclide esteso: trova x,y tali che ax + by = gcd(a,b)"""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def mod_inverso(self, e, phi):
        """Calcola d tale che e*d ≡ 1 (mod phi)"""
        gcd, x, _ = self.egcd(e, phi)
        if gcd != 1:
            raise ValueError("Inverso modulare non esiste")
        return (x % phi + phi) % phi

    def genera_chiavi(self):
        """Genera coppia di chiavi RSA"""
        print(f"Generando numeri primi da {self.key_size // 2} bit...")

        # Genera p e q
        self.p = self.genera_primo(self.key_size // 2)
        self.q = self.genera_primo(self.key_size // 2)

        # Calcola n e φ(n)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        # Scegli e (tipicamente 65537)
        self.e = 65537
        while math.gcd(self.e, self.phi) != 1:
            self.e += 2

        # Calcola d
        self.d = self.mod_inverso(self.e, self.phi)

        print(f"Chiavi generate con successo!")
        print(f"Modulo n: {self.n.bit_length()} bit")

    def cifra(self, messaggio):
        """Cifra un messaggio"""
        if isinstance(messaggio, str):
            messaggio = messaggio.encode()

        # Converti in intero
        m = int.from_bytes(messaggio, byteorder='big')

        # Cifra: c = m^e mod n
        c = pow(m, self.e, self.n)
        return c

    def decifra(self, ciphertext):
        """Decifra un ciphertext"""
        # Decifra: m = c^d mod n
        m = pow(ciphertext, self.d, self.n)

        # Converti da intero a bytes
        messaggio = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
        return messaggio

    def firma(self, messaggio):
        """Crea firma digitale di un messaggio"""
        # Hash del messaggio
        h = sha256(messaggio.encode() if isinstance(messaggio, str) else messaggio)
        h_int = int.from_bytes(h.digest(), byteorder='big')

        # Firma: σ = h^d mod n
        firma = pow(h_int, self.d, self.n)
        return firma

    def verifica_firma(self, messaggio, firma):
        """Verifica firma digitale"""
        # Hash del messaggio
        h = sha256(messaggio.encode() if isinstance(messaggio, str) else messaggio)
        h_int = int.from_bytes(h.digest(), byteorder='big')

        # Verifica: h' = σ^e mod n
        h_prime = pow(firma, self.e, self.n)

        return h_int == h_prime

# Utilizzo
rsa = RSA(key_size=1024)
rsa.genera_chiavi()

# Cifra
ciphertext = rsa.cifra("Messaggio segreto")
print(f"Ciphertext: {ciphertext}")

# Decifra
plaintext = rsa.decifra(ciphertext)
print(f"Plaintext: {plaintext}")

# Firma
firma = rsa.firma("Documento")
verifica = rsa.verifica_firma("Documento", firma)
print(f"Firma valida: {verifica}")
```

## Sicurezza RSA

- **Forza:** Difficoltà di fattorizzazione di n in p e q
- **Attacchi:** Fattorizzazione, padding oracle, timing attacks
- **Protezione:** Usa padding OAEP, chiavi 2048+ bit, liberie testate
- **Non usare:** Per implementazioni critiche, usa librerie come cryptography

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🔐🔑**
