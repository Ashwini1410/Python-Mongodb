from cgitb import lookup
from dis import pretty_flags
from pymongo import MongoClient
from datetime import datetime
import pprint

client = MongoClient()
db = client.javatpoint 


def insertdata():    
    employee = {"id": "101",  
    "name": "Peter",  
    "profession": "Software Engineer",  
    }
    employees = db.employees 
    employees.insert_one(employee)  
    pprint.pprint(employees.find_one())

def insertmany():
    mylist = [
    {"id": "102","name": "Ashwini","profession": "Software Engineer",},
    {"id": "103","name": "Abhijit","profession": "Operation Manager",},
    {"id": "104","name": "Anamica","profession": "Export Officer",},
    {"id": "105","name": "Archana","profession": "Civil Engineer",},]
    employees = db.employees
    print("1")
    employees.insert_many(mylist)
    print("2")
    pprint.pprint(employees.find())

def findqueryforall():
    Collection = db.employees
    cursor = Collection.find()   
    print("The data having Quantity greater than 40 is:")
    for record in cursor:
        print(record)

def findqueryforone():
    Collection = db.employees
    cursor = Collection.find({"id":"105"})
    print("The data having Quantity greater than 40 is:")
    for record in cursor:
        print(record)

def andoperator():
    Collection = db.employees
    cursor = Collection.find({ "$and": [{"name": "Archana"}, {"profession": "Civil Engineer"}]})
    print("andoperator:")
    for record in cursor:
        print(record)
    

def sortoperator():
    Collection = db.employees
    cursor = Collection.find().sort("name")
    ##({ "$and": [{"name": "Archana"}, {"profession": "Civil Engineer"}]})
    print("andoperator:")
    for record in cursor:
        print(record)

def limitoperator():
    Collection = db.employees
    cursor = Collection.find().limit(5)
    ##({ "$and": [{"name": "Archana"}, {"profession": "Civil Engineer"}]})
    print("limitoperator:")
    for record in cursor:
        print(record)

def lookupoperator():#as equal as join
    mylist = [
    {"id": "102","name": "Ashwini","profession": "Software Engineer","desgname" : "Senior",},
    {"id": "103","name": "Abhijit","profession": "Operation Manager","desgname" : "Senior",},
    {"id": "104","name": "Anamica","profession": "Export Officer","desgname" : "Senior",},
    {"id": "105","name": "Archana","profession": "Civil Engineer","desgname" : "Senior",},]

    print("1")
    desglist = {"desgid": "1","desgname": "Senior","location":"Mumbai",}
    print("22")

    designation = db.designation 
    designation.insert_one(desglist)
    pprint.pprint(designation.find_one())

    employees = db.employees    
    employees.insert_many(mylist)
    print("t1")   
    pprint.pprint(employees.find_one())

    print("start")
    cursor = employees.aggregate( [
    {
     "$lookup":
       {
        'from': "employees",
        'localField': "desgname",
        'foreignField': "desgname",
        'as': "Designation"
       }
    }
    ] )

    for record in cursor:
        print(record)

    # employees.aggregate([{
    #     "$lookup":{
    #         "from" : "designation",
    #         "localField" : "desgid",
    #         "foreignField" : "desgid",
    #         "as" : "Designation"

    #     }
    # }])   

def sortoperator():
    #1 for asc -1 desc
    employees = db.employees    
    cursor = employees.find().sort("name",-1)
    for record in cursor:
        print(record)

# def timeoperator():    
#     employees = db.gender
#     gender = [    
#     {"id":"productid","sequence_value":0,"gender":"Female"},
#     {"id":"productid","sequence_value":0,"gender":"Male"},]  
#     print("test")
#     cursor = employees.insert_one(gender)
#     for record in cursor:
#         print(record)

# db.timetest.insertOne( { ts: new Timestamp() } );

# def sequenceoperator():    
#     employees = db.gender
#     gender = [    
#     {"id":"productid","sequence_value":0,"gender":"Female"},
#     {"id":"productid","sequence_value":0,"gender":"Male"},]  
#     print("test")
#     cursor = employees.insert_one(gender)
#     for record in cursor:
#         print(record)

def insertdesignation():
    print("designation")
    col = db.designation
    cur = col.find()
    results = list(cur)
    now = datetime.now()
    #curdate=datetime.strptime(datetime.now(), "%d/%m/%Y")#datetime.now()
    curdate=now.strftime("%d/%m/%Y")
    if len(results)==0:
        print(len(results))
        desglist = {"desgid": "1","desgname": "Senior","createdon":curdate,}
    else:
        print("els")
        curs = db.designation.count_documents({})
        curs=curs+1        
        #db.designation.find().sort( [("desgid", -1)] ).limit(1)
        print(curs)
        desglist = {"desgid": curs,"desgname": "Ast Manager","createdon":curdate,}

    print(desglist)
    designation = db.designation 
    designation.insert_one(desglist)
    pprint.pprint(designation.find_one())



print("Hello World")
#insertmany()
#insertdata()
#findquery()
#andoperator()
#sortoperator()
#limitoperator()
#lookupoperator()
#sortoperator()
#sequenceoperator() not tested
insertdesignation()
