import pygame,sys
from settings import*
from laser import Laser
#from meteor import Meteor


class Ship (pygame.sprite.Sprite):
    def __init__(self,groups):
        #we have to init the parent class
        super().__init__(groups)
        #we need a surface call image as attribute
        self.image= pygame.image.load("asteroid\graphics\ship.png").convert_alpha()
        
        self.rect=self.image.get_rect(center=((WINDOW_WIDTH/2,WINDOW_HEIGHT/2)))
        
        #add the mask
        self.mask=pygame.mask.from_surface(self.image)
        #Timer
        self.can_shoot=True
        self.shoot_time=None

        #Sound
        self.laser_sound=pygame.mixer.Sound('asteroid\sounds\laser.ogg')
        
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time=pygame.time.get_ticks()
            if current_time-self.shoot_time>500:
                self.can_shoot=True



    def input_position(self):
        pos=pygame.mouse.get_pos()
        self.rect.center=pos

    def laser_shoot(self):
        
        
        #check mouse button pressed
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            
            Laser(self.rect.midtop,laser_group)
            
            self.can_shoot=False
            self.shoot_time=pygame.time.get_ticks()
            self.laser_sound.play()
            
    def meteor_collision(self):
        if pygame.sprite.spritecollide(sprite=self, group=meteor_group, dokill=True,collided=pygame.sprite.collide_mask):
            pygame.quit()
            sys.exit()

    def update(self):
        self.laser_timer()
        self.input_position()
        self.laser_shoot()
        self.meteor_collision()