import pygame
from data.button import ImportMainMenuButton, ImportSettingsMenuButton, ImportMaxPointsMenuButton, ImportHintButton, ImportWinLoseMenuButton, ImportHintMenuButton, ImportCreditsButton

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.bg_img_loc = 'assets/sent_images'
        self.VIOLET = (142, 68, 173)

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
        self.title = pygame.image.load(f'{self.bg_img_loc}/title.png').convert_alpha()

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.bg_loader(self.bg_img, 1)
            self.bg_loader(self.title, 1, self.mid_w, 150)

            self.game.check_events()
            self.menu_button.import_menu_button()
            self.blit_canvas()
    
    def draw_text(self, text, size, x, y, font_name=pygame.font.get_default_font(), color=(255, 255, 255)):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.game.canvas.blit(text_surface, text_rect)

class SettingsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.bg_rect = pygame.rect.Rect((0, 0), (self.game.DISPLAY_W, self.game.DISPLAY_H))
        self.bg_rect.topleft = (0, 0)
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/bg1.png').convert_alpha()

        self.settings_button = ImportSettingsMenuButton(self)

        # Texts
        self.music_txt = pygame.font.Font
  
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.bg_loader(self.bg_img, 1)
            self.settings_button.import_settings_button()

            self.draw_text('Music', 80, self.game.mid_w, self.settings_button.volume_button.bar_rect.centery - 50, self.game.ancient_font)
            self.draw_text('SFX', 80, self.game.mid_w, self.settings_button.sfx_button.bar_rect.centery - 50, self.game.ancient_font)


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
        self.hint_button = ImportHintButton(75, 675, 1, self.game)

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
        self.win_sfx = pygame.mixer.Sound('assets/audio_files/win_sfx.wav')
        self.lose_sfx = pygame.mixer.Sound('assets/audio_files/lose_sfx.wav')
        self.sfx = self.game.sfx


    def display_menu(self):
        self.run_display = True
        self.sfx = self.game.sfx
        self.win_sfx.set_volume(self.sfx)
        self.lose_sfx.set_volume(self.sfx)

        if self.game.win_state == 'You Win!':
            self.win_sfx.play()
        elif self.game.win_state == 'You Lose!':
            self.lose_sfx.play()

        while self.run_display:
            self.bg_loader(self.bg_img, 1)
            self.game.check_events()
            self.game.draw_text(self.game.win_state, 151, self.mid_w, 200, self.game.ancient_font)
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


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.back_button = ImportCreditsButton(self)
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/creditsbg.png').convert_alpha()
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.bg_loader(self.bg_img, 1)
            self.game.check_events()
            self.back_button.import_credits_button()
            self.blit_canvas()
