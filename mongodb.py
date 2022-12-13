from pymongo import MongoClient
import csv
import timeit

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

with open("data.csv", "r") as f:
    # Read the CSV data using the csv.DictReader() function
    csv_data = csv.DictReader(f)

    # Convert the CSV data to a list of dictionaries
    rows = list(csv_data)

def insert():
     collection.insert_one({
        "country_code" : "AD",
        "latitude" : 42.546245,
        "longtitude" : 1.601554,
        "country" : "Andorra",
        "usa_state_code" : "AK",
        "usa_state_latitude" : 63.588753,
        "usa_state_longitude" : -154.493062,
        "usa_state" : "Alaska"
    })

def remove():
    collection.find_one_and_delete({
        "country_code" : "II",
        "latitude" : 16.23332,
        "longtitude" : 1.3232,
        "country" : "IIII",
        "usa_state_code" : "AK1",
        "usa_state_latitude" : 66.588753,
        "usa_state_longitude" : -158.493062,
        "usa_state" : "Alaska"
    })

def update():
    collection.update_one({
        "country_code" : "AD",
        "latitude" : 42.546245,
        "longtitude" : 1.601554,
        "country" : "Andorra",
        "usa_state_code" : "AK",
        "usa_state_latitude" : 63.588753,
        "usa_state_longitude" : -154.493062,
        "usa_state" : "Alaska"
    },
    {"$set" : {
        "country_code" : "II",
        "latitude" : 16.23332,
        "longtitude" : 1.3232,
        "country" : "IIII",
        "usa_state_code" : "AK1",
        "usa_state_latitude" : 66.588753,
        "usa_state_longitude" : -158.493062,
        "usa_state" : "Alaska"
    }})

def list_operation():
    coll = collection.find({})
    #We can also print them
    #for object in coll:
    #    print(object)

#n = 5
# Call here operation which you want to measure etc. insert()
# calculate total execution time
#change operation in stmt
#insert_time = timeit.timeit(stmt='list_operation()', globals=globals(), number=n)
# calculate the execution time
#print(f"Execution time of operation is {insert_time / n} seconds")