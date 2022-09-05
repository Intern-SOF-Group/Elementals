import sys
import pygame
from button import *
import game_logic
# from debugger_pygame import debug
from menu import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Elementals')
        Button.game = self
        self.clicked_global = True
        self.running = True
        self.playing = False
        self.START_KEY = False
        self.DISPLAY_W, self.DISPLAY_H = 800, 500
        self.mid_w, self.mid_h = self.DISPLAY_W/2, self.DISPLAY_H/2
        self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.font_war = 'assets/sent_images/warpriest.ttf'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.VIOLET = (142, 68, 173)
        self.main_menu = MainMenu(self)
        self.max_points_menu = MaxPointsMenu(self)
        self.win_lose_menu = WinLoseMenu(self)
        self.hint_menu = HintMenu(self)
        self.curr_menu = self.main_menu

        # game background
        self.bg_img_loc = 'assets/sent_images'
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/main_game_bg.png').convert_alpha()
        self.image_rect = self.bg_img.get_rect()
        self.image_rect.topleft = (0, 0)

        # game logic
        self.game_logic = game_logic.GameLogic(self)

        # Points text attributes
        self.CPU_pointsx, self.CPU_pointsy = 600, 100
        self.player_pointsx, self.player_pointsy = 200, 100
        self.point_size = 25
        self.point_offsety = -30

        # buttons
        self.element_buttons = ImportElementsButton()
        self.hint_button = ImportHintMenuButton(self.hint_menu)
        
    def game_loop(self):
        while self.playing:
            self.check_events()
            self.canvas.fill(self.VIOLET)
            self.canvas.blit(self.bg_img, self.image_rect.topleft)

            # draw element buttons and check for inputs
            self.element_buttons.import_element_buttons()
            # self.hint_button.import_hint_menu_button()

            self.game_logic.game_IO_loop()

            # Draw texts
            self.draw_text('CPU Points', self.point_size, self.CPU_pointsx, self.CPU_pointsy + self.point_offsety)
            self.draw_text(str(self.game_logic.CPU.point), self.point_size, self.CPU_pointsx, self.CPU_pointsy)
            self.draw_text('Player Points', self.point_size, self.player_pointsx, self.player_pointsy + self.point_offsety)
            self.draw_text(str(self.game_logic.player.point), self.point_size, self.player_pointsx, self.player_pointsy)


            self.window.blit(self.canvas, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass

    def reset_keys(self):
        pass

    def draw_text(self, text, size, x, y, font_name=pygame.font.get_default_font(), color=(255, 255, 255)):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.canvas.blit(text_surface, text_rect)

    def quit_game(self):
        self.curr_menu.run_display = False
        pygame.event.post(pygame.event.Event(pygame.QUIT))
