import game_menu
# import menu
g = game_menu.Game()

# menu = menu.Menu()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

