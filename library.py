class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvialbleBooks(self):
        print("Available Books : ")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the Book. Thanks You!")


class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning : ")
        self.book = input()
        return self.book


lib = Library(['Think and Grow Rich', 'Who will cry when you Die', 'For One more Day'])
cus = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice == 1:
        lib.displayAvialbleBooks()
    elif userChoice == 2:
        requestedBook = cus.requestBook()
        lib.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = cus.returnBook()
        lib.addBook(returnedBook)
    elif userChoice == 4:
        quit()