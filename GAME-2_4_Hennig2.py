import pygame
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_SPACE)
import os
from random import *

class Settings(object):
    def __init__(self):
        self.width = 800                                                   
        self.height = 700                                                   
        self.fps = 60                                                       
        self.title = "Zerstör den teufel"                                          
        self.image_path = os.path.dirname(os.path.abspath(__file__))        

    def size(self):                                                        
        return (self.width, self.height)   

class Player(pygame.sprite.Sprite):
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        self.image = pygame.image.load(os.path.join(self.settings.image_path, "Maus1.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 35))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pygame.mouse.get_pos()

    def update(self):         
        self.rect.left, self.rect.top = pygame.mouse.get_pos()


class Bubble(pygame.sprite.Sprite):
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        self.size= 100
        self.image_orig = pygame.image.load(os.path.join(self.settings.image_path, "Teufel.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image_orig, (self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = randint(10,self.settings.width-10-self.size)
        self.rect.top = randint(10,self.settings.height-10-self.size)
        self.grow = 2

    def update(self):
        if self.size < 200:
            center = self.rect.center
            self.size += self.grow
            self.image = pygame.transform.scale(self.image_orig, (self.size, self.size))
            self.rect= self.image.get_rect()
            self.rect.center = center
        


class Game(object):
    def __init__(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.size())                                      
        self.pygame.display.set_caption(self.settings.title)                                                      
        self.background = self.pygame.image.load(os.path.join(self.settings.image_path, "Hölle.jpg")).convert()
        self.background = pygame.transform.scale(self.background, (800, 700))                            
        self.background_rect = self.background.get_rect()
        self.player = Player(settings)                                                    
        self.clock = pygame.time.Clock()
        self.done = False
        pygame.mouse.set_visible(False)
        self.all_bubbles = pygame.sprite.Group()
        self.the_mouse = pygame.sprite.Group()
        self.the_mouse.add(self.player) 
        self.anzahl = 0
        self.zähler = 0.02

        pygame.mouse.set_visible(False)

    
    def run(self):
        while not self.done:                            
            self.clock.tick(self.settings.fps)         
            for event in self.pygame.event.get():       
                if event.type == QUIT:                  
                    self.done = True                 
                elif event.type == KEYDOWN:            
                    if event.key == K_ESCAPE:
                        self.done = True


            self.update()                               
            self.draw()                                
 
    def draw(self):
       # for self.bubble in self.all_bubbles:
        #    touch= pygame.sprite.collide_mask(self.player,self.bubble)
         #   if touch:
          #      self.player.image = pygame.image.load(os.path.join(self.settings.image_path, "Maus1.png")).convert_alpha()
           #     self.player.image = pygame.transform.scale(self.player.image, (25, 35))
            #else:
             #   self.player.image = pygame.image.load(os.path.join(self.settings.image_path, "Maus2.png")).convert_alpha()
              #  self.player.image = pygame.transform.scale(self.player.image, (25, 35))
        self.screen.blit(self.background, self.background_rect)
        self.all_bubbles.draw(self.screen)
        self.the_mouse.draw(self.screen)
        self.screen.blit(self.player.image,(pygame.mouse.get_pos()))
        self.pygame.display.flip()                                

    def update(self):
        self.anzahl += self.zähler
        if self.anzahl > 1:
            self.all_bubbles.add(Bubble(self.settings))
            self.anzahl = 0
        self.all_bubbles.update() 
        self.the_mouse.update()
        



if __name__ == '__main__':                                    
    settings = Settings()                               

    pygame.init()                                      

    game = Game(pygame, settings)                      

    game.run()                
  
    pygame.quit()             