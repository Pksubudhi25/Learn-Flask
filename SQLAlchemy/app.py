from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
# Optional: disable modification tracking to reduce overhead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Create student class that inherits db.Model
class Student(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.String(100),
        nullable = False
    )

    age = db.Column(
        db.Integer,
        nullable = False
    )

    course = db.Column(
        db.String(100),
        nullable = False
    )
    def __repr__(self):
        return (
            f"Student("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"age={self.age}, "
            f"course='{self.course}')"
        )
with app.app_context():
    db.create_all()
    Student.query.delete() # deletes previous tables
    student1 = Student(name="Pratik", age=20, course="Flask")  # type: ignore[call-arg]
    student2 = Student(name="Rahul", age=21, course="AI")# type: ignore[call-arg]
    student3 = Student(name="Alice", age=22, course="DSA")# type: ignore[call-arg]

    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)

    db.session.commit()

    students = Student.query.all()

    for student in students:
        print(student)

if __name__ == "__main__":
    app.run(debug=True)