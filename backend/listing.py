import pickle
from opencage.geocoder import OpenCageGeocode
from backend import database
import sqlite3

openCageAPIKey = '314a7cb65c1c4dcfb675e5da37bc26bc'

def getTitle(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT title FROM listings WHERE id="+str(id))
    title = result.fetchone()[0]
    conn.close()
    return title

def getDesc(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT desc FROM listings WHERE id="+str(id))
    desc = result.fetchone()[0]
    conn.close()
    return desc

def getLocation(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT location FROM listings WHERE id="+str(id))
    location = result.fetchone()[0]
    conn.close()
    return location

def getCommitment(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT commitment FROM listings WHERE id="+str(id))
    commitment = result.fetchone()[0]
    conn.close()
    return commitment

def getPerson(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT person FROM listings WHERE id="+str(id))
    person = result.fetchone()[0]
    conn.close()
    return person

def nextID():
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT COUNT(*) FROM listings")
    id = int(result.fetchone()[0])
    conn.close()
    return id


def sortListing(num, suburb):
    ret = [
        {
            "title": "Andy needs help coding",
            "desc": "Help!",
            "location": "Randwick"
        }
    ]
    return ret

def createListing(personID = None, title = None, desc = None, commitment = None, location = None):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    id = nextID()
    print(title, desc, commitment)
    items = (str(id), title, desc, commitment, location, personID, str(-1), 0)
    cursor.execute("INSERT INTO listings VALUES (?,?,?,?,?,?,?,?)", items)
    conn.commit()
    conn.close()
