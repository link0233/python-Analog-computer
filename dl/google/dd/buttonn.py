class button:
    def __init__(self,canvas,x,y,x2,y2):
        self.canvas=canvas
        self.eu(x,y,x2,y2)
    def tu(self):
        self.canvas.delete(self.item)
        self.canvas.delete(self.itemtext)
    def eu(self,x,y,x2,y2):
        self.item=self.canvas.create_rectangle(x,y,x2,y2,fill='White')
        self.itemtext=self.canvas.create_text((x+x2)//2,(y+y2)//2,text='google',width=60)