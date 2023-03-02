from Book import *
from BookCollection import *
from BookCollectionNode import *

b = Book("new book", "Gao, Edwin", 2022)
a = Book("all good", "Chang, Tim", 2020)

d = BookCollection()
d.insertBook(b)
d.insertBook(a)


def test__lab05():
    assert b.getTitle() == "new book"
    assert a.getTitle() == "all good"
    assert b.getAuthor() == "Gao, Edwin"
    assert a.getAuthor() == "Chang, Tim"
    assert b.getYear() == 2022
    assert a.getYear() == 2020
    assert b.getBookDetails() == 'Title: new book, Author: Gao, Edwin, Year: 2022'
    assert a.getBookDetails() == 'Title: all good, Author: Chang, Tim, Year: 2020'
    assert b.__gt__(a) == True
    assert a.__gt__(b) == False


    assert d.isEmpty() == False
    assert d.getNumberOfBooks() == 2
    assert d.recursiveSearchTitle("new book", d.head) == True
    assert d.recursiveSearchTitle("New", d.head) == False
    assert d.getBooksByAuthor("Boinpally, Srijit") == ''

def test__lab05a():
    e = BookCollectionNode(Book("new book", "Gao, Edwin", 2022))
    e.setNext(Book("all good", "Chang, Tim", 2020))
    assert e.getData().getYear() == 2022
    assert e.getData().getTitle() == "new book"
    f = BookCollectionNode(None)
    f.setData(Book("new book", "Gao, Edwin", 2022))
    assert f.getData().getAuthor() == "Gao, Edwin"


    


