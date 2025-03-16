from fastapi import  FastAPI



app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

#API endpoint to fetch all books
@app.get('/books')
async def get_all_books():
    return BOOKS


#API endpoint to fetch specific book by title
@app.get('/books/{book_title}')
async def get_book_by_title(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {'message' : 'book not found'}

#API endpoint 

@app.get('/books/')
async def get_book_by_category(category:str):
    BOOKS_TO_RETURN = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            BOOKS_TO_RETURN.append(book)
    if len(BOOKS_TO_RETURN) == 0:
        return {'message' : 'no book found'}
    else:
        return BOOKS_TO_RETURN
    

#API endpoint to get books by author (path) and category (query)

@app.get('/books/{author_name}/')
async def get_book_by_author_category(author_name:str,category:str):
    BOOKS_TO_RETURN = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            if book.get('category').casefold() == category.casefold():
                BOOKS_TO_RETURN.append(book)
    return BOOKS_TO_RETURN