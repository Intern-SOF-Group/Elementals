import pygame


class Button:
    game = None
    clicked_elements = False
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
        self.hover_sfx.set_volume(0.1)
        self.clicked_sfx = pygame.mixer.Sound('assets/audio_files/button_sfx/button_clicked_sfx.wav')
        self.clicked_sfx.set_volume(0.4)
        self.is_hovered = False
        self.sfx = self.game.sfx

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_pos):
            self.curr_image = self.hover_image
        elif not self.rect_image.collidepoint(mouse_pos):
            self.curr_image = self.image  
        self.canvas.blit(self.curr_image, (self.rect_image.x, self.rect_image.y))

        # Sounds
        self.sfx = self.game.sfx
        self.hover_sfx.set_volume(0.1*self.sfx)
        self.clicked_sfx.set_volume(0.4*self.sfx)



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
    # higlight buttons at the start of game
    highlight_state = True # this is the togglestate of individual element button
    curr_highlight = ''
    highlight_duration = 1 # duration on how long the highlight will last
    highlight_time = 0 # an if variable to check if this is equals to the highlight_duration
    is_clicking_timer = 0 # this increases if player is not clicking element buttons
    is_clicking_max_timer = 8 # this will let the highlight trigger if is_clicking_timer reached this

    def __init__(self, x, y, image, scale, hover_image, player_output_str):
        Button.__init__(self, x, y, image, scale, hover_image)
        # This is the I/O of this class to the game logic part of the game
        self.player_output_str = player_output_str
        self.player_output = self.game.game_logic

        
        # sfx of each element buttons (made into a dictionary for easy coding)
        self.elements_clicked_sfx = {
            "earth": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/earth_sfx.wav'),
            "fire": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/fire_sfx.wav'),
            "lightning": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/lightning_sfx.mp3'),
            "water": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/water_sfx.wav'),
            "wind": pygame.mixer.Sound('assets/audio_files/button_sfx/elements_button_sfx/wind_sfx.wav')
        }
        self.sfx = self.game.sfx


        for i in self.elements_clicked_sfx.values():
            i.set_volume(0.4)

    def player_input(self):
        self.player_output = self.game.game_logic
        if self.is_clicked_elements():
            if Button.game.game_logic == Button.game.single_player:
                self.player_output.player_move = self.player_output_str
                self.elements_clicked_sfx[self.player_output_str].play()

            elif Button.game.game_logic == Button.game.two_player:
                if not self.player_output.player1_move:
                    self.player_output.player1_move = self.player_output_str
                elif self.player_output.player1_move:
                    self.player_output.player2_move = self.player_output_str

                # self.elements_clicked_sfx[self.player_output_str].play()

    
    def is_clicked_elements(self): # this fixes drag clicking
        mouse_pos = pygame.mouse.get_pos()

        if self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked and not Button.clicked_elements:
                self.clicked = False
                Button.clicked_elements = True
                return True
            elif pygame.mouse.get_pressed()[0] == 0 and not self.clicked and Button.clicked_elements:
                self.clicked = True
                Button.clicked_elements = False

        elif not self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 0 and not self.clicked and Button.clicked_elements:
                self.clicked = True
                Button.clicked_elements = False
    
    def draw_elements(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_pos) or (self.highlight_state and self.curr_highlight==self.player_output_str):
            self.curr_image = self.hover_image

        elif not self.rect_image.collidepoint(mouse_pos):
            self.curr_image = self.image

        self.canvas.blit(self.curr_image, (self.rect_image.x, self.rect_image.y))

        # Sounds
        self.sfx = self.game.sfx
        for i in self.elements_clicked_sfx.values():
            i.set_volume(0.4*self.sfx)

    

