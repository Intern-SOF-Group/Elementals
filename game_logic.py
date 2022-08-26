# import pygame
import random

class PlayerObj:
    def __init__(self):
        self.point = 0

    def add_point(self):
        self.point += 1


class GameLogic(PlayerObj):
    def __init__(self):
        PlayerObj.__init__(self)
        self.player = PlayerObj()
        self.player_move = ''
        self.CPU = PlayerObj()
        self.moves = ['lightning', 'wind', 'water', 'earth', 'fire']

    def game_IO_loop(self):
        cpu_input = self.moves[random.randint(0, 4)]

        if self.player_move == 'lightning':
            if cpu_input == 'lightning':
                print('Tie!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'wind':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'water':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'earth':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'fire':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''

        elif self.player_move == 'wind':
            if cpu_input == 'wind':
                print('Tie!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'water':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'earth':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'fire':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'lightning':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''

        elif self.player_move == 'water':
            if cpu_input == 'water':
                print('Tie!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'earth':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'fire':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'lightning':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'wind':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''

        elif self.player_move == 'earth':
            if cpu_input == 'earth':
                print('Tie!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'fire':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'lightning':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'wind':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'water':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''

        elif self.player_move == 'fire':
            if cpu_input == 'fire':
                print('Tie!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'lightning':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'wind':
                self.player.add_point()
                print('Player wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'water':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
            elif cpu_input == 'earth':
                self.CPU.add_point()
                print('CPU wins!')
                print(f'Player points: {self.player.point}')
                print(f'CPU points: {self.CPU.point}\n')
                self.player_move = ''
