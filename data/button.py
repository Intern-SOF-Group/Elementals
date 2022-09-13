import pygame


class Button:
    game = None
    clicked_elements = True
    def __init__(self, x, y, image, scale, hover_image):
        self.mid_w, self.mid_h = self.game.mid_w, self.game.mid_h
        self.scale = scale
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width*scale), int(self.height*scale)))
        self.rect_image = self.image.get_rect()
        self.rect_image.center = (x, y)
        self.curr_image = self.image
        self.canvas = self.game.canvas
        self.clicked = True
        self.hover_image = pygame.transform.scale(hover_image, (int(self.width*scale), int(self.height*scale)))
        self.hover_sfx = pygame.mixer.Sound('assets/audio_files/button_sfx/button_hover_sfx.mp3')
        self.clicked_sfx = pygame.mixer.Sound('assets/audio_files/button_sfx/button_clicked_sfx.mp3')
        self.is_hovered = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_pos):
            self.curr_image = self.hover_image
        elif not self.rect_image.collidepoint(mouse_pos):
            self.curr_image = self.image  
        self.canvas.blit(self.curr_image, (self.rect_image.x, self.rect_image.y))


    def is_clicked2(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_pos):
            if not self.is_hovered:
                self.hover_sfx.play()
                self.is_hovered = True

            if pygame.mouse.get_pressed()[0] == 1 and self.game.clicked_global:
                # print('Button Clicked!')
                self.game.clicked_global = False
                self.clicked_sfx.play()
                return True
            elif not pygame.mouse.get_pressed()[0] and not self.game.clicked_global:
                self.game.clicked_global = True

        elif not self.rect_image.collidepoint(mouse_pos):
            if self.is_hovered:
                self.is_hovered = False

# this class button is specifically for the elements buttons because it needs I/O connection to the game logic
class ElementsButton(Button):
    def __init__(self, x, y, image, scale, hover_image, player_output_str):
        Button.__init__(self, x, y, image, scale, hover_image)
        # This is the I/O of this class to the game logic part of the game
        self.player_output_str = player_output_str
        self.player_output = self.game.game_logic

        # sfx of each element buttons (made into a dictionary for easy coding)
        self.elements_clicked_sfx = {
            "earth": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/earth_sfx.wav'),
            "fire": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/fire_sfx.wav'),
            "lightning": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/lightning_sfx.wav'),
            "water": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/water_sfx.wav'),
            "wind": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/wind_sfx.wav')
        }

    def player_input(self):
        if self.is_clicked_elements():
            self.player_output.player_move = self.player_output_str
            self.elements_clicked_sfx[self.player_output_str].play()
    
    def is_clicked_elements(self): # this fixes drag clicking
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked and Button.clicked_elements:
                # print('Button Clicked!')
                self.clicked = False
                Button.clicked_elements = False
                return True
            elif pygame.mouse.get_pressed()[0] == 0 and not self.clicked and not Button.clicked_elements:
                self.clicked = True
                Button.clicked_elements = True
        elif not self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 0 and not self.clicked and not Button.clicked_elements:
                self.clicked = True
                Button.clicked_elements = True
    
    def draw_elements(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_pos):
            self.curr_image = self.hover_image
        elif not self.rect_image.collidepoint(mouse_pos):
            self.curr_image = self.image
        self.canvas.blit(self.curr_image, (self.rect_image.x, self.rect_image.y))


