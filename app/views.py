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
    # all_records = GeneralInfo.objects.all()      # ORM is a programing languagetechnique that allows devlopers to interact with 
    # for i in all_records:                        # the database using the programming language's syntax instead of SQL queries.
    #     print(i.company_name, i.location, i.email, i.phone, i.open_hours)
                                       
    # first_record = GeneralInfo.objects.first()  # Fetch the first record from the GeneralInfo model
    # print(first_record)

    # last_record = GeneralInfo.objects.last()    # Fetch the last record from the GeneralInfo model
    # print(last_record)

    # first_five__record = GeneralInfo.objects.all()[:5]  # Fetch the first five records from the GeneralInfo model
    # print(first_five__record)

    # last_five__record = GeneralInfo.objects.all().order_by('-id')[:5]  # Fetch the first five records from the GeneralInfo model
    # print(last_five__record)

    # hk_record = GeneralInfo.objects.filter(location = "hk")  # Fetch the first 21 records from the GeneralInfo model
    # print(hk_record)

    
    # delete

    # GeneralInfo.objects.filter(location="hk").delete()  # Delete records where location is "hk"
    # print("Records deleted successfully")

    

    # update

    # imacctz = GeneralInfo.objects.get(company_name="imacctz")  # Fetch the record with company_name "imacctz"
    # imacctz.location = "India"  # Update the location to "India"
    # imacctz.save()  # Save the changes to the database
    

    # generalInfo = GeneralInfo.objects.all().update(phone = "99999999")  # Fetch all records from the GeneralInfo mode
    
    #create

    GeneralInfo.objects.create(
        company_name="Samsung",
        location="South Korea",
        email="example@gmail.com",
        phone="1234567890",
        open_hours="9 AM - 5 PM",
        video_url="https://www.youtube.com/watch?v=example",
        twitter_url="https://twitter.com/example",
        facebook_url="https://facebook.com/example",
        instagram_url="https://instagram.com/example",
        linkedin_url="https://linkedin.com/in/example"
    )  # Create a new record in the GeneralInfo model


    
    file_path = 'sql_queries.txt'
    write_sql_quarys_to_file(file_path)  # Write SQL queries to a file

    context = {}
    return render(request,"index.html", context)

