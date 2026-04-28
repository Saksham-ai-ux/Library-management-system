# 📚 Library Management System (Python)

This is a simple menu-driven Library Management System built using Python. It allows users to issue and return books while maintaining records using a dictionary-based structure.

## 🚀 Features
- Issue books with student name and duration
- Return books with fine calculation for late days
- Case-insensitive book search (user-friendly input handling)
- Displays available books
- Menu-driven system using loops

## 🛠️ Concepts Used
- Functions
- Dictionaries
- Conditional statements
- Loops (while True)
- Modular programming (separate files for logic, data, and main)

## ▶️ How to Run
1. Run the main.py file
2. Choose an option from the menu:
   - Issue Book
   - Return Book
   - Exit
3. Enter required details
4. View results

## 📁 Project Structure
main.py → User interaction & menu  
logic.py → Core functionality  
models.py → Book data storage  

## 📌 Example
Available books: ['python', 'math', 'atomic habits']

Enter choice: 1  
Enter book name: atomic habits  
Enter student name: Yuvnesh  
Enter number of days: 5  

Output: Issued

## 💡 Note
- Book names are handled in a case-insensitive manner
- Late return fines are calculated automatically
