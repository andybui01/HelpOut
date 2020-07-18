from backend import database

def getName(id):
    db = database.getVolunteersDatabase()
    return db[id]["name"]

def getContact(id):
    db = database.getVolunteersDatabase()
    return db[id]["contact"]

def getNumberCompleted(id):
    db = database.getVolunteersDatabase()
    sum = 0
    for listing in db[id]["listings"]:
        if listing["done"] == True:
            sum += 1
    return sum

def getBadges(id):
    db = database.getVolunteersDatabase()
    return db[id]["badges"]