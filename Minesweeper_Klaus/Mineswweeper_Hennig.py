import os
import random
import time

import pygame
from pygame.constants import (K_ESCAPE, K_SPACE, KEYDOWN, KEYUP, QUIT)



class Einstellungen(object):
    def __init__(self):
        self.width = 500                                                   
        self.height = 800                                                   
        self.fps = 60                                                       
        self.title = "Minensprenger"                                          
        self.image_path = os.path.dirname(os.path.abspath(__file__))        

    def size(self):                                                        
        return (self.width, self.height)   

class Feld(pygame.sprite.Sprite):
    def __init__(self,pygame,Einstellungen,bb,bl,l,t):
        pygame.sprite.Sprite.__init__(self)
        self.pygame= pygame
        self.Einstellungen= Einstellungen
        self.image= pygame.image.load(os.path.join(self.Einstellungen.image_path,"feld.jpg")).convert_alpha()
        self.image= pygame.transform.scale(self.image,(bb,bl))
        self.mask= pygame.mask.from_surface(self.image)
        self.rect= pygame.mask.Mask.get_rect(self.mask)
        self.rect.left= l
        self.rect.top= t


class Spiel(object):
    def __init__(self, pygame, Einstellungen):
        self.pygame = pygame
        self.Einstellungen = Einstellungen 
        self.lightgrey = [150,150,150]
        self.darkgrey = [100,100,100]
        self.black = [0,0,0]
        self.white =[255,255,255]
        self.screen = pygame.display.set_mode(Einstellungen.size())
        self.pygame.display.set_caption(self.Einstellungen.title)
        self.clock = pygame.time.Clock()
        self.done = False
        self.background = self.pygame.image.load(os.path.join(self.Einstellungen.image_path, "grid.jpg")).convert()
        self.background = pygame.transform.scale(self.background, (500, 700))                            
        self.background_rect = self.background.get_rect()
        self.ticks = pygame.time.get_ticks()
        self.spawn = ((pygame.time.get_ticks()-self.ticks)/1000)

        self.secscolor= [138,43,226]
        self.font = pygame.font.Font(None, 45) 
        self.text= self.font.render("0", True, self.secscolor)
        self.textRect= self.text.get_rect()
        self.textRect.center= 30, 750
                                        #breite,länge von links beginnend und vonb oben 
        self.feld1 = Feld(pygame,Einstellungen,99,137,0,0)
        self.feld2 = Feld(pygame,Einstellungen,99,137,100,0)
        self.feld3 = Feld(pygame,Einstellungen,99,137,201,0)
        self.feld4 = Feld(pygame,Einstellungen,99,137,302,0)
        self.feld5 = Feld(pygame,Einstellungen,99,137,403,0)
        self.feld6 = Feld(pygame,Einstellungen,99,140,0,139)
        self.feld7 = Feld(pygame,Einstellungen,99,140,101,139)
        self.feld8 = Feld(pygame,Einstellungen,99,140,202,139)
        self.feld9 = Feld(pygame,Einstellungen,99,140,303,139)
        self.feld10 = Feld(pygame,Einstellungen,99,140,404,139)
        self.feld11 = Feld(pygame,Einstellungen,99,140,0,280)
        self.feld12 = Feld(pygame,Einstellungen,99,140,101,280)
        self.feld13 = Feld(pygame,Einstellungen,99,140,202,280)
        self.feld14 = Feld(pygame,Einstellungen,99,140,303,280)
        self.feld15 = Feld(pygame,Einstellungen,99,140,404,280)
        self.feld16 = Feld(pygame,Einstellungen,99,140,403,420)
        self.feld17 = Feld(pygame,Einstellungen,99,140,0,420)
        self.feld18 = Feld(pygame,Einstellungen,99,140,101,420)
        self.feld19 = Feld(pygame,Einstellungen,99,140,202,420)
        self.feld20 = Feld(pygame,Einstellungen,99,140,303,420)
        self.feld21 = Feld(pygame,Einstellungen,99,140,404,560)
        self.feld22 = Feld(pygame,Einstellungen,99,140,0,560)
        self.feld23 = Feld(pygame,Einstellungen,99,140,101,560)
        self.feld24 = Feld(pygame,Einstellungen,99,140,202,560)
        self.feld25 = Feld(pygame,Einstellungen,99,140,303,560)
        self.felder= pygame.sprite.Group()

        self.felder.add(self.feld1,self.feld2,self.feld3,self.feld4,self.feld5,self.feld6,self.feld7,self.feld8,
        self.feld9,self.feld10,self.feld11,self.feld12,self.feld13,self.feld14,self.feld15,self.feld16,self.feld17,
        self.feld18,self.feld19,self.feld20,self.feld21,self.feld22,self.feld23,self.feld24,self.feld25)
        
        
        
    def run(self):
        while not self.done:
            self.clock.tick(self.Einstellungen.fps)
            self.timef= (pygame.time.get_ticks()-self.ticks)/1000
            self.time= round(self.timef) 
            self.text= self.font.render(str(self.time), True, self.secscolor)
            for event in self.pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.done = True

                self.mouse= pygame.mouse.get_pos()



          #  self.update()
            self.draw()




    def draw(self):
        self.pygame.display.flip()
        self.screen.blit(self.background, self.background_rect)
        pygame.draw.rect(self.screen, self.black,(30,750,70,50),0)
        pygame.draw.rect(self.screen, self.black,(405,750,70,50),0)
        self.screen.blit(self.text,self.textRect.center)
        self.felder.draw(self.screen)

if __name__ =='__main__':
    Einstellungen = Einstellungen()

    pygame.init()

    game =Spiel(pygame, Einstellungen)

    game.run()

    pygame.quit()
