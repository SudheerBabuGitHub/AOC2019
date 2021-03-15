import math

#part 2
def fuelforfuel( rfuel ):
    if(rfuel < 6):
        return
    else:
        ffuel = int(math.floor(rfuel/3)-2)
        fuel.append(ffuel)
        fuelforfuel(ffuel)
        return

file = open("input_day1.txt","r")
lines = file.readlines()
mass = [[int(val) for val in line.split()] for line in lines]
fuel = []
#print(mass)
for i,m in enumerate(mass):
    temp = int(math.floor(m[0]/3)-2)
    fuel.append(temp)
    fuelforfuel(temp)
print(sum(fuel))