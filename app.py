from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os
import chromadb
from chromadb.config import Settings

app = Flask(__name__)

# File to store student data
STUDENTS_FILE = 'students.json'

# --- ChromaDB Setup ---
chroma_client = chromadb.Client(Settings(
    persist_directory="chromadb_data"
))

STUDENT_COLLECTION = 'students'

def get_student_collection():
    return chroma_client.get_or_create_collection(STUDENT_COLLECTION)

def add_student_chroma(student):
    col = get_student_collection()
    col.add(
        ids=[student['rollno']],
        documents=[json.dumps(student)],
        metadatas=[student]
    )

def get_all_students_chroma():
    col = get_student_collection()
    results = col.get(include=['metadatas'])
    return results['metadatas'] if 'metadatas' in results else []

def delete_student_chroma(rollno):
    col = get_student_collection()
    col.delete(ids=[rollno])

def load_students():
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_students(students):
    with open(STUDENTS_FILE, 'w') as f:
        json.dump(students, f, indent=4)

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
    student = {
        'name': name,
        'rollno': rollno,
        'dob': dob,
        'age': age,
        'college': 'VJIT',
        'branch': 'AI',
        'email': email
    }
    add_student_chroma(student)
    return redirect(url_for('students'))

@app.route('/search_student')
def search_student():
    rollno = request.args.get('rollno', '').strip()
    col = get_student_collection()
    student = None
    if rollno:
        results = col.get(ids=[rollno], include=['metadatas'])
        if results['metadatas'] and len(results['metadatas']) > 0:
            student = results['metadatas'][0]
    return render_template('students.html', student=student, search_rollno=rollno)

@app.route('/database')
def database():
    students = get_all_students_chroma()
    return render_template('database.html', students=students)

@app.route('/delete_student', methods=['POST'])
def delete_student():
    rollno = request.form['rollno']
    delete_student_chroma(rollno)
    return redirect(url_for('database'))

if __name__ == '__main__':
    app.run(debug=True)
