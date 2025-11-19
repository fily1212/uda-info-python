# Es5: Sistema di Combattimento a Turni (RPG)

## Obiettivi
- **Italiano**: Descrivere azioni di combattimento, creare nemici caratterizzati
- **Informatica**: Sistemi a turni, bilanciamento statistiche, AI base

## Descrizione

Crea un **sistema di combattimento RPG** come nei classici Final Fantasy, Pokémon, Dragon Quest! Turni alternati, abilità speciali, sistema di livelli.

## Meccaniche di Combattimento

### Statistiche Base
```python
class Combattente:
    HP (Health Points): Punti vita
    MP (Magic Points): Punti magia per abilità
    ATK (Attack): Forza fisica
    DEF (Defense): Resistenza ai danni
    SPD (Speed): Chi è più veloce attacca per primo
```

### Formula Danni
```
Danno = (ATK attaccante - DEF difensore/2) × moltiplicatore_casuale
moltiplicatore_casuale = random(0.85, 1.15)  # ±15%
```

### Abilità Speciali
Ogni personaggio ha abilità che costano MP:

```python
ABILITA = {
    'Attacco Forte': {
        'costo_mp': 10,
        'danno': 'ATK × 1.5',
        'descrizione': 'Colpisci con tutta la tua forza!'
    },
    'Palla di Fuoco': {
        'costo_mp': 15,
        'danno': 'ATK × 2.0',
        'descrizione': 'Lanci una sfera di fuoco!'
    },
    'Cura': {
        'costo_mp': 12,
        'effetto': '+50 HP',
        'descrizione': 'Recuperi energia vitale'
    }
}
```

### Sistema Livelli
```python
# Guadagni EXP sconfiggendo nemici
EXP necessaria = livello_corrente × 100

# Al level up:
HP_max += 20
MP_max += 10
ATK += 5
DEF += 3
SPD += 2
```

## Implementazione

### Classe Combattente
```python
class Combattente:
    def __init__(self, nome, hp, mp, atk, defe, spd):
        self.nome = nome
        self.hp_max = hp
        self.hp = hp
        self.mp_max = mp
        self.mp = mp
        self.atk = atk
        self.defe = defe
        self.spd = spd
        self.livello = 1
        self.exp = 0
        self.abilita = []

    def attacca(self, bersaglio):
        """Attacco base"""
        danno = self.calcola_danno(self.atk, bersaglio.defe)
        bersaglio.ricevi_danno(danno)
        return danno

    def usa_abilita(self, abilita, bersaglio):
        """Usa un'abilità speciale"""
        if self.mp >= abilita.costo_mp:
            self.mp -= abilita.costo_mp
            # Esegui effetto abilità
        else:
            print("❌ MP insufficienti!")

    def ricevi_danno(self, danno):
        self.hp -= danno
        if self.hp < 0:
            self.hp = 0

    def e_vivo(self):
        return self.hp > 0

    def guadagna_exp(self, exp):
        self.exp += exp
        # Controlla level up
        while self.exp >= self.exp_per_level_up():
            self.level_up()
```

### Classe Combattimento
```python
class SistemaCombattimento:
    def __init__(self, giocatore, nemico):
        self.giocatore = giocatore
        self.nemico = nemico
        self.turno = 1

    def determina_ordine(self):
        """Chi attacca per primo? Basato su SPD"""
        if self.giocatore.spd >= self.nemico.spd:
            return [self.giocatore, self.nemico]
        else:
            return [self.nemico, self.giocatore]

    def turno_nemico(self):
        """AI semplice del nemico"""
        # 70% attacco normale, 30% abilità (se ha MP)
        if random.random() < 0.3 and self.nemico.mp > 0:
            abilita = random.choice(self.nemico.abilita)
            if self.nemico.mp >= abilita.costo_mp:
                self.nemico.usa_abilita(abilita, self.giocatore)
                return

        self.nemico.attacca(self.giocatore)

    def combatti(self):
        """Loop principale del combattimento"""
        while self.giocatore.e_vivo() and self.nemico.e_vivo():
            self.mostra_stato()
            azione = self.chiedi_azione()
            self.esegui_azione(azione)

            if self.nemico.e_vivo():
                self.turno_nemico()

            self.turno += 1

        if self.giocatore.e_vivo():
            self.vittoria()
        else:
            self.sconfitta()
```

