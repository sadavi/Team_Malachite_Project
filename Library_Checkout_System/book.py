
class Book(object):
    """Book object, sorts title, author, and publishDate of each book."""

    def __init__(self, title, author, publishDate, id):
        """__init__ function, sets class variables to input"""

        self.title = title
        self.author = author
        self.publishDate = publishDate
        self.id = id
        self.iterable = [self.title, self.author, self.publishDate, self.id]

    def __getitem__(self, x):
        """Subscript support for book objects"""
        return self.iterable[x]

    def __iter__(self):
        """Supports iteration over a view of self."""
        for cursor in self.iterable:
            yield cursor

    def __str__(self):
        """Returns each variable as a list element in a new list"""
        return f"\"{self.title}\" by {self.author} ({self.publishDate})"

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPublishDate(self):
        return self.publishDate

    def getId(self):
        return self.id
