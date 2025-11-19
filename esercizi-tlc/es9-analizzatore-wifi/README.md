# Es9: Analizzatore WiFi/Bluetooth

**Livello:** INTERMEDIO
**Durata stimata:** 5-6 ore

## Descrizione

Analizzatore di reti wireless che scannerizza canali WiFi e Bluetooth, misura RSSI (Received Signal Strength Indicator), rileva interferenze e visualizza l'occupazione dello spettro radio. Permette l'analisi della qualità e della copertura wireless.

## Obiettivi

### Competenze TLC
- Comprendere lo spettro radio ISM (2.4 GHz, 5 GHz)
- Analizzare RSSI e conversione in dBm
- Identificare canali WiFi (802.11 a/b/g/n/ac)
- Comprendere la larghezza di banda dei canali
- Rilevare interferenze e collisioni
- Calcolare la copertura e la potenza ricevuta

### Competenze Informatica
- Utilizzo di librerie Python per scansione wireless (scapy, wifi, etc.)
- Parsing di frame wireless
- Visualizzazione di dati spaziali
- Mapping di canali e potenza
- Analisi statistica di segnali
- Heatmap e visualizzazione 3D

## Consegna

Il programma deve:

1. **Scansione reti WiFi:**
   - Enumera reti disponibili (SSID, BSSID)
   - Misura RSSI per ogni rete
   - Identifica canale e band (2.4 GHz o 5 GHz)
   - Fornisce info: standard (11a/b/g/n/ac), larghezza banda

2. **Analisi qualità segnale:**
   - Converte RSSI a dBm
   - Valuta qualità: Eccellente (>-50dBm), Buona (-50/-60), Accettabile (-60/-70), Scarsa (<-70)
   - Calcola SNR e SINR (Signal-to-Interference-plus-Noise Ratio)

3. **Mappa canali WiFi:**
   - Canali 2.4 GHz: 1-13 (overlapping)
   - Canali 5 GHz: 36-165 (no overlap)
   - Visualizza occupazione e conflitti
   - Identifica canali interferenti

4. **Rilevamento interferenze:**
   - Identifica reti su stessi canali
   - Misura livello di interferenza
   - Suggerisce canali alternativi
   - Rileva apparecchi Bluetooth

5. **Visualizzazioni:**
   - Grafico RSSI vs canale
   - Heatmap canali
   - Mappa copertura spaziale (simulata)
   - Cronologia scansioni

## Esempio di Utilizzo

```
=== ANALIZZATORE WIFI/BLUETOOTH ===

Scegli modalità:
1. Scansione WiFi semplice
2. Analisi dettagliata canali
3. Rilevamento interferenze
4. Mappa copertura
5. Esci

Scelta: 1

Scansione reti WiFi in corso...
[████████████████████████████████] 100%

Reti trovate: 12

┌─ RETE 1: MyWiFi
│ ├─ BSSID: 00:1A:2B:3C:4D:5E
│ ├─ Canale: 6 (2.4 GHz)
│ ├─ RSSI: -45 dBm
│ ├─ Qualità: ████████░░ 85%
│ ├─ Standard: 802.11n
│ ├─ Larghezza: 40 MHz
│ ├─ Sicurezza: WPA2 (Strong)
│ └─ Segnale: ECCELLENTE ✓

├─ RETE 2: Neighbor
│ ├─ BSSID: 00:1A:2B:3C:4D:5F
│ ├─ Canale: 11 (2.4 GHz)
│ ├─ RSSI: -67 dBm
│ ├─ Qualità: ██████░░░░ 52%
│ ├─ Standard: 802.11g
│ ├─ Larghezza: 20 MHz
│ ├─ Sicurezza: WPA (Weak)
│ └─ Segnale: ACCETTABILE ⚠

└─ RETE 3: Guest
  ├─ BSSID: 00:1A:2B:3C:4D:60
  ├─ Canale: 1 (2.4 GHz)
  ├─ RSSI: -78 dBm
  ├─ Qualità: ████░░░░░░ 38%
  ├─ Standard: 802.11b
  ├─ Larghezza: 20 MHz
  ├─ Sicurezza: Open
  └─ Segnale: SCARSO ✗

--- ANALISI CANALI 2.4 GHz ---

Canale 1 (2412 MHz):  │███████░░│ 2 reti
Canale 6 (2437 MHz):  │██████████│ 5 reti (AFFOLLATO!)
Canale 11 (2462 MHz): │████░░░░░│ 3 reti

Raccomandazioni:
✓ MyWiFi (ch.6) interferirebbe con Neighbor (ch.11)
✗ Neighbor consiglia canale 1 o 13
✗ Guest (ch.1) ha segnale debole

--- RILEVAMENTO INTERFERENZE ---

Interferenze rilevate: 3
├─ MyWiFi (ch.6) ← → Neighbor (ch.11) [Overlap parziale]
├─ Bluetooth in banda: Sì [~2450 MHz]
└─ Potenza interferenza: -72 dBm

Qualità media rete: BUONA (67 dB)
```

