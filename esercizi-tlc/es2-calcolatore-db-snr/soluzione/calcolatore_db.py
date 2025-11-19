# Calcolatore dB e SNR - SOLUZIONE
import numpy as np

def watt_to_dbm(P_watt):
    """Converti Watt in dBm"""
    return 10 * np.log10(P_watt * 1000)

def dbm_to_watt(P_dbm):
    """Converti dBm in Watt"""
    return 10**(P_dbm/10) / 1000

def db(rapporto):
    """Converti rapporto in dB"""
    return 10 * np.log10(rapporto)

def calcola_snr(P_segnale, P_rumore, unita='dBm'):
    """Calcola SNR"""
    if unita == 'dBm':
        return P_segnale - P_rumore
    else:  # Watt
        return db(P_segnale / P_rumore)

def budget_link(P_tx_dbm, G_tx_dB, L_dB, G_rx_dB):
    """Calcola budget di collegamento"""
    P_rx_dbm = P_tx_dbm + G_tx_dB - L_dB + G_rx_dB
    return P_rx_dbm

def main():
    print("=== CALCOLATORE dB e SNR ===\n")
    print("1. Conversione Watt ↔ dBm")
    print("2. Calcolo SNR")
    print("3. Budget di collegamento")

    scelta = input("\nScegli (1-3): ")

    if scelta == "1":
        P = float(input("Potenza in Watt: "))
        print(f"   {P} W = {watt_to_dbm(P):.2f} dBm")

    elif scelta == "2":
        P_sig = float(input("Potenza segnale (dBm): "))
        P_noise = float(input("Potenza rumore (dBm): "))
        SNR = calcola_snr(P_sig, P_noise)
        print(f"\n📊 SNR = {SNR:.2f} dB")

    elif scelta == "3":
        P_tx = float(input("Potenza TX (dBm): "))
        G_tx = float(input("Guadagno antenna TX (dB): "))
        L = float(input("Perdite propagazione (dB): "))
        G_rx = float(input("Guadagno antenna RX (dB): "))
        P_rx = budget_link(P_tx, G_tx, L, G_rx)
        print(f"\n📡 Potenza ricevuta: {P_rx:.2f} dBm")
        print(f"   In Watt: {dbm_to_watt(P_rx):.2e} W")

if __name__ == "__main__":
    main()
