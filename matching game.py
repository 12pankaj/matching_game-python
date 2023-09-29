import random
from tkinter import *
import tkinter.messagebox as tmsg
counter=9;
ch=0;
a = [""] * 5
winch=1;
def change(x):
    global counter,ch,winch
    if ch==5:
        return
    button_list[x].config(state=DISABLED,bg="red")
    if(counter<=47):
        button_list[set1[counter]].config(state=NORMAL)
    counter+=1
    a[ch]=x;
    for i in range(2,len(a)):
        if a[i]=="" or a[i-1]=="" or a[i-2]=="":
            break
        if (button_list[a[ch]].cget('text')==button_list[a[ch-1]].cget('text') and button_list[a[ch]].cget('text')==button_list[a[ch-2]].cget('text')):
            button_list[a[ch]].config(text=" ")
            button_list[a[ch-1]].config(text=" ")
            button_list[a[ch-2]].config(text=" ")
            a[ch]="";
            a[ch-1]="";
            a[ch-2]="";
            winch+=3;
            ch=ch-3;
        if i==2 or i==3:
            break;
    ch+=1;
    if ch==5:
        tmsg.showinfo("LOSSE", "you Losse \n try agian")
        root.destroy()
    elif winch==49:
        tmsg.showinfo("winner", "you Win \n best of luck! next chance")
        root.destroy()

hi=5;
def hint():
    global counter,hi

    if hi<=0:
        hitbut.config(state=DISABLED)
        return
    hi-=1
    if(counter<47):
        hitbut.config(text=f"hint {hi}")
        button_list[set1[counter]].config(state=NORMAL)
        counter+=1

root = Tk()
root.geometry("600x500")
root.title("matching game")
f1 =Frame(root,bg="darkturquoise")
l1 =Label(f1,text="Fast solve\n Game",bg="pink",font="lucida 20 bold")

hitbut = Button(f1,text="hint 5",font="lucida 15 bold",bg="darkturquoise",fg="hotpink",command=lambda: hint())
hitbut.pack(side=LEFT,padx=10,pady=13)
l1.pack()
f1.pack()
set1 = [0, 1, 29, 30,5, 6, 31, 32, 33, 34, 7, 8, 9, 10, 11, 12, 13,39, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 35, 36, 37, 38, 47, 40, 41, 42, 43, 2, 3, 4,  25, 26, 27, 28, 44, 45, 46]
random.shuffle(set1)
f1 =Frame(root,bg="darkturquoise")
button_list = []
count=0;
for j in range(1,7):
    f1 =Frame(root,bg="darkturquoise")
    for i in range(1,9):
        b1 = Button(f1,text=i,font="lucida 15 bold",bg="darkturquoise",fg="hotpink",state=DISABLED,command=lambda count=count: change(count))
        b1.pack(side=LEFT,padx=10,pady=10)
        button_list.append(b1)
        count+=1
    f1.pack();
f1.pack();
rang=0;
for i in set1:
    button_list[i].config(state=NORMAL)
    rang+=1;
    if rang==10:
        break;

print(set1)
root.mainloop()