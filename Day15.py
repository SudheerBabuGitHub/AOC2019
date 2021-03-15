import numpy as np
import pygame
import sys

class Intcode:
    def __init__(self, seq):
        self.sequence = seq
        self.input_val = 0
        self.output_val = 0
        self.waitonip = True
        self.waitonop = True
        self.state = 0
		#0-init
		#1-waiting on imput
		#2-waiting on output
		#3-completed
        self.pc = 0
        self.relative_base = 0
    def execute(self):
        #seq[1] = noun
        #seq[2] = verb
        #seq = [3,9,8,9,10,9,4,9,99,-1,8]
        seq = self.sequence
        idx = self.pc
        endreached = 0
        while(endreached == 0):
            opcode_str = str(seq[idx])
            param1 = '0'
            param2 = '0'
            param3 = '0'
            if(len(opcode_str)==5):
                param3=opcode_str[0]
                param2=opcode_str[1]
                param1=opcode_str[2]
                opcode = opcode_str[3:5]
            elif(len(opcode_str)==4):
                #param3=opcode_str[3]
                param2=opcode_str[0]
                param1=opcode_str[1]
                opcode = opcode_str[2:4]
            elif(len(opcode_str)==3):
                #param3=0
                #param2=opcode_str[2]
                param1=opcode_str[0]
                opcode = opcode_str[1:3]
            elif(len(opcode_str)==2):
                #param3=0
                #param2=0
                opcode = opcode_str[0:2]
            else:
                #param3=0
                #param2=0
                #param1=0
                opcode = opcode_str[0]
            if((opcode == '01')or(opcode == '1')):
                #executecode1(seq,idx+1,idx+2,idx+3)
                if(param1 == '0'):
                    arg1 = seq[seq[idx+1]]
                elif(param1 == '2'):
                    arg1 = seq[seq[idx+1]+self.relative_base]
                else:
                    arg1 = seq[idx+1]
                if(param2 == '0'):
                    arg2 = seq[seq[idx+2]]
                elif(param2 == '2'):
                    arg2 = seq[seq[idx+2]+self.relative_base]
                else:
                    arg2 = seq[idx+2]
                res = arg1+arg2
                if(param3 == '0'):
                    seq[seq[idx+3]] = res
                elif(param3 == '2'):
                    seq[seq[idx+3]+self.relative_base] = res
                else:
                    seq[idx+3] = res
                #seq[seq[idx+3]] = seq[seq[idx+1]] + seq[seq[idx+2]]
                idx = idx+4
            elif((opcode == '02')or(opcode == '2')):
                #executecode2(seq,idx+1,idx+2,idx+3)
                if(param1 == '0'):
                    arg1 = seq[seq[idx+1]]
                elif(param1 == '2'):
                    arg1 = seq[seq[idx+1]+self.relative_base]
                else:
                    arg1 = seq[idx+1]
                if(param2 == '0'):
                    arg2 = seq[seq[idx+2]]
                elif(param2 == '2'):
                    arg2 = seq[seq[idx+2]+self.relative_base]
                else:
                    arg2 = seq[idx+2]
                res = arg1*arg2
                if(param3 == '0'):
                    seq[seq[idx+3]] = res
                elif(param3 == '2'):
                    seq[seq[idx+3]+self.relative_base] = res
                else:
                    seq[idx+3] = res
                #seq[seq[idx+3]] = seq[seq[idx+1]] * seq[seq[idx+2]]
                idx = idx+4
            elif((opcode == '03')or(opcode == '3')):
                #seq[seq[idx+1]] = input_val
                if(self.waitonip):
                    endreached = 1
                    self.state = 1
                    continue
                input_val = self.input_val
                if(param1 == '0'):
                    seq[seq[idx+1]] = input_val
                elif(param1 == '2'):
                    seq[seq[idx+1]+self.relative_base] = input_val
                else:
                    seq[idx+1] = input_val
                idx = idx+2
                self.waitonip = True
            elif((opcode == '04')or(opcode == '4')):
                if(param1 == '0'):
                    output_val = seq[seq[idx+1]]
                elif(param1 == '2'):
                    output_val = seq[seq[idx+1]+self.relative_base]
                else:
                    output_val = seq[idx+1]
                #print(output_val)
                self.output_val = output_val
                idx = idx+2
                if(self.waitonop):
                    endreached = 1
                    self.state = 2
                    continue
            elif((opcode == '05')or(opcode == '5')):
                if(param1 == '0'):
                    arg1 = seq[seq[idx+1]]
                elif(param1 == '2'):
                    arg1 = seq[seq[idx+1]+self.relative_base]
                else:
                    arg1 = seq[idx+1]
                if(param2 == '0'):
                    arg2 = seq[seq[idx+2]]
                elif(param2 == '2'):
                    arg2 = seq[seq[idx+2]+self.relative_base]
                else:
                    arg2 = seq[idx+2]
                if(arg1==0):
                    idx = idx+3
                else:
                    idx = arg2
            elif((opcode == '06')or(opcode == '6')):
                if(param1 == '0'):
                    arg1 = seq[seq[idx+1]]
                elif(param1 == '2'):
                    arg1 = seq[seq[idx+1]+self.relative_base]
                else:
                    arg1 = seq[idx+1]
                if(param2 == '0'):
                    arg2 = seq[seq[idx+2]]
                elif(param2 == '2'):
                    arg2 = seq[seq[idx+2]+self.relative_base]
                else:
                    arg2 = seq[idx+2]
                if(arg1==0):
                    idx = arg2
                else:
                    idx = idx+3
            elif((opcode == '07')or(opcode == '7')):
                if(param1 == '0'):
                    arg1 = seq[seq[idx+1]]
                elif(param1 == '2'):
                    arg1 = seq[seq[idx+1]+self.relative_base]
                else:
                    arg1 = seq[idx+1]
                if(param2 == '0'):
                    arg2 = seq[seq[idx+2]]
                elif(param2 == '2'):
                    arg2 = seq[seq[idx+2]+self.relative_base]
                else:
                    arg2 = seq[idx+2]
                if(arg1<arg2):
                    res = 1
                else:
                    res = 0
                if(param3 == '0'):
                    seq[seq[idx+3]] = res
                elif(param3 == '2'):
                    seq[seq[idx+3]+self.relative_base] = res
                else:
                    seq[idx+3] = res
                idx = idx+4
            elif((opcode == '08')or(opcode == '8')):
                if(param1 == '0'):
                    arg1 = seq[seq[idx+1]]
                elif(param1 == '2'):
                    arg1 = seq[seq[idx+1]+self.relative_base]
                else:
                    arg1 = seq[idx+1]
                if(param2 == '0'):
                    arg2 = seq[seq[idx+2]]
                elif(param2 == '2'):
                    arg2 = seq[seq[idx+2]+self.relative_base]
                else:
                    arg2 = seq[idx+2]
                if(arg1==arg2):
                    res = 1
                else:
                    res = 0
                if(param3 == '0'):
                    seq[seq[idx+3]] = res
                elif(param3 == '2'):
                    seq[seq[idx+3]+self.relative_base] = res
                else:
                    seq[idx+3] = res
                idx = idx+4
            elif((opcode == '09')or(opcode == '9')):
                if(param1 == '0'):
                    arg1 = seq[seq[idx+1]]
                elif(param1 == '2'):
                    arg1 = seq[seq[idx+1]+self.relative_base]
                else:
                    arg1 = seq[idx+1]
                self.relative_base = self.relative_base + arg1
                idx = idx+2
            elif(opcode == '99'):
                endreached = 1
                self.state = 3
            else:
                endreached = 1
                self.state = 3
        #return seq[0]
        self.pc = idx
        return
    
