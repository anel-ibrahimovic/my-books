def my_books():
    books = []
    print("Welcome to MyBooks!")

    while True:
        print("\n1. Add a Book")
        print("2. View all Books")
        print("3. Search Books")
        print("4. Update Status")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            book_title = input("\n1. Enter book title: ").strip()
            book_author = input("2. Enter book author: ").strip()
            book_genre = input("3. Enter book genre: ").strip()

            while True:
                publish_year = input("4. Enter publish year: ").strip()
                if publish_year.isdigit():
                    publish_year = int(publish_year)
                    break
                else:
                    print("Please enter a valid year.")

            while True:
                status_choice = input("Enter 1 for 'Unread' or 2 for 'Read': ").strip()
                if status_choice == '1':
                    status = 'Unread'
                    break
                elif status_choice == '2':
                    status = 'Read'
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")

            book = {
                'title': book_title,
                'author': book_author,
                'genre': book_genre,
                'year': publish_year,
                'status': status,
            }
            books.append(book)
            print(f"Book '{book_title}' by '{book_author}' added!")

        elif choice == 2:
            if not books:
                print("No books added.")
            else:
                print("\nAll Books:")
                for book in books:
                    print_book(book)

        elif choice == 3:
            if not books:
                print("No books added.")
            else:
                search = input("Enter the book title to search: ").strip().lower()
                matches = [book for book in books if search in book['title'].lower()]
                if matches:
                    for book in matches:
                        print_book(book)
                else:
                    print("No matching books found.")

        elif choice == 4:
            if not books:
                print("No books added.")
            else:
                status_update = input("Enter the book title to update status: ").strip().lower()
                for book in books:
                    if book['title'].lower() == status_update:
                        print(f"Current status: {book['status']}")
                        new_status = input("Enter new status (Read/Unread): ").strip().capitalize()
                        if new_status in ['Read', 'Unread']:
                            book['status'] = new_status
                            print("Status updated!")
                        else:
                            print("Invalid status. No changes made.")
                        break
                else:
                    print("Book not found.")

        elif choice == 5:
            print("Thank you for using MyBooks!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def print_book(book):
    print("-" * 50)
    print(f"Name: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Category: {book['genre']}")
    print(f"Publish Year: {book['year']}")
    print(f"Status: {book['status']}")
    print("-" * 50)

my_books()
