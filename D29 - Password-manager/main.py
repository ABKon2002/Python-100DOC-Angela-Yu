# ---------------------------- IMPORTS ------------------------------- #
from random import choice, shuffle
import json
from cryptography.fernet import Fernet
import base64

# ---------------------------- SECURITY (Not implemented) ------------------------------- #
encryption_key = Fernet.generate_key()
fernet = Fernet(encryption_key)

def encrypt_password(password):
    encrypted = fernet.encrypt(password.encode())  # Encrypt as bytes
    return base64.urlsafe_b64encode(encrypted).decode()  # Convert to string

def decrypt_password(encrypted_password):
    encrypted_bytes = base64.urlsafe_b64decode(encrypted_password.encode())  # Decode to bytes
    return fernet.decrypt(encrypted_bytes).decode()  # Decrypt to string

# ---------------------------- GENERATE PASSWORD ------------------------------- #
def generate_password():
    small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "&"]
    newGen = []
    for _ in range(6):
        newGen.append(choice(small_letters + capital_letters))
    for _ in range(2):
        newGen.append(choice(numbers))
    for _ in range(2):
        newGen.append(choice(symbols))
    for _ in range(3):
        shuffle(newGen)
    newGen_pass = "".join(newGen)
    password_entry.delete(0, "end")
    password_entry.insert(0, newGen_pass)
    selected_or_not = messagebox.askyesno(title = "Password Generated", message = f"Generated password is: {newGen_pass} \nDo you want to copy it to clipboard?")
    if selected_or_not:
        password_entry.clipboard_append(newGen_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(default = None):
    website_name = website_entry.get()
    email_or_username = email_username_entry.get()
    password = password_entry.get()
    password_encrypted = encrypt_password(password)

    new_data = {
        website_name: {
            "email": email_or_username,
            "password": password
        }
    }

    if len(website_name) == 0 or len(email_or_username) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Error", message = "Please don't leave any fields empty.")
        return

    is_ok = messagebox.askokcancel(title = "Confirmation", message = f"These are the details entered:\nWebsite: {website_name}\nEmail/Username: {email_or_username} \nPassword: {password} \nIs it ok to save?")
    if is_ok:
        try:
            with open("D29 - Password-manager\\data.json", "r") as file:
                # Read old data
                data = json.load(file)
                # Update old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        
        with open("D29 - Password-manager\\data.json", "w") as file:
            json.dump(data, file, indent = 4)
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            messagebox.showinfo(title = "Password Saved", message = f"Password for {website_name} has been saved.")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_name = website_entry.get()
    try:
        with open("D29 - Password-manager\\data.json", "r") as file:
            data = json.load(file)
            email_or_username = data[website_name]["email"]
            password = data[website_name]["password"]            
            # password = decrypt_password(password)
            messagebox.showinfo(title = website_name, message = f"Email/Username: {email_or_username}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No data file found.")
    except KeyError:
        messagebox.showinfo(title = "Error", message = f"No details for {website_name} exists.")

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, messagebox

BG_COLOR = "#FFF8E6"  # Off white
LOCK_COLOR = "#D39D55"  # light orange
TEXT1_COLOR = "#8D0B41"  # Maroon
TEXT2_COLOR = "#D6CFB4"   # Silver grey

# Window setup
window = Tk()
window.title("Password Manager")
window.minsize(width = 200, height = 200)
window.config(padx = 50, pady = 50, bg = BG_COLOR)

# Logo
image = PhotoImage(file = "D29 - Password-manager\\logo.png")
logo_canvas = Canvas(width = 200, height = 200, highlightthickness = 0, bg = BG_COLOR)
logo_canvas.create_image(100, 100, image = image)
logo_canvas.grid(row = 0, column = 1)

# Text labels:
# website label
website_label = Label(text = "Website:", fg = TEXT1_COLOR, bg = BG_COLOR)
website_label.grid(row = 1, column = 0)

# Email/username label
email_username_label = Label(text = "Email/Username:", fg = TEXT1_COLOR, bg = BG_COLOR)
email_username_label.grid(row = 2, column = 0)

# Password label
password_label = Label(text = "Password:", fg = TEXT1_COLOR, bg = BG_COLOR)
password_label.grid(row = 3, column = 0)


# Entry fields:
# website entry
website_entry = Entry(width = 43)
website_entry.grid(row = 1, column = 1, columnspan = 2, sticky='w')
website_entry.focus()

# Email/username entry
email_username_entry = Entry(width = 51)
email_username_entry.grid(row = 2, column = 1, columnspan = 2, sticky='w')
email_username_entry.insert(0, "most_used_email@gmail.com")

# Password entry
password_entry = Entry(width = 32, show="*")    # Shows in password text...
password_entry.grid(row = 3, column = 1, sticky='w')    


# Buttons:
# Search button
search_button= Button(text = "Search", bg = TEXT2_COLOR, fg = 'black', command = find_password)
search_button.grid(row = 1, column = 2, sticky='e')

# Generate password button
generate_password_button = Button(text = "Generate Password", bg = TEXT2_COLOR, fg = 'black', command = generate_password)
generate_password_button.grid(row = 3, column = 2, sticky='w')

# Add button
add_button = Button(text = "Add", width = 43, bg = TEXT2_COLOR, fg = 'black', command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky='w')
window.bind("<Return>", save_password)      # Also binded the enter key to the save function command.

window.mainloop()
