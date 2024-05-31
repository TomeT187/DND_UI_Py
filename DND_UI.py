import tkinter as tk
from os import listdir

class DNDWindow(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.geometry("1920x1080")
        self.backGroundPic = tk.PhotoImage(file = "images\\welcome.png")
        self.scenes = []
        self.backGroundSetUp()

    def backGroundSetUp(self):
        #remember to set as a memeber var with self.var otherwise is deleted after function calls
        self.backGroundLabel = tk.Label(self,image=self.backGroundPic)
        self.backGroundLabel.place(x=0,y=0)
        self.selectSceneButton = tk.Button(self,text="scene select",command= lambda: self.showSceneSelect())
        self.selectSceneButton.place(x=0,y=0)

    def showSceneSelect(self):
        self.backGroundLabel.destroy()
        self.backGroundPic = tk.PhotoImage(file = "images\\sceneSelectBackGround.png")
        self.backGroundLabel = tk.Label(self,image=self.backGroundPic)
        self.backGroundLabel.place(x=0,y=0)
        sceneCount = 0
        
        for filename in listdir('images\\scenes'):
            # self.scenes.append(tk.PhotoImage(file = filename))
            button = tk.Button(text=filename,width=12,height=4,command=lambda:self.changeScene(filename))
            button.place(x=(sceneCount%6)*100 + 100,y=(int(sceneCount / 6) *100 )+ 300)
            sceneCount += 1


    def changeScene(self,filename):
        self.backGroundLabel.destroy()
        self.backGroundPic = tk.PhotoImage(file = f"images\\scenes\\{filename}")
        self.backGroundLabel = tk.Label(self,image=self.backGroundPic)
        self.backGroundLabel.place(x=0,y=0)
        self.selectSceneButton.lift()

        # button = tk.Button(image=self.scenes[0],width=80,height=80,text="tesst")
        # button.place(x=sceneCount*100,y=(sceneCount % 3)*100 + 100)
        
    

        

