from time import sleep
class outlook:
    def __init__(self,canvas):
        canvas.pack(side='left')
        
        canvas.create_rectangle(0,0,300,150,fill="#af6161",width=0)
        canvas.create_rectangle(300,250,600,400,fill="#ff8040",width=0)
        canvas.create_text(300,200,font=("Berlin Sans FB",20,"bold"), text="Welcome to Typing master\n   version -VIVEK",fill="green")
        
    


