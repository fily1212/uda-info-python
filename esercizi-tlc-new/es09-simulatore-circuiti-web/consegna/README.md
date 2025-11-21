# ES09 - Simulatore di Circuiti Web 💻

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐⭐⭐ AVANZATO |
| **Durata Stimata** | 6-7 ore |
| **Linguaggio** | JavaScript (ES6+) / HTML5 / CSS3 |
| **Prerequisiti** | ES06-ES08 completati, HTML/CSS/JS base |
| **Argomento TLC** | Applicazione Web: Simulazione Circuiti Interattivi |

---

## 🎓 Concetti Fondamentali

### Applicazione Web Interattiva 🌐

Un'**applicazione web interattiva** consente all'utente di:
- Disegnare circuiti graficamente
- Simulare il comportamento in tempo reale
- Visualizzare tensioni e correnti
- Salvare/caricare configurazioni

```
Architettura Web:
┌─────────────────────────────────────────────────┐
│                    BROWSER                      │
├─────────────────────────────────────────────────┤
│  HTML: Struttura (canvas, button, input)       │
│  CSS: Stile e layout (responsive grid)         │
│  JavaScript: Logica (disegno, simulazione)     │
└─────────────────────────────────────────────────┘
```

### Componenti Circuito 🔌

```
1. RESISTORI (R)
   - Oppose current flow
   - V = I × R (Ohm's law)
   - Rappresentazione: /\/\/\ oppure ⟶[R]⟶

2. CONDENSATORI (C)
   - Immagazzina energia
   - I = C × dV/dt

3. INDUTTORI (L)
   - Resiste cambiamenti di corrente
   - V = L × dI/dt

4. BATTERIE (B)
   - Fornisce tensione
   - Polarità: + e -

5. INTERRUTTORI (S)
   - Apre/chiude circuito
   - Stato: ON/OFF

6. LED
   - Emette luce quando acceso
   - Accende se V > 2V tipicamente

7. FILO (Wire)
   - Connette componenti
   - Resistenza ≈ 0Ω
```

### Canvas HTML5 🎨

L'**HTML5 Canvas** è una superficie di disegno JavaScript:

```javascript
// Creare canvas
<canvas id="circuit-canvas" width="800" height="600"></canvas>

// Accedere in JavaScript
const canvas = document.getElementById('circuit-canvas');
const ctx = canvas.getContext('2d');

// Disegnare
ctx.fillStyle = '#FF0000';
ctx.fillRect(10, 10, 100, 50);  // Rettangolo rosso
ctx.strokeStyle = '#000000';
ctx.beginPath();
ctx.arc(50, 50, 30, 0, 2*Math.PI);  // Cerchio
ctx.stroke();
```

### Drag & Drop ➡️

Permettere all'utente di trascinare componenti:

```javascript
// Eventi mouse
canvas.addEventListener('mousedown', startDrag);
canvas.addEventListener('mousemove', drag);
canvas.addEventListener('mouseup', endDrag);

function startDrag(event) {
    // Rileva quale componente è stato cliccato
    // Inizia a trascinare
}

function drag(event) {
    // Aggiorna posizione del componente
    // Ridisegna canvas
}

function endDrag(event) {
    // Rilascia il componente
}
```

### Legge di Ohm in Circuiti 📐

```
V = I × R
I = V / R
R = V / I

Dove:
- V = Tensione [Volt]
- I = Corrente [Ampere]
- R = Resistenza [Ohm]

Circuito semplice:
┌──[Battery 5V]──[R 100Ω]──┐
└─────────────────────────┘

I = V / R = 5 / 100 = 0.05 A = 50 mA
P = V × I = 5 × 0.05 = 0.25 W
```

---

## 📋 Struttura File

```
es09-simulatore-circuiti-web/
├── consegna/
│   └── README.md (questo file)
└── soluzione/
    ├── index.html
    ├── style.css
    └── script.js

Dimensione attesa:
- index.html: ~200-300 linee
- style.css: ~400-500 linee
- script.js: ~1000-1500 linee
```

---

## 💻 Componenti JavaScript

