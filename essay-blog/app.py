from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
PASSWORD = "tasu5151"
ESSAYS_FILE = "essays.json"

if not os.path.exists(ESSAYS_FILE):
    with open(ESSAYS_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def index():
    with open(ESSAYS_FILE) as f:
        essays = json.load(f)
    return render_template("index.html", essays=essays)

@app.route("/essay/<int:essay_id>")
def essay(essay_id):
    with open(ESSAYS_FILE) as f:
        essays = json.load(f)
    return render_template("essay.html", essay=essays[essay_id])

@app.route("/new", methods=["GET", "POST"])
def new_essay():
    if request.method == "POST":
        password = request.form["password"]
        if password != PASSWORD:
            return "パスワードが間違っています。"
        title = request.form["title"]
        content = request.form["content"]
        with open(ESSAYS_FILE) as f:
            essays = json.load(f)
        essays.append({"title": title, "content": content})
        with open(ESSAYS_FILE, "w") as f:
            json.dump(essays, f, indent=2, ensure_ascii=False)
        return redirect(url_for("index"))
    return render_template("new.html")