from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/student", methods=["GET", "POST"])
def student():

    # User opened the page
    if request.method == "GET":
        return render_template("student.html")

    # User submitted the form
    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    return render_template(
        "student_result.html",
        name=name,
        age=age,
        course=course
    )


if __name__ == "__main__":
    app.run(debug=True)