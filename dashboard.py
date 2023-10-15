import tkinter as tk
from tkinter import Button
import add_to_db
import updateStock

class Dashboard:
    def __init__(self, master):
        self.master = master
        master.title("Baby Garments Store Tehsil Piplan")
        
        # Set background color
        master.configure(bg="#FFD700")  # You can use any hexadecimal color code or a color name

        # Set geometry
        master.geometry("800x600")  # Adjust the size as needed

        # Add a label for the title
        title_label = tk.Label(master, text="Baby Garments Store Tehsil Piplan", font=("Arial", 24), bg="#FFD700", fg="purple")
        title_label.pack(pady=10)

        # Create buttons with colors
        self.add_button = Button(master, text="Add to Database", command=self.open_add_to_db, bg="green", fg="white")
        self.add_button.pack(pady=20)

        self.update_button = Button(master, text="Update Database", command=self.open_update_db, bg="blue", fg="white")
        self.update_button.pack(pady=20)

    def open_add_to_db(self):
        add_to_db.main()

    def open_update_db(self):
        updateStock.main()

def main():
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
