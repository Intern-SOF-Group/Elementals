import pygame

class GameSprites(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.sprite_loc = 'assets/sent_images/sprites'
        # Earth sprites
        self.earth_sprite = []
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 1.png'))
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 2.png'))
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 3.png'))
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 4.png'))
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 5.png'))
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 6.png'))
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 7.png'))

        # Fire sprites
        self.fire_sprite = []
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 1.png'))
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 2.png'))
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 3.png'))
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 4.png'))
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 5.png'))
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 6.png'))
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 7.png'))

        # Lightning sprites
        self.lightning_sprite = []
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 1.png'))
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 2.png'))
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 3.png'))
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 4.png'))
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 5.png'))
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 6.png'))
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 7.png'))

        # Water sprites
        self.water_sprite = []
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 1.png'))
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 2.png'))
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 3.png'))
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 4.png'))
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 5.png'))
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 6.png'))
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 7.png'))
        # Wind sprites
        self.wind_sprite = []
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 1.png'))
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 2.png'))
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 3.png'))
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 4.png'))
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 5.png'))
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 6.png'))
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 7.png'))


        self.turn = ''
        self.curr_element = self.lightning_sprite
        self.curr_sprite = 0
        self.scale = 1
        self.W = int(self.curr_element[int(self.curr_sprite)].get_width()*self.scale)
        self.H = int(self.curr_element[int(self.curr_sprite)].get_height()*self.scale)
        self.image = pygame.transform.scale(self.curr_element[int(self.curr_sprite)], (self.W, self.H))
        
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.display_sprites = False


    def update(self):
        self.check_turn()
        self.curr_sprite += 0.2

        if self.curr_sprite >= len(self.curr_element):
            self.curr_sprite = 0
        self.image = pygame.transform.scale(self.curr_element[int(self.curr_sprite)], (self.W, self.H))



    def check_turn(self):
        if self.turn == 'earth':
            self.curr_element = self.earth_sprite
        elif self.turn == 'fire':
            self.curr_element = self.fire_sprite
        elif self.turn == 'lightning':
            self.curr_element = self.lightning_sprite
        elif self.turn == 'water':
            self.curr_element = self.water_sprite
        elif self.turn == 'wind':
            self.curr_element = self.wind_sprite


class ScrollSprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        