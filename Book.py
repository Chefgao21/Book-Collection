class Book:

    def __init__(self, title = '', author = '', year = None):
        self.year = year
        self.title = title
        self.author = author

    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getYear(self):
        return self.year

    def getBookDetails(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

    def __gt__(self, other):
        self.key = (self.author, self.year, self.title)
        other.key = (other.author, other.year, other.title)
        return self.key > other.key





    
        
        
        

        
