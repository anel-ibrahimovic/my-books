import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

BOOKS_FILE = "books.json"

class MyBooksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MyBooks Library")
        self.books = []

        self.create_widgets()
        self.load_books()
        self.view_books()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Welcome to MyBooks!", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        self.books_listbox = tk.Listbox(self.root, width=80, height=15)
        self.books_listbox.pack(padx=10, pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Book", width=15, command=self.add_book).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Search Book", width=15, command=self.search_books).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Update Status", width=15, command=self.update_status).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(btn_frame, text="Exit", width=15, command=self.root.quit).grid(row=0, column=3, padx=5, pady=5)

    def save_books(self):
        try:
            with open(BOOKS_FILE, "w") as f:
                json.dump(self.books, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save books: {e}")

    def load_books(self):
        if os.path.exists(BOOKS_FILE):
            try:
                with open(BOOKS_FILE, "r") as f:
                    self.books = json.load(f)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load books: {e}")
                self.books = []

    def add_book(self):
        title = simpledialog.askstring("Book Title", "Enter book title:")
        if not title:
            return

        author = simpledialog.askstring("Book Author", "Enter book author:")
        if not author:
            return

        genre = simpledialog.askstring("Book Genre", "Enter book genre:")
        if not genre:
            return

        while True:
            year = simpledialog.askstring("Publish Year", "Enter publish year:")
            if year is None:
                return
            if year.isdigit():
                year = int(year)
                break
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid year.")

        status = simpledialog.askstring("Status", "Enter status (Read/Unread):", initialvalue="Unread")
        if not status or status.strip().capitalize() not in ["Read", "Unread"]:
            messagebox.showerror("Invalid Input", "Status must be 'Read' or 'Unread'.")
            return

        book = {
            'title': title.strip(),
            'author': author.strip(),
            'genre': genre.strip(),
            'year': year,
            'status': status.strip().capitalize(),
        }
        self.books.append(book)
        self.save_books()
        self.view_books()

    def view_books(self, filter_term=None):
        self.books_listbox.delete(0, tk.END)
        if not self.books:
            self.books_listbox.insert(tk.END, "No books added.")
            return

        for book in self.books:
            if filter_term and filter_term.lower() not in book['title'].lower():
                continue
            display = f"{book['title']} | {book['author']} | {book['genre']} | {book['year']} | {book['status']}"
            self.books_listbox.insert(tk.END, display)

    def search_books(self):
        if not self.books:
            messagebox.showinfo("Info", "No books to search.")
            return

        search_term = simpledialog.askstring("Search Book", "Enter part of book title to search:")
        if not search_term:
            return

        self.view_books(filter_term=search_term)

    def update_status(self):
        if not self.books:
            messagebox.showinfo("Info", "No books to update.")
            return

        selection = self.books_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a book from the list first.")
            return

        index = selection[0]
        if index >= len(self.books):
            messagebox.showerror("Error", "Invalid selection.")
            return

        book = self.books[index]

        new_status = simpledialog.askstring("Update Status",
                                            f"Current status: {book['status']}\nEnter new status (Read/Unread):")
        if not new_status:
            return

        if new_status.strip().capitalize() in ["Read", "Unread"]:
            book['status'] = new_status.strip().capitalize()
            messagebox.showinfo("Success", "Status updated.")
            self.save_books()
            self.view_books()
        else:
            messagebox.showerror("Invalid Input", "Status must be 'Read' or 'Unread'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyBooksApp(root)
    root.mainloop()