### Struttura Classe Component

```javascript
class Component {
    constructor(x, y, type) {
        this.x = x;           // Posizione X
        this.y = y;           // Posizione Y
        this.type = type;     // 'resistor', 'battery', 'led', etc
        this.width = 60;      // Larghezza disegno
        this.height = 40;     // Altezza disegno
        this.rotation = 0;    // Rotazione (gradi)
        this.selected = false; // Selezionato?

        // Proprietà specifiche per tipo
        if (type === 'resistor') {
            this.resistance = 100;  // Ohm
        } else if (type === 'battery') {
            this.voltage = 5;       // Volt
        } else if (type === 'led') {
            this.isOn = false;      // LED acceso/spento
        }
    }

    draw(ctx) {
        // Disegnare il componente
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate((this.rotation * Math.PI) / 180);

        if (this.type === 'resistor') {
            this.drawResistor(ctx);
        } else if (this.type === 'battery') {
            this.drawBattery(ctx);
        } else if (this.type === 'led') {
            this.drawLED(ctx);
        } else if (this.type === 'wire') {
            this.drawWire(ctx);
        } else if (this.type === 'switch') {
            this.drawSwitch(ctx);
        }

        ctx.restore();
    }

    drawResistor(ctx) {
        // Disegnare zigzag /\/\/\
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.beginPath();
        // ... disegno
    }

    contains(x, y) {
        // Verifica se punto (x, y) è dentro il componente
        return x >= this.x && x <= this.x + this.width &&
               y >= this.y && y <= this.y + this.height;
    }

    rotate(degrees) {
        this.rotation = (this.rotation + degrees) % 360;
    }
}
```

### Classe Circuit

```javascript
class Circuit {
    constructor() {
        this.components = [];  // Lista componenti
        this.wires = [];       // Lista fili
        this.selectedComponent = null;
    }

    addComponent(component) {
        this.components.push(component);
    }

    addWire(from, to) {
        this.wires.push({ from, to });
    }

    removeComponent(component) {
        this.components = this.components.filter(c => c !== component);
    }

    simulate() {
        // Calcolare correnti/tensioni
        // Usare Ohm's law: V = I × R
        for (let wire of this.wires) {
            const component = wire.from;
            if (component.type === 'battery') {
                const voltage = component.voltage;
                // Calcolare corrente totale
                let totalResistance = 0;
                for (let comp of this.components) {
                    if (comp.type === 'resistor') {
                        totalResistance += comp.resistance;
                    }
                }

                const current = voltage / totalResistance;

                // Aggiornare stato LED
                for (let comp of this.components) {
                    if (comp.type === 'led') {
                        comp.isOn = current > 0.001; // Acceso se corrente > 1mA
                    }
                }
            }
        }
    }

    draw(ctx) {
        // Disegnare tutti i componenti e fili
        for (let wire of this.wires) {
            // Disegnare filo
            ctx.strokeStyle = '#333333';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(wire.from.x + wire.from.width/2,
                      wire.from.y + wire.from.height/2);
            ctx.lineTo(wire.to.x + wire.to.width/2,
                      wire.to.y + wire.to.height/2);
            ctx.stroke();
        }

        for (let component of this.components) {
            component.draw(ctx);
        }
    }

    save() {
        // Esportare circuito come JSON
        return JSON.stringify({
            components: this.components,
            wires: this.wires
        });
    }

    load(jsonString) {
        // Importare circuito da JSON
        const data = JSON.parse(jsonString);
        this.components = data.components.map(c =>
            new Component(c.x, c.y, c.type)
        );
        this.wires = data.wires;
    }
}
```

### Event Handling

```javascript
// Drag & drop
let draggedComponent = null;
let dragOffsetX = 0;
let dragOffsetY = 0;

canvas.addEventListener('mousedown', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Trovare componente cliccato
    for (let component of circuit.components) {
        if (component.contains(x, y)) {
            draggedComponent = component;
            dragOffsetX = x - component.x;
            dragOffsetY = y - component.y;
            break;
        }
    }
});

canvas.addEventListener('mousemove', (event) => {
    if (draggedComponent) {
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        draggedComponent.x = x - dragOffsetX;
        draggedComponent.y = y - dragOffsetY;

        // Ridisegnare
        redraw();
    }
});

canvas.addEventListener('mouseup', () => {
    draggedComponent = null;
});
```

