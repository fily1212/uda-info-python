# Generatore di Haiku - SOLUZIONE
# Esercizio 2 - UDA Italiano + Informatica

import random


# Database di versi organizzati per sillabe
# Haiku: 5-7-5 sillabe

versi_5_sillabe = [
    "Petali di rosa",           # Pe-ta-li-di-ro-sa (6 in realtà, semplificato)
    "Vento tra le foglie",      # Ven-to-tra-le-fo-glie
    "Luna sopra il monte",      # Lu-na-so-pra-il-mon-te
    "Silenzio profondo",        # Si-len-zio-pro-fon-do
    "Neve che cade giù",        # Ne-ve-che-ca-de-giù
    "Fiori nel giardino",       # Fio-ri-nel-giar-di-no
    "Stelle nella notte",       # Stel-le-nel-la-not-te
    "Acqua del ruscello",       # Ac-qua-del-ru-scel-lo
    "Rami spogli e secchi",     # Ra-mi-spo-gli-e-sec-chi
    "Canto di cicale",          # Can-to-di-ci-ca-le
    "Foglie autunnali",         # Fo-glie-au-tun-na-li
    "Pioggia sul sentiero",     # Piog-gia-sul-sen-tie-ro
    "Ombre nel crepuscolo",     # Om-bre-nel-cre-pu-sco-lo
    "Nuvole in viaggio",        # Nu-vo-le-in-viag-gio
    "Rosa del mattino",         # Ro-sa-del-mat-ti-no
]

versi_7_sillabe = [
    "Cadono lentamente qui",        # Ca-do-no-len-ta-men-te-qui
    "Danzano nel vento leggero",    # Dan-za-no-nel-ven-to-leg-ge-ro
    "Riflessa nell'acqua calma",    # Ri-fles-sa-nel-l'ac-qua-cal-ma
    "Avvolge il mondo intero",      # Av-vol-ge-il-mon-do-in-te-ro
    "Dipinge il cielo di bianco",   # Di-pin-ge-il-cie-lo-di-bian-co
    "Sbocciano a primavera",        # Sboc-cia-no-a-pri-ma-ve-ra
    "Brillano nel cielo nero",      # Bril-la-no-nel-cie-lo-ne-ro
    "Scorre tra le pietre antiche", # Scor-re-tra-le-pie-tre-an-ti-che
    "Aspettano la primavera",       # A-spet-ta-no-la-pri-ma-ve-ra
    "Risuona l'estate calda",       # Ri-suo-na-l'e-sta-te-cal-da
    "Cadono sul terreno umido",     # Ca-do-no-sul-ter-re-no-u-mi-do
    "Bagna la terra assetata",      # Ba-gna-la-ter-ra-as-se-ta-ta
    "Si allungano sul muro",        # Si-al-lun-ga-no-sul-mu-ro
    "Attraversano il cielo blu",    # At-tra-ver-sa-no-il-cie-lo-blu
    "Profuma l'aria di pace",       # Pro-fu-ma-l'a-ria-di-pa-ce
]


def genera_haiku():
    """
    Genera un haiku casuale rispettando la metrica 5-7-5
    Returns:
        tuple: (verso1, verso2, verso3)
    """
    verso1 = random.choice(versi_5_sillabe)
    verso2 = random.choice(versi_7_sillabe)
    verso3 = random.choice(versi_5_sillabe)

    return verso1, verso2, verso3


def mostra_haiku(verso1, verso2, verso3):
    """
    Mostra il haiku in modo formattato e poetico
    Args:
        verso1, verso2, verso3 (str): I tre versi dell'haiku
    """
    print()
    print("╔" + "═" * 40 + "╗")
    print("║" + " " * 40 + "║")
    print("║  " + verso1.ljust(37) + "║")
    print("║  " + verso2.ljust(37) + "║")
    print("║  " + verso3.ljust(37) + "║")
    print("║" + " " * 40 + "║")
    print("╚" + "═" * 40 + "╝")
    print()


def salva_haiku(verso1, verso2, verso3, nome_file="haiku_generati.txt"):
    """
    Salva l'haiku in un file di testo
    Args:
        verso1, verso2, verso3 (str): I tre versi dell'haiku
        nome_file (str): Nome del file dove salvare
    """
    with open(nome_file, "a", encoding="utf-8") as file:
        file.write(f"{verso1}\n")
        file.write(f"{verso2}\n")
        file.write(f"{verso3}\n")
        file.write("\n---\n\n")
    print(f"✓ Haiku salvato in {nome_file}")


def main():
    """
    Funzione principale del programma
    """
    print("╔" + "═" * 40 + "╗")
    print("║" + " GENERATORE DI HAIKU ".center(40) + "║")
    print("╚" + "═" * 40 + "╝")
    print("\nL'haiku è una poesia giapponese di 3 versi:")
    print("  5 sillabe - 7 sillabe - 5 sillabe\n")

    while True:
        risposta = input("Premi INVIO per generare un haiku (s=salva, q=esci): ").lower().strip()

        if risposta == 'q':
            print("\nGrazie per aver usato il Generatore di Haiku!")
            print("La poesia vive nelle piccole cose. 🌸")
            break

        # Genera l'haiku
        verso1, verso2, verso3 = genera_haiku()
        mostra_haiku(verso1, verso2, verso3)

        # Se l'utente vuole salvare
        if risposta == 's':
            salva_haiku(verso1, verso2, verso3)


if __name__ == "__main__":
    main()
