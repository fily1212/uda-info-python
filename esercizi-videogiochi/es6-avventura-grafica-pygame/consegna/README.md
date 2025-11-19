# Es6: Avventura Grafica con Pygame

## Obiettivi
- **Italiano**: Narrativa visuale, ambientazioni grafiche
- **Informatica**: Game loop, sprite, gestione eventi, rendering 2D

## Descrizione

Trasforma la tua avventura testuale in un **gioco grafico 2D** usando Pygame! Point-and-click, sprite animati, interfaccia grafica.

## Differenza con Esercizi Precedenti

### Es1-3 (Testuale):
```
> vai nord
Sei entrato nella cripta oscura...
```

### Es6 (Grafica):
```
[IMMAGINE della cripta]
[Personaggio animato che cammina]
[Click su porta] → Si apre
[Click su oggetto] → Lo raccogli
```

## Installazione Pygame

```bash
pip install pygame
```

## Concetti Base Pygame

### 1. Inizializzazione e Game Loop
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    # 1. GESTIONE EVENTI
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Gestisci click

    # 2. AGGIORNAMENTO LOGICA
    # Update posizioni, animazioni, ecc.

    # 3. RENDERING
    screen.fill((0, 0, 0))  # Sfondo nero
    # Disegna tutto
    pygame.display.flip()

    # 4. FPS
    clock.tick(60)  # 60 FPS

