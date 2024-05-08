## Library Management System

This Python application is a simple library management system that allows users to perform various operations on a virtual library through the terminal. <br />
Users can add, delete, edit, display, save, or delete all books in the library.



## Features

Add Book: Add a new book to the library. <br />
Delete Book: Remove a book from the library. <br />
Edit Book: Modify the details of a book in the library. <br />
Display Library: View the details of all books in the library. <br />
Save Library: Save the current state of the library to a file. <br />
Delete All: Remove all books from the library. <br />



## Prerequisites:

Python 3.x installed on your system.

## Installation:
Clone the repository to your local machine:
```
git clone https://github.com/ghazalkhateeb/Personal-Library-Manager.git
```
Navigate to the project directory:
```
cd directory path
```

Install dependencies using pip:
```
pip install -r requirements.txt
```



## Usage:
To interact with the library management system, use the command-line interface (CLI) provided. Below are the available commands:

## Add a Book:
```
python main.py add --title "Book Title" --author "Author Name" --year "Publication Year" --genre "Book Genre"
```
## Delete a Book:
```
python main.py delete --title "Book Title"
```
## Edit a Book:
```
python main.py edit --title "Book Title" [--author "New Author Name"] [--year "New Publication Year"] [--genre "New Book Genre"]
```
## Display Library:
```
python main.py display
```

## Save Library:
```
python main.py save
```

## Delete All Books:

```
python main.py deleteall
```


## Contributing
Contributions are welcome! If you encounter any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.