class ImportElementsButton:
    def __init__(self):
        self.button_img_loc = 'assets/sent_images/button_images/elements'
        self.element_button_y = 660
        self.scale = 1
        self.x_offset = 150


        self.water_image = pygame.image.load(f'{self.button_img_loc}/water_button.png').convert_alpha()
        self.water_hover_image = pygame.image.load(f'{self.button_img_loc}/water_button_hover.png').convert_alpha()
        self.water_button = ElementsButton(0, 0, self.water_image, self.scale, self.water_hover_image, 'water')
        self.water_button.rect_image.center = (Button.game.mid_w, self.element_button_y)

        self.wind_image = pygame.image.load(f'{self.button_img_loc}/wind_button.png').convert_alpha()
        self.wind_hover_image = pygame.image.load(f'{self.button_img_loc}/wind_button_hover.png').convert_alpha()
        self.wind_button = ElementsButton(0, 0, self.wind_image, self.scale, self.wind_hover_image, 'wind')
        self.wind_button.rect_image.center = (self.water_button.rect_image.center[0] - self.x_offset, self.element_button_y)

        self.lightning_image = pygame.image.load(f'{self.button_img_loc}/lightning_button.png').convert_alpha()
        self.lightning_hover_image = pygame.image.load(f'{self.button_img_loc}/lightning_button_hover.png').convert_alpha()
        self.lightning_button = ElementsButton(0, 0, self.lightning_image, self.scale, self.lightning_hover_image, 'lightning')
        self.lightning_button.rect_image.center = (self.wind_button.rect_image.center[0] - self.x_offset, self.element_button_y)

        self.earth_image = pygame.image.load(f'{self.button_img_loc}/earth_button.png').convert_alpha()
        self.earth_hover_image = pygame.image.load(f'{self.button_img_loc}/earth_button_hover.png').convert_alpha()
        self.earth_button = ElementsButton(0, 0, self.earth_image, self.scale, self.earth_hover_image, 'earth')
        self.earth_button.rect_image.center = (self.water_button.rect_image.center[0] + self.x_offset, self.element_button_y)

        self.fire_image = pygame.image.load(f'{self.button_img_loc}/fire_button.png').convert_alpha()
        self.fire_hover_image = pygame.image.load(f'{self.button_img_loc}/fire_button_hover.png').convert_alpha()
        self.fire_button = ElementsButton(0, 0, self.fire_image, self.scale, self.fire_hover_image, 'fire')
        self.fire_button.rect_image.center = (self.earth_button.rect_image.center[0] + self.x_offset, self.element_button_y)

    def import_element_buttons(self):
        self.lightning_button.draw_elements()
        self.lightning_button.player_input()

        self.wind_button.draw_elements()
        self.wind_button.player_input()

        self.water_button.draw_elements()
        self.water_button.player_input()

        self.earth_button.draw_elements()
        self.earth_button.player_input()

        self.fire_button.draw_elements()
        self.fire_button.player_input()


class ImportMainMenuButton:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.main_menu.mid_w
        self.scale = 1
        self.y_offset = 125

        self.start_image = pygame.image.load(f'{self.button_img_loc}/start_button.png').convert_alpha()
        self.start_hover_image = pygame.image.load(f'{self.button_img_loc}/start_button_hover.png').convert_alpha()
        self.start_button = Button(self.mid_w, 370, self.start_image, self.scale, self.start_hover_image)


        self.credits_image = pygame.image.load(f'{self.button_img_loc}/credits_button.png').convert_alpha()
        self.credits_hover_image = pygame.image.load(f'{self.button_img_loc}/credits_button_hover.png').convert_alpha()
        self.credits_button = Button(self.mid_w, self.start_button.rect_image.centery + self.y_offset, self.credits_image, self.scale, self.credits_hover_image)

        self.quit_image = pygame.image.load(f'{self.button_img_loc}/quit_button.png').convert_alpha()
        self.quit_hover_image = pygame.image.load(f'{self.button_img_loc}/quit_button_hover.png').convert_alpha()
        self.quit_button = Button(self.mid_w, self.credits_button.rect_image.centery + self.y_offset, self.quit_image, self.scale, self.quit_hover_image)

    def import_menu_button(self):
        self.start_button.draw()
        self.quit_button.draw()
        self.credits_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.start_button.is_clicked2():
            self.main_menu.run_display = False
            Button.game.curr_menu = Button.game.max_points_menu

        elif self.credits_button.is_clicked2():
            self.main_menu.run_display = False
            Button.game.curr_menu = Button.game.credits_menu

        elif self.quit_button.is_clicked2():
            Button.game.quit_game()


class ImportMaxPointsMenuButton:
    def __init__(self, max_points_menu):
        self.max_points_menu = max_points_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.max_points_menu.mid_w
        self.scale = 1
        self.y_offset = 125

        self.long_game_image = pygame.image.load(f'{self.button_img_loc}/long_game_button.png').convert_alpha()
        self.long_game_hover_image = pygame.image.load(f'{self.button_img_loc}/long_game_button_hover.png').convert_alpha()
        self.long_game_button = Button(self.mid_w, 250, self.long_game_image, self.scale, self.long_game_hover_image)

        self.short_game_image = pygame.image.load(f'{self.button_img_loc}/short_game_button.png').convert_alpha()
        self.short_game_hover_image = pygame.image.load(f'{self.button_img_loc}/short_game_button_hover.png').convert_alpha()
        self.short_game_button = Button(self.mid_w, self.long_game_button.rect_image.centery + self.y_offset, self.short_game_image, self.scale, self.short_game_hover_image)

        self.back_image = pygame.image.load(f'{self.button_img_loc}/back_button.png').convert_alpha()
        self.back_hover_image = pygame.image.load(f'{self.button_img_loc}/back_button_hover.png').convert_alpha()
        self.back_button = Button(self.mid_w, self.short_game_button.rect_image.centery + self.y_offset, self.back_image, self.scale, self.back_hover_image)

    def import_max_points_menu_button(self):
        self.long_game_button.draw()
        self.short_game_button.draw()
        self.back_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.long_game_button.is_clicked2():
            Button.game.game_logic.max_points = 20
            self.max_points_menu.run_display = False
            Button.game.curr_menu = None
            Button.game.playing = True
            Button.game.playing2 = True

        elif self.short_game_button.is_clicked2():
            Button.game.game_logic.max_points = 10
            self.max_points_menu.run_display = False
            Button.game.curr_menu = None
            Button.game.playing = True
            Button.game.playing2 = True

        elif self.back_button.is_clicked2():
            self.max_points_menu.run_display = False
            Button.game.curr_menu = Button.game.main_menu

        
