from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    context = {
        "name": "Anant adwaya",
        "age" : 25,
        "hobbies": ["coding", "reading", ],
        "skills": ["Python", "Django", "JavaScript"],
        "education": {
            "degree": "Bachelor of Technology",
            "field": "Computer Science",
            "institution": "PTU University",
            "year": 2020
        },
        "experience": [
            {"company": "ABC Corp.", "position": "Software Engineer", "duration": "3 years"},
            {"company": "XYZ Inc.", "position": "Senior Software Engineer", "duration": "2 years"},
        ],
        "today" : datetime.now(),
        "is_active": True,
        "is_admin": False,
        "is_authenticated": True,
    }
    return render(request,"index.html", context)

