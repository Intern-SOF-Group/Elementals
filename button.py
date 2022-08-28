import pygame


class Button:
    def __init__(self, x, y, image, scale, game):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect_image = self.image.get_rect()
        self.rect_image.center = (x, y)
        self.canvas = game.canvas
        self.clicked = True

    def draw(self):
        '''Draws buttons into the canvas'''
        mouse_pos = pygame.mouse.get_pos()
        self.canvas.blit(self.image, (self.rect_image.x, self.rect_image.y ))

        if self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked:
                print('Button Clicked!')
                self.clicked = False
            elif pygame.mouse.get_pressed()[0] == 0 and not self.clicked:
                self.clicked = True


# this class button is specifically for the elements buttons because it needs I/O connection to the game logic
class ElementsButton:
    def __init__(self, x, y, image, scale, game_menu, player_output_str, game_logic):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect_image = self.image.get_rect()
        self.rect_image.center = (x, y)
        self.canvas = game_menu.canvas
        self.clicked = True
        self.player_output_str = player_output_str
        self.player_output = game_logic
        self.clicked_global = game_menu # fixes drag clicking

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.canvas.blit(self.image, (self.rect_image.x, self.rect_image.y ))

        if self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked and self.clicked_global.clicked_global:
                print('Button Clicked!')
                self.player_output.player_move = self.player_output_str
                # print(self.player_output)
                self.clicked = False
                self.clicked_global.clicked_global = False
            elif pygame.mouse.get_pressed()[0] == 0 and not self.clicked and not self.clicked_global.clicked_global:
                self.clicked = True
                self.clicked_global.clicked_global = True
        elif not self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 0 and not self.clicked and not self.clicked_global.clicked_global:
                self.clicked_global.clicked_global = True
                self.clicked = True
