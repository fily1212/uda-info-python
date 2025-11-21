# ES10 - Sicurezza Elettrica Quiz 🛡️

## Metadata del Corso 📋
| Campo | Valore |
|-------|--------|
| **Corso** | Telecomunicazioni (Programma Ministeriale - II ITIS) |
| **Livello di Difficoltà** | ⭐⭐ INTERMEDIO |
| **Durata Stimata** | 4-5 ore |
| **Linguaggio** | JavaScript (ES6+) / HTML5 / CSS3 |
| **Prerequisiti** | ES06-ES09 completati, HTML/CSS/JS base |
| **Argomento TLC** | Sicurezza: Rischi Elettrici in Laboratorio |

---

## 🎓 Concetti Fondamentali

### Pericoli Elettrici ⚡

L'**elettricità** è un pericolo reale che causa:
- **Scosse elettriche** (folgorazione)
- **Ustioni** termiche
- **Archi elettrici** (flash)
- **Incendi**

```
Fattori di pericolo:
┌──────────────────────────────────────┐
│ Tensione (V)                         │
│ - AC vs DC (AC è più pericoloso)    │
│ - Soglia pericolosa: > 50V AC       │
│                                      │
│ Corrente (I)                         │
│ - Soglia percezione: 1 mA           │
│ - Soglia non rilascio: 10 mA        │
│ - Fibillazione: > 100 mA            │
│                                      │
│ Tempo contatto                       │
│ - < 1 sec: potenzialmente salvabile│
│ - > 1 sec: rischio fibrillazione   │
│                                      │
│ Resistenza corpo (R)                │
│ - Pelle umida: 500 Ω               │
│ - Pelle secca: 100.000 Ω           │
│ - Cuore: ~1 Ω                      │
└──────────────────────────────────────┘

Corrente (mA) vs Effetto su corpo umano:
┌─────────────────────────────────────┐
│ 0-1 mA:      Non percettibile       │
│ 1-5 mA:      Stimolazione sensoriale│
│ 5-10 mA:     Contrazione muscolare  │
│ 10-20 mA:    Tetania muscolare      │
│ 20-50 mA:    Fibrillazione ventricoli│ ⚠️ MORTALE
│ > 200 mA:    Ustione cardiaca       │ ⚠️ MORTALE
└─────────────────────────────────────┘
```

---

### Dispositivi di Protezione 🔌

```
1. FUSIBILI (Fuse)
   - Elemento metallico che fonde se corrente > soglia
   - Protegge il circuito (non la persona!)
   - Tempo risposta: lento (non ideale)

2. INTERRUTTORE DIFFERENZIALE (RCD - Residual Current Device)
   - Rileva perdita di corrente (fuga a terra)
   - Soglia tipica: 30 mA
   - Tempo risposta: < 40 ms
   - ⭐ Protezione MIGLIORE per persone

3. PROTEZIONE SOVRACCARICO (MCB - Miniature Circuit Breaker)
   - Rileva sovraccorrente
   - Scatta in 1-30 secondi
   - Protegge impianto

4. MESSA A TERRA (Earth/Ground)
   - Fornisce percorso sicuro per dispersione corrente
   - Riduce tensione di contatto
   - Simbolo: ⏚

5. DOPPIO ISOLAMENTO
   - Due strati di isolante
   - Marcato con ⊡ (quadrato doppio)
   - Se uno fa cedere, l'altro protegge
```

---

### DPI (Dispositivi Protezione Individuale) 👷

```
GUANTI:
- Isolanti per lavori ad alta tensione
- Materiale: gomma, pelle sintetica
- Test: scarpe isolanti con 10 kV

SCARPE:
- Suola isolante
- Non conduttive
- Test con 10-15 kV

OCCHIALI:
- Protezione da scintille e archi
- Anti-abbagliamento per saldature

ABBIGLIAMENTO:
- Indumenti non infiammabili
- Non sintetici (infiammabili!)
- Cotone, lana, tessuti speciali

ELMETTO:
- Protezione da cadute di strumenti
- Visiera anti-arco (per alta tensione)

GUANTI DI PRIMO SOCCORSO:
- Sempre a disposizione
- Per non scottarsi durante RCP
```

---

### Comportamenti Sicuri 🚦

