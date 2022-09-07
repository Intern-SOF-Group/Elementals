"""
Play this game in the terminal!
Moves:
lightning
wind
water
earth
fire
"""
import random
import sys


class PlayerObj:
    def __init__(self):
        self.point = 0

    def add_point(self):
        self.point += 1


player1 = PlayerObj()
CPU = PlayerObj()

moves = ['lightning', 'wind', 'water', 'earth', 'fire']

while True:
    cpu_input = moves[random.randint(0, 4)]
    # print(f'CPU move = {cpu_input}') #for debugging
    user_input = input('Enter your move: ').lower()

    if user_input == 'lightning':
        if cpu_input == 'lightning':
            print('Tie!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'wind':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'water':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'earth':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'fire':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')

    elif user_input == 'wind':
        if cpu_input == 'wind':
            print('Tie!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'water':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'earth':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'fire':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'lightning':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')

    elif user_input == 'water':
        if cpu_input == 'water':
            print('Tie!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'earth':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'fire':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'lightning':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'wind':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')

    elif user_input == 'earth':
        if cpu_input == 'earth':
            print('Tie!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'fire':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'lightning':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'wind':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'water':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')

    elif user_input == 'fire':
        if cpu_input == 'fire':
            print('Tie!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'lightning':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'wind':
            player1.add_point()
            print('Player wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'water':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')
        elif cpu_input == 'earth':
            CPU.add_point()
            print('CPU wins!')
            print(f'Player points: {player1.point}')
            print(f'CPU points: {CPU.point}\n')

    elif user_input == 'exit':
        sys.exit()
