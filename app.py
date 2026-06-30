from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my flask course"

@app.route("/about")
def about():
    return "This website is built using Flask."

@app.route("/contact")
def contact():
    return "<h2>Contact Page</h2><p>Email: yourname@example.com</p>"

@app.route("/python")
def python():
    return "<h1>I am learning Flask!</h1>"
if __name__ == "__main__":
    app.run(debug=True)