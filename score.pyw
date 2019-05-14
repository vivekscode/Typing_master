from tkinter import Button
class score:
    def __init__(self,t_words,c_words,w_words,first_body,error,canvas):
        canvas.delete('all')
        accuracy=0
        if error is True:t_words+=1
        
        if t_words != 0:
            accuracy=(c_words/t_words)*100
        canvas.create_text(250,130,fill ='green',font=('Harrington',15,'bold italic'),text="Total letter attempted->%d"%t_words)
        canvas.create_text(250,160,fill ='green',font=('Harrington',15,'bold italic'),text="Total correct letter typed->%d"%c_words)
        canvas.create_text(250,190,fill ='green',font=('Harrington',15,'bold italic'),text="Total wrong letter typed->%d"%(t_words-c_words))
        canvas.create_text(250,220,fill ='green',font=('Harrington',15,'bold italic'),text="No. of times wrong letter typed->%d"%w_words)
        canvas.create_text(250,250,fill ='green',font=('Harrington',15,'bold italic'),text="Accuracy->%.2f"%accuracy)
        canvas.create_window(550,350,window =Button(canvas,text='Close',cursor='hand2',command=first_body,font=('Harrington',15,'bold italic'),bg='red',relief='flat'))
