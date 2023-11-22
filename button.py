import pygame

class Button():
    def __init__(self, ai_setting, screen, msg):
        self.screen = screen
        self.screen_rect= screen.get_rect()

        #dimention and property of the button
        self.width, self.height = 90,40
        self.button_color_start=(60, 179, 113)
        self.button_color_end=(0,0,255)

        self.text_color=(126, 38, 215, 0.9)
        self.font= pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        

        #the button msg is prep once 
        self.prep_msg(msg)
    def prep_msg(self, msg):
        """render msg as image on the screen """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color_start)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color_start, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