class ImportElementsButton:
    def __init__(self):
        self.button_img_loc = 'assets/sent_images/button_images/elements'
        self.element_button_y = 660
        self.scale = 1
        self.x_offset = 150

        # for highlight
        self.element_list = ['lightning', 'wind', 'water', 'earth', 'fire']
        self.element_index = 0

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
        self.highlight()
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


    def highlight(self):
        if Button.clicked_elements:
            ElementsButton.is_clicking_timer = 0
            ElementsButton.highlight_state = False
            ElementsButton.highlight_time = 0
            self.element_index = 0

        if not Button.clicked_elements and not ElementsButton.highlight_state: # for highlights
            ElementsButton.is_clicking_timer += 0.1

            if int(ElementsButton.is_clicking_timer) >= ElementsButton.is_clicking_max_timer:
                ElementsButton.highlight_state = True
                ElementsButton.is_clicking_timer = 0
            
        if ElementsButton.highlight_state:
            ElementsButton.highlight_time += 0.1
            if not int(ElementsButton.highlight_time >= ElementsButton.highlight_duration):
                ElementsButton.curr_highlight = self.element_list[self.element_index]

            elif self.element_index >= 4:
                self.element_index = 0
                ElementsButton.highlight_state = False
                ElementsButton.highlight_time = 0

            elif int(ElementsButton.highlight_time >= ElementsButton.highlight_duration):
                self.element_index += 1
                ElementsButton.highlight_time = 0
            
            
class ImportMainMenuButton:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.main_menu.mid_w
        self.scale = 1
        self.y_offset = 110

        self.start_image = pygame.image.load(f'{self.button_img_loc}/start_button.png').convert_alpha()
        self.start_hover_image = pygame.image.load(f'{self.button_img_loc}/start_button_hover.png').convert_alpha()
        self.start_button = Button(self.mid_w, 325, self.start_image, self.scale, self.start_hover_image)

        self.settings_image = pygame.image.load(f'{self.button_img_loc}/settings_button.png').convert_alpha()
        self.settings_hover_image = pygame.image.load(f'{self.button_img_loc}/settings_button_hover.png').convert_alpha()
        self.settings_button = Button(self.mid_w, self.start_button.rect_image.centery + self.y_offset, self.settings_image, self.scale, self.settings_hover_image)


        self.credits_image = pygame.image.load(f'{self.button_img_loc}/credits_button.png').convert_alpha()
        self.credits_hover_image = pygame.image.load(f'{self.button_img_loc}/credits_button_hover.png').convert_alpha()
        self.credits_button = Button(self.mid_w, self.settings_button.rect_image.centery + self.y_offset, self.credits_image, self.scale, self.credits_hover_image)

        self.quit_image = pygame.image.load(f'{self.button_img_loc}/quit_button.png').convert_alpha()
        self.quit_hover_image = pygame.image.load(f'{self.button_img_loc}/quit_button_hover.png').convert_alpha()
        self.quit_button = Button(self.mid_w, self.credits_button.rect_image.centery + self.y_offset, self.quit_image, self.scale, self.quit_hover_image)

    def import_menu_button(self):
        self.start_button.draw()
        self.settings_button.draw()
        self.quit_button.draw()
        self.credits_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.start_button.is_clicked2():
            self.main_menu.run_display = False
            Button.game.curr_menu = Button.game.game_mode_menu
        
        elif self.settings_button.is_clicked2():
            self.main_menu.run_display = False
            Button.game.curr_menu = Button.game.settings_menu


        elif self.credits_button.is_clicked2():
            self.main_menu.run_display = False
            Button.game.curr_menu = Button.game.credits_menu

        elif self.quit_button.is_clicked2():
            self.main_menu.run_display = False
            Button.game.last_menu = Button.game.main_menu
            Button.game.curr_menu = Button.game.quit_menu



