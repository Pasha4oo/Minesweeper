def presets_def():
    from random import randint   
    import matplotlib.pyplot as plt
    import time
    import json

    desk = []                       
    points = {}
    number = 1
    again = 0
    again_2 = 0
    angle = [1,9,73,81]
    finish_score = 0
    finish_scores = []
    result_scores = [0]
    result_scores_2 = {0}
    integer = 1
    random_number_storage = [100]
    finish_number_storage =[]
    not_finish_points_score = 0
    stuff = 0
    nop = 0
    new_stuff = []
    finish_new_stuff =[0]
    setting = 0
    preset_mines = []
    preset_mine = 0 

    n = int(input('Please, set n: '))                                             
    m = int(input('Please, set m: '))
    number_bombs = int(input(f'Please, set number of the bombs (< {n*m}): '))
    number_runs = int(input('Please, set number of runs: '))
    eliminate = input('Eliminate small values? (The score table will be incorrect) (Y or N): ')

    class Pos():
        def __init__(self, place):
            self.place = place
        def pos(self):
            if number_for_points == random_number + self.place and random_number + self.place not in random_number_storage:
                points[random_number + self.place] += 1

    right = Pos(1)
    left = Pos(- 1)
    down = Pos(n)
    up = Pos(- n)
    right_down = Pos((n+1))
    left_down = Pos((n-1))
    right_up = Pos(- (n-1))
    left_up = Pos(- (n+1))

    start_time = time.time()

    while number <= n*m:
        desk.append(number)
        points[number] = 0
        number += 1

    while True:
        preset_mine = int(input('Please, set COORDS of new preset mine. If you done please type "-1": \n'))
        if preset_mine == -1:
            break
        else:
            if preset_mine not in preset_mines:
                preset_mines.append(preset_mine)
                integer = 1
                while integer <= n*m:
                    if integer not in range(n,n*m,n):
                        if integer not in preset_mines:
                            print(f"{points[integer]} ", end='')
                        else:
                            print('@ ', end='')
                    else:
                        if integer not in preset_mines:
                            print(f"{points[integer]} ")
                        else:
                            print('@ ')
                    integer += 1

    while again_2 < number_runs:        
        again = 0
        while number <= n*m:
            desk.append(number)
            points[number] = 0
            number += 1
        for each_mine in preset_mines:
            random_number_storage.append(each_mine)
        while again < number_bombs:                     
            if sum(finish_new_stuff[0:again]) <= sum(new_stuff[0:again]) and finish_new_stuff and new_stuff or again == 0 or again_2 == 0 or eliminate == 'N':
                random_number_1 = randint(1,n*m)
                random_number = random_number_1
                print(random_number)
                if random_number not in random_number_storage:   
                    points[random_number] = 0                        
                    if random_number not in random_number_storage:    
                        random_number_storage.append(random_number)
                        for number_for_points in desk:               
                            number_for_points = number_for_points
                            random_number = random_number_1
                            if random_number in range(2,n-1):                                                                      
                                left.pos()
                                right.pos()
                                down.pos()
                                right_down.pos()
                                left_down.pos()

                            elif random_number in range(n+1,n*m-(2*n-2),n):                                                         #Левой стороны
                                right.pos()
                                up.pos()
                                down.pos()
                                right_up.pos()
                                right_down.pos()

                            elif random_number in range(n*2,n*m-n+2,n):                                                             #Правой
                                left.pos()
                                up.pos()
                                down.pos()
                                left_down.pos()
                                left_up.pos()

                            elif random_number in range(n*m-n+2,n*m-1):                                                           #И нижней стороны списка
                                left.pos()
                                right.pos()
                                up.pos()
                                right_up.pos()
                                left_up.pos()

                            elif random_number == 1:                                                                                    #А дальше исключения - углы
                                right.pos()
                                down.pos()
                                right_down.pos()

                            elif random_number == n:
                                left.pos()
                                down.pos()
                                left_down.pos()

                            elif random_number == n*m-(n-1):
                                right.pos()
                                up.pos()
                                right_up.pos()

                            elif random_number == n*m:
                                left.pos()
                                up.pos()
                                left_up.pos()

                            else:
                                up.pos()
                                down.pos()
                                right.pos()
                                left.pos()
                                left_down.pos()
                                left_up.pos()
                                right_up.pos()
                                right_down.pos()
                            not_finish_points_score += points.get(number_for_points)
                        new_stuff.append(not_finish_points_score)
                        not_finish_points_score = 0
                        print(random_number)
                    again += 1
                else:             
                    continue
            else:
                break

        finish_score = sum(points.values())      
        if int(finish_score) >= int(nop):      
            nop = 0
            nop = finish_score + 1         #Смотрит: была ли комбинация лучше всех предыдущих? Если так перезаписывает переменные, которые позже будут показываться как лучший результат
            result_scores = desk[:]
            finish_new_stuff = new_stuff[:]
            finish_number_storage = random_number_storage[:]
            result_scores_2 = points.copy()
            print(nop)
            print(finish_score)
        print(desk)
        print(points)
  
        finish_scores.append(finish_score)


        desk = []                               #Обнуление цикла
        number = 1 
        finish_score = 0
        points = {}
        random_number_storage = []
        new_stuff = []
        again_2 += 1


    print(f'Score: {finish_scores}')        #Вывод лучшего значения
    print(result_scores_2)
    print(result_scores)
    integer = 1
    while integer <= n*m:
        if integer not in range(n,n*m,n):
            if integer != n*m+1:
                if integer not in finish_number_storage:
                    print(f"{result_scores_2[integer]} ", end='')
                else:
                    print('@ ', end='')
        else:
                if integer not in finish_number_storage:
                    print(f"{result_scores_2[integer]} ")
                else:
                    print('@ ')
        integer += 1
    print(f"\nMax score: {sorted(finish_scores)[-1:]}")
    print(not_finish_points_score)
    print(finish_new_stuff)
    print('Time', time.time() - start_time)

    while True:
        setting = input('(graph, scatter, save, quit: )')
        if setting.upper() == 'GRAPH':
            plt.xlabel('Move number', fontsize=16)
            plt.ylabel(r'Points', fontsize=16)
            plt.plot(range(len(finish_new_stuff)), finish_new_stuff, '--r',  label=r'First')
            plt.legend(fontsize=16)
            plt.tight_layout()
            plt.show()
            graph = 0
        if setting.upper() == 'SCATTER':
            plt.scatter(range(len(finish_new_stuff)), finish_new_stuff, marker='o', s=1)
            plt.tight_layout()
            plt.show()
            graph = 0
        if setting.upper() == 'QUIT':
            break
        if setting.upper() == 'SAVE':
            save_name = input('Please, set name of your save: ')
            with open(save_name, 'w') as f:
                json.dump(finish_number_storage, f)
                print(f'Saved as {save_name}')




