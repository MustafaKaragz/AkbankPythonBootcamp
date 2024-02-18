import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, dosya_adı="books.txt"):
        self.dosya_adı = dosya_adı
        self.dosya = open(self.dosya_adı, "a+")

    def __del__(self):
        self.dosya.close()

    def add_kitap(self, kitap_bilgisi):
        self.dosya.write(kitap_bilgisi + '\n')

    def remove_kitap(self, kitap_baslik):
        with open(self.dosya_adı, "r+") as dosya:
            satirlar = dosya.readlines()
            dosya.seek(0)
            kitapisimi_var = False
            yeni_satirlar = []
            for satir in satirlar:
                if kitap_baslik.strip() in satir:
                    kitapisimi_var = True
                else:
                    yeni_satirlar.append(satir)
            dosya.seek(0)
            dosya.writelines(yeni_satirlar)
            dosya.truncate()
        return kitapisimi_var

    def all_kitap(self):
        self.dosya.seek(0)
        with open(self.dosya_adı, "r") as dosya:
            return dosya.readlines()


library = Library()

def list_books():
    kayitlar = library.all_kitap()
    if kayitlar:
        book_list = "\n".join(kayitlar)
        messagebox.showinfo("Books", book_list)
    else:
        messagebox.showinfo("Books", "No Registered Books.")

def is_valid_number(input_str):
    return input_str.isdigit()

def is_valid_string(input_str):
    return input_str.isalpha()

def add_books():
    def add_to_file():
        baslik = entry_baslik.get()
        yazar = entry_yazar.get()
        yayin_yili = entry_yayin_yili.get()
        sayfa_sayisi = entry_sayfa_sayisi.get()

        if not is_valid_string(baslik) or not is_valid_string(yazar):
            messagebox.showerror("Error", "Title and author must consist of letters only.")
            return

        if not is_valid_number(yayin_yili) or not is_valid_number(sayfa_sayisi):
            messagebox.showerror("Error", "Publication year and number of pages must be numeric.")
            return

        kitap_bilgisi = (f"Title: {baslik}, Author: {yazar}, Year Of Publication: {yayin_yili}, Number Of Pages: {sayfa_sayisi}")
        library.add_kitap(kitap_bilgisi)
        messagebox.showinfo("Successful", f"Book: '{baslik}' added successfully.")

    add_window = tk.Toplevel()
    add_window.title("Add Book")

    label_baslik = tk.Label(add_window, text="Title:")
    label_baslik.grid(row=0, column=0)
    entry_baslik = tk.Entry(add_window)
    entry_baslik.grid(row=0, column=1)


    label_yazar = tk.Label(add_window, text="Author:")
    label_yazar.grid(row=1, column=0)
    entry_yazar = tk.Entry(add_window)
    entry_yazar.grid(row=1, column=1)

    label_yayin_yili = tk.Label(add_window, text="Year Of Publication:")
    label_yayin_yili.grid(row=2, column=0)
    entry_yayin_yili = tk.Entry(add_window)
    entry_yayin_yili.grid(row=2, column=1)

    label_sayfa_sayisi = tk.Label(add_window, text="Number Of Pages:")
    label_sayfa_sayisi.grid(row=3, column=0)
    entry_sayfa_sayisi = tk.Entry(add_window)
    entry_sayfa_sayisi.grid(row=3, column=1)

    button_add = tk.Button(add_window, text="Add", command=add_to_file)
    button_add.grid(row=4, column=0, columnspan=2)

def remove_books():
    def remove_from_file():
        kitaptitle = entry_kitaptitle.get().strip()

        if not kitaptitle:
            messagebox.showwarning("Warning", "Please Enter Book Title !")
            return

        if library.remove_kitap("Title: " + kitaptitle):
            messagebox.showinfo("Successful", f"Book: '{kitaptitle}' was successfully deleted.")
        else:
            messagebox.showerror("Error", f"Book '{kitaptitle}' not found.")

    remove_window = tk.Toplevel()
    remove_window.title("Remove Book")

    label_kitaptitle = tk.Label(remove_window, text="Book Title:")
    label_kitaptitle.grid(row=0, column=0)
    entry_kitaptitle = tk.Entry(remove_window)
    entry_kitaptitle.grid(row=0, column=1)

    button_remove = tk.Button(remove_window, text="Remove", command=remove_from_file)
    button_remove.grid(row=2, column=0, columnspan=2)



def menu():
    menu_window = tk.Tk()
    menu_window.title("Menu")

    button_list_books = tk.Button(menu_window, text="List Books", command=list_books)
    button_list_books.pack(pady=15,padx=10)

    button_add_books = tk.Button(menu_window, text="Add Book", command=add_books)
    button_add_books.pack(pady=15,padx=10)

    button_remove_books = tk.Button(menu_window, text="Remove Book", command=remove_books)
    button_remove_books.pack(pady=15,padx=10)

    button_quit = tk.Button(menu_window, text="Exit", command=menu_window.quit)
    button_quit.pack(pady=15,padx=10)

    menu_window.mainloop()

if __name__ == "__main__":
    menu()
