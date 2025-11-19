# Statistica Descrittiva - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt

def calcola_statistiche(dati):
    """Calcola statistiche descrittive"""
    dati = np.array(dati)

    stats = {
        'media': np.mean(dati),
        'mediana': np.median(dati),
        'moda': None,  # calcolata dopo
        'varianza': np.var(dati),
        'dev_std': np.std(dati),
        'min': np.min(dati),
        'max': np.max(dati),
        'range': np.ptp(dati),
        'q1': np.percentile(dati, 25),
        'q3': np.percentile(dati, 75)
    }

    # Moda (valore più frequente)
    valori, conteggi = np.unique(dati, return_counts=True)
    stats['moda'] = valori[np.argmax(conteggi)]

    return stats

def visualizza_dati(dati):
    """Visualizza dati con istogramma e boxplot"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Istogramma
    ax1.hist(dati, bins=10, edgecolor='black', alpha=0.7)
    ax1.axvline(np.mean(dati), color='r', linestyle='--', label='Media')
    ax1.axvline(np.median(dati), color='g', linestyle='--', label='Mediana')
    ax1.set_xlabel('Valore')
    ax1.set_ylabel('Frequenza')
    ax1.set_title('Istogramma')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Boxplot
    ax2.boxplot(dati, vert=True)
    ax2.set_ylabel('Valore')
    ax2.set_title('Boxplot')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('statistica.png', dpi=150)
    plt.show()

def main():
    print("=== STATISTICA DESCRITTIVA ===\n")

    # Input dati
    dati_str = input("Inserisci dati (separati da spazio): ")
    dati = list(map(float, dati_str.split()))

    stats = calcola_statistiche(dati)

    print(f"\n📊 STATISTICHE ({len(dati)} valori):")
    print(f"   Media: {stats['media']:.2f}")
    print(f"   Mediana: {stats['mediana']:.2f}")
    print(f"   Moda: {stats['moda']:.2f}")
    print(f"   Varianza: {stats['varianza']:.2f}")
    print(f"   Dev. Standard: {stats['dev_std']:.2f}")
    print(f"   Min: {stats['min']:.2f}")
    print(f"   Max: {stats['max']:.2f}")
    print(f"   Range: {stats['range']:.2f}")
    print(f"   Q1 (25%): {stats['q1']:.2f}")
    print(f"   Q3 (75%): {stats['q3']:.2f}")
    print(f"   IQR: {stats['q3'] - stats['q1']:.2f}")

    visualizza_dati(dati)

if __name__ == "__main__":
    # Demo con dati esempio
    dati_demo = [23, 45, 67, 45, 89, 12, 34, 56, 45, 78, 90, 23, 45, 67, 89]
    print("Demo con dati:", dati_demo)
    stats = calcola_statistiche(dati_demo)
    print(f"Media: {stats['media']:.2f}")
    visualizza_dati(dati_demo)
