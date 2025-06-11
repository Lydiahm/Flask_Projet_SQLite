from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

DB_PATH = 'database.db'  # ✅ Constante unique pour le chemin de la base

def get_connection():
    return sqlite3.connect(DB_PATH)

def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # ⚠️ TODO: remplacer par une authentification sécurisée (hash/password config)
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['authentifie'] = True
            return redirect(url_for('lecture'))
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def read_fiche(post_id):  # ✅ nom de fonction conforme PEP8
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
        data = cursor.fetchall()
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def read_bdd():  # ✅ nom de fonction conforme
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clients')
        data = cursor.fetchall()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)',
            (1002938, nom, prenom, "ICI")
        )
        conn.commit()
    return redirect('/consultation/')

if __name__ == "__main__":
    app.run(debug=True)
