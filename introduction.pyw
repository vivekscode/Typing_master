from tkinter import Label,Button
from msvcrt import getch
class introduce:
    def __init__(self,canvas,no,first_body):
        
        self.first_body=first_body
        self.canvas=canvas
        
        self.canvas.delete('all')
        if no is 1:self.first()
        if no is 2:self.second()
        if no is 3:self.third()
    def first(self):
         self.canvas.delete('all')
         lab1=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Place your left four fingers from 'a' to 'f'\n and your rigt four fingers from 'h' to 'p'\n,Now press 'q' with your little left finger.")
         lab2=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'w' with left ring finger")
         lab3=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'e' with left middle finger")
         lab4=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'r' with left index finger")
         lab5=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 't' with left index finger")
         lab6=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'y' with right index finger")
         lab7=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'u' with right index finger")
         lab8=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'i' with right middle finger")
         lab9=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'o' with right ring finger")
         lab10=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'p' with right little finger")
         self.canvas.create_window(300,200,window=lab1)
         lab1.focus_set()
         lab1.bind('<KeyPress-q>',lambda x : self.unbind(lab1,lab2))
         lab2.bind('<KeyPress-w>',lambda x :self.unbind(lab2,lab3))
         lab3.bind('<KeyPress-e>',lambda x : self.unbind(lab3,lab4))
         lab4.bind('<KeyPress-r>',lambda x : self.unbind(lab4,lab5))
         lab5.bind('<KeyPress-t>',lambda x : self.unbind(lab5,lab6))
         lab6.bind('<KeyPress-y>',lambda x : self.unbind(lab6,lab7))
         lab7.bind('<KeyPress-u>',lambda x : self.unbind(lab7,lab8))
         lab8.bind('<KeyPress-i>',lambda x : self.unbind(lab8,lab9))
         lab9.bind('<KeyPress-o>',lambda x : self.unbind(lab9,lab10))
         lab10.bind('<KeyPress-p>',lambda x : self.unbind(lab10,'None'))
         
         
         
         
             
    def second(self):
        self.canvas.delete('all')
        lab1=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Place your left four fingers from 'a' to 'f'\n and your rigt four fingers from 'h' to 'p'\n,Now press 'a' with your little left finger.")
        lab2=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 's' with left ring finger")
        lab3=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'd' with left middle finger")
        lab4=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'f' with left index finger")
        lab5=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'g' with left index finger")
        lab6=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'h' with right index finger")
        lab7=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'j' with right index finger")
        lab8=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'k' with right middle finger")
        lab9=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'l' with right ring finger")         
        lab10=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press ';' with right little finger")
      
        self.canvas.create_window(300,200,window=lab1)
        lab1.focus_set()
        lab1.bind('<KeyPress-a>',lambda x : self.unbind(lab1,lab2))
        lab2.bind('<KeyPress-s>',lambda x :self.unbind(lab2,lab3))
        lab3.bind('<KeyPress-d>',lambda x : self.unbind(lab3,lab4))
        lab4.bind('<KeyPress-f>',lambda x : self.unbind(lab4,lab5))
        lab5.bind('<KeyPress-g>',lambda x : self.unbind(lab5,lab6))
        lab6.bind('<KeyPress-h>',lambda x : self.unbind(lab6,lab7))
        lab7.bind('<KeyPress-j>',lambda x : self.unbind(lab7,lab8))
        lab8.bind('<KeyPress-k>',lambda x : self.unbind(lab8,lab9))
        lab9.bind('<KeyPress-l>',lambda x : self.unbind(lab9,lab10))
        lab10.bind('<KeyPress-;>',lambda x : self.unbind(lab10,'None'))
         
    def third(self):
        self.canvas.delete('all')
        lab1=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Place your left four fingers from 'a' to 'f'\n and your rigt four fingers from 'h' to 'p'\n,Now press 'z' with your little left finger.")
        lab2=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'x' with left ring finger")
        lab3=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'c' with left middle finger")
        lab4=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'v' with left index finger")
        lab5=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'b' with left index finger")
        lab6=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'n' with right index finger")
        lab7=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press 'm' with right index finger")
        lab8=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press ',' with right middle finger")
        lab8=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press ',' with right middle finger")
        lab9=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press '.' with right ring finger")
        lab10=Label(self.canvas,font =('Courier New',14,'bold'),bg ='Yellow',fg ='green',text="Now press '/' with right little finger")
        self.canvas.create_window(300,200,window=lab1)
        lab1.focus_set()
        
        
        lab1.bind('<KeyPress-z>',lambda x : self.unbind(lab1,lab2))
        lab2.bind('<KeyPress-x>',lambda x :self.unbind(lab2,lab3))
        lab3.bind('<KeyPress-c>',lambda x : self.unbind(lab3,lab4))
        lab4.bind('<KeyPress-v>',lambda x : self.unbind(lab4,lab5))
        lab5.bind('<KeyPress-b>',lambda x : self.unbind(lab5,lab6))
        lab6.bind('<KeyPress-n>',lambda x : self.unbind(lab6,lab7))
        lab7.bind('<KeyPress-m>',lambda x : self.unbind(lab7,lab8))
        lab8.bind('<KeyPress-,>',lambda x : self.unbind(lab8,lab9))
        lab9.bind('<KeyPress-.>',lambda x : self.unbind(lab9,lab10))
        lab10.bind('<KeyPress-/>',lambda x : self.unbind(lab10,'None'))

    def unbind(self,_del,fcs):
        if fcs is not 'None':
            _del.destroy()
            self.canvas.create_window(300,200,window=fcs)
            fcs.focus_set()
        else:
            self.canvas.delete('all')
            
            self.canvas.create_window(300,200,window=Button(self.canvas,text="Close",command = self.first_body,cursor='hand2',font =('Courier New',14,'bold'),bg ='Yellow',fg ='green'))
        
      
   




      


