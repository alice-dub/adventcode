input = open("day2.txt", "r")

program_init = input.read().split(',')
program_init = [int(i) for i in program_init]

def intcode(program):
    for cursor in range(len(program)):
        if cursor % 4 == 0:
            position = program[cursor + 3]
            element1 = program[cursor + 1]
            element2 = program[cursor + 2]
            if program[cursor] == 1:
                program[position] = program[element1] + program[element2]
            elif program[cursor] == 2:
                program[position] = program[element1] * program[element2]
            elif program[cursor] == 99:
                break
            else:
                print('Fake Cursor')
                break
    return(program[0])

# Initializing inputs for the 1st problem : 
program_1 = list(program_init)
program_1[1] = 12
program_1[2] = 2
print('Position 0 is {}'.format(intcode(program_1)))

# Initializing output for the 2nd problem : 
output = 19690720

for noun in range(100):
    for verb in range(100):
        program_2 = list(program_init)
        program_2[1] = noun
        program_2[2] = verb
        if intcode(program_2) == output:
            inputs = 100 * noun + verb
            print('The answer is {}'.format(inputs))
            break 
