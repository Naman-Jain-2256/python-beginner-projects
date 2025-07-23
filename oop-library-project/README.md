# 📚 Library Management Class in Python

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Improving-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

This project demonstrates a simple Python class named `Library` to manage a collection of books.  
It's a beginner-friendly implementation showcasing basic **Object-Oriented Programming (OOP)** concepts in Python.

---

## 🚀 Features

- 📥 Add books to the library
- 🗑️ Discard (remove) books from the library
- 🔍 Search for a book
- 📋 View all books (sorted alphabetically)
- 🔢 Check total books in the library
- ✅ Check internal consistency between book list and book count

---

## 🧠 Class Overview

### `class Library`

| Method | Description |
|--------|-------------|
| `add_book(*books)` | Adds one or more books to the library |
| `discard_book(*books)` | Removes specified books if they exist |
| `view_books()` | Displays all books in the library |
| `total_books()` | Prints the total count of books |
| `search_book(*books)` | Searches for specific books |
<!-- | `check()` | Verifies internal consistency of book count | -->
| `book_clean(book)` | Helper to clean input (lowercase + trim) |

---

## 🧠 How it Works

```python
library = Library()

# Add books
library.add_book("Book A", "Book B")

# View all books
library.view_books()

# Discard a book
library.discard_book("Book A")

# Search for a book
library.search_book("Book B")

# Check total books
library.total_books()
```

---

## 📦 Output Example

```python
The Psychology of Money added to the library.
Rich Dad Poor Dad added to the library.
1.) Rich Dad Poor Dad
2.) The Psychology Of Money
The Psychology of Money removed from the library.
1.) Rich Dad Poor Dad
The Art of Seduction added to the library.
48 Laws of Power added to the library.
The Psychology of Money added to the library.
How to Win Friends and Influence People added to the library.
1.) 48 Laws Of Power
2.) How To Win Friends And Influence People
3.) Rich Dad Poor Dad
4.) The Art Of Seduction
5.) The Psychology Of Money
True
Total books:5
The Psychology of Money is in the library.
Atomic Habits is not in the library.
Empty book cannot be added.
```

---

## 📂 File Structure

```
📁 oop-library-project/
│
├── library.py         # Python script containing the Library class and usage example
└── README.md          # This file
```

---

## 🛠️ Requirements

- Python 3.6 or higher

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](../LICENSE.txt) file for details.

---

## 🌟 Acknowledgements
Thanks to the Python community and all open-source contributors! 💛

---

## Author 🙋‍♂️
- **Name**: [Naman Jain](https://github.com/Naman-Jain-2256)
- **Email**: [jain.naman.22560@gmail.com](mailto:jain.naman.22560@gmail.com)
