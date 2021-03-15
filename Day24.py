import numpy

file = open("input_day24.txt","r")
#file = open("test.txt","r")
lines = file.readlines()

grid = numpy.zeros((5,5))

for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if(c=='#'):
            grid[i][j]=1
            
def updategrid(grid):
    grid_nbhd = numpy.zeros((5,5))
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if(i>0):
                grid_nbhd[i][j] = grid_nbhd[i][j]+grid[i-1][j]
            if(j>0):
                grid_nbhd[i][j] = grid_nbhd[i][j]+grid[i][j-1]
            if(i<4):
                grid_nbhd[i][j] = grid_nbhd[i][j]+grid[i+1][j]
            if(j<4):
                grid_nbhd[i][j] = grid_nbhd[i][j]+grid[i][j+1]
    grid2 = numpy.zeros((5,5))
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if(col==1 and grid_nbhd[i][j]==1):
                grid2[i][j]=1
            elif(col==0 and (grid_nbhd[i][j]==1 or grid_nbhd[i][j]==2)):
                grid2[i][j]=1
    return grid2

def calcbiodiversity(grid):
    power=0
    biodiversity = 0
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if(grid[i][j]==1):
                biodiversity = biodiversity+pow(2,power)
            power = power+1
    return biodiversity

#itr=0
log=[]
log.append(calcbiodiversity(grid))
foundmatch=True
itr = 0
while(foundmatch):
    grid = updategrid(grid)
    bd = calcbiodiversity(grid)
    for val in log:
        if(val==bd):
            foundmatch = False
            break
    log.append(bd)
    itr = itr+1
    if(itr%100==0):
        print(itr)
print(grid)
print(log[itr])
