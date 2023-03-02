from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    
    def __init__(self):
        self.head = None
        self.total = 0
        
    def isEmpty(self):
        return self.total == 0

    def getNumberOfBooks(self):
        return self.total

    def insertBook(self, book):
        newBookNode = BookCollectionNode(book)
        previous = None
        new = self.head
        while new and book > new.getData():
            previous = new
            new = new.next
        if previous == None:
            newBookNode.setNext(self.head)
            self.head = newBookNode
        else:
            newBookNode.setNext(previous.getNext())
            previous.setNext(newBookNode)
        self.total += 1
        
    def getBooksByAuthor(self, author):
        stop = False
        string = ''
        new = self.head
        while new != None:
            if new.getData().getAuthor().lower() == author.lower():
                string += str(new.getData().getBookDetails()) + '\n'
                new = new.getNext()
            else:
                new = new.getNext()
        return string

    def getAllBooksInCollection(self):
        new = self.head
        string = ''
        while new != None:
            string += str(new.getData().getBookDetails()) + '\n'
            new = new.getNext()
        return string
        
            
    def removeAuthor(self, author):
        node = self.head
        previous = None
        while node:
            if node.getData().author.lower() == author.lower():
                if previous:
                    previous.setNext(node.getNext())
                else:
                    self.head = node.getNext()
            else:
                previous = node
            node = node.getNext()

        
    def recursiveSearchTitle(self, title, bookNode):
        if not bookNode:
            return False
        if bookNode.getData().title.lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())
        
        

        
