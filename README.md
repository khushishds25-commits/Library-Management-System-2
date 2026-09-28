# Library Management System

## Project Title

**Library Management System**

## Project Description

Library Management System is a Python-based application designed to help librarians manage books and library members efficiently.

The system provides functions for managing book information and member information. More features will be added as the project is developed.

---

## Problem Statement

Develop a Python-based Library Management System that enables librarians to efficiently manage books, members, and book transactions.

The application should allow users to add, search, update, and remove books, register library members, issue and return books, calculate overdue fines, and maintain complete transaction records.

The system should store all data permanently using file handling or a database and provide a user-friendly, menu-driven interface.

---

# Assessment-I

## Objectives

* To manage library books efficiently.
* To add and display book details.
* To understand the basic working of a Library Management System.
* To design the basic logic and structure of the project.
* To create the initial GitHub repository.

## Assessment-I Features

The initial version includes:

1. Add Book
2. Display Books

## Assessment-I Implementation

In the first assessment, the basic book management module was developed.

The user can enter:

* Book ID
* Book Name
* Author Name

The book details are stored in a Python list using a dictionary.

## Assessment-I Output

Example:

```text
Enter Book ID: B101
Enter Book Name: Python Programming
Enter Author Name: ABC

Book added successfully!

Library Books:
Book ID: B101
Book Name: Python Programming
Author: ABC
```

---

# Assessment-II

## Assessment-II Objectives

In Assessment-II, the initial project was further developed by adding new modules for book and member management.

## Assessment-II Features

The following features were added:

1. Add Book
2. Display Books
3. Search Book
4. Update Book
5. Remove Book
6. Register Member
7. Display Members

## Assessment-II Implementation

### Book Management

The system can:

* Add new books
* Display available books
* Search for a book using Book ID
* Update book details
* Remove a book

### Member Management

The system can:

* Register a new library member
* Display registered members

## Assessment-II Example Output

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Add Book
2. Display Books
3. Search Book
4. Update Book
5. Remove Book
6. Register Member
7. Display Members
8. Exit

Enter your choice: 1

Enter Book ID: B101
Enter Book Name: Python Programming
Enter Author Name: ABC

Book added successfully!
```

Example of member registration:

```text
Enter your choice: 6

Enter Member ID: M001
Enter Member Name: Rahul

Member registered successfully!
```

---

# Technologies Used

* Python
* Git
* GitHub

---

# Python Concepts Used

* Variables
* Input and Output
* Lists
* Dictionaries
* Functions
* Conditional Statements
* Loops

---

# Project Structure

```text
Library-Management-System/
│
├── library.py
└── README.md
```

### library.py

Contains the Python source code of the Library Management System.

### README.md

Contains information about the project, objectives, features, implementation and progress.

---

# Project Progress

## Assessment-I

Basic book management was implemented.

**Completed:**

* Add Book
* Display Books
* Initial GitHub Repository
* Basic Project Structure

## Assessment-II

The project was extended with additional book and member management modules.

**Completed:**

* Add Book
* Display Books
* Search Book
* Update Book
* Remove Book
* Register Member
* Display Members

---

# Future Development

The following features will be developed in the next stage:

* Issue Book
* Return Book
* Overdue Fine Calculation
* Transaction Records
* Permanent Data Storage
* Complete Menu-Driven System
* Testing and Final Demonstration

---

# Conclusion

The Library Management System is being developed step by step using Python. Assessment-I established the basic project structure, while Assessment-II added more book and member management features. Further features will be implemented in the final stage of the project.
