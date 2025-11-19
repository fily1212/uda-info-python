# Es1: Modulazione di Segnali

## Obiettivi
- **TLC**: Modulazione AM, FM, PM
- **Informatica**: NumPy, Matplotlib, generazione segnali

## Descrizione
Simulazione e visualizzazione di tecniche di modulazione analogica.

## Funzionalità
1. Generazione portante e segnale modulante
2. Modulazione AM (Amplitude Modulation)
3. Modulazione FM (Frequency Modulation)
4. Modulazione PM (Phase Modulation)
5. Grafici nel tempo e frequenza (FFT)

## Installazione
```bash
pip install numpy matplotlib scipy
```

## Formule
- **AM**: s(t) = [1 + m·cos(2πfₘt)]·cos(2πfₚt)
- **FM**: s(t) = cos(2πfₚt + β·sin(2πfₘt))
- **PM**: s(t) = cos(2πfₚt + φₘ·cos(2πfₘt))

## Consegna
Generare e visualizzare i 3 tipi di modulazione con parametri configurabili.
