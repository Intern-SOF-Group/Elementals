import game_menu

g = game_menu.Game()

while g.running:
    g.playing = True
    g.game_loop()
