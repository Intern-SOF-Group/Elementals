import sys
import pygame
# from menu import MainMenu
import button
import game_logic
from debugger_pygame import debug


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Elementals')
        self.running = True
        self.playing = False
        self.START_KEY = False
        self.DISPLAY_W, self.DISPLAY_H = 800, 500
        self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.VIOLET = (142, 68, 173)
        # self.clicked_global = True # fixes drag clicking
        # self.curr_menu = MainMenu(self)

        # game logic
        self.game_logic = game_logic.GameLogic(self)

        # Element buttons
        self.element_button_scale = 8.05/15
        self.element_button_y = 1180/3 + 1

        # self.lightning_image = pygame.image.load('images/lightning_button.png').convert_alpha()
        # self.lightning_button = button.ElementsButton(0, 0, self.lightning_image, self.element_button_scale, self, 'lightning')
        # self.lightning_button.rect_image.topleft = (0, self.element_button_y)

        # self.wind_image = pygame.image.load('images/wind_button.png').convert_alpha()
        # self.wind_button = button.ElementsButton(0, 0, self.wind_image, self.element_button_scale, self, 'wind')
        # self.wind_button.rect_image.topleft = (self.lightning_button.rect_image.topright[0] - 1, self.element_button_y)

        # self.water_image = pygame.image.load('images/water_button.png').convert_alpha()
        # self.water_button = button.ElementsButton(0, 0, self.water_image, self.element_button_scale, self, 'water')
        # self.water_button.rect_image.topleft = (self.wind_button.rect_image.topright[0], self.element_button_y)

        # self.earth_image = pygame.image.load('images/earth_button.png').convert_alpha()
        # self.earth_button = button.ElementsButton(0, 0, self.earth_image, self.element_button_scale, self, 'earth')
        # self.earth_button.rect_image.topleft = (self.water_button.rect_image.topright[0], self.element_button_y)

        # self.fire_image = pygame.image.load('images/fire_button.png').convert_alpha()
        # self.fire_button = button.ElementsButton(0, 0, self.fire_image, self.element_button_scale, self, 'fire')
        # self.fire_button.rect_image.topleft = (self.earth_button.rect_image.topright[0], self.element_button_y)


        # Points text attributes
        self.CPU_pointsx, self.CPU_pointsy = 600, 100
        self.player_pointsx, self.player_pointsy = 200, 100
        self.point_size = 25
        self.point_offsety = -30

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.canvas.fill(self.VIOLET)

            # draw element buttons and check for inputs
            # self.lightning_button.draw()
            # self.lightning_button.player_input()
            # self.wind_button.draw()
            # self.water_button.draw()
            # self.earth_button.draw()
            # self.fire_button.draw()
            button.import_element_buttons(self, self.element_button_scale)

            self.game_logic.game_IO_loop()
            debug(self.game_logic.cpu_input, 725, 10, self.canvas)

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
                # self.curr_menu.run_display = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass

    def reset_keys(self):
        pass

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.canvas.blit(text_surface, text_rect)

    def quit_game(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
