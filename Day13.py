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

grid = np.zeros((100,100))
curr_pos = [0,0]

file = open("input_day13.txt","r")
#file = open("test.txt","r")
line = file.readlines()
sequence = [int(val) for val in line[0].split(",")]
add_memory = [0]*100000
sequence.extend(add_memory)
sequence[0]=2
output = 0
amp = Intcode(sequence)

file2 = open("paddlemove.txt","r")
lines = file2.readlines()
paddlemove = [int(line.rstrip()) for line in lines]

#print(paddlemove2)
x=0
y=0
block=0
SCREEN_SIZE   = 640,480
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
font = pygame.font.Font(None,30)
cntr=0
clock = pygame.time.Clock()

screen.fill(BLACK)           
#print(cntr)
move = 0
score=0
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #clock.tick(200)
    amp.execute()
    if(amp.state == 2):
        if(amp.output_val==-1):
           amp.execute()
           amp.execute()
           score = amp.output_val
           #font_surface = font.render("SCORE: " + str(score), False, WHITE)
           #screen.blit(font_surface, (500,0))
           #print(score)
        else:
           x=amp.output_val
           amp.execute()
           y=amp.output_val
           amp.execute()
           block=amp.output_val
           #grid[y][x] = block
           
    elif(amp.state == 1):
        
        if(move<len(paddlemove)):
            #clock.tick(80)
            amp.input_val = paddlemove[move]
            move = move+1
        else:
            clock.tick(1)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                amp.input_val = -1
            elif keys[pygame.K_RIGHT]:
                amp.input_val = 1
            else:
                amp.input_val = 0
        amp.waitonip = False
        print(amp.input_val)
    elif(amp.state == 3):
        break;
            #clock.tick(50)
    if(block == 0):
        pygame.draw.rect(screen, BLACK, pygame.Rect(x*BRICK_WIDTH+x,y*BRICK_HEIGHT+y,BRICK_WIDTH,BRICK_HEIGHT))
    elif(block == 1):
        pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(x*BRICK_WIDTH+x,y*BRICK_HEIGHT+y,BRICK_WIDTH,BRICK_HEIGHT))
    elif(block == 2):
        #cntr = cntr+1
        pygame.draw.rect(screen, BRICK_COLOR, pygame.Rect(x*BRICK_WIDTH+x,y*BRICK_HEIGHT+y,BRICK_WIDTH,BRICK_HEIGHT))
    elif(block == 3):
        pygame.draw.rect(screen, WHITE, pygame.Rect(x*BRICK_WIDTH+x,y*BRICK_HEIGHT+y,BRICK_WIDTH,BRICK_HEIGHT))
    else:
        pygame.draw.rect(screen, BLUE, pygame.Rect(x*BRICK_WIDTH+x,y*BRICK_HEIGHT+y,BRICK_WIDTH,BRICK_HEIGHT))
    pygame.display.flip()
#game = Bricka()
#game.run()
#with open("output_day13.txt", 'w') as file:
#    file.writelines(','.join(str(j) for j in i) + '\n' for i in grid)
print("score:",score)