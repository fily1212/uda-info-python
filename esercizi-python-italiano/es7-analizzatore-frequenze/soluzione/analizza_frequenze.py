# Analizzatore di Frequenze - SOLUZIONE
# Esercizio 7 - UDA Italiano + Informatica

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import string
import os

# Stopwords italiane comuni
STOPWORDS_IT = set([
    'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una', 'di', 'a', 'da', 'in',
    'con', 'su', 'per', 'tra', 'fra', 'e', 'ed', 'o', 'che', 'chi', 'cui', 'mi',
    'ti', 'si', 'ci', 'vi', 'ne', 'del', 'dello', 'della', 'dei', 'degli', 'delle',
    'al', 'allo', 'alla', 'ai', 'agli', 'alle', 'dal', 'dallo', 'dalla', 'dai',
    'dagli', 'dalle', 'nel', 'nello', 'nella', 'nei', 'negli', 'nelle', 'sul',
    'sullo', 'sulla', 'sui', 'sugli', 'sulle', 'è', 'sono', 'sei', 'siamo', 'siete',
    'ho', 'hai', 'ha', 'abbiamo', 'avete', 'hanno', 'non', 'più', 'anche', 'come',
    'mai', 'molto', 'poco', 'tutto', 'tutti', 'ogni', 'altro', 'stesso'
])


def carica_testo(percorso_file=None):
    """Carica testo da file o input"""
    if percorso_file and os.path.exists(percorso_file):
        with open(percorso_file, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return input("Inserisci il testo da analizzare:\n")


def pulisci_testo(testo):
    """Pulisce e normalizza il testo"""
    testo = testo.lower()
    # Rimuovi punteggiatura
    translator = str.maketrans('', '', string.punctuation)
    testo = testo.translate(translator)
    return testo


def analizza_parole(testo, rimuovi_stopwords=True):
    """Analizza frequenze parole"""
    parole = testo.split()

    if rimuovi_stopwords:
        parole = [p for p in parole if p not in STOPWORDS_IT and len(p) > 2]

    return Counter(parole)


def analizza_lettere(testo):
    """Analizza frequenze lettere"""
    lettere = [c for c in testo if c.isalpha()]
    return Counter(lettere)


def analizza_lunghezze(testo):
    """Analizza distribuzione lunghezza parole"""
    parole = testo.split()
    lunghezze = [len(p) for p in parole]
    return Counter(lunghezze)


def crea_grafico_barre(dati, titolo, nome_file):
    """Crea grafico a barre delle frequenze"""
    parole, frequenze = zip(*dati.most_common(15))

    plt.figure(figsize=(12, 6))
    plt.bar(parole, frequenze, color='steelblue')
    plt.xlabel('Parole')
    plt.ylabel('Frequenza')
    plt.title(titolo)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(nome_file, dpi=300)
    plt.close()
    print(f"  ✅ {nome_file}")


def crea_wordcloud(testo, nome_file):
    """Crea word cloud"""
    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        stopwords=STOPWORDS_IT,
        max_words=100,
        colormap='viridis'
    ).generate(testo)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud', fontsize=16)
    plt.tight_layout()
    plt.savefig(nome_file, dpi=300)
    plt.close()
    print(f"  ✅ {nome_file}")


def crea_grafico_torta(dati, nome_file):
    """Crea grafico a torta lunghezze"""
    # Raggruppa lunghezze
    gruppi = {'1-3 lettere': 0, '4-6 lettere': 0, '7-9 lettere': 0, '10+ lettere': 0}

    for lunghezza, freq in dati.items():
        if lunghezza <= 3:
            gruppi['1-3 lettere'] += freq
        elif lunghezza <= 6:
            gruppi['4-6 lettere'] += freq
        elif lunghezza <= 9:
            gruppi['7-9 lettere'] += freq
        else:
            gruppi['10+ lettere'] += freq

    plt.figure(figsize=(8, 8))
    plt.pie(gruppi.values(), labels=gruppi.keys(), autopct='%1.1f%%',
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.title('Distribuzione Lunghezza Parole')
    plt.savefig(nome_file, dpi=300)
    plt.close()
    print(f"  ✅ {nome_file}")


def salva_statistiche(freq_parole, nome_file='statistiche.csv'):
    """Salva statistiche in CSV"""
    with open(nome_file, 'w', encoding='utf-8') as f:
        f.write('Parola,Frequenza\n')
        for parola, freq in freq_parole.most_common():
            f.write(f'{parola},{freq}\n')
    print(f"💾 Statistiche salvate: {nome_file}")


def main():
    print("=== ANALIZZATORE DI FREQUENZE ===\n")

    # Input
    percorso = input("Percorso file testo (INVIO per input manuale): ").strip()
    testo_originale = carica_testo(percorso if percorso else None)
    testo_pulito = pulisci_testo(testo_originale)

    # Analisi
    freq_parole = analizza_parole(testo_pulito, rimuovi_stopwords=True)
    freq_lettere = analizza_lettere(testo_pulito)
    freq_lunghezze = analizza_lunghezze(testo_pulito)

    # Statistiche
    parole_totali = sum(freq_parole.values())
    parole_uniche = len(freq_parole)
    varieta = (parole_uniche / parole_totali * 100) if parole_totali > 0 else 0

    print(f"\n--- ANALISI COMPLETATA ---\n")
    print(f"Parole totali: {parole_totali}")
    print(f"Parole uniche: {parole_uniche}")
    print(f"Varietà lessicale: {varieta:.1f}%\n")

    print("Top 10 parole più frequenti:")
    for i, (parola, freq) in enumerate(freq_parole.most_common(10), 1):
        print(f"  {i}. {parola} ({freq} occorrenze)")

    # Crea cartella grafici
    os.makedirs('grafici', exist_ok=True)

    # Genera grafici
    print("\n📊 Generazione grafici...")
    crea_grafico_barre(freq_parole, 'Parole più Frequenti', 'grafici/frequenze_parole.png')
    crea_wordcloud(testo_pulito, 'grafici/wordcloud.png')
    crea_grafico_torta(freq_lunghezze, 'grafici/lunghezze.png')

    # Salva CSV
    print()
    salva_statistiche(freq_parole)


if __name__ == "__main__":
    main()
