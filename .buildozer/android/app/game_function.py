import pygame
import sys
from bullet import Bullet
from allien import Allien
import time

def check_keydown_event(event, ai_settings, screen,ship, bullets):
    if event.key==pygame.K_RIGHT:
        ship.move_right=True
    elif event.key==pygame.K_LEFT:
        ship.move_left=True
    elif event.key ==pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    
    elif event.key==pygame.K_q:
        sys.exit()
def update_screen(ai_settings, screen, stats, sb, ship,alliens, bullets, play_button):
    screen.fill(ai_settings.bgr_color)
    ship.blitme()
    alliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #draw the score information
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
def updated_bullets(ai_settings, screen, stats, sb, ship, alliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)  
   
    check_bullet_allien_collision(ai_settings, screen, stats, sb, ship, alliens, bullets)
    
def check_bullet_allien_collision(ai_settings, screen, stats, sb, ship, alliens, bullets):
    #check bullet that hit allien
    collisions= pygame.sprite.groupcollide(bullets, alliens, True, True) 
    if len(alliens)==0:
        #destroy existing bullets, speed up gam  e and create a new fleets

        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, alliens)
    if collisions:
        for allien in collisions.values():
            stats.score+= ai_settings.allien_point *len(allien)
            sb.prep_score()
        check_high_score(stats,sb)
def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets)<=ai_settings.bullet_allowed:
            new_bullets= Bullet(ai_settings, screen, ship)
            bullets.add(new_bullets)
def check_keyup_event(event, ship):
    if event.key==pygame.K_RIGHT:
        ship.move_right=False
    elif event.key==pygame.K_LEFT:
        ship.move_left=False
def check_event(ai_settings, screen, stats, play_button, ship,alliens, bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_event(event,ai_settings, screen, ship, bullets)
            if event.key == pygame.K_ESCAPE or event.key ==pygame.K_BACKSPACE:
                # stats.game_active=not stats.game_active
                ai_settings.pause = not ai_settings.pause  
        elif event.type ==pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings, screen,stats, play_button, ship, alliens, bullets,mouse_x, mouse_y)

def get_number_alliens(ai_settings,allien_width):
    """ Determine the number of allien that fit in a row."""
    available_space_x= ai_settings.screen_width-2*allien_width
    number_allien_x=int(available_space_x/(2*allien_width))
    return number_allien_x
def get_number_row(ai_settings, ship_height, allien_height):
    available_space_y=(ai_settings.screen_height-(3*allien_height)-ship_height)
    number_row=int(available_space_y/(2*allien_height))
    return number_row

def create_allien(ai_settings, screen, alliens, allien_number , row_number):
    """create allien and place it in the row."""
    allien=Allien(ai_settings, screen)
    allien_width = allien.rect.width
    allien.x= allien_width+ 2*allien_width*allien_number
    allien.rect.y=allien.rect.height + 2* allien.rect.height * row_number
    allien.rect.x= allien.x
    alliens.add(allien)


            
def create_fleet(ai_settings, screen,ship, alliens):
    allien=Allien(ai_settings, screen)
    number_allien_x=get_number_alliens(ai_settings, allien.rect.width)
    number_rows=get_number_row(ai_settings, ship.rect.height, allien.rect.height)
    for row_number in range(number_rows):
        for allien_number in range(number_allien_x):
            create_allien(ai_settings, screen, alliens, allien_number, row_number)
def check_fleet_edges(ai_settings, alliens):
    for allien in alliens.sprites():
        if allien.check_edge():
            change_fleet_direction(ai_settings,alliens)
            break
def change_fleet_direction(ai_setting, alliens):
    for allien in alliens.sprites():
        allien.rect.y+=ai_setting.fleet_drop_speed
    ai_setting.fleet_direction*=-1
def update_alliens(ai_settings, stats, screen, ship, alliens, bullets):
    check_fleet_edges(ai_settings, alliens)
    alliens.update()
    if pygame.sprite.spritecollideany(ship, alliens):
        ship_hit(ai_settings, stats, screen, ship, alliens, bullets)
    check_allien_bottom(ai_settings, stats, screen, ship, alliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, alliens, bullets):
    """responds to ship being hit by allien"""
    if stats.ships_left>0:
        stats.ships_left -=1 
        # empty the list of alliens and bullents
        alliens.empty()
        bullets.empty()

        #create new fleet 
        create_fleet(ai_settings, screen,ship, alliens)
        ship.center_ship()
        #pause for some time 
        time.sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def check_allien_bottom(ai_settings, stats, screen, ship, alliens, bullets):
    screen_rect =screen.get_rect()
    for allien in alliens.sprites():
        if allien.rect.bottom >=screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, alliens, bullets)
            break

def check_play_button(ai_settings, screen,stats, play_button, ship, alliens, bullets,mouse_x, mouse_y):
    """ start a new game when play clicks start button """
    button_clicked=play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        #reset the game setting 
        ai_settings.initize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.rest_stats()
        stats.game_active = True
        alliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen,ship, alliens)
        ship.center_ship()
def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()