from tkinter import*
import sqlite3
import tkinter.messagebox
conn = sqlite3.connect("D:\Storemanagement software\Database\store.db")
c= conn.cursor()

result = c.execute("SELECT MAX(id) FROM inventory")
for row in result:
    Id = row[0]

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text="Add to the database", font="arial 40 bold", fg="steelblue")
        self.heading.place(x=400,y=0)

        # self.I=Label(master,text="ID has reached upto: "+str(Id),font="arial 18 bold")
        # self.I.place(x=0,y=40)

        # labels and entries for the product 
        self.name_L = Label(master,text="Enter product name", font="arial 18 bold")
        self.name_L.place(x=0,y=70)

        self.stock_L = Label(master,text="Enter stocks", font="arial 18 bold")
        self.stock_L.place(x=0,y=120)

        self.cp_L = Label(master,text="Enter Cost Price", font="arial 18 bold")
        self.cp_L.place(x=0,y=170)

        self.sp_L = Label(master,text="Enter Sale Price", font="arial 18 bold")
        self.sp_L.place(x=0,y=220)

        

        self.vendor_L = Label(master,text="Enter Dealer's Name", font="arial 18 bold")
        self.vendor_L.place(x=0,y=270)

        self.vedor_phone_L = Label(master,text="Enter Dealer's Phone Number", font="arial 18 bold")
        self.vedor_phone_L.place(x=0,y=320)

        self.Id_L = Label(master,text="Enter ID", font="arial 18 bold")
        self.Id_L.place(x=0,y=370)

        # entries for the labels 
        self.name_E=Entry(master,width=25,font="arial 18 bold")
        self.name_E.place(x=380,y=70)

        self.stock_E=Entry(master,width=25,font="arial 18 bold")
        self.stock_E.place(x=380,y=120)

        self.cp_E=Entry(master,width=25,font="arial 18 bold")
        self.cp_E.place(x=380,y=170)

        self.sp_E=Entry(master,width=25,font="arial 18 bold")
        self.sp_E.place(x=380,y=220)

        self.vendor_E=Entry(master,width=25,font="arial 18 bold")
        self.vendor_E.place(x=380,y=270)

        self.vendor_phone_E=Entry(master,width=25,font="arial 18 bold")
        self.vendor_phone_E.place(x=380,y=320)

        self.Id_e = Entry(master, width=25,font="arial 18 bold")
        self.Id_e.place(x=380,y=370)

        # button add to the database 
        self.btn_add=Button(master,text="Add To DataBase", width=25, height=2, bg="steelblue", fg="white", command=self.get_Entries)
        self.btn_add.place(x=520,y=420)
        # clear entries 
        self.btn_clear=Button(master,text="Clear All Fields", width=25, height=2, bg="steelblue", fg="white", command=self.clear_all)
        self.btn_clear.place(x=350,y=420)

        # text box for the logs 
        self.tBox=Text(master, width=60,height=18)
        self.tBox.place(x=740,y=70)
        self.tBox.insert(END,"Id has been reached: "+str(Id))

        self.master.bind('<Return>',self.get_Entries)
        self.master.bind('<Up>',self.clear_all)


    def get_Entries(self,*args,**kwargs):
        # get data from entries 
        self.name= self.name_E.get()
        self.stock= self.stock_E.get()
        self.cp = self.cp_E.get()
        self.sp = self.sp_E.get()
        self.vendor=self.vendor_E.get()
        self.vendor_phone=self.vendor_phone_E.get()

        # dynamic entries 
        self.totalcp =float(self.cp)*float(self.stock)
        self.totalsp = float(self.sp)*float(self.stock)
        self.assumed_profit = float(self.totalsp-self.totalcp)
        if self.name == "" or self.stock =="" or self.cp == "" or self.sp=="":
            tkinter.messagebox.showinfo('error','Please fill all the entries')
        else:
            # print(self.name,self.stock,self.cp,self.sp,self.vendor,self.vendor_phone)

            sql = "INSERT INTO inventory (name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phone) VALUES (?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendor_phone))
            conn.commit()
            self.tBox.insert(END,"\n\nInserted  "+str(self.name)+ " into database with code: "+ str(self.Id_e.get()))

            tkinter.messagebox.showinfo('Success',"Successfully added to the database")


    def clear_all(self,*args,**kwargs):
        num= Id+1
        self.name_E.delete(0,END)
        self.stock_E.delete(0,END)
        self.cp_E.delete(0,END)
        self.sp_E.delete(0,END)
        self.vendor_E.delete(0,END)
        self.vendor_phone_E.delete(0,END)
        self.Id_e.delete(0,END)
        # self.tBox.insert(END,"Id has been reached "+str(num))





# root = Tk()
# b = Database(root)
# root.geometry("1366x768+0+0")
# root.title('Add to tha database')
# root.mainloop()

def main():
    root = Tk()
    b = Database(root)
    root.geometry("1366x768+0+0")
    root.title('Add to tha database')
    root.mainloop()

if __name__ == "__main__":
    main()



