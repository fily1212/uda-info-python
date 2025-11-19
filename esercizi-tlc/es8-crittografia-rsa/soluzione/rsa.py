# Crittografia RSA - SOLUZIONE
import random

def is_prime(n, k=5):
    """Test primalità Miller-Rabin"""
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n == p: return True
        if n % p == 0: return False
    # Versione semplificata
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Inverso modulare con algoritmo di Euclide esteso"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    _, x, _ = extended_gcd(e, phi)
    return (x % phi + phi) % phi

def genera_chiavi():
    """Genera coppia chiavi RSA (semplificato)"""
    p, q = 61, 53  # Primi piccoli per demo
    n = p * q
    phi = (p - 1) * (q - 1)

    # Scelta e
    e = 17
    while gcd(e, phi) != 1:
        e += 2

    # Calcola d
    d = mod_inverse(e, phi)

    print(f"🔐 RSA Generato:")
    print(f"   p={p}, q={q}")
    print(f"   n={n}, φ(n)={phi}")
    print(f"   Chiave pubblica: (e={e}, n={n})")
    print(f"   Chiave privata: (d={d}, n={n})")

    return (e, n), (d, n)

def cifra(messaggio, chiave_pubblica):
    e, n = chiave_pubblica
    return pow(messaggio, e, n)

def decifra(cifrato, chiave_privata):
    d, n = chiave_privata
    return pow(cifrato, d, n)

# Demo
pub, priv = genera_chiavi()
msg = 42
cifrato = cifra(msg, pub)
decifrato = decifra(cifrato, priv)

print(f"\n📨 Messaggio originale: {msg}")
print(f"🔒 Cifrato: {cifrato}")
print(f"🔓 Decifrato: {decifrato}")
