# Library Management System

A simple library management system implemented in Python.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)


## Description

A Library Management System that allows users to manage books, users, and book checkouts. The system provides functionalities such as adding, updating, and deleting books and users, checking out and in books, listing books and users, and searching for books and users.

## Features

- Add, update, and delete books
- Add, update, and delete users
- Check out and in books
- List books and users
- Search for books and users

## Installation

1. Clone the repository: `git clone https://github.com/your-username/library-management-system.git`

## Usage

1. Run the application: `python main.py`
2. Follow the on-screen instructions to manage books, users, and checkouts.

## Project Structure

- `main.py`: Entry point of the application.
- `models.py`: Defines the data models used in the system.
- `book.py`: Contains the BookManager class for managing books.
- `user.py`: Contains the UserManager class for managing users.
- `check.py`: Contains the CheckManager class for managing book checkouts.
- `storage.py`: Contains the Storage class for loading and saving data.
- `requirements.txt`: List of dependencies.
- `book.json`: JSON file to store book data.
- `user.json`: JSON file to store user data.
- `check.json`: JSON file to store checkout data.

## Dependencies

- Python (>=3.10)
- dataclasses