### Salvataggio su localStorage

```javascript
function saveCircuit() {
    const jsonData = circuit.save();
    localStorage.setItem('savedCircuit', jsonData);
    alert('Circuito salvato!');
}

function loadCircuit() {
    const jsonData = localStorage.getItem('savedCircuit');
    if (jsonData) {
        circuit.load(jsonData);
        redraw();
        alert('Circuito caricato!');
    } else {
        alert('Nessun circuito salvato!');
    }
}
```

---

## 🌍 Interfaccia Utente

### Layout Responsive (CSS Grid)

```html
<div class="container">
    <div class="toolbar">
        <button id="btn-resistor">Resistore</button>
        <button id="btn-battery">Batteria</button>
        <button id="btn-led">LED</button>
        <button id="btn-wire">Filo</button>
        <button id="btn-clear">Cancella</button>
    </div>

    <canvas id="circuit-canvas"></canvas>

    <div class="info-panel">
        <div id="voltage-display">Tensione: -- V</div>
        <div id="current-display">Corrente: -- A</div>
        <div id="power-display">Potenza: -- W</div>
        <button id="btn-simulate">Simula</button>
        <button id="btn-save">Salva</button>
        <button id="btn-load">Carica</button>
    </div>
</div>
```

### CSS Responsive

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    height: 100vh;
}

.toolbar {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 15px;
    background-color: #f0f0f0;
    border-radius: 5px;
}

#circuit-canvas {
    border: 2px solid #333;
    cursor: crosshair;
    background-color: white;
}