```
✅ COMPORTAMENTI CORRETTI:
1. Verificare tensione prima di toccare
2. Usare tester/multimetro
3. Lavorare con una sola mano se possibile
   (Evita percorso attraverso il cuore)
4. Indossare DPI appropriati
5. Segnalare pericoli ai colleghi
6. Non lavorare da soli su impianti
7. Togliere orologi/braccialetti (conduttivi)
8. Tenere capelli lunghi legati
9. Usare piattaforme isolanti
10. Controllare strumenti (niente cavi lisi)

❌ COMPORTAMENTI VIETATI:
1. Lavorare su circuiti con le mani bagnate
2. Indossare scarpe non isolanti
3. Toccare di due mani (percorso pericoloso)
4. Usare utensili non isolati
5. Lavorare da soli (nessuno per RCP!)
6. Ignorare allarmi/segnalazioni
7. Bypassare protezioni/fusibili
8. Lavorare sotto tensione senza autorizzazione
9. Staccare cavi viventi a mano nuda
10. Distrazioni mentre si lavora
```

---

### Primo Soccorso Base 🏥

```
PASSO 1: PROTEGGERE SE STESSI
┌──────────────────────────────────┐
│ ⚠️ NON toccare direttamente!     │
│ 1. Spegnere alimentazione (if   │
│    possibile senza rischio)      │
│ 2. Se impossibile, usare oggetto │
│    non conduttivo (legno, gomma) │
│    per allontanare infortunato   │
│ 3. Indossare guanti se disponibili
└──────────────────────────────────┘

PASSO 2: VERIFICARE SEGNI VITALI
- Controllare respiro (ascolta 10 sec)
- Controllare polso (carotideo o radiale)
- Guarda se petto si muove

PASSO 3: CONTATTARE SOCCORSI
- Chiama 118 (o emergenza locale)
- Descrivi la situazione
- Segui istruzioni operatore

PASSO 4: RCP (Rianimazione Cardiopolmonare)
Se incosciente + non respira:
┌────────────────────────────────────┐
│ 1. Metti persona su schiena (piano)│
│ 2. Inclina testa leggermente       │
│ 3. Compressionb petto:             │
│    - Posiziona mani al centro      │
│    - Prem forte 5-6 cm di profond. │
│    - Frequenza: 100-120/min        │
│ 4. Alternan con respirazione bocca │
│    a bocca (30:2 ratio)            │
│ 5. Continua finché:                │
│    - Ambulanza arriva              │
│    - Persona respira               │
│    - Esausto (non puoi più)        │
└────────────────────────────────────┘

PASSO 5: DEFIBRILLATORE (AED)
Se disponibile:
- Attacca elettrodi come indicato
- Segui istruzioni vocali
- Assicura nessuno tocca
- Prem bottone per shock
```

---

## 📋 Struttura Quiz

```
es10-sicurezza-elettrica-quiz/
├── consegna/
│   └── README.md (questo file)
└── soluzione/
    ├── index.html (quiz HTML)
    ├── style.css (styling)
    └── script.js (logica quiz)

Contenuto atteso:
- 20-30 domande multiple choice
- 4 opzioni per domanda
- Timer countdown per sezione
- Punteggio finale con feedback
- Spiegazioni per risposte sbagliate
- Best score salvato su localStorage
- Certificato finale (generato dinamicamente)
```

---

## 💻 Struttura HTML

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Quiz Sicurezza Elettrica</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Schermata Iniziale -->
    <div id="home-screen" class="screen">
        <h1>🛡️ Quiz Sicurezza Elettrica</h1>
        <p>Valuta le tue conoscenze sulla sicurezza in laboratorio</p>
        <button id="btn-start">Inizia Quiz</button>
        <div id="best-score">Best score: <span id="score-display">--</span>%</div>
    </div>

    <!-- Quiz Screen -->
    <div id="quiz-screen" class="screen hidden">
        <div class="quiz-container">
            <div class="timer">
                ⏱️ Tempo: <span id="timer-display">60</span>s
            </div>

            <div class="progress">
                Domanda <span id="current-question">1</span> di <span id="total-questions">20</span>
            </div>

            <div class="question-container">
                <h2 id="question-text"></h2>

                <div id="options-container">
                    <!-- Opzioni generate dinamicamente -->
                </div>

                <div class="buttons">
                    <button id="btn-previous" class="btn-nav">← Precedente</button>
                    <button id="btn-next" class="btn-nav">Prossima →</button>
                    <button id="btn-finish" class="btn-finish hidden">Finisci Quiz</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Risultati Screen -->
    <div id="results-screen" class="screen hidden">
        <h1>Risultati Quiz 📊</h1>

        <div class="results-container">
            <div class="score-display">
                <div class="score-circle">
                    <span id="final-score">--</span>%
                </div>
                <div id="score-message"></div>
            </div>

            <div class="stats">
                <p>Domande Corrette: <strong id="correct-count">0</strong>/<span id="total-count">20</span></p>
                <p>Tempo Impiegato: <strong id="time-spent">0</strong>s</p>
            </div>

            <div id="review-mistakes">
                <h3>Risposte Sbagliate</h3>
                <div id="mistakes-list"></div>
            </div>

            <div id="certificate-section" class="hidden">
                <h3>🎓 Certificato di Completamento</h3>
                <canvas id="certificate-canvas" width="800" height="600"></canvas>
                <button id="btn-download-certificate">⬇️ Scarica Certificato</button>
            </div>

            <div class="buttons">
                <button id="btn-retry">🔄 Ritenta Quiz</button>
                <button id="btn-home">🏠 Torna Home</button>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

