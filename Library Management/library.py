class Library:
    def __init__(self):
        self.books = []
        self.users = {} #{'user_id':user er object}

    def add_book(self,book):
        self.books.append(book)
        print(f'Succesfully added this "{book.title}" book to the library')

    def list_books(self):
        if not self.books:
            print('Kaka kono boi naire !')
        for book in self.books:
            print(book)

    def borrow_book(self,isbn,user):
        if user.user_id not in self.users:
            print('ete to member na,kemne boi dimu')
            return
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = user.name
                print(f'Succesfully\n {user.name} Borrowed "{book.title}" book')
                return
        print('Ayhay! Eida to nai,thakelo agei loiya laiche')

    def return_book(self,isbn,user):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed and book.borrowed_by == user.name:
                book.is_borrowed = False
                book.borrowed_by = None
                print(f'{user.name} has returned {book.title}.')
                return
        print('Kuch to garbar he doya\nhoy boi er isbn bhul naile user bhul')

    def add_user(self,user):
        if user.user_id in self.users:
            print('Ei beda ete to agei achere')
            return
        self.users[user.user_id]=user
        print(f'{user.name} added to library')
    def list_users(self):
        if not self.users:
            print('Kew nai re')
            return
        for user in self.users.values():
            print(user)
    def update_user(self,user_id,name=None,email=None):
        if user_id not in self.users:
            print('ete to naire mona!')
            return
        if name:
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
        print(f'user - {user_id} is updated!!')
    def delete_user(self,user_id):
        if user_id in self.users:
            halar_nam = self.users[user_id].name
            del self.users[user_id]
            print(f'Id: {user_id} Name: {halar_nam} removed from library')
        else:
            print('kaka halay to naire')