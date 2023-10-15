from tkinter import*
import sqlite3
import tkinter.messagebox
import datetime

conn = sqlite3.connect("D:\Storemanagement software\Database\store.db")
c= conn.cursor()

# date using globally=]
date =datetime.datetime.now().date()

#  temporary list like session
products_list =[]
product_price=[]
product_Quanity=[]
product_id=[]

class Application:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        # self.heading = Label(master,text="Add to the database", font="arial 40 bold", fg="steelblue")
        # self.heading.place(x=400,y=0)
        self.left=Frame(master,width=700,height=768,bg="wheat")
        self.left.pack(side=LEFT)

        self.right=Frame(master,width=666,height=768,bg="lightblue")
        self.right.pack(side=LEFT)

        # components
        self.heading = Label(self.left,text="Baby Garments Store", font="arial 40 bold",bg="wheat", fg="black")
        self.heading.place(x=0,y=0)

        self.date_L = Label(self.right,text="Today's Date: "+str(date), font="arial 18 bold",bg="white", fg="black")
        self.date_L.place(x=0,y=0)

        # table invoice ============================================================================================
        self.tproduct = Label(self.right,text="Products", font="arial 18 bold",bg="lightblue", fg="black")
        self.tproduct.place(x=0,y=60)

        self.tquantity = Label(self.right,text="Quantity", font="arial 18 bold",bg="lightblue", fg="black")
        self.tquantity.place(x=300,y=60)

        self.tamount = Label(self.right,text="Amount", font="arial 18 bold",bg="lightblue", fg="black")
        self.tamount.place(x=500,y=60)

        # enter stuff
        self.enteredid_L = Label(self.left,text="Enter Products ID", font="arial 18 bold",bg="wheat", fg="black")
        self.enteredid_L.place(x=0,y=80)

        self.enteredid_E= Entry(self.left,width=25, font="arial 18 bold",bg="lightblue" )
        self.enteredid_E.place(x=210,y=80)
        self.enteredid_E.focus()
        
        self.btn_search = Button(self.left,text="Search", width=25,height=2,bg="orange", command=self.ajax)
        self.btn_search.place(x=350,y=120)

        self.productname = Label(self.left,text="", font="arial 18 bold",bg="wheat", fg="blue")
        self.productname.place(x=0,y=250)


        self.prodPrice = Label(self.left,text="", font="arial 40 bold",bg="wheat", fg="green")
        self.prodPrice.place(x=0,y=290)

        # total label
        # self.total_L=Label
    def ajax(self,*args,**kwargs):
        self.get_id = self.enteredid_E.get()
        # get the product
        query ="SELECT id,name,sp,stock FROM inventory WHERE id=?"
        result=c.execute(query,(self.get_id),)
        for self.r in result:
            # print(self.r) #output (1, 'sandal', 600, 10)
            self.get_id=self.r[0]
            self.get_name = self.r[1]
            self.get_sp=self.r[2]
            self.get_stock=self.r[3]
        self.productname.configure(text=str(self.get_name).upper())
        self.prodPrice.configure(text="Price:(Rs."+str(self.get_sp)+")")

        self.quantity_L = Label(self.left,text="Enter Quantity", font="arial 18 bold",bg="wheat", fg="black")
        self.quantity_L.place(x=0,y=370)

        self.quantity_E= Entry(self.left,width=25, font="arial 18 bold",bg="lightblue" )
        self.quantity_E.place(x=190,y=370)
        self.quantity_E.focus()
        #  discount
        self.discount_L = Label(self.left,text="Enter Discount", font="arial 18 bold",bg="wheat", fg="black")
        self.discount_L.place(x=0,y=410)
        
        self.discount_E= Entry(self.left,width=25, font="arial 18 bold",bg="lightblue" )
        self.discount_E.place(x=190,y=410)
        self.discount_E.insert(END,0)

        self.add_to_cart_btn = Button(self.left,text="Add To Cart", width=20,height=2,bg="orange",command=self.add_To_Cart)
        self.add_to_cart_btn.place(x=365,y=450)

        # Generate bill and change
        self.change_L = Label(self.left,text="Paid Amount", font="arial 18 bold",bg="wheat", fg="black")
        self.change_L.place(x=0,y=550)
        self.change_E= Entry(self.left,width=25, font="arial 18 bold",bg="lightblue" )
        self.change_E.place(x=190,y=550)

        self.change_btn = Button(self.left,text="Calculate Change", width=20,height=2,bg="orange")
        self.change_btn.place(x=365,y=590)

        # Generate Bill Button
        self.bill_btn = Button(self.left,text="Generate Bill",font="arial 15 bold", width=30,height=2,bg="red",fg="white")
        self.bill_btn.place(x=2,y=640)

    def add_To_Cart(self,*args,**kwargs):
        #  get the quantity value
        self.quantity_value = int(self.quantity_E.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showerror("error","Demanded Quantity is not available in stock")
        else:
            # print("working great")
            # calculate the price
            self.final_price = float(self.quantity_value)*float(self.get_sp)
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_Quanity.append(self.quantity_value)
            product_id.append(self.get_id)
            print(products_list)
            print(product_price)
            print(product_Quanity)




root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.title('Point of Sale')
root.mainloop()