---

## 💻 JavaScript: Struttura Dati Quiz

```javascript
const quizData = [
    {
        question: "Quale corrente è considerata pericolosa per il corpo umano?",
        options: [
            "1 mA",
            "10 mA (fibillazione cardiaca)",
            "100 mA",
            "1 A"
        ],
        correct: 1,  // Indice dell'opzione corretta
        explanation: "Una corrente di 10 mA causa tetania muscolare e fibrillazione cardiaca, rischio mortale.",
        category: "rischi"
    },
    {
        question: "Qual è la funzione principale di un Differenziale (RCD)?",
        options: [
            "Proteggere da sovraccarichi",
            "Rilevare perdite di corrente e proteggere da elettrocuzione",
            "Limitare la potenza",
            "Nulla, è decorativo"
        ],
        correct: 1,
        explanation: "Il dispositivo differenziale rileva se corrente scappa a terra (fuga) e interrompe il circuito in milli-secondi.",
        category: "protezione"
    },
    {
        question: "Come proteggi il cuore da una scossa elettrica?",
        options: [
            "Toccando con due mani",
            "Toccando con una sola mano, se possibile",
            "Evitando completamente l'elettricità",
            "Indossando un maglioncino"
        ],
        correct: 1,
        explanation: "Evitare di toccare con entrambi le mani per non creare un circuito attraverso il cuore (da un braccio all'altro)",
        category: "comportamento"
    },
    {
        question: "Quale DPI (Dispositivo di Protezione) è OBBLIGATORIO in laboratorio?",
        options: [
            "Solo guanti",
            "Solo scarpe isolanti",
            "Guanti + Scarpe isolanti + Abbigliamento appropriato",
            "Niente, gli attrezzi sono isolati"
        ],
        correct: 2,
        explanation: "DPI multipli proteggono da molteplici rischi. Niente è 100% sicuro da solo.",
        category: "dpi"
    },
    {
        question: "Quale azione fare PRIMA di toccare un circuito apparentemente spento?",
        options: [
            "Toccare subito (se non vedi tensione, è sicuro)",
            "Verificare con un tester/multimetro",
            "Chiedere a un collega",
            "Attendere 10 minuti"
        ],
        correct: 1,
        explanation: "Sempre verificare con un multimetro! Condensatori possono stoccare tensione anche se apparentemente spenti.",
        category: "verifica"
    },
    {
        question: "Cosa fare se una persona tocca un cavo ad alta tensione?",
        options: [
            "Toccarla subito per trascinarlа via",
            "Spegnere l'alimentazione (o usare oggetto non conduttivo per allontanarla)",
            "Aspettare che si rilasci da sola",
            "Lanciare acqua per interrompere il contatto"
        ],
        correct: 1,
        explanation: "Non toccare direttamente! Potresti diventare parte del circuito. Spegni o usa legno/gomma.",
        category: "emergenza"
    },
    {
        question: "Quale primo soccorso fare se una persona è incosciente e non respira dopo choc?",
        options: [
            "Aspettare che si riprenda da sola",
            "Iniziare RCP (rianimazione cardiopolmonare) e chiamare 118",
            "Dare acqua zuccherata",
            "Muoverla ripetutamente"
        ],
        correct: 1,
        explanation: "RCP (30 compressioni: 2 respirazioni) + ambulanza sono critica. Ogni minuto senza azione = danni cerebrali.",
        category: "primo_soccorso"
    },
    {
        question: "Quale materiale è VIETATO come abbigliamento nei laboratori ad alta tensione?",
        options: [
            "Cotone",
            "Lana",
            "Nylon/Sintetici (infiammabili!)",
            "Denim"
        ],
        correct: 2,
        explanation: "I sintetici bruciano/si sciolgono sul corpo. Cotone e lana sono molto più sicuri.",
        category: "dpi"
    },
    {
        question: "A cosa serve un FUSIBILE?",
        options: [
            "Proteggere la persona dall'elettrocuzione",
            "Proteggere il CIRCUITO da sovraccorrente",
            "Entrambi",
            "Nulla, è decorativo"
        ],
        correct: 1,
        explanation: "Il fusibile protegge l'impianto (brucia se corrente troppo alta). NON protegge la persona! Per quello serve il differenziale.",
        category: "protezione"
    },
    {
        question: "Quale tensione è considerata SICURA per il corpo umano?",
        options: [
            "< 50V AC (corrente alternata)",
            "< 120V DC (corrente continua)",
            "< 1000V",
            "Niente è 100% sicuro"
        ],
        correct: 0,
        explanation: "Per circuiti AC, < 50V è considerato 'bassissima tensione' sicuro. DC è meno pericoloso (no fibrillazione), ma comunque pericoloso.",
        category: "rischi"
    },
    {
        question: "Come dovrebbe essere posizionato il corpo durante un primo soccorso RCP?",
        options: [
            "Su un lato (posizione di recupero)",
            "Su schiena, su superficie piana",
            "In piedi se possibile",
            "Non importa la posizione"
        ],
        correct: 1,
        explanation: "Su schiena, superficie PIANA, permette compressioni al petto efficaci. Testa leggermente inclinata per via aeree libere.",
        category: "primo_soccorso"
    },
    {
        question: "Quale frequenza di compressione toracica è corretta nella RCP?",
        options: [
            "30-50 al minuto",
            "100-120 al minuto",
            "150-200 al minuto",
            "Non importa la frequenza, solo fai compressioni"
        ],
        correct: 1,
        explanation: "100-120 compressioni/minuto è il standard internazionale. Troppo lento o troppo veloce riduce efficacia.",
        category: "primo_soccorso"
    },
    {
        question: "Se noti un odore di bruciato/fumo da un cavo, cosa fare?",
        options: [
            "Ignorare, è normale",
            "Spegnere immediatamente e non usare finché non riparato",
            "Toccare il cavo per vedere se è caldo",
            "Continuare a usare se non scintilla"
        ],
        correct: 1,
        explanation: "Odore di bruciato = isolamento compromesso = rischio altissimo. Spegni e sostituisci. Non toccare!",
        category: "verifica"
    },
    {
        question: "Quale resistenza ha il corpo umano in condizioni normali (pelle secca)?",
        options: [
            "~50 Ω",
            "~500 Ω",
            "~100.000 Ω",
            "~1.000.000 Ω"
        ],
        correct: 2,
        explanation: "Pelle secca: ~100 kΩ. Con pelle bagnata scende a ~500 Ω, molta più pericolosa per lo stesso voltaggio.",
        category: "rischi"
    },
    {
        question: "Quale è la sequenza corretta di RCP?",
        options: [
            "Compressionè petto → respira → verifica polso",
            "Verifica polso → respira → compressionè petto",
            "30 compressionè petto → 2 respiri → ripeti",
            "Chiama 118 → 10 respiri → stop"
        ],
        correct: 2,
        explanation: "Rapporto 30:2 è standard. Non perdere tempo a controllare polso, inizia subito compressioni.",
        category: "primo_soccorso"
    },
    {
        question: "Quale strumento usare per verificare se un circuito è 'spento' in sicurezza?",
        options: [
            "Le dita (test rapido)",
            "Multimetro/Tester digitale",
            "Uno stecchetto di legno",
            "Niente, basta guardare"
        ],
        correct: 1,
        explanation: "Multimetro è lo strumento standard. Con impostazione corretta (V AC/DC) dice la verità. Le dita non sono affidabili!",
        category: "verifica"
    },
    {
        question: "A quale voltaggio gli archi elettrici diventano pericolosi?",
        options: [
            "Sopra 12V",
            "Sopra 50V",
            "Sopra 1000V",
            "Non è il voltaggio, è solo la corrente"
        ],
        correct: 2,
        explanation: "Sopra 1000V gli archi diventano violenti (lunghezza arc > 1cm), causano ustioni gravi anche da lontano.",
        category: "rischi"
    },
    {
        question: "Se stai lavorando su un circuito con una sola mano, perché è più sicuro?",
        options: [
            "Non importa quante mani, il rischio è lo stesso",
            "Evita un percorso attraverso il cuore (da un braccio all'altro)",
            "L'altra mano distrae il corpo dal danno",
            "È solo una superstizione, non ha senso fisico"
        ],
        correct: 1,
        explanation: "Toccare con 2 mani = corrente da braccio → braccio = attraverso il cuore = aritmia cardiaca mortale.",
        category: "comportamento"
    },
    {
        question: "Quale è il tempo massimo di contatto elettrico sopravvivibile?",
        options: [
            "< 0.1 secondi",
            "< 1 secondo",
            "< 5 secondi",
            "Non dipende dal tempo, solo dalla corrente"
        ],
        correct: 1,
        explanation: "Oltre 1 secondo il rischio di fibrillazione aumenta drasticamente. Ogni secondo conta!",
        category: "rischi"
    },
    {
        question: "Quale colore di isolamento indica 'TERRA' nei cavi?",
        options: [
            "Rosso e nero a strisce",
            "Giallo e verde a strisce (⏚)",
            "Blu",
            "Bianco"
        ],
        correct: 1,
        explanation: "Giallo-verde = TERRA (ground). Blu = Neutro. Marrone = Fase. Standard internazionale.",
        category: "codice_colori"
    },
    {
        question: "Se una persona è folgorata e rimane attaccata al cavo, cosa NON fare?",
        options: [
            "Toccarla direttamente (diventi parte del circuito)",
            "Spegnere l'alimentazione",
            "Usare un oggetto conduttivo (metallo) per allontanarla",
            "Tutte le precedenti sono scorrette"
        ],
        correct: 2,
        explanation: "Non usare metallo! Usa legno, gomma, o carta. Il metallo conduce e peggior la situazione.",
        category: "emergenza"
    }
];
```

