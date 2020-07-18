import sqlite3

def getName(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM persons WHERE id="+str(id))
    name = result.fetchone()[0]
    conn.close()
    return name

def getContact(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT contact FROM persons WHERE id="+str(id))
    contact = result.fetchone()[0]
    conn.close()
    return contact

def getListings(id):
    """
    Returns a list of Listings
    Args:
        id - The customer ID of the person to match them with their listings
    """
    listOfListings = []
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    rowData = cursor.execute(f"SELECT (*) FROM listings where {id} = person")
    rowDataResult = rowData.fetchall()
    
    for row in rowDataResult:
        dictOfListings = {"ID" : row[0], "Title": row[1], "Description" : row[2], "Done" : row[7]}
        listOfListings.append(dictOfListings)
    conn.close()
    return listOfListings

