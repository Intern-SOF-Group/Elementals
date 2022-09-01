import random

class PlayerObj:
    def __init__(self):
        self.point = 0

    def add_point(self):
        self.point += 1

class GameLogic(PlayerObj):
    def __init__(self, game_menu):
        PlayerObj.__init__(self)
        self.player = PlayerObj()
        self.player_move = ''
        self.CPU = PlayerObj()
        self.moves = ['lightning', 'wind', 'water', 'earth', 'fire']
        self.game_menu = game_menu
        self.cpu_input = self.moves[random.randint(0, 4)]
        self.max_points = 0
        
    def game_IO_loop(self):
        # self.game_menu.draw_text(f'for debugging purposes: {self.cpu_input}', 10, 700, 200)

        if self.player_move:
            if self.player_move == 'lightning':
                if self.cpu_input == 'lightning':
                    print('Tie!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    # self.game_menu.draw_text(str(self.player.point), 10, 100, 200)
                    self.player_move = ''
                elif self.cpu_input == 'wind':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'water':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'earth':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'fire':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''

            elif self.player_move == 'wind':
                if self.cpu_input == 'wind':
                    print('Tie!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'water':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'earth':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'fire':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'lightning':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''

            elif self.player_move == 'water':
                if self.cpu_input == 'water':
                    print('Tie!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'earth':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'fire':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'lightning':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'wind':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''

            elif self.player_move == 'earth':
                if self.cpu_input == 'earth':
                    print('Tie!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'fire':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'lightning':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'wind':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'water':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''

            elif self.player_move == 'fire':
                if self.cpu_input == 'fire':
                    print('Tie!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'lightning':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'wind':
                    self.player.add_point()
                    print('Player wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'water':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
                elif self.cpu_input == 'earth':
                    self.CPU.add_point()
                    print('CPU wins!')
                    print(f'Player points: {self.player.point}')
                    print(f'CPU points: {self.CPU.point}\n')
                    self.player_move = ''
            self.cpu_input = self.moves[random.randint(0, 4)]

        if self.player.point == self.max_points:
            self.game_menu.playing = False
            self.game_menu.curr_menu = None
            self.player.point = 0
            self.CPU.point = 0
        elif self.CPU.point == self.max_points:
            self.game_menu.playing = False
            self.game_menu.curr_menu = None
            self.player.point = 0
            self.CPU.point = 0