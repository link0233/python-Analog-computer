class dktext:
    def __init__(self):
        self.texts=[['九九乘法表',[]]]
        with open('九九乘法表.txy','r') as f:
            for i in f:
                self.texts[0][1].append(i.strip())
    def text(self,text):
        self.textt=[]
        self.des=[]
        for dk in self.texts:
            if text in dk[0]:
                self.textt.append(dk[1])
                self.des.append(dk[0])
                break
        return [self.textt,self.des]