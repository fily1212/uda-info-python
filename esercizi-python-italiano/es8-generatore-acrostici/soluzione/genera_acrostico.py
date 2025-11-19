# Generatore Acrostici - SOLUZIONE
import random

VERSI_DB = {
    'A': ["Anime che si incontrano", "Alberi che danzano", "Attimi preziosi", "Aquile che volano"],
    'B': ["Baci rubati", "Boschi incantati", "Brillano stelle", "Brezze leggere"],
    'C': ["Cuori che battono", "Cieli infiniti", "Canzoni d'amore", "Colori vivaci"],
    'D': ["Destini intrecciati", "Dolci ricordi", "Danze notturne", "Desideri nascosti"],
    'E': ["Eternità in un istante", "Emozioni profonde", "Echi lontani", "Esistenze parallele"],
    'F': ["Fiori che sbocciano", "Fiamme che ardono", "Favole antiche", "Fuochi fatui"],
    'G': ["Gioie infinite", "Giardini segreti", "Gemme preziose", "Grida silenziose"],
    'H': ["Hanno sogni comuni", "Harmoniae celesti"],
    'I': ["Infiniti mondi", "Istanti magici", "Illusioni dolci", "Incontri fatali"],
    'L': ["Luci nella notte", "Lacrime e sorrisi", "Lune crescenti", "Legami eterni"],
    'M': ["Mondi che si fondono", "Mani che si cercano", "Melodie celesti", "Misteri profondi"],
    'N': ["Notti stellate", "Nebbie mattutine", "Nuvole passeggere", "Nomi scolpiti"],
    'O': ["Occhi che parlano", "Orizzonti lontani", "Onde del mare", "Ombre danzanti"],
    'P': ["Parole non dette", "Promesse eterne", "Petali di rosa", "Pensieri vaganti"],
    'Q': ["Quando tutto tace", "Quiete profonda"],
    'R': ["Respiri sincronizzati", "Raggi di sole", "Ricordi indelebili", "Riflessi d'acqua"],
    'S': ["Sguardi complici", "Sogni condivisi", "Strade parallele", "Silenzi eloquenti"],
    'T': ["Tempo che scorre", "Tramonti infuocati", "Tenerezze infinite", "Tracce nel vento"],
    'U': ["Universi paralleli", "Unioni perfette", "Uccelli in volo"],
    'V': ["Vite intrecciate", "Venti che soffiano", "Verità nascoste", "Voci lontane"],
    'Z': ["Zefiri primaverili", "Zone d'ombra"],
}

def genera_acrostico(parola):
    linee = []
    for lettera in parola.upper():
        if lettera in VERSI_DB:
            linee.append(random.choice(VERSI_DB[lettera]))
        else:
            linee.append(f"{lettera}...")
    return '\n'.join(linee)

def main():
    print("=== GENERATORE DI ACROSTICI ===\n")
    while True:
        parola = input("Parola chiave (o 'q' per uscire): ").strip()
        if parola.lower() == 'q':
            break
        print(f"\n✨ Acrostico per '{parola.upper()}':\n")
        print(genera_acrostico(parola))
        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
