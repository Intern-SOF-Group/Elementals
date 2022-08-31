import game_menu
g = game_menu.Game()


while g.running:
    # print(g.clicked_global)
    g.curr_menu.display_menu()
    g.game_loop()

