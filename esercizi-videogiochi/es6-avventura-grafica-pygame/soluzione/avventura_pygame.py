# 🎮 AVVENTURA GRAFICA PYGAME - SOLUZIONE
# "Il Mistero della Casa Abbandonata"
# Point-and-click adventure game

import pygame
import sys
import json
from enum import Enum
from typing import List, Dict, Optional

# Inizializzazione Pygame
pygame.init()

# Costanti
LARGHEZZA = 800
ALTEZZA = 600
FPS = 60

# Colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
GRIGIO = (128, 128, 128)
VERDE = (0, 255, 0)
ROSSO = (255, 0, 0)
BLU = (100, 100, 255)
GIALLO = (255, 255, 0)

class Stato(Enum):
    """Stati del gioco"""
    MENU = 1
    GIOCO = 2
    INVENTARIO = 3
    DIALOGO = 4
    VITTORIA = 5


class Oggetto:
    """Oggetto interattivo nel gioco"""
    def __init__(self, nome: str, x: int, y: int, larghezza: int, altezza: int,
                 colore: tuple, descrizione: str, raccoglibile: bool = True):
        self.nome = nome
        self.rect = pygame.Rect(x, y, larghezza, altezza)
        self.colore = colore
        self.descrizione = descrizione
        self.raccoglibile = raccoglibile
        self.raccolto = False

    def draw(self, screen):
        """Disegna l'oggetto"""
        if not self.raccolto:
            pygame.draw.rect(screen, self.colore, self.rect)
            # Bordino per renderlo più visibile
            pygame.draw.rect(screen, BIANCO, self.rect, 2)

    def on_click(self):
        """Cosa succede quando viene cliccato"""
        if self.raccoglibile and not self.raccolto:
            self.raccolto = True
            return f"Hai raccolto: {self.nome}"
        elif not self.raccoglibile:
            return self.descrizione
        return None


