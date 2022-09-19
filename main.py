import pygame
from data import game_menu

g = game_menu.Game()

while g.running:
    g.game_loop()
    g.curr_menu.display_menu()
