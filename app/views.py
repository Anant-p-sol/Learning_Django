from django.shortcuts import render
from app.models import GeneralInfo
from django.db import connection

def write_sql_quarys_to_file(file_path):
    with open('sql_queries.txt', 'w') as file:
        queries = connection.queries
        for query in queries:
            sql = query['sql']
            file.write(f"{sql}\n")

# Create your views here.

def index(request): 
    #read                                        # ORM (Object-Relational Mapping) to fetch data from the database
    all_records = GeneralInfo.objects.all()      # ORM is a programing languagetechnique that allows devlopers to interact with 
    for i in all_records:                        # the database using the programming language's syntax instead of SQL queries.
        print(i.company_name, i.location, i.email, i.phone, i.open_hours)
                                       
    first_record = GeneralInfo.objects.first()  # Fetch the first record from the GeneralInfo model
    print(first_record)

    last_record = GeneralInfo.objects.last()    # Fetch the last record from the GeneralInfo model
    print(last_record)

    file_path = 'sql_queries.txt'
    write_sql_quarys_to_file(file_path)  # Write SQL queries to a file

    context = {}
    return render(request,"index.html", context)