class Uscita:
    """Porta/uscita verso un'altra stanza"""
    def __init__(self, x: int, y: int, larghezza: int, altezza: int,
                 destinazione: str, direzione: str):
        self.rect = pygame.Rect(x, y, larghezza, altezza)
        self.destinazione = destinazione
        self.direzione = direzione
        self.colore = (100, 50, 0)  # Marrone per porta

    def draw(self, screen):
        """Disegna l'uscita"""
        pygame.draw.rect(screen, self.colore, self.rect)
        pygame.draw.rect(screen, BIANCO, self.rect, 3)

        # Testo direzione
        font = pygame.font.Font(None, 24)
        testo = font.render(self.direzione, True, BIANCO)
        screen.blit(testo, (self.rect.centerx - testo.get_width()//2,
                           self.rect.centery - testo.get_height()//2))


class Stanza:
    """Una stanza del gioco"""
    def __init__(self, nome: str, descrizione: str, colore_sfondo: tuple):
        self.nome = nome
        self.descrizione = descrizione
        self.colore_sfondo = colore_sfondo
        self.oggetti: List[Oggetto] = []
        self.uscite: List[Uscita] = []
        self.visitata = False

    def aggiungi_oggetto(self, oggetto: Oggetto):
        self.oggetti.append(oggetto)

    def aggiungi_uscita(self, uscita: Uscita):
        self.uscite.append(uscita)

    def draw(self, screen):
        """Disegna la stanza"""
        # Sfondo
        screen.fill(self.colore_sfondo)

        # Disegna descrizione se prima visita
        if not self.visitata:
            font = pygame.font.Font(None, 28)
            righe = self.wrap_text(self.descrizione, 70)
            for i, riga in enumerate(righe[:3]):  # Max 3 righe
                testo = font.render(riga, True, BIANCO)
                screen.blit(testo, (50, 50 + i * 30))

        # Titolo stanza
        font_titolo = pygame.font.Font(None, 36)
        titolo = font_titolo.render(self.nome, True, BIANCO)
        pygame.draw.rect(screen, NERO, (0, 0, LARGHEZZA, 40))
        screen.blit(titolo, (20, 5))

        # Oggetti
        for oggetto in self.oggetti:
            oggetto.draw(screen)

        # Uscite
        for uscita in self.uscite:
            uscita.draw(screen)

        self.visitata = True

    @staticmethod
    def wrap_text(testo: str, max_larghezza: int) -> List[str]:
        """Spezza il testo in righe"""
        parole = testo.split()
        righe = []
        riga_corrente = []

        for parola in parole:
            riga_corrente.append(parola)
            if len(' '.join(riga_corrente)) > max_larghezza:
                riga_corrente.pop()
                righe.append(' '.join(riga_corrente))
                riga_corrente = [parola]

        if riga_corrente:
            righe.append(' '.join(riga_corrente))

        return righe


class Giocatore:
    """Il giocatore"""
    def __init__(self):
        self.inventario: List[Oggetto] = []
        self.stanza_corrente: Optional[str] = None

    def raccogli(self, oggetto: Oggetto):
        """Raccogli un oggetto"""
        if oggetto not in self.inventario:
            self.inventario.append(oggetto)

    def ha_oggetto(self, nome: str) -> bool:
        """Controlla se ha un oggetto"""
        return any(obj.nome == nome for obj in self.inventario)


class UI:
    """Interfaccia utente"""
    def __init__(self):
        self.font = pygame.font.Font(None, 28)
        self.font_piccolo = pygame.font.Font(None, 20)
        self.messaggio = ""
        self.timer_messaggio = 0

    def mostra_messaggio(self, testo: str, durata: int = 3000):
        """Mostra un messaggio temporaneo"""
        self.messaggio = testo
        self.timer_messaggio = durata

    def update(self, dt):
        """Aggiorna timer messaggi"""
        if self.timer_messaggio > 0:
            self.timer_messaggio -= dt

    def draw_inventario_bottom(self, screen, inventario: List[Oggetto]):
        """Disegna inventario in basso allo schermo"""
        # Box inventario
        pygame.draw.rect(screen, (50, 50, 50), (0, ALTEZZA - 80, LARGHEZZA, 80))
        pygame.draw.rect(screen, BIANCO, (0, ALTEZZA - 80, LARGHEZZA, 80), 2)

        # Titolo
        testo = self.font_piccolo.render("INVENTARIO (I per dettagli):", True, BIANCO)
        screen.blit(testo, (10, ALTEZZA - 75))

        # Oggetti
        for i, oggetto in enumerate(inventario):
            x = 30 + i * 100
            y = ALTEZZA - 50

            # Icona oggetto (quadratino colorato)
            pygame.draw.rect(screen, oggetto.colore, (x, y, 40, 40))
            pygame.draw.rect(screen, BIANCO, (x, y, 40, 40), 2)

            # Nome
            nome_breve = oggetto.nome[:8]
            testo_nome = self.font_piccolo.render(nome_breve, True, BIANCO)
            screen.blit(testo_nome, (x - 5, y + 42))

    def draw_messaggio(self, screen):
        """Disegna messaggio temporaneo"""
        if self.timer_messaggio > 0:
            # Box messaggio
            larghezza_box = 600
            altezza_box = 60
            x = (LARGHEZZA - larghezza_box) // 2
            y = 150

            pygame.draw.rect(screen, (0, 0, 0, 200), (x, y, larghezza_box, altezza_box))
            pygame.draw.rect(screen, GIALLO, (x, y, larghezza_box, altezza_box), 3)

            # Testo
            testo = self.font.render(self.messaggio, True, BIANCO)
            screen.blit(testo, (x + 20, y + 15))

    def draw_schermata_inventario(self, screen, inventario: List[Oggetto]):
        """Schermata inventario completa"""
        screen.fill((30, 30, 30))

        # Titolo
        font_titolo = pygame.font.Font(None, 48)
        titolo = font_titolo.render("INVENTARIO", True, GIALLO)
        screen.blit(titolo, (LARGHEZZA//2 - titolo.get_width()//2, 50))

        # Istruzioni
        istruzioni = self.font_piccolo.render("Premi I o ESC per chiudere", True, GRIGIO)
        screen.blit(istruzioni, (LARGHEZZA//2 - istruzioni.get_width()//2, 100))

        # Oggetti
        if not inventario:
            vuoto = self.font.render("Inventario vuoto", True, GRIGIO)
            screen.blit(vuoto, (LARGHEZZA//2 - vuoto.get_width()//2, ALTEZZA//2))
        else:
            for i, oggetto in enumerate(inventario):
                y = 150 + i * 80

                # Icona
                pygame.draw.rect(screen, oggetto.colore, (100, y, 60, 60))
                pygame.draw.rect(screen, BIANCO, (100, y, 60, 60), 2)

                # Nome
                nome = self.font.render(oggetto.nome, True, BIANCO)
                screen.blit(nome, (180, y + 5))

                # Descrizione
                desc = self.font_piccolo.render(oggetto.descrizione, True, GRIGIO)
                screen.blit(desc, (180, y + 35))


class Gioco:
    """Classe principale del gioco"""
    def __init__(self):
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        pygame.display.set_caption("Il Mistero della Casa Abbandonata")
        self.clock = pygame.time.Clock()
        self.running = True
        self.stato = Stato.MENU

        self.giocatore = Giocatore()
        self.ui = UI()
        self.stanze: Dict[str, Stanza] = {}

        self.crea_mondo()

    def crea_mondo(self):
        """Crea tutte le stanze e oggetti del gioco"""

        # STANZA 1: Ingresso
        ingresso = Stanza(
            "Ingresso della Casa",
            "Un ingresso polveroso. C'è un odore di chiuso. Vedi porte a nord e est.",
            (40, 40, 50)
        )
        ingresso.aggiungi_oggetto(Oggetto(
            "Chiave", 200, 300, 30, 30, GIALLO,
            "Una vecchia chiave arrugginita", True
        ))
        ingresso.aggiungi_oggetto(Oggetto(
            "Quadro", 500, 200, 80, 120, (100, 70, 50),
            "Un quadro di una famiglia felice... ora coperto di polvere", False
        ))
        ingresso.aggiungi_uscita(Uscita(350, 100, 100, 50, "salone", "NORD"))
        ingresso.aggiungi_uscita(Uscita(650, 250, 50, 100, "cucina", "EST"))
        self.stanze["ingresso"] = ingresso

        # STANZA 2: Salone
        salone = Stanza(
            "Salone",
            "Un grande salone con mobili coperti da lenzuola bianche.",
            (50, 30, 30)
        )
        salone.aggiungi_oggetto(Oggetto(
            "Candelabro", 300, 250, 40, 60, (200, 180, 0),
            "Un candelabro d'oro prezioso", True
        ))
        salone.aggiungi_oggetto(Oggetto(
            "Libreria", 100, 150, 100, 200, (80, 50, 30),
            "Scaffali pieni di libri antichi", False
        ))
        salone.aggiungi_uscita(Uscita(350, 450, 100, 50, "ingresso", "SUD"))
        salone.aggiungi_uscita(Uscita(650, 250, 50, 100, "biblioteca", "EST"))
        self.stanze["salone"] = salone

        # STANZA 3: Cucina
        cucina = Stanza(
            "Cucina",
            "Pentole arrugginite e un vecchio forno. Sul tavolo c'è qualcosa...",
            (60, 50, 40)
        )
        cucina.aggiungi_oggetto(Oggetto(
            "Coltello", 350, 300, 40, 20, (150, 150, 150),
            "Un coltello da cucina ancora affilato", True
        ))
        cucina.aggiungi_oggetto(Oggetto(
            "Torcia", 500, 280, 30, 60, ROSSO,
            "Una torcia elettrica funzionante!", True
        ))
        cucina.aggiungi_uscita(Uscita(50, 250, 50, 100, "ingresso", "OVEST"))
        cucina.aggiungi_uscita(Uscita(350, 100, 100, 50, "cantina", "SCALE GIÙ"))
        self.stanze["cucina"] = cucina

        # STANZA 4: Biblioteca
        biblioteca = Stanza(
            "Biblioteca Segreta",
            "Sei entrato in una stanza nascosta! Libri ovunque e... un tesoro?",
            (30, 50, 70)
        )
        biblioteca.aggiungi_oggetto(Oggetto(
            "Libro Magico", 300, 250, 60, 80, BLU,
            "Un libro che brilla di luce propria!", True
        ))
        biblioteca.aggiungi_oggetto(Oggetto(
            "TESORO", 400, 350, 80, 80, GIALLO,
            "IL TESORO DELLA CASA! L'hai trovato!", True
        ))
        biblioteca.aggiungi_uscita(Uscita(50, 250, 50, 100, "salone", "OVEST"))
        self.stanze["biblioteca"] = biblioteca

        # STANZA 5: Cantina (richiede torcia)
        cantina = Stanza(
            "Cantina Buia",
            "È completamente buio. Hai bisogno di una torcia!",
            (10, 10, 10)
        )
        cantina.aggiungi_oggetto(Oggetto(
            "Mappa", 400, 300, 50, 40, (200, 200, 150),
            "Una mappa della casa con una X segnata!", True
        ))
        cantina.aggiungi_uscita(Uscita(350, 100, 100, 50, "cucina", "SCALE SU"))
        self.stanze["cantina"] = cantina

        # Posizione iniziale
        self.giocatore.stanza_corrente = "ingresso"

    def gestisci_eventi(self):
        """Gestisce gli eventi"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Menu
                if self.stato == Stato.MENU:
                    if event.key == pygame.K_SPACE:
                        self.stato = Stato.GIOCO

                # Gioco
                elif self.stato == Stato.GIOCO:
                    if event.key == pygame.K_i:
                        self.stato = Stato.INVENTARIO
                    elif event.key == pygame.K_ESCAPE:
                        self.stato = Stato.MENU

                # Inventario
                elif self.stato == Stato.INVENTARIO:
                    if event.key == pygame.K_i or event.key == pygame.K_ESCAPE:
                        self.stato = Stato.GIOCO

                # Vittoria
                elif self.stato == Stato.VITTORIA:
                    if event.key == pygame.K_SPACE:
                        self.stato = Stato.MENU
                        self.crea_mondo()  # Reset gioco

            if event.type == pygame.MOUSEBUTTONDOWN and self.stato == Stato.GIOCO:
                self.gestisci_click(event.pos)

    def gestisci_click(self, pos):
        """Gestisce i click del mouse"""
        stanza = self.stanze[self.giocatore.stanza_corrente]

        # Click su oggetti
        for oggetto in stanza.oggetti:
            if oggetto.rect.collidepoint(pos) and not oggetto.raccolto:
                # Cantina buia: serve torcia
                if self.giocatore.stanza_corrente == "cantina":
                    if not self.giocatore.ha_oggetto("Torcia"):
                        self.ui.mostra_messaggio("È troppo buio! Serve una torcia!")
                        return

                messaggio = oggetto.on_click()
                if messaggio:
                    self.ui.mostra_messaggio(messaggio)
                    if oggetto.raccoglibile:
                        self.giocatore.raccogli(oggetto)

                        # Controlla vittoria
                        if oggetto.nome == "TESORO":
                            self.stato = Stato.VITTORIA
                return

        # Click su uscite
        for uscita in stanza.uscite:
            if uscita.rect.collidepoint(pos):
                # Biblioteca richiede chiave
                if uscita.destinazione == "biblioteca":
                    if not self.giocatore.ha_oggetto("Chiave"):
                        self.ui.mostra_messaggio("La porta è chiusa! Serve una chiave!")
                        return
                    else:
                        self.ui.mostra_messaggio("Hai aperto la porta con la chiave!")

                self.giocatore.stanza_corrente = uscita.destinazione
                return

    def update(self):
        """Aggiorna logica di gioco"""
        dt = self.clock.tick(FPS)
        self.ui.update(dt)

    def draw(self):
        """Disegna tutto"""
        if self.stato == Stato.MENU:
            self.draw_menu()
        elif self.stato == Stato.GIOCO:
            self.draw_gioco()
        elif self.stato == Stato.INVENTARIO:
            self.ui.draw_schermata_inventario(self.screen, self.giocatore.inventario)
        elif self.stato == Stato.VITTORIA:
            self.draw_vittoria()

        pygame.display.flip()

    def draw_menu(self):
        """Disegna menu principale"""
        self.screen.fill((20, 20, 40))

        # Titolo
        font_titolo = pygame.font.Font(None, 64)
        titolo = font_titolo.render("Il Mistero della Casa Abbandonata", True, GIALLO)
        self.screen.blit(titolo, (LARGHEZZA//2 - titolo.get_width()//2, 150))

        # Sottotitolo
        font_sub = pygame.font.Font(None, 32)
        sub = font_sub.render("Un'avventura point-and-click", True, BIANCO)
        self.screen.blit(sub, (LARGHEZZA//2 - sub.get_width()//2, 230))

        # Istruzioni
        font_testo = pygame.font.Font(None, 28)
        istruzioni = [
            "",
            "STORIA:",
            "Sei entrato in una casa abbandonata.",
            "Si dice che nasconda un tesoro...",
            "",
            "COMANDI:",
            "CLICK = Interagisci con oggetti e porte",
            "I = Inventario",
            "ESC = Menu",
            "",
            "Premi SPAZIO per iniziare"
        ]

        for i, riga in enumerate(istruzioni):
            colore = GIALLO if "SPAZIO" in riga else BIANCO
            testo = font_testo.render(riga, True, colore)
            self.screen.blit(testo, (LARGHEZZA//2 - testo.get_width()//2, 300 + i * 30))

    def draw_gioco(self):
        """Disegna il gioco"""
        stanza = self.stanze[self.giocatore.stanza_corrente]

        # Stanza
        stanza.draw(self.screen)

        # UI
        self.ui.draw_inventario_bottom(self.screen, self.giocatore.inventario)
        self.ui.draw_messaggio(self.screen)

        # Mostra hint per cantina buia
        if self.giocatore.stanza_corrente == "cantina" and not self.giocatore.ha_oggetto("Torcia"):
            font = pygame.font.Font(None, 36)
            testo = font.render("È BUIO PESTO! Serve una torcia!", True, BIANCO)
            self.screen.blit(testo, (LARGHEZZA//2 - testo.get_width()//2, ALTEZZA//2))

    def draw_vittoria(self):
        """Schermata vittoria"""
        self.screen.fill((50, 20, 80))

        # Titolo
        font_titolo = pygame.font.Font(None, 72)
        titolo = font_titolo.render("🏆 VITTORIA! 🏆", True, GIALLO)
        self.screen.blit(titolo, (LARGHEZZA//2 - titolo.get_width()//2, 150))

        # Testo
        font_testo = pygame.font.Font(None, 32)
        testi = [
            "",
            "Hai trovato il tesoro della casa abbandonata!",
            "",
            f"Oggetti raccolti: {len(self.giocatore.inventario)}",
            "",
            "Congratulazioni!",
            "",
            "Premi SPAZIO per tornare al menu"
        ]

        for i, riga in enumerate(testi):
            testo = font_testo.render(riga, True, BIANCO)
            self.screen.blit(testo, (LARGHEZZA//2 - testo.get_width()//2, 280 + i * 40))

    def run(self):
        """Loop principale"""
        while self.running:
            self.gestisci_eventi()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    gioco = Gioco()
    gioco.run()
