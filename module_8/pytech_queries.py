import mysql.connector
from mysql.connector import errorcode

config={
    "user": "pysport_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db= mysql.connector.connect(**config) # connect to the pysports database 
    
    #display team records
    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams=cursor.fetchall() 
    print("-- DISPLAYING TEAM RECORDS --")
    #display team info
    for t in teams:
        print("Team ID: {} \n Team Name:{} \n Mascot: {} \n".format(t[0], t[1], t[2]))

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    players=cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")

    #display player records
    for p in players:
        print(" Player ID: {} \n First Name: {} \n Last Name: {} \n Team ID: {} \n".format(p[1], p[2], p[3]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()


