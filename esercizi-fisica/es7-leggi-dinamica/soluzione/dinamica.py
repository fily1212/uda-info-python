# Leggi della Dinamica - SOLUZIONE

def seconda_legge_newton(m, a):
    """F = m·a"""
    return m * a

def accelerazione_da_forza(F, m):
    """a = F/m"""
    return F / m

def massa_da_forza(F, a):
    """m = F/a"""
    return F / a

def peso(m, g=9.81):
    """P = m·g"""
    return m * g

def forza_attrito(mu, N):
    """Fa = μ·N"""
    return mu * N

def piano_inclinato(m, theta_gradi, g=9.81):
    """Componenti forza su piano inclinato"""
    import math
    theta = math.radians(theta_gradi)

    P = m * g
    P_parallelo = P * math.sin(theta)
    P_perpendicolare = P * math.cos(theta)

    return P_parallelo, P_perpendicolare

def main():
    print("=== LEGGI DELLA DINAMICA ===\n")
    print("1. Seconda legge Newton (F = ma)")
    print("2. Calcolo peso (P = mg)")
    print("3. Forza di attrito (Fa = μN)")
    print("4. Piano inclinato")

    scelta = input("\nScegli (1-4): ")

    if scelta == "1":
        m = float(input("Massa m (kg): "))
        a = float(input("Accelerazione a (m/s²): "))

        F = seconda_legge_newton(m, a)
        print(f"\n⚙️ SECONDA LEGGE DI NEWTON")
        print(f"   F = m·a = {m} × {a} = {F:.2f} N")

    elif scelta == "2":
        m = float(input("Massa m (kg): "))
        g = float(input("Gravità g (m/s², default 9.81): ") or "9.81")

        P = peso(m, g)
        print(f"\n⚖️ PESO")
        print(f"   P = m·g = {m} × {g} = {P:.2f} N")

    elif scelta == "3":
        mu = float(input("Coefficiente attrito μ: "))
        N = float(input("Forza normale N (N): "))

        Fa = forza_attrito(mu, N)
        print(f"\n🛑 FORZA DI ATTRITO")
        print(f"   Fa = μ·N = {mu} × {N} = {Fa:.2f} N")

    elif scelta == "4":
        m = float(input("Massa m (kg): "))
        theta = float(input("Angolo inclinazione (gradi): "))

        P_par, P_perp = piano_inclinato(m, theta)

        print(f"\n⛰️ PIANO INCLINATO")
        print(f"   Peso totale: {peso(m):.2f} N")
        print(f"   Componente parallela: {P_par:.2f} N")
        print(f"   Componente perpendicolare: {P_perp:.2f} N")

    # Esempi
    print("\n📋 Esempi pratici:")
    print(f"   Auto 1000kg a 2m/s²: F = {seconda_legge_newton(1000, 2):.0f} N")
    print(f"   Peso persona 70kg: P = {peso(70):.0f} N")

if __name__ == "__main__":
    main()
