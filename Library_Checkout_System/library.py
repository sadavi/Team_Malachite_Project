from book import Book
import csv


class Library(object):

    def __init__(self, sourceCollection=None):
        """    Basic __init__ method, if we decide to read a file instead of creating another one, this should
        create/read in the data to self.inventory instead of taking a source collection as input (Unless we
        have multiple libraries and allow the user to type in the file name for the __init__ method to find and
        read from in the main class)."""

        self.inventory = []
        self.length = 0
        self.currentId = 0o00001
        self.source_file = 'library_inventory.txt'
        if sourceCollection:
            for book in sourceCollection:
                self.add(book[0], book[1], book[2])

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

    def saveInventory(self):
        """Saves the current inventory into """
        with open(self.source_file, mode='w', newline='') as save_file:
            save_writer = csv.writer(save_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            save_writer.writerow(['title', 'author', 'publish_date'])
            for book in self.inventory:
                save_writer.writerow([book[0], book[1], book[2]])

    def loadInventory(self):
        """Reset self.inventory, self.length, and self.currentId and loads the contents of source_file into inventory"""
        self.inventory = []
        self.length = 0
        self.currentId = 0o00001
        with open(self.source_file, mode='r') as library_file:
            library_reader = csv.DictReader(library_file)
            row_count = 0
            for row in library_reader:
                self.add(row["title"], row["author"], row["publish_date"])

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

    def sortedInventory(self, method):
        """ Return library in different sorting configuration depending on included method"""
        if self.isEmpty():
            return "Library is Empty"
        elif method == "title":
            return Library(sorted(self, key=lambda x: x[0]))
        elif method == "author":
            return Library(sorted(self, key=lambda x: x[1]))
        elif method == "date":
            return Library(sorted(self, key=lambda x: x[2]))
        else:
            raise Exception("Illegal argument.")

            