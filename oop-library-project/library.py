class Library:

    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def book_clean(self,book):
        return book.strip().lower()
    
    def add_book(self,*books):
            for book in books:
                if self.book_clean(book):
                    if self.book_clean(book) not in self.books:
                        self.books.append(self.book_clean(book))
                        self.no_of_books += 1
                        print(f'{book} added to the library.')
                    else:
                        print(f'{book} is already in the library.')
                else:
                    print('Empty book cannot be added.')
        

    def discard_book(self,*books):
        for book in books:
            if self.book_clean(book) not in self.books:
                print(f'{book} not in the library.')
            else:
                self.books.remove(self.book_clean(book))
                self.no_of_books -= 1
                print(f'{book} removed from the library.')

    # def check(self):
    #     return len(self.books) == self.no_of_books

    def view_books(self):
        if not self.books:
            print("Library is currently empty.")
        else:
            for i,book in enumerate(sorted(self.books),1):
                print(f'{i}.) {book.title()}')
    
    def total_books(self):
        print(f'Total books:{self.no_of_books}')

    def search_book(self,*books):
        for book in books:
            if self.book_clean(book) in self.books:
                print(f'{book} is in the library.')
            else:
                print(f'{book} is not in the library.')
                
        
# ----------------------------
# 🔍 Sample Test Calls Below:
# ----------------------------

a = Library()
a.add_book('The Psychology of Money','Rich Dad Poor Dad')
a.view_books()

a.discard_book('The Psychology of Money')
a.view_books()

a.add_book(
    'The Art of Seduction',
    '48 Laws of Power',
    'The Psychology of Money',
    'How to Win Friends and Influence People'
)
a.view_books()

a.total_books()

a.search_book('The Psychology of Money')
a.search_book('Atomic Habits') 

a.add_book('') # Trying to add an empty book