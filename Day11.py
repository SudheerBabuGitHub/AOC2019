import numpy as np
import enum

class HEADING(enum.Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Intcode:
    def __init__(self, seq):
        self.sequence = seq
        self.input_val = 0
        self.output_val = 0
        self.waitonip = True
        self.waitonop = True
        self.completed = False
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
                self.completed = True
            else:
                endreached = 1
                self.completed = True
        #return seq[0]
        self.pc = idx
        return

def updateposition(pos,heading,update):
    newpos = pos
    newheading = heading
    if(update==0):
        #turn left
        if(heading == HEADING.UP):
            newheading = HEADING.LEFT
            newpos[1] = newpos[1]-1
        elif(heading == HEADING.LEFT):
            newheading = HEADING.DOWN
            newpos[0] = newpos[0]+1
        elif(heading == HEADING.DOWN):
            newheading = HEADING.RIGHT
            newpos[1] = newpos[1]+1
        else:
            newheading = HEADING.UP
            newpos[0] = newpos[0]-1
    else:
        #turn right
        if(heading == HEADING.UP):
            newheading = HEADING.RIGHT
            newpos[1] = newpos[1]+1
        elif(heading == HEADING.RIGHT):
            newheading = HEADING.DOWN
            newpos[0] = newpos[0]+1
        elif(heading == HEADING.DOWN):
            newheading = HEADING.LEFT
            newpos[1] = newpos[1]-1
        else:
            newheading = HEADING.UP
            newpos[0] = newpos[0]-1
    return(newpos,newheading)

grid = np.zeros((100,100))
repaint = np.zeros((100,100))
curr_pos = [50,50]
facing = HEADING.UP

file = open("input_day11.txt","r")
#file = open("test.txt","r")
line = file.readlines()
sequence = [int(val) for val in line[0].split(",")]
add_memory = [0]*100000
sequence.extend(add_memory)

output = 0
amp = Intcode(sequence)
amp.execute()
grid[int(curr_pos[0])][int(curr_pos[1])] = 1
while(True):
    amp.input_val = int(grid[int(curr_pos[0])][int(curr_pos[1])])
    amp.waitonip = False
    amp.execute()
    output = amp.output_val
    grid[curr_pos[0]][curr_pos[1]] = output
    repaint[curr_pos[0]][curr_pos[1]] = 1
    amp.execute()
    output = amp.output_val
    curr_pos,facing = updateposition(curr_pos,facing,output)
    amp.execute()
    
    if(amp.completed):
        break
total = 0
for row in repaint:
    total = total+sum(row)
print(total)
with open("output_day11.txt", 'w') as file:
    file.writelines(','.join(str(j) for j in i) + '\n' for i in grid)
