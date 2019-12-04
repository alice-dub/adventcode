puzzle_min = 347312
puzzle_max = 805915
count = 0

for i in range(puzzle_min, puzzle_max+1):
    password = str(i)
    same_digit = False
    def_same_digit = False
    order = True
    for j in range(1,6):
        if int(password[j]) < int(password[j-1]):
            order = False
        if password[j] == password[j-1]:
            same_digit = True
            # For part 2 only    
            if j > 1:
                if password[j] == password[j-2]:
                    same_digit = False
        if password[j] != password[j-1] and same_digit == True:
            def_same_digit = True 

    if def_same_digit == True or same_digit == True:
        if order == True:
            count += 1

print('Part 2 answer is {}'.format(count))


