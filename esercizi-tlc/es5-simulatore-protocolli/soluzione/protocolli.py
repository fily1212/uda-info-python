# Simulatore Protocolli - SOLUZIONE
import random

def stop_and_wait(pacchetti, prob_errore=0.1):
    """Protocollo Stop-and-Wait"""
    trasmessi = 0
    ritrasmissioni = 0

    for i, pkt in enumerate(pacchetti):
        successo = False
        while not successo:
            trasmessi += 1
            # Simula trasmissione
            if random.random() > prob_errore:
                successo = True
                print(f"✓ Pacchetto {i}: ACK ricevuto")
            else:
                ritrasmissioni += 1
                print(f"✗ Pacchetto {i}: NACK, ritrasmetto...")

    print(f"\n📊 Statistiche:")
    print(f"   Pacchetti: {len(pacchetti)}")
    print(f"   Trasmissioni totali: {trasmessi}")
    print(f"   Ritrasmissioni: {ritrasmissioni}")
    print(f"   Efficienza: {len(pacchetti)/trasmessi*100:.1f}%")

pacchetti = list(range(10))
stop_and_wait(pacchetti, prob_errore=0.2)
