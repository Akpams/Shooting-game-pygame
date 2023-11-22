import pygame
import pygame.font

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats= stats

        #settings for scoring information
        self.text_color=(60, 60, 60)
        self.font= pygame.font.SysFont(None,48)
        #initial score image
        self.prep_score()
        self.prep_high_score()
        
    def prep_score(self):
        score_str =  str(self.stats.score)
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: " + " {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bgr_color)

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top =10
    def prep_high_score(self):
        high_score=str(self.stats.high_score)
        rounded_h_score=int(round(self.stats.high_score, -1))
        high_score="High Score: " + "{:,}".format(rounded_h_score)
        self.high_score_image = self.font.render(high_score, True, self.text_color, self.ai_settings.bgr_color)

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx= self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
   