## Esercizio per Gli Studenti

### Parte 1: Creazione Personaggi
Crea almeno:
- 1 personaggio giocatore con background
- 5 nemici diversi (facili, medi, difficili)
- 3 boss con abilità speciali

Esempi:
```
Slime (Facile):
HP: 50, ATK: 10, DEF: 5
Descrizione: "Una creatura gelatinosa che rimbalza verso di te!"

Drago Oscuro (Boss):
HP: 300, ATK: 50, DEF: 30
Abilità: Soffio di Fuoco (danno massivo)
Descrizione: "Le sue scaglie nere brillano nella luce..."
```

### Parte 2: Bilanciamento
Testa il combattimento e assicurati che:
- I nemici facili siano battibili a livello 1-3
- I nemici medi richiedano livello 5-7
- I boss siano sfide a livello 10+

### Parte 3: Estensioni
Aggiungi almeno 2 di queste feature:
- [ ] Sistema di oggetti (pozioni HP/MP)
- [ ] Colpi critici (5% di probabilità, danno ×2)
- [ ] Elementi (Fuoco > Ghiaccio > Terra > Fuoco)
- [ ] Stato alterati (veleno, sonno, paralisi)
- [ ] Equipaggiamento (armi, armature)

## Esempio di Combattimento

```
╔════════════════════════════════════════════════╗
║           ⚔️  COMBATTIMENTO! ⚔️                ║
╚════════════════════════════════════════════════╝

🧙 Eroe                  vs                🐉 Drago
HP: 100/100 ████████████                  HP: 150/150 ████████████
MP:  50/50  ████████████                  MP:  30/30  ████████████

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TURNO 1

Cosa fai?
1. ⚔️  Attacco normale
2. 🔥 Palla di Fuoco (15 MP)
3. ⚡ Fulmine (20 MP)
4. 💚 Cura (12 MP)
5. 🎒 Usa oggetto

> 2

🧙 Eroe usa: Palla di Fuoco!
🔥 Una sfera infuocata colpisce il Drago!
💥 Danno: 45 HP

🐉 Drago: HP 105/150 ████████░░░░

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐉 Turno del Drago!
Il Drago ti colpisce con gli artigli!
💥 Danno: 25 HP

🧙 Eroe: HP 75/100 █████████░░░

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Risorse

### Formule Bilanciamento
```
HP_nemico = 30 + (livello × 20)
ATK_nemico = 5 + (livello × 3)
EXP_drop = livello × 25
```

### RPG Famosi da Studiare
- **Final Fantasy** - Combattimento ATB (Active Time Battle)
- **Pokémon** - Sistema di tipi/debolezze
- **Dragon Quest** - Combattimento a turni classico
- **Undertale** - Combattimento con bullet hell

## Valutazione

| Aspetto | Peso |
|---------|------|
| Bilanciamento statistiche | 25% |
| Descrizioni azioni/nemici | 20% |
| AI nemici (varietà) | 20% |
| Sistema livelli funzionante | 15% |
| Features extra | 20% |

## Bonus: Sistema di Fuga

```python
def tenta_fuga(self):
    """Prova a scappare dal combattimento"""
    probabilita = min(0.9, self.giocatore.spd / self.nemico.spd)
    if random.random() < probabilita:
        print("💨 Sei fuggito!")
        return True
    else:
        print("❌ Non riesci a scappare!")
        return False
```

**Trasforma le battaglie in esperienze epiche! ⚔️🔥**
