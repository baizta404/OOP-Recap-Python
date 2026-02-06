class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None

        
    def __str__(self):
        status = f'Yes ,by {self.borrowed_by}' if self.is_borrowed else 'NO'
        return f'Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Borrowed: {status}'

