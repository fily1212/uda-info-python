# Es7: Editor di Storie Interattive

## Obiettivi
- **Italiano**: Progettazione narrativa, struttura di una storia
- **Informatica**: GUI programming, JSON, graph data structures

## Descrizione

Crea un **tool visuale** per scrivere storie interattive senza programmare! I tuoi compagni potranno creare le loro avventure con un'interfaccia grafica e condividerle.

## Perché un Editor?

### Senza Editor:
```python
# Devi programmare ogni scena...
scena1 = Scena("Ti svegli...", [
    Scelta("Vai a sinistra", scena2),
    Scelta("Vai a destra", scena3)
])
# ... tante righe di codice ...
```

### Con Editor:
```
[GUI]
┌────────────────────┐
│ Nuova Scena       │
│                   │
│ Testo: [_______]  │
│ Scelta 1: [____]  │
│ → Scena: [____]   │
│                   │
│ [Salva]  [Test]   │
└────────────────────┘
```

**Chiunque può creare storie!** ✨

## Architettura del Progetto

### 3 Componenti Principali

```
┌─────────────────┐
│  1. EDITOR      │ → Crea/modifica storie (GUI)
│  (Tkinter/PyQt) │
└────────┬────────┘
         │
         ↓ salva
┌─────────────────┐
│  2. FILE JSON   │ → Formato dati
│  storia.json    │
└────────┬────────┘
         │
         ↓ carica
┌─────────────────┐
│  3. PLAYER      │ → Gioca le storie
│  (Console/GUI)  │
└─────────────────┘
```

## Formato Dati: JSON

### Struttura Base
```json
{
  "titolo": "La Foresta Incantata",
  "autore": "Mario Rossi",
  "descrizione": "Un'avventura fantasy...",
  "scena_iniziale": "inizio",
  "scene": {
    "inizio": {
      "testo": "Ti svegli in una foresta misteriosa. Cosa fai?",
      "scelte": [
        {
          "testo": "Segui il sentiero a sinistra",
          "prossima_scena": "sentiero_sinistro"
        },
        {
          "testo": "Segui il sentiero a destra",
          "prossima_scena": "sentiero_destro"
        }
      ]
    },
    "sentiero_sinistro": {
      "testo": "Trovi un lago cristallino...",
      "scelte": [...]
    }
  }
}
```

### Con Features Avanzate
```json
{
  "scene": {
    "incontro_mago": {
      "testo": "Un mago ti blocca il cammino...",
      "immagine": "mago.png",
      "musica": "tema_mago.mp3",
      "condizione": "ha_chiave",  // Richiede oggetto
      "scelte": [
        {
          "testo": "Dagli la chiave magica",
          "prossima_scena": "mago_felice",
          "rimuovi_oggetto": "chiave_magica",
          "aggiungi_oggetto": "bacchetta"
        }
      ],
      "tipo": "finale",  // È una scena finale
      "finale_tipo": "buono"
    }
  },
  "inventario_iniziale": ["torcia", "mappa"],
  "variabili": {
    "karma": 0,
    "vita": 100
  }
}
```

## Implementazione Editor

### 1. GUI con Tkinter (Semplice)

