class bbutton:
    def __init__(self,canvas):
        self.text=[]
        self.canvas=canvas
        self.item=[]
    def loop(self,text,eventx,eventy,button1):
        self.text=text
        if self.item!=[]:
            for se in self.item:
                self.canvas.delete(se)
            self.item=[]
        self.id=''
        if self.text!=[]:
            self.y=10
            self.x=50
            for dkdk in self.text:
                self.item.append(self.canvas.create_text(self.x,self.y,text=dkdk))
                if button1==1 and eventx>self.x-50 and eventx<self.x+50 and eventy>self.y-5 and eventy<self.y+5:
                    self.id=dkdk
                self.y+=10
        return self.id