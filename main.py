from library import Library
from book import Book
import argparse
from rich.console import Console

def main():
    library = Library()
    console = Console()
    parser = argparse.ArgumentParser(description="Library System")
    parser.add_argument("action", choices=["add", "delete", "edit", "display", "save", "deleteall"],
                        help="Action to perform")
    parser.add_argument("--title", help="Title of the book")
    parser.add_argument("--author", help="Author of the book")
    parser.add_argument("--year", help="Publication year of the book")
    parser.add_argument("--genre", help="Genre of the book")
    args = parser.parse_args()

    if args.action == "add":
        if args.title and args.author and args.year and args.genre:
            book = Book(args.title, args.author, args.year, args.genre)
            library.add_book(book)
        else:
            console.print("[bold red]Parameters of the book is required for adding.")

    elif args.action == "delete":
        if args.title:
            current_book = library.find_book_according_title(args.title)
            if(current_book):
                library.delete_book(current_book)
            else:
                console.print(f"[bold red]Book {args.title} doesn't exist so can't delete it.")
        else:
            console.print("[bold red]Title of the book is required for deleting.")


    elif args.action == "deleteall":
        library.delete_library()

    elif args.action == "edit":
        if args.title:
            current_book = library.find_book_according_title(args.title)
            if current_book:
                #Create a dictionary to store the parameters to be edited.
                edit_params = {}
                if args.author:
                    edit_params['author'] = args.author
                if args.year:
                    edit_params['publication_year'] = args.year
                if args.genre:
                    edit_params['genre'] = args.genre

                #Check if there are parameters to edit.
                if edit_params:
                    library.edit_book(current_book, **edit_params)
                else:
                    console.print("[bold yellow]No parameters provided to edit.")
            else:
                console.print(f"[bold red]Book {args.title} doesn't exist so can't edit it.")
        else:
            console.print("[bold red]Title of the book is required for editing.")


    elif args.action == "display":
        library.display_library()

    elif args.action == "save":
        library.save_library()


if __name__ == "__main__":
    main()