## Suggerimenti

- Per WiFi reale, usa librerie: `scapy`, `pyshark`, o `wifi` package
- RSSI tipicamente -20 a -120 dBm
- Mappa frequenze: 2.4 GHz = 2412 + (canale-1)*5 MHz
- Canali 2.4 GHz sovrapposti: 1/6/11 non interferiscono
- Per simulazione: genera dati realistici basati su distanza
- Usa heatmap (seaborn/matplotlib) per visualizzare occupazione
- Calcola SNR da RSSI e noise floor (-95 dBm typical)

## Esempio di Codice Struttura

```python
import subprocess
import re
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List

@dataclass
class ReteWiFi:
    ssid: str
    bssid: str
    canale: int
    rssi: int  # dBm
    standard: str  # 802.11a/b/g/n/ac
    larghezza_banda: int  # MHz
    sicurezza: str

class AnalizzatoreWiFi:
    # Mappatura canale → frequenza (2.4 GHz)
    CANALI_2_4GHZ = {
        i: 2412 + (i - 1) * 5 for i in range(1, 14)
    }

    # Canali non interferenti
    CANALI_NON_INTERFERENTI = {
        1, 6, 11  # Per 2.4 GHz
    }

    def __init__(self):
        self.reti: List[ReteWiFi] = []

    def scansiona_wifi(self):
        """Scansiona reti WiFi (implementazione per Linux/Mac)"""
        try:
            if sys.platform == 'darwin':  # macOS
                result = subprocess.run(
                    ['/System/Library/PrivateFrameworks/Apple80211.framework/'
                     'Versions/Current/Resources/airport', '-s'],
                    capture_output=True, text=True
                )
            else:  # Linux (richiede sudo)
                result = subprocess.run(
                    ['sudo', 'iwlist', 'wlan0', 'scan'],
                    capture_output=True, text=True
                )

            # Parse output
            self._parse_scan_output(result.stdout)

        except Exception as e:
            print(f"Errore scansione: {e}")

    def genera_dati_simulati(self, num_reti=12):
        """Genera dati WiFi simulati per demo"""
        ssids = ['MyWiFi', 'Neighbor', 'Guest', 'HomeNetwork',
                'CoffeeShop', 'Apartment5', 'NETGEAR123', 'TPLink',
                'Vodafone', 'TIM_Router', 'OpenWiFi', 'Vodafone_Guest']

        for i, ssid in enumerate(ssids):
            canale = np.random.choice([1, 6, 11])
            rssi = np.random.randint(-90, -30)
            standard = np.random.choice(['802.11b', '802.11g', '802.11n', '802.11ac'])
            larghezza = 40 if standard == '802.11n' else 20

            rete = ReteWiFi(
                ssid=ssid,
                bssid=f"00:1A:2B:3C:4D:{5*i:02X}",
                canale=canale,
                rssi=rssi,
                standard=standard,
                larghezza_banda=larghezza,
                sicurezza=np.random.choice(['WPA2', 'WPA', 'Open'])
            )
            self.reti.append(rete)

    def valuta_qualita_segnale(self, rssi: int) -> tuple:
        """Valuta qualità in base a RSSI"""
        if rssi > -50:
            return "ECCELLENTE", 90
        elif rssi > -60:
            return "BUONA", 75
        elif rssi > -70:
            return "ACCETTABILE", 50
        else:
            return "SCARSA", 25

    def analizza_canali(self):
        """Analizza occupazione canali"""
        occupazione = {i: 0 for i in range(1, 14)}

        for rete in self.reti:
            occupazione[rete.canale] += 1

        print("\n--- ANALISI OCCUPAZIONE CANALI 2.4 GHz ---\n")
        for canale in sorted(occupazione.keys()):
            freq = self.CANALI_2_4GHZ[canale]
            count = occupazione[canale]

            # Barra di occupazione
            bar = '█' * count + '░' * (10 - count)
            print(f"Canale {canale:2d} ({freq} MHz): │{bar}│ {count} reti")

    def rileva_interferenze(self):
        """Rileva possibili interferenze"""
        interferenze = []

        for i, rete1 in enumerate(self.reti):
            for rete2 in self.reti[i+1:]:
                if rete1.canale == rete2.canale:
                    interferenze.append((rete1.ssid, rete2.ssid, rete1.canale))

        print(f"\nInterferenze rilevate: {len(interferenze)}")
        for ssid1, ssid2, canale in interferenze:
            print(f"  ✗ {ssid1} ↔ {ssid2} (stesso canale {canale})")

        return interferenze

    def visualizza_reti(self):
        """Visualizza lista reti ordinata per RSSI"""
        print("\n=== RETI WIFI TROVATE ===\n")

        reti_ordinate = sorted(self.reti, key=lambda r: r.rssi, reverse=True)

        for i, rete in enumerate(reti_ordinate, 1):
            qualita, percentuale = self.valuta_qualita_segnale(rete.rssi)
            barra = '█' * (percentuale // 10) + '░' * (10 - percentuale // 10)

            print(f"┌─ RETE {i}: {rete.ssid}")
            print(f"│ ├─ BSSID: {rete.bssid}")
            print(f"│ ├─ Canale: {rete.canale} (2.4 GHz)")
            print(f"│ ├─ RSSI: {rete.rssi} dBm")
            print(f"│ ├─ Qualità: {barra} {percentuale}%")
            print(f"│ ├─ Standard: {rete.standard}")
            print(f"│ ├─ Larghezza: {rete.larghezza_banda} MHz")
            print(f"│ ├─ Sicurezza: {rete.sicurezza}")
            print(f"│ └─ Segnale: {qualita}")
            print()

    def grafica_rssi_vs_canale(self):
        """Visualizza RSSI vs canale"""
        canali = [r.canale for r in self.reti]
        rssi_vals = [r.rssi for r in self.reti]
        ssids = [r.ssid for r in self.reti]

        plt.figure(figsize=(10, 6))
        plt.scatter(canali, rssi_vals, s=100, alpha=0.6)

        for i, ssid in enumerate(ssids):
            plt.annotate(ssid, (canali[i], rssi_vals[i]),
                        fontsize=8, alpha=0.7)

        plt.xlabel('Canale WiFi')
        plt.ylabel('RSSI (dBm)')
        plt.title('Potenza Ricevuta vs Canale')
        plt.grid(True, alpha=0.3)
        plt.xticks(range(1, 14))
        plt.show()

# Utilizzo
analizzatore = AnalizzatoreWiFi()
analizzatore.genera_dati_simulati()
analizzatore.visualizza_reti()
analizzatore.analizza_canali()
analizzatore.rileva_interferenze()
analizzatore.grafica_rssi_vs_canale()
```

## Parametri WiFi Importanti

- **RSSI:** -30 dBm (eccellente) a -100 dBm (pessimo)
- **2.4 GHz:** 2412-2472 MHz, 13 canali (1-13)
- **5 GHz:** 5170-5825 MHz, 36+ canali (no overlap)
- **Larghezza banda:** 20 MHz (legacy), 40 MHz (HT), 80/160 MHz (VHT)
- **Standard:** 802.11a (5GHz), 802.11b (2.4GHz lento), 802.11g (2.4GHz 54Mbps), 802.11n (HT), 802.11ac (VHT)

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 📶📡**
