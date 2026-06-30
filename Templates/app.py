from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<name>/<int:age>/<city>")
def profile(name, age, city):
    return render_template("profile.html", name=name, age=age, city=city)

if __name__ == "__main__":
    app.run(debug=True)