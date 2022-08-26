import pygame
# from menu import MainMenu
import sys
import button


class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.START_KEY = False
        self.DISPLAY_W, self.DISPLAY_H = 800, 500
        self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        # self.curr_menu = MainMenu(self)

        # Button objects inside the game
        self.start_image = pygame.image.load('images/sample_button.png').convert_alpha()
        self.test_button = button.Button(500, 300, self.start_image, 1, self)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.canvas.fill(self.BLACK)
            self.draw_text('Thanks for playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.test_button.draw()
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
