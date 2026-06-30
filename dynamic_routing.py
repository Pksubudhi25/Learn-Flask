from flask import Flask

app = Flask(__name__)

# @app.route("/hello/<name>")
# def hello(name):
#     return f"Hello {name}"

# @app.route("/square/<int:number>")
# def square(number):
#     return str(number*number) # return type must be string, dict, list, tuple with headers or status, Response instance, or WSGI callable

# @app.route("/files/<path:filename>")
# def files(filename):
#     return filename

@app.route("/")
def home():
   return "Welcome to dynamic Flask app"


@app.route("/hello/<name>")
def hello(name):
  return f"Hello {name} ! Welcome to Flask"


@app.route("/square/<int:num>")
def square(num):
  return f"Square of {num} is {num*num}"

@app.route("/profile/<name>/<int:age>")
def profile(name, age):
  return f"Name: {name}\n age:{age}"

@app.route("/calculator/<int:num1>/<int:num2>")
def calculator(num1, num2):

    if num2 == 0:
        division = "Cannot divide by zero"
    else:
        division = num1 / num2

    return (
        f"Addition: {num1 + num2}<br>"
        f"Subtraction: {num1 - num2}<br>"
        f"Multiplication: {num1 * num2}<br>"
        f"Division: {division}"
    )


if __name__ == "__main__":
    app.run(debug=True)