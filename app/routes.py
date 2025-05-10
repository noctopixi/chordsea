from app import app
from app.generator import generate_chords
from flask import render_template
from flask import request # Proxy representing the form


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the values of the form by the 'name' attribute and convert to int
        count = request.form.get("count", type=int)
        sets = request.form.get("sets", type=int)
        homepage_random_chords = generate_chords(count=count, sets=sets, no_tab=True)
    else:
        # Generate tabs with default values if customization form was not sent
        homepage_random_chords = generate_chords(no_tab=True)

    return render_template("index.html", chords=homepage_random_chords)


@app.route("/about")
def about():
    return render_template("about.html")
