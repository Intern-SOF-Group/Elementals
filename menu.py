import pygame
from button import ImportHintButton, ImportHintMenuButton, ImportMainMenuButton, ImportMaxPointsMenuButton, ImportWinLoseMenuButton

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.bg_img_loc = 'assets/sent_images'
       

    def blit_canvas(self):
        self.game.window.blit(self.game.canvas, (0,0))
        pygame.display.update()

    def bg_loader(self, img, scale, x=0, y=0):
        W = img.get_width()
        H = img.get_height()
        image = pygame.transform.scale(img, (int(W*scale), int(H*scale)))
        if x==0 and y==0:
            image_rect = image.get_rect()
            image_rect.topleft = (0, 0)
        else:
            image_rect = image.get_rect()
            image_rect.center = (x, y)
        self.draw_bg(image, image_rect)

    def draw_bg(self, image, image_rect):
        self.game.canvas.blit(image, image_rect.topleft)



class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menu_button = ImportMainMenuButton(self)
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/bg1.png').convert_alpha()


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.bg_loader(self.bg_img, 1)
            self.draw_text('ELEMENTALS', 150, self.mid_w, 100, self.game.font_war, (38, 19, 0))

            self.game.check_events()
            self.menu_button.import_menu_button()
            self.blit_canvas()
    
    def draw_text(self, text, size, x, y, font_name=pygame.font.get_default_font(), color=(255, 255, 255)):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.game.canvas.blit(text_surface, text_rect)

class MaxPointsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menu_button = ImportMaxPointsMenuButton(self)
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/bg2.png').convert_alpha()
        self.hint_button = ImportHintButton(50, 450, 1, self.game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.bg_loader(self.bg_img, 1)
            self.game.check_events()
            self.menu_button.import_max_points_menu_button()
            self.hint_button.import_hint_button()
            self.blit_canvas()


class WinLoseMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.win_lose_button = ImportWinLoseMenuButton(self)
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/bg2.png').convert_alpha()

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.bg_loader(self.bg_img, 1)
            self.game.check_events()
            self.win_lose_button.import_win_lose_menu_button()
            self.blit_canvas()

class HintMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.hint_button = ImportHintMenuButton(self)
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/hint.png').convert_alpha()
        self.bg2_img = pygame.image.load(f'{self.bg_img_loc}/bg2.png').convert_alpha()

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.bg_loader(self.bg2_img, 1)
            self.bg_loader(self.bg_img, 1, self.mid_w, self.mid_h)
            self.game.check_events()
            self.hint_button.import_hint_menu_button()
            self.blit_canvas()
