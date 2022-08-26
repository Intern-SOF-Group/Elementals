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
        mouse_pos = pygame.mouse.get_pos()
        self.canvas.blit(self.image, (self.rect_image.x, self.rect_image.y ))

        if self.rect_image.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked:
                print('Button Clicked!')
                self.clicked = False
            elif pygame.mouse.get_pressed()[0] == 0 and not self.clicked:
                self.clicked = True
