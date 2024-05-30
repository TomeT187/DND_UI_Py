import tkinter as tk

class DNDWindow():
    def __init__(self,root):
        super().__init__()
        root.geometry("400x400")
        self.backGroundSetUp(root)

    def backGroundSetUp(self,root):
        backGroundPic = tk.PhotoImage(file = "doubleconescoop.png")
        backGroundLabel = tk.Label(root,image=backGroundPic)
        backGroundLabel

root = tk.Tk()
app = DNDWindow(root)
root.mainloop()