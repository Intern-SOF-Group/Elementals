import pygame
from Elementals.data import game_menu

g = game_menu.Game()

pygame.mixer.music.load('assets/audio_files/bg1_music.mp3')
pygame.mixer.music.play(loops=-1, fade_ms=2000)


while g.running:
    g.game_loop()
    g.curr_menu.display_menu()
