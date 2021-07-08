'''Python App using tkinter with integrated database using sqlite3
Author : Allevry
Date : 26/4/21
'''
from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

if __name__=="__main__":
# Variables
    fclick=False
    pm=''
#===================================================================================================
# Create Database
    con = sqlite3.connect("14_set5.db")
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Rental(receiptNum text,date text,
                company text,representative text,location text,statezip text,phoneRep text,
                name text,license text,address text,cityzip text,phoneLessee text,
                vin text,make text,year text,color text,regNum text,model text,mileage text,
                bill text,paymode text)""")
    con.commit()
    con.close()
#====================================================================================================
# Autofill Data
    def fill():
        global fclick,vin,lt,s,tax,tot,ap
        
        if v1.get()==''or cd.get()==''or d.get()==''or ac.get()=='':
            messagebox.showerror("Error","No Field(s) can be empty !")
        else:
            fclick=True                  # the fill button was clicked 
            vin.config(state='normal') 
            vin.insert(0,v1.get())    
            vin.config(state='disabled')
            lt.config(state='normal')
            A=round(float(cd.get())*float(d.get())+float(ac.get()), 2)
            lt.insert(0,str(A))
            lt.config(state='disabled')
            s.config(state='normal')
            s.insert(0,str(A))
            s.config(state='disabled')          
            tax.config(state='normal')
            B=round(A * 0.18 , 2)
            tax.insert(0,str(B))
            tax.config(state='disabled')            
            tot.config(state='normal')
            C=A+B
            tot.insert(0,str(C))
            tot.config(state='disabled')            
            ap.config(state='normal')
            ap.insert(0,str(C))
            ap.config(state='disabled')
# Validate
    def valid():
        if(e1.get()=='' or e2.get()=='' or
           r1.get()=='' or r2.get()=='' or r3.get()=='' or r4.get()=='' or r5.get()=='' or
           l1.get()=='' or l2.get()=='' or l3.get()=='' or l4.get()=='' or l5.get()=='' or
           v1.get()=='' or v2.get()=='' or v3.get()=='' or v4.get()=='' or
           v5.get()=='' or v6.get()=='' or v7.get()=='' or
           cd.get()=='' or d.get()=='' or ac.get()=='' or
           not 1<=pay.get()<=4 or (pay.get()==4 and other.get()=='') or
           (pay.get()==3 and card.get()=='') or (pay.get()==2 and cheq.get()=='')):
            messagebox.showerror("Error","No Field(s) can be empty !")
        elif not l2.get().isalnum() or len(l2.get())!=16:
            messagebox.showerror("Error","Invalid License Number!")
        elif not r5.get().isdigit() or len(r5.get())!=10:
            messagebox.showerror("Error","Invalid Company Phone number!")
        elif not l5.get().isdigit() or len(l5.get())!=10:
            messagebox.showerror("Error","Invalid Lessee Phone number!")
        elif not v1.get().isalnum() or len(v1.get())!=17:
            messagebox.showerror("Error","Invalid Vehicle Id Number!")
        elif not v5.get().isalnum() or len(v5.get())!=10:
            messagebox.showerror("Error","Invalid Registration number!")
        elif not v3.get().isdigit() or len(v3.get())!=4:
            messagebox.showerror("Error","Invalid Year!")
        elif not check(v7.get()):
            messagebox.showerror("Error","Invalid Mileage!")
        elif not check(cd.get()):
            messagebox.showerror("Error","Invalid Cost/Day!")
        elif not check(d.get()):
            messagebox.showerror("Error","Invalid No. of Days!")
        elif not check(ac.get()):
            messagebox.showerror("Error","Invalid Additional Cost!")
        elif not fclick:
            messagebox.showerror("Error","Click on Fill !")
        else:
            reg()           
# Register
    def reg():
        if pay.get()==1:pm="Cash"
        elif pay.get()==2:pm="Cheque : "+cheq.get()
        elif pay.get()==3:pm="Credit Card : "+card.get()
        else:pm=other.get() 
    # the variables being inserted into the Table
    # e1,e2,r1,r2,r3,r4,r5,l1,l2,l3,l4,l5,v1,v2,v3,v4,v5,v6,v7,tot,ap,pm
        con = sqlite3.connect("14_set5.db")
        c = con.cursor()
        c.execute("INSERT INTO Rental VALUES (:a,:b,:c,:d,:e,:f,:g,:h,:i,:j,:k,:l,:m,:n,:o,:p,:q,:r,:s,:t,:v)",
                {   'a':e2.get(),'b':e1.get(),               
                    'c':r1.get(),'d':r2.get(),'e':r3.get(),'f':r4.get(),'g':r5.get(),
                    'h':l1.get(),'i':l2.get(),'j':l3.get(),'k':l4.get(),'l':l5.get(),
                    'm':v1.get(),'n':v2.get(),'o':v3.get(),'p':v4.get(),'q':v5.get(),'r':v6.get(),'s':v7.get(),
                    't':tot.get(),'v':pm   })
        con.commit()
        con.close()
        messagebox.showinfo("Success","Submitted !")          
# Show
    def show():
        con = sqlite3.connect("14_set5.db")
        c = con.cursor()
        c.execute("SELECT * FROM Rental")
        datas = c.fetchall()
        con.close()
    #display database    
        ob=Tk()
        ob.title("Rental Database")
        ob.geometry("1365x695+-7+0")
        scrollx = Scrollbar(ob, orient=HORIZONTAL)
        tree=ttk.Treeview(ob,column=("a","b","c","d","e","f","g","h","i","j","k",
                                     "l","m","n","o","p","q","r","s","t","u"),
                          show='headings',selectmode="extended", height=100,
                          xscrollcommand=scrollx.set)
        scrollx.config(command=tree.xview)
        scrollx.pack(side=BOTTOM, fill=X)
        tree.heading("#1", text="Receipt #")
        tree.heading("#2", text="Date")
        tree.heading("#3", text="Company")
        tree.heading("#4", text="Representative")
        tree.heading("#5", text="Location")
        tree.heading("#6", text="State/zip")
        tree.heading("#7", text="Phone")
        tree.heading("#8", text="Lessee Name")
        tree.heading("#9", text="License #")
        tree.heading("#10", text="Address")
        tree.heading("#11", text="City/zip")
        tree.heading("#12", text="Phone")
        tree.heading("#13", text="VIN")
        tree.heading("#14", text="Make")
        tree.heading("#15", text="Year")
        tree.heading("#16", text="Color")
        tree.heading("#17", text="Reg. no.")
        tree.heading("#18", text="Model")
        tree.heading("#19", text="Mileage (km/L)")
        tree.heading("#20", text="Bill (Rs.)")
        tree.heading("#21", text="Paymode")
        for row in datas:
            tree.insert("", END, values=row)
        tree.pack()
        ob.mainloop()    
# Clear Screen    
    def clr():
        e1.delete(0,END)
        e2.delete(0,END)
        r1.delete(0,END)
        r2.delete(0,END)
        r3.delete(0,END)
        r4.delete(0,END)
        r5.delete(0,END)
        l1.delete(0,END)
        l2.delete(0,END)
        l3.delete(0,END)
        l4.delete(0,END)
        l5.delete(0,END)
        v1.delete(0,END)
        v2.delete(0,END)
        v3.delete(0,END)
        v4.delete(0,END)
        v5.delete(0,END)
        v6.delete(0,END)
        v7.delete(0,END)
        cd.delete(0,END)
        d.delete(0,END)
        ac.delete(0,END)
        vin.config(state='normal')
        vin.delete(0,END)
        vin.config(state='disabled')
        lt.config(state='normal')
        lt.delete(0,END)
        lt.config(state='disabled')
        s.config(state='normal')
        s.delete(0,END)
        s.config(state='disabled')
        tax.config(state='normal')
        tax.delete(0,END)
        tax.config(state='disabled')
        tot.config(state='normal')
        tot.delete(0,END)
        tot.config(state='disabled')
        ap.config(state='normal')
        ap.delete(0,END)
        ap.config(state='disabled')
        pay.set(None)
        cheq.delete(0,END)
        card.delete(0,END)
        other.delete(0,END)        
# Numeric data check
    def check(a):
        if not a.isdigit():
            try:
                a =float(a)
            except:
                return False
        return True
#====================================================================================================
# Main Frame 
    root=Tk()
    root.title("014   Set5")
    root.geometry("+380+100")
# Receipt BLock
    Label(root, text="Rental Receipt", font=("",14),fg='darkred').grid(row=0,column=2)
    Label(root, text="Date").grid(row=1,column=0)
    Label(root, text="Receipt #").grid(row=2,column=0)
    e1=Entry(root)
    e2=Entry(root)
    e1.grid(row=1,column=1)
    e2.grid(row=2,column=1)
# Company Info
    Label(root, text="Company Info", font=("",12),fg='brown').grid(row=3,column=1)
    Label(root, text="Rental Company").grid(row=4,column=0)
    Label(root, text="Representative").grid(row=5,column=0)
    Label(root, text="Location").grid(row=6,column=0)
    Label(root, text="City/State/ZIP").grid(row=7,column=0)
    Label(root, text="Phone").grid(row=8,column=0)
    r1= Entry(root)
    r2= Entry(root)
    r3= Entry(root)
    r4= Entry(root)
    r5= Entry(root)
    r1.grid(row=4,column=1)
    r2.grid(row=5,column=1)
    r3.grid(row=6,column=1)
    r4.grid(row=7,column=1)
    r5.grid(row=8,column=1)
# Lessee Info
    Label(root, text="Lessee Info", font=("",12),fg='brown').grid(row=3,column=3)
    Label(root, text="Name").grid(row=4,column=2)
    Label(root, text="License #").grid(row=5,column=2)
    Label(root, text="Address").grid(row=6,column=2)
    Label(root, text="City/State/ZIP").grid(row=7,column=2)
    Label(root, text="Phone").grid(row=8,column=2)
    l1= Entry(root)
    l2= Entry(root)
    l3= Entry(root)
    l4= Entry(root)
    l5= Entry(root)
    l1.grid(row=4,column=3)
    l2.grid(row=5,column=3)
    l3.grid(row=6,column=3)
    l4.grid(row=7,column=3)
    l5.grid(row=8,column=3)
# Vehicle Info
    Label(root, text="Vehicle Info", font=("",12),fg='brown').grid(row=9,column=2)
    Label(root, text="VIN").grid(row=10,column=0)
    Label(root, text="Make").grid(row=11,column=0)
    Label(root, text="Year").grid(row=12,column=0)
    Label(root, text="Color").grid(row=13,column=0)
    Label(root, text="Registration No.").grid(row=10,column=2)
    Label(root, text="Model").grid(row=11,column=2)
    Label(root, text="Mileage").grid(row=12,column=2)
    v1= Entry(root)
    v2= Entry(root)
    v3= Entry(root)
    v4= Entry(root)
    v5= Entry(root)
    v6= Entry(root)
    v7= Entry(root)
    v1.grid(row=10,column=1)
    v2.grid(row=11,column=1)
    v3.grid(row=12,column=1)
    v4.grid(row=13,column=1)
    v5.grid(row=10,column=3)
    v6.grid(row=11,column=3)
    v7.grid(row=12,column=3)
# Table
    Label(root, text="VIN").grid(row=14,column=0)
    Label(root, text="Cost/Day").grid(row=14,column=1)
    Label(root, text="# of Days").grid(row=14,column=2)
    Label(root, text="Additional Costs").grid(row=14,column=3)
    Label(root, text="Line Total").grid(row=14,column=4)
    vin=Entry(root,state='disabled')
    cd=Entry(root)
    d=Entry(root)
    ac=Entry(root)
    lt=Entry(root,state='disabled')
    vin.grid(row=15,column=0)
    cd.grid(row=15,column=1)
    d.grid(row=15,column=2)
    ac.grid(row=15,column=3)
    lt.grid(row=15,column=4)
# Subtotal
    Label(root, text="Subtotal").grid(row=16,column=3)
    Label(root, text="Tax (18%)").grid(row=17,column=3)
    Label(root, text="Total").grid(row=18,column=3)
    Label(root, text="Amount Paid").grid(row=19,column=3)
    s=Entry(root,state='disabled')
    tax=Entry(root,state='disabled')
    tot=Entry(root,state='disabled')
    ap=Entry(root,state='disabled')
    s.grid(row=16,column=4)
    tax.grid(row=17,column=4)
    tot.grid(row=18,column=4)
    ap.grid(row=19,column=4)
# Payment
    pay = IntVar()
    Label(root, text="Payment Method - ",font=("",11),fg='brown').grid(row=16,column=0)
    Radiobutton(root, text="          Cash",variable=pay,value=1).grid(row=17,)
    Radiobutton(root, text="     Cheque",variable=pay,value=2).grid(row=18,)
    Radiobutton(root, text="Credit Card",variable=pay,value=3).grid(row=19,)
    Radiobutton(root, text="         Other",variable=pay,value=4).grid(row=20,)
    cheq = Entry(root)
    card = Entry(root)
    other=Entry(root)
    cheq.grid(row=18,column=1)
    card.grid(row=19,column=1)
    other.grid(row=20,column=1)
# Buttons
    Label(root, text="\n\n").grid(row=21,)
    sub=Button(root,text="Submit→",command=valid,cursor = "hand2",font=("",14),bg="lightgreen",fg="darkgreen")
    sub.place(x=310,y=475)
    fil=Button(root,text="Fill ↑",command=fill,cursor="hand2",font=("",10),bg="lightgray",fg="blue")
    fil.place(x=582,y=440)
    clear=Button(root,text="←  Clear",command=clr,cursor="hand2",font=("",14),bg="pink",fg="red")
    clear.place(x=215,y=475)
    see=Button(root,text="Show ►",command=show,cursor="hand2",font=("",12),bg="skyblue",fg="darkblue")
    see.place(x=550,y=481)
# Initiate GUI
    root.mainloop()
