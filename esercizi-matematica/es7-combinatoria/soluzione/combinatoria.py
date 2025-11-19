# Combinatoria - SOLUZIONE
from math import factorial, comb, perm

def fattoriale(n):
    """Calcola n!"""
    return factorial(n)

def permutazioni(n, k=None):
    """P(n,k) = n!/(n-k)! oppure P(n) = n!"""
    if k is None:
        return factorial(n)
    return perm(n, k)

def combinazioni(n, k):
    """C(n,k) = n! / (k!(n-k)!)"""
    return comb(n, k)

def disposizioni(n, k):
    """D(n,k) = n!/(n-k)!"""
    return perm(n, k)

def main():
    print("=== CALCOLATORE COMBINATORIA ===\n")
    print("1. Fattoriale n!")
    print("2. Permutazioni P(n,k)")
    print("3. Combinazioni C(n,k)")
    print("4. Disposizioni D(n,k)")

    scelta = input("\nScegli (1-4): ")

    if scelta == "1":
        n = int(input("n: "))
        risultato = fattoriale(n)
        print(f"\n🔢 {n}! = {risultato}")

    elif scelta == "2":
        n = int(input("n (totale elementi): "))
        k = int(input("k (elementi da disporre): "))
        risultato = permutazioni(n, k)
        print(f"\n🔢 P({n},{k}) = {risultato}")
        print(f"   Modi di disporre {k} elementi tra {n}")

    elif scelta == "3":
        n = int(input("n (totale elementi): "))
        k = int(input("k (elementi da scegliere): "))
        risultato = combinazioni(n, k)
        print(f"\n🔢 C({n},{k}) = {risultato}")
        print(f"   Modi di scegliere {k} elementi tra {n} (ordine NON conta)")

    elif scelta == "4":
        n = int(input("n (totale elementi): "))
        k = int(input("k (posti): "))
        risultato = disposizioni(n, k)
        print(f"\n🔢 D({n},{k}) = {risultato}")
        print(f"   Modi di disporre {k} tra {n} (ordine conta)")

    # Esempi pratici
    print("\n📋 Esempi pratici:")
    print(f"   Anagrammi di 'CIAO' (4 lettere): {fattoriale(4)} = 24")
    print(f"   Combinazioni lotto (5 su 90): {combinazioni(90, 5):,}")
    print(f"   Podio gara (3 su 10): {permutazioni(10, 3)}")

if __name__ == "__main__":
    main()