class ImportWinLoseMenuButton:
    def __init__(self, win_lose_menu):
        self.win_lose_menu = win_lose_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.win_lose_menu.mid_w
        self.scale = 1
        self.y_offset = 125


        self.play_again_image = pygame.image.load(f'{self.button_img_loc}/play_again_button.png').convert_alpha()
        self.play_again_hover_image = pygame.image.load(f'{self.button_img_loc}/play_again_button_hover.png').convert_alpha()
        self.play_again_button = Button(self.mid_w, 500, self.play_again_image, self.scale, self.play_again_hover_image)

        self.quit_image = pygame.image.load(f'{self.button_img_loc}/quit_button.png').convert_alpha()
        self.quit_hover_image = pygame.image.load(f'{self.button_img_loc}/quit_button_hover.png').convert_alpha()
        self.quit_button = Button(self.mid_w, self.play_again_button.rect_image.centery + self.y_offset, self.quit_image, self.scale, self.quit_hover_image)

    def import_win_lose_menu_button(self):
        self.play_again_button.draw()
        self.quit_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.play_again_button.is_clicked2():
            Button.game.win_state = ''
            Button.game.curr_menu = Button.game.max_points_menu
            self.win_lose_menu.run_display = False
        elif self.quit_button.is_clicked2():
            Button.game.quit_game()


class ImportHintMenuButton:
    def __init__(self, hint_menu):
        self.hint_menu = hint_menu
        self.button_img_loc = 'assets/sent_images/button_images'

        self.back_image = pygame.image.load(f'{self.button_img_loc}/back_button.png').convert_alpha()
        self.back_hover_image = pygame.image.load(f'{self.button_img_loc}/back_button_hover.png').convert_alpha()
        self.back_button = Button(Button.game.mid_w, 650, self.back_image, 1, self.back_hover_image)

    def import_hint_menu_button(self):
        self.back_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if Button.game.playing2:
            if self.back_button.is_clicked2():
                self.hint_menu.run_display = False
                Button.game.playing = True
        else:
            if self.back_button.is_clicked2():
                Button.game.curr_menu = Button.game.max_points_menu
                self.hint_menu.run_display = False

class ImportHintButton:
    def __init__(self, x, y, scale, game):
        self.game = game
        self.scale = scale
        self.button_img_loc = 'assets/sent_images/button_images'
        self.hint_image = pygame.image.load(f'{self.button_img_loc}/hint_button.png').convert_alpha()
        self.hint_hover_image = pygame.image.load(f'{self.button_img_loc}/hint_button_hover.png').convert_alpha()
        self.hint_button = Button(x, y, self.hint_image, self.scale, self.hint_hover_image)

    def import_hint_button(self):
        self.hint_button.draw()
        self.check_curr_menu()
    
    def check_curr_menu(self):
        if self.hint_button.is_clicked2():
            if Button.game.playing:
                self.game.playing = False
                self.game.curr_menu = Button.game.hint_menu
            else:
                self.game.curr_menu.run_display = False
                self.game.curr_menu = Button.game.hint_menu          


class ImportCreditsButton:
    def __init__(self, hint_menu):
        self.hint_menu = hint_menu
        self.mid_w = self.hint_menu.mid_w
        self.button_img_loc = 'assets/sent_images/button_images'
        self.back_image = pygame.image.load(f'{self.button_img_loc}/back_button.png').convert_alpha()
        self.back_hover_image = pygame.image.load(f'{self.button_img_loc}/back_button_hover.png').convert_alpha()
        self.back_button = Button(self.mid_w, 600, self.back_image, 1, self.back_hover_image)

    def import_credits_button(self):
        self.back_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.back_button.is_clicked2():
            self.hint_menu.run_display = False
            Button.game.curr_menu = Button.game.main_menu