import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def showplayers(cursor):
    #Retreves player records
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players=cursor.fetchall()
    
    for p in players:
        print(" Player ID: {} \n First Name: {} \n Last Name: {} \n Team ID: {} \n".format(p[0], p[1], p[2], p[3]))

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #insert player
    add_player = ("INSERT INTO player(first_name, last_name, team_id)" "Values(%s,%s,%s)")

    #player data
    player_data = ("Smeagol", "Shire Folk", 1)

    #inserts player record
    cursor.execute(add_player, player_data)

    #commit insert
    db.commit()

    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    #display player records
    showplayers(cursor)

    #update
    update_player =("UPDATE player SET team_id =2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(update_player)
    print("-- DISPLAYING PLAYERS AFTER UPDATE --")
    showplayers(cursor)

    #delete
    delete_player =("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)
    print("-- DISPLAYING PLAYERS AFTER DELETE--")
    showplayers(cursor)


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
