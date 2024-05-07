from rich.console import Console

class Book:

    console = Console()
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    #get title book.
    def get_book_title(self):
        return self.title

    #get author book.
    def get_book_author(self):
        return self.author

    #get publication year book.
    def get_book_publication_year(self):
        return self.publication_year

    #get genre book.
    def get_book_genre(self):
        return self.genre

    #This method update the details of a book object.
    # It takes optional parameters for author, publication_year, and genre.
    # If any of these parameters are provided, the corresponding attribute of the book object is updated with the new value.
    def update_book_details(self, author=None, publication_year=None, genre=None):
        if author:
            self.author = author
        if publication_year:
            self.publication_year = publication_year
        if genre:
            self.genre = genre

    #This method display the book details: Title, Author, Publication Year, Genre.
    def display_book_details(self):
        self.console.print("Book details")
        self.console.print(f"[bold blue]Book Title: {self.get_book_title()}")
        self.console.print(f"[bold blue]Book Author: {self.get_book_author()}")
        self.console.print(f"[bold blue]Publication Year: {self.get_book_publication_year()}")
        self.console.print(f"[bold blue]Genre: {self.get_book_genre()}")

