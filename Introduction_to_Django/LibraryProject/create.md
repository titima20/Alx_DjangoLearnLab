# Create Operation

## Django Shell Commands

```python
# Create a new book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_date=1949
)

# Output: <Book: Book object (1)>
```
