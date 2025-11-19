# Pendolo Animato - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simula_pendolo(L=1.0, theta0=30, durata=10):
    """Animazione pendolo semplice"""
    g = 9.81
    omega = np.sqrt(g/L)  # frequenza angolare
    T = 2*np.pi/omega  # periodo

    t = np.linspace(0, durata, 500)
    theta = np.radians(theta0) * np.cos(omega * t)

    # Setup grafico
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Pendolo
    ax1.set_xlim(-L*1.5, L*1.5)
    ax1.set_ylim(-L*1.5, 0.5)
    ax1.set_aspect('equal')
    line, = ax1.plot([], [], 'o-', lw=2, markersize=15)
    ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)

    # Grafico angolo nel tempo
    ax2.plot(t, np.degrees(theta))
    ax2.set_xlabel('Tempo (s)')
    ax2.set_ylabel('Angolo (°)')
    ax2.set_title(f'Oscillazione (T={T:.2f}s)')
    ax2.grid(True, alpha=0.3)
    punto_tempo, = ax2.plot([], [], 'ro', markersize=10)

    def animate(i):
        x = [0, L*np.sin(theta[i])]
        y = [0, -L*np.cos(theta[i])]
        line.set_data(x, y)
        punto_tempo.set_data([t[i]], [np.degrees(theta[i])])
        return line, punto_tempo

    anim = FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)
    plt.tight_layout()
    plt.show()

    print(f"\n⚖️ PENDOLO SEMPLICE")
    print(f"   Lunghezza: {L} m")
    print(f"   Angolo iniziale: {theta0}°")
    print(f"   Periodo: {T:.3f} s")
    print(f"   Frequenza: {1/T:.3f} Hz\n")

simula_pendolo(L=1.5, theta0=45, durata=10)
