import pickle
from backend import database
from geopy.geocoders import Nominatim
from geopy import distance

openCageAPIKey = '314a7cb65c1c4dcfb675e5da37bc26bc'

def getTitle(id):
    db = database.readListingsDatabase()
    return db[id]['Title']

def getDesc(id):
    db = database.readListingsDatabase()
    return db[id]['Description']

def getLocation(id):
    db = database.readListingsDatabase()
    return db[id]['Location']

def getCommitment(id):
    db = database.readListingsDatabase()
    return db[id]['Commitment']

def getPerson(id):
    db = database.readListingsDatabase()
    return db[id]['Person']

def createID(database):
    id = len(database) - 1
    return id


def sortListing(id):
    closeListings = []

    db = database.readListingsDatabase()
    geolocator = Nominatim(user_agent = 'myGeocoder')

    currentsuburb = str(db[id]['Location'])
    currentLoc = geolocator.geocode(currentsuburb)
    currentLoc_lat = currentLoc.latitude
    currentLoc_lng = currentLoc.longitude

    for listing in db:
        suburb = str(db[listing]['Location'])  

        location = geolocator.geocode(suburb)

        subCheck_lat = location.latitude
        subCheck_lng = location.longitude

        dist = distance.distance((currentLoc_lat,currentLoc_lng), (subCheck_lat,subCheck_lng)).kilometers

        listing = (suburb, dist)
        closeListings.append(listing)

    closeListings = closeListings.sort(key = lambda x: x[1]) # sort by distance
    tempList = []

    for i in range(len(closeListings)):
        tempList.append(closeListings[i][1])

    return tempList


def createListing(title = None, desc = None, commitment = None, location = None):
    db = database.readListingsDatabase()
    info = {
        "title": title,
        "desc": desc,
        "commitment": commitment,
        "location": location
    }
    id = createID(database)
    db[id] = info
    database.dumpDatabase(db)

