# NOTE: This file is deprecated. Student data is now managed by ChromaDB.
import json
from datetime import datetime, timedelta
import random

# Student data
students = {
    "22911A3532": {
        "name": "Malkedi Ashwitha",
        "rollno": "22911A3532",
        "dob": "2004-05-15",  # Example DOB
        "age": 19,
        "college": "VJIT",
        "branch": "AI",
        "email": "ashwitha.malkedi@vjit.ac.in"
    },
    "22911A3515": {
        "name": "DHUGYALA RUCHITHA",
        "rollno": "22911A3515",
        "dob": "2004-03-20",  # Example DOB
        "age": 19,
        "college": "VJIT",
        "branch": "AI",
        "email": "ruchitha.dhugyala@vjit.ac.in"
    },
    "22911A3512": {
        "name": "DASARI LITHIN GOUD",
        "rollno": "22911A3512",
        "dob": "2004-07-10",  # Example DOB
        "age": 19,
        "college": "VJIT",
        "branch": "AI",
        "email": "lithin.dasari@vjit.ac.in"
    },
    "22911A3506": {
        "name": "BURRA SUKESH GOUD",
        "rollno": "22911A3506",
        "dob": "2004-02-28",  # Example DOB
        "age": 19,
        "college": "VJIT",
        "branch": "AI",
        "email": "sukesh.burra@vjit.ac.in"
    },
    "22911A3535": {
        "name": "MARAVONI SATHISH",
        "rollno": "22911A3535",
        "dob": "2004-09-05",  # Example DOB
        "age": 19,
        "college": "VJIT",
        "branch": "AI",
        "email": "sathish.maravoni@vjit.ac.in"
    },
    "22911A3551": {
        "name": "RAGIRI SRINU",
        "rollno": "22911A3551",
        "dob": "2004-11-15",  # Example DOB
        "age": 19,
        "college": "VJIT",
        "branch": "AI",
        "email": "srinu.ragiri@vjit.ac.in"
    }
}

# Save to JSON file
with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)

print("Student database initialized successfully!") 