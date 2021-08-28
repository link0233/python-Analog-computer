from tkinter import*
import time
import dl.google.uk as u

class canvas(Canvas):
    def __init__(self,name):
        self.root=Tk()
        self.root.title(name)
        self.ent=Entry(self.root)
        self.ent.pack()
        self.dke=Button(self.root,text='輸入',command=self.dkdkdkdkdkddkdkdkdk)
        self.dke.pack()
        super(canvas,self).__init__(self.root,width=640,height=480)
        self.pack()
        self.setp()
        self.button11=0
        self.enttext=''
        while True:
            self.loop()
            time.sleep(0.01)
            if self.button11==1:
                self.button11=0
            self.enttext=''
            self.root.update()
        self.root.mainloop()
    def setp(self):
        self.goga=u.google_game(self)
        self.eventx=0
        self.eventy=0
        self.bind('<Button-1>',self.button1)

    def loop(self):
        self.goga.loop(self.eventx,self.eventy,self.button11,self.enttext)
    def button1(self,event):
        self.eventx=event.x
        self.eventy=event.y
        self.button11=1
    def dkdkdkdkdkddkdkdkdk(self):
        self.enttext=self.ent.get()