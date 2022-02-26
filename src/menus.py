def show_main_menu() -> None:
    """
    Prints the main menu and shows the available options
    """

    options = {
        0: "Exit",
        1: "Sign in",
        2: "Login"
    }
    
    for index, option in options.items():
        print(index, option)

    print("\n\tMade by Tomas Iglesias, 2022")

def show_user_menu() -> None:
    """
    Prints user's main menu and shows the available options
    """

    options = {
        0: "Exit",
        1: "New note",
        2: "Show notes",
        3: "Delete note"
    }
    
    for index, option in options.items():
        print(index, option)