---

## 🧪 Checklist Funzionalità

### Fase 1: Interfaccia Base ✅
- [ ] Home screen con pulsante "Inizia"
- [ ] Quiz screen con domande
- [ ] Results screen con punteggio
- [ ] Navigazione tra schermate (hidden/visible)

### Fase 2: Logica Quiz 🎯
- [ ] Caricare domande da array
- [ ] Mostrare una domanda alla volta
- [ ] Selezionare risposte (radio buttons)
- [ ] Pulsanti Precedente/Prossima funzionanti
- [ ] Indicatore progresso (domanda X di Y)

### Fase 3: Timer ⏱️
- [ ] Timer countdown per sezione
- [ ] Timer globale per intero quiz
- [ ] Allerta quando tempo finisce
- [ ] Salva tempo impiegato

### Fase 4: Punteggio 📊
- [ ] Controlla risposte corrette
- [ ] Calcola punteggio percentuale
- [ ] Conta domande sbagliate
- [ ] Mostra feedback per ogni errore

### Fase 5: Spiegazioni 📖
- [ ] Visualizza spiegazione per risposta sbagliata
- [ ] Mostra la risposta corretta
- [ ] Sezione "Risposte Sbagliate" nei risultati
- [ ] Categoria per ogni domanda (per studio)

