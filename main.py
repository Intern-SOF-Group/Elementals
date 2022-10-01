from data import game_menu

g = game_menu.Game()

while g.running:
    g.game_loop()
    print(g.curr_menu)
    print(g.playing, g.playing2)
    g.curr_menu.display_menu()
