import database_conection
from notes.note import Note

database, cursor = database_conection.connect()

class User:
    """
    User object. Initializated with .. es una clase logica, contiene funciones como escribir y ver ntoas
    """

    def __init__(self, email : str ="", password : str ="" ) -> None:
        self.__first_name = ""
        self.__last_name = ""
        self.__email = email
        self.__password = password
        self.__user_id = -1

    def signin(self) -> None:
        """
        Asks user's first name, last name, email and password then inserts them
        into the database with current date
        """

        # Ask data
        self.__first_name = input("What's your first name?")
        self.__last_name = input("What's your last name?")
        self.__email = input("What's your email?")
        self.__password = input("Insert a password: ")

        # Insert new user data into database
        cursor.execute("INSERT INTO users VALUES(null, %s, %s, %s, %s, NOW())", 
        (self.__first_name, self.__last_name, self.__email, self.__password))

        # Commit database changes
        database.commit()

    def login(self) -> None:
        """
        Logins the user by email and password. If there isn't any user in the database
        with provided email and password, raises an exception

        Login a User means fill its attributes with those fetched from database
        """
        
        # Check login data
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", 
        (self.__email, self.__password))
        user = cursor.fetchone()
        
        # If user with provided email and password wasn't found, raise exception
        if not user:
            raise Exception("UnfoundUser")

        self.__user_id = user[0]
        self.__first_name = user[1]
        self.__last_name = user[2]

    def create_note(self) -> None:
        """
        Creates a note in the database. Asks the user for note's title and content
        """

        # Ask for note data
        title = input("Note title:\n")
        content = input("Note content:\n")

        # Upload note to database
        cursor.execute("INSERT INTO notes VALUES(null, %s, %s, %s, NOW())",
        (self.__user_id, title, content))

        # Commit database changes
        database.commit()

    def show_notes(self) -> None:
        """
        Fetchs all user's notes and prints them in this format:

        note_title
        note_description
        """

        # Fetch all user's notes in the database
        cursor.execute(f"SELECT * FROM notes WHERE user_id = {self.__user_id}")
        user_notes = cursor.fetchall()
         
        # I could have shown it directly from user
        print(f"{self.__first_name}, these are you notes:\n")

        for note in user_notes:
            note_ = Note(self.__user_id, note[2], note[3])
            note_.show()

    def delete_note(self, note : Note) -> None:
        """
        """

        cursor.execute(f"DELETE FROM notes WHERE user_id = {self.__user_id} AND title LIKE '%{note.getTitle()}%'")
        print(cursor.rowcount, "notes were deleted successfully\n")

        # Commit database changes
        database.commit()

    # Getters
    def getFirstName(self) -> str:
        """
        Returns user's first name
        """
        return self.__first_name

    def getLastName(self) -> str:
        """
        Returns user's last name
        """
        return self.__last_name

    def getEmail(self) -> str:
        """
        Returns user's email
        """
        return self.__email

    def getId(self) -> int:
        """
        Returns user's id
        """
        return self.__user_id

    # Setters
    def setFirstname(self, first_name: str) -> None:
        """
        Sets user's first name with received
        """
        self.__first_name = first_name

    def setLastname(self, last_name : str) -> None:
        """
        Sets user's last name with received
        """
        self.__last_name = last_name

    def setEmail(self, email : str) -> None:
        """
        Sets user's email with received
        """
        self.__email = email

    def setPassword(self, password : str) -> None:
        """
        Sets user's password with received
        """
        self.__password = password
