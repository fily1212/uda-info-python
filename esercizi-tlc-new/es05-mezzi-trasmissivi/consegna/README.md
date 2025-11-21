# ES05 - Mezzi Trasmissivi e Attenuazione del Segnale 📡

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐⭐ BASE |
| **Durata Stimata** | 3-4 ore |
| **Linguaggio** | Python 3.8+ |
| **Librerie Richieste** | matplotlib, numpy (opzionale) |
| **Prerequisiti** | ES03 Legge di Ohm, ES04 Circuiti |
| **Argomento TLC** | Infrastruttura: tipi mezzi, parametri, attenuazione |

---

## 🎓 Concetti Fondamentali

### Cosa sono i Mezzi Trasmissivi? 📡

Un **mezzo trasmissivo** è il canale fisico attraverso il quale si propagano i segnali di comunicazione.

```
Schema generale:
┌─────────────┐        Mezzo Trasmissivo        ┌─────────────┐
│  SORGENTE   │ ──────────────────────────────> │ DESTINATARIO│
│  (Trasmitter)│      (Cavo, Aria, Fibra)       │  (Receiver) │
└─────────────┘                                  └─────────────┘
  P_tx (Potenza                              P_rx = P_tx - L
   trasmessa)                                 (Potenza ricevuta,
                                              ridotta da attenuazione)
```

**Caratteristiche principali:**
1. **Velocità di propagazione** - quanto velocemente il segnale viaggia
2. **Attenuazione** - perdita di potenza nel tempo/distanza
3. **Banda passante** - range di frequenze trasmissibili
4. **Capacità** - velocità massima trasmissione dati
5. **Costo** - prezzo per km
6. **Immunità ai disturbi** - resistenza a interferenze

---

## 📋 Tipi di Mezzi Trasmissivi Principali

### 1. Doppino Telefonico (Twisted Pair) 🔌
**Descrizione:** Due fili di rame intrecciati, ricoperti di isolante.

```
Sezione trasversale:
    ┌─────┐
    │  ┌─────┐
    │  │ Isolante
    │  │ Rame
    │  └─────┘
    └─────┘
    Diametro: ~1 mm
```

**Parametri:**
```
Velocità propagazione:     c' ≈ 0.6-0.77 × c (in rame)
Attenuazione tipica:       2-6 dB/km @ 1 MHz
Distanza massima:          100-200 m (cablaggio strutturato)
Banda passante:            Fino a 100 MHz (Cat 6)
                           Fino a 600 MHz (Cat 6A)
                           Fino a 10 GHz (Cat 8)
Impedenza caratteristica:  100 Ω (Ethernet)
Costo:                     Molto basso (~0.10-0.50 €/metro)
Applicazioni:              Telefonia, LAN (Ethernet)
Immunità disturbi:         MEDIA (interferenze vicine)
```

**Varianti:**
- **UTP** (Unshielded): Senza schermo
- **FTP** (Foiled): Con schermo lamina
- **STP** (Shielded): Schermo intrecciato (migliore)

**Esempio:** Cat 5e per Gigabit Ethernet in ufficio

### 2. Cavo Coassiale 📺
**Descrizione:** Conduttore centrale circondata da schermo metallico, tutto isolato.

```
Sezione trasversale:
    ┌─────────────────┐
    │ Isolante esterno│
    │ ┌───────────────┤
    │ │ Schermo (rame)│
    │ │ ┌─────────────┤
    │ │ │ Isolante    │
    │ │ │ ┌─────────┐ │
    │ │ │ │ Conduttore
    │ │ │ │ centrale
    │ │ │ └─────────┘
    └─┴─┴───────────┘
```

**Parametri:**
```
Velocità propagazione:     c' ≈ 0.66 × c
Attenuazione tipica:       2-15 dB/km @ 1 GHz (dipende tipo)
Distanza massima:          500+ m (bassa attenuazione)
Banda passante:            Fino a 2.5 GHz
Impedenza caratteristica:  50 Ω (RF), 75 Ω (video)
Costo:                     Basso-medio (~0.50-2 €/metro)
Applicazioni:              TV, antenne RF, collegamenti strumentali
Immunità disturbi:         ALTA (schermo protegge)
```

**Tipi:** RG-58 (RF), RG-6 (video), RG-59 (composite)

**Esempio:** Cavo antenna TV domestica

### 3. Fibra Ottica 🌊
**Descrizione:** Sottile filamento di vetro/plastica che propaga segnali luminosi.

```
Sezione trasversale:
         Coating (protezione)
    ┌────────────────────────┐
    │ ┌──────────────────────┤ Cladding (~125 μm)
    │ │ ┌──────────────────┐ │
    │ │ │ Core (Nucleo)    │ │ Monomodal: ~8 μm
    │ │ │ n₁ > n₂          │ │ Multimodal: ~50-62.5 μm
    │ │ └──────────────────┘ │
    │ └──────────────────────┘
    └────────────────────────┘
    Diametro: 250 μm
```

