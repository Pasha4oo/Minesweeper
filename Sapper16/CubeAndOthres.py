from random import randint   

random_number = 0
random_number_storage = []
points = {}
number = 1
figure = []


number_of_sides = int(input('Please, set number of sides: '))
number_of_connections = int(input('Please, set number of connections: '))
random_usage = input('Use random? (Y or N): ')
if random_usage.upper() == 'Y':
    count_of_bombs = int(input('Please, set number of bombs: '))
    counts_of_runs = int(input('Please, set number of runs: '))

while number <= number_of_sides:
    figure.append(number)
    points[number] = 0
    number += 1

def random_script():
    count = 0
    while True:
        while count_of_bombs >= count:
            random_number = randint(1, number_of_sides+1)
            if random_number not in random_number_storage:
                random_number_storage.append(random_number)
            else:
                continue
            count += 1
        for n in random_number_storage:
            if range(1 +n, number_of_connections + 1 + n) not in figure:
                for m in range(1, number_of_connections + 1):
                    if n - m not in figure and m not in random_number_storage:
                        points[number_of_sides + (n-m)] += 1
                    if n + m not in figure and m not in random_number_storage:
                        points[0 + (m + n - number_of_sides)] += 1
            for m in range(1, number_of_connections + 1):
                if n - m in figure and m not in random_number_storage:
                    points[n - m] += 1
                if n + m in figure and m not in random_number_storage:
                    points[n + m] += 1
        break
if random_usage == 'Y':
    random_script()

print(points)

for k in range(1, number_of_sides + 1):
    if k in random_number_storage:
        print('@ ', end='')
    else:
        print(f'{points[k]} ', end='')