### Fase 6: Persistenza 💾
- [ ] Salva best score su localStorage
- [ ] Salva tempo migliore
- [ ] Ricorda impostazioni (dark mode, etc)
- [ ] Mostra best score su home

### Fase 7: Certificato 🎓 (BONUS)
- [ ] Genera certificato come immagine Canvas
- [ ] Mostra nome e data
- [ ] Punteggio finale
- [ ] Scarica come PNG

### Fase 8: Animazioni & Polish 🎨
- [ ] Feedback visivo su risposte (verde/rosso)
- [ ] Transizioni tra schermate
- [ ] Animazioni bottoni
- [ ] Responsive mobile design

---

## 🛠️ Step Implementazione (7-10 passaggi)

### STEP 1: Setup HTML e CSS ✅
- [ ] Creare struttura HTML con 3 screen
- [ ] Stilizzare con CSS (mobile-friendly)
- [ ] Aggiungere colori (tema verde sicurezza)
- [ ] Testare su mobile

### STEP 2: Logica Base Quiz 🎯
- [ ] Creare array quizData
- [ ] Funzione per caricàre domanda
- [ ] Funzione per visualizzàre opzioni
- [ ] Navigazione base (prossima/precedente)

### STEP 3: Selezione Risposte 📝
- [ ] Implementare radio buttons per opzioni
- [ ] Event listener su click opzione
- [ ] Salvare risposta in array
- [ ] Evidenziare opzione selezionata

