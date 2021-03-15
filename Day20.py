import numpy as np

PYTHON2=True
if(PYTHON2):
    import pygame
    import sys

file = open("input_day20.txt","r")
#file = open("test2.txt","r")
lines = file.readlines()
#print(line[0])
grid = []

for i,line in enumerate(lines):
    row = []
    for j,c in enumerate(line):
        if(not (c=='\n')):
          row.append(c)
    grid.append(row)
grid_height = i+1
grid_width = j

#for i,c in enumerate(grid[int(grid_height/2)]):
#    if(i>1):
#        if(not(c=='#' or c=='.')):
#               break
#donut_width = i-2
#print(donut_width)

#map portals
portalA = {}
portalB = {}
order = {}

def getportalname(y,x):
    name=""
    for key, value in portalA.items(): 
         if value == [y,x]: 
             name = key
             break
    if(name == ""):
        for key, value in portalB.items():
            if value == [y,x]:
                name = key
                break
    return name
         
def getportalend(y,x):
    name=""
    for key, value in portalA.items(): 
         if value == [y,x]: 
             name = key
             break 
         
    if(name == ""):
        for key, value in portalB.items():
            if value == [y,x]:
                name = key
                break
        if(portalA.get(name)):
             return portalA.get(name)
        else:
             return None
    else:
        if(portalB.get(name)):
            return portalB.get(name)
        else:
            return None

class Node:
    def __init__(self, name):
        self.name = name
        self.dist = 1000000000
        self.prev = "AA"
        
unvisited = []
visited = []
        
serial_num=0
for i,row in enumerate(grid):
    if(i==grid_height-1):
        break
    for j,col in enumerate(row):
        if(j==grid_width-1):
            break
        name = ""
        if(col>='A' and col<='Z'):
          if(grid[i+1][j]>='A' and grid[i+1][j]<='Z'):
              name=name+col+grid[i+1][j]
              #print(name)
              if(not(i+2==grid_height) and grid[i+2][j]=='.'):
                  #print(i+2,j)
                  if(portalA.get(name)==None):
                      portalA.update({name:[i+2,j]})
                  else:
                      portalB.update({name:[i+2,j]})
              else:
                  #print(i-1,j)
                  if(portalA.get(name)==None):
                      portalA.update({name:[i-1,j]})
                  else:
                      portalB.update({name:[i-1,j]})
              if(order.get(name)==None):
                  order.update({name:serial_num})
                  serial_num = serial_num+1
                  node = Node(name)
                  unvisited.append(node)
          elif(grid[i][j+1]>='A' and grid[i][j+1]<='Z'):
              name=name+col+grid[i][j+1]
              #print(name)
              if(not(j+2==grid_width) and grid[i][j+2]=='.'):
                  #print(i,j+2)
                  if(portalA.get(name)==None):
                      portalA.update({name:[i,j+2]})
                  else:
                      portalB.update({name:[i,j+2]})
              else:
                  #print(i,j-1)
                  if(portalA.get(name)==None):
                      portalA.update({name:[i,j-1]})
                  else:
                      portalB.update({name:[i,j-1]})
              if(order.get(name)==None):
                  order.update({name:serial_num})
                  serial_num = serial_num+1
                  node = Node(name)
                  unvisited.append(node)
#print(portalA)
#print(portalB)
#print(order)
#print(unvisited)
##############################################################

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
#grid_nbhd = np.zeros((grid_height,grid_width))
#grid_log = np.zeros((grid_height,grid_width))
grid_path = np.zeros((grid_height,grid_width))

#for i,row in enumerate(grid):
#    if(i<2 or i>grid_height-2):
#        continue
#    for j,col in enumerate(row):
#        if(j<2 or j>grid_width-2):
#            continue
#        if(grid[i][j]=='.'):
#            nbhd = 0
#            if(grid[i-1][j]=='.'):
#                nbhd= nbhd+1
#            if(grid[i+1][j]=='.'):
#                nbhd= nbhd+1
#            if(grid[i][j-1]=='.'):
#                nbhd= nbhd+1
#            if(grid[i][j+1]=='.'):
#                nbhd= nbhd+1
#            if(getportalend(i,j)):
#                nbhd= nbhd+1
#            grid_nbhd[i][j]=nbhd
        
#staring pos
[y0,x0] = portalA.get('AA')
#destination
[Y,X] = portalA.get('ZZ')
[start_y,start_x] = portalA.get('AA')
src_x = start_x
src_y = start_y
node = None
for n in unvisited:
    if(n.name == "AA"):
        node = n
        break