```python
import tkinter as tk
from tkinter import ttk, messagebox
import json

class EditorStorie:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Editor Storie Interattive")
        self.root.geometry("900x700")

        self.storia = {
            "titolo": "",
            "scene": {}
        }

        self.scena_corrente = None
        self.crea_interfaccia()

    def crea_interfaccia(self):
        # Frame sinistro: Lista scene
        frame_sinistra = tk.Frame(self.root, width=250, bg="lightgray")
        frame_sinistra.pack(side=tk.LEFT, fill=tk.BOTH)

        tk.Label(frame_sinistra, text="SCENE", font=("Arial", 14, "bold")).pack()

        # Lista scene
        self.lista_scene = tk.Listbox(frame_sinistra)
        self.lista_scene.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.lista_scene.bind('<<ListboxSelect>>', self.on_scena_selezionata)

        # Bottoni
        tk.Button(frame_sinistra, text="+ Nuova Scena",
                 command=self.nuova_scena).pack(fill=tk.X, padx=5)
        tk.Button(frame_sinistra, text="🗑️ Elimina",
                 command=self.elimina_scena).pack(fill=tk.X, padx=5)

        # Frame destro: Editor scena
        frame_destra = tk.Frame(self.root)
        frame_destra.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Titolo storia
        tk.Label(frame_destra, text="Titolo Storia:").pack()
        self.entry_titolo = tk.Entry(frame_destra, font=("Arial", 14))
        self.entry_titolo.pack(fill=tk.X, padx=10)

        # ID Scena
        tk.Label(frame_destra, text="ID Scena:").pack()
        self.entry_id_scena = tk.Entry(frame_destra)
        self.entry_id_scena.pack(fill=tk.X, padx=10)

        # Testo scena
        tk.Label(frame_destra, text="Testo Scena:").pack()
        self.text_scena = tk.Text(frame_destra, height=6)
        self.text_scena.pack(fill=tk.X, padx=10)

        # Scelte
        tk.Label(frame_destra, text="SCELTE:", font=("Arial", 12, "bold")).pack()

        self.frame_scelte = tk.Frame(frame_destra)
        self.frame_scelte.pack(fill=tk.BOTH, expand=True)

        tk.Button(frame_destra, text="+ Aggiungi Scelta",
                 command=self.aggiungi_scelta).pack()

        # Bottoni finali
        frame_bottoni = tk.Frame(frame_destra)
        frame_bottoni.pack(side=tk.BOTTOM, fill=tk.X)

        tk.Button(frame_bottoni, text="💾 Salva", bg="green", fg="white",
                 command=self.salva_storia).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(frame_bottoni, text="📂 Carica", bg="blue", fg="white",
                 command=self.carica_storia).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(frame_bottoni, text="▶️ Testa", bg="orange", fg="white",
                 command=self.testa_storia).pack(side=tk.LEFT, expand=True, fill=tk.X)

    def nuova_scena(self):
        """Crea una nuova scena"""
        id_scena = f"scena_{len(self.storia['scene']) + 1}"
        self.storia['scene'][id_scena] = {
            "testo": "",
            "scelte": []
        }
        self.aggiorna_lista_scene()
        self.lista_scene.selection_set(len(self.storia['scene']) - 1)

    def aggiungi_scelta(self):
        """Aggiungi una nuova scelta alla scena corrente"""
        frame_scelta = tk.Frame(self.frame_scelte, relief=tk.RIDGE, borderwidth=2)
        frame_scelta.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(frame_scelta, text="Testo:").pack(side=tk.LEFT)
        entry_testo = tk.Entry(frame_scelta, width=30)
        entry_testo.pack(side=tk.LEFT, padx=5)

        tk.Label(frame_scelta, text="→").pack(side=tk.LEFT)

        # Dropdown scene
        combo_scene = ttk.Combobox(frame_scelta, values=list(self.storia['scene'].keys()))
        combo_scene.pack(side=tk.LEFT, padx=5)

        tk.Button(frame_scelta, text="❌", command=frame_scelta.destroy).pack(side=tk.RIGHT)

    def salva_storia(self):
        """Salva la storia in JSON"""
        filename = tk.filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
        if filename:
            self.storia['titolo'] = self.entry_titolo.get()
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.storia, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Successo", "Storia salvata!")

    def run(self):
        self.root.mainloop()
```

### 2. Player per Testare

```python
import json

class StoryPlayer:
    def __init__(self, file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            self.storia = json.load(f)

        self.scena_corrente = self.storia.get('scena_iniziale', 'inizio')
        self.inventario = []

    def gioca(self):
        """Loop principale"""
        print(f"\n{'='*60}")
        print(f"  {self.storia['titolo']}")
        print(f"{'='*60}\n")

        while True:
            if self.scena_corrente not in self.storia['scene']:
                print("❌ Scena non trovata!")
                break

            scena = self.storia['scene'][self.scena_corrente]

            # Mostra testo scena
            print(f"\n{scena['testo']}\n")

            # È una scena finale?
            if scena.get('tipo') == 'finale':
                print(f"\n{'='*60}")
                print(f"  FINE")
                print(f"{'='*60}")
                break

            # Mostra scelte
            scelte = scena.get('scelte', [])
            if not scelte:
                print("Fine della storia!")
                break

            for i, scelta in enumerate(scelte, 1):
                print(f"{i}. {scelta['testo']}")

            # Input giocatore
            while True:
                try:
                    scelta_num = int(input("\n> ")) - 1
                    if 0 <= scelta_num < len(scelte):
                        self.scena_corrente = scelte[scelta_num]['prossima_scena']
                        break
                    else:
                        print("❌ Scelta non valida!")
                except ValueError:
                    print("❌ Inserisci un numero!")

# Uso
if __name__ == "__main__":
    player = StoryPlayer("la_mia_storia.json")
    player.gioca()
```

## Esercizio per Gli Studenti

### Parte 1: Editor Base
Implementa un editor che permetta di:
- [ ] Creare nuove scene con ID e testo
- [ ] Aggiungere scelte con destinazioni
- [ ] Salvare in JSON
- [ ] Caricare JSON esistente
- [ ] Lista scene nella sidebar

### Parte 2: Player
Implementa un player che:
- [ ] Carica file JSON
- [ ] Mostra scene e scelte
- [ ] Gestisce navigazione
- [ ] Riconosce scene finali

### Parte 3: Features Avanzate
Aggiungi almeno 2 di:
- [ ] **Validazione**: Controlla che tutte le scene esistano
- [ ] **Grafo visuale**: Mostra mappa delle scene
- [ ] **Inventario**: Oggetti raccoglibili/utilizzabili
- [ ] **Condizioni**: Scene accessibili solo con oggetti
- [ ] **Variabili**: Karma, vita, ecc.
- [ ] **Immagini**: Associa immagini alle scene
- [ ] **Anteprima**: Testa direttamente dall'editor
- [ ] **Export HTML**: Genera una pagina web giocabile

