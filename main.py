import pygame
from data import game_menu

g = game_menu.Game()

bg_music = pygame.mixer.Sound('assets/audio_files/bg1_music.mp3')
bg_music.set_volume(0.4)
bg_music.play(loops=-1, fade_ms=1000)

while g.running:
    g.game_loop()
    g.curr_menu.display_menu()
