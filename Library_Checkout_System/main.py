import library


def main():
    """
    Asks user for different command options to perform
    with the Library object.
    """
    print("Welcome to the virtual library.")

    lib = library.Library()

    running = True
    while running:
        print("[0] Exit")
        print("[1] View Library")
        print("[2] Add book")
        print("[3] Remove book")
        print("[4] Search in the library")
        print("[5] Load library from file")
        print("[6] Save library to file")
        print("[7] Clear the library")

        entry = input("\nWhat would you like to do? ")

        if entry == '0':    # Exit the program
            running = False
        elif entry == '1':  # View the inventory
            viewLib(lib)
        elif entry == '2':  # Add book to the library
            addBook(lib)
        elif entry == '3':  # Remove book from library
            removeBook(lib)
        elif entry == '4':  # Search book in the library
            searchBook(lib)
        elif entry == '5':  # Load library from file
            print("Loading file...")
            lib.loadInventory()
        elif entry == '6':  # Save library to file
            print("Saving file...")
            lib.saveInventory()
        elif entry == '7':  # Clear library
            clearLibrary(lib)
        else:
            print("Incorrect input, try again.")

    print("Closing the program.")


def viewLib(lib):
    """ Display library sorted by user choice """
    while True:
        print("[1] By Title")
        print("[2] By Author")
        print("[3] By Publish year")

        entry = input("\nHow would like it to be sorted? ")

        if entry == "1":
            print(lib.sortedInventory("title"))
        elif entry == "2":
            print(lib.sortedInventory("author"))
        elif entry == "3":
            print(lib.sortedInventory("date"))
        else:
            print("Wrong input")
            next
        break


def addBook(lib):
    """ Adds a book to the library """
    title = input("Title: ")
    author = input("Author: ")

    while True:
        try:
            year = int(input("Publish Year: "))
            break
        except:
            print("Input must be a number. Please try again")

    lib.add(title, author, year)


def removeBook(lib):
    """ Removes a book to the library """
    item = input("Enter the book title you wish to remove\n")
    lib.remove(item)


def searchBook(lib):
    """ Searches for a book based on the given substring in the library """
    entry = input("Type out the text to search for in the title\n").lower()
    result = lib.findAll(entry)

    if len(result) == 0:
        print("Nothing was found.")

    for item in lib.findAll(entry):
        print(item)


def clearLibrary(lib):
    """ Clears out the library """
    entry = input("Are you sure you want to clear the library? [y/n]\n")

    while True:
        if entry.lower() == 'y':
            lib.clearLibrary()
            return
        elif entry.lower() == 'n':
            print("Canceling...")
            return
        else:
            print("Wrong input")


main()
