# Moto Planetario - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simula_orbita(M=1.0, m=0.001, r0=1.0, v0=1.0, durata=10):
    """Simula orbita pianeta attorno al sole (semplificato)"""
    G = 1.0  # costante gravitazionale normalizzata
    dt = 0.01
    steps = int(durata / dt)

    # Condizioni iniziali
    x, y = r0, 0
    vx, vy = 0, v0

    # Arrays per traiettoria
    xs, ys = [x], [y]

    for _ in range(steps):
        r = np.sqrt(x**2 + y**2)
        F = G * M * m / r**2

        # Accelerazione
        ax = -F * x / (m * r)
        ay = -F * y / (m * r)

        # Integrazione (Euler)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        xs.append(x)
        ys.append(y)

    # Grafico orbita
    plt.figure(figsize=(8, 8))
    plt.plot(xs, ys, 'b-', linewidth=1, alpha=0.7)
    plt.plot(0, 0, 'yo', markersize=30, label='Sole')
    plt.plot(xs[0], ys[0], 'go', markersize=10, label='Posizione iniziale')
    plt.plot(xs[-1], ys[-1], 'ro', markersize=10, label='Posizione finale')
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.title('Orbita Planetaria')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('orbita.png', dpi=150)
    plt.show()

    print("\n🪐 SIMULAZIONE ORBITALE")
    print(f"   Durata: {durata} unità di tempo")
    print(f"   Punti calcolati: {len(xs)}")
    print(f"   Distanza finale dal sole: {np.sqrt(xs[-1]**2 + ys[-1]**2):.3f}\n")

simula_orbita(M=100, m=1, r0=10, v0=3, durata=50)
