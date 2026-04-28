from logic import issue_book, return_book
from models import books

while True:
    print("\nAvailable books:", list(books.keys()))
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        student = input("Enter student name: ")
        days = int(input("Enter number of days: "))

        result = issue_book(name, student, days)
        print(result)

    elif choice == "2":
        name = input("Enter book name: ")
        late_days = int(input("Enter late days: "))

        result = return_book(name, late_days)

        if result == "Book not found":
            print(result)
        else:
            print("Book returned successfully")
            print("Fine:", result)

    elif choice == "3":
        break