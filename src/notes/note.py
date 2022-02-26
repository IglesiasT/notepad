class Note:
    """
    clase contenedora de datos, no tiene funciones logicas
    """

    def __init__(self, user_id : int, title : str, content : str ="") -> None:
        self.__user_id = user_id
        self.__title = title
        self.__content = content

    def show(self):
        """
        Prints note's content below its title
        """
        
        print(f"{self.__title}:\n{self.__content}\n")

    # Getters
    def getTitle(self) -> str:
        """
        Returns note's title
        """

        return self.__title
