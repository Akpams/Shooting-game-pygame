import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from allien import Allien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    
    pygame.init()
    settings_ai=Settings()
    screen = pygame.display.set_mode((settings_ai.screen_width, settings_ai.screen_height))
    pygame.display.set_caption("Akp-shoot Game")
    ship =Ship(settings_ai, screen)
    play_button= Button(settings_ai, screen, "Start")
    bullets=Group()
    alliens = Group()
    stats=GameStats(settings_ai)
    sb = Scoreboard(settings_ai, screen, stats)
    gf.create_fleet(settings_ai, screen,ship, alliens)
    # allien=Allien(settings_ai, screen)
    while True:
        gf.check_event(settings_ai, screen, stats, sb, play_button, ship, alliens,bullets)
        if stats.game_active and not settings_ai.pause:
            ship.updated_movement()
            gf.updated_bullets(settings_ai, screen, stats, sb, ship,alliens, bullets)
            gf.update_alliens(settings_ai,stats, screen, ship, alliens, bullets)
        gf.update_screen(settings_ai,screen, stats, sb, ship,alliens, bullets, play_button)     
    
run_game()