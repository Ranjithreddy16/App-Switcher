  
from tkinter import*
from tkinter import messagebox
import random

root=Tk()
root.title("my notpad")
root.geometry("500x500")
root.configure(width=50,height=50)
c=Canvas(root,bg="light green",height=800,width=800,cursor="arrow")
r=c.create_rectangle(50,170,400,400,width=2,fill="light pink",outline="black")

c.propagate()
c.pack()
#page1 labels
l1=Label(root,text="enter user name :",bg="light pink")
l1.place(x=80,y=200)
l2=Label(root,text="enter passward :",bg="light pink")
l2.place(x=80,y=250)
l4=Label(root,text="enter 0 to conform :",bg="light pink")
l4.place(x=80,y=300)
l3=Label(root,text="WELCOME TO MULTI APP",bg="light green",font=("Helevetica",20))
l3.place(x=95,y=30)
#page1 entry 
ee1=Entry(root,width=20)
ee1.place(x=230,y=200)
ee2=Entry(root,width=20)
ee2.place(x=230,y=250)
ee3=Entry(root,width=20)
ee3.place(x=230,y=300)
#page1 buttons



def vinay1():
    ll=['vinay','chintu','prabhu','prasad','meena']
    lll=['1200','1201','1202','1203','1204']
    a=ee1.get()
    b=ee2.get()
    c=ee3.get()
    if a in ll:
        if b in lll:
            b11=Button(root,text="next",bg="light pink",command=openwindow3)
            b11.place(x=350,y=350)
            l66=Label(root,text="next slide -> ",bg="light pink",)
            l66.place(x=250,y=350)
        else:
            l44=Label(root,text="wrong passward",bg="light pink")
            l44.place(x=200,y=225)
            
    else:
        l55=Label(root,text="wrong user name",bg="light pink")
        l55.place(x=200,y=175)
    
    
    ee1.delete(0,END)
    ee2.delete(0,END)
    ee3.delete(0,END)



new_window3=""
def openwindow3():
    global new_window3
    new_window3=Toplevel(root)
    new_window3.geometry("400x400")
    cc=Canvas(new_window3,bg="light green",height=800,width=800,cursor="arrow")
    rr=c.create_rectangle(50,170,400,400,width=2,fill="light pink",outline="black")

    cc.propagate()
    cc.pack()
    new_window3.title("new window")
    new_window3.resizable(False,False)
    
    
    labelab=Label(new_window3,text="WELCOME TO MULTI APP",bg="light green",font=("Helevetica",15))
    labelab.place(x=80,y=50)
    
    b1=Button(new_window3,text="tic tac toe",bg="light pink",command=openwindow2)
    b1.place(x=230,y=300)
    ba1=Button(new_window3,text="calculator",bg="light pink",command=openwindow1)
    ba1.place(x=80,y=300)
    





