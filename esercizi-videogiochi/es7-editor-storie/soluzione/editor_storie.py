# 📝 EDITOR DI STORIE INTERATTIVE - SOLUZIONE
# Crea storie senza programmare!

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import json
from typing import Dict, List

class EditorStorie:
    """Editor completo per storie interattive"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("📝 Editor Storie Interattive")
        self.root.geometry("1100x750")

        # Dati della storia
        self.storia = {
            "titolo": "La Mia Storia",
            "autore": "",
            "descrizione": "",
            "scena_iniziale": "inizio",
            "scene": {
                "inizio": {
                    "testo": "Scrivi qui l'inizio della tua storia...",
                    "scelte": []
                }
            }
        }

        self.scena_corrente_id = "inizio"
        self.widgets_scelte = []

        self.crea_interfaccia()
        self.carica_scena("inizio")

    def crea_interfaccia(self):
        """Crea l'interfaccia grafica"""

        # === MENU BAR ===
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="💾 Salva", command=self.salva_storia)
        file_menu.add_command(label="📂 Carica", command=self.carica_storia)
        file_menu.add_separator()
        file_menu.add_command(label="🌐 Esporta HTML", command=self.export_html)
        file_menu.add_separator()
        file_menu.add_command(label="❌ Esci", command=self.root.quit)

        test_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Test", menu=test_menu)
        test_menu.add_command(label="▶️ Testa Storia", command=self.testa_storia)
        test_menu.add_command(label="✅ Valida", command=self.valida_storia)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="?", menu=help_menu)
        help_menu.add_command(label="ℹ️ Info", command=self.mostra_info)

        # === FRAME PRINCIPALE ===
        # Diviso in 3 colonne: sidebar sinistra, editor centrale, info destra

        # SIDEBAR SINISTRA: Lista scene
        frame_sinistra = tk.Frame(self.root, width=200, bg="#2c3e50", relief=tk.RIDGE, borderwidth=2)
        frame_sinistra.pack(side=tk.LEFT, fill=tk.BOTH)
        frame_sinistra.pack_propagate(False)

        tk.Label(frame_sinistra, text="📚 SCENE", font=("Arial", 14, "bold"),
                bg="#2c3e50", fg="white").pack(pady=10)

        # Lista scene
        self.lista_scene = tk.Listbox(frame_sinistra, bg="#34495e", fg="white",
                                     font=("Courier", 11), selectbackground="#3498db")
        self.lista_scene.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.lista_scene.bind('<<ListboxSelect>>', self.on_scena_selezionata)

        # Bottoni scene
        tk.Button(frame_sinistra, text="➕ Nuova Scena", bg="#27ae60", fg="white",
                 command=self.nuova_scena, font=("Arial", 10, "bold")).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(frame_sinistra, text="🗑️ Elimina Scena", bg="#e74c3c", fg="white",
                 command=self.elimina_scena, font=("Arial", 10, "bold")).pack(fill=tk.X, padx=10, pady=5)

        # FRAME CENTRALE: Editor
        frame_centrale = tk.Frame(self.root, bg="#ecf0f1")
        frame_centrale.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Header
        header = tk.Frame(frame_centrale, bg="#3498db", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(header, text="📖 INFORMAZIONI STORIA", font=("Arial", 14, "bold"),
                bg="#3498db", fg="white").pack(pady=5)

        # Info storia
        info_frame = tk.Frame(frame_centrale, bg="#ecf0f1")
        info_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(info_frame, text="Titolo:", bg="#ecf0f1").grid(row=0, column=0, sticky="w", padx=5)
        self.entry_titolo = tk.Entry(info_frame, font=("Arial", 12), width=30)
        self.entry_titolo.grid(row=0, column=1, padx=5, pady=2)
        self.entry_titolo.insert(0, self.storia['titolo'])
        self.entry_titolo.bind('<KeyRelease>', lambda e: self.aggiorna_titolo())

        tk.Label(info_frame, text="Autore:", bg="#ecf0f1").grid(row=0, column=2, sticky="w", padx=5)
        self.entry_autore = tk.Entry(info_frame, font=("Arial", 12), width=20)
        self.entry_autore.grid(row=0, column=3, padx=5, pady=2)
        self.entry_autore.insert(0, self.storia.get('autore', ''))

        # Separatore
        ttk.Separator(frame_centrale, orient='horizontal').pack(fill=tk.X, pady=10)

        # Editor scena
        tk.Label(frame_centrale, text="✏️ EDITOR SCENA", font=("Arial", 14, "bold"),
                bg="#ecf0f1").pack(pady=5)

        # ID Scena
        id_frame = tk.Frame(frame_centrale, bg="#ecf0f1")
        id_frame.pack(fill=tk.X, padx=10)

        tk.Label(id_frame, text="ID Scena:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        self.entry_id_scena = tk.Entry(id_frame, font=("Courier", 11), width=25)
        self.entry_id_scena.pack(side=tk.LEFT, padx=10)
        tk.Button(id_frame, text="✏️ Rinomina", command=self.rinomina_scena).pack(side=tk.LEFT)

        # Checkbox finale
        self.var_finale = tk.BooleanVar()
        tk.Checkbutton(id_frame, text="Scena Finale", variable=self.var_finale,
                      bg="#ecf0f1").pack(side=tk.LEFT, padx=20)

        # Testo scena
        tk.Label(frame_centrale, text="Testo della scena:", bg="#ecf0f1",
                font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(10, 0))

        self.text_scena = scrolledtext.ScrolledText(frame_centrale, height=8,
                                                    font=("Arial", 11), wrap=tk.WORD)
        self.text_scena.pack(fill=tk.BOTH, padx=10, pady=5, expand=False)

        # Scelte
        tk.Label(frame_centrale, text="🔀 SCELTE (opzioni per il lettore):",
                font=("Arial", 12, "bold"), bg="#ecf0f1").pack(anchor="w", padx=10, pady=(10, 5))

        # Frame scrollabile per scelte
        scelte_container = tk.Frame(frame_centrale, bg="#ecf0f1")
        scelte_container.pack(fill=tk.BOTH, expand=True, padx=10)

        canvas = tk.Canvas(scelte_container, bg="#ecf0f1")
        scrollbar = tk.Scrollbar(scelte_container, orient="vertical", command=canvas.yview)
        self.frame_scelte = tk.Frame(canvas, bg="#ecf0f1")

        self.frame_scelte.bind("<Configure>",
                              lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.frame_scelte, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bottone aggiungi scelta
        tk.Button(frame_centrale, text="➕ Aggiungi Scelta", bg="#9b59b6", fg="white",
                 font=("Arial", 10, "bold"), command=self.aggiungi_scelta).pack(pady=10)

        # Bottone salva scena
        tk.Button(frame_centrale, text="💾 Salva Modifiche Scena", bg="#16a085", fg="white",
                 font=("Arial", 12, "bold"), command=self.salva_scena_corrente).pack(pady=5)

        # SIDEBAR DESTRA: Info
        frame_destra = tk.Frame(self.root, width=250, bg="#ecf0f1", relief=tk.RIDGE, borderwidth=2)
        frame_destra.pack(side=tk.RIGHT, fill=tk.BOTH)
        frame_destra.pack_propagate(False)

        tk.Label(frame_destra, text="ℹ️ INFO", font=("Arial", 14, "bold"),
                bg="#ecf0f1").pack(pady=10)

        info_text = scrolledtext.ScrolledText(frame_destra, wrap=tk.WORD,
                                              font=("Arial", 9), bg="#f9f9f9")
        info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        info_text.insert("1.0", """
📚 GUIDA RAPIDA

1. SCENE
   - Ogni storia è composta da scene
   - Ogni scena ha un ID univoco
   - Usa ID chiari (es: "bosco", "castello")

2. SCELTE
   - Aggiungi scelte per rendere la storia interattiva
   - Ogni scelta porta a una nuova scena
   - Le scene finali non hanno scelte

3. WORKFLOW
   a) Crea nuova scena (➕)
   b) Scrivi il testo
   c) Aggiungi scelte
   d) Collega ad altre scene
   e) Salva modifiche
   f) Testa la storia (▶️)

4. VALIDAZIONE
   - Controlla che tutte le scene siano raggiungibili
   - Verifica i collegamenti
   - Test → Valida

5. EXPORT
   - Salva in JSON per condividere
   - Esporta in HTML per giocare nel browser

💡 TIP: Disegna prima la mappa della tua storia su carta!
        """)
        info_text.config(state="disabled")

        self.aggiorna_lista_scene()

    def aggiorna_lista_scene(self):
        """Aggiorna la lista delle scene nella sidebar"""
        self.lista_scene.delete(0, tk.END)
        for scena_id in self.storia['scene'].keys():
            # Evidenzia scena iniziale
            if scena_id == self.storia.get('scena_iniziale', 'inizio'):
                self.lista_scene.insert(tk.END, f"🏠 {scena_id}")
            else:
                self.lista_scene.insert(tk.END, f"   {scena_id}")

    def nuova_scena(self):
        """Crea una nuova scena"""
        # Chiedi ID
        dialogo = tk.Toplevel(self.root)
        dialogo.title("Nuova Scena")
        dialogo.geometry("400x150")

        tk.Label(dialogo, text="ID della nuova scena:", font=("Arial", 11)).pack(pady=10)
        entry = tk.Entry(dialogo, font=("Arial", 12), width=25)
        entry.pack(pady=5)
        entry.focus()

        def crea():
            id_scena = entry.get().strip().replace(' ', '_').lower()
            if not id_scena:
                messagebox.showwarning("Errore", "Inserisci un ID!")
                return
            if id_scena in self.storia['scene']:
                messagebox.showwarning("Errore", "ID già esistente!")
                return

            self.storia['scene'][id_scena] = {
                "testo": "Scrivi qui il testo della scena...",
                "scelte": []
            }
            self.aggiorna_lista_scene()
            dialogo.destroy()
            self.carica_scena(id_scena)

        tk.Button(dialogo, text="Crea", bg="#27ae60", fg="white",
                 font=("Arial", 11, "bold"), command=crea).pack(pady=10)
        entry.bind('<Return>', lambda e: crea())

    def elimina_scena(self):
        """Elimina la scena corrente"""
        if len(self.storia['scene']) <= 1:
            messagebox.showwarning("Errore", "Non puoi eliminare l'unica scena!")
            return

        if self.scena_corrente_id == self.storia.get('scena_iniziale'):
            messagebox.showwarning("Errore", "Non puoi eliminare la scena iniziale!")
            return

        risposta = messagebox.askyesno("Conferma",
                                      f"Eliminare la scena '{self.scena_corrente_id}'?")
        if risposta:
            del self.storia['scene'][self.scena_corrente_id]
            self.aggiorna_lista_scene()
            self.carica_scena(list(self.storia['scene'].keys())[0])

    def on_scena_selezionata(self, event):
        """Quando si seleziona una scena dalla lista"""
        selezione = self.lista_scene.curselection()
        if selezione:
            # Salva scena corrente prima
            self.salva_scena_corrente()

            # Carica nuova scena
            testo = self.lista_scene.get(selezione[0])
            scena_id = testo.replace('🏠 ', '').strip()
            self.carica_scena(scena_id)

    def carica_scena(self, scena_id):
        """Carica una scena nell'editor"""
        if scena_id not in self.storia['scene']:
            return

        self.scena_corrente_id = scena_id
        scena = self.storia['scene'][scena_id]

        # Carica dati
        self.entry_id_scena.delete(0, tk.END)
        self.entry_id_scena.insert(0, scena_id)

        self.text_scena.delete("1.0", tk.END)
        self.text_scena.insert("1.0", scena['testo'])

        self.var_finale.set(scena.get('tipo') == 'finale')

        # Carica scelte
        for widget in self.widgets_scelte:
            widget.destroy()
        self.widgets_scelte.clear()

        for scelta in scena.get('scelte', []):
            self.aggiungi_scelta_widget(scelta['testo'], scelta.get('prossima_scena', ''))

        # Evidenzia nella lista
        for i, item in enumerate(self.lista_scene.get(0, tk.END)):
            if scena_id in item:
                self.lista_scene.selection_clear(0, tk.END)
                self.lista_scene.selection_set(i)
                break

    def aggiungi_scelta(self):
        """Aggiungi una nuova scelta vuota"""
        self.aggiungi_scelta_widget("", "")

    def aggiungi_scelta_widget(self, testo="", destinazione=""):
        """Aggiunge un widget scelta"""
        frame = tk.Frame(self.frame_scelte, relief=tk.GROOVE, borderwidth=2, bg="white")
        frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(frame, text="Testo:", bg="white", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        entry_testo = tk.Entry(frame, width=40, font=("Arial", 10))
        entry_testo.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        entry_testo.insert(0, testo)

        tk.Label(frame, text="→ Scena:", bg="white", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # Combobox per scegliere scena
        combo = ttk.Combobox(frame, values=list(self.storia['scene'].keys()),
                            width=25, font=("Courier", 10))
        combo.grid(row=1, column=1, padx=5, pady=5)
        if destinazione:
            combo.set(destinazione)

        tk.Button(frame, text="❌", bg="#e74c3c", fg="white",
                 command=lambda: self.rimuovi_scelta(frame)).grid(row=0, column=3, rowspan=2, padx=5)

        self.widgets_scelte.append((frame, entry_testo, combo))

    def rimuovi_scelta(self, frame):
        """Rimuovi una scelta"""
        for i, (f, _, _) in enumerate(self.widgets_scelte):
            if f == frame:
                self.widgets_scelte.pop(i)
                frame.destroy()
                break

    def salva_scena_corrente(self):
        """Salva le modifiche alla scena corrente"""
        if not self.scena_corrente_id:
            return

        # Salva testo
        self.storia['scene'][self.scena_corrente_id]['testo'] = self.text_scena.get("1.0", tk.END).strip()

        # Salva tipo
        if self.var_finale.get():
            self.storia['scene'][self.scena_corrente_id]['tipo'] = 'finale'
        elif 'tipo' in self.storia['scene'][self.scena_corrente_id]:
            del self.storia['scene'][self.scena_corrente_id]['tipo']

        # Salva scelte
        scelte = []
        for _, entry_testo, combo in self.widgets_scelte:
            testo = entry_testo.get().strip()
            dest = combo.get().strip()
            if testo and dest:
                scelte.append({
                    "testo": testo,
                    "prossima_scena": dest
                })

        self.storia['scene'][self.scena_corrente_id]['scelte'] = scelte

    def rinomina_scena(self):
        """Rinomina la scena corrente"""
        nuovo_id = self.entry_id_scena.get().strip().replace(' ', '_').lower()

        if not nuovo_id:
            messagebox.showwarning("Errore", "Inserisci un ID valido!")
            return

        if nuovo_id == self.scena_corrente_id:
            return

        if nuovo_id in self.storia['scene']:
            messagebox.showwarning("Errore", "ID già esistente!")
            return

        # Salva scena con nuovo ID
        self.storia['scene'][nuovo_id] = self.storia['scene'][self.scena_corrente_id]
        del self.storia['scene'][self.scena_corrente_id]

        # Aggiorna riferimenti in tutte le scelte
        for scena in self.storia['scene'].values():
            for scelta in scena.get('scelte', []):
                if scelta.get('prossima_scena') == self.scena_corrente_id:
                    scelta['prossima_scena'] = nuovo_id

        # Aggiorna scena iniziale se necessario
        if self.storia.get('scena_iniziale') == self.scena_corrente_id:
            self.storia['scena_iniziale'] = nuovo_id

        self.scena_corrente_id = nuovo_id
        self.aggiorna_lista_scene()
        messagebox.showinfo("Successo", f"Scena rinominata in '{nuovo_id}'")

    def aggiorna_titolo(self):
        """Aggiorna titolo storia"""
        self.storia['titolo'] = self.entry_titolo.get()

    def salva_storia(self):
        """Salva la storia in JSON"""
        self.salva_scena_corrente()
        self.storia['autore'] = self.entry_autore.get()

        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Salva Storia"
        )

        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.storia, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Successo", f"Storia salvata in:\n{filename}")

    def carica_storia(self):
        """Carica una storia da JSON"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Carica Storia"
        )

        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    self.storia = json.load(f)

                self.entry_titolo.delete(0, tk.END)
                self.entry_titolo.insert(0, self.storia.get('titolo', ''))

                self.entry_autore.delete(0, tk.END)
                self.entry_autore.insert(0, self.storia.get('autore', ''))

                self.aggiorna_lista_scene()
                self.carica_scena(self.storia.get('scena_iniziale', list(self.storia['scene'].keys())[0]))

                messagebox.showinfo("Successo", "Storia caricata!")
            except Exception as e:
                messagebox.showerror("Errore", f"Errore nel caricamento:\n{str(e)}")

    def valida_storia(self):
        """Valida la struttura della storia"""
        self.salva_scena_corrente()
        errori = []

        # Controlla scena iniziale
        scena_iniz = self.storia.get('scena_iniziale', 'inizio')
        if scena_iniz not in self.storia['scene']:
            errori.append(f"❌ Scena iniziale '{scena_iniz}' non esiste!")

        # Controlla collegamenti
        for scena_id, scena in self.storia['scene'].items():
            for scelta in scena.get('scelte', []):
                dest = scelta.get('prossima_scena')
                if dest and dest not in self.storia['scene']:
                    errori.append(f"❌ '{scena_id}' → '{dest}' inesistente!")

        # Controlla scene irraggiungibili
        raggiungibili = set()

        def trova(scena_id):
            if scena_id in raggiungibili or scena_id not in self.storia['scene']:
                return
            raggiungibili.add(scena_id)
            for scelta in self.storia['scene'][scena_id].get('scelte', []):
                if 'prossima_scena' in scelta:
                    trova(scelta['prossima_scena'])

        trova(scena_iniz)

        irraggiungibili = set(self.storia['scene'].keys()) - raggiungibili
        if irraggiungibili:
            errori.append(f"⚠️ Scene irraggiungibili: {', '.join(irraggiungibili)}")

        # Mostra risultato
        if errori:
            messagebox.showwarning("Validazione",
                                  f"Trovati {len(errori)} problemi:\n\n" + "\n".join(errori))
        else:
            messagebox.showinfo("Validazione", "✅ Storia valida! Nessun errore trovato!")

    def testa_storia(self):
        """Apre il player in una nuova finestra"""
        self.salva_scena_corrente()

        # Crea finestra player
        player_window = tk.Toplevel(self.root)
        player = StoryPlayerGUI(player_window, self.storia)

    def export_html(self):
        """Esporta la storia come HTML"""
        self.salva_scena_corrente()

        filename = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")],
            title="Esporta HTML"
        )

        if filename:
            html_content = self.genera_html()
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            messagebox.showinfo("Successo", f"Storia esportata in HTML:\n{filename}")

    def genera_html(self):
        """Genera codice HTML per la storia"""
        storia_json = json.dumps(self.storia, ensure_ascii=False)

        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{self.storia['titolo']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 700px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        #container {{
            background: rgba(0,0,0,0.7);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        h1 {{ text-align: center; color: #ffd700; }}
        #testo {{
            font-size: 18px;
            line-height: 1.8;
            margin: 30px 0;
            padding: 20px;
            background: rgba(255,255,255,0.1);
            border-left: 4px solid #ffd700;
            border-radius: 5px;
        }}
        button {{
            display: block;
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            font-size: 16px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }}
        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }}
        #info {{
            text-align: center;
            color: #ccc;
            font-size: 14px;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div id="container">
        <h1>{self.storia['titolo']}</h1>
        <div id="info">di {self.storia.get('autore', 'Autore Sconosciuto')}</div>
        <div id="testo"></div>
        <div id="scelte"></div>
    </div>

    <script>
    const storia = {storia_json};
    let scenaCorrente = '{self.storia.get("scena_iniziale", "inizio")}';

    function mostraScena() {{
        const scena = storia.scene[scenaCorrente];
        if (!scena) {{
            document.getElementById('testo').innerHTML = '❌ Scena non trovata!';
            return;
        }}

        document.getElementById('testo').innerHTML = scena.testo;
        const divScelte = document.getElementById('scelte');
        divScelte.innerHTML = '';

        // Controlla se è finale
        if (scena.tipo === 'finale') {{
            divScelte.innerHTML = '<div style="text-align:center; margin-top:30px; font-size:24px;">🏁 FINE 🏁</div>';
            return;
        }}

        scena.scelte.forEach(scelta => {{
            const btn = document.createElement('button');
            btn.textContent = scelta.testo;
            btn.onclick = () => {{
                scenaCorrente = scelta.prossima_scena;
                mostraScena();
            }};
            divScelte.appendChild(btn);
        }});
    }}

    mostraScena();
    </script>
</body>
</html>"""
        return html

    def mostra_info(self):
        """Mostra informazioni sull'editor"""
        messagebox.showinfo("Info", """
📝 Editor Storie Interattive v1.0

Creato per il progetto UDA Italiano-Informatica

Funzionalità:
• Editor visuale per storie interattive
• Salvataggio/caricamento JSON
• Validazione automatica
• Export HTML
• Player integrato

© 2024
        """)

    def run(self):
        """Avvia l'editor"""
        self.root.mainloop()


class StoryPlayerGUI:
    """Player GUI per testare le storie"""

    def __init__(self, root, storia):
        self.root = root
        self.storia = storia
        self.scena_corrente = storia.get('scena_iniziale', 'inizio')

        self.root.title(f"▶️ {storia['titolo']}")
        self.root.geometry("700x500")

        self.crea_interfaccia()
        self.mostra_scena()

    def crea_interfaccia(self):
        # Titolo
        tk.Label(self.root, text=self.storia['titolo'],
                font=("Arial", 20, "bold")).pack(pady=20)

        # Testo scena
        self.text_scena = scrolledtext.ScrolledText(self.root, height=12,
                                                    font=("Arial", 12), wrap=tk.WORD)
        self.text_scena.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)

        # Frame scelte
        self.frame_scelte = tk.Frame(self.root)
        self.frame_scelte.pack(fill=tk.X, padx=20, pady=10)

    def mostra_scena(self):
        """Mostra la scena corrente"""
        if self.scena_corrente not in self.storia['scene']:
            messagebox.showerror("Errore", f"Scena '{self.scena_corrente}' non trovata!")
            return

        scena = self.storia['scene'][self.scena_corrente]

        # Mostra testo
        self.text_scena.config(state="normal")
        self.text_scena.delete("1.0", tk.END)
        self.text_scena.insert("1.0", scena['testo'])
        self.text_scena.config(state="disabled")

        # Rimuovi vecchie scelte
        for widget in self.frame_scelte.winfo_children():
            widget.destroy()

        # Controlla se è finale
        if scena.get('tipo') == 'finale':
            tk.Label(self.frame_scelte, text="🏁 FINE DELLA STORIA 🏁",
                    font=("Arial", 18, "bold")).pack(pady=20)
            return

        # Mostra scelte
        for scelta in scena.get('scelte', []):
            btn = tk.Button(self.frame_scelte, text=scelta['testo'],
                          font=("Arial", 11), bg="#3498db", fg="white",
                          command=lambda s=scelta: self.scegli(s))
            btn.pack(fill=tk.X, pady=5)

    def scegli(self, scelta):
        """Gestisci una scelta"""
        self.scena_corrente = scelta['prossima_scena']
        self.mostra_scena()


if __name__ == "__main__":
    editor = EditorStorie()
    editor.run()
