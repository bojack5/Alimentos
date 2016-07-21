from tkinter import *
class fe:
    def __init__(self,master):
        self.b=Button(master,justify = LEFT)
        self.photo=PhotoImage(file="/home/bojack/Documents/Almentos/Imagenes/updater.png")
        self.b.config(image=self.photo,width="50",height="50")
        self.b.pack(side=LEFT)
root = Tk()
front_end=fe(root)
root.mainloop()
