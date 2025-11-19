# Simulatore Moto - SOLUZIONE
import numpy as np
import matplotlib.pyplot as plt

def moto_parabolico(v0, angolo_gradi, g=9.81):
    """Simula moto del proiettile"""
    angolo = np.radians(angolo_gradi)
    v0x = v0 * np.cos(angolo)
    v0y = v0 * np.sin(angolo)

    # Tempo di volo
    t_volo = 2 * v0y / g
    # Gittata
    gittata = v0x * t_volo
    # Altezza max
    h_max = (v0y**2) / (2*g)

    # Traiettoria
    t = np.linspace(0, t_volo, 100)
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2

    # Grafici
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Traiettoria
    ax1.plot(x, y, 'b-', linewidth=2)
    ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax1.set_xlabel('x (m)')
    ax1.set_ylabel('y (m)')
    ax1.set_title(f'Moto Parabolico (v₀={v0} m/s, θ={angolo_gradi}°)')
    ax1.grid(True, alpha=0.3)

    # Velocità nel tempo
    vx = v0x * np.ones_like(t)
    vy = v0y - g * t
    v_tot = np.sqrt(vx**2 + vy**2)

    ax2.plot(t, vx, label='vₓ(t)')
    ax2.plot(t, vy, label='vᵧ(t)')
    ax2.plot(t, v_tot, label='|v|(t)', linewidth=2)
    ax2.set_xlabel('Tempo (s)')
    ax2.set_ylabel('Velocità (m/s)')
    ax2.set_title('Componenti Velocità')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('moto_parabolico.png', dpi=150)
    plt.show()

    print(f"\n🚀 MOTO DEL PROIETTILE")
    print(f"   Velocità iniziale: {v0} m/s")
    print(f"   Angolo: {angolo_gradi}°")
    print(f"   Tempo di volo: {t_volo:.2f} s")
    print(f"   Gittata: {gittata:.2f} m")
    print(f"   Altezza massima: {h_max:.2f} m\n")

def main():
    print("=== SIMULATORE DI MOTO ===\n")
    v0 = float(input("Velocità iniziale (m/s): ") or "20")
    angolo = float(input("Angolo (gradi): ") or "45")
    moto_parabolico(v0, angolo)

if __name__ == "__main__":
    main()
