import pygame
from settings import*
from laser import Laser

class Score:
    def __init__(self):
        self.font = pygame.font.Font('asteroid\graphics\subatomic.ttf', 50)
        self.score = Laser.count
        self.update_text()

    def update_text(self):
        self.score_text = f'Score: {self.score}'
        self.text_surf = self.font.render(self.score_text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
        


    
       