# ⚔️ SISTEMA DI COMBATTIMENTO RPG - SOLUZIONE
# Combattimento a turni come nei classici JRPG!

import random
import time
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Abilita:
    """Abilità speciale che un combattente può usare"""
    nome: str
    costo_mp: int
    moltiplicatore_danno: float
    descrizione: str
    tipo: str  # 'attacco', 'cura', 'buff'
    valore_extra: int = 0  # Per cure o buff

class Combattente:
    """Classe base per giocatore e nemici"""
    def __init__(self, nome, hp, mp, atk, defe, spd, livello=1):
        self.nome = nome
        self.hp_max = hp
        self.hp = hp
        self.mp_max = mp
        self.mp = mp
        self.atk = atk
        self.defe = defe
        self.spd = spd
        self.livello = livello
        self.exp = 0
        self.abilita: List[Abilita] = []
        self.vivo = True

    def attacca(self, bersaglio):
        """Attacco base"""
        # Formula danno con variazione casuale
        danno_base = max(1, self.atk - bersaglio.defe // 2)
        moltiplicatore = random.uniform(0.85, 1.15)
        danno = int(danno_base * moltiplicatore)

        # Colpo critico (5% probabilità)
        critico = random.random() < 0.05
        if critico:
            danno *= 2
            print(f"   💥 COLPO CRITICO!")

        bersaglio.ricevi_danno(danno)
        return danno

    def usa_abilita(self, abilita: Abilita, bersaglio):
        """Usa un'abilità speciale"""
        if self.mp < abilita.costo_mp:
            print(f"❌ MP insufficienti per {abilita.nome}!")
            return False

        self.mp -= abilita.costo_mp

        if abilita.tipo == 'attacco':
            danno_base = max(1, int(self.atk * abilita.moltiplicatore_danno) - bersaglio.defe // 2)
            moltiplicatore = random.uniform(0.9, 1.1)
            danno = int(danno_base * moltiplicatore)
            bersaglio.ricevi_danno(danno)
            print(f"   {abilita.descrizione}")
            print(f"   💥 Danno: {danno} HP")
            return danno

        elif abilita.tipo == 'cura':
            cura = abilita.valore_extra
            self.hp = min(self.hp_max, self.hp + cura)
            print(f"   {abilita.descrizione}")
            print(f"   💚 Recuperati: {cura} HP")
            return cura

        return True

    def ricevi_danno(self, danno):
        """Ricevi danno e controlla se è ancora vivo"""
        self.hp -= danno
        if self.hp <= 0:
            self.hp = 0
            self.vivo = False

    def e_vivo(self):
        return self.vivo and self.hp > 0

    def exp_per_level_up(self):
        """EXP necessaria per salire di livello"""
        return self.livello * 100

    def guadagna_exp(self, exp):
        """Guadagna esperienza e controlla level up"""
        self.exp += exp
        level_ups = 0

        while self.exp >= self.exp_per_level_up():
            self.exp -= self.exp_per_level_up()
            self.level_up()
            level_ups += 1

        return level_ups

    def level_up(self):
        """Aumenta di livello e migliora statistiche"""
        self.livello += 1
        self.hp_max += 20
        self.mp_max += 10
        self.atk += 5
        self.defe += 3
        self.spd += 2
        self.hp = self.hp_max  # Recupero completo al level up!
        self.mp = self.mp_max

        print(f"\n{'='*60}")
        print(f"🌟 LEVEL UP! {self.nome} è ora livello {self.livello}! 🌟")
        print(f"{'='*60}")
        print(f"HP: {self.hp_max - 20} → {self.hp_max}")
        print(f"MP: {self.mp_max - 10} → {self.mp_max}")
        print(f"ATK: {self.atk - 5} → {self.atk}")
        print(f"DEF: {self.defe - 3} → {self.defe}")
        print(f"SPD: {self.spd - 2} → {self.spd}")
        print(f"HP e MP completamente ripristinati!")
        time.sleep(2)

    def mostra_barra_hp(self):
        """Barra HP visuale"""
        percentuale = self.hp / self.hp_max
        barre = int(percentuale * 12)
        return '█' * barre + '░' * (12 - barre)

    def mostra_barra_mp(self):
        """Barra MP visuale"""
        percentuale = self.mp / self.mp_max
        barre = int(percentuale * 12)
        return '█' * barre + '░' * (12 - barre)


class Giocatore(Combattente):
    """Classe specializzata per il giocatore"""
    def __init__(self, nome):
        super().__init__(nome, hp=100, mp=50, atk=20, defe=15, spd=18, livello=1)

        # Abilità del giocatore
        self.abilita = [
            Abilita("Attacco Forte", 10, 1.5, "⚔️  Colpisci con tutta la tua forza!", "attacco"),
            Abilita("Palla di Fuoco", 15, 2.0, "🔥 Una sfera infuocata esplode sul nemico!", "attacco"),
            Abilita("Fulmine", 20, 2.5, "⚡ Un fulmine squarcia il cielo!", "attacco"),
            Abilita("Cura", 12, 0, "💚 Una luce verde ti avvolge...", "cura", valore_extra=50),
        ]
        self.oggetti = {'Pozione': 3, 'Super Pozione': 1}

    def usa_oggetto(self, oggetto):
        """Usa un oggetto dall'inventario"""
        if oggetto not in self.oggetti or self.oggetti[oggetto] <= 0:
            print(f"❌ Non hai {oggetto}!")
            return False

        self.oggetti[oggetto] -= 1

        if oggetto == 'Pozione':
            cura = 50
            self.hp = min(self.hp_max, self.hp + cura)
            print(f"💊 Hai usato una Pozione! +{cura} HP")
            return True
        elif oggetto == 'Super Pozione':
            cura = 100
            self.hp = min(self.hp_max, self.hp + cura)
            print(f"💊 Hai usato una Super Pozione! +{cura} HP")
            return True

        return False


class Nemico(Combattente):
    """Classe per i nemici"""
    def __init__(self, nome, hp, mp, atk, defe, spd, livello, descrizione, exp_drop):
        super().__init__(nome, hp, mp, atk, defe, spd, livello)
        self.descrizione = descrizione
        self.exp_drop = exp_drop

    def ai_azione(self, giocatore):
        """AI semplice per decidere cosa fare"""
        # HP basso? Tenta di fuggire (non implementato) o attacca disperatamente
        if self.hp < self.hp_max * 0.3 and len(self.abilita) > 0:
            # Usa abilità più forte se possibile
            for abilita in sorted(self.abilita, key=lambda a: a.moltiplicatore_danno, reverse=True):
                if self.mp >= abilita.costo_mp:
                    return ('abilita', abilita)

        # 40% usa abilità se ha MP
        if len(self.abilita) > 0 and random.random() < 0.4:
            abilita_usabili = [a for a in self.abilita if self.mp >= a.costo_mp]
            if abilita_usabili:
                return ('abilita', random.choice(abilita_usabili))

        # Attacco normale
        return ('attacco', None)


# DATABASE NEMICI
def crea_nemico(tipo: str, livello: int = 1) -> Nemico:
    """Factory per creare nemici"""

    nemici_base = {
        'slime': {
            'nome': 'Slime',
            'hp': 50,
            'mp': 10,
            'atk': 10,
            'defe': 5,
            'spd': 8,
            'descrizione': '🟢 Una creatura gelatinosa che rimbalza verso di te!',
            'exp': 25,
            'abilita': [Abilita("Rimbalzo", 5, 1.2, "Rimbalza addosso a te!", "attacco")]
        },
        'goblin': {
            'nome': 'Goblin',
            'hp': 80,
            'mp': 15,
            'atk': 15,
            'defe': 10,
            'spd': 12,
            'descrizione': '👹 Un piccolo mostro verde con un randello!',
            'exp': 40,
            'abilita': [Abilita("Colpo Randello", 8, 1.4, "Ti colpisce col randello!", "attacco")]
        },
        'lupo': {
            'nome': 'Lupo Feroce',
            'hp': 100,
            'mp': 20,
            'atk': 22,
            'defe': 12,
            'spd': 20,
            'descrizione': '🐺 Un lupo dagli occhi rossi ringhia minaccioso!',
            'exp': 60,
            'abilita': [
                Abilita("Morso", 10, 1.5, "Ti azzanna ferocemente!", "attacco"),
                Abilita("Urlo", 15, 1.3, "Emette un urlo terrificante!", "attacco")
            ]
        },
        'scheletro': {
            'nome': 'Guerriero Scheletro',
            'hp': 120,
            'mp': 25,
            'atk': 25,
            'defe': 18,
            'spd': 15,
            'descrizione': '💀 Uno scheletro armato di spada e scudo!',
            'exp': 80,
            'abilita': [
                Abilita("Fendente", 12, 1.6, "Fende l'aria con la spada!", "attacco")
            ]
        },
        'drago': {
            'nome': 'Drago Oscuro',
            'hp': 300,
            'mp': 50,
            'atk': 40,
            'defe': 30,
            'spd': 25,
            'descrizione': '🐉 Un drago dalle scaglie nere! Le sue fauci sprizzano fuoco!',
            'exp': 200,
            'abilita': [
                Abilita("Soffio di Fuoco", 20, 2.5, "🔥 Sputa un torrente di fiamme!", "attacco"),
                Abilita("Morso Devastante", 15, 2.0, "Ti afferra con le sue fauci!", "attacco"),
                Abilita("Colpo di Coda", 10, 1.7, "La sua coda ti colpisce!", "attacco")
            ]
        }
    }

    if tipo not in nemici_base:
        tipo = 'slime'

    dati = nemici_base[tipo]

    # Scala statistiche con il livello
    hp = dati['hp'] + (livello - 1) * 20
    mp = dati['mp'] + (livello - 1) * 5
    atk = dati['atk'] + (livello - 1) * 3
    defe = dati['defe'] + (livello - 1) * 2
    spd = dati['spd'] + (livello - 1) * 1
    exp = dati['exp'] + (livello - 1) * 20

    nemico = Nemico(dati['nome'], hp, mp, atk, defe, spd, livello, dati['descrizione'], exp)
    nemico.abilita = dati['abilita']

    return nemico


class SistemaCombattimento:
    """Gestisce un combattimento tra giocatore e nemico"""

    def __init__(self, giocatore: Giocatore, nemico: Nemico):
        self.giocatore = giocatore
        self.nemico = nemico
        self.turno = 1
        self.vittoria_giocatore = False

    def mostra_stato(self):
        """Mostra lo stato attuale del combattimento"""
        print(f"\n{'='*70}")
        print(f"⚔️  {self.giocatore.nome} (Lv.{self.giocatore.livello})".ljust(35) +
              f"vs".center(10) +
              f"{self.nemico.nome} (Lv.{self.nemico.livello}) ⚔️ ".rjust(35))
        print(f"{'='*70}")

        # Giocatore
        print(f"🧙 {self.giocatore.nome}")
        print(f"   HP: {self.giocatore.hp}/{self.giocatore.hp_max} {self.giocatore.mostra_barra_hp()}")
        print(f"   MP: {self.giocatore.mp}/{self.giocatore.mp_max} {self.giocatore.mostra_barra_mp()}")

        print()

        # Nemico
        print(f"👾 {self.nemico.nome}")
        print(f"   HP: {self.nemico.hp}/{self.nemico.hp_max} {self.nemico.mostra_barra_hp()}")
        print(f"   MP: {self.nemico.mp}/{self.nemico.mp_max} {self.nemico.mostra_barra_mp()}")

        print(f"{'='*70}\n")

    def menu_azioni(self):
        """Mostra menu azioni e ritorna scelta"""
        print("Cosa fai?")
        print("1. ⚔️  Attacco normale")

        for i, abilita in enumerate(self.giocatore.abilita, 2):
            print(f"{i}. {abilita.nome} ({abilita.costo_mp} MP)")

        offset = len(self.giocatore.abilita) + 2
        print(f"{offset}. 🎒 Usa oggetto")
        print(f"{offset + 1}. 💨 Tenta fuga")

        while True:
            try:
                scelta = int(input("\n> "))
                if 1 <= scelta <= offset + 1:
                    return scelta
                else:
                    print("❌ Scelta non valida!")
            except ValueError:
                print("❌ Inserisci un numero!")

    def turno_giocatore(self):
        """Gestisce il turno del giocatore"""
        scelta = self.menu_azioni()

        if scelta == 1:
            # Attacco normale
            print(f"\n🧙 {self.giocatore.nome} attacca!")
            danno = self.giocatore.attacca(self.nemico)
            print(f"   💥 Danno: {danno} HP")

        elif 2 <= scelta <= len(self.giocatore.abilita) + 1:
            # Abilità
            abilita = self.giocatore.abilita[scelta - 2]
            print(f"\n🧙 {self.giocatore.nome} usa: {abilita.nome}!")
            self.giocatore.usa_abilita(abilita, self.nemico)

        elif scelta == len(self.giocatore.abilita) + 2:
            # Oggetti
            print("\n🎒 INVENTARIO:")
            for i, (obj, qta) in enumerate(self.giocatore.oggetti.items(), 1):
                print(f"{i}. {obj} (x{qta})")
            print(f"{len(self.giocatore.oggetti) + 1}. Annulla")

            try:
                scelta_obj = int(input("\n> "))
                if 1 <= scelta_obj <= len(self.giocatore.oggetti):
                    oggetto = list(self.giocatore.oggetti.keys())[scelta_obj - 1]
                    if not self.giocatore.usa_oggetto(oggetto):
                        return self.turno_giocatore()  # Riprova
            except ValueError:
                print("❌ Scelta non valida!")
                return self.turno_giocatore()

        elif scelta == len(self.giocatore.abilita) + 3:
            # Fuga
            probabilita = min(0.9, self.giocatore.spd / self.nemico.spd)
            if random.random() < probabilita:
                print(f"\n💨 {self.giocatore.nome} è fuggito!")
                return 'FUGA'
            else:
                print(f"\n❌ Non riesci a scappare!")

        return 'CONTINUA'

    def turno_nemico(self):
        """Gestisce il turno del nemico"""
        print(f"\n👾 Turno di {self.nemico.nome}!")
        time.sleep(1)

        azione, dati = self.nemico.ai_azione(self.giocatore)

        if azione == 'attacco':
            print(f"{self.nemico.nome} attacca!")
            danno = self.nemico.attacca(self.giocatore)
            print(f"   💥 Danno: {danno} HP")
        elif azione == 'abilita':
            abilita = dati
            print(f"{self.nemico.nome} usa: {abilita.nome}!")
            self.nemico.usa_abilita(abilita, self.giocatore)

    def combatti(self):
        """Loop principale del combattimento"""
        print(f"\n{'╔' + '═'*68 + '╗'}")
        print(f"║{'⚔️  COMBATTIMENTO INIZIATO! ⚔️'.center(68)}║")
        print(f"{'╚' + '═'*68 + '╝'}\n")
        print(self.nemico.descrizione)
        time.sleep(1.5)

        # Determina chi attacca per primo
        ordine = [self.giocatore, self.nemico] if self.giocatore.spd >= self.nemico.spd else [self.nemico, self.giocatore]
        primo = ordine[0]

        if primo == self.giocatore:
            print(f"\n⚡ Sei più veloce! Attacchi per primo!")
        else:
            print(f"\n⚠️  {self.nemico.nome} è più veloce! Attacca per primo!")

        time.sleep(1.5)

        while self.giocatore.e_vivo() and self.nemico.e_vivo():
            self.mostra_stato()

            if primo == self.giocatore:
                risultato = self.turno_giocatore()
                if risultato == 'FUGA':
                    return 'FUGA'

                if self.nemico.e_vivo():
                    time.sleep(1)
                    self.turno_nemico()
            else:
                self.turno_nemico()

                if self.giocatore.e_vivo():
                    time.sleep(1)
                    risultato = self.turno_giocatore()
                    if risultato == 'FUGA':
                        return 'FUGA'

            self.turno += 1
            time.sleep(1)

        # Risultato
        if self.giocatore.e_vivo():
            return self.vittoria()
        else:
            return self.sconfitta()

    def vittoria(self):
        """Gestisce la vittoria"""
        print(f"\n{'='*70}")
        print(f"🎉 VITTORIA! 🎉")
        print(f"{'='*70}")
        print(f"Hai sconfitto {self.nemico.nome}!")
        print(f"\n💰 Ricompense:")
        print(f"   EXP guadagnata: +{self.nemico.exp_drop}")

        level_ups = self.giocatore.guadagna_exp(self.nemico.exp_drop)

        print(f"\n{'='*70}")
        self.vittoria_giocatore = True
        return 'VITTORIA'

    def sconfitta(self):
        """Gestisce la sconfitta"""
        print(f"\n{'='*70}")
        print(f"💀 GAME OVER 💀")
        print(f"{'='*70}")
        print(f"Sei stato sconfitto da {self.nemico.nome}...")
        self.vittoria_giocatore = False
        return 'SCONFITTA'


def storia_introduttiva():
    """Storia introduttiva del gioco"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║             ⚔️  LA LEGGENDA DEL GUERRIERO PERDUTO ⚔️             ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

📖 C'era una volta un regno in pace, ma un giorno...

Un'oscurità si abbatté sulla terra. Mostri emersero dalle ombre.
Il re chiamò a raccolta tutti i guerrieri coraggiosi.

Tu sei uno di loro. La tua missione: sconfiggere il Drago Oscuro
che terrorizza il regno dalla sua torre!

Ma prima, dovrai allenarti affrontando i mostri più deboli...
    """)
    input("\n⏎ Premi INVIO per iniziare la tua avventura...")


def gioco_principale():
    """Funzione principale del gioco"""
    storia_introduttiva()

    # Creazione giocatore
    nome = input("\n👤 Qual è il tuo nome, guerriero? ")
    if not nome:
        nome = "Eroe"

    giocatore = Giocatore(nome)

    print(f"\n✨ Benvenuto, {giocatore.nome}!")
    print("\n📊 Le tue statistiche iniziali:")
    print(f"   HP: {giocatore.hp_max}")
    print(f"   MP: {giocatore.mp_max}")
    print(f"   ATK: {giocatore.atk}")
    print(f"   DEF: {giocatore.defe}")
    print(f"   SPD: {giocatore.spd}")

    time.sleep(2)

    # Sequenza di combattimenti
    sequenza_nemici = [
        ('slime', 1),
        ('goblin', 2),
        ('lupo', 3),
        ('scheletro', 4),
        ('drago', 5)  # Boss finale
    ]

    for i, (tipo_nemico, livello) in enumerate(sequenza_nemici, 1):
        if not giocatore.e_vivo():
            break

        # Ripristina HP/MP tra i combattimenti (tranne il boss)
        if i > 1 and tipo_nemico != 'drago':
            print(f"\n💚 Ti riposi prima del prossimo combattimento...")
            giocatore.hp = min(giocatore.hp_max, giocatore.hp + 50)
            giocatore.mp = min(giocatore.mp_max, giocatore.mp + 30)
            time.sleep(1.5)

        # Boss fight
        if tipo_nemico == 'drago':
            print(f"\n{'='*70}")
            print(f"🏰 Arrivi finalmente alla torre del Drago Oscuro...")
            print(f"{'='*70}")
            print(f"\nLe porte si aprono con un boato.\nUn drago immenso ti guarda dall'alto...\n")
            print("🐉 'FINALMENTE UN AVVERSARIO DEGNO!' tuona il drago.")
            time.sleep(3)
            print(f"\n⚠️  BOSS FIGHT! ⚠️")
            time.sleep(2)

        nemico = crea_nemico(tipo_nemico, livello)
        combattimento = SistemaCombattimento(giocatore, nemico)
        risultato = combattimento.combatti()

        if risultato == 'SCONFITTA':
            print("\n💀 Il tuo viaggio finisce qui...")
            break
        elif risultato == 'FUGA':
            print("\n💨 Sei fuggito, ma dovrai combattere di nuovo!")
            continue
        elif risultato == 'VITTORIA' and tipo_nemico == 'drago':
            # Vittoria finale!
            print(f"\n{'╔' + '═'*68 + '╗'}")
            print(f"║{'🏆  HAI SALVATO IL REGNO! 🏆'.center(68)}║")
            print(f"{'╚' + '═'*68 + '╝'}")
            print(f"""
Il Drago Oscuro cade sconfitto!
La luce torna sulla terra!

Il re ti nomina Eroe del Regno!
Il tuo nome verrà ricordato per sempre!

╔═══════════════════════════════════════════════════════════════════╗
║                        MISSIONE COMPLETATA!                       ║
║                                                                   ║
║                    Guerriero: {giocatore.nome.center(38)}║
║                    Livello finale: {str(giocatore.livello).center(33)}║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
            """)
            break

        time.sleep(2)


if __name__ == "__main__":
    gioco_principale()