.info-panel {
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

@media (max-width: 768px) {
    .container {
        grid-template-columns: 1fr;
    }
}
```

---

## 🧪 Checklist Funzionalità

### Fase 1: Disegno Componenti ✅
- [ ] Disegnare resistore (zigzag)
- [ ] Disegnare batteria (+ e -)
- [ ] Disegnare LED
- [ ] Disegnare interruttore
- [ ] Disegnare filo

### Fase 2: Interazione Utente 🖱️
- [ ] Drag & drop componenti
- [ ] Click per selezionare
- [ ] Rotate con tasto R
- [ ] Delete con tasto D
- [ ] Double-click per properties

### Fase 3: Connessione Fili 🔌
- [ ] Disegnare fili tra componenti
- [ ] Rilevare connessioni
- [ ] Visualizzare nodi di connessione
- [ ] Validare circuito (nessun loop aperto)

### Fase 4: Simulazione ⚡
- [ ] Calcolare tensione totale
- [ ] Calcolare corrente (Ohm's law)
- [ ] Calcolare potenza (P = V × I)
- [ ] Aggiornare stato LED
- [ ] Mostrare valori in info panel

### Fase 5: Persistenza 💾
- [ ] Salvare su localStorage
- [ ] Caricare da localStorage
- [ ] Esportare JSON
- [ ] Importare JSON

### Fase 6: UI/UX 🎨
- [ ] Responsive design (mobile-friendly)
- [ ] Dark mode toggle (bonus)
- [ ] Zoom e pan del canvas
- [ ] Undo/Redo (bonus)

---

## 🛠️ Step Implementazione (7-10 passaggi)

### STEP 1: Setup HTML Base ✅
- [ ] Creare `index.html` con canvas
- [ ] Aggiungere toolbar buttons
- [ ] Creare info panel
- [ ] Linkare CSS e JS

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Simulatore Circuiti</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="toolbar">
            <button id="btn-resistor">➕ Resistore</button>
            <button id="btn-battery">🔋 Batteria</button>
            <button id="btn-led">💡 LED</button>
            <button id="btn-wire">〰️ Filo</button>
            <button id="btn-clear">❌ Cancella Tutto</button>
        </div>

        <canvas id="circuit-canvas" width="800" height="600"></canvas>

        <div class="info-panel">
            <h3>Info Circuito</h3>
            <p>Tensione: <span id="voltage">-- V</span></p>
            <p>Corrente: <span id="current">-- A</span></p>
            <p>Potenza: <span id="power">-- W</span></p>
            <button id="btn-simulate">Simula</button>
            <button id="btn-save">Salva</button>
            <button id="btn-load">Carica</button>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### STEP 2: CSS Styling 🎨
- [ ] Creare layout responsivo con Grid
- [ ] Stilizzare buttons e canvas
- [ ] Aggiungere colori e bordi
- [ ] Mobile-friendly media queries

### STEP 3: Classe Component 🔌
- [ ] Implementare Component class
- [ ] Metodi draw() per ogni tipo
- [ ] Metodo contains() per hit detection
- [ ] Proprietà per resistenza, tensione, etc

### STEP 4: Classe Circuit ⚙️
- [ ] Implementare Circuit class
- [ ] addComponent(), removeComponent()
- [ ] addWire(), removeWire()
- [ ] simulate() con Ohm's law
- [ ] draw() per tutto

### STEP 5: Event Handling - Drag & Drop 🖱️
- [ ] Implementare mousedown, mousemove, mouseup
- [ ] Drag per trascinare componenti
- [ ] Click per selezionare
- [ ] Visualizzare selezione con bordo/evidenziazione

### STEP 6: Disegno Componenti 🎨
- [ ] drawResistor() - zigzag /\/\/\
- [ ] drawBattery() - + e -
- [ ] drawLED() - cerchio + triagolo luce
- [ ] drawWire() - linea
- [ ] drawSwitch() - linea + cerchietto

### STEP 7: Connessione Fili 🔌
- [ ] Rilevare click su "connettore" componente
- [ ] Disegnare filo temporaneo seguendo mouse
- [ ] Connettere quando mouse rilasciato
- [ ] Mostrare nodi di connessione

### STEP 8: Simulazione Circuito ⚡
- [ ] Calcolare V (da batteria)
- [ ] Calcolare R_totale (somma resistori)
- [ ] Calcolare I = V / R
- [ ] Calcolare P = V × I
- [ ] Aggiornare LED se I > soglia
- [ ] Mostrare valori su info panel

### STEP 9: Salvataggio e Caricamento 💾
- [ ] Implementare save() → localStorage
- [ ] Implementare load() ← localStorage
- [ ] JSON serialization/deserialization
- [ ] Pulsanti Save/Load funzionanti

### STEP 10: Polish e Testing 🎯
- [ ] Testare drag & drop
- [ ] Testare simulazione con vari circuiti
- [ ] Testare save/load
- [ ] Responsive design (prova su mobile)
- [ ] Gestire edge cases (circuito vuoto, etc)

---

## 💡 Trucchi JavaScript 🎯

### 1. Canvas Drawing API

```javascript
// Salva stato
ctx.save();
ctx.translate(x, y);
ctx.rotate(angle);
// ... disegni
ctx.restore();

// Path (outlines)
ctx.beginPath();
ctx.moveTo(x1, y1);
ctx.lineTo(x2, y2);
ctx.stroke();

// Shapes riempite
ctx.fillRect(x, y, w, h);
ctx.fillStyle = 'rgb(255, 0, 0)';

// Testo
ctx.font = '16px Arial';
ctx.fillText('Testo', x, y);

// Trasformazioni
ctx.scale(1.5, 1.5);
ctx.skew(angolo);
```

### 2. Event Listeners

```javascript
// Click
canvas.addEventListener('click', (e) => {
    console.log(e.clientX, e.clientY);
});

// Drag
let isDragging = false;
canvas.addEventListener('mousedown', () => isDragging = true);
canvas.addEventListener('mousemove', (e) => {
    if (isDragging) {
        // Drag logic
    }
});
canvas.addEventListener('mouseup', () => isDragging = false);

// Keyboard
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        // Deselect
    }
});
```

### 3. localStorage

```javascript
// Salvare
const data = { x: 10, y: 20, type: 'resistor' };
localStorage.setItem('myData', JSON.stringify(data));

