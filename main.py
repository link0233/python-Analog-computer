import dl.canvas as canvas
from tkinter import*

s=[]
def e():
    with open('dkd.dkdkdkrded','r')as f:
        global s
        s=[]
        for i in f:
            s.append(i.strip().split(','))
        s.append([name_entry.get(),au4a8_entry.get()])
    with open('dkd.dkdkdkrded','w') as f:
        for d in s:
            f.write(str(d[0])+','+str(d[1])+'\n')

def t():
    with open('dkd.dkdkdkrded','r')as f:
        u=[name_entry.get(),au4a8_entry.get()]
        for d in f:
            d=d.strip().split(',')
            if u[0]==d[0] and u[1]== d[1]:
                canvas.canvas(d[0])
        

rot=Tk()#登入視窗
rot.title('登入')

name_text=Label(rot,text='name').pack()#name輸入
name_entry=Entry(rot)
name_entry.pack()

au4a8_text=Label(rot,text='密碼').pack()#密碼輸入
au4a8_entry=Entry(rot)
au4a8_entry.pack()

d=Button(rot,text='建立帳號',command=e).pack()
ed=Button(rot,text='登入',command=t).pack()

rot.mainloop()