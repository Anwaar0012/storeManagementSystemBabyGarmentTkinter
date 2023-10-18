from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random
from prettytable import PrettyTable

conn = sqlite3.connect("D:/Storemanagement software/Database/store.db")
c = conn.cursor()

date = datetime.datetime.now().date()

class SalePoint:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.products_list = []
        self.product_price = []
        self.product_quantity = []
        self.product_stock = []
        self.product_id = []

        self.labels_list = []

        self.left = Frame(master, width=700, height=768, bg="wheat")
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg="lightblue")
        self.right.pack(side=LEFT)

        self.heading = Label(self.left, text="Baby Garments Store", font="arial 40 bold", bg="wheat", fg="black")
        self.heading.place(x=0, y=0)

        self.date_L = Label(self.right, text="Today's Date: " + str(date), font="arial 18 bold", bg="white", fg="black")
        self.date_L.place(x=0, y=0)

        self.tproduct = Label(self.right, text="Products", font="arial 18 bold", bg="lightblue", fg="black")
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Quantity", font="arial 18 bold", bg="lightblue", fg="black")
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font="arial 18 bold", bg="lightblue", fg="black")
        self.tamount.place(x=500, y=60)

        self.enteredid_L = Label(self.left, text="Enter Products ID", font="arial 18 bold", bg="wheat", fg="black")
        self.enteredid_L.place(x=0, y=80)

        self.enteredid_E = Entry(self.left, width=25, font="arial 18 bold", bg="lightblue")
        self.enteredid_E.place(x=210, y=80)
        self.enteredid_E.focus()

        self.btn_search = Button(self.left, text="Search", width=25, height=2, bg="orange", command=self.ajax)
        self.btn_search.place(x=350, y=120)

        self.productname = Label(self.left, text="", font="arial 18 bold", bg="wheat", fg="blue")
        self.productname.place(x=0, y=250)

        self.stock_label = Label(self.left, text="", font="arial 15 bold", bg="wheat", fg="green")
        self.stock_label.place(x=0, y=290)

        self.prodPrice = Label(self.left, text="", font="arial 25 bold", bg="wheat", fg="blue")
        self.prodPrice.place(x=0, y=330)

        self.total_L = Label(self.right, text="", font="arial 40 bold", bg="lightblue", fg="black")
        self.total_L.place(x=0, y=600)

    def ajax(self, *args, **kwargs):
        self.get_id = self.enteredid_E.get()

        if not self.get_id:
            tkinter.messagebox.showerror("Error", "Please enter Product ID")
            return
        
        query = "SELECT id, name, sp, stock FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id,))

        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_sp = self.r[2]
            self.get_stock = self.r[3]

        self.productname.configure(text=str(self.get_name).upper())
        self.prodPrice.configure(text="Price:(Rs." + str(self.get_sp) + ")")

        stock_label_text = f"Stock Availability: {self.get_stock} units"
        self.stock_label.configure(text=stock_label_text)

        self.quantity_L = Label(self.left, text="Enter Quantity", font="arial 18 bold", bg="wheat", fg="black")
        self.quantity_L.place(x=0, y=380)

        self.quantity_E = Entry(self.left, width=23, font="arial 18 bold", bg="lightblue")
        self.quantity_E.place(x=190, y=380)
        self.quantity_E.focus()

        self.discount_L = Label(self.left, text="Enter Discount", font="arial 18 bold", bg="wheat", fg="black")
        self.discount_L.place(x=0, y=420)

        self.discount_E = Entry(self.left, width=23, font="arial 18 bold", bg="lightblue")
        self.discount_E.place(x=190, y=420)
        self.discount_E.insert(END, 0)

        self.add_to_cart_btn = Button(self.left, text="Add To Cart", width=10,font="arial 20 bold", height=2,fg="black", bg="orange", command=self.add_to_cart)
        self.add_to_cart_btn.place(x=500, y=370)

        self.change_L = Label(self.left, text="Given Amount", font="arial 18 bold", bg="wheat", fg="black")
        self.change_L.place(x=0, y=550)

        self.change_E = Entry(self.left, width=23, font="arial 18 bold", bg="lightblue")
        self.change_E.place(x=190, y=550)

        self.change_btn = Button(self.left, text="Calculate Change", width=20, height=2, bg="orange", command=self.change_func)
        self.change_btn.place(x=500, y=545)

        self.bill_btn = Button(self.left, text="Generate Bill", font="arial 20 bold", width=30, height=2, bg="red", fg="white", command=self.generate_bill)
        self.bill_btn.place(x=20, y=640)

    def add_to_cart(self, *args, **kwargs):

        if not self.quantity_E.get() or not self.discount_E.get():
            tkinter.messagebox.showerror("Error", "Please enter Quantity and Discount")
            return
        
        self.quantity_value = int(self.quantity_E.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showerror("Error", "Demanded Quantity is not available in stock")
        else:
            self.final_price = (float(self.quantity_value) * float(self.get_sp)) - (float(self.discount_E.get()))
            self.products_list.append(self.get_name)
            self.product_price.append(self.final_price)
            self.product_quantity.append(self.quantity_value)
            self.product_stock.append(self.get_stock)
            self.product_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for p, q, price, stock in zip(self.products_list, self.product_quantity, self.product_price, self.product_stock):
                temp_name = Label(self.right, text=str(p), font="arial 15 bold", bg="lightblue", fg="black")
                temp_name.place(x=0, y=self.y_index)
                self.labels_list.append(temp_name)

                temp_qt = Label(self.right, text=str(q), font="arial 15 bold", bg="lightblue", fg="black")
                temp_qt.place(x=300, y=self.y_index)
                self.labels_list.append(temp_qt)

                temp_price = Label(self.right, text=str(price), font="arial 15 bold", bg="lightblue", fg="black")
                temp_price.place(x=500, y=self.y_index)
                self.labels_list.append(temp_price)

                temp_stock = Label(self.right, text=str(stock), font="arial 15 bold", bg="lightblue", fg="black")
                temp_stock.place(x=700, y=self.y_index)
                self.labels_list.append(temp_stock)

                self.y_index += 40
                self.counter += 1

            self.total_L.configure(text="Total : Rs." + str(sum(self.product_price)))

            self.quantity_L.place_forget()
            self.quantity_E.place_forget()
            self.discount_L.place_forget()
            self.discount_E.place_forget()

            self.productname.configure(text="")
            self.stock_label.configure(text="")
            self.prodPrice.configure(text="")

            self.add_to_cart_btn.destroy()

            self.enteredid_E.focus()
            self.enteredid_E.delete(0, END)

    def change_func(self, *args, **kwargs):
        if not self.change_E.get():
            tkinter.messagebox.showerror("Error", "Please enter Given Amount")
            return
        
        try:
            self.amount_given = float(self.change_E.get())
            self.our_total = float(sum(self.product_price))
            self.to_give = self.amount_given - self.our_total
            self.change_amount = Label(self.left, text=f"Change amount: Rs. {self.to_give}", font=("arial 18 bold"), bg="wheat", fg="red")
            self.change_amount.place(x=200, y=590)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid input for Given Amount")

    def generate_bill(self, *args, **kwargs):
        # Create a dynamic directory named "Invoice" if it doesn't exist
        invoice_directory = "D:/Storemanagement software/Invoice/"
        if not os.path.exists(invoice_directory):
            os.makedirs(invoice_directory)

        # Generate a more understandable filename
        file_name = f"{invoice_directory}Invoice_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.rtf"

        company = "BABY GARMENTS & SHOES"
        address = "Near Telenor Franchise Piplan"
        phone = "0300-4602762"
        sample = "INVOICE"
        dt = str(date)

        # Create a PrettyTable
        table = PrettyTable()
        table.field_names = ["SNO.", "PRODUCT NAME", "QTY", "AMOUNT", "STOCK"]

        for i, (product, quantity, price, stock) in enumerate(zip(self.products_list, self.product_quantity, self.product_price, self.product_stock), start=1):
            table.add_row([i, str(product)[:20], quantity, price, stock])

        # Set the alignment of columns
        table.align["SNO."] = "r"
        table.align["PRODUCT NAME"] = "l"
        table.align["QTY"] = "r"
        table.align["AMOUNT"] = "r"
        table.align["STOCK"] = "r"

        # Create the final formatted bill string
        final = f"{company}\n{address}\n{phone}\n{sample}\n{dt}\n\n{table}\n\nTOTAL PAYABLE : Rs.{sum(self.product_price)}\nThanks for visiting."

        with open(file_name, "w") as f:
            f.write(final)

        os.startfile(file_name, 'print')

        self.decrease_stock()
        self.clear_cart()

        tkinter.messagebox.showinfo("Success", "Everything is working fine")


    def decrease_stock(self):
        for x, product_id in enumerate(self.product_id):
            initial = "SELECT * FROM inventory WHERE id=?"
            result = c.execute(initial, (product_id,))

            for r in result:
                old_stock = r[2]
                new_stock = int(old_stock) - int(self.product_quantity[x])

                # Update the database
                sql = "UPDATE inventory SET stock=? WHERE id=?"
                c.execute(sql, (new_stock, product_id))
                conn.commit()

                # Insert data into transactions table
                sql = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
                c.execute(sql, (self.products_list[x], self.product_quantity[x], self.product_price[x], date))
                conn.commit()

    def clear_cart(self):
        # Check if the entry boxes are not empty
        if self.quantity_E.get() or self.discount_E.get() or self.change_E.get() or self.enteredid_E.get():
            tkinter.messagebox.showerror("Error", "Please clear all fields before proceeding")
            return
        for label in self.labels_list:
            label.destroy()

        self.products_list.clear()
        self.product_quantity.clear()
        self.product_stock.clear()
        self.product_id.clear()
        self.product_price.clear()

        self.total_L.configure(text="")
        self.change_E.delete(0, END)
        self.enteredid_E.focus()


def main():
    root = Tk()
    b = SalePoint(root)
    root.geometry("1366x768+100+0")
    root.title('Update Stock into database')

    try:
        root.mainloop()
    finally:
        conn.close()


if __name__ == "__main__":
    main()


