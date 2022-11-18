from book import Book


class Library(object):

    def __init__(self, sourceCollection=None):
        """    Basic __init__ method, if we decide to read a file instead of creating another one, this should
        create/read in the data to self.inventory instead of taking a source collection as input (Unless we
        have multiple libraries and allow the user to type in the file name for the __init__ method to find and
        read from in the main class)."""

        self.inventory = []
        self.length = 0
        self.currentId = 0o00001
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def returnSortedInventory(self):
        """Sort and return inventory, programmer's choice unless later specified. Multiple sort methods may be
        created"""
        pass

    def isEmpty(self):
        return self.length == 0

    def __len__(self):
        """To avoid having to use self.inventory.length every time."""
        return self.length

    def __str__(self):
        """Allows for printing the Library"""
        return "{" + "\n".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        for cursor in self.inventory:
            yield cursor

    def add(self, title, author, year):
        """Add a book item to the Library"""
        self.inventory.append(Book(title, author, year, self.newId()))
        self.length += 1

    def remove(self, item):
        """Removes a book from the Library using book title, library must not be empty"""
        if not self.isEmpty():
            for i in range(0, self.length):
                if item == self.inventory[i][0]:
                    print("Removed " + str(self.inventory[i]))
                    self.inventory.pop(i)
                    self.length -= 1
                    return

            print("Book not found in inventory.")
        else:
            print("Library empty, cannot remove book.")

    def newId(self):
        """Returns a unique ID"""
        yield self.currentId
        self.currentId += 1

    def getId(self, title):
        """Finds a book by title and returns the book's ID. Library must not be empty"""
        if not self.isEmpty():
            for i in range(0, self.length):
                if title in self.inventory[i][0]:
                    return self.inventory[i].getId

            print("Book not found in inventory.")
        else:
            print("Library empty, cannot retrieve book ID.")

    def getIndex(self, title):
        """Finds a book by title and returns the book's index. Library must not be empty"""
        if not self.isEmpty():
            for i in range(0, self.length):
                if title in self.inventory[i][0]:
                    return i

            print("Book not found in inventory.")
        else:
            print("Library empty, cannot retrieve book ID.")
