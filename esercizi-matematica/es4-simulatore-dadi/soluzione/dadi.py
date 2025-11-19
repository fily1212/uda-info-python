# Simulatore Dadi - SOLUZIONE
import random
import matplotlib.pyplot as plt

def lancia_dadi(n_dadi=2, n_lanci=1000):
    """Simula lancio di n dadi per n_lanci volte"""
    risultati = []

    for _ in range(n_lanci):
        lancio = sum(random.randint(1, 6) for _ in range(n_dadi))
        risultati.append(lancio)

    # Statistiche
    print(f"🎲 SIMULAZIONE {n_dadi} DAD{'O' if n_dadi == 1 else 'I'}")
    print(f"   Lanci: {n_lanci}")
    print(f"   Media: {sum(risultati)/len(risultati):.2f}")
    print(f"   Valore più frequente: {max(set(risultati), key=risultati.count)}")
    print(f"   Min: {min(risultati)}, Max: {max(risultati)}")

    # Distribuzione
    plt.figure(figsize=(10, 6))
    plt.hist(risultati, bins=range(n_dadi, 6*n_dadi+2),
             edgecolor='black', alpha=0.7)
    plt.xlabel('Somma')
    plt.ylabel('Frequenza')
    plt.title(f'Distribuzione {n_lanci} lanci di {n_dadi} dadi')
    plt.grid(True, alpha=0.3)

    # Media teorica
    media_teorica = 3.5 * n_dadi
    plt.axvline(media_teorica, color='r', linestyle='--',
                label=f'Media teorica: {media_teorica}')
    plt.legend()
    plt.savefig('dadi.png', dpi=150)
    plt.show()

def main():
    print("=== SIMULATORE DADI ===\n")
    n_dadi = int(input("Numero dadi (default 2): ") or "2")
    n_lanci = int(input("Numero lanci (default 1000): ") or "1000")
    lancia_dadi(n_dadi, n_lanci)

if __name__ == "__main__":
    main()
