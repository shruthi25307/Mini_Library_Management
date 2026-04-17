from datetime import date, timedelta

# TEXTBOOKS
booknames = [
    "Maths Textbook - 1","Maths Textbook - 2","Maths Textbook - 3",
    "Maths Textbook - 4","Maths Textbook - 5","Maths Textbook - 6",
    "Maths Textbook - 7","Maths Textbook - 8","Maths Textbook - 9",
    "Maths Textbook - 10","Maths Textbook - 11","Maths Textbook - 12",

    "Science Textbook - 1","Science Textbook - 2","Science Textbook - 3",
    "Science Textbook - 4","Science Textbook - 5","Science Textbook - 6",
    "Science Textbook - 7","Science Textbook - 8","Science Textbook - 9",
    "Science Textbook - 10",

    "English Textbook - 1","English Textbook - 2","English Textbook - 3",
    "English Textbook - 4","English Textbook - 5","English Textbook - 6",
    "English Textbook - 7","English Textbook - 8","English Textbook - 9",
    "English Textbook - 10","English Textbook - 11","English Textbook - 12",

    "Physics Textbook - 11","Physics Textbook - 12",
    "Chemistry Textbook - 11","Chemistry Textbook - 12",
    "Biology Textbook - 11","Biology Textbook - 12",
    "Computer Science Textbook - 11","Computer Science Textbook - 12"
]

# STORY BOOKS
storybooks = [
    "The Magic Tree", "The Lost Prince", "Adventures of Tom",
    "The Secret Island", "The Brave Little Girl", "Jungle Tales",
    "The Mystery House", "Fairy World", "The Clever Fox", "The Hidden Treasure"
]

# GLOBAL STORAGE
issued_books = {}
due_dates = {}

# DUE DATE
def showDueDate(book):
    due = date.today() + timedelta(days=7)
    due_dates[book] = due
    print("Return the book by:", due)

# BASIC TEXTBOOK FUNCTIONS
def checkAvailability(bookname):
    if bookname.lower() in [b.lower() for b in booknames]:
        print("The book is available!")
    else:
        print("Sorry, the book is not available :( ")

def issueTextbook(bookname, user):
    for b in booknames:
        if bookname.lower() == b.lower():
            print("Book issued successfully!")
            booknames.remove(b)
            issued_books.setdefault(user, []).append(bookname)
            showDueDate(bookname)
            return True
    print("Sorry, the book is not available :( ")
    return False

# STORY BOOK ISSUE
def issueStoryBook(user):
    print("\nAvailable Story Books:")
    for i in range(len(storybooks)):
        print(i+1, ".", storybooks[i])
    s_choice = int(input("Select a book by number: "))
    if 1 <= s_choice <= len(storybooks):
        book = storybooks[s_choice-1]
        issued_books.setdefault(user, []).append(book)
        storybooks.remove(book)
        print(book, "issued successfully!")
        showDueDate(book)
    else:
        print("Invalid choice!")

# RETURN BOOK
def returnBook(user):
    if user not in issued_books or not issued_books[user]:
        print("You have no books to return.")
        return
    print("\nYour issued books:")
    for i, b in enumerate(issued_books[user], 1):
        print(i, ".", b)
    choice = int(input("Select a book to return: "))
    if 1 <= choice <= len(issued_books[user]):
        book = issued_books[user].pop(choice-1)
        booknames.append(book)  # add back to library
        due_dates.pop(book, None)
        print(book, "returned successfully!")
    else:
        print("Invalid choice!")

# DAMAGE REPORT
def reportDamage(user):
    if user not in issued_books or not issued_books[user]:
        print("You have no books to report damage.")
        return
    print("\nYour issued books:")
    for i, b in enumerate(issued_books[user], 1):
        print(i, ".", b)
    choice = int(input("Select a book to report damage: "))
    if 1 <= choice <= len(issued_books[user]):
        book = issued_books[user][choice-1]
        print("Damage report submitted for:", book)
        print("Library staff will review and contact you.")
    else:
        print("Invalid choice!")

# LATE FEES
def calculateLateFees(user):
    if user not in issued_books or not issued_books[user]:
        print("You have no books issued.")
        return
    today = date.today()
    total_fee = 0
    print("\nLate Fee Details:")
    for book in issued_books[user]:
        due = due_dates.get(book, today)
        if today > due:
            days_late = (today - due).days
            fee = days_late * 5  # ₹5 per day
            print(f"{book} is {days_late} days late. Fee: ₹{fee}")
            total_fee += fee
    if total_fee == 0:
        print("No late fees. Well done!")
    else:
        print("Total Late Fee: ₹", total_fee)

# VIEW ISSUED BOOKS
def viewIssuedBooks(user):
    if user not in issued_books or not issued_books[user]:
        print("You have no books issued.")
    else:
        print("\nYour issued books:")
        for b in issued_books[user]:
            print("-", b)

# RENEW BOOK
def renewBook(user):
    if user not in issued_books or not issued_books[user]:
        print("You have no books to renew.")
        return
    print("\nYour issued books:")
    for i, b in enumerate(issued_books[user], 1):
        print(i, ".", b)
    choice = int(input("Select a book to renew: "))
    if 1 <= choice <= len(issued_books[user]):
        book = issued_books[user][choice-1]
        due_dates[book] = due_dates[book] + timedelta(days=7)
        print(book, "renewed successfully! New due date:", due_dates[book])
    else:
        print("Invalid choice!")

# MULTIPLE ISSUE LOOP
def issueMultipleBooks(user):
    while True:
        print("\nDo you want to issue:")
        print("1. School Textbook")
        print("2. Story Book")
        print("3. Stop Issuing")
        cat_choice = int(input("Enter your choice: "))
        if cat_choice == 1:
            bookname = input("Enter the Book Name (Example: Subject Textbook - Standard -  Maths Textbook - 12): ")
            issueTextbook(bookname, user)
        elif cat_choice == 2:
            issueStoryBook(user)
        elif cat_choice == 3:
            break
        else:
            print("Invalid choice!")

        more = input("Do you want to issue another book? (yes/no): ")
        if more.lower() != "yes":
            break

# MAIN PROGRAM
print("-----------WELCOME TO SCHOOL LIBRARY SYSTEM-----------")

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
phno = input("Enter your Phone Number: ")

while True:
    print("Select Option:")
    print("1. Issue Books (Multiple Allowed)")
    print("2. Return Book")
    print("3. Report Damage")
    print("4. View Issued Books")
    print("5. Renew Book")
    print("6. Late Fees Details")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        issueMultipleBooks(name)
    elif choice == 2:
        returnBook(name)
    elif choice == 3:
        reportDamage(name)
    elif choice == 4:
        viewIssuedBooks(name)
    elif choice == 5:
        renewBook(name)
    elif choice == 6:
        calculateLateFees(name)
    elif choice == 7:
        print("Thank you for using the library!")
        break
    else:
        print("Invalid choice!")

    print("\n--------------------------------------\n")