class ImportGameModeMenuButton:
    def __init__(self, game_mode_menu) -> None:
        self.game_mode_menu = game_mode_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.game_mode_menu.mid_w
        self.scale = 1
        self.y_offset = 110

        self.oneplayer_image = pygame.image.load(f'{self.button_img_loc}/oneplayer_button.png').convert_alpha()
        self.oneplayer_hover_image = pygame.image.load(f'{self.button_img_loc}/oneplayer_button_hover.png').convert_alpha()
        self.oneplayer_button = Button(self.mid_w, 325, self.oneplayer_image, self.scale, self.oneplayer_hover_image)

        self.twoplayer_image = pygame.image.load(f'{self.button_img_loc}/twoplayer_button.png').convert_alpha()
        self.twoplayer_hover_image = pygame.image.load(f'{self.button_img_loc}/twoplayer_button_hover.png').convert_alpha()
        self.twoplayer_button = Button(self.mid_w, 500, self.twoplayer_image, self.scale, self.twoplayer_hover_image)

    def import_game_mode_menu_button(self):
        self.oneplayer_button.draw()
        self.twoplayer_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.oneplayer_button.is_clicked2():
            self.game_mode_menu.run_display = False
            Button.game.game_logic = Button.game.single_player
            Button.game.curr_menu = Button.game.max_points_menu

        elif self.twoplayer_button.is_clicked2():
            self.game_mode_menu.run_display = False
            Button.game.game_logic = Button.game.two_player
            Button.game.curr_menu = Button.game.max_points_menu



class VolumeSlider:
    def __init__(self, game, y, target_volume="None") -> None:
        self.game = game
        self.target_volume = target_volume
        self.canvas = game.canvas
        self.mid_w = game.mid_w
        self.bar_slide = pygame.image.load(r"assets\sent_images\button_images\settings\bar.png")
        self.bar_rect = self.bar_slide.get_rect()
        self.bar_rect.center = (self.mid_w, y)

        self.slider = pygame.image.load(r"assets\sent_images\button_images\settings\slider.png")
        self.slider_unclicked = pygame.image.load(r"assets\sent_images\button_images\settings\slider.png")
        self.slider_hovered = pygame.image.load(r"assets\sent_images\button_images\settings\slider_hover.png")
        self.slider_clicked = pygame.image.load(r"assets\sent_images\button_images\settings\slider_clicked.png")

        self.slider_rect = self.slider.get_rect()
        self.slider_rect.centery = self.bar_rect.centery
        self.slider_rect.centerx = self.bar_rect.right

        # Slider rules
        self.slider_isclicked = False # the use of this is so that the slider can still slide while clicking even if it is not colliding with the mouse pointer

        # Tester volume
        self.volume = 1.0

    def draw(self):
        self.canvas.blit(self.bar_slide, self.bar_rect)
        self.canvas.blit(self.slider, self.slider_rect)
        # print(self.volume)
        # print(self.slider_rect.centerx)

    def check_input(self):
        mouse_pos  = pygame.mouse.get_pos()
        self.slider = self.slider_unclicked # I placed it at the top so that if any of the arguments below are true it will just be overwritten

        if self.slider_rect.collidepoint(mouse_pos):
            self.slider = self.slider_hovered
            if pygame.mouse.get_pressed()[0]:
                self.slider_isclicked = True

        if not pygame.mouse.get_pressed()[0]:
            self.slider_isclicked = False

        # This part is so that the slider does not go beyond the size of the bar
        if self.slider_isclicked:
            self.slider = self.slider_clicked
            if self.bar_rect.left < self.slider_rect.centerx < self.bar_rect.right:
                self.slider_rect.centerx = mouse_pos[0]

            elif self.slider_rect.centerx <= self.bar_rect.left:
                self.slider_rect.centerx = max(mouse_pos[0], self.bar_rect.left)
         
            elif self.slider_rect.centerx >= self.bar_rect.right:
                self.slider_rect.centerx = min(mouse_pos[0], self.bar_rect.right)

        # Changes the volume value according to the postition of the slider
        self.volume = (self.slider_rect.centerx - self.bar_rect.left)/(self.bar_rect.width)    
        if self.target_volume == 'music':
            self.game.music = self.volume
        elif self.target_volume == 'sfx':
            self.game.sfx = self.volume
        else:
            pass    

