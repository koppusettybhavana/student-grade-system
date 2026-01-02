from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection 
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8179821404",     
    database="studentgrade_db",
    port=3307
)

cursor = db.cursor()

# Home page – show students
@app.route("/")
def home():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

# Add student
@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    subject = request.form["subject"]
    marks = request.form["marks"]
    grade = request.form["grade"]

    sql = """
    INSERT INTO students (name, subject, marks, grade)
    VALUES (%s, %s, %s, %s)
    """
    values = (name, subject, marks, grade)
    cursor.execute(sql, values)
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
