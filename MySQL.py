import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='robotics',
    db='MyApp',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

def makeSQL ( branch=0 , tablenum=0, userID='1', userPass='None', userName='None' ) :
    # Select a table
    if ( tablenum == 0 ) :
        table = 'account_name'
    if ( tablenum == 1 ) :
        table = 'account_pass'

    # Create a SQL
    if ( branch == 0 ): # Select
        sql = "SELECT * FROM " + table + " WHERE ID=" + userID +";"

    if ( branch == 1 ): # Insert
        if ( userName != 'None' ) :
            sql = "INSERT INTO "   + table + " (ID,name) VALUES (" + userID + " " + userName + ");"
        if ( userPass != 'None' ) :
            sql = "INSERT INTO "   + table + " (ID,pass) VALUES (" + userID + " " + userPass + ");"

    if ( branch == 2 ): # Update
        if ( userPass != 'None' ) :
            sql = "UPDATE " + table + " SET pass=" + userPass + " WHERE ID=" + useID + ";"

    print ( "sql : ", sql )
    return ( sql )

def useSQL  ( sql ) :
    cursor.execute ( sql )
    result = cursor.fetchone()

    if ( str(result) != 'None' ) :
        print ( result )
    else :
        print ( "No data" )



if __name__ == "__main__" :
    cursor = connection.cursor()

#    while ( ) :
    userID = "1"
    #makeSQL ( branch=0 , tablenum=0, userID='1', userPass='None', userName='None' ) :
    sql = makeSQL ( 0, 1, userID )
    useSQL ( sql )

    cursor.close ()
    connection.close()

