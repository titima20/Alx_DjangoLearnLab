````markdown:LibraryProject/retrieve.md
# Retrieve Operation

## Django Shell Commands

```python
# Get the book we just created
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Date: {book.publication_date}")

# Expected Output:
# Title: 1984
# Author: George Orwell
# Publication Date: 1949
````
