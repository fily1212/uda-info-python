# Calcolatore Derivate - SOLUZIONE
from sympy import *

x = symbols('x')

def analizza_funzione(expr_str):
    expr = sympify(expr_str)
    print(f"\n📐 f(x) = {expr}")

    # Derivate
    derivata1 = diff(expr, x)
    derivata2 = diff(expr, x, 2)
    print(f"   f'(x) = {derivata1}")
    print(f"   f''(x) = {derivata2}")

    # Punti critici
    punti_critici = solve(derivata1, x)
    if punti_critici:
        print(f"   Punti critici: {', '.join(f'x={p}' for p in punti_critici)}")

    # Integrale
    integrale = integrate(expr, x)
    print(f"   ∫f(x)dx = {integrale} + C")

    # Limite all'infinito
    lim_inf = limit(expr, x, oo)
    print(f"   lim(x→∞) f(x) = {lim_inf}")

    # Serie di Taylor
    taylor = series(expr, x, 0, 4).removeO()
    print(f"   Taylor(x=0, n=3): {taylor}")

def main():
    print("=== CALCOLATORE SIMBOLICO ===\n")
    while True:
        expr_str = input("f(x) = ").strip()
        if not expr_str:
            break
        try:
            analizza_funzione(expr_str)
        except Exception as e:
            print(f"❌ Errore: {e}")

if __name__ == "__main__":
    main()
