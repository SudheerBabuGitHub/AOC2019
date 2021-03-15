import numpy as np

PYTHON2=False
if(PYTHON2):
    import pygame
    import sys

#file = open("input_day18.txt","r")
file = open("test.txt","r")

lines = file.readlines()
#print(line[0])
grid = []
grid_log = []
keys = {}

X=0
Y=0
for i,line in enumerate(lines):
    row = []
    row_log = []
    for j,c in enumerate(line):
        if(not (c=='\n')):
          row.append(c)
          if(c=='#'):
             row_log.append(0)
          else:
             row_log.append(1)
          if(c>='a' and c<='z'):
              if(keys.get(c)==None):
                  keys.update({c:[i,j]})
        if(c=='@'):
            Y = i
            X = j
            keys.update({c:[i,j]})
    grid.append(row)
    grid_log.append(row_log)
grid_height = i+1
grid_width = j+1

def updateposition(x,y,direction):
    new_x = x
    new_y = y
    if(direction == 1):
        new_y = y-1
    elif(direction == 2):
        new_y = y+1
    elif(direction == 3):
        new_x = x-1
    elif(direction==4):
        new_x = x+1
    else:
        new_x = x
    return(new_x,new_y)

def turnleft(curr_dir):
    new_dir = 1
    if(curr_dir==1):
        new_dir = 3
    elif(curr_dir==2):
        new_dir = 4
    elif(curr_dir==3):
        new_dir=2
    else:
        new_dir=1
    return new_dir

def turnright(curr_dir):
    new_dir = 1
    if(curr_dir==1):
        new_dir = 4
    elif(curr_dir==2):
        new_dir = 3
    elif(curr_dir==3):
        new_dir=1
    else:
        new_dir=2
    return new_dir

def turnback(curr_dir):
    new_dir = 1
    if(curr_dir==1):
        new_dir = 2
    elif(curr_dir==2):
        new_dir = 1
    elif(curr_dir==3):
        new_dir=4
    else:
        new_dir=3
    return new_dir

def traceback(y,x,g,gmap):
    file =  open("output_day18.txt", 'a')
    xi = x
    yi = y
    path = ""+g[yi][xi]+" "
    if(gmap[yi+1][xi]>0):
        yi=yi+1
    elif(gmap[yi][xi+1]>0):
        xi=xi+1
    elif(gmap[yi-1][xi]>0):
        yi=yi-1
    elif(gmap[yi][xi-1]>0):
        xi=xi-1
    path = path+str(int(gmap[yi][xi]))+" "
    if(not g[yi][xi]=='.' and not g[yi][xi]=='@'):
        path = path+g[yi][xi]+" "+str(int(gmap[yi][xi])-1)+" "
    while(not gmap[yi][xi]==1):
        val = gmap[yi][xi]
        if(gmap[yi+1][xi]==val-1):
            yi=yi+1
        elif(gmap[yi][xi+1]==val-1):
            xi=xi+1
        elif(gmap[yi-1][xi]==val-1):
            yi=yi-1
        elif(gmap[yi][xi-1]==val-1):
            xi=xi-1
        if(not g[yi][xi]=='.'):
            path = path+g[yi][xi]+" "+str(int(gmap[yi][xi])-1)+" "
    print(path[::-1])
    file.writelines(path[::-1]+'\n')
    return

SCREEN_SIZE   = 2*640,2*480

# Object dimensions
BRICK_WIDTH   = 5
BRICK_HEIGHT  = 5

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE  = (0,0,255)
BRICK_COLOR = (200,200,0)
WALL_COLOR = (100,100,0)

if(PYTHON2):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    
    screen.fill(BLACK) 

grid_crossover = np.zeros((grid_height,grid_width,4))
grid_path = np.zeros((grid_height,grid_width))

        
#staring pos
x0 = X
y0 = Y

