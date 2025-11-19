"""
TEXT ADVENTURE ENGINE
=====================

Motore completo per avventure testuali con parser di linguaggio naturale.
Progettato per l'UDA Avventure Testuali - Narrativa e Parser

Autore: Sistema Didattico
Versione: 1.0

CLASSI PRINCIPALI:
- Game: Gestisce il gioco principale
- Room: Rappresenta una stanza/location
- Item: Rappresenta un oggetto interattivo
- NPC: Rappresenta un personaggio non giocante
- Parser: Analizza i comandi del giocatore
"""

import re
from typing import Dict, List, Callable, Optional, Set, Any


# ============================================================================
# PARSER DI LINGUAGGIO NATURALE
# ============================================================================

class Parser:
    """
    Parser di comandi in linguaggio naturale italiano.
    Gestisce sinonimi, articoli, preposizioni e varianti.
    """

    def __init__(self):
        # Dizionario dei verbi e loro sinonimi
        self.verbs = {
            'vai': ['vai', 'va', 'muovi', 'muoviti', 'cammina', 'dirigiti', 'procedi', 'entra'],
            'nord': ['nord', 'n', 'su in alto', 'sopra'],
            'sud': ['sud', 's', 'giù in basso', 'sotto'],
            'est': ['est', 'e', 'destra'],
            'ovest': ['ovest', 'o', 'ovst', 'sinistra'],
            'su': ['su', 'sali', 'scala'],
            'giù': ['giù', 'scendi', 'giu'],
            'prendi': ['prendi', 'raccogli', 'afferra', 'prendo', 'prende', 'prenda', 'togli', 'prendi', 'ottieni'],
            'lascia': ['lascia', 'posa', 'metti giù', 'rilascia', 'butta', 'getta'],
            'osserva': ['osserva', 'guarda', 'esamina', 'ispeziona', 'controlla', 'leggi', 'vedi', 'scruta'],
            'usa': ['usa', 'utilizza', 'adopera', 'aziona', 'attiva', 'impiega'],
            'parla': ['parla', 'dialoga', 'conversa', 'chiacchiera', 'chiedi', 'domanda', 'interroga'],
            'inventario': ['inventario', 'inv', 'i', 'zaino', 'borsa', 'tasche', 'oggetti'],
            'aiuto': ['aiuto', 'help', '?', 'comandi', 'come si gioca'],
            'guarda': ['guarda', 'descrizione', 'desc', 'dove sono', 'guardati intorno'],
            'apri': ['apri', 'spalanca', 'sblocca'],
            'chiudi': ['chiudi', 'serra', 'blocca'],
            'combina': ['combina', 'unisci', 'mescola', 'metti insieme'],
            'tira': ['tira', 'strappa', 'estrai'],
            'spingi': ['spingi', 'premi', 'schiaccia', 'pigi'],
            'tocca': ['tocca', 'palpa', 'sfiora', 'tastare'],
            'ascolta': ['ascolta', 'senti', 'odi'],
            'annusa': ['annusa', 'odora', 'fiuta'],
            'mangia': ['mangia', 'assaggia', 'gusta'],
            'bevi': ['bevi', 'sorseggia', 'tracanna'],
            'rompi': ['rompi', 'distruggi', 'frantuma', 'spacca'],
            'esci': ['esci', 'exit', 'quit', 'chiudi', 'termina'],
        }

        # Direzioni valide
        self.directions = ['nord', 'sud', 'est', 'ovest', 'su', 'giù', 'n', 's', 'e', 'o']

        # Parole da ignorare (articoli, preposizioni, ecc.)
        self.noise_words = {
            'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una',
            'del', 'dello', 'della', 'dei', 'degli', 'delle',
            'al', 'allo', 'alla', 'ai', 'agli', 'alle',
            'nel', 'nello', 'nella', 'nei', 'negli', 'nelle',
            'sul', 'sullo', 'sulla', 'sui', 'sugli', 'sulle',
            'per', 'con', 'da', 'in', 'su', 'a', 'di',
            'che', 'cosa', 'è', 'e', 'ed'
        }

    def normalize_verb(self, word: str) -> Optional[str]:
        """Converte un sinonimo nel verbo canonico."""
        word = word.lower().strip()
        for canonical, synonyms in self.verbs.items():
            if word in synonyms:
                return canonical
        return None

    def clean_input(self, text: str) -> List[str]:
        """Pulisce l'input rimuovendo punteggiatura e parole inutili."""
        # Rimuove punteggiatura
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        # Divide in parole
        words = text.split()
        # Rimuove noise words ma mantiene le parole importanti
        cleaned = []
        for word in words:
            if word not in self.noise_words or len(cleaned) == 0:
                # Mantiene la prima parola anche se è noise
                if word not in self.noise_words:
                    cleaned.append(word)
        return cleaned

    def parse(self, command: str) -> Dict[str, Any]:
        """
        Analizza un comando e restituisce un dizionario strutturato.

        Returns:
            {
                'verb': str,           # Verbo canonico
                'target': str,         # Oggetto target (se presente)
                'secondary': str,      # Oggetto secondario (se presente)
                'raw': str,           # Comando originale
                'words': List[str]    # Parole pulite
            }
        """
        result = {
            'verb': None,
            'target': None,
            'secondary': None,
            'raw': command,
            'words': []
        }

        # Pulisce l'input
        words = self.clean_input(command)
        result['words'] = words

        if not words:
            return result

        # Normalizza il primo verbo trovato
        verb = self.normalize_verb(words[0])

        # Gestione speciale per direzioni
        if words[0] in self.directions:
            result['verb'] = 'vai'
            result['target'] = self.normalize_verb(words[0]) or words[0]
            return result

        if verb:
            result['verb'] = verb
            # Il resto sono target
            if len(words) > 1:
                # Cerca 'con', 'e', 'usando' per trovare oggetto secondario
                secondary_markers = ['con', 'usando', 'e', 'su']
                target_words = []
                secondary_words = []
                found_marker = False

                for i, word in enumerate(words[1:], 1):
                    if word in secondary_markers and i < len(words) - 1:
                        found_marker = True
                        continue
                    if found_marker:
                        secondary_words.append(word)
                    else:
                        target_words.append(word)

                result['target'] = ' '.join(target_words) if target_words else None
                result['secondary'] = ' '.join(secondary_words) if secondary_words else None
        else:
            # Prova a interpretare come direzione singola
            if words[0] in self.directions:
                result['verb'] = 'vai'
                result['target'] = words[0]

        return result

    def get_help(self) -> str:
        """Restituisce il testo di aiuto sui comandi disponibili."""
        return """
╔════════════════════════════════════════════════════════════════╗
║                     COMANDI DISPONIBILI                        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  MOVIMENTO:                                                    ║
║    vai <direzione>  - Vai nord, sud, est, ovest, su, giù      ║
║    nord, n          - Vai a nord (anche s, e, o)              ║
║                                                                ║
║  OSSERVAZIONE:                                                 ║
║    guarda           - Guarda la stanza corrente               ║
║    osserva <cosa>   - Esamina un oggetto o persona            ║
║                                                                ║
║  OGGETTI:                                                      ║
║    prendi <oggetto> - Prendi un oggetto                       ║
║    lascia <oggetto> - Lascia un oggetto                       ║
║    usa <oggetto>    - Usa un oggetto                          ║
║    usa <X> con <Y>  - Combina due oggetti                     ║
║    inventario       - Mostra gli oggetti che hai              ║
║                                                                ║
║  INTERAZIONE:                                                  ║
║    parla <persona>  - Parla con qualcuno                      ║
║    apri <cosa>      - Apri qualcosa                           ║
║    tocca <cosa>     - Tocca qualcosa                          ║
║                                                                ║
║  ALTRO:                                                        ║
║    aiuto            - Mostra questo messaggio                 ║
║    esci             - Esci dal gioco                          ║
║                                                                ║
║  SUGGERIMENTO: Puoi scrivere comandi in linguaggio naturale! ║
║  Esempio: "prendi la chiave arrugginita dalla scrivania"     ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""


# ============================================================================
# CLASSE ITEM (OGGETTO)
# ============================================================================

class Item:
    """
    Rappresenta un oggetto nel gioco.
    Supporta azioni multiple e comportamenti personalizzati.
    """

    def __init__(
        self,
        name: str,
        description: str,
        can_take: bool = True,
        visible: bool = True,
        aliases: Optional[List[str]] = None,
        **properties
    ):
        """
        Inizializza un oggetto.

        Args:
            name: Nome dell'oggetto (identificatore)
            description: Descrizione quando viene osservato
            can_take: Se può essere preso
            visible: Se è visibile nella stanza
            aliases: Nomi alternativi per l'oggetto
            **properties: Proprietà custom (es. is_container, is_locked, ecc.)
        """
        self.name = name.lower()
        self.description = description
        self.can_take = can_take
        self.visible = visible
        self.aliases = [a.lower() for a in (aliases or [])]
        self.properties = properties

        # Azioni custom definibili dallo studente
        self.actions: Dict[str, Callable] = {}

    def matches(self, word: str) -> bool:
        """Verifica se una parola corrisponde a questo oggetto."""
        word = word.lower()
        if word == self.name:
            return True
        if word in self.aliases:
            return True
        # Match parziale
        if word in self.name or self.name in word:
            return True
        return False

    def add_action(self, verb: str, callback: Callable):
        """
        Aggiunge un'azione custom all'oggetto.

        Args:
            verb: Il verbo che attiva l'azione (es. 'apri', 'leggi')
            callback: Funzione da chiamare. Riceve (game, item) come parametri
        """
        self.actions[verb.lower()] = callback

    def perform_action(self, verb: str, game: 'Game') -> Optional[str]:
        """
        Esegue un'azione sull'oggetto.

        Returns:
            Messaggio di risultato, o None se l'azione non esiste
        """
        if verb in self.actions:
            return self.actions[verb](game, self)
        return None

    def get_property(self, prop: str, default: Any = None) -> Any:
        """Ottiene una proprietà custom."""
        return self.properties.get(prop, default)

    def set_property(self, prop: str, value: Any):
        """Imposta una proprietà custom."""
        self.properties[prop] = value

    def __str__(self):
        return self.name


# ============================================================================
# CLASSE NPC (PERSONAGGIO NON GIOCANTE)
# ============================================================================

class NPC:
    """
    Rappresenta un personaggio non giocante.
    Supporta dialoghi, stati e comportamenti.
    """

    def __init__(
        self,
        name: str,
        description: str,
        dialogue: Optional[Dict[str, str]] = None,
        aliases: Optional[List[str]] = None,
        **properties
    ):
        """
        Inizializza un NPC.

        Args:
            name: Nome del personaggio
            description: Descrizione quando viene osservato
            dialogue: Dizionario di dialoghi {chiave: testo}
            aliases: Nomi alternativi
            **properties: Proprietà custom (es. mood, knows_player, ecc.)
        """
        self.name = name.lower()
        self.description = description
        self.dialogue = dialogue or {'default': f'{name} non ha nulla da dire.'}
        self.aliases = [a.lower() for a in (aliases or [])]
        self.properties = properties

        # Stato corrente dialogo
        self.dialogue_state = 'default'

        # Callback per eventi
        self.on_talk: Optional[Callable] = None

    def matches(self, word: str) -> bool:
        """Verifica se una parola corrisponde a questo NPC."""
        word = word.lower()
        if word == self.name:
            return True
        if word in self.aliases:
            return True
        if word in self.name or self.name in word:
            return True
        return False

    def talk(self, game: 'Game') -> str:
        """
        Parla con l'NPC.

        Returns:
            Il dialogo corrente
        """
        # Callback personalizzato
        if self.on_talk:
            self.on_talk(game, self)

        # Restituisce il dialogo dello stato corrente
        return self.dialogue.get(self.dialogue_state, self.dialogue.get('default', 'Non ha nulla da dire.'))

    def set_dialogue_state(self, state: str):
        """Cambia lo stato del dialogo."""
        self.dialogue_state = state

    def get_property(self, prop: str, default: Any = None) -> Any:
        """Ottiene una proprietà custom."""
        return self.properties.get(prop, default)

    def set_property(self, prop: str, value: Any):
        """Imposta una proprietà custom."""
        self.properties[prop] = value

    def __str__(self):
        return self.name


# ============================================================================
# CLASSE ROOM (STANZA)
# ============================================================================

class Room:
    """
    Rappresenta una location/stanza nel gioco.
    """

    def __init__(
        self,
        name: str,
        description: str,
        short_desc: Optional[str] = None,
        **properties
    ):
        """
        Inizializza una stanza.

        Args:
            name: Nome identificativo della stanza
            description: Descrizione dettagliata
            short_desc: Descrizione breve (usata quando ritorni)
            **properties: Proprietà custom (es. is_dark, is_locked, ecc.)
        """
        self.name = name
        self.description = description
        self.short_desc = short_desc or name
        self.properties = properties

        # Collegamenti ad altre stanze
        self.exits: Dict[str, str] = {}  # {direzione: nome_stanza}

        # Oggetti nella stanza
        self.items: List[Item] = []

        # NPC nella stanza
        self.npcs: List[NPC] = []

        # Flag per sapere se è la prima visita
        self.visited = False

        # Callback per eventi
        self.on_enter: Optional[Callable] = None
        self.on_exit: Optional[Callable] = None

    def add_exit(self, direction: str, room_name: str):
        """Aggiunge un'uscita verso un'altra stanza."""
        self.exits[direction.lower()] = room_name

    def get_exit(self, direction: str) -> Optional[str]:
        """Ottiene il nome della stanza in una direzione."""
        return self.exits.get(direction.lower())

    def add_item(self, item: Item):
        """Aggiunge un oggetto alla stanza."""
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item: Item):
        """Rimuove un oggetto dalla stanza."""
        if item in self.items:
            self.items.remove(item)

    def find_item(self, name: str) -> Optional[Item]:
        """Cerca un oggetto per nome nella stanza."""
        name = name.lower()
        for item in self.items:
            if item.visible and item.matches(name):
                return item
        return None

    def add_npc(self, npc: NPC):
        """Aggiunge un NPC alla stanza."""
        if npc not in self.npcs:
            self.npcs.append(npc)

    def remove_npc(self, npc: NPC):
        """Rimuove un NPC dalla stanza."""
        if npc in self.npcs:
            self.npcs.remove(npc)

    def find_npc(self, name: str) -> Optional[NPC]:
        """Cerca un NPC per nome nella stanza."""
        name = name.lower()
        for npc in self.npcs:
            if npc.matches(name):
                return npc
        return None

    def get_full_description(self) -> str:
        """Restituisce la descrizione completa della stanza con oggetti e NPC."""
        desc = self.description if not self.visited else self.short_desc

        # Aggiunge oggetti visibili
        visible_items = [i for i in self.items if i.visible]
        if visible_items:
            desc += "\n\n🔍 Vedi: " + ", ".join([i.name for i in visible_items]) + "."

        # Aggiunge NPC
        if self.npcs:
            desc += "\n\n👤 Qui c'è: " + ", ".join([n.name for n in self.npcs]) + "."

        # Aggiunge uscite
        if self.exits:
            exits_str = ", ".join(self.exits.keys())
            desc += f"\n\n🚪 Uscite: {exits_str}."

        return desc

    def get_property(self, prop: str, default: Any = None) -> Any:
        """Ottiene una proprietà custom."""
        return self.properties.get(prop, default)

    def set_property(self, prop: str, value: Any):
        """Imposta una proprietà custom."""
        self.properties[prop] = value


# ============================================================================
# CLASSE GAME (GIOCO PRINCIPALE)
# ============================================================================

class Game:
    """
    Classe principale che gestisce il gioco.
    """

    def __init__(self, title: str, author: str, intro: str):
        """
        Inizializza il gioco.

        Args:
            title: Titolo del gioco
            author: Autore/i
            intro: Testo introduttivo
        """
        self.title = title
        self.author = author
        self.intro = intro

        # Stanze del gioco
        self.rooms: Dict[str, Room] = {}

        # Stanza corrente
        self.current_room: Optional[Room] = None

        # Inventario del giocatore
        self.inventory: List[Item] = []

        # Parser
        self.parser = Parser()

        # Flag di gioco
        self.running = False
        self.game_over = False
        self.game_won = False

        # Variabili di stato globali (per eventi, flag, ecc.)
        self.state: Dict[str, Any] = {}

        # Contatore turni
        self.turn_count = 0

    def add_room(self, key: str, room: Room):
        """Aggiunge una stanza al gioco."""
        self.rooms[key] = room

    def get_room(self, key: str) -> Optional[Room]:
        """Ottiene una stanza per chiave."""
        return self.rooms.get(key)

    def set_start(self, room_key: str):
        """Imposta la stanza di partenza."""
        self.current_room = self.rooms.get(room_key)

    def connect_rooms(self, from_room: str, direction: str, to_room: str, bidirectional: bool = False):
        """
        Connette due stanze.

        Args:
            from_room: Chiave della stanza di partenza
            direction: Direzione (nord, sud, est, ovest, su, giù)
            to_room: Chiave della stanza di destinazione
            bidirectional: Se True, crea anche il collegamento inverso
        """
        room = self.get_room(from_room)
        if room:
            room.add_exit(direction, to_room)

        if bidirectional:
            # Direzioni opposte
            opposites = {
                'nord': 'sud', 'sud': 'nord',
                'est': 'ovest', 'ovest': 'est',
                'su': 'giù', 'giù': 'su',
                'n': 's', 's': 'n',
                'e': 'o', 'o': 'e'
            }
            opposite_dir = opposites.get(direction.lower())
            if opposite_dir:
                dest_room = self.get_room(to_room)
                if dest_room:
                    dest_room.add_exit(opposite_dir, from_room)

    def find_item_in_inventory(self, name: str) -> Optional[Item]:
        """Cerca un oggetto nell'inventario."""
        name = name.lower()
        for item in self.inventory:
            if item.matches(name):
                return item
        return None

    def print_wrapped(self, text: str, width: int = 70):
        """Stampa testo con word wrapping."""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            word_length = len(word)
            if current_length + word_length + len(current_line) <= width:
                current_line.append(word)
                current_length += word_length
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = word_length

        if current_line:
            lines.append(' '.join(current_line))

        print('\n'.join(lines))

    def display_intro(self):
        """Mostra l'introduzione del gioco."""
        print("\n" + "=" * 70)
        print(f"{self.title.upper()}")
        print(f"di {self.author}")
        print("=" * 70)
        print()
        self.print_wrapped(self.intro)
        print("\n" + "-" * 70)
        print("Scrivi 'aiuto' per la lista dei comandi.")
        print("-" * 70 + "\n")

    # ========================================================================
    # COMANDI
    # ========================================================================

    def cmd_look(self, parsed: Dict) -> str:
        """Guarda la stanza corrente."""
        if self.current_room:
            return self.current_room.get_full_description()
        return "Non sei da nessuna parte!"

    def cmd_go(self, parsed: Dict) -> str:
        """Vai in una direzione."""
        direction = parsed.get('target')
        if not direction:
            return "Dove vuoi andare?"

        # Normalizza direzione
        direction = direction.lower()
        if direction in ['n']: direction = 'nord'
        elif direction in ['s']: direction = 'sud'
        elif direction in ['e']: direction = 'est'
        elif direction in ['o']: direction = 'ovest'

        if not self.current_room:
            return "Non sei in nessuna stanza!"

        next_room_key = self.current_room.get_exit(direction)
        if not next_room_key:
            return f"Non puoi andare verso {direction}."

        next_room = self.get_room(next_room_key)
        if not next_room:
            return f"Errore: la stanza '{next_room_key}' non esiste!"

        # Callback on_exit
        if self.current_room.on_exit:
            self.current_room.on_exit(self, self.current_room)

        # Cambia stanza
        self.current_room = next_room

        # Callback on_enter
        if self.current_room.on_enter:
            self.current_room.on_enter(self, self.current_room)

        # Mostra descrizione
        description = self.current_room.get_full_description()
        self.current_room.visited = True

        return f"Vai verso {direction}.\n\n{description}"

    def cmd_take(self, parsed: Dict) -> str:
        """Prendi un oggetto."""
        target = parsed.get('target')
        if not target:
            return "Cosa vuoi prendere?"

        if not self.current_room:
            return "Non sei in nessuna stanza!"

        item = self.current_room.find_item(target)
        if not item:
            return f"Non vedo nessun '{target}' qui."

        if not item.can_take:
            return f"Non puoi prendere {item.name}."

        self.current_room.remove_item(item)
        self.inventory.append(item)
        return f"Hai preso {item.name}."

    def cmd_drop(self, parsed: Dict) -> str:
        """Lascia un oggetto."""
        target = parsed.get('target')
        if not target:
            return "Cosa vuoi lasciare?"

        item = self.find_item_in_inventory(target)
        if not item:
            return f"Non hai nessun '{target}'."

        self.inventory.remove(item)
        if self.current_room:
            self.current_room.add_item(item)
        return f"Hai lasciato {item.name}."

    def cmd_examine(self, parsed: Dict) -> str:
        """Esamina un oggetto o NPC."""
        target = parsed.get('target')
        if not target:
            # Se non c'è target, guarda la stanza
            return self.cmd_look(parsed)

        # Cerca nell'inventario
        item = self.find_item_in_inventory(target)
        if item:
            return item.description

        # Cerca nella stanza
        if self.current_room:
            item = self.current_room.find_item(target)
            if item:
                return item.description

            # Cerca NPC
            npc = self.current_room.find_npc(target)
            if npc:
                return npc.description

        return f"Non vedo nessun '{target}'."

    def cmd_use(self, parsed: Dict) -> str:
        """Usa un oggetto."""
        target = parsed.get('target')
        secondary = parsed.get('secondary')

        if not target:
            return "Cosa vuoi usare?"

        # Trova l'oggetto
        item = self.find_item_in_inventory(target)
        if not item:
            if self.current_room:
                item = self.current_room.find_item(target)

        if not item:
            return f"Non hai nessun '{target}'."

        # Se c'è un oggetto secondario (combina)
        if secondary:
            item2 = self.find_item_in_inventory(secondary)
            if not item2 and self.current_room:
                item2 = self.current_room.find_item(secondary)

            if not item2:
                return f"Non vedo nessun '{secondary}'."

            # Prova azione combina su entrambi
            result = item.perform_action('combina', self)
            if result:
                return result
            result = item2.perform_action('combina', self)
            if result:
                return result

            return f"Non puoi usare {item.name} con {item2.name}."

        # Usa singolo oggetto
        result = item.perform_action('usa', self)
        if result:
            return result

        return f"Non sai come usare {item.name}."

    def cmd_talk(self, parsed: Dict) -> str:
        """Parla con un NPC."""
        target = parsed.get('target')
        if not target:
            return "Con chi vuoi parlare?"

        if not self.current_room:
            return "Non c'è nessuno qui."

        npc = self.current_room.find_npc(target)
        if not npc:
            return f"Non vedo nessun '{target}' qui."

        return f"{npc.name.capitalize()}: \"{npc.talk(self)}\""

    def cmd_inventory(self, parsed: Dict) -> str:
        """Mostra l'inventario."""
        if not self.inventory:
            return "Non hai nulla con te."

        items_list = ", ".join([item.name for item in self.inventory])
        return f"🎒 Inventario: {items_list}."

    def cmd_help(self, parsed: Dict) -> str:
        """Mostra l'aiuto."""
        return self.parser.get_help()

    # Comandi aggiuntivi per azioni comuni
    def cmd_open(self, parsed: Dict) -> str:
        """Apri qualcosa."""
        target = parsed.get('target')
        if not target:
            return "Cosa vuoi aprire?"

        # Cerca oggetto
        item = self.find_item_in_inventory(target)
        if not item and self.current_room:
            item = self.current_room.find_item(target)

        if not item:
            return f"Non vedo nessun '{target}'."

        result = item.perform_action('apri', self)
        if result:
            return result

        return f"Non puoi aprire {item.name}."

    def cmd_close(self, parsed: Dict) -> str:
        """Chiudi qualcosa."""
        target = parsed.get('target')
        if not target:
            return "Cosa vuoi chiudere?"

        item = self.find_item_in_inventory(target)
        if not item and self.current_room:
            item = self.current_room.find_item(target)

        if not item:
            return f"Non vedo nessun '{target}'."

        result = item.perform_action('chiudi', self)
        if result:
            return result

        return f"Non puoi chiudere {item.name}."

    def cmd_touch(self, parsed: Dict) -> str:
        """Tocca qualcosa."""
        target = parsed.get('target')
        if not target:
            return "Cosa vuoi toccare?"

        item = self.find_item_in_inventory(target)
        if not item and self.current_room:
            item = self.current_room.find_item(target)

        if not item:
            return f"Non vedo nessun '{target}'."

        result = item.perform_action('tocca', self)
        if result:
            return result

        return f"Tocchi {item.name}. Non succede nulla di particolare."

    def cmd_push(self, parsed: Dict) -> str:
        """Spingi qualcosa."""
        target = parsed.get('target')
        if not target:
            return "Cosa vuoi spingere?"

        item = self.find_item_in_inventory(target)
        if not item and self.current_room:
            item = self.current_room.find_item(target)

        if not item:
            return f"Non vedo nessun '{target}'."

        result = item.perform_action('spingi', self)
        if result:
            return result

        return f"Spingi {item.name}. Non succede nulla."

    def cmd_pull(self, parsed: Dict) -> str:
        """Tira qualcosa."""
        target = parsed.get('target')
        if not target:
            return "Cosa vuoi tirare?"

        item = self.find_item_in_inventory(target)
        if not item and self.current_room:
            item = self.current_room.find_item(target)

        if not item:
            return f"Non vedo nessun '{target}'."

        result = item.perform_action('tira', self)
        if result:
            return result

        return f"Tiri {item.name}. Non succede nulla."

    # ========================================================================
    # GAME LOOP
    # ========================================================================

    def process_command(self, command: str) -> Optional[str]:
        """
        Processa un comando del giocatore.

        Returns:
            Messaggio di risposta, o None se deve uscire
        """
        # Parse del comando
        parsed = self.parser.parse(command)
        verb = parsed.get('verb')

        if not verb:
            return "Non ho capito. Scrivi 'aiuto' per la lista dei comandi."

        # Mappa verbi -> comandi
        command_map = {
            'vai': self.cmd_go,
            'prendi': self.cmd_take,
            'lascia': self.cmd_drop,
            'osserva': self.cmd_examine,
            'guarda': self.cmd_look,
            'usa': self.cmd_use,
            'parla': self.cmd_talk,
            'inventario': self.cmd_inventory,
            'aiuto': self.cmd_help,
            'apri': self.cmd_open,
            'chiudi': self.cmd_close,
            'tocca': self.cmd_touch,
            'spingi': self.cmd_push,
            'tira': self.cmd_pull,
            'esci': lambda p: None,  # Esce dal gioco
        }

        # Esegue il comando
        cmd_func = command_map.get(verb)
        if cmd_func:
            result = cmd_func(parsed)
            self.turn_count += 1
            return result

        return f"Non so come '{verb}'. Scrivi 'aiuto' per i comandi disponibili."

    def start(self):
        """Avvia il game loop."""
        self.running = True
        self.display_intro()

        # Mostra la stanza iniziale
        if self.current_room:
            print(self.current_room.get_full_description())
            self.current_room.visited = True
            print()

        # Game loop
        while self.running and not self.game_over:
            try:
                command = input("> ").strip()
                if not command:
                    continue

                print()  # Linea vuota per separazione

                result = self.process_command(command)

                if result is None:
                    # Comando esci
                    print("\nGrazie per aver giocato!")
                    self.running = False
                else:
                    self.print_wrapped(result)
                    print()

                # Controlla condizioni di vittoria/sconfitta
                if self.game_won:
                    print("\n" + "=" * 70)
                    print("🎉 HAI VINTO! 🎉")
                    print("=" * 70)
                    self.running = False
                elif self.game_over:
                    print("\n" + "=" * 70)
                    print("💀 GAME OVER 💀")
                    print("=" * 70)
                    self.running = False

            except KeyboardInterrupt:
                print("\n\nGioco interrotto.")
                self.running = False
            except Exception as e:
                print(f"\n❌ Errore: {e}")
                import traceback
                traceback.print_exc()


# ============================================================================
# FUNZIONI HELPER
# ============================================================================

def create_simple_item(name: str, desc: str, can_take: bool = True) -> Item:
    """Helper per creare rapidamente un oggetto semplice."""
    return Item(name=name, description=desc, can_take=can_take)


def create_simple_npc(name: str, desc: str, dialogue: str) -> NPC:
    """Helper per creare rapidamente un NPC semplice."""
    return NPC(name=name, description=desc, dialogue={'default': dialogue})


# ============================================================================
# FINE MODULO
# ============================================================================

if __name__ == "__main__":
    print("Questo è il motore per avventure testuali.")
    print("Importalo nel tuo progetto per creare la tua avventura!")
    print("\nEsempio:")
    print("  from text_adventure_engine import Game, Room, Item, NPC")
