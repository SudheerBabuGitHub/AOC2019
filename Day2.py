
def intcode(seq,noun,verb):
    seq[1] = noun
    seq[2] = verb
#seq = [1,1,1,4,99,5,6,0,99]
    idx = 0
    endreached = 0
    while(endreached == 0):
        opcode = seq[idx]
        if(opcode == 1):
            #executecode1(seq,idx+1,idx+2,idx+3)
            seq[seq[idx+3]] = seq[seq[idx+1]] + seq[seq[idx+2]]
            idx = idx+4
        elif(opcode == 2):
            #executecode2(seq,idx+1,idx+2,idx+3)
            seq[seq[idx+3]] = seq[seq[idx+1]] * seq[seq[idx+2]]
            idx = idx+4
        elif(opcode == 99):
            endreached = 1
        else:
            endreached = 1
    return seq[0]

param1 = 0
param2 = 0
output = 0
result = 0
while(output == 0):
    file = open("input_day2.txt","r")
    line = file.readlines()
    #print(line[0])
    sequence = [int(val) for val in line[0].split(",")]
    output = intcode(sequence,param1,param2)
    if(output == 19690720):
        result = 100*param1 + param2
    else:
        output = 0
        if(param1<99):
            param2 = param2+1
            if(param2 == 100):
                param2 = 0
                param1 = param1+1
        else:
            output = -1
print(output)
print(result)