// Caricare
const loaded = JSON.parse(localStorage.getItem('myData'));

// Verificare
if (localStorage.getItem('myData')) {
    console.log('Data found');
}
```

### 4. requestAnimationFrame

```javascript
function animate() {
    // Pulire canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Disegnare
    circuit.draw(ctx);

    // Prossimo frame
    requestAnimationFrame(animate);
}

animate(); // Iniziare
```

### 5. Classes (ES6)

```javascript
class MyComponent {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    move(dx, dy) {
        this.x += dx;
        this.y += dy;
    }

    static createDefault() {
        return new MyComponent(0, 0);
    }
}

const comp = new MyComponent(10, 20);
comp.move(5, 5);
```

---

## ⚠️ Errori Comuni 🐛

### JavaScript

1. **Canvas non ridisegnato**
   ```javascript
   ❌ function draw() {
        ctx.fillRect(10, 10, 100, 50);
   }
   // Non ridisegna loop!

   ✅ function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillRect(10, 10, 100, 50);
        requestAnimationFrame(animate);
   }
   ```

2. **Event listener su elemento inesistente**
   ```javascript
   ❌ document.getElementById('btn-resistor').addEventListener(...);
   // Se btn-resistor non esiste, crash!

   ✅ const btn = document.getElementById('btn-resistor');
      if (btn) btn.addEventListener(...);
   ```

3. **Mouse coordinates sbagliate**
   ```javascript
   ❌ const x = event.clientX;  // Relativo a viewport

   ✅ const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;  // Relativo a canvas
   ```

4. **JSON.parse fallisce silenziosamente**
   ```javascript
   ❌ const data = JSON.parse(localStorage.getItem('key'));
      // Se non valido, crash!

   ✅ try {
        const data = JSON.parse(localStorage.getItem('key') || '{}');
   } catch (e) {
        console.error('Invalid JSON', e);
   }
   ```

### HTML/CSS

1. **Canvas non responsive**
   ```css
   ❌ #circuit-canvas {
        width: 100%;
        height: 100%;
   }
   /* Non scala proprietà interne! */

   ✅ #circuit-canvas {
        max-width: 100%;
        height: auto;
   }
   /* Oppure scalare via JavaScript */
   ```

2. **Buttons overlapping su mobile**
   ```css
   ❌ .toolbar button {
        width: 150px;
   }

   ✅ .toolbar button {
        flex: 1;
        min-width: 80px;
   }
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Dark Mode Toggle ⭐

```javascript
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}
```

### Sfida 2: Zoom e Pan ⭐

```javascript
let zoom = 1;
let panX = 0;
let panY = 0;

canvas.addEventListener('wheel', (e) => {
    e.preventDefault();
    zoom *= (e.deltaY > 0) ? 0.9 : 1.1;
    redraw();
});
```

### Sfida 3: Undo/Redo ⭐⭐

```javascript
class History {
    constructor() {
        this.states = [];
        this.currentIndex = -1;
    }

    save(state) {
        this.states = this.states.slice(0, this.currentIndex + 1);
        this.states.push(JSON.stringify(state));
        this.currentIndex++;
    }

    undo() {
        if (this.currentIndex > 0) {
            this.currentIndex--;
            return JSON.parse(this.states[this.currentIndex]);
        }
    }

    redo() {
        if (this.currentIndex < this.states.length - 1) {
            this.currentIndex++;
            return JSON.parse(this.states[this.currentIndex]);
        }
    }
}
```

### Sfida 4: Esportazione Immagine ⭐⭐

```javascript
function exportAsImage() {
    const link = document.createElement('a');
    link.href = canvas.toDataURL('image/png');
    link.download = 'circuito.png';
    link.click();
}
```

### Sfida 5: Editor Properties Avanzato ⭐⭐⭐

