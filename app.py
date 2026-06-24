from flask import Flask, render_template, send_from_directory, abort, redirect
from markdown import markdown
from pathlib import Path
import json

app = Flask(__name__)

PAGES_DIR = Path("pages")

@app.route("/<page>")
def md(page):
    with open("links.json", "r", encoding="utf-8") as f:
        items = json.load(f)
    
    item = next((i for i in items if i["path"] == page), None)
    if item:
        return redirect(item["url"])

    file = PAGES_DIR / f"{page}.md"

    if not file.exists():
        abort(404)

    content = file.read_text(encoding="utf-8")
    title = page

    for line in content.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break

    html = markdown(
        content,
        extensions=["fenced_code", "tables"]
    )

    return render_template(
        "markdown_page.html",
        content=html,
        title=title
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route("/robots.txt")
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/socials")
def socials():
    return render_template("socials.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1313)