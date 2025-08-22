Python Password Manager

A secure desktop application for password management, built with Python and Tkinter. The application allows users to save, view, delete, and copy passwords safely and efficiently, storing all data locally in an SQLite database.

Key Features

Intuitive Graphical Interface: Built with Tkinter for simple and easy use.

Local and Secure Storage: Data is saved in a local SQLite database on the user's computer.

Full CRUD Operations:

CREATE: Save new entries (website, username, password).

READ: Display all saved entries (without exposing the password) in a sorted list.

DELETE: Permanently delete a selected entry.

Clipboard Copy: Allows copying a password to the clipboard with a single click without displaying it on screen.

Clean Formatting: The password list is displayed in a neatly aligned tabular format for maximum readability.

Technologies Used

Language: Python

GUI: Tkinter

Database: SQLite 3

Query Language: SQL (CREATE, INSERT, SELECT, DELETE)

How to Run

Clone the Repository:

git clone https://github.com/MironCristian/python-password-manager.git
cd python-password-manager


(Optional) Create and Activate a Virtual Environment:

python -m venv venv
.\venv\Scripts\activate


Run the Database Setup Script (One-Time Only!):
This script will create the passwords.db file in your folder.

python database_setup.py


Run the Main Application:

python main.py