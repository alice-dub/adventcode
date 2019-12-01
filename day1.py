input = open("day1.txt", "r")
total_1 = 0
total_2 = 0

for line in input:
    fuel = int(line) // 3 - 2
    total_1 += fuel
    while fuel > 0:
        total_2 += fuel
        fuel = int(fuel) // 3 - 2 

print(total_1)
print(total_2)
