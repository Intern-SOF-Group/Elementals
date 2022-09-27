import pygame

class GameSprites(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.sprite_loc = 'assets/sent_images/sprites'
        # Earth sprites
        self.earth_sprite = []
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 1.png').convert_alpha())
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 2.png').convert_alpha())
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 3.png').convert_alpha())
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 4.png').convert_alpha())
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 5.png').convert_alpha())
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 6.png').convert_alpha())
        self.earth_sprite.append(pygame.image.load(f'{self.sprite_loc}/earth_button_sprite/Earth 7.png').convert_alpha())

        # Fire sprites
        self.fire_sprite = []
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 1.png').convert_alpha())
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 2.png').convert_alpha())
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 3.png').convert_alpha())
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 4.png').convert_alpha())
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 5.png').convert_alpha())
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 6.png').convert_alpha())
        self.fire_sprite.append(pygame.image.load(f'{self.sprite_loc}/fire_button_sprite/Fire 7.png').convert_alpha())

        # Lightning sprites
        self.lightning_sprite = []
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 1.png').convert_alpha())
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 2.png').convert_alpha())
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 3.png').convert_alpha())
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 4.png').convert_alpha())
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 5.png').convert_alpha())
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 6.png').convert_alpha())
        self.lightning_sprite.append(pygame.image.load(f'{self.sprite_loc}/lightning_button_sprite/Lightning 7.png').convert_alpha())

        # Water sprites
        self.water_sprite = []
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 1.png').convert_alpha())
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 2.png').convert_alpha())
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 3.png').convert_alpha())
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 4.png').convert_alpha())
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 5.png').convert_alpha())
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 6.png').convert_alpha())
        self.water_sprite.append(pygame.image.load(f'{self.sprite_loc}/water_button_sprite/Water 7.png').convert_alpha())
        # Wind sprites
        self.wind_sprite = []
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 1.png').convert_alpha())
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 2.png').convert_alpha())
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 3.png').convert_alpha())
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 4.png').convert_alpha())
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 5.png').convert_alpha())
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 6.png').convert_alpha())
        self.wind_sprite.append(pygame.image.load(f'{self.sprite_loc}/wind_button_sprite/Wind 7.png').convert_alpha())


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
    def __init__(self, pos_x):
        super().__init__()
        self.sprite_loc = 'assets/sent_images/sprites/scroll_sprite'

        # Total of 10 sprite images
        self.scroll_sprite = []
        for i in range(1,11):
            self.scroll_sprite.append(pygame.image.load(f'{self.sprite_loc}/Scroll {i}.png'))

        self.curr_sprite = 0
        self.image = self.scroll_sprite[int(self.curr_sprite)]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, 300)
        self.display_sprites = True
        self.is_animation_done = False 

    def update(self):

        if self.display_sprites:
            self.curr_sprite += 0.2
            if int(self.curr_sprite >= 10): 
                self.curr_sprite = 9
                self.display_sprites = False
                self.is_animation_done = True
        self.image = self.scroll_sprite[int(self.curr_sprite)]

    def reset_var(self):
        self.curr_sprite = 0
        self.display_sprites = True
        self.is_animation_done = False
