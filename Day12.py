import copy

file = open("input_day12.txt","r")
#file = open("test.txt","r")
lines = file.readlines()
#print(lines)
moons=[]
for line in lines:
    coord='u'
    readingvalue = False
    val=""
    coordinates = []
    for c in line:
        if(readingvalue):
            if(not((c==',')or(c=='>'))):
                val = val+c
            else:
                coordinates.append(int(val))
                readingvalue=False
                val = ""
        elif c=='x':
            coord='x'
        elif c=='y':
            coord='y'
        elif c=='z':
            coord='z'
        elif c=='=':
            readingvalue = True
    moons.append(coordinates)

    
#append velocity vector
for coordinates in moons:
    coordinates.extend([0,0,0])
#print(moons)

itr=0
foundmatch = True
moons_init = copy.deepcopy(moons)
print(moons_init)
    
while(foundmatch):
    #update velocity
    for i,moon in enumerate(moons):
        for j,coord in enumerate(moons):
            if(moon[0]<coord[0]):
                moon[3]=moon[3]+1
            elif(moon[0]>coord[0]):
                moon[3]=moon[3]-1
            if(moon[1]<coord[1]):
                moon[4]=moon[4]+1
            elif(moon[1]>coord[1]):
                moon[4]=moon[4]-1
            if(moon[2]<coord[2]):
                moon[5]=moon[5]+1
            elif(moon[2]>coord[2]):
                moon[5]=moon[5]-1

    #update position
    for moon in moons:
        moon[0:3] = [moon[i] + moon[3+i] for i in range(3)]
        #moon[3:6] = [0,0,0]
    itr=itr+1
    if(itr%100000==0):
        print(itr)
    if(moons == moons_init):
        foundmatch = False
        print(itr)

#energy
energy = 0
for moon in moons:
    pot = sum([abs(val) for val in moon[0:3]])
    kin = sum([abs(val) for val in moon[3:6]])
    energy = energy + pot*kin

print(energy)
