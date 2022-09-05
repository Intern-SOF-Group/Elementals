import game_menu
import pygame
g = game_menu.Game()

music = pygame.mixer.music.load('assets/audio_files/bg1_music.mp3')
pygame.mixer.music.play(loops=-1, fade_ms=2000)


while g.running:
    # print(g.playing)
    # print(g.playing2)
    g.game_loop()
    g.curr_menu.display_menu()
