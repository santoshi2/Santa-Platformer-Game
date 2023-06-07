import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((1900,1000))
from pygame.locals import QUIT
pygame.display.set_caption('Platformer')
clock=pygame.time.Clock()
def show_text(msg, x, y, colorcode, size):
    fontobj= pygame.font.SysFont('freesans', size)
    msgobj = fontobj.render(msg,False,colorcode)
    screen.blit(msgobj,(x, y))


x=100
y=720
right=False
left=False
up=False
down=False
tileslist=[1,1,0,0,1,0,1]
lstidleright=[]
lstidleleft=[]
lstrunright=[]
lstrunleft=[]
lstjumpright=[]
lstjumpleft=[]
counterrunright=0
counterrunleft=0
counterjumpidle=0
counteridleright=0
counteridleleft=0
runrightboo=False
jumprightboo=False
runleftboo=False
jumpleftboo=False
jumpboo=False
idlebooright=True
idlebooleft=False
direction="right"
yjumpdestination=720
jumpcounter=0
ytarget=720
jump=0
reset=0

for idle in range(1,17,1):
    loadidle=pygame.image.load("santasprites\png\Idle ("+str(idle)+").png")
    loadidle=pygame.transform.scale(loadidle,(300,200))
    loadidleleft=pygame.transform.flip(loadidle,True, False)
    lstidleright.append(loadidle)
    lstidleleft.append(loadidleleft)


for run in range(1,12,1):
    loadrun=pygame.image.load("santasprites\png\Run ("+str(run)+").png")
    loadrun=pygame.transform.scale(loadrun,(300,200))
    loadrunleft=pygame.transform.flip(loadrun,True, False) 
    lstrunright.append(loadrun)
    lstrunleft.append(loadrunleft)


for jump in range(1,17,1):
    loadjump=pygame.image.load("santasprites\png\Jump ("+str(jump)+").png")
    loadjump=pygame.transform.scale(loadjump,(300,200))
    loadjumpleft=pygame.transform.flip(loadjump,True, False)
    lstjumpright.append(loadjump)
    lstjumpleft.append(loadjumpleft)

#Images
tiles=pygame.image.load("wintertileset\png\Tiles/2.png")
tiles=pygame.transform.scale(tiles,(200,300))
bg=pygame.image.load("wintertileset\png\BG\BG.png")
bg=pygame.transform.scale(bg,(1900,1000))

def restright(x,y):
    global counteridleright
    counteridleright=counteridleright+1
    if counteridleright==16:
        counteridleright=0
    screen.blit(lstidleright[counteridleright],(x,y))

def restleft(x,y):
    global counteridleleft
    counteridleleft=counteridleleft+1
    if counteridleleft==16:
        counteridleleft=0
    screen.blit(lstidleleft[counteridleleft],(x,y))

def runright(x,y):
    global counterrunright
    counterrunright=counterrunright+1
    if counterrunright==11:
        counterrunright=0
    screen.blit(lstrunright[counterrunright],(x,y))


def runleft(x,y):
    global counterrunleft
    counterrunleft=counterrunleft+1
    if counterrunleft==11:
        counterrunleft=0
    screen.blit(lstrunleft[counterrunleft],(x,y))

def jumpright(x,y):
    global counterjumpidle
    global jump
    counterjumpidle=counterjumpidle+1
    if counterjumpidle==16:
        counterjumpidle=0
    if jump==1:
        if y<=ytarget:
            y=y+50
            if y>yjumpdestination:
                y=yjumpdestination
                jump=0
        else:
            y=y-50
    screen.blit(lstjumpright[counterjumpidle],(x,y))

def jumpleft(x,y):
    global counterjumpidle
    global jump
    counterjumpidle=counterjumpidle+1
    if counterjumpidle==16:
        counterjumpidle=0
    if jump==1:
        if y<=ytarget:
            y=y+50
            if y>yjumpdestination:
                y=yjumpdestination
                jump=0
        else:
            y=y-50
    screen.blit(lstjumpleft[counterjumpidle],(x,y))

while True:
    clock.tick(10)
    screen.blit(bg,(0,0))
    screen.blit(tiles,(0,900))
    if runrightboo==True:
        runright(x,y)
        x=x+20

    elif jumprightboo==True:
        jumpright(x,y)
        x=x+10
        
    elif runleftboo==True:
        runleft(x,y)
        x=x-20

    elif jumpleftboo==True:
        jumpleft(x,y)
        x=x-10
        
    elif jumpboo==True:
        jumpright(x,y)
        x=x+10

    elif idlebooright==True and direction=="right":
        restright(x,y)

    elif idlebooleft==True and direction=="left":
        restleft(x,y)
   
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                if direction=="left":
                    x=x+50
                direction="right"
                runrightboo=True
                idlebooright=False 
                idlebooleft=False

            if event.key==pygame.K_SPACE and runleftboo==True:
                direction="left"
                jumpleftboo=True
                idlebooright=False
                idlebooleft=False
                runleftboo=False
                yjumpdestination=y
                ytarget=yjumpdestination-400
                jump=1                

            if event.key==pygame.K_a:
                if direction=="right":
                    x=x-50
                direction="left"
                runleftboo=True
                idlebooright=False
                idlebooleft=False

            if event.key==pygame.K_SPACE and runrightboo==True and jumpcounter==0:
                direction="right"
                jumprightboo=True
                idlebooright=False
                idlebooleft=False
                runrightboo=False
                yjumpdestination=y
                ytarget=yjumpdestination-400
                jump=1
                jumpcounter=jumpcounter+1                
        if event.type==pygame.KEYUP:
            jumpcounter=0
            idlebooright=True
            idlebooleft=True
            jumprightboo=False
            jumpleftboo=False
            runleftboo=False
            jumpboo=False
            runrightboo=False          
    pygame.display.update() 
    # show_text('hi',300,300,(39,150,63),30)
