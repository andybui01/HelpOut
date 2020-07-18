from backend import database

def getName(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM volunteers WHERE id="+str(id))
    name = result.fetchone()[0]
    conn.close()
    return name

def getContact(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT contact FROM volunteers WHERE id="+str(id))
    contact = result.fetchone()[0]
    conn.close()
    return contact 

def getNumberCompleted(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT completed FROM volunteers WHERE id="+str(id))
    num = result.fetchone()[0]
    conn.close()
    return num

def getBadges(id):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    kindness = cursor.execute("SELECT kindness, speed, diligence FROM volunteers WHERE id="+str(id))
    kindness, speed, diligence = result.fetchall()
    conn.close()
    return kindness[0] + speed[0] + diligence[0]

def createVolunteer(id, name, contact):
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    id = nextID()
    items = (str(id), name, contact, 0, 0, 0, 0)
    cursor.execute("INSERT INTO volunteers VALUES (?,?,?,?,?,?,?)", items)
    conn.commit()
    conn.close()

def nextID():
    conn = sqlite3.connect('helpout.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT COUNT(*) FROM volunteers")
    id = int(result.fetchone()[0])
    conn.close()
    return id