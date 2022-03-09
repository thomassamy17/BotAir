from tkinter import*
from abc import abstractmethod
import time

#################
# Thomas SAMY   #
# Maxime HOLEC  #
#################

DIRECTION = ["DROITE", "BAS", "GAUCHE", "HAUT"]
CASE_SIZE = 11

# Interface IMotion
class IMotion():
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def rotate(self):
        pass

# Class Motion
class Motion(IMotion):
    
    # IMotion méthode Move
    def move(self, x,y):
        case=self.listeCases[x][y]
        textCase = self.canvas.itemcget(case,"text")
        if textCase == "0":
            self.canvas.itemconfigure(case,text="1")
            self.canvas.move(self.botair[0],(x-self.botair[1][0])*CASE_SIZE,(y-self.botair[1][1])*CASE_SIZE)
            self.botair[1][0]=x
            self.botair[1][1]=y
            self.canvas.update()
            return True
        else:
            return False
        
    # IMotion méthode Rotate
    def rotate(self):
        if self.direction==DIRECTION[0]:
            self.direction = DIRECTION[1]
        elif self.direction==DIRECTION[1]:
            self.direction = DIRECTION[2]
        elif self.direction==DIRECTION[2]:
             self.direction = DIRECTION[3]
        else:
            self.direction = DIRECTION[0]
    
    # Méthode Scan
    def scan(self):
        if self.direction==DIRECTION[0]:
            res=self.move(self.botair[1][0]+1,self.botair[1][1])
        elif self.direction==DIRECTION[1]:
            res=self.move(self.botair[1][0],self.botair[1][1]+1)
        elif self.direction==DIRECTION[2]:
            res=self.move(self.botair[1][0]-1,self.botair[1][1])
        else:
            res=self.move(self.botair[1][0],self.botair[1][1]-1)
        if res == False:
            self.rotate()
        time.sleep(0.1)
        self.scan()
    # Constructeur
    def __init__(self,can,text):
        self.canvas = can
        self.v = text
        self.botair = ""
        self.direction = DIRECTION[0]
        self.listeCases = []
        self.grille()
        self.botair = [self.canvas.create_rectangle(22,22,33,33,outline="red",fill="white"),[2,2]]
        
    
    # Méthode pour initialiser la grille
    def grille(self):
        for x in range(67):
            self.listeCases.append([""]*67)
            for y in range(67):
                if x == 0 or y == 0 :
                    self.canvas.create_rectangle(
                        x * CASE_SIZE,
                        y * CASE_SIZE,
                        x * CASE_SIZE + CASE_SIZE,
                        y * CASE_SIZE + CASE_SIZE,
                        fill="white", outline="white"
                    )
                else:
                    self.canvas.create_rectangle(
                        x * CASE_SIZE,
                        y * CASE_SIZE,
                        x * CASE_SIZE + CASE_SIZE,
                        y * CASE_SIZE + CASE_SIZE,
                        fill="white", outline="black"
                    )                       
                    if x == 1 or y == 1 or x == 66 or y == 66 :
                        text=self.canvas.create_text(((x * CASE_SIZE)+5,(y * CASE_SIZE)+5),font=("Purisa", 9), text="-1")
                    elif x == 2 and y == 2 :
                        text=self.canvas.create_text(((x * CASE_SIZE)+5,(y * CASE_SIZE)+5),font=("Purisa", 9), text="1")
                    else:
                        text=self.canvas.create_text(((x * CASE_SIZE)+5,(y * CASE_SIZE)+5),font=("Purisa", 9), text="0")
                    self.listeCases[x][y] = text
            
    
# Création du widget principal ("maître") :
fen = Tk()
fen.title("BotAir Simulation / SAMY HOLEC")
# Création des widgets ("esclaves") :
canvas = Canvas(fen,bg='dark grey',height=737,width=737)
canvas.pack(side=LEFT,padx=10)

v = StringVar()
d = Motion(canvas,v)

Label(fen, textvariable=v).pack()

fen.mainloop()
