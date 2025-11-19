# Esercizio 10: Blog Letterario con Flask

## Livello: AVANZATO

## Obiettivi
- **Informatica**: Flask, SQLite, CRUD, forms, template Jinja2
- **Italiano**: Scrittura articoli letterari, critica letteraria

## Descrizione
Web app per pubblicare e gestire articoli letterari con database.

## Funzionalità
- CRUD articoli (Create, Read, Update, Delete)
- Database SQLite per persistenza
- Categorie/tag
- Sistema commenti (opzionale)
- Ricerca articoli

## Installazione
```bash
pip install Flask Flask-SQLAlchemy
```

## Struttura
```
blog/
├── app.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── articolo.html
│   └── nuovo.html
└── blog.db
```

## Consegna
Crea almeno 5 articoli su autori/opere italiane diverse.
