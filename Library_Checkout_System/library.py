from book import Book


class Library(object):

    def __init__(self, sourceCollection=None):
        """    Basic __init__ method, if we decide to read a file instead of creating another one, this should
        create/read in the data to self.inventory instead of taking a source collection as input (Unless we
        have multiple libraries and allow the user to type in the file name for the __init__ method to find and
        read from in the main class).

        May have to add other methods in the future"""

        self.inventory = []
        self.length = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def returnSortedInventory(self):
        """Sort and return inventory, programmer's choice unless later specified. Multiple sort methods may be
        created"""
        pass

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
        self.inventory.append(Book(title, author, year))

    def remove(self, item):
        """Remove a book from the Library using book title"""
        for i in self.inventory:
            if item in self.inventory[i]:
                return self.inventory.pop(i)
        print("Item not found in inventory.")
        pass
