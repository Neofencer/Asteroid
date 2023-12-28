import pygame
from settings import*


class Laser(pygame.sprite.Sprite):
    count=0
    def __init__(self,pos,groups):
        #we have to init the parent class
        super().__init__(groups)
        #we need a surface call image as attribute
        self.image= pygame.image.load("asteroid\graphics\laser.png").convert_alpha()
        
        self.rect=self.image.get_rect(midbottom=pos)
        self.mask=pygame.mask.from_surface(self.image)
        self.pos=pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed=600
        
        self.explosion_sound=pygame.mixer.Sound('asteroid\sounds\explosion.wav')
        self.shoot_time=None
        
        
        
    def move(self,dt):
       self.pos +=self.direction * self.speed*dt
       self.rect.topleft=(round(self.pos.x),round(self.pos.y))
       
    
    def meteor_collision(self):
        
        if pygame.sprite.spritecollide(sprite=self, group=meteor_group, dokill=True,collided=pygame.sprite.collide_mask):
            Laser.count+=1
            self.kill()
            self.explosion_sound.play()
            
        
    
            

    def score(self):
        
        hits= pygame.sprite.spritecollideany(self,meteor_group)
        

       
            
        
           
        
       

    def update(self,dt):
        self.move(dt)
        self.meteor_collision()
        self.score()
        if self.rect.bottom<0:
            self.kill()
       
       