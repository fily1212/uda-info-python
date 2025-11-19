# Grafici Funzioni Base - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt

def grafica_funzione_base(tipo='lineare', parametri=None):
    """Grafica funzioni base"""
    x = np.linspace(-10, 10, 400)

    plt.figure(figsize=(10, 6))

    if tipo == 'lineare':  # y = mx + q
        m, q = parametri if parametri else (1, 0)
        y = m * x + q
        plt.plot(x, y, label=f'y = {m}x + {q}')
        plt.title('Funzione Lineare')

    elif tipo == 'quadratica':  # y = ax² + bx + c
        a, b, c = parametri if parametri else (1, 0, 0)
        y = a * x**2 + b * x + c
        plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
        plt.title('Funzione Quadratica (Parabola)')

        # Vertice
        xv = -b / (2*a)
        yv = a * xv**2 + b * xv + c
        plt.plot(xv, yv, 'ro', markersize=10, label=f'Vertice ({xv:.2f}, {yv:.2f})')

    elif tipo == 'cubica':  # y = x³
        y = x**3
        plt.plot(x, y, label='y = x³')
        plt.title('Funzione Cubica')

    elif tipo == 'esponenziale':  # y = a^x
        a = parametri[0] if parametri else 2
        x_pos = np.linspace(0, 5, 200)
        y = a ** x_pos
        plt.plot(x_pos, y, label=f'y = {a}^x')
        plt.title('Funzione Esponenziale')

    elif tipo == 'logaritmica':  # y = log(x)
        x_pos = np.linspace(0.1, 10, 200)
        y = np.log(x_pos)
        plt.plot(x_pos, y, label='y = ln(x)')
        plt.title('Funzione Logaritmica')

    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.savefig(f'grafico_{tipo}.png', dpi=150)
    plt.show()

def main():
    print("=== GRAFICI FUNZIONI BASE ===\n")
    print("1. Lineare (y = mx + q)")
    print("2. Quadratica (y = ax² + bx + c)")
    print("3. Cubica (y = x³)")
    print("4. Esponenziale (y = aˣ)")
    print("5. Logaritmica (y = ln(x))")

    scelta = input("\nScegli (1-5): ")

    if scelta == "1":
        m = float(input("Coefficiente m: ") or "1")
        q = float(input("Termine noto q: ") or "0")
        grafica_funzione_base('lineare', (m, q))

    elif scelta == "2":
        a = float(input("Coefficiente a: ") or "1")
        b = float(input("Coefficiente b: ") or "0")
        c = float(input("Termine noto c: ") or "0")
        grafica_funzione_base('quadratica', (a, b, c))

    elif scelta == "3":
        grafica_funzione_base('cubica')

    elif scelta == "4":
        a = float(input("Base a: ") or "2")
        grafica_funzione_base('esponenziale', (a,))

    elif scelta == "5":
        grafica_funzione_base('logaritmica')

if __name__ == "__main__":
    main()
