# Blog Letterario Flask - SOLUZIONE
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Articolo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titolo = db.Column(db.String(200), nullable=False)
    autore = db.Column(db.String(100))
    contenuto = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50))
    data_creazione = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Articolo {self.titolo}>'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    articoli = Articolo.query.order_by(Articolo.data_creazione.desc()).all()
    return render_template('home.html', articoli=articoli)

@app.route('/articolo/<int:id>')
def articolo(id):
    art = Articolo.query.get_or_404(id)
    return render_template('articolo.html', articolo=art)

@app.route('/nuovo', methods=['GET', 'POST'])
def nuovo():
    if request.method == 'POST':
        nuovo_art = Articolo(
            titolo=request.form['titolo'],
            autore=request.form['autore'],
            contenuto=request.form['contenuto'],
            categoria=request.form.get('categoria', 'Generale')
        )
        db.session.add(nuovo_art)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('nuovo.html')

@app.route('/elimina/<int:id>')
def elimina(id):
    art = Articolo.query.get_or_404(id)
    db.session.delete(art)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
