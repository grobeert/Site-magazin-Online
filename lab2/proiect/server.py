"""
server.py - Aplicatie Flask pentru laboratorul de web design

Task 03:
  - Serveste fisiere statice din /public/ (imaginile, CSS-ul)
  - Ruta "/" serveste initial_design.html prin render_template
  - Ruta "/google" redirectioneaza catre Google

Task 04:
  - Ruta "/second" serveste second.html cu variabila dinamica "mycontent"
    preluata din parametrii GET ai cererii
  - Exemplu: http://localhost:5000/second?mycontent=Salut+Lume
"""

from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)


# ----------------------------------------------------------------
# Task 03: servire fisiere statice din directorul "public/"
# Aceasta e necesara pentru CSS, imagini etc.
# Flask serveste automat din /static/, dar proiectul foloseste /public/
# ----------------------------------------------------------------
@app.route('/public/<path:filename>')
def public_files(filename):
    return send_from_directory('public', filename)


# ----------------------------------------------------------------
# Task 03: pagina principala - servita cu render_template
# ----------------------------------------------------------------
@app.route('/')
def index():
    return render_template('initial_design.html')


# ----------------------------------------------------------------
# Task 04: a doua pagina - cu continut dinamic prin Jinja
# Acceseaza: http://localhost:5000/second?mycontent=Mesajul+tau
# ----------------------------------------------------------------
@app.route('/second')
def second_page():
    # request.args.get("mycontent", "<not specified>") citeste
    # parametrul GET "mycontent" din URL; daca lipseste, returneaza "<not specified>"
    mycontent = request.args.get("mycontent", "<not specified>")
    return render_template("second.html", mycontent=mycontent)


# ----------------------------------------------------------------
# Task 03: ruta /google - redirectioneaza catre motorul de cautare
# ----------------------------------------------------------------
@app.route('/google')
def google_redirect():
    return redirect("https://www.google.com")


# ----------------------------------------------------------------
# Pornire server
# ----------------------------------------------------------------
if __name__ == '__main__':
    print("Serverul ruleaza pe http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)
