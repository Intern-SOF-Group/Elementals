import pygame


class Button:
    game_logic = None
    clicked_global = False
    def __init__(self, x, y, image, scale, game):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect_image = self.image.get_rect()
        self.rect_image.center = (x, y)
        self.canvas = game.canvas
        self.clicked = True
        # self.clicked_global = game # fixes drag clicking


    def draw(self):
        self.canvas.blit(self.image, (self.rect_image.x, self.rect_image.y ))


    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked and self.clicked_global:
                print('Button Clicked!')
                self.clicked = False
                self.clicked_global = False
                return True
            elif pygame.mouse.get_pressed()[0] == 0 and not self.clicked and not self.clicked_global:
                self.clicked = True
                self.clicked_global = True
        elif not self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 0 and not self.clicked and not self.clicked_global:
                self.clicked_global = True
                self.clicked = True


# this class button is specifically for the elements buttons because it needs I/O connection to the game logic
class ElementsButton(Button):
    def __init__(self, x, y, image, scale, game, player_output_str):
        Button.__init__(self, x, y, image, scale, game)
        self.player_output_str = player_output_str
        self.player_output = game.game_logic
        self.clicked_global = game # fixes drag clicking

    def player_input(self):
        if self.is_clicked():
            self.player_output.player_move = self.player_output_str



def import_element_buttons(game, scale):
    element_button_y = 1180/3 + 1

    lightning_image = pygame.image.load('images/lightning_button.png').convert_alpha()
    lightning_button = ElementsButton(0, 0, lightning_image, scale, game, 'lightning')
    lightning_button.rect_image.topleft = (0, element_button_y)

    wind_image = pygame.image.load('images/wind_button.png').convert_alpha()
    wind_button = ElementsButton(0, 0, wind_image, scale, game, 'wind')
    wind_button.rect_image.topleft = (lightning_button.rect_image.topright[0] - 1, element_button_y)

    water_image = pygame.image.load('images/water_button.png').convert_alpha()
    water_button = ElementsButton(0, 0, water_image, scale, game, 'water')
    water_button.rect_image.topleft = (wind_button.rect_image.topright[0], element_button_y)

    earth_image = pygame.image.load('images/earth_button.png').convert_alpha()
    earth_button = ElementsButton(0, 0, earth_image, scale, game, 'earth')
    earth_button.rect_image.topleft = (water_button.rect_image.topright[0], element_button_y)

    fire_image = pygame.image.load('images/fire_button.png').convert_alpha()
    fire_button = ElementsButton(0, 0, fire_image, scale, game, 'fire')
    fire_button.rect_image.topleft = (earth_button.rect_image.topright[0], element_button_y)

    lightning_button.draw()
    lightning_button.player_input()

    wind_button.draw()
    wind_button.player_input()

    water_button.draw()
    water_button.player_input()

    earth_button.draw()
    earth_button.player_input()

    fire_button.draw()
    fire_button.player_input()
