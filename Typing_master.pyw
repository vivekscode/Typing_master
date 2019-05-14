import time
from random__file import random__file
from practice import _practice
from outlook import outlook
from tkinter import *
from introduction import introduce

tk=Tk()
tk.wm_title("Typing master version -VIVEK")
tk.wm_resizable(0,0)
sbar=Scrollbar(tk)
def first_body():
    canvas.delete("all") 
    b_1=Button(canvas,command=lambda :Introductions(1),cursor='hand2',text="Introduction : to top row letters   ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_2=Button(canvas,command =lambda :practice(1),cursor='hand2',text="Practice : q to r, u to p           ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_3=Button(canvas,command =lambda :practice(2),cursor='hand2',text="practice : q to t, t to p           ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_4=Button(canvas,command=lambda :Introductions(2),cursor='hand2',text="Introduction : to middle row letters",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_5=Button(canvas,command =lambda :practice(3),cursor='hand2',text="Practice : a to f, j to ;           ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_6=Button(canvas,command =lambda :practice(4),cursor='hand2 ',text="Practice : a to g, h to ;           ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_7=Button(canvas,command=lambda :Introductions(3),cursor='hand2',text="Introduction : to bottom row letters",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_8=Button(canvas,command =lambda :practice(5),cursor='hand2',text="Practice : z to v, m to /           ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_9=Button(canvas,command =lambda :practice(6),cursor='hand2',text="Practice : z to b, n to /           ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_10=Button(canvas,command =lambda :practice(7),cursor='hand2',text=" Practice : All letters  ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    b_11=Button(canvas,command =lambda :random__file(canvas,sbar,first_body),cursor='hand2',text=" Practice : Random words ",font=("Berlin Sans FB",15,"bold"),relief='flat',bg="#ffff6c",fg='Dark Green')
    canvas.create_window(160,25,window=b_1)
    canvas.create_window(135,70,window=b_2)
    canvas.create_window(135,115,window=b_3)
    canvas.create_window(170,160,window=b_4)
    canvas.create_window(135,205,window=b_5)
    canvas.create_window(135,250,window=b_6)
    canvas.create_window(170,295,window=b_7)
    canvas.create_window(135,340,window=b_8)
    canvas.create_window(135,385,window=b_9)
    canvas.create_window(100,430,window=b_10)
    canvas.create_window(120,475,window=b_11)
    
    canvas.config(scrollregion=(0, 0, 600,500)) 
    
    sbar.config(command=canvas.yview) 
    canvas.config(yscrollcommand=sbar.set) 
    sbar.pack(side=RIGHT,fill='y')

def Introductions(no):
    sbar.pack_forget() 
    canvas.delete('all')
    canvas.config(scrollregion=(0, 0, 600,400))
   
    b_back=Button(canvas,relief=FLAT,bg ='orange',text ="GO",command =first_body)
    canvas.create_window(20,15,window=b_back)
    b_back.bind('<Enter>',lambda x:b_back.config(text='Back'))
    b_back.bind('<Leave>',lambda x:b_back.config(text='GO'))
    b_back.bind('<Button-1>',lambda x:first_body)
    
    canvas.create_text(300,50,font=("Berlin Sans FB",30,"bold"), text="INTRODUCTION",fill="red")
    
    s_btn=Button(canvas,command =lambda :introduce(canvas,no,first_body),text = "Start",relief ='flat',font=("Berlin Sans FB",20,"bold"),fg ='blue',bg ="#ffff6c",cursor ='hand2')
    canvas.create_window(500,300,window=s_btn)

def practice(no):
    sbar.pack_forget() 
    canvas.delete('all')
    canvas.config(scrollregion=(0, 0, 600,400))
   
    b_back=Button(canvas,relief=FLAT,bg ='orange',text ="GO",command =first_body)
    

    canvas.create_window(20,15,window=b_back)
    b_back.bind('<Enter>',lambda x:b_back.config(text='Back'))
    b_back.bind('<Leave>',lambda x:b_back.config(text='GO'))
    b_back.bind('<Button-1>',lambda x:first_body)
    
    canvas.create_text(300,50,font=("Berlin Sans FB",30,"bold"), text="PRACTICE",fill="red")
    
    
    ##timer
    var = StringVar()
    
    opt=OptionMenu(canvas,var,'None','30 sec','2 min','5 min','10 min','15 min','30 min')
    var.set('None')
    canvas.create_text(100,225,font=("Berlin Sans FB",10,"bold"), text="Timer",fill="brown")
    canvas.create_window(100,250,window=opt)
    s_btn=Button(canvas,text = "Start",command = lambda :_practice(var.get(),first_body,canvas,tk,no),relief ='flat',font=("Berlin Sans FB",20,"bold"),fg ='blue',bg ="#ffff6c",cursor ='hand2')
    canvas.create_window(500,300,window=s_btn)



canvas=Canvas(tk,height=400,width=600,highlightthickness=0,bg="#ffff6c")
outlook(canvas)

##next button                                                 
b_next=Button(canvas,text='Next',command=first_body,font=("Berlin Sans FB",20,"bold"),bg="#ff8040",padx=3,fg="Green",relief="flat",cursor="hand2")
canvas.create_window(550,350,window=b_next)




tk.mainloop()