**Parametri:**
```
Velocità propagazione:     c' ≈ 0.66-0.70 × c
Attenuazione tipica:       0.2-0.5 dB/km @ 1.55 μm (INFRAROSSO!)
Distanza massima:          100+ km (senza rigeneratori)
                           Illimitata (con rigeneratori)
Banda passante:            Praticamente illimitata (terabit/s teorici)
Lunghezze d'onda:          850 nm (corto raggio), 1310 nm, 1550 nm (lungo)
Costo:                     ALTO (~5-50 €/metro + componenti)
Applicazioni:              Backbone TLC, intercontinentali, FTTH
Immunità disturbi:         PERFETTA (niente radiazione EM)
Immunità umidit./temp:     ALTA (vetro stabile)
```

**Tipi:**
- **MMF** (Multimodal): Molti modi di propagazione, ~100m
- **SMF** (Singlemodal): Un solo modo, ~100km

**Esempio:** Backbone fibra ottica fra città

### 4. Wireless (Aria) 🛰️
**Descrizione:** Propagazione di onde elettromagnetiche nello spazio libero.

```
Propagazione:
    Trasmettitore ─── Onde EM ──> Ricevitore
    (Antenna TX)  (Frequenza f)  (Antenna RX)

    Distanza d
```

**Parametri:**
```
Velocità propagazione:     c = 3×10⁸ m/s (vuoto)
Attenuazione:             Dipende da frequenza e distanza
                          Path Loss = 20log₁₀(d) + 20log₁₀(f) + cost
Distanza massima:         Dipende da potenza e sensibilità
Banda passante:           Dipende dalla banda di frequenza allocata
Costo:                    Basso (no cavi), alto (infrastruttura)
Applicazioni:             WiFi, 4G/5G, satelliti, radio
Immunità disturbi:        BASSA (interferenze EM)
```

**Varianti:**
- **WiFi**: 2.4 GHz, 5 GHz (per LAN)
- **4G/LTE**: 700 MHz - 2.6 GHz (larga area)
- **5G NR**: 700 MHz - 28 GHz (e oltre)
- **Satelliti**: 10-30 GHz (banda Ku/Ka)
- **Microonde**: 6-38 GHz (point-to-point terrestri)

**Esempio:** Connessione WiFi da router

---

## 📐 Formule Attenuazione e Path Loss

### Attenuazione Generale (Cavi)

```
L = L₀ + α × d

Dove:
- L = Perdita totale [dB]
- L₀ = Perdita dovuta a riflessioni, connettori [dB]
- α = Attenuazione specifica [dB/km] (dipende da frequenza)
- d = Distanza [km]
```

**Esempio pratico:**
```
Collegamento Ethernet Cat 5e @ 100 MHz:
- L₀ = 0.5 dB (connettori)
- α = 2 dB/km
- d = 50 m = 0.05 km
- L = 0.5 + 2 × 0.05 = 0.6 dB
- Segnale perduto: 10^(-0.6/10) ≈ 87% della potenza arriva
```

### Path Loss - Spazio Libero (Wireless)

```
PL = 20 × log₁₀(f) + 20 × log₁₀(d) + 20 × log₁₀(4π/c) - Gt - Gr

Semplificato (in dB):
PL(dB) ≈ 32.4 + 20×log₁₀(f[MHz]) + 20×log₁₀(d[km]) - Gt(dB) - Gr(dB)

Dove:
- f = Frequenza [MHz]
- d = Distanza [km]
- Gt, Gr = Guadagni antenne trasmettitore e ricevitore [dB]
```

**Esempio WiFi:**
```
Dati:
- f = 2400 MHz (banda 2.4 GHz)
- d = 100 m = 0.1 km
- Gt = Gr = 0 dB (antenne omnidirezionali)

PL = 32.4 + 20×log₁₀(2400) + 20×log₁₀(0.1)
   = 32.4 + 67.6 + (-20)
   = 80 dB

Potenza ricevuta:
P_rx = P_tx - PL = 10 dBm - 80 dB = -70 dBm
Sensibilità tipica WiFi: -90 dBm
Margine: 20 dB (buono)
```

### Decibel (dB) - Logaritmico

```
dB (potenza) = 10 × log₁₀(P_out / P_in)

Esempi:
- Rapporto 1:1 (nessuna perdita)  →  0 dB
- Rapporto 10:1 (perdita 90%)     → -10 dB
- Rapporto 1:10 (guadagno 10×)    → +10 dB
- Rapporto 2:1 (perdita 50%)      → -3 dB
- Rapporto 1:2 (raddoppio)        → +3 dB

dBm (potenza assoluta) = 10 × log₁₀(P [mW])
- 0 dBm = 1 mW
- -30 dBm = 1 μW
- 30 dBm = 1 W
- 33 dBm = 2 W
```

