from library_manager import LibraryManager
from rich.console import Console

class Library:

    console = Console()
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.list_of_books = LibraryManager.load_library(filename)

    # Adds a book to the list of books if it doesn't already exist.
    def add_book(self, book):
        for book_in_list in self.list_of_books:
            if book_in_list.get_book_title() == book.get_book_title():
                self.console.print(f"[bold red]Book {book.get_book_title()} is already exist.")
                return
        self.list_of_books.append(book)
        self.console.print(f"[bold green]Book {book.get_book_title()} added successfully.")
        self.save_library()

    #Deletes a book from the list of books if it exists.
    def delete_book(self, book):
        for book_in_list in self.list_of_books:
            if book_in_list.get_book_title() == book.get_book_title():
                self.list_of_books.remove(book)
                self.console.print(f"[bold green]Book {book.get_book_title()} deleted successfully.")
                self.save_library()
                return
        self.console.print(f"[bold red]Book {book.get_book_title()} doesn't exist so can't delete it.")


    #Deletes all books from the library.
    def delete_library(self):
        self.list_of_books = []
        self.save_library()
        self.console.print(f"[bold green] All the books deleted successfully.")

    #Given a book title return the book object if exist.
    def find_book_according_title(self, book_title):
        for book_in_list in self.list_of_books:
            if book_in_list.get_book_title() == book_title:
                return book_in_list
        return


    def edit_book(self, book, **kwargs):
        """
           Edits the details of a book in the library.

           Args:
               book: The book object to be edited.
               **kwargs: Variable keyword arguments containing the details to be updated.
        """
        if self.list_of_books:
            for book_in_list in self.list_of_books:
                if book_in_list.get_book_title() == book.get_book_title():
                    book_in_list.update_book_details(**kwargs)
                    self.console.print(f"[bold green]Book details updated successfully.")
                    self.save_library()
                    return
            print(f"Error: Book {book.get_book_title()} not found.")
        else:
            print("Error: The library is empty.")

    # Displays the details of all books in the library.
    def display_library(self):
        if self.list_of_books:
            for book in self.list_of_books:
                book.display_book_details()
        else:
            self.console.print(f"[bold red] The library is Empty.")


    #Saves the current state of the library to a file.
    def save_library(self):
        LibraryManager.save_library(self.filename, self.list_of_books)










