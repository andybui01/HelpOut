import pickle

def readListingsDatabase():
    db = open('ListingDatabase.p', 'r')
    return db

def dumpDatabase(data):
    db = open('ListingDatabase.p', 'w')
    pickle.dump(data, 'ListingDatabase.p')
    db.close()
    