---

## 💻 Funzioni Python da Implementare

### Livello 1: Classe MezzoTrasmissivo 🏗️

```python
class MezzoTrasmissivo:
    """
    Rappresenta un mezzo trasmissivo generico.

    Attributi:
    - nome (str): Nome del mezzo (es: "Doppino Cat 5e")
    - tipo (str): Categoria ('cavo_rame', 'coassiale', 'fibra', 'wireless')
    - velocita_propagazione (float): Frazione di c [0-1]
    - attenuazione_db_per_km (float): α [dB/km]
    - banda_max_hz (float): Banda passante [Hz]
    - impedenza_ohm (float): Impedenza caratteristica [Ω]
    - distanza_max_km (float): Distanza massima raccomandata [km]
    - costo_euro_per_metro (float): Costo [€/m]
    """

    def __init__(self, nome, tipo, velocita_propagazione,
                 attenuazione_db_per_km, banda_max_hz, impedenza_ohm,
                 distanza_max_km, costo_euro_per_metro):
        """Inizializza mezzo trasmissivo"""
        self.nome = nome
        self.tipo = tipo
        self.velocita_propagazione = velocita_propagazione
        self.attenuazione_db_per_km = attenuazione_db_per_km
        self.banda_max_hz = banda_max_hz
        self.impedenza_ohm = impedenza_ohm
        self.distanza_max_km = distanza_max_km
        self.costo_euro_per_metro = costo_euro_per_metro

    def calcola_perdita_segnale(self, distanza_km, attenuazione_connettori_db=0.5):
        """
        Calcola perdita di segnale (attenuazione).

        Formula: L = L₀ + α × d

        Args:
            distanza_km (float): Distanza percorsa [km]
            attenuazione_connettori_db (float): Perdita connettori [dB]

        Returns:
            float: Perdita totale [dB]
        """
        # L = attenuazione_connettori_db + attenuazione_specifica × distanza

    def calcola_potenza_ricevuta(self, potenza_trasmessa_dbm, distanza_km):
        """
        Calcola potenza ricevuta.

        P_rx [dBm] = P_tx [dBm] - L [dB]

        Args:
            potenza_trasmessa_dbm (float): Potenza TX [dBm]
            distanza_km (float): Distanza [km]

        Returns:
            float: Potenza RX [dBm]
        """

    def velocita_segnale_ms(self):
        """
        Calcola velocità del segnale in m/s.

        v = velocita_propagazione × c
        dove c = 3×10⁸ m/s

        Returns:
            float: Velocità [m/s]
        """

    def tempo_propagazione(self, distanza_km):
        """
        Calcola tempo di propagazione.

        t = distanza / velocita

        Args:
            distanza_km (float): Distanza [km]

        Returns:
            float: Tempo [secondi]
        """

    def costo_totale(self, lunghezza_m):
        """
        Calcola costo totale del mezzo.

        Args:
            lunghezza_m (float): Lunghezza [m]

        Returns:
            float: Costo totale [€]
        """

    def __str__(self):
        """Rappresentazione leggibile"""
        # Ritornare stringa con parametri principali
```

### Livello 2: Creazione Mezzi Predefiniti 📦

