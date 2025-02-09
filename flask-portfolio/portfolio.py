from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/resume")
def resume():
    return render_template("resume.html", title="Resume")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
