from users.user import User
from notes.note import Note
import menus

def main() -> None:
    user_input = -1

    print("Welcome to Notepad!\n")

    #Main loop
    while user_input != 0:
        menus.show_main_menu()

        # Ask and validate option
        try:
            user_input = int(input("Please enter an option: "))

            if (user_input < 0) or (user_input > 2):
                raise ValueError
        except:
            print("Please enter a valid option")

        # Manage option
        if user_input == 1:
            try:
                print("Ok! Let's sign you into the system\n")
                
                new_user = User()
                new_user.signin()
            except:
                print("Something went wrong, please try again")
            else:
                print("Successful sign in!")

        if user_input == 2:
            try:
                email = input("\nPlease enter your email: ")
                password = input("Now your password: ")

                old_user = User(email, password)
                old_user.login()
            except:
                print("Something went wrong, please try again")
            else:
                print(f"\nWelcome back {old_user.getFirstName()}!")
                
                while user_input:
                    menus.show_user_menu()
                    # Ask and validate option
                    try:
                        user_input = int(input("\nPlease enter an option: "))

                        if (user_input < 0) or (user_input > 3):
                            raise ValueError
                    except:
                        print("Please enter a valid option")
                    else:   # Can implement with dictionary switch
                        if user_input == 0:
                            break

                        elif user_input == 1:
                            old_user.create_note()

                        elif user_input == 2:
                            old_user.show_notes()
                        
                        elif user_input == 3:
                            note_title = input("Enter the title of the note that you want delete: ")
                            note_to_delete = Note(old_user.getId(), note_title)
                            old_user.delete_note(note_to_delete)
                        
                        else:
                            print("Please enter a valid option")

    print("Goodbye!")

main()
