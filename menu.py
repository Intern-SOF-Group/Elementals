import pygame
from button import ImportMainMenuButton, ImportMaxPointsMenuButton, ImportWinLoseMenuButton

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.bg_img_loc = 'assets/sent_images'
       

    def blit_canvas(self):
        self.game.window.blit(self.game.canvas, (0,0))
        pygame.display.update()

    def bg_loader(self, img, scale):
        W = img.get_width()
        H = img.get_height()
        image = pygame.transform.scale(img, (int(W*scale), int(H*scale)))
        image_rect = image.get_rect()
        image_rect.topleft = (0, 0)
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
            # self.game.canvas.fill(self.game.VIOLET)
            self.bg_loader(self.bg_img, 1)

            self.game.check_events()
            self.menu_button.import_menu_button()
            self.blit_canvas()

class MaxPointsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menu_button = ImportMaxPointsMenuButton(self)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.canvas.fill(self.game.VIOLET)
            self.game.check_events()
            self.menu_button.import_max_points_menu_button()
            self.blit_canvas()


class WinLoseMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.win_lose_button = ImportWinLoseMenuButton(self)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.canvas.fill(self.game.VIOLET)
            self.game.check_events()
            self.win_lose_button.import_win_lose_menu_button()
            self.blit_canvas()
