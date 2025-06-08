from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# File to store student data
STUDENTS_FILE = 'students.json'

# --- PostgreSQL/SQLAlchemy Setup ---
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    rollno = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    college = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the table (run once, or use Flask-Migrate for production)
@app.before_first_request
def create_tables():
    db.create_all()

def calculate_age(dob):
    today = datetime.now()
    birth_date = datetime.strptime(dob, '%Y-%m-%d')
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/students')
def students():
    return render_template('students.html')

@app.route('/register_student', methods=['POST'])
def register_student():
    name = request.form['name']
    rollno = request.form['rollno']
    dob = request.form['dob']
    email = request.form['email']
    age = calculate_age(dob)
    student = Student(
        rollno=rollno,
        name=name,
        dob=dob,
        age=age,
        college='VJIT',
        branch='AI',
        email=email
    )
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('students'))

@app.route('/search_student')
def search_student():
    rollno = request.args.get('rollno', '').strip()
    student = Student.query.filter_by(rollno=rollno).first() if rollno else None
    return render_template('students.html', student=student, search_rollno=rollno)

@app.route('/database')
def database():
    students = Student.query.all()
    return render_template('database.html', students=students)

@app.route('/delete_student', methods=['POST'])
def delete_student():
    rollno = request.form['rollno']
    student = Student.query.filter_by(rollno=rollno).first()
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('database'))

if __name__ == '__main__':
    app.run(debug=True)