```javascript
// Dialog interattivo per cambiare proprietà componente
function showPropertyDialog(component) {
    const dialog = document.createElement('div');
    dialog.className = 'property-dialog';

    if (component.type === 'resistor') {
        dialog.innerHTML = `
            <label>Resistenza (Ω):
                <input type="number" id="resistance-input"
                       value="${component.resistance}">
            </label>
        `;
    } else if (component.type === 'battery') {
        dialog.innerHTML = `
            <label>Tensione (V):
                <input type="number" id="voltage-input"
                       value="${component.voltage}">
            </label>
        `;
    }

    document.body.appendChild(dialog);
}
```

---

## 📚 Risorse e Link Utili 🔗

### Documentazione JavaScript
- [MDN: Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
- [MDN: localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [MDN: Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)

### HTML/CSS
- [MDN: CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)

### Simulatori Circuiti Online
- [CircuitJS.org](https://www.circuitjs.org/) - Simulatore interattivo (open source)
- [EveryCircuit](https://www.everycircuit.com/) - Simulatore cloud
- [Falstad Circuit Simulator](http://www.falstad.com/circuit/) - Classico

### Letture Consigliate
1. Mozilla MDN: "Canvas Tutorial"
2. "Interactive JavaScript" - Douglas Crockford
3. "HTML5 Canvas Cookbook" - Eric Rowell

---

## 📱 Mock-up Interfaccia

```
┌────────────────────────────────────────────────┐
│  [➕ Resistore] [🔋 Batteria] [💡 LED]...      │  ← Toolbar
├────────────────────────────────────────────────┤
│                                         │ Info  │
│                                         │ Panel │
│                                         │       │
│   Canvas - Disegna qui i circuiti      │       │
│                                         │ Tens. │
│   [Component 1]      [Component 2]     │ Curr. │
│         |════════════════╪════════     │ Power │
│         |                      |       │       │
│   [Component 3]           [Component 4]│       │
│                                         │ Simul.│
│                                         │ Save  │
│                                         │ Load  │
└────────────────────────────────────────────────┘

Mobile (responsive):
┌──────────────────────┐
│ [➕] [🔋] [💡] [〰️]  │
├──────────────────────┤
│    Canvas            │
│  (zoom: 1x)          │
├──────────────────────┤
│ Tensione: -- V       │
│ Corrente: -- A       │
│ Potenza: -- W        │
│ [Simula] [Salva]     │
└──────────────────────┘
```

---

## 🎯 Checklist Completamento Finale

```
HTML & CSS:
[ ] index.html con canvas e controls
[ ] style.css responsive (mobile-friendly)
[ ] Dark mode support (bonus)
[ ] Layout grid con toolbar + canvas + info

JavaScript - Struttura:
[ ] Classe Component con subclass per tipi
[ ] Classe Circuit per gestire circuito
[ ] Funzioni draw per ogni componente
[ ] Event listeners setup

JavaScript - Interazione:
[ ] Drag & drop componenti
[ ] Selezionare/deselezionare
[ ] Disegnare fili tra componenti
[ ] Rotare componenti (bonus)
[ ] Cancellare componenti

JavaScript - Simulazione:
[ ] Calcolare V da batterie
[ ] Calcolare R totale
[ ] Calcolare I (Ohm's law)
[ ] Calcolare P (potenza)
[ ] Aggiornare LED state
[ ] Mostrare valori su UI

JavaScript - Persistenza:
[ ] Save → localStorage
[ ] Load ← localStorage
[ ] JSON serialize/deserialize
[ ] Export image (bonus)

Testing:
[ ] Creare circuito e simulare
[ ] Salvare e ricaricare
[ ] Test su mobile
[ ] Edge cases (circuito vuoto, etc)

BONUS:
[ ] 1-2 sfide bonus completate
[ ] Dark mode + light mode
[ ] Zoom/pan canvas
[ ] Property editor dialogs
```

---

## 🎓 Conclusione

Hai creato un'**applicazione web interattiva** completa che permette di:
- Disegnare circuiti visualmente
- Simulare il comportamento
- Visualizzare grandezze elettriche in tempo reale
- Salvare e caricare le tue creazioni

Questo è un vero progetto che potrebbe essere usato per insegnare l'elettrotecnica agli studenti!

**Prossimo step:** ES10 - Quiz sulla Sicurezza Elettrica 🛡️

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS
