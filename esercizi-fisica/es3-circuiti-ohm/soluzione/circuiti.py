# Circuiti e Ohm - SOLUZIONE
def serie(*resistenze):
    """Resistenze in serie"""
    return sum(resistenze)

def parallelo(*resistenze):
    """Resistenze in parallelo"""
    return 1 / sum(1/r for r in resistenze)

def calcola_circuito(V, R):
    """Legge di Ohm"""
    I = V / R
    P = V * I
    return I, P

def main():
    print("=== CALCOLATORE CIRCUITI ===\n")
    print("1. Resistenze in serie")
    print("2. Resistenze in parallelo")
    print("3. Legge di Ohm")

    scelta = input("\nScegli (1-3): ")

    if scelta == "1":
        R = list(map(float, input("Resistenze (separate da spazio): ").split()))
        R_tot = serie(*R)
        print(f"\n⚡ Resistenza totale (serie): {R_tot:.2f} Ω")

    elif scelta == "2":
        R = list(map(float, input("Resistenze (separate da spazio): ").split()))
        R_tot = parallelo(*R)
        print(f"\n⚡ Resistenza totale (parallelo): {R_tot:.2f} Ω")

    elif scelta == "3":
        V = float(input("Tensione (V): "))
        R = float(input("Resistenza (Ω): "))
        I, P = calcola_circuito(V, R)
        print(f"\n⚡ CIRCUITO")
        print(f"   Tensione: {V} V")
        print(f"   Resistenza: {R} Ω")
        print(f"   Corrente: {I:.3f} A")
        print(f"   Potenza: {P:.3f} W\n")

if __name__ == "__main__":
    main()
