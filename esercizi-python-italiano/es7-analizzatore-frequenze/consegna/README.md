# Esercizio 7: Analizzatore di Frequenze con Grafici

## Livello: FACILE-INTERMEDIO

## Obiettivi didattici
- **Informatica**: Dizionari, matplotlib, visualizzazione dati, file I/O
- **Italiano**: Analisi statistica del testo, frequenza lessicale, stopwords

## Descrizione
Crea un programma che analizza la frequenza delle parole in un testo letterario e genera grafici statistici.

## Requisiti

1. Caricare un testo da file o input utente
2. Calcolare:
   - Frequenza di ogni parola
   - Frequenza di ogni lettera
   - Le 10 parole più comuni
   - Le 10 parole più rare
3. Generare grafici:
   - Grafico a barre delle parole più frequenti
   - Grafico a torta distribuzione lunghezza parole
   - Word cloud del testo
4. Filtrare stopwords italiane (articoli, preposizioni, ecc.)
5. Salvare statistiche in file CSV

## Installazione dipendenze

```bash
pip install matplotlib wordcloud
```

## Esempio di Output

```
=== ANALIZZATORE DI FREQUENZE ===

Caricamento testo da: divina_commedia_canto1.txt
✅ Testo caricato: 457 parole

--- ANALISI COMPLETATA ---

Parole totali: 457
Parole uniche: 243
Rapporto varietà lessicale: 53.2%

Top 10 parole più frequenti:
  1. che (18 occorrenze)
  2. per (12 occorrenze)
  3. mi (10 occorrenze)
  ...

📊 Generazione grafici...
  ✅ Grafico a barre salvato: grafici/frequenze_parole.png
  ✅ Word cloud salvato: grafici/wordcloud.png
  ✅ Distribuzione lunghezze: grafici/lunghezze.png

💾 Statistiche salvate in: statistiche.csv
```

## Estensioni opzionali
- Confronto tra più testi (es: Dante vs Manzoni)
- Analisi sentiment (positivo/negativo)
- Identificazione di figure retoriche comuni
- Analisi temporale (se il testo ha capitoli)

## Consegna
Salva come `analizza_frequenze.py` e testa con almeno 2 testi letterari diversi.