```python
def crea_mezzi_standard():
    """
    Crea istanze di mezzi trasmissivi standard.

    Returns:
        dict: Dizionario di MezzoTrasmissivo
    ```

    Mezzi da creare:
    - 'Doppino Cat 5e'
    - 'Doppino Cat 6'
    - 'Doppino Cat 6A'
    - 'Coassiale RG-6'
    - 'Fibra Monomodal'
    - 'WiFi 2.4GHz'
    - 'WiFi 5GHz'
    - '4G LTE'
    - '5G NR'
    """

    mezzi = {
        'Doppino Cat 5e': MezzoTrasmissivo(
            nome='Doppino Twisted Pair Cat 5e',
            tipo='cavo_rame',
            velocita_propagazione=0.77,
            attenuazione_db_per_km=2.5,  # @ 100 MHz
            banda_max_hz=100e6,
            impedenza_ohm=100,
            distanza_max_km=0.1,
            costo_euro_per_metro=0.20
        ),
        # ... aggiungere altri
    }

    return mezzi
```

### Livello 3: Comparazione Mezzi 📊

```python
def compara_mezzi(lista_mezzi, parametro='capacita'):
    """
    Confronta più mezzi trasmissivi.

    Args:
        lista_mezzi (list): Lista di oggetti MezzoTrasmissivo
        parametro (str): Campo da usare per ordinamento
                        ('banda_max_hz', 'attenuazione', 'distanza_max_km', 'costo')

    Returns:
        str: Tabella ASCII comparativa

    Output formato:
    ┌─────────────────────────────┬─────────┬──────────┬─────────┐
    │ Mezzo                       │ Banda   │ Dista    │ Costo   │
    ├─────────────────────────────┼─────────┼──────────┼─────────┤
    │ Doppino Cat 5e              │ 100MHz  │ 100m     │ 0.20€/m │
    │ Doppino Cat 6               │ 250MHz  │ 100m     │ 0.30€/m │
    ...
    """
```

### Livello 4: Simulazione Path Loss 🛰️

```python
def calcola_path_loss_spazio_libero(frequenza_mhz, distanza_km,
                                    guadagno_tx_db=0, guadagno_rx_db=0):
    """
    Calcola Path Loss per propagazione in spazio libero (wireless).

    Formula semplificata:
    PL(dB) = 32.4 + 20×log₁₀(f[MHz]) + 20×log₁₀(d[km]) - Gt - Gr

    Args:
        frequenza_mhz (float): Frequenza in MHz
        distanza_km (float): Distanza in km
        guadagno_tx_db (float): Guadagno antenna TX [dB]
        guadagno_rx_db (float): Guadagno antenna RX [dB]

    Returns:
        float: Path Loss [dB]

    Esempio:
        >>> calcola_path_loss_spazio_libero(2400, 0.1)
        80.0  # dB
    """
    # Applicare formula
```

### Livello 5: Simulazione Trasmissione con Attenuazione 📡

```python
def simula_trasmissione(mezzo, potenza_tx_dbm, distanza_km,
                       frequenza_hz=None, sensibilita_rx_dbm=-90):
    """
    Simula trasmissione attraverso mezzo.

    Args:
        mezzo (MezzoTrasmissivo): Mezzo trasmissivo
        potenza_tx_dbm (float): Potenza trasmessa [dBm]
        distanza_km (float): Distanza [km]
        frequenza_hz (float): Frequenza (opzionale, per calcoli)
        sensibilita_rx_dbm (float): Sensibilità ricevitore [dBm]

    Returns:
        dict: {
            'potenza_tx_dbm': P_tx,
            'attenuazione_db': L,
            'potenza_rx_dbm': P_rx,
            'margine_db': P_rx - sensibilita_rx,
            'collegamento_ok': P_rx > sensibilita_rx,
            'tempo_propagazione_ms': t,
            'costo_totale_euro': costo
        }
    """
    # Calcolare P_rx = P_tx - attenuazione
    # Verificare margine
    # Calcolare tempo propagazione
```

### Livello 6: Visualizzazione Attenuazione 📈

```python
def disegna_attenuazione(mezzo, potenza_tx_dbm, max_distanza_km=1, step_km=0.01):
    """
    Traccia grafico attenuazione vs distanza.

    Grafico:
    - X: Distanza [km]
    - Y: Potenza ricevuta [dBm]
    - Linea orizzontale: Sensibilità ricevitore

    Mostra il punto limite dove P_rx = sensibilita_rx

    Args:
        mezzo (MezzoTrasmissivo)
        potenza_tx_dbm (float)
        max_distanza_km (float)
        step_km (float)

    Returns:
        matplotlib.figure.Figure
    """
    # Usare matplotlib per tracciare
```

---

## 🌍 Esempi Reali in Telecomunicazioni

### Esempio 1: Cablaggio LAN Aziendale 🏢
```
Progetto:
- Distanza: 50 m
- Velocità desiderata: Gigabit Ethernet (1 Gbps)
- Ambiente: Ufficio

Scelta mezzo:
- Opzione 1: Doppino Cat 5e
  - Attenuazione: 2.5 dB/km × 0.05 km = 0.125 dB
  - Potenza RX: 10 dBm - 0.125 dB = 9.875 dBm (Buono!)
  - Costo: 0.20 €/m × 50 m = 10 €

- Opzione 2: Fibra Monomodal
  - Attenuazione: 0.3 dB/km × 0.05 km = 0.015 dB
  - Potenza RX: 10 dBm - 0.015 dB = 9.985 dBm (Eccellente!)
  - Costo: 20 €/m × 50 m = 1000 € (Troppo caro!)

Conclusione: Usare Cat 5e (rapporto costo-prestazione)
```

### Esempio 2: Collegamento WiFi Domestico 🏠
```
Dati:
- Distanza: 10 m
- Frequenza: 2.4 GHz (WiFi 802.11n)
- Potenza TX: +20 dBm (100 mW)
- Guadagno antenne: 0 dB (omnidirezionali)
- Sensibilità RX: -90 dBm (decente)

Path Loss:
PL = 32.4 + 20×log₁₀(2400) + 20×log₁₀(0.01)
   = 32.4 + 67.6 - 40
   = 60 dB

Potenza ricevuta:
P_rx = 20 - 60 = -40 dBm (Buono!)
Margine: -40 - (-90) = 50 dB (Massimo margine!)

Conclusione: Segnale forte (4-5 tacche)
```

### Esempio 3: Antenna Parabolica RF 📡
```
Collegamento point-to-point 10 GHz:
- Distanza: 5 km
- Frequenza: 10 GHz = 10.000 MHz
- Potenza TX: +30 dBm (1 W)
- Guadagno antenna TX: +40 dB (parabolica)
- Guadagno antenna RX: +40 dB
- Sensibilità RX: -80 dBm

Path Loss (spazio libero):
PL = 32.4 + 20×log₁₀(10000) + 20×log₁₀(5)
   = 32.4 + 80 + 13.98
   = 126.38 dB

Potenza ricevuta:
P_rx = 30 + 40 + 40 - 126.38 = -16.38 dBm (Buono!)
Margine: -16.38 - (-80) = 63.62 dB

Conclusione: Collegamento robusto, affidabile
```

### Esempio 4: Fibra Ottica Backbone 🌐
```
Collegamento intercontinentale:
- Distanza: 1000 km
- Tipo: Fibra monomodal @ 1550 nm
- Attenuazione: 0.2 dB/km
- Larghezza banda: 400+ Tbps teorici
- Potenza trasmessa: +10 dBm
- Sensibilità ricevitore: -35 dBm

Attenuazione totale:
L = 0.5 + 0.2 × 1000 = 200.5 dB

Potenza ricevuta senza rigeneratori:
P_rx = 10 - 200.5 = -190.5 dBm (Impossibile!)

Soluzione: Rigeneratori ogni 80-100 km
Con rigeneratori:
- Rigeneratore prende segnale a -35 dBm
- Lo rigenerai (amplifica e ripulisce)
- Lo ritrasmette a +10 dBm
- Segmento successivo: 80-100 km senza perdita

Conclusione: Affidabilità mondiale di Internet grazie ai rigeneratori
```

### Esempio 5: Rete 5G Mobile 📱
```
Celle 5G:
- Frequenza: 28 GHz (mmWave)
- Distanza: 100 m (raggio cella ridotto)
- Potenza TX: +30 dBm
- Guadagno antenna (MIMO 64×64): +20 dBm equivalente
- Sensibilità RX: -110 dBm (sofisticata)

Path Loss:
PL = 32.4 + 20×log₁₀(28000) + 20×log₁₀(0.1)
   = 32.4 + 89 - 20
   = 101.4 dB

Potenza ricevuta:
P_rx = 30 + 20 - 101.4 = -51.4 dBm (Buono!)
Margine: -51.4 - (-110) = 58.6 dB

Conclusione: Margine abbondante, ma distanza < 4G
per questo le celle 5G sono più piccole
```

---

## 🧪 Test Cases (8-10 casi)

```python
# TEST 1: Classe MezzoTrasmissivo - creazione
mezzo = MezzoTrasmissivo('Test', 'cavo_rame', 0.77, 2.5, 100e6, 100, 0.1, 0.2)
assert mezzo.nome == 'Test'
assert mezzo.velocita_propagazione == 0.77

# TEST 2: Calcolo perdita segnale
L = mezzo.calcola_perdita_segnale(0.1)  # 100 m = 0.1 km
assert abs(L - (0.5 + 2.5*0.1)) < 1e-9  # L₀ + α×d

# TEST 3: Calcolo potenza ricevuta
P_rx = mezzo.calcola_potenza_ricevuta(10, 0.1)  # P_tx=10dBm, d=100m
L = mezzo.calcola_perdita_segnale(0.1)
assert abs(P_rx - (10 - L)) < 1e-9

# TEST 4: Velocità segnale
v = mezzo.velocita_segnale_ms()
assert abs(v - 0.77 * 3e8) < 1e-6

# TEST 5: Tempo propagazione
t = mezzo.tempo_propagazione(0.3)  # 300 m
v = mezzo.velocita_segnale_ms()
assert abs(t - 0.3 / (v/1000)) < 1e-9

# TEST 6: Path Loss spazio libero
PL = calcola_path_loss_spazio_libero(2400, 0.1)
# Formula: 32.4 + 20×log₁₀(2400) + 20×log₁₀(0.1) ≈ 80 dB
assert abs(PL - 80) < 1  # Tolleranza 1 dB

# TEST 7: Comparazione mezzi
mezzi = crea_mezzi_standard()
assert isinstance(mezzi, dict)
assert len(mezzi) >= 5

# TEST 8: Simulazione trasmissione
mezzo_test = MezzoTrasmissivo('Test', 'cavo_rame', 0.77, 2.5, 100e6, 100, 0.1, 0.2)
sim = simula_trasmissione(mezzo_test, 10, 0.05, sensibilita_rx_dbm=-90)
assert 'potenza_rx_dbm' in sim
assert 'collegamento_ok' in sim
assert sim['collegamento_ok'] == True  # A 50m con 10dBm, dovrebbe ok

# TEST 9: Costo totale mezzo
costo = mezzo.costo_totale(100)  # 100 metri
assert abs(costo - 0.2 * 100) < 1e-9

# TEST 10: Margine segnale positivo/negativo
mezzo_cattivo = MezzoTrasmissivo('Cattivo', 'cavo_rame', 0.77, 100, 1e6, 100, 0.001, 0.2)
sim_cattivo = simula_trasmissione(mezzo_cattivo, 0, 0.1, sensibilita_rx_dbm=-90)
assert sim_cattivo['collegamento_ok'] == False  # Attenuazione troppa
```

---

## 🛠️ Step Implementazione (7-8 passaggi)

### STEP 1: Classe MezzoTrasmissivo Base ✅
- [ ] Creare file `soluzione.py`
- [ ] Definire classe `MezzoTrasmissivo` con `__init__` e attributi
- [ ] Implementare `__str__()` per output leggibile
- [ ] Testare creazione istanza

```python
class MezzoTrasmissivo:
    def __init__(self, nome, tipo, velocita_propagazione, ...):
        self.nome = nome
        # ... inizializzare tutti gli attributi
```

### STEP 2: Metodi Calcolo Base 📐
- [ ] Implementare `calcola_perdita_segnale()` - Formula: L = L₀ + α × d
- [ ] Implementare `calcola_potenza_ricevuta()` - P_rx = P_tx - L
- [ ] Implementare `velocita_segnale_ms()` - v = c × fattore
- [ ] Testare con doppino Cat 5e @ 100m

### STEP 3: Metodi Austeri 🔧
- [ ] Implementare `tempo_propagazione()` - t = d / v
- [ ] Implementare `costo_totale()` - costo = lunghezza × costo_unitario
- [ ] Testare con valori realistici

### STEP 4: Creazione Mezzi Predefiniti 📦
- [ ] Implementare `crea_mezzi_standard()`
- [ ] Creare almeno 8-9 mezzi:
  - Doppino Cat 5e, Cat 6, Cat 6A
  - Coassiale RG-6
  - Fibra monomodal
  - WiFi 2.4 GHz, 5 GHz
  - 4G LTE
  - 5G NR
- [ ] Testare creazione e accesso dizionario

### STEP 5: Path Loss Wireless 🛰️
- [ ] Implementare `calcola_path_loss_spazio_libero()`
- [ ] Formula: PL = 32.4 + 20×log₁₀(f[MHz]) + 20×log₁₀(d[km]) - Gt - Gr
- [ ] Testare con WiFi 2.4GHz @ 100m
- [ ] Testare con 5GHz @ 50m

### STEP 6: Simulazione Trasmissione 📡
- [ ] Implementare `simula_trasmissione()`
- [ ] Ritornare dizionario con: potenza_rx, attenuazione, margine, ok/no, tempo, costo
- [ ] Verificare margine > 0 per collegamento affidabile
- [ ] Testare casi di successo e fallimento

### STEP 7: Comparazione e Visualizzazione 📊
- [ ] Implementare `compara_mezzi()` - tabella ASCII
- [ ] Opzionale: `disegna_attenuazione()` - grafico matplotlib
- [ ] Testare comparazione con 3-4 mezzi

### STEP 8: Test Completo e Documentazione ✓
- [ ] Eseguire tutti i 10 test cases
- [ ] Verificare edge cases (distanza = 0, potenza molto bassa, ecc)
- [ ] Aggiungere docstring complete
- [ ] Creare file `esempi_pratici.py` con case reali

---

## 💡 Trucchi Python & TLC 🎯

### Trucchi Python 🐍
1. **Logaritmi in dB:**
   ```python
   import math
   db = 10 * math.log10(rapporto_potenza)
   # Se rapporto = 10: db = 10 dB
   # Se rapporto = 0.1: db = -10 dB
   ```

2. **Dizionario per mezzi:**
   ```python
   mezzi = {
       'Cat 5e': MezzoTrasmissivo(...),
       'Fibra': MezzoTrasmissivo(...),
       ...
   }
   for nome, mezzo in mezzi.items():
       print(f"{nome}: {mezzo}")
   ```

3. **Classe con metodi ritornano info:**
   ```python
   def get_parametri(self):
       return {
           'banda': self.banda_max_hz,
           'attenuazione': self.attenuazione_db_per_km
       }
   ```

4. **F-string con numeri formattati:**
   ```python
   print(f"Potenza: {P_rx:.1f} dBm")
   print(f"Distanza: {d*1000:.0f} m")
   ```

5. **Validazione con assert (nei test):**
   ```python
   assert mezzo.velocita_propagazione > 0
   assert mezzo.velocita_propagazione < 1
   ```

### Trucchi TLC 📡
1. **dB vs dBm:**
   ```
   dB = 10×log₁₀(P_out / P_in)  ← Rapporto relativo
   dBm = 10×log₁₀(P [mW])        ← Valore assoluto vs 1mW

   Es: 1 mW = 0 dBm, 10 mW = 10 dBm, 100 mW = 20 dBm
   ```

2. **Regola del 3 dB:**
   ```
   +3 dB = raddoppio potenza
   -3 dB = dimezzamento potenza

   Utile per stime rapide!
   ```

3. **Lunghezza d'onda e frequenza:**
   ```
   λ = c / f

   Es: 2.4 GHz WiFi → λ = 3×10⁸ / 2.4×10⁹ = 0.125 m = 12.5 cm
   ```

4. **Attenuazione cavi aumenta con frequenza:**
   ```
   α(f) ≈ α₀ × √f

   A 100 MHz: piccolo α
   A 1 GHz: α aumenta significativamente
   A 10 GHz: α molto grande (fibra necessaria)
   ```

5. **Velocità propagazione ≠ velocità della luce:**
   ```
   Vuoto: v = c = 3×10⁸ m/s
   Rame: v = 0.77c = 2.31×10⁸ m/s
   Fibra: v = 0.66c = 1.98×10⁸ m/s

   Importante per calcoli di ritardo (latenza)
   ```

---

## ⚠️ Errori Comuni 🐛

### Errori Fisici 📉

1. **Confondere dB e dBm**
   ```
   ❌ "La potenza è 20 dBm di attenuazione"
   ✅ "La potenza è 20 dBm, con attenuazione di 10 dB"
   ```

2. **Ignorare velocità propagazione < c**
   ```
   ❌ t = d / c  (sempre c!)
   ✅ t = d / (c × fattore_velocita)

   Esempio: Fibra 100 km
   ❌ t = 100000 / 3×10⁸ = 0.33 ms (SBAGLIATO!)
   ✅ t = 100000 / (3×10⁸ × 0.66) = 0.505 ms (GIUSTO!)
   ```

3. **Path Loss in cavi vs spazio libero**
   ```
   ❌ Usare path loss formula anche per cavi
   ✅ Usare L = α × d per cavi
   ✅ Usare path loss formula solo per wireless
   ```

4. **Attenuazione aumenta con frequenza**
   ```
   ❌ Assumere α costante per tutte le f
   ✅ Consultare tabelle di attenuazione @ frequenza specifica
   ```

5. **Impedenza caratteristica ignorata**
   ```
   ❌ Mescolate fili di impedenza diversa
   ✅ Sempre adattare impedenza (100Ω per Ethernet, 50Ω per RF)
   ```

### Errori di Codice 💻

1. **Logaritmo di zero**
   ```python
   ❌ db = 10 * math.log10(0)  # Errore!
   ✅ if rapporto > 0:
       db = 10 * math.log10(rapporto)
   ```

2. **Confondere fattore e dB**
   ```python
   ❌ P_rx = P_tx - 10  # dB o mW?
   ✅ P_rx_dbm = P_tx_dbm - L_db  # Sempre chiarire unità!
   ```

3. **Frequenza in MHz vs Hz**
   ```python
   ❌ PL = 32.4 + 20*log₁₀(2.4e9) + ...  # GHz in formula MHz!
   ✅ f_mhz = 2.4e9 / 1e6  # Convertire
       PL = 32.4 + 20*log₁₀(f_mhz) + ...
   ```

4. **Distanza in km vs m**
   ```python
   ❌ d_km = 100  # È in metri!
   ✅ d_km = 100 / 1000 = 0.1  # Conversione corretta
   ```

5. **Indice lista vs accesso dizionario**
   ```python
   ❌ mezzi[0]  # IndexError se lista vuota
   ✅ mezzi.get('Cat 5e')  # Ritorna None se non esiste
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Progetto Cablaggio Ottico ⭐
```python
def progetta_rete_fibra(distanza_totale_km, throughput_richiesto_gbps):
    """
    Progetta rete fibra ottica.

    Determinare:
    - Tipo fibra (monomodal vs multimodal)
    - Numero rigeneratori
    - Posizionamento rigeneratori
    - Costo totale
    - Tempo propagazione
    """
```

### Sfida 2: Simulatore WiFi Multipath ⭐
```python
def simula_wifi_multipath(frequenza_ghz, distanza_m, num_ostacoli):
    """
    Simula propagazione WiFi con ostacoli.

    Path Loss = Free Space + Shadowing Loss

    Effetti considerare:
    - Riflessioni (muri, pavimenti)
    - Diffrazione (angoli edifici)
    - Scattering (superfici irregolari)
    - Fading (interferenza costruttiva/distruttiva)
    """
```

### Sfida 3: Ottimizzatore Potenza TX ⭐⭐
```python
def ottimizza_potenza_tx(mezzo, distanza_km, sensibilita_rx_dbm,
                         guadagno_antenna_tx_db, guadagno_antenna_rx_db,
                         margine_desiderato_db=10):
    """
    Trova potenza TX minima per collegamento affidabile.

    P_tx_min tale che:
    P_rx = P_tx - L + Gt + Gr >= sensibilita + margine

    Minimizzare P_tx (consumo energetico)
    """
```

### Sfida 4: Comparazione Costo-Prestazione ⭐⭐
```python
def analizza_rapporto_costo_prestazione(lista_mezzi, distanza_km):
    """
    Calcola rapporto costo vs capacità per ogni mezzo.

    Metrica: Costo [€] / Capacità [Gbps]

    Ritorna ranking e consigliazione scelta ottima.
    """
```

### Sfida 5: Simulatore Rete Complessa ⭐⭐⭐
```python
def simula_backbone_telecom(config_rotta):
    """
    Simula intera rotta di trasmissione.

    Config:
    [
        {'mezzo': fibra, 'distanza_km': 100, 'potenza_tx': 10},
        {'tipo': 'amplificatore', 'guadagno_db': 20},
        {'mezzo': fibra, 'distanza_km': 100, 'potenza_tx': 10},
        ...
    ]

    Simulare propagazione progressiva del segnale
    attraverso tutta la rotta con rigeneratori.
    """
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione Python
- [math.log10()](https://docs.python.org/3/library/math.html)
- [Dizionari Python](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### TLC - Mezzi Trasmissivi
- [Wikipedia: Ethernet](https://en.wikipedia.org/wiki/Ethernet)
- [Wikipedia: Fiber Optics](https://en.wikipedia.org/wiki/Fiber-optic_communication)
- [Wikipedia: Wireless Power Transfer](https://en.wikipedia.org/wiki/Wireless_transmission)

### Standard Ufficiali
- IEEE 802.3: Ethernet (cablaggio)
- IEC 60794: Fibra ottica
- ITU-R: Radiocomunicazioni (wireless)

### Calcolatori Online
- [RF Path Loss Calculator](https://www.everythingrf.com/tools/path-loss)
- [Ethernet Distance Calculator](https://www.blackmagicdesign.com/support/download/cd7866bc-0b1e-11e7-93f1-0cc47a6172f5)

### Letture Consigliate
1. Agrawal, "Fiber-Optic Communication Systems" (Cap. 2)
2. Goldsmith, "Wireless Communications" (Cap. 2-3)
3. Proakis & Salehi, "Digital Communications" (Cap. 2)

---

## 🎯 Preparazione Esercizi Successivi 🔮

### Esercizi Successivi
Questo corso di TLC forma la base per:
- **Modulazione e Trasmissione:** AM, FM, FSK, QAM
- **Reti di Accesso:** DSL, GPON, 5G
- **Sicurezza:** Crittografia, certificati
- **Qualità del Servizio (QoS):** Latenza, jitter, perdita pacchetti
- **Routing e Switching:** Inoltro pacchetti a livello fisica
- **Antenna e Propagazione:** Teoria antenna, modelli di propagazione

---

## ✅ Checklist Completamento

```
PRE-IMPLEMENTAZIONE:
[ ] Leggi tutta la consegna
[ ] Comprendi formula path loss e attenuazione
[ ] Conosci i mezzi trasmissivi principali
[ ] Capisci dB e dBm

IMPLEMENTAZIONE:
[ ] Step 1: Classe MezzoTrasmissivo
[ ] Step 2: Metodi calcolo perdita
[ ] Step 3: Metodi ausiliari
[ ] Step 4: Mezzi predefiniti
[ ] Step 5: Path loss spazio libero
[ ] Step 6: Simulazione trasmissione
[ ] Step 7: Comparazione e visualizzazione
[ ] Step 8: Test e documentazione

VALIDAZIONE:
[ ] Tutti i 10 test passano
[ ] Classe funziona correttamente
[ ] Formule applicate giustamente
[ ] Unità coerenti (dB, dBm, km, m)

BONUS:
[ ] Almeno 1 sfida bonus
[ ] Esempi pratici (LAN, WiFi, 5G, fibra)
[ ] Grafico attenuazione vs distanza
```

---

## 🎓 Conclusione

Hai imparato come i **segnali viaggiano attraverso mezzi reali**, subendo attenuazione. Ogni rete TLC (dalle prese Ethernet alle antenne 5G) è progettata considerando:
- Attenuazione del mezzo
- Distanza massima affidabile
- Potenza disponibile
- Sensibilità ricevitore

Questi concetti saranno cruciali in tutti i progetti di telecomunicazioni!

**Hai completato i 5 esercizi fondamentali di TLC!** 🎉

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS