import pygame
from button import ImportMainMenuButton, ImportMaxPointsMenuButton, ImportWinLoseMenuButton

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
       

    def blit_canvas(self):
        self.game.window.blit(self.game.canvas, (0,0))
        pygame.display.update()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menu_button = ImportMainMenuButton(self)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.canvas.fill(self.game.VIOLET)
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
