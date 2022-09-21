import sys
import pygame
from data.button import Button, ImportElementsButton, ImportHintButton
from data import game_logic, sprites
from data.menu import CreditsMenu, MainMenu, SettingsMenu, MaxPointsMenu, WinLoseMenu, HintMenu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Elementals')
        Button.game = self
        self.clicked_global = True
        self.running = True
        self.playing = False
        self.playing2 = False # This is for hint buttons and also to have two states of playing
        self.DISPLAY_W, self.DISPLAY_H = 1200, 750
        self.mid_w, self.mid_h = self.DISPLAY_W/2, self.DISPLAY_H/2
        self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.scroll_game_canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H)) # the reason for another canvas because of the animation scroll
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.font_war = 'assets/sent_images/warpriest.ttf'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.VIOLET = (142, 68, 173)

        # Sounds
        self.sfx = 1.0
        self.music = 1.0
        self.bg_music = pygame.mixer.Sound('assets/audio_files/bg1_music.mp3')
        self.bg_music.set_volume(0.4)
        self.bg_music.play(loops=-1, fade_ms=1000)

        # menus
        self.main_menu = MainMenu(self)
        self.settings_menu = SettingsMenu(self)
        self.max_points_menu = MaxPointsMenu(self)
        self.win_lose_menu = WinLoseMenu(self)
        self.hint_menu = HintMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.curr_menu = self.main_menu

        # game background
        self.bg_img_loc = 'assets/sent_images'
        self.bg_img = pygame.image.load(f'{self.bg_img_loc}/bg4.png').convert_alpha()
        self.image_rect = self.bg_img.get_rect()
        self.image_rect.topleft = (0, 0)

        # game logic
        self.game_logic = game_logic.GameLogic(self)
        self.player_input = ''
        self.CPU_input = ''
        self.win_state = ''

        # Points text attributes
        self.playersy = 250
        self.CPU_pointsx, self.CPU_pointsy = 956, self.playersy
        self.player_pointsx, self.player_pointsy = 245, self.playersy
        self.point_size = 75
        self.point_offsety = -30
        self.ancient_font = 'assets/sent_images/AncientModernTales-a7Po.ttf'

        # buttons
        self.element_buttons = ImportElementsButton()
        self.hint_button = ImportHintButton(60, 700, 1, self)

        # element images
        self.turny = 400
        self.button_img_loc = 'assets/sent_images/button_images/elements'
        self.water_image = pygame.image.load(f'{self.button_img_loc}/water_button.png').convert_alpha()
        self.water_rect = self.water_image.get_rect()

        self.wind_image = pygame.image.load(f'{self.button_img_loc}/wind_button.png').convert_alpha()
        self.wind_rect = self.wind_image.get_rect()

        self.lightning_image = pygame.image.load(f'{self.button_img_loc}/lightning_button.png').convert_alpha()
        self.lightning_rect = self.lightning_image.get_rect()

        self.earth_image = pygame.image.load(f'{self.button_img_loc}/earth_button.png').convert_alpha()
        self.earth_rect = self.earth_image.get_rect()

        self.fire_image = pygame.image.load(f'{self.button_img_loc}/fire_button.png').convert_alpha()
        self.fire_rect = self.fire_image.get_rect()
      
        # clock
        self.clock = pygame.time.Clock()

        # Sprites
        self.turn_sprite = sprites.GameSprites(self.player_pointsx, self.turny)
        self.CPU_turn_sprite = sprites.GameSprites(self.CPU_pointsx, self.turny)
        self.group_sprites = pygame.sprite.Group()
        self.group_sprites.add(self.turn_sprite)
        self.group_sprites.add(self.CPU_turn_sprite)

        # Scroll Sprite
        self.scroll = sprites.ScrollSprite(self.player_pointsx)
        self.scroll_sprite_group = pygame.sprite.Group()
        self.scroll_sprite_group.add(self.scroll)

        


    def game_loop(self):
        while self.playing:
            self.check_events()

            self.scroll_game_canvas.blit(self.bg_img, self.image_rect.topleft)
            self.scroll_sprite_group.update()
            self.scroll_sprite_group.draw(self.scroll_game_canvas)

            self.canvas.blit(self.scroll_game_canvas, (0, 0))
            



            # draw element buttons and check for inputs
            self.element_buttons.import_element_buttons()
            self.hint_button.import_hint_button()

            self.game_logic.game_IO_loop()

            # Draw texts
            self.draw_text(str(self.game_logic.CPU.point), self.point_size, self.CPU_pointsx, self.CPU_pointsy, self.ancient_font, color=(0, 0, 0))
            self.draw_text(str(self.game_logic.player.point), self.point_size, self.player_pointsx, self.player_pointsy, self.ancient_font, color=(0, 0, 0))

            # Display turn images
            self.display_turn()

            # Display sprites
            self.draw_sprite()

            


            self.window.blit(self.canvas, (0, 0))
            pygame.display.update()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing, self.playing2 = False, False, False
                pygame.quit()
                sys.exit()
        
        # Sound settings
        self.bg_music.set_volume(0.4*self.music)

    def draw_text(self, text, size, x, y, font_name=pygame.font.get_default_font(), color=(255, 255, 255)):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.canvas.blit(text_surface, text_rect)

    def quit_game(self):
        self.curr_menu.run_display = False
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    # displays turn images
    def display_turn(self):
        if self.game_logic.game_start:
            self.turn_sprite.display_sprites = True
            self.turn_sprite.turn = self.player_input
            self.CPU_turn_sprite.turn = self.CPU_input

            if self.player_input == 'water':
                self.water_rect.center = (self.player_pointsx, self.turny)
                # self.canvas.blit(self.water_image, self.water_rect)
            elif self.player_input == 'wind':
                self.wind_rect.center = (self.player_pointsx, self.turny)
                # self.canvas.blit(self.wind_image, self.wind_rect)
            elif self.player_input == 'lightning':
                self.lightning_rect.center = (self.player_pointsx, self.turny)
                # self.canvas.blit(self.lightning_image, self.lightning_rect)
            elif self.player_input == 'earth':
                self.earth_rect.center = (self.player_pointsx, self.turny)
                # self.canvas.blit(self.earth_image, self.earth_rect)
            elif self.player_input == 'fire':
                self.fire_rect.center = (self.player_pointsx, self.turny)
                # self.canvas.blit(self.fire_image, self.fire_rect)

            if self.CPU_input == 'water':
                self.water_rect.center = (self.CPU_pointsx, self.turny)
                # self.canvas.blit(self.water_image, self.water_rect)
            elif self.CPU_input == 'wind':
                self.wind_rect.center = (self.CPU_pointsx, self.turny)
                # self.canvas.blit(self.wind_image, self.wind_rect)
            elif self.CPU_input == 'lightning':
                self.lightning_rect.center = (self.CPU_pointsx, self.turny)
                # self.canvas.blit(self.lightning_image, self.lightning_rect)
            elif self.CPU_input == 'earth':
                self.earth_rect.center = (self.CPU_pointsx, self.turny)
                # self.canvas.blit(self.earth_image, self.earth_rect)
            elif self.CPU_input == 'fire':
                self.fire_rect.center = (self.CPU_pointsx, self.turny)
                # self.canvas.blit(self.fire_image, self.fire_rect)

    def draw_sprite(self):
        self.group_sprites.update()
        if self.turn_sprite.display_sprites:
            self.group_sprites.draw(self.canvas)