### STEP 4: Calcolo Punteggio 📊
- [ ] Confrontare risposte con dati corretti
- [ ] Contare domande giuste/sbagliate
- [ ] Calcolare percentuale
- [ ] Generare feedback message

### STEP 5: Timer ⏱️
- [ ] Implementare countdown timer
- [ ] Visualizzare tempo su UI
- [ ] Avvertimento tempo finisce
- [ ] Finire automaticamente se tempo scade

### STEP 6: Spiegazioni Errori 📖
- [ ] Mostrare spiegazione per risposta sbagliata
- [ ] Evidenziare risposta corretta
- [ ] Review section nei risultati
- [ ] Categorizzare domande per studio

### STEP 7: Best Score e localStorage 💾
- [ ] Salvare punteggio su localStorage
- [ ] Caricare best score da localStorage
- [ ] Mostrare su home screen
- [ ] Aggiornare se nuovo score è migliore

### STEP 8: Certificato Canvas 🎓 (BONUS)
- [ ] Creare canvas per certificato
- [ ] Disegnare template certificato
- [ ] Aggiungere nome, data, punteggio
- [ ] Pulsante download come PNG

### STEP 9: Animazioni e Feedback 🎨
- [ ] Feedback visivo risposta giusta (verde)
- [ ] Feedback visivo risposta sbagliata (rosso)
- [ ] Transizioni smooth tra schermate
- [ ] Animazione bottoni (hover effects)

### STEP 10: Testing Completo 🧪
- [ ] Testare su browser (Chrome, Firefox)
- [ ] Testare su mobile (responsivo)
- [ ] Verificare localStorage
- [ ] Edge cases (quiz vuoto, ecc)

---

## 💡 Trucchi JavaScript 🎯

### 1. Array di Oggetti per Quiz

```javascript
const quizData = [
    {
        question: "...",
        options: ["a", "b", "c", "d"],
        correct: 1,
        explanation: "...",
        category: "..."
    }
];

// Accesso
quizData[0].question  // Domanda 1
quizData[0].options[1]  // Opzione B della domanda 1
quizData[0].correct  // Indice risposta corretta
```

### 2. Timer Countdown

```javascript
let timeLeft = 60;
const timer = setInterval(() => {
    timeLeft--;
    document.getElementById('timer-display').textContent = timeLeft;

    if (timeLeft <= 0) {
        clearInterval(timer);
        finishQuiz();  // Termina quiz
    }
}, 1000);  // Aggiorna ogni 1 secondo
```

### 3. Radio Buttons e Selezione

```javascript
// HTML
<input type="radio" name="answer" value="0"> Opzione A
<input type="radio" name="answer" value="1"> Opzione B

// JavaScript
const selectedRadio = document.querySelector('input[name="answer"]:checked');
const selectedIndex = selectedRadio ? parseInt(selectedRadio.value) : -1;
```

### 4. Calcolo Punteggio

```javascript
let correctCount = 0;
for (let i = 0; i < quizData.length; i++) {
    if (userAnswers[i] === quizData[i].correct) {
        correctCount++;
    }
}
const percentage = Math.round((correctCount / quizData.length) * 100);
```

### 5. Salva e Carica localStorage

```javascript
// Salvare
const bestScore = {
    score: 85,
    date: new Date().toLocaleDateString(),
    time: '120 sec'
};
localStorage.setItem('bestScore', JSON.stringify(bestScore));

// Caricare
const loaded = JSON.parse(localStorage.getItem('bestScore'));
if (loaded) {
    console.log(loaded.score);  // 85
}
```

### 6. Generare Certificato Canvas

