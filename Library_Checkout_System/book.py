

class Book(object):
    """Book object, srotes title, author, and publishDate of each book."""

    def __init__(self, title, author, publishDate):
        """__init__ function, sets class variables to input"""

        self.title = title
        self.author = author
        self.publishDate = publishDate

    def __str__(self):
        """Returns each variable as a list element in a new list"""
        return f"\"{self.title}\" by {self.author} ({self.publishDate})"