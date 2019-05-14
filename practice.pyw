from score import score
from random import shuffle
from tkinter import Button,Label
from tkinter.messagebox import showinfo
class _practice:
    def __init__(self,timer,first_body,canvas,tk,no):
        self.error=False
        self.c_words=0
        self.t_words=0
        self.w_words=0
        self.no=no
        self.tk=tk
        self.canvas=canvas
        self.canvas.delete('all')
        self.timer=timer
        time={'None':0,'30 sec':30*1000,'2 min': 120*1000,'5 min':300*1000,'10 min':600*1000,'15 min':900*1000,'30 min':1800*1000}
        if time[self.timer] is not 0:
            self.tk.after(time[self.timer],lambda :showinfo('Time out!!','Time has ended.You should now leave typing, but I will not force you to go.If you want to close it then click "Cancel" button.'))
        
        self.first_body=first_body
        self.canvas.create_window(500,10,window =Button(self.canvas,relief ='flat',cursor ='hand2',bg ='red',text="Cancel",command=lambda :score(self.t_words,self.c_words,self.w_words,self.first_body,self.error,self.canvas)))
        self.p_buttons()
    def p_buttons(self):
        
        if self.no is 1:
            self.list=['q','w','e','r','u','i','o','p']
        if self.no is 2:
            self.list=['q','w','e','r','t','y','u','i','o','p']
        if self.no is 3:
            self.list=['a','s','d','f','j','k','l',';']
        if self.no is 4:
            self.list=['a','s','d','f','g','h','j','k','l',';']
        if self.no is 5:
            self.list=['z','x','c','v','m',',','.','/']
        if self.no is 6:
            self.list=['z','x','c','v','b','n','m',',','.','/']
        if self.no is 7:
            self.list=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
        shuffle(self.list)
        self.list=self.list[:8]
        self.test_button()
    def test_button(self):
        
        lab1=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[0])
        lab2=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[1])
        lab3=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[2])
        lab4=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[3])
        lab5=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[4])
        lab6=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[5])
        lab7=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[6])
        lab8=Label(self.canvas,font =('Courier New',18,'bold'),bg ='Yellow',fg ='green',text=self.list[7])
       
        
        self.canvas.create_window(100,200,window=lab1)
        lab1.focus_set()
        lab1.bind('<KeyPress-%s>'%self.list[0],lambda x : self.unbind(lab1,lab2,1))
        lab2.bind('<KeyPress-%s>'%self.list[1],lambda x : self.unbind(lab2,lab3,2))
        lab3.bind('<KeyPress-%s>'%self.list[2],lambda x : self.unbind(lab3,lab4,3))
        lab4.bind('<KeyPress-%s>'%self.list[3],lambda x : self.unbind(lab4,lab5,4))
        lab5.bind('<KeyPress-%s>'%self.list[4],lambda x : self.unbind(lab5,lab6,5))
        lab6.bind('<KeyPress-%s>'%self.list[5],lambda x : self.unbind(lab6,lab7,6))
        lab7.bind('<KeyPress-%s>'%self.list[6],lambda x : self.unbind(lab7,lab8,7))
        lab8.bind('<KeyPress-%s>'%self.list[7],lambda x : self.unbind(lab8,'None',8))
    
        lab1.bind('<KeyPress>',lambda x : self.wrong(lab1))
        lab2.bind('<KeyPress>',lambda x : self.wrong(lab2))
        lab3.bind('<KeyPress>',lambda x : self.wrong(lab3))
        lab4.bind('<KeyPress>',lambda x : self.wrong(lab4))
        lab5.bind('<KeyPress>',lambda x : self.wrong(lab5))
        lab6.bind('<KeyPress>',lambda x : self.wrong(lab6))
        lab7.bind('<KeyPress>',lambda x : self.wrong(lab7))
        lab8.bind('<KeyPress>',lambda x : self.wrong(lab8))
    
    def unbind(self,_del,fcs,__no):
        if self.error is False:
            self.c_words+=1
        if fcs is not 'None':
            pos={1:140,2:180,3:220,4:260,5:320,6:360,7:400,8:440}
            _del.destroy()
            
            self.canvas.create_window(pos[__no],200,window=fcs)
            self.error=False
            fcs.focus_set()
        else:
            self.canvas.delete('all')
            self.canvas.create_window(500,10,window =Button(self.canvas,relief ='flat',cursor ='hand2',bg ='red',text="Cancel",command=lambda :score(self.t_words,self.c_words,self.w_words,self.first_body,self.error,self.canvas)))
            self.p_buttons()
        self.t_words+=1
        
    def wrong(self,color):
        
        self.error=True
        self.w_words+=1
        color.config(bg='red')


