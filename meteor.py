import pygame
from settings import*
from random import randint,uniform

class Meteor(pygame.sprite.Sprite):
    total_destroyed=0
    def __init__(self,pos,groups):
        #we have to init the parent class
        super().__init__(groups)
        #randomizing the meteor size
    
        meteor_surf=pygame.image.load('asteroid\graphics\meteor.png')
        meteor_size=pygame.math.Vector2(meteor_surf.get_size())*uniform(0.5,1.5)
        self.scaled_surf=pygame.transform.scale(meteor_surf,meteor_size)
        self.image=self.scaled_surf
        

        self.rect=self.image.get_rect(center=pos)
        self.mask=pygame.mask.from_surface(self.image)
        self.pos=pygame.math.Vector2(self.rect.topright)
        self.direction = pygame.math.Vector2(uniform(-0.5,0.5),1)
        self.speed=randint(400,600)

        self.rotation = 0
        self.rotation_speed= randint(20,50)
    

    def rotate(self,dt):
        self.rotation += self.rotation_speed*dt
        rotate_surf=pygame.transform.rotozoom(self.scaled_surf,self.rotation,1)
        self.image=rotate_surf
        self.rect=self.image.get_rect(center=self.rect.center)
        #we are updating the mask if we get a rotation
        self.mask=pygame.mask.from_surface(self.image)   
    def move(self,dt):
         self.pos +=self.direction * self.speed*dt
         self.rect.topright=(round(self.pos.x),round(self.pos.y))
         
    
    def update(self,dt):
        self.move(dt)
        self.rotate(dt)
        if self.rect.top>WINDOW_HEIGHT:
            self.kill()
    
    def kill(self):
        Meteor.total_destroyed += 1  # Increment the total count before killing the instance
        super().kill() 