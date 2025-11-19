# Es10: Comunicazione Seriale

**Livello:** BASE
**Durata stimata:** 4-5 ore

## Descrizione

Implementazione di comunicazione seriale UART/RS232 con gestione di protocolli seriali, invio/ricezione di dati, parsing di messaggi e comunicazione con dispositivi hardware (simulati o reali).

## Obiettivi

### Competenze TLC
- Comprendere i protocolli seriali (UART, RS232)
- Configurare parametri seriali (baud rate, bit di stop, parità)
- Implementare handshake e controllo di flusso
- Gestire errori e timeout
- Implementare protocolli semplici (ASCII, binari, con checksum)

### Competenze Informatica
- Utilizzo di librerie di comunicazione seriale (pySerial)
- Gestione di porte seriali
- Parsing di dati binari e testuali
- Threading per I/O non-bloccante
- Gestione di buffer e code
- Implementazione di macchine a stati semplici

## Consegna

Il programma deve:

1. **Configurare porta seriale:**
   - Enumera porte disponibili
   - Configura baud rate (9600, 19200, 38400, 115200, etc.)
   - Bit dati (7 o 8)
   - Bit di stop (1 o 2)
   - Parità (None, Odd, Even)
   - Apri/chiudi connessione

2. **Inviare dati:**
   - Invio stringhe ASCII
   - Invio dati binari
   - Gestione newline (CR, LF, CRLF)
   - Controllo tempo di trasmissione

3. **Ricevere dati:**
   - Lettura linea per linea
   - Lettura a dimensione fissa
   - Timeout di ricezione
   - Buffering dati

4. **Protocolli di comunicazione:**
   - **Echo:** Verifica connessione
   - **AT commands:** Formato comando/risposta
   - **CSV:** Dati separati da virgole
   - **Binario:** Strutture dati con checksum
   - **JSON:** Messaggi strutturati

5. **Utilità:**
   - Monitor seriale (visualizza traffic)
   - Logger di comunicazione
   - Simulatore dispositivo (per test)
   - Grafico dati in tempo reale

## Esempio di Utilizzo

```
=== COMUNICAZIONE SERIALE ===

Porte seriali disponibili:
1. COM1 (USB Serial: PL2303)
2. COM3 (Intel Serial)
3. /dev/ttyUSB0 (Raspberry Pi)

Scelta porta: 1

Configurazione porta COM1:
├─ Baud rate: 9600 bps
├─ Bit di dati: 8
├─ Bit di stop: 1
├─ Parità: NONE
├─ Timeout: 1.0 sec
└─ Porta aperta ✓

Menu:
1. Invia comando
2. Leggi risposta
3. Monitor seriale (continuo)
4. Test connessione (echo)
5. Comunica con dispositivo
6. Esci

Scelta: 4

Test Echo:
├─ Invio: "ECHO TEST\n"
├─ Attesa risposta...
├─ Ricevuto: "ECHO TEST\n"
├─ Tempo round-trip: 42 ms
└─ Connessione: ✓ OK

Scelta: 1

Inserisci comando: GET_TEMP

Invio: "GET_TEMP\n"
Risposta ricevuta:
T=25.3°C, H=62%
Pressure=1013mbar

Scelta: 3

Monitor seriale (premi Ctrl+C per uscire):
[13:45:23.123] Ricevuto: Ready
[13:45:24.456] Ricevuto: Waiting for command
[13:45:25.123] Invio: GET_TEMP
[13:45:25.234] Ricevuto: T=25.3°C, H=62%

--- COMUNICAZIONE STRUTTURATA (CSV) ---

Invio dati sensore:
TIMESTAMP,TEMPERATURE,HUMIDITY,PRESSURE
1634567890,25.3,62.5,1013.25

Dati ricevuti e parsati:
├─ Timestamp: 1634567890
├─ Temperatura: 25.3°C
├─ Umidità: 62.5%
├─ Pressione: 1013.25 mbar
└─ Calcoli: ✓ Dati validi
```

## Suggerimenti

- Usa libreria `pyserial`: `pip install pyserial`
- Enumera porte: `serial.tools.list_ports.comports()`
- Test connessione con echo semplice prima di protocolli complessi
- Aggiungi checksum (XOR, CRC) per robustezza
- Implementa timeout per evitare blocchi infiniti
- Usa thread separate per ricezione (non bloccare invio)
- Testa con simulatore prima di hardware reale
- Gestisci disconnessioni e riconnessioni

## Esempio di Codice Struttura

