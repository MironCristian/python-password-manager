import tkinter as tk
import sqlite3

def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    
    if not website or not username or not password:
        print("All fields are required.")
        return

    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    sql_command = "INSERT INTO entries (website, username, password) VALUES (?, ?, ?)"
    cursor.execute(sql_command, (website, username, password))
    connection.commit()
    connection.close()
    entry_website.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    print(f"Parola de pe platforma '{website}' a fost salvata cu succes!")
    load_passwords()
    pass

def load_passwords():
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    sql_command = "SELECT website, username FROM entries"
    cursor.execute(sql_command)
    all_entries = cursor.fetchall()
    connection.close()
    list_entries.delete(0, tk.END)
    for entry in all_entries:
        website = entry[0]
        username = entry[1]
        display_text = f"Site: {website:<30} | User: {username}"
        list_entries.insert(tk.END, display_text)
    pass

def get_selected_website():
    selected_indices = list_entries.curselection()
    if not selected_indices:
        return None
    
    selected_index = selected_indices[0]
    selected_text = list_entries.get(selected_index)
    part1 = selected_text.split('|')[0]
    website = part1.split(':')[1].strip()
    
    return website

def delete_entry():
    website_to_delete = get_selected_website()
    
    if not website_to_delete:
        print("Please select an item to delete!")
        return
    
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    
    sql_command = "DELETE FROM entries WHERE website = ?"
    
    cursor.execute(sql_command, (website_to_delete,))
    connection.commit()
    connection.close()
    print(f"The entry for '{website_to_delete}' has been deleted!")
    load_passwords()
    
def copy_password():
    website_to_copy = get_selected_website()
    if not website_to_copy:
     print("Please select an entry to copy!")
     return

    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    sql_command = "SELECT password FROM entries WHERE website = ?"
    cursor.execute(sql_command, (website_to_copy,))
    result = cursor.fetchone()
    connection.close()
    if result:
        password_to_copy = result[0]
        window.clipboard_clear()
        window.clipboard_append(password_to_copy)
        print(f"The password for '{website_to_copy}' has been copied to the clipboard.")



window = tk.Tk()
window.title("Password_Manager")

window.minsize(800, 900)
label_website = tk.Label(master=window, text="Website:")
label_website.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_website = tk.Entry(master=window, width=40)
entry_website.grid(row=0, column=1, padx=10, pady=5)
label_username = tk.Label(master=window, text="Username/Email:")
label_username.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_username = tk.Entry(master=window, width=40)
entry_username.grid(row=1, column=1, padx=10, pady=5)
label_password = tk.Label(master=window, text="Password: ")
label_password.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_password = tk.Entry(master=window, width=40)
entry_password.grid(row=2, column=1, padx=10, pady=5)
button_save = tk.Button(master=window, text="Save Password", command=save_password)
button_save.grid(row=3, column=0, columnspan=2, pady=10)
label_list = tk.Label(master=window, text="Saved passwords:", font=("Helvetica", 12))
label_list.grid(row=4, column=0, columnspan=2, pady=(10, 0))
list_entries = tk.Listbox(master=window, width=70, height=15, font=("Courier", 10))
list_entries.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
button_frame = tk.Frame(master=window)
button_frame.grid(row=6, column=0, columnspan=2, pady=10)
button_copy = tk.Button(master=button_frame, text="Copy Password!", command=copy_password)
button_copy.pack(side=tk.LEFT, padx=5)
button_delete = tk.Button(master=button_frame, text="Delete!", command=delete_entry)
button_delete.pack(side=tk.LEFT, padx=5)

load_passwords()
window.mainloop()