# Simulatore Monte Carlo - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt

def stima_pi(n=100000):
    """Stima π con metodo Monte Carlo"""
    punti_x = np.random.uniform(-1, 1, n)
    punti_y = np.random.uniform(-1, 1, n)
    distanze = punti_x**2 + punti_y**2
    dentro_cerchio = np.sum(distanze <= 1)
    pi_stimato = 4 * dentro_cerchio / n

    # Visualizza
    plt.figure(figsize=(8, 8))
    dentro = distanze <= 1
    plt.scatter(punti_x[dentro], punti_y[dentro], c='blue', s=1, alpha=0.5)
    plt.scatter(punti_x[~dentro], punti_y[~dentro], c='red', s=1, alpha=0.5)
    plt.title(f'Stima di π = {pi_stimato:.5f} (con {n} punti)')
    plt.axis('equal')
    plt.savefig('monte_carlo_pi.png')
    plt.show()

    print(f"\n🎲 Simulazione con {n:,} punti")
    print(f"   π stimato: {pi_stimato:.6f}")
    print(f"   π reale: {np.pi:.6f}")
    print(f"   Errore: {abs(pi_stimato - np.pi):.6f}\n")

def monty_hall(n=10000):
    """Simula problema di Monty Hall"""
    vince_cambiando = 0
    vince_non_cambiando = 0

    for _ in range(n):
        # 3 porte: 0, 1, 2
        auto = np.random.randint(0, 3)
        scelta = np.random.randint(0, 3)

        # Monty apre una porta con capra
        porte = [0, 1, 2]
        porte.remove(scelta)
        if auto in porte:
            porte.remove(auto)
        monty_apre = np.random.choice(porte)

        # Cambia scelta
        porte_rimanenti = [0, 1, 2]
        porte_rimanenti.remove(scelta)
        porte_rimanenti.remove(monty_apre)
        nuova_scelta = porte_rimanenti[0]

        if nuova_scelta == auto:
            vince_cambiando += 1
        if scelta == auto:
            vince_non_cambiando += 1

    print(f"🚪 Problema di Monty Hall ({n} simulazioni)")
    print(f"   Vince cambiando: {vince_cambiando/n*100:.1f}%")
    print(f"   Vince NON cambiando: {vince_non_cambiando/n*100:.1f}%\n")

def main():
    print("=== SIMULATORE MONTE CARLO ===\n")
    print("1. Stima di π")
    print("2. Problema di Monty Hall")

    scelta = input("\nScegli simulazione (1-2): ")

    if scelta == "1":
        n = int(input("Numero punti (default 100000): ") or "100000")
        stima_pi(n)
    elif scelta == "2":
        n = int(input("Numero simulazioni (default 10000): ") or "10000")
        monty_hall(n)

if __name__ == "__main__":
    main()
