from os import name


def python_code_def():
    from random import randint   
    import matplotlib.pyplot as plt
    import time
    import json

    new_or_load = input("New file or load save? (New or 'Your_save_name'): ")

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

    def load(name2):
        try:
            with open(new_or_load + '_' +name2) as f:
                print(f"{new_or_load + '_' + name2} successfully loaded")
                i = json.load(f)
                return i
        except FileNotFoundError:
            print(f"{new_or_load + '_' + name2} doesn`t found")
    if new_or_load.upper() == 'NEW':
        n = int(input('Please, set n: '))
        m = int(input('Please, set m: '))
    if new_or_load.upper() == 'NEW':
        number_bombs = int(input(f'Please, set number of the bombs (< {n*m}): '))
    else:
        number_bombs = int(input(f'Please, set number of the bombs: '))
    number_runs = int(input('Please, set number of runs: '))
    eliminate = input('Eliminate small values? (The score table will be incorrect) (Y or N): ')

    class Pos():
        def __init__(self, place):
            self.place = place
        def pos(self):
            if number_for_points == random_number + self.place and random_number + self.place not in random_number_storage:
                points[random_number + self.place] += 1

    if new_or_load.upper() == 'NEW':
        pass
    else:
        finish_number_storage = load('finish_number_storage')
        finish_scores = load('finish_scores')
        finish_new_stuff = load('finish_new_stuff')
        result_scores = load('result_scores')
        result_scores_2 = load('result_scores_2')
        n = load('n')
        m = load('m')
        finish_score = load('finish_score')
        nop = load('nop')

    right = Pos(1)
    left = Pos(- 1)
    down = Pos(n)
    up = Pos(- n)
    right_down = Pos((n+1))
    left_down = Pos((n-1))
    right_up = Pos(- (n-1))
    left_up = Pos(- (n+1))

    start_time = time.time()


    while again_2 < number_runs:        
        again = 0
        while number <= n*m:
            desk.append(number)
            points[number] = 0
            number += 1
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
            nop = finish_score + 1         
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
        try:
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
        except KeyError:
            if integer not in range(n,n*m,n):
                if integer != n*m+1:
                    if integer not in finish_number_storage:
                        print(f"{result_scores_2[str(integer)]} ", end='')
                    else:
                        print('@ ', end='')
            else:
                    if integer not in finish_number_storage:
                        print(f"{result_scores_2[str(integer)]} ")
                    else:
                        print('@ ')
            integer += 1
    print(f"\nMax score: {sorted(finish_scores)[-1:]}")
    print(not_finish_points_score)
    print(finish_new_stuff)
    print('Time', time.time() - start_time)

    class Save():
        def __init__(self, name, name2):
            self.name = name
            self.name2 = name2
        def save(self):
            with open(save_name + "_" + self.name2, 'w') as f:
                json.dump(self.name, f)
                print(f"Saved as {save_name + '_' + self.name2}")
    
    finish_number_storage_save = Save(finish_number_storage, 'finish_number_storage')
    finish_scores_save = Save(finish_scores, 'finish_scores')
    finish_new_stuff_save = Save(finish_new_stuff, 'finish_new_stuff')
    result_scores_save = Save(result_scores, 'result_scores')
    result_scores_2_save = Save(result_scores_2, 'result_scores_2')
    n_save = Save(n, 'n')
    m_save = Save(m, 'm')
    finish_score_save = Save(finish_score, 'finish_score')
    nop_save = Save(nop, 'nop')

    while True:
        setting = input('(graph, scatter, save, quit): ')
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
            finish_number_storage_save.save()
            finish_scores_save.save()
            finish_new_stuff_save.save()
            result_scores_save.save()
            result_scores_2_save.save()
            n_save.save()
            m_save.save()
            finish_score_save.save()
            nop_save.save()