#caliculater window program    
new_window1=""
def openwindow1():
    global new_window1
    new_window1=Toplevel(root)
    new_window1.geometry("600x600")
    new_window1.title("new window")
    c1=Canvas(new_window1,bg="light green",height=700,width=1200,cursor="arrow")
    r=c1.create_rectangle(40,40,353,510,width=2,fill="light pink",outline="black")
    c1.propagate()
    c1.pack()
    
    new_window1.resizable(False,False)
    lbl=Label(new_window1,text="i am in new_window1 caliculater")
    lbl.pack()
    btn2=Button(new_window1,text="close me",command=lambda:new_window1.destroy())
    btn2.pack()
    
    e=Entry(new_window1,width=40,borderwidth=5)
    e.place(x=70,y=50)


    def button_click(number):
        #e.delete(0,END)
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))
    
    def button_clear():
        e.delete(0,END)
    
    def button_add():
        first_number=e.get()
        global f_num
        global a
        a="+"
        f_num=int(first_number)
        e.delete(0,END)
    
    def button_subtract():
        first_number=e.get()
        global f_num
        global a
        a="-"
        f_num=int(first_number)
        e.delete(0,END)
    
    def button_equal():
        second_number=e.get()
        e.delete(0,END)
        if a=="/":
            e.insert(0,f_num // int(second_number))
        if a=="+":
            e.insert(0,f_num + int(second_number))
        if a=="-":
            e.insert(0,f_num - int(second_number))
        if a=="*":
            e.insert(0,f_num * int(second_number))
        
    
    def button_multiply():
        first_number=e.get()
        global f_num
        global a
        a="*"
        f_num=int(first_number)
        e.delete(0,END)

    def button_divide():
        first_number=e.get()
        global f_num
        global a
        a="/"
        f_num=int(first_number)
        e.delete(0,END)


    button_1=Button(new_window1,text="1",padx=40,pady=20,command=lambda:button_click("1"))
    button_2=Button(new_window1,text="2",padx=40,pady=20,command=lambda:button_click("2"))
    button_3=Button(new_window1,text="3",padx=40,pady=20,command=lambda:button_click("3"))
    button_4=Button(new_window1,text="4",padx=40,pady=20,command=lambda:button_click("4"))
    button_5=Button(new_window1,text="5",padx=40,pady=20,command=lambda:button_click("5"))
    button_6=Button(new_window1,text="6",padx=40,pady=20,command=lambda:button_click("6"))
    button_7=Button(new_window1,text="7",padx=40,pady=20,command=lambda:button_click("7"))
    button_8=Button(new_window1,text="8",padx=40,pady=20,command=lambda:button_click("8"))
    button_9=Button(new_window1,text="9",padx=40,pady=20,command=lambda:button_click("9"))
    button_0=Button(new_window1,text="0",padx=40,pady=20,command=lambda:button_click("0"))
    button_add=Button(new_window1,text="+",padx=39,pady=20,command=button_add)
    button_equal=Button(new_window1,text="=",padx=89,pady=20,command=button_equal)
    button_clear=Button(new_window1,text="clear",padx=81,pady=20,command=button_clear)
    button_subtract=Button(new_window1,text="-",padx=40,pady=20,command=button_subtract)
    button_multiply=Button(new_window1,text="*",padx=40,pady=20,command=button_multiply)
    button_divide=Button(new_window1,text="/",padx=40,pady=20,command=button_divide)

    button_1.place(x=50,y=90)
    button_2.place(x=150,y=90)
    button_3.place(x=250,y=90)

    button_4.place(x=50,y=160)
    button_5.place(x=150,y=160)
    button_6.place(x=250,y=160)

    button_7.place(x=50,y=230)
    button_8.place(x=150,y=230)
    button_9.place(x=250,y=230)

    button_0.place(x=50,y=300)
    button_subtract.place(x=150,y=300)
    button_multiply.place(x=250,y=300)

    button_equal.place(x=150,y=370)
    button_add.place(x=50,y=370)

    button_divide.place(x=50,y=440)
    button_clear.place(x=150,y=440)


new_window2=""
def openwindow2():
    global new_window2
    new_window2=Toplevel(root)
    new_window2.geometry("600x600")
    new_window2.title("new window")
    c2=Canvas(new_window2,bg="light green",height=700,width=1200,cursor="arrow")
    r=c2.create_rectangle(105,90,450,480,width=2,fill="light pink",outline="black")
    c2.propagate()
    c2.pack()
    
    new_window2.resizable(False,False)
    clicked = True
    count = 0

    def disable_all_buttons():
        bb1.config(state=DISABLED)
        bb2.config(state=DISABLED)
        bb3.config(state=DISABLED)
        bb4.config(state=DISABLED)
        bb5.config(state=DISABLED)
        bb6.config(state=DISABLED)
        bb7.config(state=DISABLED)
        bb8.config(state=DISABLED)
        bb9.config(state=DISABLED)

    
    def checkifwon():
        global winner
        winner = False
        #x's program
        if bb1["text"] == "x" and bb2["text"] == "x" and bb3["text"] == "x":
            bb1.config(bg="red")
            bb2.config(bg="red")
            bb3.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        
        elif bb4["text"] == "x" and bb5["text"] == "x" and bb6["text"] == "x":
            bb4.config(bg="red")
            bb5.config(bg="red")
            bb6.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        
        elif bb7["text"] == "x" and bb8["text"] == "x" and bb9["text"] == "x":
            bb7.config(bg="red")
            bb8.config(bg="red")
            bb9.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        
        elif bb1["text"] == "x" and bb4["text"] == "x" and bb7["text"] == "x":
            bb1.config(bg="red")
            bb4.config(bg="red")
            bb7.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        
        elif bb2["text"] == "x" and bb5["text"] == "x" and bb8["text"] == "x":
            bb2.config(bg="red")
            bb5.config(bg="red")
            bb8.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        
        elif bb3["text"] == "x" and bb6["text"] == "x" and bb9["text"] == "x":
            bb3.config(bg="red")
            bb6.config(bg="red")
            bb9.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        
        elif bb1["text"] == "x" and bb5["text"] == "x" and bb9["text"] == "x":
            bb1.config(bg="red")
            bb5.config(bg="red")
            bb9.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        
        elif bb3["text"] == "x" and bb5["text"] == "x" and bb7["text"] == "x":
            bb3.config(bg="red")
            bb5.config(bg="red")
            bb7.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x winner")
            disable_all_buttons()
        # o's  program    
        elif bb1["text"] == "0" and bb2["text"] == "0" and bb3["text"] == "0":
            bb1.config(bg="red")
            bb2.config(bg="red")
            bb3.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","x0winner")
            disable_all_buttons()
        
        elif bb4["text"] == "0" and bb5["text"] == "0" and bb6["text"] == "0":
            bb4.config(bg="red")
            bb5.config(bg="red")
            bb6.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","0 winner")
            disable_all_buttons()
        
        elif bb7["text"] == "0" and bb8["text"] == "0" and bb9["text"] == "0":
            bb7.config(bg="red")
            bb8.config(bg="red")
            bb9.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","0 winner")
            disable_all_buttons()
        
        elif bb1["text"] == "0" and bb4["text"] == "0" and bb7["text"] == "0":
            bb1.config(bg="red")
            bb4.config(bg="red")
            bb7.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","0 winner")
            disable_all_buttons()
        
        elif bb2["text"] == "0" and bb5["text"] == "0" and bb8["text"] == "0":
            bb2.config(bg="red")
            bb5.config(bg="red")
            bb8.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","0 winner")
            disable_all_buttons()
        
        elif bb3["text"] == "0" and bb6["text"] == "0" and bb9["text"] == "0":
            bb3.config(bg="red")
            bb6.config(bg="red")
            bb9.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","0 winner")
            disable_all_buttons()
        
        elif bb1["text"] == "0" and bb5["text"] == "0" and bb9["text"] == "0":
            bb1.config(bg="red")
            bb5.config(bg="red")
            bb9.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","0 winner")
            disable_all_buttons()
        
        elif bb3["text"] == "0" and bb5["text"] == "0" and bb7["text"] == "0":
            bb3.config(bg="red")
            bb5.config(bg="red")
            bb7.config(bg="red")
            winner = True
            messagebox.showinfo("tic tac toe","0 winner")
            disable_all_buttons()
    
        elif count == 9 and winner == False:
            messagebox.showinfo("tic tac toe","its a tie \n no onw wins!")
            disable_all_buttons()
    



    def b_click(b):
        global clicked,count

        if b["text"] == " " and clicked == True:
            b["text"] = "x"
            clicked = False
            count += 1
            checkifwon()
        elif b["text"] == " " and clicked == False:
            b["text"] = "0"
            clicked = True
            count += 1
            checkifwon()
        
        else:
            messagebox.showerror("tic tac toe ","hey! that box has alredy been selected \n pick another box.. ")
        

        
        
    def reset():
        global bb1,bb2,bb3,bb4,bb5,bb6,bb7,bb8,bb9
        global clicked,count
        clicked = True
        count = 0

        bb1=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb1))
        bb2=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb2))
        bb3=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb3))

        bb4=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb4))
        bb5=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb5))
        bb6=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb6))

        bb7=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb7))
        bb8=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb8))
        bb9=Button(new_window2,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(bb9))


        bb1.place(x=115,y=100)
        bb2.place(x=225,y=100)
        bb3.place(x=335,y=100)

        bb4.place(x=115,y=225)
        bb5.place(x=225,y=225)
        bb6.place(x=335,y=225)

        bb7.place(x=115,y=350)
        bb8.place(x=225,y=350)
        bb9.place(x=335,y=350)
        llaa1=Label(new_window2,text="tic tak toe",bg="light green",font=("Helevetica",20))
        llaa1.place(x=225,y=30)

    my_menu= Menu(new_window2)
    new_window2.config(menu=my_menu)

    options_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="option",menu=options_menu)
    options_menu.add_command(label="rest game",command=reset)


    reset()
    
ba1=Button(root,text="Enter",bg="light pink",command=vinay1)
ba1.place(x=80,y=350)
    


root.mainloop()