## Esempio: Grafo Visuale

```python
import networkx as nx
import matplotlib.pyplot as plt

def visualizza_grafo(storia):
    """Crea un grafo delle scene"""
    G = nx.DiGraph()

    # Aggiungi nodi
    for scena_id in storia['scene']:
        G.add_node(scena_id)

    # Aggiungi archi (scelte)
    for scena_id, scena in storia['scene'].items():
        for scelta in scena.get('scelte', []):
            if 'prossima_scena' in scelta:
                G.add_edge(scena_id, scelta['prossima_scena'],
                          label=scelta['testo'][:20])

    # Disegna
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=3000, font_size=10, arrows=True)
    plt.show()
```

## Esempio: Export HTML

```python
def export_html(storia, output_file):
    """Esporta storia come HTML giocabile"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{titolo}</title>
        <style>
            body {{ font-family: Arial; max-width: 600px; margin: 50px auto; }}
            #testo {{ font-size: 18px; margin: 20px 0; }}
            button {{ padding: 10px 20px; margin: 5px; font-size: 16px; }}
        </style>
    </head>
    <body>
        <h1 id="titolo">{titolo}</h1>
        <div id="testo"></div>
        <div id="scelte"></div>

        <script>
        const storia = {storia_json};
        let scenaCorrente = '{scena_iniziale}';

        function mostraScena() {{
            const scena = storia.scene[scenaCorrente];
            document.getElementById('testo').innerHTML = scena.testo;

            const divScelte = document.getElementById('scelte');
            divScelte.innerHTML = '';

            scena.scelte.forEach(scelta => {{
                const btn = document.createElement('button');
                btn.textContent = scelta.testo;
                btn.onclick = () => {{
                    scenaCorrente = scelta.prossima_scena;
                    mostraScena();
                }};
                divScelte.appendChild(btn);
                divScelte.appendChild(document.createElement('br'));
            }});
        }}

        mostraScena();
        </script>
    </body>
    </html>
    """.format(
        titolo=storia['titolo'],
        storia_json=json.dumps(storia),
        scena_iniziale=storia.get('scena_iniziale', 'inizio')
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
```

## Validazione Storia

```python
def valida_storia(storia):
    """Controlla se la storia è valida"""
    errori = []

    # Controlla che esista scena iniziale
    scena_iniz = storia.get('scena_iniziale', 'inizio')
    if scena_iniz not in storia['scene']:
        errori.append(f"❌ Scena iniziale '{scena_iniz}' non esiste!")

    # Controlla che tutte le scelte puntino a scene esistenti
    for scena_id, scena in storia['scene'].items():
        for scelta in scena.get('scelte', []):
            dest = scelta.get('prossima_scena')
            if dest and dest not in storia['scene']:
                errori.append(f"❌ Scena '{scena_id}' ha scelta verso '{dest}' inesistente!")

    # Controlla scene irraggiungibili
    raggiungibili = set()

    def trova_raggiungibili(scena_id):
        if scena_id in raggiungibili:
            return
        raggiungibili.add(scena_id)
        for scelta in storia['scene'][scena_id].get('scelte', []):
            if 'prossima_scena' in scelta:
                trova_raggiungibili(scelta['prossima_scena'])

    trova_raggiungibili(scena_iniz)

    irraggiungibili = set(storia['scene'].keys()) - raggiungibili
    if irraggiungibili:
        errori.append(f"⚠️ Scene irraggiungibili: {irraggiungibili}")

    return errori
```

## Struttura Completa Progetto

```
editor-storie/
│
├── editor.py           # GUI editor
├── player.py           # Player console
├── validatore.py       # Validazione storie
├── esportatore.py      # Export HTML
│
├── gui/
│   ├── finestra_principale.py
│   ├── editor_scena.py
│   └── visualizzatore_grafo.py
│
├── esempi/
│   ├── foresta_incantata.json
│   ├── mistero_castello.json
│   └── viaggio_spaziale.json
│
└── storie_create/
    └── (storie degli studenti)
```

## Valutazione

| Aspetto | Peso |
|---------|------|
| Funzionalità editor base | 30% |
| Player funzionante | 20% |
| Interfaccia intuitiva | 20% |
| Features avanzate | 20% |
| Creatività/originalità | 10% |

## Librerie GUI Alternative

### Tkinter (Standard)
```python
import tkinter as tk
# Pro: Incluso in Python, semplice
# Contro: Grafica basic
```

### PyQt5 (Professionale)
```python
from PyQt5.QtWidgets import QApplication, QMainWindow
# Pro: Bellissimo, potente
# Contro: Più complesso
```

### Kivy (Mobile)
```python
from kivy.app import App
# Pro: Funziona su Android/iOS
# Contro: Sintassi particolare
```

**Dai il potere di creare storie a tutti! 📝✨**
