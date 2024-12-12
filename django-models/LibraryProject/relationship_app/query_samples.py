from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author"""
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_library_books(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_library_librarian(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Example usage:
if __name__ == "__main__":
    # Get books by author
    author_books = get_books_by_author("J.K. Rowling")
    for book in author_books:
        print(f"Book by author: {book.title}")

    # Get library books
    library_books = get_library_books("Central Library")
    for book in library_books:
        print(f"Library book: {book.title}")

    # Get librarian
    librarian = get_library_librarian("Central Library")
    print(f"Librarian: {librarian.name}")