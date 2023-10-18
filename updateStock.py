from tkinter import*
import sqlite3
import tkinter.messagebox
conn = sqlite3.connect("D:\Storemanagement software\Database\store.db")
c= conn.cursor()

result = c.execute("SELECT MAX(id) FROM inventory")
for row in result:
    Id = row[0]

class UpdateDatabase:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text="Update The Stock into  Database", font="arial 40 bold",bg="green", fg="white")
        self.heading.place(x=370,y=0)
        master.configure(bg="green")

        # lable and entries for Id
        self.Id_Le = Label(master, text="Eneter ID",font="arial 18 bold")
        self.Id_Le.place(x=0,y=70)

        self.Id_leb = Entry(master,font="arial 18 bold",width=10)
        self.Id_leb.place(x=380,y=70)

        self.btn_search = Button(master,text="Search", width=15,height=2,bg="orange",command=self.Search)
        self.btn_search.place(x=550,y=68)

        # labels and entries for the product 
        self.name_L = Label(master,text="Enter product name", font="arial 18 bold")
        self.name_L.place(x=0,y=120)

        self.stock_L = Label(master,text="Enter stocks", font="arial 18 bold")
        self.stock_L.place(x=0,y=170)

        self.cp_L = Label(master,text="Enter Cost Price", font="arial 18 bold")
        self.cp_L.place(x=0,y=220)

        self.sp_L = Label(master,text="Enter Sale Price", font="arial 18 bold")
        self.sp_L.place(x=0,y=270)

        self.totalcp_L = Label(master,text="Enter Total Cost Price", font="arial 18 bold")
        self.totalcp_L.place(x=0,y=320)

        self.totalsp_L = Label(master,text="Enter Total Sale Price", font="arial 18 bold")
        self.totalsp_L.place(x=0,y=370)

        self.vendor_L = Label(master,text="Enter Dealer's Name", font="arial 18 bold")
        self.vendor_L.place(x=0,y=420)

        self.vedor_phone_L = Label(master,text="Enter Dealer's Phone Number", font="arial 18 bold")
        self.vedor_phone_L.place(x=0,y=470)

       
        # entries for the labels 
        self.name_E=Entry(master,width=25,font="arial 18 bold")
        self.name_E.place(x=380,y=120)

        self.stock_E=Entry(master,width=25,font="arial 18 bold")
        self.stock_E.place(x=380,y=170)

        self.cp_E=Entry(master,width=25,font="arial 18 bold")
        self.cp_E.place(x=380,y=220)

        self.sp_E=Entry(master,width=25,font="arial 18 bold")
        self.sp_E.place(x=380,y=270)

        self.totalcp_E =Entry(master,width=25,font="arial 18 bold")
        self.totalcp_E.place(x=380,y=320)

        self.totalsp_E =Entry(master,width=25,font="arial 18 bold")
        self.totalsp_E.place(x=380,y=370)

        self.vendor_E=Entry(master,width=25,font="arial 18 bold")
        self.vendor_E.place(x=380,y=420)

        self.vendor_phone_E=Entry(master,width=25,font="arial 18 bold")
        self.vendor_phone_E.place(x=380,y=470)

        # button add to the database 
        self.btn_update=Button(master,text="Update",font="arial 15 bold", width=12, height=2, bg="steelblue", fg="white",command=self.Update)
        self.btn_update.place(x=550,y=520)

        # text box for the logs 
        self.tBox=Text(master, width=60,height=18)
        self.tBox.place(x=740,y=70)
        self.tBox.insert(END,"Id has been reached upto : "+str(Id))

    def Search(self,*args,**kwargs):
        sql="SELECT * FROM inventory WHERE id=?"
        result=c.execute(sql,(self.Id_leb.get(),))
        # print(result) #it will give sqlite obj genrator
        
        for r in result:
            self.n1=r[1]#name
            self.n2=r[2]#stock
            self.n3=r[3]#cp
            self.n4=r[4]#sp
            self.n5=r[5]#totalcp
            self.n6=r[6]#totalsp
            self.n7=r[7]#assumed profit
            self.n8=r[8]#vendor
            self.n9=r[9]#vendor phone
        conn.commit()

        # insert into entries to update
        self.name_E.delete(0,END)
        self.name_E.insert(0,str(self.n1))

        self.stock_E.delete(0,END)
        self.stock_E.insert(0,str(self.n2))

        self.cp_E.delete(0,END)
        self.cp_E.insert(0,str(self.n3))

        self.sp_E.delete(0,END)
        self.sp_E.insert(0,str(self.n4))

        self.totalcp_E.delete(0,END)
        self.totalcp_E.insert(0,str(self.n5))

        self.totalsp_E.delete(0,END)
        self.totalsp_E.insert(0,str(self.n6))

        self.vendor_E.delete(0,END)
        self.vendor_E.insert(0,str(self.n8))

        self.vendor_phone_E.delete(0,END)
        self.vendor_phone_E.insert(0,str(self.n9))

    def Update(self,*args,**kwargs):
        
        self.update_name=self.name_E.get()
        self.update_stock=self.stock_E.get()
        self.update_cp=self.cp_E.get()
        self.update_sp=self.sp_E.get()
        self.update_totalcp=self.totalcp_E.get()
        self.update_totalsp=self.totalsp_E.get()
        self.update_vendor=self.vendor_E.get()
        self.update_vendor_phone=self.vendor_phone_E.get()

        # dynamic entries 
        self.totalcp =float(self.update_cp)*float(self.update_stock)
        self.totalsp = float(self.update_sp)*float(self.update_stock)
        self.assumed_profit = float(self.totalsp-self.totalcp)

        query="UPDATE inventory SET name=?,stock=?,cp=?,sp=?,totalcp=?,totalsp=?,assumed_profit=?,vendor=?,vendor_phone=? WHERE id=?"
        # c.execute(query,(self.update_name,self.update_stock,self.update_cp,self.update_sp,self.update_totalcp,self.update_totalsp,self.update_vendor,self.update_vendor_phone,self.Id_leb.get()))
        c.execute(query,(self.update_name,self.update_stock,self.update_cp,self.update_sp,self.totalcp,self.totalsp,self.assumed_profit,self.update_vendor,self.update_vendor_phone,self.Id_leb.get()))
        conn.commit()

        tkinter.messagebox.showinfo('Success','updated successfully')



def main():
    root = Tk()
    b = UpdateDatabase(root)
    root.geometry("1366x768+0+0")
    root.title('Udate Stock into database')

    root.mainloop()

if __name__ == "__main__":
    main()