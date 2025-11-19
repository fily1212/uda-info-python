# 🎒 SISTEMA INVENTARIO con CRAFTING/COMBINAZIONI
# Combina oggetti per crearne di nuovi!

class OggettoCraftable:
    def __init__(self, nome, descrizione, peso=1):
        self.nome = nome
        self.descrizione = descrizione
        self.peso = peso


class SistemaCrafting:
    """Sistema per combinare oggetti"""

    # Ricette: {(oggetto1, oggetto2): risultato}
    RICETTE = {
        ('bastone', 'pietra'): {
            'risultato': 'piccone',
            'descrizione': 'Hai legato la pietra al bastone creando un piccone!'
        },
        ('corda', 'legno'): {
            'risultato': 'arco',
            'descrizione': 'Hai costruito un arco rudimentale!'
        },
        ('erba', 'acqua'): {
            'risultato': 'pozione',
            'descrizione': 'Hai preparato una pozione curativa!'
        },
        ('chiave spezzata', 'nastro'): {
            'risultato': 'chiave riparata',
            'descrizione': 'Hai riparato la chiave con il nastro!'
        },
    }

    @classmethod
    def combina(cls, oggetto1, oggetto2):
        """Prova a combinare due oggetti"""
        # Prova entrambi gli ordini
        ricetta1 = (oggetto1.lower(), oggetto2.lower())
        ricetta2 = (oggetto2.lower(), oggetto1.lower())

        if ricetta1 in cls.RICETTE:
            return cls.RICETTE[ricetta1]
        elif ricetta2 in cls.RICETTE:
            return cls.RICETTE[ricetta2]

        return None


class Inventario:
    def __init__(self, capacita_max=20):
        self.oggetti = []
        self.capacita_max = capacita_max
        self.peso_corrente = 0

    def aggiungi(self, oggetto):
        """Aggiungi oggetto all'inventario"""
        if self.peso_corrente + oggetto.peso > self.capacita_max:
            return f"❌ Inventario pieno! (Peso: {self.peso_corrente}/{self.capacita_max})"

        self.oggetti.append(oggetto)
        self.peso_corrente += oggetto.peso
        return f"✅ Aggiunto: {oggetto.nome}"

    def rimuovi(self, nome_oggetto):
        """Rimuovi oggetto dall'inventario"""
        for oggetto in self.oggetti:
            if oggetto.nome.lower() == nome_oggetto.lower():
                self.oggetti.remove(oggetto)
                self.peso_corrente -= oggetto.peso
                return oggetto

        return None

    def cerca(self, nome):
        """Cerca oggetto per nome"""
        for oggetto in self.oggetti:
            if nome.lower() in oggetto.nome.lower():
                return oggetto
        return None

    def mostra(self):
        """Mostra contenuto inventario"""
        if not self.oggetti:
            return "🎒 Inventario vuoto"

        testo = f"🎒 INVENTARIO ({self.peso_corrente}/{self.capacita_max} kg):\n"
        for i, oggetto in enumerate(self.oggetti, 1):
            testo += f"  {i}. {oggetto.nome} ({oggetto.peso}kg) - {oggetto.descrizione}\n"

        return testo

    def combina_oggetti(self, nome1, nome2):
        """Combina due oggetti"""
        ogg1 = self.cerca(nome1)
        ogg2 = self.cerca(nome2)

        if not ogg1:
            return f"❌ Non hai '{nome1}'"
        if not ogg2:
            return f"❌ Non hai '{nome2}'"

        # Prova combinazione
        ricetta = SistemaCrafting.combina(ogg1.nome, ogg2.nome)

        if ricetta:
            # Rimuovi oggetti originali
            self.rimuovi(ogg1.nome)
            self.rimuovi(ogg2.nome)

            # Aggiungi nuovo oggetto
            nuovo = OggettoCraftable(
                ricetta['risultato'],
                f"Creato combinando {ogg1.nome} e {ogg2.nome}",
                peso=(ogg1.peso + ogg2.peso) // 2
            )
            self.aggiungi(nuovo)

            return f"✨ {ricetta['descrizione']}\n   Ottenuto: {nuovo.nome}!"
        else:
            return f"❌ Non puoi combinare {ogg1.nome} e {ogg2.nome}."


# DEMO
if __name__ == "__main__":
    print("🎒 DEMO SISTEMA INVENTARIO + CRAFTING\n")

    inv = Inventario(capacita_max=20)

    # Aggiungi oggetti
    inv.aggiungi(OggettoCraftable("bastone", "Un bastone di legno robusto", peso=2))
    inv.aggiungi(OggettoCraftable("pietra", "Una pietra affilata", peso=3))
    inv.aggiungi(OggettoCraftable("corda", "Una corda resistente", peso=1))

    print(inv.mostra())

    print("\n💡 Prova a combinare bastone + pietra:")
    print(inv.combina_oggetti("bastone", "pietra"))

    print("\n" + inv.mostra())
