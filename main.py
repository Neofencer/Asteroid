import pygame, sys
from ship import Ship
from settings import*
from random import randint
from meteor import Meteor
from score import Score
from laser import Laser

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Asteroid shooter')
        self.clock= pygame.time.Clock()
        self.space_group=pygame.sprite.GroupSingle()
        #timer
        self.meteor_timer=pygame.event.custom_type()
        #pygame is going to raise this event meteor timer every 400 ms
        pygame.time.set_timer(self.meteor_timer,400)
        
        self.setup()
        self.score=Score()
        
    def setup(self):
        ship=Ship(self.space_group)
        
        
        #replace add group
    def random_pos(self):
        meteor_y_pos=randint(-150,-50)
        meteor_x_pos=randint(-100,WINDOW_WIDTH+100)
        position=(meteor_x_pos,meteor_y_pos)
        return position

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type==self.meteor_timer:
                   Meteor(self.random_pos(),groups=meteor_group)
                
                if event.type == self.meteor_timer:
                    Meteor(self.random_pos(), groups=meteor_group)

            score=Score()       
            dt=self.clock.tick()/1000
            pygame.display.update()
            
            
            background_surf=pygame.image.load('asteroid\graphics\Background.png').convert()
            self.display_surface.blit(background_surf,(0,0))
            self.display_surface.blit(score.text_surf,score.text_rect)
            
            #update groups
            self.space_group.update()
            laser_group.update(dt)
            meteor_group.update(dt)
            
                        
            

            #draw groups
            self.space_group.draw(self.display_surface)
            pygame.draw.rect(self.display_surface,(255,255,255),score.text_rect.inflate(30,30), width=8,border_radius=5)
            meteor_group.draw(self.display_surface)
            laser_group.draw(self.display_surface)
    
   


if __name__=='__main__':
    game = Game()
    game.run()
    