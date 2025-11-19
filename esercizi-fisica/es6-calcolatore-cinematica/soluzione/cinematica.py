# Calcolatore Cinematica - SOLUZIONE
import matplotlib.pyplot as plt
import numpy as np

def moto_uniforme(s0, v, t):
    """s = s0 + v·t"""
    return s0 + v * t

def moto_uniformemente_accelerato(s0, v0, a, t):
    """s = s0 + v0·t + ½a·t²"""
    return s0 + v0 * t + 0.5 * a * t**2

def velocita_finale(v0, a, t):
    """v = v0 + a·t"""
    return v0 + a * t

def velocita_da_spazio(v0, a, s):
    """v² = v0² + 2a·s  →  v = √(v0² + 2a·s)"""
    return np.sqrt(v0**2 + 2*a*s)

def main():
    print("=== CALCOLATORE CINEMATICA ===\n")
    print("1. Moto rettilineo uniforme")
    print("2. Moto uniformemente accelerato")
    print("3. Velocità finale (da accelerazione)")
    print("4. Tempo di caduta libera")

    scelta = input("\nScegli (1-4): ")

    if scelta == "1":
        s0 = float(input("Posizione iniziale s0 (m): ") or "0")
        v = float(input("Velocità v (m/s): "))
        t = float(input("Tempo t (s): "))

        s = moto_uniforme(s0, v, t)
        print(f"\n🚗 MOTO UNIFORME")
        print(f"   Posizione finale: {s:.2f} m")
        print(f"   Spazio percorso: {s - s0:.2f} m")

        # Grafico
        t_vals = np.linspace(0, t, 100)
        s_vals = [moto_uniforme(s0, v, ti) for ti in t_vals]

        plt.figure(figsize=(10, 5))
        plt.plot(t_vals, s_vals, 'b-', linewidth=2)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Posizione (m)')
        plt.title('Moto Rettilineo Uniforme')
        plt.grid(True, alpha=0.3)
        plt.savefig('moto_uniforme.png', dpi=150)
        plt.show()

    elif scelta == "2":
        s0 = float(input("Posizione iniziale s0 (m): ") or "0")
        v0 = float(input("Velocità iniziale v0 (m/s): ") or "0")
        a = float(input("Accelerazione a (m/s²): "))
        t = float(input("Tempo t (s): "))

        s = moto_uniformemente_accelerato(s0, v0, a, t)
        v = velocita_finale(v0, a, t)

        print(f"\n🚀 MOTO UNIFORMEMENTE ACCELERATO")
        print(f"   Posizione finale: {s:.2f} m")
        print(f"   Velocità finale: {v:.2f} m/s")
        print(f"   Spazio percorso: {s - s0:.2f} m")

        # Grafici
        t_vals = np.linspace(0, t, 100)
        s_vals = [moto_uniformemente_accelerato(s0, v0, a, ti) for ti in t_vals]
        v_vals = [velocita_finale(v0, a, ti) for ti in t_vals]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        ax1.plot(t_vals, s_vals, 'b-', linewidth=2)
        ax1.set_xlabel('Tempo (s)')
        ax1.set_ylabel('Posizione (m)')
        ax1.set_title('Legge oraria s(t)')
        ax1.grid(True, alpha=0.3)

        ax2.plot(t_vals, v_vals, 'r-', linewidth=2)
        ax2.set_xlabel('Tempo (s)')
        ax2.set_ylabel('Velocità (m/s)')
        ax2.set_title('Velocità v(t)')
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('moto_accelerato.png', dpi=150)
        plt.show()

    elif scelta == "3":
        v0 = float(input("Velocità iniziale v0 (m/s): "))
        a = float(input("Accelerazione a (m/s²): "))
        t = float(input("Tempo t (s): "))

        v = velocita_finale(v0, a, t)
        print(f"\n⚡ Velocità finale: {v:.2f} m/s")

    elif scelta == "4":
        h = float(input("Altezza h (m): "))
        g = 9.81

        # t = √(2h/g)
        t = np.sqrt(2 * h / g)
        v = g * t

        print(f"\n🪂 CADUTA LIBERA")
        print(f"   Tempo di caduta: {t:.2f} s")
        print(f"   Velocità impatto: {v:.2f} m/s ({v*3.6:.2f} km/h)")

if __name__ == "__main__":
    main()
