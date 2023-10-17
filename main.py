from tkinter import*
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random


conn = sqlite3.connect("D:\Storemanagement software\Database\store.db")
c= conn.cursor()

# date using globally=]
date =datetime.datetime.now().date()

#  temporary list like session
products_list =[]
product_price=[]
product_Quanity=[]
product_id=[]

# list for labels 
labels_list=[]

class SalePoint:
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
        self.total_L = Label(self.right,text="", font="arial 40 bold",bg="lightblue", fg="black")
        self.total_L.place(x=0,y=600)
    def ajax(self,*args,**kwargs):
        self.get_id = self.enteredid_E.get()
        # print(self.get_id)
        # get the product
        query ="SELECT id,name,sp,stock FROM inventory WHERE id=?"
        # result=c.execute(query,(self.get_id))
        # print("Query:", query)
        # print("Values:", (self.get_id,))
        result = c.execute(query, (self.get_id,))

        for self.r in result:
            # print(self.r) #output (1, 'sandal', 600, 10)
            # self.get_id=self.get_id
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
        self.change_L = Label(self.left,text="Given Amount", font="arial 18 bold",bg="wheat", fg="black")
        self.change_L.place(x=0,y=550)
        self.change_E= Entry(self.left,width=25, font="arial 18 bold",bg="lightblue" )
        self.change_E.place(x=190,y=550)

        self.change_btn = Button(self.left,text="Calculate Change", width=20,height=2,bg="orange", command=self.change_func)
        self.change_btn.place(x=365,y=590)

        # Generate Bill Button
        self.bill_btn = Button(self.left,text="Generate Bill",font="arial 15 bold", width=30,height=2,bg="red",fg="white",command=self.generate_bill)
        self.bill_btn.place(x=2,y=640)

    def add_To_Cart(self,*args,**kwargs):
        #  get the quantity value
        self.quantity_value = int(self.quantity_E.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showerror("error","Demanded Quantity is not available in stock")
        else:
            # print("working great")
            # calculate the price
            self.final_price = (float(self.quantity_value)*float(self.get_sp))-(float(self.discount_E.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_Quanity.append(self.quantity_value)
            product_id.append(self.get_id)
            # print(products_list)
            # print(product_price)
            # print(product_Quanity)

            self.x_index=0
            self.y_index=100
            self.counter=0
            for self.p in products_list:
                self.tempname=Label(self.right,text=str(products_list[self.counter]),font="arial 15 bold",bg="lightblue", fg="black" )
                self.tempname.place(x=0,y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqt=Label(self.right,text=str(product_Quanity[self.counter]),font="arial 15 bold",bg="lightblue", fg="black" )
                self.tempqt.place(x=300,y=self.y_index)
                labels_list.append(self.tempqt)

                self.tempprice=Label(self.right,text=str(product_price[self.counter]),font="arial 15 bold",bg="lightblue", fg="black" )
                self.tempprice.place(x=500,y=self.y_index)
                labels_list.append(self.tempprice)


                self.y_index +=40
                self.counter+=1

                # total configure 
                self.total_L.configure(text="Total : Rs."+str(sum(product_price)))


                # delete or clear when data added to the database 
                self.quantity_L.place_forget()
                self.quantity_E.place_forget()
                self.discount_L.place_forget()
                self.discount_E.place_forget()
                # self.change_L.place_forget()
                # self.change_E.place_forget()
                # make them default 
                self.productname.configure(text="")
                self.prodPrice.configure(text="")
                # destroy the add to cart button 
                self.add_to_cart_btn.destroy()
                # self.change_btn.destroy()

                # Auto focus to the enter id 
                self.enteredid_E.focus()
                self.enteredid_E.delete(0,END) 


    def change_func(self,*args,**kwargs):
        # get the amount given by customer and amount generated by computer 
        self.amount_given =float(self.change_E.get())
        self.our_total =float(sum(product_price))

        self.to_give=float(self.amount_given)-float(self.our_total)

        # label change
        self.change_amount=Label(self.left,text="Change amount: Rs. "+str(self.to_give), font=("arial 18 bold"),bg="wheat", fg="red")
        self.change_amount.place(x=300,y=550)

    def generate_bill(self,*args,**kwargs):
        # create biil
        directory="D:/Storemanagement software/"+str(date)+"/"
        if not os.path.exists(directory):
            os.mkdir(directory)

        #  Template
        compnay="\t\t\t\t    BABY GARMENTS & SHOES\n"
        address="\t\t\t\tNear Telenor Franchise Piplan\n"
        phone="\t\t\t\t\t0300-4602762\n"
        sample="\t\t\t\t\tINVOICE\n"
        dt="\t\t\t\t\t"+str(date)
        table_header="\n\n\t------------------------------------------------------\n\t SNO.\t\tPRODUCT NAME \t\tQTY\t\tAMOUNT\n\t------------------------------------------------------"
        final=compnay + address + phone+sample+dt+"\n"+table_header
        # open file to write it to 
        file_name=str(directory)+str(random.randrange(5000,10000))+".rtf"
        f = open(file_name,"w")
        f.write(final)
        f.close


        # #  first decrease the stock 
        # self.x=0

        # initial="SELECT * FROM inventory WHERE id=?"
        # result=c.execute(initial,(product_id[self.x],))

        # for i in products_list:
        #     for r in result:
        #         self.old_stock=r[2]
        #     self.new_stock = int(self.old_stock)-int(product_Quanity[self.x])

        #     # updating the database
        #     sql = "UPDATE inventory SET stock=? WHERE id=?"
        #     c.execute(sql,(self.new_stock,product_id[self.x]))
        #     conn.commit()

        #     # inserting data into transactions table 
        #     sql="INSERT INTO transactions (product_name,quantity,amount,date)VALUES(?,?,?,?)"
        #     c.execute(sql,(products_list[self.x],product_Quanity[self.x],product_price[self.x],date))
        #     conn.commit()

        #     self.x+=1
        #      # print statements 
        #     # print(self.new_stock)
        #     # print("decreased")

        #     for a in labels_list:
        #         a.destroy()

        #     del(product_Quanity[:])
        #     del(product_id[:])
        #     del(product_Quanity[:])
        #     del(product_price[:])

        #     self.total_L.configure(text="")
        #     self.change_amount.configure(text="")
        #     self.change_E.delete(0,END)
        #     self.enteredid_E.focus()
        tkinter.messagebox.showinfo("Success","Evry thing is working fine")


           



def main():
    root = Tk()
    b = SalePoint(root)
    root.geometry("1366x768+0+0")
    root.title('Udate Stock into database')

    root.mainloop()

if __name__ == "__main__":
    main()

# root = Tk()
# b = Application(root)
# root.geometry("1366x768+0+0")
# root.title('Point of Sale')
# root.mainloop()
