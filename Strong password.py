from tkinter import*
import random

root=Tk()
root.title("Password Generator")
root.geometry("400x400")

label= Label(root)
label2= Label(root)
label3= Label(root,text="Guess Your Password")
box= Entry(root)
array_3d =[[['1','2','3','4','5','6'],["head","tail"],["A","B","C","D","E","F"]]]
print(array_3d[0][2][3])


def new_password():
    r_n_1 = random.randint(0,5)
    r_n_2 = random.randint(0,1)
    r_n_3 = random.randint(0,5)
    
    letter1 =str(array_3d[0][0][r_n_1])
    letter2 =(array_3d[0][1][r_n_2])
    letter3 =(array_3d[0][2][r_n_3])
    label["text"] = letter1 + "" + letter2 + "" + letter3
    label2["text"] = "Guessed Password="+box.get()

btn = Button(root, text= "Check", command = new_password)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

label.place(relx = 0.5, rely =0.6, anchor = CENTER)
box.place(relx = 0.5, rely =0.7, anchor = CENTER)
label3.place(relx = 0.5, rely =0.8, anchor = CENTER)
label2.place(relx = 0.5, rely =0.9, anchor = CENTER)
root.mainloop()