#def waitforkeypress():
#    while True:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                sys.exit()
#            if event.type == pygame.KEYDOWN:
#                return pygame.key.get_pressed()

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
BRICK_WIDTH   = 10
BRICK_HEIGHT  = 10

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE  = (0,0,255)
BRICK_COLOR = (200,200,0)
WALL_COLOR = (100,100,0)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

screen.fill(BLACK) 
#pygame.draw.rect(screen, WHITE, pygame.Rect(x0*BRICK_WIDTH+x0,y0*BRICK_HEIGHT+y0,BRICK_WIDTH,BRICK_HEIGHT))


file = open("input_day15.txt","r")
#file = open("test.txt","r")
line = file.readlines()
sequence = [int(val) for val in line[0].split(",")]
add_memory = [0]*100000
sequence.extend(add_memory)
#sequence[0]=2

grid = np.zeros((100,100))
grid_crossover = np.zeros((100,100,4))
#staring pos
x0=35
y0=35
#destination
X=x0
Y=y0

cntr=1
start_x=x0
start_y=y0
grid[start_y][start_x]=cntr        
curr_x = start_x
curr_y = start_y

pygame.draw.rect(screen, BLUE, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
pygame.display.flip()
# 1-North
# 2-South
# 3-West
# 4-East
direction = 1
next_ip = 1
amp = Intcode(sequence)
checkbox=1
while(True):
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #clock.tick(50)
    amp.execute()
    if(amp.state == 1):
        #waiting for input
        amp.input_val = next_ip
        amp.waitonip = False
        curr_x,curr_y = updateposition(curr_x,curr_y,next_ip)
        continue
    elif(amp.state == 2):
        #waiting for output
        val = amp.output_val
        if(val==0):
            #wall
            grid[curr_y][curr_x] = -1
            pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
            curr_x = start_x
            curr_y = start_y
        elif(val==1):
            #free
            if(grid[curr_y][curr_x]==0):
                cntr=cntr+1
                grid[curr_y][curr_x]=cntr
            pygame.draw.rect(screen, BLUE, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
            pygame.draw.rect(screen, BRICK_COLOR, pygame.Rect(start_x*BRICK_WIDTH+start_x,start_y*BRICK_HEIGHT+start_y,BRICK_WIDTH,BRICK_HEIGHT))
        else:
            #destination
            grid[curr_y][curr_x]=cntr
            X = curr_x
            Y = curr_y
            pygame.draw.rect(screen, BLUE, pygame.Rect(curr_x*BRICK_WIDTH+curr_x,curr_y*BRICK_HEIGHT+curr_y,BRICK_WIDTH,BRICK_HEIGHT))
            pygame.draw.rect(screen, BRICK_COLOR, pygame.Rect(start_x*BRICK_WIDTH+start_x,start_y*BRICK_HEIGHT+start_y,BRICK_WIDTH,BRICK_HEIGHT))
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
            if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and grid[y][x]>0):
                start_x=x
                start_y = y
                direction=new_direction
                grid_crossover[curr_y][curr_x][new_direction-1]=1
            else:
                x,y = updateposition(curr_x,curr_y,direction)
                if(grid_crossover[curr_y][curr_x][direction-1]==0 and grid[y][x]>0):
                    start_x=x
                    start_y = y
                    grid_crossover[curr_y][curr_x][direction-1]=1
                else:
                    new_direction = turnright(direction)
                    x,y = updateposition(curr_x,curr_y,new_direction)
                    if(grid_crossover[curr_y][curr_x][new_direction-1]==0 and grid[y][x]>0):
                        start_x=x
                        start_y = y
                        direction=new_direction
                        grid_crossover[curr_y][curr_x][new_direction-1]=1
                    else:
                        new_direction = turnback(direction)
                        x,y = updateposition(curr_x,curr_y,new_direction)
                        start_x=x
                        start_y = y
                        direction=new_direction
                        grid_crossover[curr_y][curr_x][new_direction-1]=1
            #curr_x = start_x
            #curr_y = start_y
            next_ip=direction
            cntr = grid[start_y][start_x]
            if((start_x==X and start_y==Y) and BLUE == (255,0,0)):
                break
            if(start_x==X and start_y==Y):
                grid = np.zeros((100,100))
                grid_crossover = np.zeros((100,100,4))
                grid[Y][X] = 1
                cntr=1
                BLUE  = (255,0,0)

    elif(amp.state == 3):
        break;
            #clock.tick(50)
    pygame.draw.rect(screen, WHITE, pygame.Rect(x0*BRICK_WIDTH+x0,y0*BRICK_HEIGHT+y0,BRICK_WIDTH,BRICK_HEIGHT))
    pygame.draw.rect(screen, WHITE, pygame.Rect(41*BRICK_WIDTH+41,47*BRICK_HEIGHT+47,BRICK_WIDTH,BRICK_HEIGHT))
    pygame.display.flip()
    

print(np.amax(grid))
print(np.argmax(grid))
print(grid[x0][y0])
with open("output_day15.txt", 'w') as file:
    file.writelines(','.join(str(j) for j in i) + '\n' for i in grid)
