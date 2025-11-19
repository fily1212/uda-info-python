# Onde e Interferenza - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt

def onda_1d(A=1, lambd=1, T=1, durata=5):
    """Visualizza onda sinusoidale"""
    x = np.linspace(0, 10, 500)
    t_vals = np.linspace(0, durata, 100)

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, t in enumerate(t_vals[::10]):
        y = A * np.sin(2*np.pi*(x/lambd - t/T))
        ax.clear()
        ax.plot(x, y, 'b-', linewidth=2)
        ax.set_ylim(-A*1.5, A*1.5)
        ax.set_xlabel('Posizione x')
        ax.set_ylabel('Ampiezza y')
        ax.set_title(f'Onda Sinusoidale (t={t:.2f}s)')
        ax.grid(True, alpha=0.3)
        plt.pause(0.1)

    plt.show()

def interferenza_2_sorgenti():
    """Interferenza di due sorgenti puntiformi"""
    size = 200
    x = np.linspace(-5, 5, size)
    y = np.linspace(-5, 5, size)
    X, Y = np.meshgrid(x, y)

    # Posizione sorgenti
    x1, y1 = -1, 0
    x2, y2 = 1, 0

    # Distanze
    r1 = np.sqrt((X - x1)**2 + (Y - y1)**2)
    r2 = np.sqrt((X - x2)**2 + (Y - y2)**2)

    # Onde
    k = 2 * np.pi / 1.0  # numero d'onda
    onda1 = np.sin(k * r1) / (r1 + 0.1)
    onda2 = np.sin(k * r2) / (r2 + 0.1)

    # Interferenza
    interferenza = onda1 + onda2

    # Visualizza
    plt.figure(figsize=(10, 8))
    plt.imshow(interferenza, extent=[-5, 5, -5, 5], cmap='RdBu', vmin=-2, vmax=2)
    plt.colorbar(label='Ampiezza')
    plt.plot([x1, x2], [y1, y2], 'ko', markersize=10, label='Sorgenti')
    plt.title('Interferenza di Due Sorgenti')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.savefig('interferenza.png', dpi=150)
    plt.show()

    print("\n🌊 INTERFERENZA")
    print("   Due sorgenti puntiformi")
    print("   Pattern di interferenza costruttiva/distruttiva\n")

def main():
    print("=== SIMULATORE ONDE ===\n")
    print("1. Onda sinusoidale 1D")
    print("2. Interferenza 2 sorgenti")

    scelta = input("\nScegli (1-2): ")

    if scelta == "1":
        onda_1d(A=1, lambd=2, T=1, durata=5)
    elif scelta == "2":
        interferenza_2_sorgenti()

if __name__ == "__main__":
    main()