for key, value in keys.items():
    cntr=1
    src_x=value[1]
    src_y=value[0]
    start_x = src_x
    start_y = src_y
    grid_path[start_y][start_x]=cntr        
    curr_x = start_x
    curr_y = start_y
    if(PYTHON2):
        pygame.draw.rect(screen, BLUE, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
        pygame.display.flip()
    direction = 1
    next_ip = 1
    checkbox=1
    numpasses = 0
    while(True):
        if(PYTHON2):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        #clock.tick(50)
        curr_x,curr_y = updateposition(curr_x,curr_y,next_ip)
    
        val = grid[curr_y][curr_x]
        if(not (val=='#' or ((val>='a' and val<='z') and not val==grid[src_y][src_x]))):
            #free
            grid_log[curr_y][curr_x]=0
            if(grid_path[curr_y][curr_x]==0):
                grid_path[curr_y][curr_x] = grid_path[start_y][start_x]+1
            if(PYTHON2):
                pygame.draw.rect(screen, BLUE, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
                pygame.draw.rect(screen, BRICK_COLOR, pygame.Rect(start_x*BRICK_WIDTH+start_x,start_y*BRICK_HEIGHT+start_y,BRICK_WIDTH,BRICK_HEIGHT))
        elif((val>='a' and val<='z') and not val==grid[src_y][src_x]):
            grid_path[curr_y][curr_x] = -1
        else:
            #wall
            if(PYTHON2):
                pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
            curr_x = start_x
            curr_y = start_y
    
        if(not(curr_x==start_x) or not(curr_y==start_y)):
            #back track
            if(next_ip == 1):
                next_ip = 2
            elif(next_ip == 2):
                next_ip = 1
            elif(next_ip == 3):
                next_ip = 4
            elif(next_ip == 4):
                next_ip = 3
        elif(checkbox<4):
            checkbox = checkbox+1
            next_ip = checkbox
            #continue
        elif(checkbox==4):
            checkbox=0
            #update position
            new_direction = turnleft(direction)
            x,y = updateposition(curr_x,curr_y,new_direction)
            if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and (not grid_path[y][x]==0)):
                start_x=x
                start_y = y
                direction=new_direction
                grid_crossover[curr_y][curr_x][new_direction-1]=1
    #                grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
            else:
                x,y = updateposition(curr_x,curr_y,direction)
                if(grid_crossover[curr_y][curr_x][direction-1]==0 and (not grid_path[y][x]==0)):
                    start_x=x
                    start_y = y
                    grid_crossover[curr_y][curr_x][direction-1]=1
    #                    grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
    
                else:
                    new_direction = turnright(direction)
                    x,y = updateposition(curr_x,curr_y,new_direction)
                    if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and  (not grid_path[y][x]==0)):
                        start_x=x
                        start_y = y
                        direction=new_direction
                        grid_crossover[curr_y][curr_x][new_direction-1]=1
    #                        grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
                    else:
                        if(grid[curr_y][curr_x]==grid[src_y][src_x]):
                            numpasses = numpasses+1
                        new_direction = turnback(direction)
                        x,y = updateposition(curr_x,curr_y,new_direction)
                        start_x=x
                        start_y = y
                        direction=new_direction
                        grid_crossover[curr_y][curr_x][new_direction-1]=1
    #                        grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
            #curr_x = start_x
            #curr_y = start_y
            next_ip=direction
    #        iscompleted = True
    #        for i,row in enumerate(grid_nbhd):
    #            for j,col in enumerate(grid_nbhd):
    #                if(grid_log[i][j] < grid_nbhd[i][j]):
    #                    iscompleted = False
    #                    break
    #            if(grid_log[i][j] < grid_nbhd[i][j]):
    #                break
    #        if(iscompleted):
    #            print(grid_path)
    #            break
    #        if(sum(grid_crossover[curr_y][curr_x])>=grid_nbhd[curr_y][curr_x]):
    #            grid_crossover[curr_y][curr_x] = [0,0,0,0]
            #cntr = grid[start_y][start_x]
    #            if(start_x == src_x and start_y == src_y):
    #                grid_crossover = np.zeros((grid_height,grid_width,4))
    #                grid_path = np.zeros((grid_height,grid_width))
    #                break
    #            if(start_x==X and start_y==Y):
    #                grid = np.zeros((100,100))
    #                grid_crossover = np.zeros((100,100,4))
    #                grid[Y][X] = 1
    #                cntr=1
    #                BLUE  = (255,0,0)
    
            #clock.tick(50)
        if(PYTHON2):
            pygame.draw.rect(screen, WHITE, pygame.Rect(x0*BRICK_WIDTH+x0,y0*BRICK_HEIGHT+y0,BRICK_WIDTH,BRICK_HEIGHT))
            pygame.display.flip()
        if(numpasses>1):
            for i,row in enumerate(grid_path):
                for j,col in enumerate(row):
                    if(col==-1):
                        traceback(i,j,grid,grid_path)
            grid_crossover = np.zeros((grid_height,grid_width,4))
            grid_path = np.zeros((grid_height,grid_width))
            break
    #print(keys)
    #print(grid_path)
    
#    for key, value in keys.items():
#        traceback(value[0],value[1],grid,grid_path)
