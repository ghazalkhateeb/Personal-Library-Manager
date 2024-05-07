import json
from book import Book

class LibraryManager:

    #This method loads the library from a file specified by filename.
    def load_library(filename):
        try:
            #Open the file in read mode ("r").
            with open(filename, "r") as file:
                data = json.load(file)
                list_of_books = []
                for book_data in data:
                    # Create a Book object from the book data.
                    book = Book(**book_data)
                    # Append the Book object to the list of books.
                    list_of_books.append(book)
            return list_of_books
        except FileNotFoundError:
            return []

    # This method takes two arguments: filename, specifying the file to which the library will be saved.
    # And list_of_books, containing the list of books to be saved.
    def save_library(filename, list_of_books):
        data = [vars(book) for book in list_of_books]
        #Open the file in write mode ("w").
        with open(filename, "w") as file:
            #This line writes the data list to the file in JSON format with an indentation level of 5 spaces.
            json.dump(data, file, indent=5)




