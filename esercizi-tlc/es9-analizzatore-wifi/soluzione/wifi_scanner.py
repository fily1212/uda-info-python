# Analizzatore WiFi - SOLUZIONE (Simulato)
import random

def scansiona_reti_wifi(num_reti=5):
    """Simula scansione reti WiFi"""
    canali = [1, 6, 11, 36, 40, 44, 48]  # Canali WiFi comuni
    bande = ['2.4 GHz', '5 GHz']

    print("📶 SCANSIONE RETI WiFi\n")
    print(f"{'SSID':<20} {'Canale':<8} {'Banda':<10} {'RSSI (dBm)':<12} {'Qualità'}")
    print("-" * 70)

    reti = []
    for i in range(num_reti):
        ssid = f"WiFi-{random.choice(['Home', 'Office', 'Public'])}-{i+1}"
        canale = random.choice(canali)
        banda = '2.4 GHz' if canale <= 14 else '5 GHz'
        rssi = random.randint(-90, -30)

        # Qualità segnale
        if rssi >= -50:
            qualita = "★★★★★ Eccellente"
        elif rssi >= -60:
            qualita = "★★★★☆ Buona"
        elif rssi >= -70:
            qualita = "★★★☆☆ Media"
        elif rssi >= -80:
            qualita = "★★☆☆☆ Bassa"
        else:
            qualita = "★☆☆☆☆ Pessima"

        print(f"{ssid:<20} {canale:<8} {banda:<10} {rssi:<12} {qualita}")
        reti.append({'ssid': ssid, 'canale': canale, 'rssi': rssi})

    # Analisi congestione canali
    print(f"\n📊 ANALISI CANALI:")
    canali_usati = {}
    for rete in reti:
        c = rete['canale']
        canali_usati[c] = canali_usati.get(c, 0) + 1

    for canale, count in sorted(canali_usati.items()):
        congestione = "Alta" if count > 2 else "Media" if count > 1 else "Bassa"
        print(f"   Canale {canale}: {count} reti - Congestione {congestione}")

scansiona_reti_wifi(num_reti=8)