```javascript
const canvas = document.getElementById('certificate-canvas');
const ctx = canvas.getContext('2d');

// Sfondo
ctx.fillStyle = '#f5f5dc';  // Beige (carta)
ctx.fillRect(0, 0, canvas.width, canvas.height);

// Bordo
ctx.strokeStyle = '#DAA520';  // Oro
ctx.lineWidth = 5;
ctx.strokeRect(10, 10, canvas.width - 20, canvas.height - 20);

// Testo
ctx.fillStyle = '#000';
ctx.font = 'bold 36px Georgia';
ctx.textAlign = 'center';
ctx.fillText('Certificato di Completamento', canvas.width/2, 100);

ctx.font = '24px Georgia';
ctx.fillText(`Punteggio: ${score}%`, canvas.width/2, 300);
ctx.fillText(`Data: ${new Date().toLocaleDateString()}`, canvas.width/2, 400);
```

---

## ⚠️ Errori Comuni 🐛

### JavaScript

1. **Radio button non funziona**
   ```javascript
   ❌ const val = document.getElementById('answer').value;
      // Se multiple radio, quale prendi?

   ✅ const selected = document.querySelector('input[name="answer"]:checked');
      const val = selected ? selected.value : null;
   ```

2. **Timer continua in background**
   ```javascript
   ❌ setInterval(...);  // Mai salvato, non puoi stoparlo

   ✅ this.timerId = setInterval(...);  // Salva ID
      clearInterval(this.timerId);  // Stoppa quando serve
   ```

3. **localStorage serializzazione**
   ```javascript
   ❌ localStorage.setItem('score', {score: 85});
      // Salva "[object Object]"!

   ✅ localStorage.setItem('score', JSON.stringify({score: 85}));
   ```

4. **Punteggio calcolato male**
   ```javascript
   ❌ percentage = correctCount / totalQuestions;
      // 8/10 = 0.8, non 80!

   ✅ percentage = (correctCount / totalQuestions) * 100;
      // 8/10 = 80 (come percentuale)
   ```

### HTML/CSS

1. **Screen overlapping**
   ```css
   ❌ .screen {
        position: absolute;
        opacity: 0.5;  // Ancora visibile!
      }

   ✅ .screen.hidden {
        display: none;  /* Completamente nascoste */
      }
   ```

2. **Radio button non stilizzabili**
   ```css
   ❌ input[type="radio"] {
        width: 50px;  /* Non funziona! */
      }

   ✅ input[type="radio"] {
        transform: scale(1.5);  /* Funziona */
      }
   ```

---

## 🚀 Sfide Bonus (5 sfide avanzate)

### Sfida 1: Dark Mode Toggle ⭐

```javascript
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode',
        document.body.classList.contains('dark-mode'));
}
```

### Sfida 2: Domande Categorizzate ⭐

```javascript
function filterByCategory(category) {
    return quizData.filter(q => q.category === category);
}

// Menu per scegliere categoria
const categories = new Set(quizData.map(q => q.category));
```

### Sfida 3: Randomizzare Ordine ⭐

```javascript
function shuffleQuestions() {
    return quizData.sort(() => Math.random() - 0.5);
}

// O più affidabile:
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}
```

### Sfida 4: Statistiche Dettagliate ⭐⭐

```javascript
function getStatistics() {
    const stats = {
        totalScore: percentage,
        byCategory: {},
        timePerQuestion: totalTime / quizData.length,
        averageResponseTime: ...
    };

    for (let category of categories) {
        const qInCat = quizData.filter(q => q.category === category);
        const correctInCat = qInCat.filter(q =>
            userAnswers[quizData.indexOf(q)] === q.correct
        ).length;
        stats.byCategory[category] =
            (correctInCat / qInCat.length) * 100;
    }

    return stats;
}
```

### Sfida 5: Multi-lingua ⭐⭐

```javascript
const translations = {
    it: {
        title: "Quiz Sicurezza Elettrica",
        startBtn: "Inizia Quiz",
        nextBtn: "Prossima"
    },
    en: {
        title: "Electrical Safety Quiz",
        startBtn: "Start Quiz",
        nextBtn: "Next"
    }
};

function setLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.dataset.i18n;
        el.textContent = translations[lang][key];
    });
}
```

---

## 📚 Risorse e Link Utili 🔗

