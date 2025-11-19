# Es5: Simulatore Protocolli

**Livello:** AVANZATO
**Durata stimata:** 8-10 ore

## Descrizione

Simulatore di protocolli di comunicazione affidabili (ARQ): Stop-and-Wait, Go-Back-N e Sliding Window. Permette di analizzare performance in condizioni di errore e delay, visualizzando i meccanismi di ritrasmissione e controllo di flusso.

## Obiettivi

### Competenze TLC
- Comprendere i protocolli ARQ (Automatic Repeat reQuest)
- Implementare meccanismi di ritrasmissione e timeout
- Analizzare l'impatto di latenza e tasso d'errore sulla throughput
- Comprendere windowing e buffering
- Calcolare l'efficienza dei diversi protocolli

### Competenze Informatica
- Programmazione ad eventi (event-driven simulation)
- Gestione di code (queue) e buffer
- Implementazione di state machine per ricevitore/trasmettitore
- Logging e tracciamento di messaggi
- Analisi delle performance e visualizzazione risultati

## Consegna

Il programma deve implementare:

1. **Stop-and-Wait (SSW):**
   - Trasmettitore invia 1 frame, attende ACK
   - Se timeout → ritrasmette
   - Efficienza: η = Tp / (Tp + 2*Td + Tprop) dove Tp=tempo frame, Td=delay
   - Numero di sequenza: 0, 1, 0, 1, ...

2. **Go-Back-N (GBN):**
   - Trasmettitore invia fino a N frame consecutivi
   - Ricevitore richiede ritrasmissione di tutti i frame da K in poi (NAK)
   - Window size: W = 1 + 2a, dove a = Tprop/Tp
   - Efficienza: η = W / (1 + 2a) se senza errori

3. **Sliding Window (SW) - Selective Repeat:**
   - Trasmettitore invia fino a N frame, mantiene buffer di ritrasmissione
   - Ricevitore buffra frame out-of-order, richiede solo frame mancanti
   - Numero sequenza: 0 a 2N-1
   - Più efficiente di GBN ma richiede buffer

4. **Simulazione con parametri:**
   - Dimensione frame (byte)
   - Velocità canale (bps)
   - BER (Bit Error Rate)
   - Propagation delay (ms)
   - Window size (per GBN/SW)
   - Durata simulazione

5. **Analisi e statistiche:**
   - Numero frame trasmessi/ritrasmessi
   - Numero ACK ricevuti
   - Throughput netto (dati utili / tempo totale)
   - Utilizzo canale (%)
   - Media ritrasmissioni per frame

## Esempio di Utilizzo

```
=== SIMULATORE PROTOCOLLI ARQ ===

Parametri canale:
- Velocità: 1 Mbps
- Propagation delay: 10 ms
- BER: 0.001 (0.1%)
- Frame size: 1000 bit

Scegli protocollo:
1. Stop-and-Wait (W=1)
2. Go-Back-N (W=32)
3. Sliding Window (W=32)
4. Confronto tutti

Scelta: 2

--- Go-Back-N: Window Size = 32 ---

Simulazione in corso...
[████████████████████████████████] 100%

Risultati:
├─ Tempo simulazione: 100 sec
├─ Frame trasmessi: 1234 (incl. ritrasmissioni)
├─ Frame persi: 67
├─ Ritrasmissioni: 234
├─ Throughput lordo: 1 Mbps
├─ Throughput netto: 892 kbps
└─ Efficienza: 89.2%

Dettagli trasmissioni:
Frame  0: TX[10ms] RX[30ms] ✓
Frame  1: TX[20ms] RX[40ms] ✓
Frame  2: TX[30ms] LOST[50ms] RETX[210ms] ✓
Frame  3: TX[40ms] LOST[60ms] (va in GBN)
...
```

## Suggerimenti

- Usa una classe per simulare trasmettitore e ricevitore
- Implementa timeout con `time.time()` o evento virtuale
- Mantieni log di tutti i frame: (ID, TX_time, RX_time, RX_status)
- Simula errori casualmente: `if random.random() < BER_per_frame`
- Usa code (collections.deque) per buffer trasmettitore/ricevitore
- Calcola BER per frame dai bit: P_frame_error = 1 - (1-BER)^frame_size
- Visualizza timeline con eventi TX/RX/TIMEOUT

## Esempio di Codice Struttura

```python
import random
import time
from collections import deque
from dataclasses import dataclass
from enum import Enum

class Stato(Enum):
    ATTESA_ACK = 1
    PRONTO = 2
    TIMEOUT = 3

@dataclass
class Frame:
    id: int
    data: bytes
    timestamp_tx: float
    timestamp_rx: float = None
    status: str = "PENDING"  # PENDING, SENT, LOST, ACK_RX

class StopAndWait:
    def __init__(self, velocita_bps, frame_size, ber, prop_delay_ms):
        self.velocita_bps = velocita_bps
        self.frame_size = frame_size
        self.ber = ber
        self.prop_delay = prop_delay_ms / 1000  # converti in sec
        self.timeout = self.prop_delay * 2 + frame_size * 8 / velocita_bps

        self.frame_in_flight = None
        self.seq_num = 0
        self.stats = {
            'tx': 0, 'rx': 0, 'lost': 0,
            'retx': 0, 'ack': 0
        }

    def calcola_ber_frame(self):
        """Probabilità errore per intero frame"""
        return 1 - (1 - self.ber) ** self.frame_size

    def trasmetti_frame(self, frame_id, tempo_attuale):
        """Trasmette frame e imposta timer"""
        frame = Frame(id=frame_id, data=b'X'*self.frame_size,
                     timestamp_tx=tempo_attuale)

        # Simula perdita per errore
        if random.random() < self.calcola_ber_frame():
            frame.status = "LOST"
            self.stats['lost'] += 1
            return None

        frame.status = "SENT"
        self.stats['tx'] += 1
        self.frame_in_flight = frame
        return frame

    def ricevi_ack(self, frame_id, tempo_attuale):
        """Riceve ACK per frame"""
        if self.frame_in_flight and self.frame_in_flight.id == frame_id:
            self.frame_in_flight.status = "ACK_RX"
            self.frame_in_flight.timestamp_rx = tempo_attuale
            self.stats['ack'] += 1
            self.seq_num = (self.seq_num + 1) % 2
            return True
        return False

    def timeout_handler(self):
        """Gestisce timeout - ritrasmette"""
        if self.frame_in_flight:
            self.stats['retx'] += 1
            self.frame_in_flight.status = "PENDING"

class Simulatore:
    def __init__(self, protocollo, durata_sec=100):
        self.protocollo = protocollo
        self.durata = durata_sec
        self.tempo = 0
        self.events = []

    def run(self):
        """Esegui simulazione"""
        frame_id = 0
        while self.tempo < self.durata:
            self.tempo += 0.001  # step di 1ms

            # Trasmetti nuovo frame se pronto
            if self.tempo % 0.01 == 0:  # ogni 10ms
                self.protocollo.trasmetti_frame(frame_id, self.tempo)
                frame_id += 1

            # Simula ricezione ACK
            # ... logica di propagazione delay ...

            # Controlla timeout
            # ... logica timeout ...

# Utilizzo
protocollo = StopAndWait(velocita_bps=1e6, frame_size=1000,
                        ber=0.001, prop_delay_ms=10)
sim = Simulatore(protocollo, durata_sec=100)
sim.run()
print(protocollo.stats)
```

## Performance: Formula di Efficiency

- **Stop-and-Wait:** η = 1/(1 + 2a) dove a = Tprop/Tframe
- **Go-Back-N:** η = W/(1 + 2a·Pd) dove Pd = prob. frame error
- **Sliding Window:** η = W (ideale, senza errori)

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🔄📡**
