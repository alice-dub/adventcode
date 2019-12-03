input = open("day3.txt", "r")
paths = input.read().splitlines()

paths = [line.split(',') for line in paths]
position_1 = [0, 0, 0]
pos_1 = []
pos_1_p = []
position_2 = [0, 0, 0]
pos_2 = []
dist_intersect = 0
num_steps = 0

def move_on_the_grid(move, position):
    if move[0] == 'L':
        position[0] -= 1
    elif move[0] == 'R':
        position[0] += 1
    elif move[0] == 'U':
        position[1] += 1
    elif move[0] == 'D':
        position[1] -= 1
    else:
        print('Cannot detect position')
    next_num = int(move[1:]) - 1
    next_move = ('{}{}'.format(move[0], next_num))
    return next_move, position

for move_1 in paths[0]:
    while int(move_1[1:]) > 0:
        pos_1.append(list(position_1))
        move_1, position_1 = move_on_the_grid(move_1, position_1)
        position_1[2] += 1

for move_2 in paths[1]:
    while int(move_2[1:]) > 0:
        for position_1 in pos_1:
            if position_2[:-1] == position_1[:-1]:
                position_tot = list(position_2) + [position_1[-1]]
                pos_2.append(list(position_tot))
        move_2, position_2 = move_on_the_grid(move_2, position_2)
        position_2[2] += 1

for element in pos_2:
    if dist_intersect == 0 :
        dist_intersect = abs(element[0]) + abs(element[1])
    elif dist_intersect > abs(element[0]) + abs(element[1]):
        dist_intersect = abs(element[0]) + abs(element[1])
    if num_steps == 0 :
        num_steps = element[2] + element[3]
    elif num_steps > element[2] + element[3]:
        num_steps = element[2] + element[3]

print('The smaller intersection is {} and the smaller number of steps is {}'
    .format(dist_intersect, num_steps))