# Visualizzatore Funzioni - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize
from scipy.integrate import quad

def grafica_funzione(func_str, intervallo=(-10, 10)):
    x = np.linspace(intervallo[0], intervallo[1], 1000)

    # Valuta funzione (usa numpy per funzioni matematiche)
    func = lambda t: eval(func_str, {"x": t, "np": np,
                                     "sin": np.sin, "cos": np.cos,
                                     "log": np.log, "exp": np.exp,
                                     "sqrt": np.sqrt})

    try:
        y = np.array([func(xi) for xi in x])
    except:
        print("❌ Errore nella funzione!")
        return

    # Grafico
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {func_str}')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Grafico di f(x) = {func_str}')
    plt.legend()

    # Trova zeri
    print(f"\n📊 Analisi di f(x) = {func_str}")
    print(f"   Intervallo: [{intervallo[0]}, {intervallo[1]}]")

    zeri = []
    for x0 in np.linspace(intervallo[0], intervallo[1], 20):
        try:
            zero = fsolve(func, x0)[0]
            if intervallo[0] <= zero <= intervallo[1]:
                if not any(abs(zero - z) < 0.1 for z in zeri):
                    zeri.append(zero)
                    plt.plot(zero, 0, 'ro', markersize=8)
        except:
            pass

    if zeri:
        print(f"   Zeri trovati: {', '.join(f'x≈{z:.2f}' for z in sorted(zeri))}")

    # Area sotto curva
    try:
        area, _ = quad(func, intervallo[0], intervallo[1])
        print(f"   Area (integrale): {area:.2f}")
    except:
        pass

    plt.savefig(f'grafico_{func_str.replace("/","_")}.png', dpi=150)
    plt.show()
    print(f"   ✅ Grafico salvato\n")

def main():
    print("=== VISUALIZZATORE DI FUNZIONI ===\n")
    print("Funzioni disponibili: sin, cos, log, exp, sqrt, x**n")
    print("Esempio: x**2 - 4, sin(x), 1/x\n")

    while True:
        func_str = input("Funzione f(x) = ").strip()
        if not func_str:
            break

        try:
            a = float(input("Intervallo min: "))
            b = float(input("Intervallo max: "))
            grafica_funzione(func_str, (a, b))
        except ValueError:
            print("Valori non validi!\n")

if __name__ == "__main__":
    main()
