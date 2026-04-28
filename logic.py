from models import books

def issue_book(name, student, days):
    name = name.strip().lower()

    if name not in books:
        return "Book not found"

    if books[name]["available"]:
        books[name]["available"] = False
        books[name]["issued_to"] = student
        books[name]["days"] = days
        return "Issued"

    return "Not Available"


def return_book(name, late_days):
    name = name.strip().lower()

    if name not in books:
        return "Book not found"

    fine = 0
    if late_days > 0:
        fine = late_days * 10

    books[name]["available"] = True
    books[name]["issued_to"] = None
    books[name]["days"] = 0

    return fine