from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("D:\Storemanagement software\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT MAX(id) FROM inventory")
for row in result:
    Id = row[0]

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Add YOUR PRODUCTS INTO THE DATABASE", font="arial 40 bold", fg="skyblue",bg="green")
        self.heading.place(x=10, y=0)
        master.configure(bg="green")

        self.name_L = Label(master, text="Enter Product Name", font="arial 18 bold", fg="white",bg="green")
        self.name_L.place(x=20, y=70)

        self.stock_L = Label(master, text="Enter Available Stock", font="arial 18 bold", fg="white",bg="green")
        self.stock_L.place(x=20, y=120)

        self.cp_L = Label(master, text="Enter Cost Price/Unit", font="arial 18 bold", fg="white",bg="green")
        self.cp_L.place(x=20, y=170)

        self.sp_L = Label(master, text="Enter Sale Price/Unit", font="arial 18 bold", fg="white",bg="green")
        self.sp_L.place(x=20, y=220)

        self.vendor_L = Label(master, text="Enter Dealer's Name", font="arial 18 bold", fg="white",bg="green")
        self.vendor_L.place(x=20, y=270)

        self.vedor_phone_L = Label(master, text="Dealer's Phone Number", font="arial 18 bold", fg="white",bg="green")
        self.vedor_phone_L.place(x=20, y=320)

        self.Id_L = Label(master, text="Enter ID", font="arial 18 bold", fg="white",bg="green")
        self.Id_L.place(x=20, y=370)

        self.name_E = Entry(master, width=25, font="arial 18 bold",bg="wheat")
        self.name_E.place(x=380, y=70)

        self.stock_E = Entry(master, width=25, font="arial 18 bold",bg="wheat")
        self.stock_E.place(x=380, y=120)

        self.cp_E = Entry(master, width=25, font="arial 18 bold",bg="wheat")
        self.cp_E.place(x=380, y=170)

        self.sp_E = Entry(master, width=25, font="arial 18 bold",bg="wheat")
        self.sp_E.place(x=380, y=220)

        self.vendor_E = Entry(master, width=25, font="arial 18 bold",bg="wheat")
        self.vendor_E.place(x=380, y=270)

        self.vendor_phone_E = Entry(master, width=25, font="arial 18 bold",bg="wheat")
        self.vendor_phone_E.place(x=380, y=320)

        self.Id_e = Entry(master, width=25, font="arial 18 bold",bg="wheat")
        self.Id_e.place(x=380, y=370)

        self.btn_add = Button(master, text="Add To DataBase",font="arial 10 bold", width=15, height=3, bg="skyblue", fg="black",
                              command=self.get_Entries)
        self.btn_add.place(x=430, y=420)

        self.btn_clear = Button(master, text="Clear All Fields",font="arial 10 bold", width=15, height=3, bg="skyblue", fg="black",
                                command=self.clear_all)
        self.btn_clear.place(x=800, y=420)

        self.tBox = Text(master, width=50, height=21,bg="wheat")
        self.tBox.place(x=740, y=70)
        self.tBox.insert(END, "Id has been reached: " + str(Id))

        self.master.bind('<Return>', self.get_Entries)
        self.master.bind('<Up>', self.clear_all)

    def get_Entries(self, *args, **kwargs):
        self.name = self.name_E.get()
        self.stock = self.stock_E.get()
        self.cp = self.cp_E.get()
        self.sp = self.sp_E.get()
        self.vendor = self.vendor_E.get()
        self.vendor_phone = self.vendor_phone_E.get()
        self.id_entry = self.Id_e.get()

        if not all((self.name, self.stock, self.cp, self.sp)):
            tkinter.messagebox.showinfo('Error', 'Please fill all the entries')
            return

        # Check if product name already exists
        product_exists_query = "SELECT id FROM inventory WHERE name=?"
        result = c.execute(product_exists_query, (self.name,))
        if result.fetchone():
            tkinter.messagebox.showinfo('Error', 'Product with the same name already exists')
            return

        try:
            self.totalcp = float(self.cp) * float(self.stock)
            self.totalsp = float(self.sp) * float(self.stock)
            self.assumed_profit = float(self.totalsp - self.totalcp)

            # Remaining code remains unchanged
            sql = "INSERT INTO inventory (name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phone) VALUES (?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit,
                            self.vendor, self.vendor_phone))
            conn.commit()
            self.tBox.insert(END, "\n\nInserted  " + str(self.name) + " into database with code: " + str(self.Id_e.get()))

            tkinter.messagebox.showinfo('Success', "Successfully added to the database")

        except Exception as e:
            tkinter.messagebox.showinfo('Error', f'Error: {e}')

    def clear_all(self, *args, **kwargs):
        num = Id + 1
        self.name_E.delete(0, END)
        self.stock_E.delete(0, END)
        self.cp_E.delete(0, END)
        self.sp_E.delete(0, END)
        self.vendor_E.delete(0, END)
        self.vendor_phone_E.delete(0, END)
        self.Id_e.delete(0, END)


def main():
    root = Tk()
    b = Database(root)
    root.geometry("1200x500+250+150")
    root.title('Add to the database')
    root.mainloop()


if __name__ == "__main__":
    main()




