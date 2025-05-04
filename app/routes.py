from app import app
from app.generator import generate_chords
from flask import render_template


@app.route("/")
def index():
    homepage_random_chords = generate_chords(no_tab=True)
    return render_template("index.html", chords=homepage_random_chords)


@app.route("/about")
def about():
    return render_template("about.html")