```python
import serial
import serial.tools.list_ports
import time
from datetime import datetime
import threading
from queue import Queue

class ComunicazioneSeriale:
    def __init__(self):
        self.porta = None
        self.is_open = False
        self.buffer_ricezione = Queue()
        self.thread_ricezione = None

    def lista_porte_disponibili(self):
        """Enumera porte seriali disponibili"""
        porte = []
        for porta_info in serial.tools.list_ports.comports():
            porte.append((porta_info.device, porta_info.description))
        return porte

    def apri_porta(self, porta, baud_rate=9600, timeout=1.0):
        """Apre porta seriale con parametri specificati"""
        try:
            self.porta = serial.Serial(
                port=porta,
                baudrate=baud_rate,
                bytesize=serial.EIGHTBITS,
                stopbits=serial.STOPBITS_ONE,
                parity=serial.PARITY_NONE,
                timeout=timeout
            )
            self.is_open = True
            print(f"✓ Porta {porta} aperta a {baud_rate} baud")

            # Avvia thread di ricezione
            self.thread_ricezione = threading.Thread(
                target=self._ricevi_continuo, daemon=True
            )
            self.thread_ricezione.start()

            return True
        except Exception as e:
            print(f"✗ Errore apertura porta: {e}")
            return False

    def chiudi_porta(self):
        """Chiude porta seriale"""
        if self.porta and self.porta.is_open:
            self.porta.close()
            self.is_open = False
            print("Porta chiusa")

    def invia(self, dati, aggiungi_newline=True):
        """Invia dati sulla porta seriale"""
        if not self.is_open:
            print("✗ Porta non aperta")
            return False

        try:
            if isinstance(dati, str):
                dati = dati.encode()

            if aggiungi_newline and not dati.endswith(b'\n'):
                dati += b'\n'

            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            self.porta.write(dati)
            self.porta.flush()

            print(f"[{timestamp}] Invio: {dati.decode('utf-8', errors='ignore').strip()}")
            return True

        except Exception as e:
            print(f"✗ Errore invio: {e}")
            return False

    def _ricevi_continuo(self):
        """Thread di ricezione continua"""
        while self.is_open:
            try:
                if self.porta.in_waiting > 0:
                    linea = self.porta.readline()
                    if linea:
                        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        testo = linea.decode('utf-8', errors='ignore').strip()
                        print(f"[{timestamp}] Ricevuto: {testo}")
                        self.buffer_ricezione.put((timestamp, testo))
                else:
                    time.sleep(0.01)
            except Exception as e:
                print(f"✗ Errore ricezione: {e}")

    def ricevi_risposta(self, timeout=2.0):
        """Riceve una risposta con timeout"""
        try:
            start = time.time()
            while time.time() - start < timeout:
                if not self.buffer_ricezione.empty():
                    timestamp, testo = self.buffer_ricezione.get()
                    return testo
                time.sleep(0.01)

            return None
        except Exception as e:
            print(f"✗ Errore ricezione: {e}")
            return None

    def test_echo(self):
        """Test connessione con echo"""
        print("\nTest ECHO:")
        msg = "ECHO_TEST"

        start = time.time()
        self.invia(msg, aggiungi_newline=True)
        risposta = self.ricevi_risposta(timeout=1.0)
        tempo_round_trip = (time.time() - start) * 1000

        if risposta and msg in risposta:
            print(f"✓ Connessione OK (round-trip: {tempo_round_trip:.0f} ms)")
            return True
        else:
            print("✗ Nessuna risposta")
            return False

    def comunica_comandi(self):
        """Interfaccia per inviare comandi e ricevere risposte"""
        print("\nModalità comando (scrivi 'exit' per uscire):")
        while self.is_open:
            try:
                cmd = input("cmd> ")
                if cmd.lower() == 'exit':
                    break

                self.invia(cmd, aggiungi_newline=True)
                risposta = self.ricevi_risposta(timeout=1.0)

                if risposta:
                    print(f"Risposta: {risposta}")
                else:
                    print("⏱ Timeout - nessuna risposta")

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Errore: {e}")

    def monitor_seriale(self):
        """Monitor continuo della porta seriale"""
        print("\nMonitor seriale (premi Ctrl+C per uscire):")
        try:
            while self.is_open:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nMonitor terminato")

class SimulatorDispositivo:
    """Simula un dispositivo seriale per test"""
    def __init__(self, porta_virtuale="/dev/pts/1"):
        # Nota: Per test reali, usa socat o similare per creare coppie di porte virtuali
        pass

# Utilizzo
def main():
    comm = ComunicazioneSeriale()

    # Mostra porte disponibili
    porte = comm.lista_porte_disponibili()
    print("Porte disponibili:")
    for i, (porta, desc) in enumerate(porte, 1):
        print(f"{i}. {porta} ({desc})")

    # Apri porta
    if porte:
        porta_scelta = porte[0][0]
        if comm.apri_porta(porta_scelta, baud_rate=9600):

            # Test connessione
            comm.test_echo()

            # Menu interattivo
            while True:
                print("\nMenu:")
                print("1. Invia comando")
                print("2. Monitor seriale")
                print("3. Esci")

                scelta = input("Scelta: ")

                if scelta == "1":
                    comm.comunica_comandi()
                elif scelta == "2":
                    comm.monitor_seriale()
                elif scelta == "3":
                    break

            comm.chiudi_porta()

if __name__ == "__main__":
    main()
```

## Parametri Comuni UART

- **Baud rate:** 9600 (default), 19200, 38400, 57600, 115200 bps
- **Bit di dati:** 8 (standard)
- **Bit di stop:** 1 (standard) o 2
- **Parità:** None, Odd, Even
- **Handshake:** RTS/CTS, XON/XOFF
- **Timeout:** 0.5-1.0 sec per reading

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 🔌📡**
