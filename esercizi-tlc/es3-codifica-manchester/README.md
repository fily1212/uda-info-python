# Es3: Codifica Manchester e NRZ

**Livello:** INTERMEDIO
**Durata stimata:** 5-6 ore

## Descrizione

Simulatore di codifiche di linea (NRZ, Manchester, 4B/5B) con visualizzazione delle forme d'onda, clock recovery e eye diagram. Permette di comprendere come i dati digitali vengono codificati per la trasmissione su canali fisici.

## Obiettivi

### Competenze TLC
- Comprendere le codifiche di linea (NRZ, RZ, Manchester, Differential Manchester)
- Implementare algoritmi di clock recovery
- Analizzare l'eye diagram per valutare la qualità del segnale
- Comprendere l'importanza dell'assenza di lunghe sequenze uguali
- Applicare codifiche ridondanti (4B/5B)

### Competenze Informatica
- Generazione e manipolazione di sequenze binarie
- Visualizzazione di segnali con matplotlib
- Elaborazione di segnali digitali
- Algoritmi di sincronizzazione
- Utilizzo di NumPy per operazioni vettoriali

## Consegna

Il programma deve:

1. **Implementare codifiche di linea:**
   - **NRZ (Non-Return-to-Zero):** 0 = basso, 1 = alto
   - **Manchester:** 0 = transizione alta→bassa, 1 = bassa→alta
   - **Differential Manchester:** Cambia transizione per 0, no cambia per 1
   - **4B/5B:** Codifica 4 bit in 5 bit per evitare lunghe sequenze uguali

2. **Visualizzare le forme d'onda:**
   - Grafico della sequenza binaria codificata
   - Sovrapposizione di più codifiche a confronto
   - Marcatura delle transizioni di clock

3. **Implementare clock recovery:**
   - Estrazione del clock dal segnale Manchester
   - Campionamento ai momenti giusti
   - Decodifica della sequenza originale

4. **Generare eye diagram:**
   - Sovrapposizione di multiple transizioni
   - Valutazione della qualità del segnale
   - Margini di timing e ampiezza

## Esempio di Utilizzo

```
=== CODIFICATORE MANCHESTER ===

Inserisci sequenza binaria (es: 10110101): 101010

Codifiche implementate:
1. NRZ (Non-Return-to-Zero)
2. Manchester
3. Differential Manchester
4. Eye Diagram
5. Mostra Tutto

Scelta: 2

Sequenza originale:    1 0 1 0 1 0
Manchester codificato:
┌─┐   ┌─┐   ┌─┐
│ └─┬─┘ └─┬─┘ └─┬
└───┴─────┴─────┘

Cambiamento di livello per ogni bit
0 = alto→basso  |  1 = basso→alto

Vantaggi Manchester:
✓ Auto-sincronizzazione
✓ Rilevamento errori (assenza transizione)
✓ Bilanciamento energetico
✗ Richiede 2x la banda di NRZ
```

## Suggerimenti

- Rappresenta i segnali come array NumPy (livelli di tensione nel tempo)
- Per Manchester: dividi ogni bit in 2 intervalli e fai una transizione
- NRZ è semplice: usa livelli costanti
- Eye diagram: sovrappondi lunghi tratti del segnale codificato
- Usa matplotlib subplots per confrontare diverse codifiche
- Aggiungi rumore gaussiano al segnale per simulare condizioni reali
- Implementa un semplice ricercatore di transizioni per clock recovery

## Esempio di Codice Struttura

```python
import numpy as np
import matplotlib.pyplot as plt

class CodificatoreLinea:
    def __init__(self, sequenza_bit, campioni_per_bit=100):
        self.sequenza_bit = [int(b) for b in str(sequenza_bit)]
        self.campioni_per_bit = campioni_per_bit

    def nrz(self):
        """Non-Return-to-Zero: 0=basso(-1), 1=alto(+1)"""
        segnale = []
        for bit in self.sequenza_bit:
            livello = 1 if bit == 1 else -1
            segnale.extend([livello] * self.campioni_per_bit)
        return np.array(segnale)

    def manchester(self):
        """Manchester: 0=alto→basso, 1=basso→alto"""
        segnale = []
        for bit in self.sequenza_bit:
            meta = self.campioni_per_bit // 2
            if bit == 0:
                # Alto poi basso
                segnale.extend([1] * meta + [-1] * meta)
            else:
                # Basso poi alto
                segnale.extend([-1] * meta + [1] * meta)
        return np.array(segnale)

    def visualizza_manchester(self):
        """Visualizza il segnale Manchester"""
        segnale = self.manchester()
        tempo = np.arange(len(segnale)) / self.campioni_per_bit

        plt.figure(figsize=(12, 6))
        plt.plot(tempo, segnale, linewidth=2)
        plt.xlabel('Tempo (periodi bit)')
        plt.ylabel('Tensione (V)')
        plt.title('Codifica Manchester')
        plt.grid(True)
        plt.show()

# Utilizzo
codificatore = CodificatoreLinea("10110101")
segnale_manchester = codificatore.manchester()
codificatore.visualizza_manchester()
```

## Concetti Chiave

- **NRZ:** Semplice, efficiente in banda, ma no self-clock
- **Manchester:** Self-synchronizing, richiede 2x banda
- **4B/5B:** Aggiunge ridondanza, limita sequenze lunghe
- **Eye Diagram:** Indica qualità e margini del segnale
- **Clock Recovery:** Essenziale per sincronizzazione ricevitore

## Soluzione

La soluzione completa è disponibile nella cartella [`soluzione/`](./soluzione/).

⚠️ **Importante:** Consulta la soluzione solo dopo aver provato a completare l'esercizio autonomamente!

---

**Buon lavoro! 💾📊**
