import mysql.connector

def connect() -> tuple:
    """
    
    """
    database = mysql.connector.connect(
        host="localhost",
        user="mroot",
        passwd="Pass!1234",
        database="notepad",
        port=3306 
    )

    cursor = database.cursor(buffered=True)

    return database, cursor
    