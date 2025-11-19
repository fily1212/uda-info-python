# Campionamento e Nyquist - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt

def dimostra_aliasing(f_segnale=5, fs_campionamento=8):
    """Dimostra aliasing e teorema di Nyquist"""
    t_continuo = np.linspace(0, 2, 1000)
    segnale_continuo = np.sin(2 * np.pi * f_segnale * t_continuo)

    # Campionamento
    t_campionato = np.arange(0, 2, 1/fs_campionamento)
    segnale_campionato = np.sin(2 * np.pi * f_segnale * t_campionato)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(t_continuo, segnale_continuo, 'b-', label='Segnale originale', alpha=0.5)
    plt.stem(t_campionato, segnale_campionato, 'r', label='Campioni')
    plt.title(f'Campionamento: f={f_segnale} Hz, fs={fs_campionamento} Hz')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Ampiezza')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Verifica Nyquist
    f_nyquist = fs_campionamento / 2
    if f_segnale <= f_nyquist:
        plt.text(0.5, 0.9, '✓ Nyquist rispettato', transform=plt.gca().transAxes,
                 bbox=dict(boxstyle='round', facecolor='green', alpha=0.3))
    else:
        plt.text(0.5, 0.9, '✗ Aliasing!', transform=plt.gca().transAxes,
                 bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

    plt.savefig('nyquist.png', dpi=150)
    plt.show()

    print(f"📏 Frequenza Nyquist: {f_nyquist} Hz")
    print(f"   Campionamento {'corretto' if f_segnale <= f_nyquist else 'ERRATO (aliasing)'}")

dimostra_aliasing(f_segnale=5, fs_campionamento=15)  # OK
dimostra_aliasing(f_segnale=10, fs_campionamento=15) # Aliasing!