class ImportSettingsMenuButton:
    def __init__(self, settings_menu):
        self.settings_menu = settings_menu
        self.canvas = self.settings_menu.game.canvas
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.settings_menu.mid_w

        self.back_image = pygame.image.load(f'{self.button_img_loc}/back_button.png').convert_alpha()
        self.back_hover_image = pygame.image.load(f'{self.button_img_loc}/back_button_hover.png').convert_alpha()
        self.back_button = Button(self.mid_w, 650, self.back_image, 1, self.back_hover_image)

        self.volume_button = VolumeSlider(self.settings_menu.game, 250, target_volume='music')
        self.sfx_button = VolumeSlider(self.settings_menu.game, 450, target_volume='sfx')



    def import_settings_button(self):
        self.back_button.draw()
        self.check_curr_menu()

        self.volume_button.check_input()
        self.volume_button.draw()

        self.sfx_button.check_input()
        self.sfx_button.draw()


    def check_curr_menu(self):
        if self.back_button.is_clicked2():
            if Button.game.playing2:
                self.settings_menu.run_display = False
                Button.game.curr_menu = Button.game.pause_menu
                
            else:
                self.settings_menu.run_display = False
                Button.game.curr_menu = Button.game.main_menu


class ImportMaxPointsMenuButton:
    def __init__(self, max_points_menu):
        self.max_points_menu = max_points_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.max_points_menu.mid_w
        self.scale = 1
        self.y_offset = 125

        self.long_game_image = pygame.image.load(f'{self.button_img_loc}/long_game_button.png').convert_alpha()
        self.long_game_hover_image = pygame.image.load(f'{self.button_img_loc}/long_game_button_hover2.png').convert_alpha()
        self.long_game_button = Button(self.mid_w, 250, self.long_game_image, self.scale, self.long_game_hover_image)

        self.short_game_image = pygame.image.load(f'{self.button_img_loc}/short_game_button.png').convert_alpha()
        self.short_game_hover_image = pygame.image.load(f'{self.button_img_loc}/short_game_button_hover2.png').convert_alpha()
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
            Button.game.curr_menu = Button.game.game_mode_menu

        
class ImportWinLoseMenuButton:
    def __init__(self, win_lose_menu):
        self.win_lose_menu = win_lose_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.win_lose_menu.mid_w
        self.scale = 0.8
        self.y_offset = 100


        self.play_again_image = pygame.image.load(f'{self.button_img_loc}/play_again_button.png').convert_alpha()
        self.play_again_hover_image = pygame.image.load(f'{self.button_img_loc}/play_again_button_hover.png').convert_alpha()
        self.play_again_button = Button(self.mid_w, 350, self.play_again_image, self.scale, self.play_again_hover_image)

        self.main_menu_image = pygame.image.load(f'{self.button_img_loc}/main_menu_button.png').convert_alpha()
        self.main_menu_hover_image = pygame.image.load(f'{self.button_img_loc}/main_menu_button_hover.png').convert_alpha()
        self.main_menu_button = Button(self.mid_w, self.play_again_button.rect_image.centery + self.y_offset, self.main_menu_image, self.scale, self.main_menu_hover_image)

        self.quit_image = pygame.image.load(f'{self.button_img_loc}/quit_button.png').convert_alpha()
        self.quit_hover_image = pygame.image.load(f'{self.button_img_loc}/quit_button_hover.png').convert_alpha()
        self.quit_button = Button(self.mid_w, self.main_menu_button.rect_image.centery + self.y_offset, self.quit_image, self.scale, self.quit_hover_image)

    def import_win_lose_menu_button(self):
        self.play_again_button.draw()
        self.main_menu_button.draw()
        self.quit_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.play_again_button.is_clicked2():
            Button.game.win_state = ''
            # Button.game.curr_menu = Button.game.max_points_menu
            Button.game.playing = True
            Button.game.playing2 = True
            self.win_lose_menu.run_display = False
            Button.game.curr_menu = None
        elif self.main_menu_button.is_clicked2():
            self.win_lose_menu.run_display = False
            Button.game.curr_menu = Button.game.main_menu

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


