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
        self.CPU = PlayerObj()
        self.moves = ['lightning', 'wind', 'water', 'earth', 'fire']
        self.game_menu = game_menu
        self.player_move = ''
        self.cpu_input = ''
        self.max_points = 0
        self.winner_state = ''
        self.game_start = False # This is for checking if to display the rotating sprite or not

    def game_IO_loop(self):
        # self.game_menu.draw_text(f'for debugging purposes: {self.cpu_input}', 10, 700, 200)

        if self.player_move:
            self.game_start = True
            self.cpu_input = self.moves[random.randint(0, 4)]
            if self.player_move == 'lightning':
                if self.cpu_input == 'lightning':
                    # print('Tie!')
                    self.winner_state = 'Tie!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                    # self.game_menu.draw_text(str(self.player.point), 10, 100, 200)                   
                elif self.cpu_input == 'wind':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')                    
                elif self.cpu_input == 'water':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')                    
                elif self.cpu_input == 'earth':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')                    
                elif self.cpu_input == 'fire':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')                    

            elif self.player_move == 'wind':
                if self.cpu_input == 'wind':
                    # print('Tie!')
                    self.winner_state = 'Tie!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')                   
                elif self.cpu_input == 'water':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')                    
                elif self.cpu_input == 'earth':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')                    
                elif self.cpu_input == 'fire':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'lightning':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')

            elif self.player_move == 'water':
                if self.cpu_input == 'water':
                    # print('Tie!')
                    self.winner_state = 'Tie!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'earth':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'fire':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'lightning':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'wind':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')

            elif self.player_move == 'earth':
                if self.cpu_input == 'earth':
                    # print('Tie!')
                    self.winner_state = 'Tie!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'fire':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'lightning':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'wind':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'water':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')

            elif self.player_move == 'fire':
                if self.cpu_input == 'fire':
                    # print('Tie!')
                    self.winner_state = 'Tie!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'lightning':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'wind':
                    self.player.add_point()
                    # print('Player wins!')
                    self.winner_state = 'Player Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'water':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
                elif self.cpu_input == 'earth':
                    self.CPU.add_point()
                    # print('CPU wins!')
                    self.winner_state = 'CPU Wins!'
                    # print(f'Player points: {self.player.point}')
                    # print(f'CPU points: {self.CPU.point}\n')
            
            self.game_menu.player1_input = self.player_move
            self.game_menu.CPU_input = self.cpu_input
            self.player_move = ''
            self.cpu_input = self.moves[random.randint(0, 4)]

        if (self.player.point == self.max_points) or (self.CPU.point == self.max_points):
            if self.player.point == self.max_points:
                self.player.point = 0
                self.CPU.point = 0
                self.game_menu.win_state = 'You Win!'
            elif self.CPU.point == self.max_points:
                self.player.point = 0
                self.CPU.point = 0
                self.game_menu.win_state = 'You Lose!'

            # Resets the important variables after the game finishes
            self.game_start = False
            self.game_menu.player_scroll.reset_var() # Resets the scroll variables so that every restart of the game it unfolds again.
            self.game_menu.CPU_scroll.reset_var()
            self.game_menu.turn_sprite.display_sprites = False
            self.game_menu.CPU_turn_sprite.display_sprites = False
            self.player_move = ''
            self.cpu_input = ''
            self.game_menu.player_input = self.player_move
            self.game_menu.CPU_input = self.cpu_input
            self.winner_state = ''
            self.game_menu.playing = False
            self.game_menu.playing2 = False
            self.game_menu.curr_menu = self.game_menu.win_lose_menu

        self.game_menu.draw_text(self.winner_state, 80, self.game_menu.mid_w, self.game_menu.mid_h, self.game_menu.ancient_font)


class GameLogic2Player:
    def __init__(self, game_menu):
        self.player1 = PlayerObj()
        self.player2 = PlayerObj()
        self.moves = ['lightning', 'wind', 'water', 'earth', 'fire']
        self.game_menu = game_menu
        self.player1_move = ''
        self.player2_move = ''
        self.max_points = 0
        self.winner_state = ''
        self.game_start = False # This is for checking if to display the rotating sprite or not
        self.is_player2_turn = False # this becomes true after player 1 takes a turn

    def game_IO_loop(self):
        if self.player1_move:
            self.is_player2_turn = True
            if self.player2_move:
                if self.player1_move == 'lightning':
                    if self.player2_move == 'lightning':
                        # print('Tie!')
                        self.winner_state = 'Tie!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                        # self.game_menu.draw_text(str(self.player1.point), 10, 100, 200)                   
                    elif self.player2_move == 'wind':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')                    
                    elif self.player2_move == 'water':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')                    
                    elif self.player2_move == 'earth':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')                    
                    elif self.player2_move == 'fire':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')                    

                elif self.player1_move == 'wind':
                    if self.player2_move == 'wind':
                        # print('Tie!')
                        self.winner_state = 'Tie!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')                   
                    elif self.player2_move == 'water':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')                    
                    elif self.player2_move == 'earth':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')                    
                    elif self.player2_move == 'fire':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'lightning':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')

                elif self.player1_move == 'water':
                    if self.player2_move == 'water':
                        # print('Tie!')
                        self.winner_state = 'Tie!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'earth':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'fire':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'lightning':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'wind':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')

                elif self.player1_move == 'earth':
                    if self.player2_move == 'earth':
                        # print('Tie!')
                        self.winner_state = 'Tie!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'fire':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'lightning':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'wind':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'water':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')

                elif self.player1_move == 'fire':
                    if self.player2_move == 'fire':
                        # print('Tie!')
                        self.winner_state = 'Tie!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'lightning':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'wind':
                        self.player1.add_point()
                        # print('Player1 Wins!')
                        self.winner_state = 'Player1 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'water':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
                    elif self.player2_move == 'earth':
                        self.player2.add_point()
                        # print('Player2 Wins!')
                        self.winner_state = 'Player2 Wins!'
                        # print(f'Player points: {self.player1.point}')
                        # print(f'CPU points: {self.CPU.point}\n')
            
                # for displaying sprites
                self.game_menu.player1_input = self.player1_move
                self.game_menu.player2_input = self.player2_move
                self.player1_move = ''
                self.player2_move = ''
                self.is_player2_turn = False

        if (self.player1.point == self.max_points) or (self.player2.point == self.max_points):
            if self.player1.point == self.max_points:
                self.player1.point = 0
                self.player2.point = 0
                self.game_menu.win_state = 'Player 1 Wins!'
            elif self.player2.point == self.max_points:
                self.player1.point = 0
                self.player2.point = 0
                self.game_menu.win_state = 'Player 2 Wins!'

            # Resets the important variables after the game finishes
            self.game_start = False
            self.game_menu.player_scroll.reset_var() # Resets the scroll variables so that every restart of the game it unfolds again.
            self.game_menu.CPU_scroll.reset_var()
            self.game_menu.turn_sprite.display_sprites = False
            self.game_menu.CPU_turn_sprite.display_sprites = False
            self.player1_move = ''
            self.player2_move = ''
            self.game_menu.player_input = self.player1_move
            self.game_menu.CPU_input = self.player2_move
            self.winner_state = ''
            self.game_menu.playing = False
            self.game_menu.playing2 = False
            self.game_menu.curr_menu = self.game_menu.win_lose_menu

        self.game_menu.draw_text(self.winner_state, 80, self.game_menu.mid_w, self.game_menu.mid_h, self.game_menu.ancient_font)
