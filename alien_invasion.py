import pygame
from settings import Settings
from ship import Ship
from alien import  Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import  GameStats
from button import  Button
from scoreboard import  Scoreboard


def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("打飞机")
    play_button = Button(ai_settings, screen, "Play")
    alien = Alien(ai_settings, screen)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 开始游戏主循环
    while True:
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # 监视键鼠事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
