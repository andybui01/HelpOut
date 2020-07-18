import sqlite3

def readListingsDatabase():
    conn = sqlite3.connect('helpout.db')
    return db

def dumpDatabase(data):
    db = open('ListingDatabase.p', 'wb')
    pickle.dump(data, 'ListingDatabase.p')
    db.close()
    

