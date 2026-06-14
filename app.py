from flask import Flask, render_template, send_from_directory, abort
from pathlib import Path
from markdown import markdown

app = Flask(__name__)

PAGES_DIR = Path("pages")

@app.route("/<page>")
def wiki(page):
    file = PAGES_DIR / f"{page}.md"

    if not file.exists():
        abort(404)

    html = markdown(
        file.read_text(encoding="utf-8")
    )

    html = f'<div class="markdown-content">{html}</div>'

    return render_template("markdown_page.html", content=html)

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