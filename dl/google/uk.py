from dl.google.dd.buttonn import button
from dl.google.dd.dktext import dktext
from dl.google.dd.bbutton import bbutton

class google_game:
    def __init__(self,canvas):
        self.canvas=canvas
        self.td=[]
        self.bu=button(canvas,10,10,70,70)
        self.textss=dktext()
        self.bbu=bbutton(self.canvas)
        self.dese=['','']

    def loop(self,eventx,eventy,button1,enttext):
        if eventx<70 and eventx>0 and button1==1 and eventy>0 and eventy<70:
            self.td=1
        if self.td==1:   
            self.googledk(eventx,eventy,button1,enttext)
    
    def googledk(self,eventx,eventy,button1,enttext):
        self.bu.tu()
        self.canvas.create_rectangle(0,0,640,480,fill='White')
        self.text=self.canvas.create_text(320,10,text='請在此搜尋')  
        if enttext!='':                   
            self.dese=self.textss.text(enttext)
        self.des=self.bbu.loop(self.dese[1],eventx,eventy,button1)
        print(self.des)