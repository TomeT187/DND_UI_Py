import tkinter as tk

class DNDWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.backGroundSetUp()

    def backGroundSetUp(self):
        #remember to set as a memeber var with self.var otherwise is deleted after function calls
        self.backGroundPic = tk.PhotoImage(file = "bidenTDM.png")
        backGroundLabel = tk.Label(self,image=self.backGroundPic)
        backGroundLabel.pack()
        

