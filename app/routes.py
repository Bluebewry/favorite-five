from app import app
from flask import render_template

@app.route("/index.html")
def homePage():
    welcome = "welcome to the homepage"
    text = "sending this from python"
    return render_template('index.html', welcome = welcome, my_text = text)

@app.route("/favfive.html")
def favfivePage():
    fav = ["BTS", "Pierce the veil", "DPR Ian", "Twice", "Deftones"]
    m = "Dont judge me for my music lol"
    return render_template('favfive.html', fav = fav, m = m)

