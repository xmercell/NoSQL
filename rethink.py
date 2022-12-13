from rethinkdb import RethinkDB
import csv
import timeit

# Connect to the RethinkDB server
r = RethinkDB()
conn = r.connect("localhost", 28015).repl()

# Load the dataset file into a Python object
with open("data.csv", "r") as f:
    # Read the CSV data using the csv.DictReader() function
    csv_data = csv.DictReader(f)

    # Convert the CSV data to a list of dictionaries
    rows = list(csv_data)

#Create a database and a table
r.db_create("test1").run(conn)
r.db("test1").table_create("my_table").run(conn)
#Insert rows into the database
r.db("test1").table("my_table").insert(rows)


def insert():
   r.db("test1").table("my_table").insert({ #existing one
        "country_code" : "AD",
        "latitude" : 42.546245,
        "longtitude" : 1.601554,
        "country" : "Andorra",
        "usa_state_code" : "AK",
        "usa_state_latitude" : 63.588753,
        "usa_state_longitude" : -154.493062,
        "usa_state" : "Alaska"
    }).run(conn)

def remove():
    r.db("test1").table("my_table").filter({"country_code" : "II",
        "latitude" : 16.23332,
        "longtitude" : 1.3232,
        "country" : "IIII",
        "usa_state_code" : "AK1",
        "usa_state_latitude" : 66.588753,
        "usa_state_longitude" : -158.493062,
        "usa_state" : "Alaska"}).delete().run(conn)

def update():
    r.db("test1").table("my_table").filter({ 
        #existing one
        "country_code" : "AD",
        "latitude" : 42.546245,
        "longtitude" : 1.601554,
        "country" : "Andorra",
        "usa_state_code" : "AK",
        "usa_state_latitude" : 63.588753,
        "usa_state_longitude" : -154.493062,
        "usa_state" : "Alaska"
    }).update({
        "country_code" : "II",
        "latitude" : 16.23332,
        "longtitude" : 1.3232,
        "country" : "IIII",
        "usa_state_code" : "AK1",
        "usa_state_latitude" : 66.588753,
        "usa_state_longitude" : -158.493062,
        "usa_state" : "Alaska"
    }).run(conn)

def list_operation():
    coll = r.db("test1").table("my_table").run(conn)
    #We can also print what list operation returned
    #for object in coll:
    #   print(object)

# Measure the execution time of an  operation
#Call here operation you want to measure insert()
# run same code 5 times to get measurable data
#n = 5
# calculate total execution time
#insert_time = timeit.timeit(stmt='list_operation()', globals=globals(), number=n)
#print(f"Execution time of insert is {insert_time / n} seconds")