from tkinter import Entry,Button
from random import randrange
from english_words import english_words_set
class random__file:
    def __init__(self,canvas,sbar,first_body):
        self.w =0
        self.count=0
        self.t=0
        self.c=0
        self.false=False
        self.fb=first_body
        self.t_del='None'
        self.canvas=canvas
        sbar.pack_forget()
        self.canvas.delete('all')
        self.canvas.config(scrollregion=(0,0,600,400))
        self.display()
        self.entry()
        self.canvas.create_window(530,50,window =Button(self.canvas,text='Close',cursor='hand2',command=self._close,font=('Courier new',15,'bold italic'),bg='red',relief='flat'))
        
    def get_r_word(self):
        self.t+=1
        self.false=False
        p=0
        n=randrange(0,25488)
        for x in english_words_set:
            if p==n:
                self.r_word =x
                return(x)
            p+=1
    def display(self):
        self.count=0
        self.canvas.delete(self.t_del)
        self.t_del=self.canvas.create_text(300,200,text=self.get_r_word(),font=('Courier new',15,'bold italic'),fill='green')
    def entry(self):
        self.ent=Entry(self.canvas,bg ='yellow',fg ='green',font=('Courier new',18,'bold italic'))
        self.canvas.create_window(300,300,window=self.ent)
        self.ent.focus_set()
        self.canvas.bind_all('<space>',lambda x :self.check())
    def check(self):
        try:
            if self.r_word==self.ent.get().strip():
                self.c+=1
                self.ent.config(bg='yellow')
                self.display()
                self.ent.delete(0,'end')

            else:
                if self.count == 0:
                    self.w+=1
                self.count=1
                self.ent.config(bg='red')
        except:print('hello')
    def _close(self):
        self.canvas.delete('all')
        if self.t-self.w==1:
            
            self.correct = 0
        else:
            self.correct =(self.t-self.w)
        self.canvas.create_text(250,130,fill ='green',font=('Harrington',15,'bold italic'),text="Total word given->%d"%self.t)
        self.canvas.create_text(250,160,fill ='green',font=('Harrington',15,'bold italic'),text="Total correct word typed->%d"%(self.correct))
        self.canvas.create_text(250,190,fill ='green',font=('Harrington',15,'bold italic'),text="Total wrong word typed->%d"%(self.w))
        self.canvas.create_window(530,350,window =Button(self.canvas,text='Close',cursor='hand2',command=self.fb,font=('Harrington',15,'bold italic'),bg='red',relief='flat'))

        
        






