import game_menu
g = game_menu.Game()


while g.running:
    print(g.curr_menu)
    g.curr_menu.display_menu()
    g.game_loop()

