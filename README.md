# Student Regstry System CLI

A robust, terminal-based student registry system built with Python. This project demonstrates safe data persistence using JSON and follows professional Object-Oriented Programming (OOP) principles.

##  Features
- **Data Persistence:** Stores and retrieves student records (Name, Age, Favorite Subject) using a local `JSON` database.
- **Robust Error Handling:** Uses `try-except` blocks to handle file corruption, missing files, and invalid data types.
- **Auto-Initialization:** Automatically creates the storage file on first run if it doesn't exist.
- **Clean Architecture:** Built using a class-based structure for better scalability.

##  Tech Stack
- **Language:** Python 3.x
- **Storage:** JSON (Standard Library)

##  How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com
Use code with caution.

Navigate to the folder:
bash
cd student-vault
Use code with caution.

Run the script:
bash
python student_vault.py
Use code with caution.

Error Handling Implemented
JSONDecodeError: Handles corrupted or improperly formatted JSON files.
FileNotFoundError: Ensures the system doesn't crash if the database is missing.
ValueError: Validates user input (e.g., ensuring Age is a number).

### Pro-Tip for Github:
Create a file named **`.gitignore`** in the same folder and add this single line inside it:
```text
