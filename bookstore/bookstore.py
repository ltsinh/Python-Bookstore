class Bookstore(object):
    def __init__(self,storeName): #Initialize a method, there are 2 parameters listed
        self.name = storeName  #self is available to method, takes value stored .name and stores it in the variable storeName
        self.books = [] #Creates a new list books
    
    
    def add_book(self,book): #Initialize a method, there are 2 parameters listed
        self.books.append(book) #extends list of book
        
            
    def get_books(self): #Initialize method with 1 parameter
        return self.books 


    def search_books(self, title=None, author=None): #Initialize method and set title author to none, total 3 parameters
        new_list = []
        for book in self.books:
            if book.author == author:
                new_list.append(book)
            elif book.title == title:
               new_list.append(book)
            elif title and book.title.lower().startswith(title.lower()):
                new_list.append(book) #extends list of book
        return new_list


class Author(object):
    def __init__(self,name,nation): #Initialize a method, there are 3 parameters listed
        self.name = name #self is available to method, takes value stored .name and stores it in the variable name
        self.nationality = nation  #self is available to method, takes value store .nationality and stores it in the variable name nation
        self.books = [] #extends list of books
    
    def get_books(self): #Initialize method with 1 parameter
        return self.books 


class Book(object):
    def __init__(self,title,author): #Initialize a method, there are 3 parameters listed
        self.title = title  #self is available to method, takes value stored .title and stores it in the variable title
        self.author = author #self is available to method, takes value store .author and stores it in the variable name author
        author.books.append(self) #extends list of book