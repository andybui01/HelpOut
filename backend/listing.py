from geopy.geocoders import Nominatim
from geopy import distance
from backend import database
import sqlite3


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

def sortListing(num, location):
    num = int(num)

    closeListings = []

    geolocator = Nominatim(user_agent= 'myGeocoder')

    currentLoc = geolocator.geocode(location)
    currentLoc_lat = currentLoc.latitude
    currentLoc_lng = currentLoc.longitude

    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT COUNT(*) FROM listings")
    length = int(result.fetchone()[0])


    for i in range(length):
        result = cursor.execute("SELECT location FROM listings WHERE id="+str(i))
        location = result.fetchone()[0]
        result = cursor.execute("SELECT title FROM listings WHERE id="+str(i))
        title = result.fetchone()[0]
        result = cursor.execute("SELECT desc FROM listings WHERE id="+str(i))
        desc = result.fetchone()[0]

        subCheck = geolocator.geocode(location)

        subCheck_lat = subCheck.latitude
        subCheck_lng = subCheck.longitude

        dist = distance.distance((currentLoc_lat,currentLoc_lng), (subCheck_lat,subCheck_lng)).km

        subDist = {"id": str(i), "location":location, "title":title, "desc":desc,"distance":dist}
        
        closeListings.append(subDist)

    closeListings = sorted(closeListings, key = lambda x: x['distance']) # sort by distance
    tempList = []

    conn.close()

    for i in range(num):
        tempDict = {key: closeListings[i][key] for key in closeListings[i].keys() & {'location', 'title', 'desc'}}
        tempList.append(tempDict)

    return tempList


def createListing(personID = None, title = None, desc = None, commitment = None, location = None):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    id = nextID()
    items = (str(id), title, desc, commitment, location, personID, str(-1), 0)
    cursor.execute("INSERT INTO listings VALUES (?,?,?,?,?,?,?,?)", items)
    conn.commit()
    conn.close()
