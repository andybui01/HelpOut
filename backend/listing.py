import pickle
from opencage.geocoder import OpenCageGeocoder
from backend import database

openCageAPIKey = '314a7cb65c1c4dcfb675e5da37bc26bc'

def getTitle(id):
    database = database.readListingsDatabase()
    return database[id]['Title']

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
    geocoder = OpenCageGeocode(openCageAPIKey)

    currentuburb = str(db[id]['Location'])
    currentLoc = geocoder.geocode(suburb)
    currentLoc_lat = currentLoc[0]['geometry']['lat']
    currentLoc_lng = currentLoc[0]['geometry']['lng']

    for listing in db:
        suburb = str(db[listing]['Location'])  
        subCheck = geocoder.geocode(suburb, countrycode = au)

        subCheck_lat = subCheck[0]['geometry']['lat']
        subCheck_lng = subCheck[0]['geometry']['lng']

        distance = geodesic((currentLoc_lat,currentLoc_lng), (subCheck_lat,subCheck_lng)).kilometers

        listing = (suburb, distance)
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

