import pygame
 
pygame.init()
 
window = pygame.display.set_mode((800,600))
 
pygame.display.set_caption("Collision Detection")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
 
clock = pygame.time.Clock()
 
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
 
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
 
        return True
 
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
 
        return True
 
    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
 
        return True
 
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
 
        return True
 
    else:
 
        return False
 
class Sprite:
 
    def __init__(self,x,y,width,height):
 
        self.x=x
 
        self.y=y
 
        self.width=width
 
        self.height=height
 
    def render(self,collision):
 
        if (collision==True):
 
            pygame.draw.rect(window,red,(self.x,self.y,self.width,self.height))
 
        else:
 
            pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))
 
Sprite1=Sprite(100,50,100,100)
Sprite2=Sprite(300,50,100,100)
 
moveX,moveY=0,0
 
gameLoop=True
while gameLoop:
 
    for event in pygame.event.get():
 
        if (event.type==pygame.QUIT):
 
            gameLoop=False
 
        if (event.type==pygame.KEYDOWN):
 
            if (event.key==pygame.K_LEFT):
 
                moveX = -4
 
            if (event.key==pygame.K_RIGHT):
 
                moveX = 4
 
            if (event.key==pygame.K_UP):
 
                moveY = -4
 
            if (event.key==pygame.K_DOWN):
 
                moveY = 4
 
        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_LEFT):
 
                moveX=0
 
            if (event.key==pygame.K_RIGHT):
 
                moveX=0
 
            if (event.key==pygame.K_UP):
 
                moveY=0
 
            if (event.key==pygame.K_DOWN):
 
                moveY=0
 
    window.fill(white)
 
    Sprite1.x+=moveX
 
    Sprite1.y+=moveY
 
    collisions=detectCollisions(Sprite1.x,Sprite1.y,Sprite1.width,Sprite1.height,Sprite2.x,Sprite2.y,Sprite2.width,Sprite2.height)
 
    Sprite1.render(collisions)
 
    Sprite2.render(False)
 
    pygame.display.flip()
 
    clock.tick(50)
 
pygame.quit()