pygame.quit()
```

### 2. Sprite e Immagini
```python
class Personaggio(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('personaggio.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Animazioni, movimento
        pass

    def muovi(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
```

### 3. Gestione Click su Oggetti
```python
class Oggetto(pygame.sprite.Sprite):
    def __init__(self, x, y, immagine, nome):
        super().__init__()
        self.image = pygame.image.load(immagine)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nome = nome
        self.interagibile = True

    def on_click(self, giocatore):
        """Cosa succede quando clicchi sull'oggetto"""
        if self.interagibile:
            giocatore.raccogli(self)
            self.kill()  # Rimuovi dalla scena
            return f"Hai raccolto: {self.nome}"
```

### 4. Stanze con Background
```python
class Stanza:
    def __init__(self, nome, immagine_sfondo):
        self.nome = nome
        self.sfondo = pygame.image.load(immagine_sfondo)
        self.oggetti = pygame.sprite.Group()
        self.uscite = {}  # direzione: nuova_stanza

    def aggiungi_oggetto(self, oggetto):
        self.oggetti.add(oggetto)

    def draw(self, screen):
        # Disegna sfondo
        screen.blit(self.sfondo, (0, 0))
        # Disegna oggetti
        self.oggetti.draw(screen)
```

### 5. Interfaccia Utente
```python
class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 32)
        self.font_piccolo = pygame.font.Font(None, 24)

    def mostra_inventario(self, screen, inventario):
        """Mostra inventario in basso"""
        y = 500
        for i, oggetto in enumerate(inventario):
            x = 50 + i * 100
            # Disegna icona oggetto
            screen.blit(oggetto.icona, (x, y))
            # Nome oggetto
            testo = self.font_piccolo.render(oggetto.nome, True, (255, 255, 255))
            screen.blit(testo, (x, y + 60))

    def mostra_dialogo(self, screen, testo, personaggio=None):
        """Finestra di dialogo in basso"""
        # Box dialogo
        pygame.draw.rect(screen, (0, 0, 0), (50, 450, 700, 120))
        pygame.draw.rect(screen, (255, 255, 255), (50, 450, 700, 120), 3)

        # Testo
        righe = wrap_text(testo, 60)  # Spezza in righe
        for i, riga in enumerate(righe):
            superficie = self.font.render(riga, True, (255, 255, 255))
            screen.blit(superficie, (70, 470 + i * 30))
```

### 6. Animazioni
```python
class Animazione:
    def __init__(self, frames, fps=10):
        self.frames = frames  # Lista di immagini
        self.fps = fps
        self.frame_corrente = 0
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= 1000 / self.fps:
            self.timer = 0
            self.frame_corrente = (self.frame_corrente + 1) % len(self.frames)

    def get_frame(self):
        return self.frames[self.frame_corrente]

# Uso:
camminata = Animazione([
    pygame.image.load('walk1.png'),
    pygame.image.load('walk2.png'),
    pygame.image.load('walk3.png'),
])
```

### 7. Transizioni tra Stanze
```python
class TransizioneStanza:
    def __init__(self, stanza_attuale, stanza_nuova):
        self.alpha = 0
        self.in_corso = True
        self.fase = 'fade_out'  # fade_out → fade_in

    def update(self):
        if self.fase == 'fade_out':
            self.alpha += 10
            if self.alpha >= 255:
                self.alpha = 255
                self.fase = 'fade_in'
                # Cambia stanza
        elif self.fase == 'fade_in':
            self.alpha -= 10
            if self.alpha <= 0:
                self.in_corso = False

    def draw(self, screen):
        # Overlay nero con alpha
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(self.alpha)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
```

## Esercizio per Gli Studenti

### Parte 1: Asset Grafici
Crea o trova immagini per:
- Almeno 5 stanze (sfondi 800x600)
- Sprite personaggio (64x64)
  - Fermo
  - Camminata (4 frame)
- 10 oggetti interattivi (32x32 o 64x64)
- 3 personaggi NPC (64x64)
- UI: icone inventario, cursore

**Risorse gratuite:**
- [OpenGameArt.org](https://opengameart.org/)
- [itch.io](https://itch.io/game-assets/free)
- [Kenney.nl](https://kenney.nl/)

### Parte 2: Implementazione Base
Implementa:
- Game loop funzionante
- Personaggio che si muove (WASD o frecce)
- Click per raccogliere oggetti
- Cambio stanza (porte/uscite)
- Inventario visuale

### Parte 3: Features Avanzate
Aggiungi almeno 2 di:
- [ ] Animazioni personaggio
- [ ] Dialoghi con NPC (click su NPC)
- [ ] Puzzle (usa oggetto X su oggetto Y)
- [ ] Musica di sottofondo e effetti sonori
- [ ] Salvataggio/caricamento partita
- [ ] Menu principale (Nuova Partita/Carica/Esci)

## Struttura Progetto

```
progetto/
│
├── main.py              # File principale
├── classi/
│   ├── giocatore.py
│   ├── stanza.py
│   ├── oggetto.py
│   ├── npc.py
│   └── ui.py
│
├── assets/
│   ├── immagini/
│   │   ├── stanze/
│   │   ├── personaggi/
│   │   ├── oggetti/
│   │   └── ui/
│   ├── suoni/
│   └── musica/
│
└── dati/
    └── stanze.json      # Configurazione stanze
```

## Esempio: Struttura Main Loop

```python
import pygame
from classi.giocatore import Giocatore
from classi.stanza import carica_stanze
from classi.ui import UI

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("La Mia Avventura")
    clock = pygame.time.Clock()

    # Inizializzazione
    giocatore = Giocatore(400, 300)
    stanze = carica_stanze()
    stanza_corrente = stanze['ingresso']
    ui = UI()

    running = True
    while running:
        dt = clock.tick(60)

        # Eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Check click su oggetti
                for oggetto in stanza_corrente.oggetti:
                    if oggetto.rect.collidepoint(x, y):
                        messaggio = oggetto.on_click(giocatore)
                        ui.mostra_messaggio(messaggio)

                # Check click su uscite
                for uscita in stanza_corrente.uscite_visive:
                    if uscita.rect.collidepoint(x, y):
                        stanza_corrente = stanze[uscita.destinazione]

        # Movimento con tastiera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            giocatore.muovi(-5, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            giocatore.muovi(5, 0)

        # Update
        giocatore.update(dt)
        stanza_corrente.update(dt)

        # Rendering
        stanza_corrente.draw(screen)
        screen.blit(giocatore.image, giocatore.rect)
        ui.draw(screen, giocatore)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
```

## Esempio: Sistema di Dialoghi

```python
class SistemaDialoghi:
    def __init__(self):
        self.attivo = False
        self.testo_corrente = ""
        self.indice_carattere = 0
        self.velocita = 2  # Caratteri per frame
        self.completato = False

    def avvia(self, testo):
        self.attivo = True
        self.testo_corrente = testo
        self.indice_carattere = 0
        self.completato = False

    def update(self):
        if not self.completato:
            self.indice_carattere += self.velocita
            if self.indice_carattere >= len(self.testo_corrente):
                self.indice_carattere = len(self.testo_corrente)
                self.completato = True

    def get_testo_visibile(self):
        return self.testo_corrente[:int(self.indice_carattere)]

    def salta(self):
        """Salta animazione e mostra tutto"""
        self.indice_carattere = len(self.testo_corrente)
        self.completato = True
```

## Sound e Musica

```python
# Musica di sottofondo
pygame.mixer.music.load('assets/musica/tema_principale.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # Loop infinito

# Effetti sonori
suono_raccolta = pygame.mixer.Sound('assets/suoni/raccolta.wav')
suono_porta = pygame.mixer.Sound('assets/suoni/porta.wav')

# Riproduzione
suono_raccolta.play()
```

## Salvataggio Partita

```python
import json

def salva_partita(giocatore, stanza_corrente):
    dati = {
        'posizione_giocatore': [giocatore.rect.x, giocatore.rect.y],
        'stanza_corrente': stanza_corrente.nome,
        'inventario': [obj.nome for obj in giocatore.inventario],
        'oggetti_raccolti': giocatore.oggetti_raccolti_global
    }

    with open('salvataggio.json', 'w') as f:
        json.dump(dati, f, indent=2)

def carica_partita():
    with open('salvataggio.json', 'r') as f:
        return json.load(f)
```

## Valutazione

| Aspetto | Peso |
|---------|------|
| Qualità grafica (coerenza, estetica) | 20% |
| Gameplay fluido (60 FPS, niente bug) | 25% |
| Interfaccia intuitiva | 20% |
| Features implementate | 20% |
| Creatività | 15% |

## Tips per Performance

```python
# 1. Carica immagini una sola volta
IMMAGINI = {}
def carica_immagine(path):
    if path not in IMMAGINI:
        IMMAGINI[path] = pygame.image.load(path).convert_alpha()
    return IMMAGINI[path]

# 2. Usa dirty sprites per rendering parziale
class OggettoOttimizzato(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.dirty = 1  # Renderizza solo quando cambia

# 3. Limita area di rendering
screen.set_clip(pygame.Rect(0, 0, 800, 600))
```

## Esempi di Giochi Point-and-Click

- **Monkey Island** - Classico avventura grafica
- **Machinarium** - Arte splendida
- **Deponia** - Umorismo e puzzle
- **Grim Fandango** - Atmosfera noir

**Trasforma la tua storia in un'esperienza visuale! 🎨🎮**
