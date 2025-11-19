# Calcolo Probabilità - SOLUZIONE
from math import comb, factorial

def prob_dado(esito, facce=6):
    """Probabilità singolo dado"""
    return 1 / facce

def prob_moneta(risultato):
    """Probabilità moneta"""
    return 0.5

def prob_eventi_indipendenti(p1, p2):
    """P(A e B) = P(A) × P(B)"""
    return p1 * p2

def prob_eventi_mutuamente_esclusivi(p1, p2):
    """P(A o B) = P(A) + P(B)"""
    return p1 + p2

def prob_complemento(p):
    """P(non A) = 1 - P(A)"""
    return 1 - p

def main():
    print("=== CALCOLATORE PROBABILITÀ ===\n")
    print("1. Probabilità dado")
    print("2. Probabilità eventi indipendenti (E)")
    print("3. Probabilità eventi mutuamente esclusivi (O)")
    print("4. Evento complementare")

    scelta = input("\nScegli (1-4): ")

    if scelta == "1":
        esito = int(input("Esito desiderato (1-6): "))
        p = prob_dado(esito)
        print(f"\n🎲 P(dado={esito}) = {p:.4f} = {p*100:.2f}%")

    elif scelta == "2":
        p1 = float(input("P(A): "))
        p2 = float(input("P(B): "))
        p = prob_eventi_indipendenti(p1, p2)
        print(f"\n📊 P(A E B) = {p:.4f} = {p*100:.2f}%")

    elif scelta == "3":
        p1 = float(input("P(A): "))
        p2 = float(input("P(B): "))
        p = prob_eventi_mutuamente_esclusivi(p1, p2)
        print(f"\n📊 P(A O B) = {p:.4f} = {p*100:.2f}%")

    elif scelta == "4":
        p = float(input("P(A): "))
        p_comp = prob_complemento(p)
        print(f"\n📊 P(non A) = {p_comp:.4f} = {p_comp*100:.2f}%")

    # Esempi
    print("\n📋 Esempi comuni:")
    print(f"   Testa o croce: {prob_moneta('T')*100:.0f}%")
    print(f"   Dado = 6: {prob_dado(6)*100:.2f}%")
    print(f"   2 dadi = 12: {prob_eventi_indipendenti(1/6, 1/6)*100:.2f}%")

if __name__ == "__main__":
    main()
