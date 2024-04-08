#17
from random import randint   
import matplotlib.pyplot as plt
import time
import RSapper
import Presets
import PythonCode

def menu():
    mode = ''
    calc_mode = ''

    print("\n██╗░░██╗██╗  ████████╗██╗░░██╗███████╗██████╗░███████╗\n██║░░██║██║  ╚══██╔══╝██║░░██║██╔════╝██╔══██╗██╔════╝\n███████║██║  ░░░██║░░░███████║█████╗░░██████╔╝█████╗░░\n██╔══██║██║  ░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██╔══╝░░\n██║░░██║██║  ░░░██║░░░██║░░██║███████╗██║░░██║███████╗\n╚═╝░░╚═╝╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝")
    print("""
█████████████████████████████████████████████████████████████████████████
█▄─▀█▀─▄█▄─▄█▄─▀█▄─▄█▄─▄▄─█─▄▄▄▄█▄─█▀▀▀█─▄█▄─▄▄─█▄─▄▄─█▄─▄▄─█▄─▄▄─█▄─▄▄▀█
██─█▄█─███─███─█▄▀─███─▄█▀█▄▄▄▄─██─█─█─█─███─▄█▀██─▄█▀██─▄▄▄██─▄█▀██─▄─▄█
▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀
""")
    print("\n█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   █▀█ ▄▀█ █▀ █░█ ▄▀█ █░█ █▀█ █▀█\n█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▀▀ █▀█ ▄█ █▀█ █▀█ ▀▀█ █▄█ █▄█")

def stat():
    version = input('Use Cython? (Much faster, but experimental) (Y or N): ')

    if version.upper() == 'N':
        print('Used Python')
        PythonCode.python_code_def()
    elif version.upper() == 'Y':
        print('Used Cython')
        import Sapper145
    else:
        print(f'ERROR: WRONG ANSWER')

def calc():
    calc_mode = input('Sides (s), corners (c) or both (b): ')

    print('Be sure that m >= n')

    n = int(input('Please, set n: '))
    m = int(input('Please, set m: '))

    if calc_mode.upper() == 'B':
        print('Max possible score: ' + f'{(3*n - 2)*(m - 1)}')
    if calc_mode.upper() == 'S':
        print('Max possible score: ' + f'{n*(m - 1)}')
    if calc_mode.upper() == 'C':
        print('Max possible score: ' + f'{(2*n - 2)*(m - 1)}')

menu()

while True:
    print("\nMods:")
    print('1. Play - feel yourself like a real sapper in this small game')
    print('2. Calc - calculate max points from your own size and rules')
    print('3. Stat - analyzes different game options and displays data')
    print('4. Pres - add your preseted mine to stat mode!')
    print('\nWrite "menu" to show this screen again')
    print('\nIf you done, quit by typing "q"')
    mode = input('\nPlease, select mode (play, calc, stat, pres or quit (q)): ')
    if mode.upper() == 'Q':
        break
    if mode.upper() == 'STAT' or mode == '3':
        stat()
    if mode.upper() == 'CALC' or mode == '2':
        calc()
    if mode.upper() == 'PLAY' or mode == '1':
        RSapper.rsapper_def()
    if mode.upper() == 'MENU':
        menu()
    if mode.upper() == 'PRES' or mode == '4':
        Presets.presets_def()