### Standard Sicurezza Internazionali
- [IEC 60417](https://webstore.iec.ch/) - Simboli elettrici
- [ISO 13849-1](https://www.iso.org/) - Sicurezza funzionale
- [ANSI C95.2](https://www.acgih.org/) - Limiti esposizione RF

### Organizzazioni Sicurezza
- [OSHA](https://www.osha.gov/) - Occupational Safety (USA)
- [INAIL](https://www.inail.it/) - Prevenzione infortuni (Italia)
- [CEI](https://www.ceiweb.it/) - Comitato Elettrotecnico Italiano

### Risorse Educative
- [NFPA 70E](https://www.nfpa.org/) - Standard sicurezza elettrica
- [IEEE 1048](https://www.ieee.org/) - Protezione personale
- [CPSC Electrical Safety](https://www.cpsc.gov/) - Consumer safety

### Letture Consigliate
1. "Electrical Safety Handbook" - NFPA
2. "Electrical Safety in the Workplace" - OSHA
3. "Industrial Electricity and Motor Controls" - Stephen Herman

---

## 📱 Mock-up Interfaccia

```
HOME SCREEN:
┌─────────────────────────────────┐
│     🛡️ Quiz Sicurezza Elettrica│
│                                 │
│  Valuta le tue conoscenze su   │
│  sicurezza in laboratorio      │
│                                 │
│        [🚀 Inizia Quiz]        │
│                                 │
│    Best Score: 92% (15/11/2025)│
└─────────────────────────────────┘

QUIZ SCREEN:
┌─────────────────────────────────┐
│ ⏱️ Tempo: 45s          1 di 20  │
├─────────────────────────────────┤
│ Quale corrente è pericolosa?    │
│                                 │
│ ○ 1 mA                          │
│ ◉ 10 mA  ← Selezionata        │
│ ○ 100 mA                        │
│ ○ 1 A                           │
│                                 │
│ [← Prec] [Pross →] [Finisci]   │
└─────────────────────────────────┘

RESULTS SCREEN:
┌─────────────────────────────────┐
│      📊 Risultati Quiz          │
│                                 │
│          ┌───────┐              │
│          │ 85%   │              │
│          └───────┘              │
│    Ottimo lavoro! 🎉            │
│                                 │
│  17 / 20 domande corrette       │
│  Tempo: 8:45                    │
│                                 │
│  ❌ Errori:                     │
│  Q5: Sbagliato (spiega...)      │
│  Q12: Sbagliato (spiega...)     │
│                                 │
│  🎓 Certificato: [Scarica]      │
│                                 │
│  [🔄 Ritenta] [🏠 Home]        │
└─────────────────────────────────┘
```

---

## 🎯 Checklist Completamento Finale

```
HTML & CSS:
[ ] index.html con 3 screen (home, quiz, results)
[ ] style.css responsive (mobile-friendly)
[ ] Timer visibile e aggiornato
[ ] Progress indicator (domanda X di Y)
[ ] Feedback colori (verde = corretto, rosso = sbagliato)

JavaScript - Dati:
[ ] Array quizData con 20-30 domande
[ ] Ogni domanda ha: question, options, correct, explanation, category
[ ] Domande copre: rischi, protezione, DPI, comportamento, primo soccorso

JavaScript - Logica:
[ ] Caricamento domande sequenziale
[ ] Selezione risposte funzionante
[ ] Navigazione Prec/Pross
[ ] Timer countdown accurato
[ ] Calcolo punteggio corretto
[ ] Spiegazioni errori visualizzate

JavaScript - Persistenza:
[ ] Best score salvato su localStorage
[ ] Best score caricato all'avvio
[ ] Mostra best score su home

JavaScript - Risultati:
[ ] Punteggio percentuale
[ ] Conteggio domande giuste
[ ] Lista errori con spiegazioni
[ ] Tempo totale impiegato
[ ] Feedback message (Scarso, Buono, Ottimo, Perfetto)

BONUS:
[ ] Certificato Canvas generato
[ ] Download certificato PNG
[ ] Dark mode toggle
[ ] Statistiche per categoria
[ ] Domande randomizzate

Testing:
[ ] Quiz completo funziona da start a results
[ ] Best score aggiornato correttamente
[ ] Mobile responsive (prova su phone)
[ ] Nessun errore console
[ ] Timer non si avvia da solo all'avvio
```

---

## 🎓 Conclusione

Hai creato un **quiz interattivo sulla sicurezza elettrica** che non solo insegna importanti conoscenze, ma salva anche i progressi e offre spiegazioni dettagliate.

La sicurezza in laboratorio è **FONDAMENTALE**. Questo quiz potrebbe salvare vite!

---

**Versione:** 1.0 | **Data:** 2025-11-21 | **Autore:** Programma TLC ITIS
