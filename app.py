from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

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