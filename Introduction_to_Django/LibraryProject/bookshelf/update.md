````markdown:LibraryProject/update.md
# Update Operation

## Django Shell Commands

```python
# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(f"Updated title: {updated_book.title}")

# Expected Output:
# Updated title: Nineteen Eighty-Four
````
