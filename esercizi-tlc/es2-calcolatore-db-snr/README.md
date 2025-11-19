# Es2: Calcolatore dB e SNR

**Livello:** FACILE
**Durata stimata:** 3-4 ore

## Descrizione

Calcolatore interattivo per conversioni tra unità di potenza (Watt, dBm, dB) e calcolo del Signal-to-Noise Ratio (SNR). Permette l'analisi del budget di collegamento radio/cablato e verifica della qualità del segnale.

## Obiettivi

### Competenze TLC
- Comprendere le conversioni dB/dBm/Watt
- Calcolare il Signal-to-Noise Ratio (SNR)
- Analizzare il budget di collegamento
- Comprendere i fattori di perdita di segnale (path loss, attenuazione)
- Applicare formule di telecomunicazioni in pratica

### Competenze Informatica
- Funzioni per conversioni logaritmiche
- Interfaccia utente interattiva
- Validazione di input numerici
- Utilizzo di librerie di calcolo scientifico (numpy)
- Gestione di errori e casi limite

## Consegna

Il programma deve:

1. **Convertire Watt ↔ dBm ↔ dB:**
   - Watt a dBm: `P(dBm) = 10 * log10(P(mW))`
   - dBm a Watt: `P(mW) = 10^(P(dBm)/10)`
   - Aggiungere/sottrarre dB per amplificazione/attenuazione

2. **Calcolare SNR:**
   - Da potenza segnale e rumore: `SNR(dB) = 10 * log10(P_segnale / P_rumore)`
   - Capacità del canale Shannon: `C = B * log2(1 + SNR_lineare)`

3. **Analizzare Budget di Collegamento:**
   - Potenza trasmessa - Perdite + Guadagni - Rumore = Potenza ricevuta
   - Verifica se il segnale è sopra il noise floor

4. **Menu interattivo con opzioni:**
   - Conversioni singole
   - Calcolo SNR
   - Analisi budget collegamento
   - Salvataggio risultati

## Esempio di Utilizzo

```
=== CALCOLATORE dB E SNR ===

Scegli operazione:
1. Converti Watt ↔ dBm
2. Converti Potenza → dB
3. Calcola SNR
4. Analizza Budget di Collegamento
5. Esci

Scelta: 3

Inserisci Potenza Segnale (dBm): 10
Inserisci Potenza Rumore (dBm): -80

SNR = 10 - (-80) = 90 dB
SNR lineare = 10^(90/10) = 1000000000
Capacità Canale (B=1MHz) = 1000000 * log2(1+1000000000) ≈ 29.9 Mbps

Risultato: Segnale BUONO ✓
```

## Suggerimenti

- Usa `math.log10()` per conversioni logaritmiche
- Ricorda: dB è una grandezza relativa, dBm è assoluta (riferita a 1mW)
- Crea funzioni separate per ogni tipo di conversione
- Usa dizionari per memorizzare i risultati intermedi
- Gestisci gli errori per potenze negative o valori nulli
- Fai attenzione ai fattori di scala (mW vs W)

## Esempio di Codice Struttura

```python
import math

# Conversioni base
def watt_to_dbm(potenza_w):
    """Converti Watt a dBm"""
    if potenza_w <= 0:
        return None
    potenza_mw = potenza_w * 1000
    return 10 * math.log10(potenza_mw)

def dbm_to_watt(potenza_dbm):
    """Converti dBm a Watt"""
    potenza_mw = 10 ** (potenza_dbm / 10)
    return potenza_mw / 1000

def calcola_snr(p_segnale_dbm, p_rumore_dbm):
    """Calcola SNR in dB e in scala lineare"""
    snr_db = p_segnale_dbm - p_rumore_dbm
    snr_lineare = 10 ** (snr_db / 10)
    return snr_db, snr_lineare

def capacita_canale(banda_hz, snr_lineare):
    """Shannon capacity: C = B * log2(1 + SNR)"""
    import math
    return banda_hz * math.log2(1 + snr_lineare)

# Menu principale
while True:
    print("\n=== CALCOLATORE dB e SNR ===")
    print("1. Watt → dBm")
    print("2. dBm → Watt")
    print("3. Calcola SNR")
    print("4. Esci")

    scelta = input("\nScelta: ")

    if scelta == "1":
        w = float(input("Inserisci Watt: "))
        dbm = watt_to_dbm(w)
        print(f"{w} W = {dbm:.2f} dBm")
```

## Formule Fondamentali

- **Watt → dBm:** `P(dBm) = 10 * log₁₀(P(W) * 1000)`
- **dBm → Watt:** `P(W) = 10^(P(dBm)/10) / 1000`
- **SNR (dB):** `SNR(dB) = P_segnale(dBm) - P_rumore(dBm)`
- **Capacità (Shannon):** `C(bps) = B(Hz) * log₂(1 + SNR_lineare)`

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 📊📡**
