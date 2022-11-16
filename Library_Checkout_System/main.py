import library

# Question for next meeting: Is the library object going to be stored in a file outside the program and read into
# the program on launch, or are we going to create a new blank Library object every time we launch the program?


def main():
    """
    Asks user for different command options to perform
    with the Library object.
    """
    print("Welcome to the virtual library.")

    # TODO: possibly change to loading a file instead of creating a blank one.
    lib = library.Library()

    # TODO: Implement each option in the interface
    running = True
    while running:
        print("[0] Exit")
        print("[1] View Library")
        print("[2] Add book")
        print("[3] Remove book")

        entry = input("\nWhat would you like to do? ")

        if entry == '0':    # Exit the program
            running = False
        elif entry == '1':  # View the inventory
            print(lib)
        elif entry == '2':  # Add book to the library
            title = input("Title: ")
            author = input("Author: ")
            # TODO: add data validity check for a published year
            year = int(input("Publish Year: "))

            lib.add(title, author, year)
        elif entry == '3':  # Remove book from library
            pass
        else:
            print("Incorrect input, try again.")

    print("Closing the program.")


main()
