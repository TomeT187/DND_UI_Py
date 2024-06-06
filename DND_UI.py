import tkinter as tk
from os import listdir
from character import Character

class DNDWindow(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.sceneButtons = []
        self.geometry("1920x1080")
        self.backGroundPic = tk.PhotoImage(file = "images\\welcome.png")
        self.backGroundSetUp()
        testFrame = self.addCharacterHUD()
        testFrame.pack()

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
            self.addSceneButton(filename,sceneCount)
            sceneCount += 1
            
        
    #button class generator, needed so each object is its own object
    def addSceneButton(self,filename,sceneCount):
        button = tk.Button(text=filename,width=12,height=4,command=lambda: self.changeScene(filename))
        button.place(x=(sceneCount%6)*100 + 100,y=(int(sceneCount / 6) *100 )+ 300)
        self.sceneButtons.append(button)
        

    def changeScene(self,filename):
        for sceneButton in self.sceneButtons:
            sceneButton.destroy()
        self.sceneButtons = []
        self.backGroundLabel.destroy()
        self.backGroundPic = tk.PhotoImage(file = f"images\\scenes\\{filename}")
        self.backGroundLabel = tk.Label(self,image=self.backGroundPic)
        self.backGroundLabel.place(x=0,y=0)
        self.backGroundLabel.lower()
        
        #self.selectSceneButton.lift()

    def addCharacterHUD(self):
        newCharacter = Character()
        characterFrame = tk.Frame(self)

        nameText = tk.Entry(characterFrame)
        nameButton = tk.Button(characterFrame,text=" ",command=lambda: newCharacter.setName(nameText.get()))

        hpText = tk.Entry(characterFrame)
        tempHpText = tk.Entry(characterFrame)
        armorText = tk.Entry(characterFrame)

        nameText.grid(column=0,row=0,)
        nameText.insert(0,newCharacter.name)
        nameButton.grid(column=1,row=0)

        hpText.grid(column=0,row=1,)
        hpText.insert(0,f"HP: {newCharacter.hp}/{newCharacter.maxHp}")

        tempHpText.grid(column=0,row=2)
        tempHpText.insert(0,f"Temp: {newCharacter.tempHp}")

        armorText.grid(column=0,row=3)
        armorText.insert(0,f"Armor: {newCharacter.armor}")

        return characterFrame
        

        
    

        

