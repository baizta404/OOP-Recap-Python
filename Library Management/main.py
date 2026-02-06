from book import Book
from library import Library
from user import User

book1 = Book('Sample re Kaka','Son of Mofiz','6251232')
book2 = Book('Ki ar korar','Kangailla Hunkirpoa','4044201')
book3 = Book('Mayer Dowa','Johntu Majhi','6969420')
book4 = Book('Egula Edit Kora Jay','Ahsan Habib Peyar','6251404')

library  = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# library.list_books()

user1 = User(1012,'Ramim','ramim@gmail.com')
user2 = User(962,'Noman','noman@gmail.com')
user3 = User(6251,'Mubin','mubin@gmail.com')

library.add_user(user1)
library.add_user(user2)
library.borrow_book('4044201',user1)
library.borrow_book('6251404',user2)
print('---------')
library.return_book('6251404',user1)
library.return_book('6251404',user2)
print('---------')
library.list_books()
library.update_user(962,'Rohoman','rohoman@mail.com')
library.update_user(1012,email='eklapothikramim@hotmail.com')
library.list_users()
library.delete_user(4201)
library.delete_user(1012)
library.list_users()