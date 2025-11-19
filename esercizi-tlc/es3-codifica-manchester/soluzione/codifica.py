# Codifica Manchester/NRZ - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt

def nrz_encode(bits):
    """Codifica NRZ: 0→-1, 1→+1"""
    return np.array([1 if b else -1 for b in bits])

def manchester_encode(bits):
    """Codifica Manchester: 0→[-1,+1], 1→[+1,-1]"""
    signal = []
    for bit in bits:
        if bit == 0:
            signal.extend([-1, 1])
        else:
            signal.extend([1, -1])
    return np.array(signal)

def plot_codifiche(bits):
    nrz = nrz_encode(bits)
    manchester = manchester_encode(bits)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8))

    # Bits
    ax1.step(range(len(bits)), bits, where='post', linewidth=2)
    ax1.set_ylabel('Bit')
    ax1.set_title('Dati Digitali')
    ax1.grid(True, alpha=0.3)

    # NRZ
    ax2.step(range(len(nrz)), nrz, where='post', linewidth=2, color='blue')
    ax2.set_ylabel('Ampiezza')
    ax2.set_title('Codifica NRZ')
    ax2.grid(True, alpha=0.3)

    # Manchester
    t_manchester = np.linspace(0, len(bits), len(manchester))
    ax3.step(t_manchester, manchester, where='post', linewidth=2, color='red')
    ax3.set_ylabel('Ampiezza')
    ax3.set_xlabel('Tempo')
    ax3.set_title('Codifica Manchester')
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('codifiche.png', dpi=150)
    plt.show()

bits = [1, 0, 1, 1, 0, 0, 1, 0, 1]
print("💾 Bits:", bits)
plot_codifiche(bits)