node.dist=0
unvisited.remove(node)
visited.append(node)
isportal = False
while(True):
    cntr=1
    grid_path[start_y][start_x]=cntr        
    curr_x = start_x
    curr_y = start_y
    #
    if(PYTHON2):
        pygame.draw.rect(screen, BLUE, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
        pygame.display.flip()
    direction = 1
    next_ip = 1
    checkbox=1
    while(True):
        
        if(PYTHON2):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    #    clock.tick(50)
        #amp.execute()
    #    if(amp.state == 1):
    #        #waiting for input
    #        amp.input_val = next_ip
    #        amp.waitonip = False
        curr_x,curr_y = updateposition(curr_x,curr_y,next_ip)
    #        continue
    #    elif(amp.state == 2):
        #waiting for output
        val = grid[curr_y][curr_x]
        if(val=='.'):
            #free
            if(grid_path[curr_y][curr_x]==0):
                grid_path[curr_y][curr_x] = grid_path[start_y][start_x]+1
            if(PYTHON2):
                pygame.draw.rect(screen, BLUE, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
                pygame.draw.rect(screen, BRICK_COLOR, pygame.Rect(start_x*BRICK_WIDTH+start_x,start_y*BRICK_HEIGHT+start_y,BRICK_WIDTH,BRICK_HEIGHT))
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
            if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and grid[y][x]=='.'):
                start_x=x
                start_y = y
                direction=new_direction
                grid_crossover[curr_y][curr_x][new_direction-1]=1
#                grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
#            elif(grid_crossover[curr_y][curr_x][new_direction-1]==0 and (not([curr_y,curr_x] == [y0,x0] or [curr_y,curr_x] == [Y,X]) and not(grid[y][x]=='#'))):
#                 [y,x] = getportalend(curr_y,curr_x)
#                 if(grid_path[y][x]==0):
#                     grid_path[y][x] = grid_path[curr_y][curr_x]+1
#                 start_x=x
#                 start_y=y
#                 direction=new_direction
#                 grid_crossover[curr_y][curr_x][new_direction-1]=1
    #             grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
            else:
                if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and (not([curr_y,curr_x] == [y0,x0]) and not(grid[y][x]=='#'))):
                   new_node = None
                   for n in unvisited:
                       if(n.name == getportalname(curr_y,curr_x)):
                           new_node = n
                   if(new_node):
                       if(grid_path[curr_y][curr_x]+node.dist<new_node.dist):
                           new_node.dist = grid_path[curr_y][curr_x]+node.dist
                           new_node.prev = node.name
                x,y = updateposition(curr_x,curr_y,direction)
                if(grid_crossover[curr_y][curr_x][direction-1]==0 and grid[y][x]=='.'):
                    start_x=x
                    start_y = y
                    grid_crossover[curr_y][curr_x][direction-1]=1
#                    grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
    #            elif(grid_crossover[curr_y][curr_x][direction-1]==0 and (not([curr_y,curr_x] == [y0,x0] or [curr_y,curr_x] == [Y,X]) and not(grid[y][x]=='#'))):
    #                 [y,x] = getportalend(curr_y,curr_x)
    #                 if(grid_path[y][x]==0):
    #                     grid_path[y][x] = grid_path[curr_y][curr_x]+1
    #                 start_x=x
    #                 start_y = y
    #                 direction=direction
    #                 grid_crossover[curr_y][curr_x][direction-1]=1
    #                 grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
                else:
                    if(grid_crossover[curr_y][curr_x][direction-1]==0 and (not([curr_y,curr_x] == [y0,x0]) and not(grid[y][x]=='#'))):
                       new_node = None
                       for n in unvisited:
                           if(n.name == getportalname(curr_y,curr_x)):
                               new_node = n
                       if(new_node):
                           if(grid_path[curr_y][curr_x]+node.dist<new_node.dist):
                               new_node.dist = grid_path[curr_y][curr_x]+node.dist
                               new_node.prev = node.name
                    new_direction = turnright(direction)
                    x,y = updateposition(curr_x,curr_y,new_direction)
                    if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and grid[y][x]=='.'):
                        start_x=x
                        start_y = y
                        direction=new_direction
                        grid_crossover[curr_y][curr_x][new_direction-1]=1
#                        grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
    #                elif(grid_crossover[curr_y][curr_x][new_direction-1]==0 and (not([curr_y,curr_x] == [y0,x0] or [curr_y,curr_x] == [Y,X]) and not(grid[y][x]=='#'))):
    #                     [y,x] = getportalend(curr_y,curr_x)
    #                     if(grid_path[y][x]==0):
    #                         grid_path[y][x] = grid_path[curr_y][curr_x]+1
    #                     start_x=x
    #                     start_y = y
    #                     direction=new_direction
    #                     grid_crossover[curr_y][curr_x][new_direction-1]=1
    #                     grid_log[curr_y][curr_x] = grid_log[curr_y][curr_x]+1
                    else:
                        if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and (not([curr_y,curr_x] == [y0,x0]) and not(grid[y][x]=='#'))):
                           new_node = None
                           for n in unvisited:
                               if(n.name == getportalname(curr_y,curr_x)):
                                   new_node = n
                           if(new_node):
                               if(grid_path[curr_y][curr_x]+node.dist<new_node.dist):
                                   new_node.dist = grid_path[curr_y][curr_x]+node.dist
                                   new_node.prev = node.name
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
            if(start_x == src_x and start_y == src_y):
                grid_crossover = np.zeros((grid_height,grid_width,4))
                if(isportal):
                    [start_y,start_x] = getportalend(start_y,start_x)
                    src_y = start_y
                    src_x = start_x
                    isportal = False
                    break
                else:
                    min_dist = 1000000
                    idx = 0
                    for i,n in enumerate(unvisited):
                        if(n.dist<min_dist):
                           min_dist = n.dist
                           idx = i
                    node = unvisited[idx]
                    unvisited.remove(node)
                    visited.append(node)
                    [start_y,start_x] = portalA.get(node.name)
                    src_y = start_y
                    src_x = start_x
                    if(not node.name == "ZZ"):
                        isportal = True
                    grid_path = np.zeros((grid_height,grid_width))
                    break
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
    if(node.name == "ZZ"):
        print(node.dist,node.prev)
        break

