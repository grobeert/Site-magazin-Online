"""
server.py - Lab 03 Advanced Flask

Task 01: Template inheritance cu Jinja2 (_base.html + pagini copil)
Task 02: Autentificare mock cu session Flask
Task 03: File database (database.txt) pentru date personale
Task 04: Upload poza de profil (bonus)
"""

import os
import json
from flask import (
    Flask, render_template, request,
    redirect, session, flash, send_from_directory
)
from werkzeug.utils import secure_filename

# ── Configurare aplicatie ──────────────────────────────────────────────────
# BASE_DIR = directorul unde se afla server.py, indiferent de unde e pornit
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "public"),
    static_url_path="/public",
)

# Task 02: secret_key obligatoriu pentru sesiuni Flask
# In productie foloseste un string aleator lung si secret!
app.secret_key = "schimba-asta-cu-ceva-secret-in-productie"

# ── Constante ─────────────────────────────────────────────────────────────
DATABASE_FILE = os.path.join(BASE_DIR, "database.txt")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "public", "images", "profile")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# Utilizatori mock pentru autentificare (Task 02)
# In productie: parole hash-uite + baza de date reala!
USERS = {
    "admin": "admin",
    "user":  "user",
}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ── Helper: extensie fisier permisa (Task 04) ──────────────────────────────
def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Helper: citire / scriere database.txt (Task 03) ───────────────────────
def read_db(username):
    """Citeste datele userului din database.txt (format JSON per linie)."""
    if not os.path.exists(DATABASE_FILE):
        return {}
    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                if entry.get("username") == username:
                    return entry
            except json.JSONDecodeError:
                continue
    return {}


def write_db(username, data):
    """
    Scrie / actualizeaza datele userului in database.txt.
    Fiecare linie = un obiect JSON cu datele unui utilizator.
    """
    entries = []
    # Citeste toate intrarile existente
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                    if entry.get("username") != username:
                        entries.append(entry)
                except json.JSONDecodeError:
                    continue

    # Adauga / actualizeaza intrarea curenta
    data["username"] = username
    entries.append(data)

    # Rescrie fisierul
    with open(DATABASE_FILE, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── Task 01: Pagina principala ─────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", active_page="home")


# ── Task 01: A doua pagina ────────────────────────────────────────────────
@app.route("/second")
def second_page():
    mycontent = request.args.get("mycontent", None)
    return render_template("second.html", active_page="second", mycontent=mycontent)


# ── Task 02: Login ────────────────────────────────────────────────────────
@app.route("/login", methods=["GET", "POST"])
def login():
    # Daca deja autentificat, redirectioneaza
    if session.get("authenticated"):
        return redirect("/")

    if request.method == "POST":
        # Citeste datele din formular (name="username" si name="password")
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Verifica credentialele
        if username in USERS and USERS[username] == password:
            # Seteaza sesiunea
            session["authenticated"] = True
            session["username"] = username
            flash(f"Bun venit, {username}!", "success")
            return redirect("/")
        else:
            flash("Utilizator sau parola gresita!", "danger")

    return render_template("login.html", active_page="login")


# ── Task 02: Logout ───────────────────────────────────────────────────────
@app.route("/logout")
def logout():
    username = session.get("username", "")
    # Sterge sesiunea
    session.clear()
    flash(f"La revedere, {username}!", "info")
    return redirect("/")


# ── Task 03 + 04: Detalii cont ────────────────────────────────────────────
@app.route("/account-details", methods=["GET", "POST"])
def account_details():
    # Protectie: doar utilizatori autentificati
    if not session.get("authenticated"):
        flash("Trebuie sa fii autentificat pentru a accesa aceasta pagina.", "warning")
        return redirect("/login")

    username = session["username"]

    if request.method == "POST":
        # Citeste datele din formular
        data = {
            "full_name": request.form.get("full_name", "").strip(),
            "email":     request.form.get("email", "").strip(),
            "phone":     request.form.get("phone", "").strip(),
            "bio":       request.form.get("bio", "").strip(),
        }

        # Task 04 Bonus: procesare upload poza de profil
        file = request.files.get("profile_photo")
        if file and file.filename and allowed_file(file.filename):
            # secure_filename previne path traversal attacks
            filename = secure_filename(f"{username}_{file.filename}")
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            data["profile_photo"] = filename
            flash("Poza de profil actualizata!", "success")
        else:
            # Pastreaza poza veche daca nu s-a incarcat una noua
            old_data = read_db(username)
            if "profile_photo" in old_data:
                data["profile_photo"] = old_data["profile_photo"]

        # Task 03: salveaza in database.txt
        write_db(username, data)
        flash("Datele au fost salvate cu succes!", "success")
        return redirect("/account-details")

    # GET: citeste datele existente din database.txt
    data = read_db(username)
    profile_photo = data.get("profile_photo", None)

    return render_template(
        "account-details.html",
        active_page="account",
        data=data,
        profile_photo=profile_photo
    )


# ── Task 03 din lab anterior: redirect Google ─────────────────────────────
@app.route("/google")
def google_redirect():
    return redirect("https://www.google.com")


# ── Pornire server ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Server pornit: http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)