class ImportPauseButton:
    def __init__(self, x, y, scale, game):
        self.game = game
        self.scale = scale
        self.button_img_loc = 'assets/sent_images/button_images'
        self.pause_image = pygame.image.load(f'{self.button_img_loc}/pause_button.png').convert_alpha()
        self.pause_hover_image = pygame.image.load(f'{self.button_img_loc}/pause_button_hover.png').convert_alpha()
        self.pause_button = Button(x, y, self.pause_image, self.scale, self.pause_hover_image)

    def import_pause_button(self):
        self.pause_button.draw()
        self.check_curr_menu()

    def check_curr_menu(self):
        if self.pause_button.is_clicked2():
            self.game.canvas2.blit(self.game.canvas, self.game.canvas2.get_rect()) # Captures the last frame before pausing
            self.game.playing = False
            self.game.curr_menu = Button.game.pause_menu

class ImportPauseMenuButton:
    def __init__(self, pause_menu):
        self.pause_menu = pause_menu
        self.button_img_loc = 'assets/sent_images/button_images'

        self.y_offset = 100

        self.settings_image = pygame.image.load(f'{self.button_img_loc}/settings_button.png').convert_alpha()
        self.settings_hover_image = pygame.image.load(f'{self.button_img_loc}/settings_button_hover.png').convert_alpha()
        self.settings_button = Button(Button.game.mid_w, Button.game.mid_h, self.settings_image, 0.6, self.settings_hover_image)

        self.resume_image = pygame.image.load(f'{self.button_img_loc}/resume_button.png').convert_alpha()
        self.resume_hover_image = pygame.image.load(f'{self.button_img_loc}/resume_button_hover.png').convert_alpha()
        self.resume_button = Button(Button.game.mid_w, self.settings_button.rect_image.centery - self.y_offset, self.resume_image, 0.6, self.resume_hover_image)

        self.quit_image = pygame.image.load(f'{self.button_img_loc}/quit_button.png').convert_alpha()
        self.quit_hover_image = pygame.image.load(f'{self.button_img_loc}/quit_button_hover.png').convert_alpha()
        self.quit_button = Button(Button.game.mid_w, self.settings_button.rect_image.centery + self.y_offset, self.quit_image, 0.6, self.quit_hover_image)



    def import_pause_menu_button(self):
        self.resume_button.draw()
        self.settings_button.draw()
        self.quit_button.draw()

        self.check_curr_menu()

    def check_curr_menu(self):
        if self.resume_button.is_clicked2():
            self.pause_menu.run_display = False
            Button.game.playing = True
        elif self.settings_button.is_clicked2():
            self.pause_menu.run_display = False
            Button.game.curr_menu = Button.game.settings_menu

        elif self.quit_button.is_clicked2():
            self.pause_menu.run_display = False
            Button.game.last_menu = Button.game.pause_menu
            Button.game.curr_menu = Button.game.quit_menu


class ImportQuitMenuButton:
    def __init__(self, quit_menu) -> None:
        self.quit_menu = quit_menu
        self.button_img_loc = 'assets/sent_images/button_images'
        self.mid_w = self.quit_menu.mid_w
        self.y_pos = 450

        self.yes_image = pygame.image.load(f'{self.button_img_loc}/yes_button.png').convert_alpha()
        self.yes_hover_image = pygame.image.load(f'{self.button_img_loc}/yes_button_hover.png').convert_alpha()
        self.yes_button = Button(self.mid_w - 100, self.y_pos, self.yes_image, 1, self.yes_hover_image)

        self.no_image = pygame.image.load(f'{self.button_img_loc}/no_button.png').convert_alpha()
        self.no_hover_image = pygame.image.load(f'{self.button_img_loc}/no_button_hover.png').convert_alpha()
        self.no_button = Button(self.mid_w + 100, self.y_pos, self.no_image, 1, self.no_hover_image)

    def import_quit_menu_button(self):
        self.yes_button.draw()
        self.no_button.draw()

        self.check_curr_menu()

    def check_curr_menu(self):
        if self.yes_button.is_clicked2():
            Button.game.quit_game()
        elif self.no_button.is_clicked2():
            self.quit_menu.run_display = False
            Button.game.curr_menu = Button.game.last_menu




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
