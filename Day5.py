def intcode(seq,input_val):
    #seq[1] = noun
    #seq[2] = verb
    #seq = [3,9,8,9,10,9,4,9,99,-1,8]
    idx = 0
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
        if(len(opcode_str)==4):
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
            else:
                arg1 = seq[idx+1]
            if(param2 == '0'):
                arg2 = seq[seq[idx+2]]
            else:
                arg2 = seq[idx+2]
            res = arg1+arg2
            if(param3 == '0'):
                seq[seq[idx+3]] = res
            else:
                seq[idx+3] = res
            #seq[seq[idx+3]] = seq[seq[idx+1]] + seq[seq[idx+2]]
            idx = idx+4
        elif((opcode == '02')or(opcode == '2')):
            #executecode2(seq,idx+1,idx+2,idx+3)
            if(param1 == '0'):
                arg1 = seq[seq[idx+1]]
            else:
                arg1 = seq[idx+1]
            if(param2 == '0'):
                arg2 = seq[seq[idx+2]]
            else:
                arg2 = seq[idx+2]
            res = arg1*arg2
            if(param3 == '0'):
                seq[seq[idx+3]] = res
            else:
                seq[idx+3] = res
            #seq[seq[idx+3]] = seq[seq[idx+1]] * seq[seq[idx+2]]
            idx = idx+4
        elif((opcode == '03')or(opcode == '3')):
            #seq[seq[idx+1]] = input_val
            if(param1 == '0'):
                seq[seq[idx+3]] = input_val
            else:
                seq[idx+3] = input_val
            idx = idx+2
        elif((opcode == '04')or(opcode == '4')):
            if(param1 == '0'):
                output_val = seq[seq[idx+1]]
            else:
                output_val = seq[idx+1]
            print(output_val)
            idx = idx+2
        elif((opcode == '05')or(opcode == '5')):
            if(param1 == '0'):
                arg1 = seq[seq[idx+1]]
            else:
                arg1 = seq[idx+1]
            if(param2 == '0'):
                arg2 = seq[seq[idx+2]]
            else:
                arg2 = seq[idx+2]
            if(arg1==0):
                idx = idx+3
            else:
                idx = arg2
        elif((opcode == '06')or(opcode == '6')):
            if(param1 == '0'):
                arg1 = seq[seq[idx+1]]
            else:
                arg1 = seq[idx+1]
            if(param2 == '0'):
                arg2 = seq[seq[idx+2]]
            else:
                arg2 = seq[idx+2]
            if(arg1==0):
                idx = arg2
            else:
                idx = idx+3
        elif((opcode == '07')or(opcode == '7')):
            if(param1 == '0'):
                arg1 = seq[seq[idx+1]]
            else:
                arg1 = seq[idx+1]
            if(param2 == '0'):
                arg2 = seq[seq[idx+2]]
            else:
                arg2 = seq[idx+2]
            if(arg1<arg2):
                res = 1
            else:
                res = 0
            if(param3 == '0'):
                seq[seq[idx+3]] = res
            else:
                seq[idx+3] = res
            idx = idx+4
        elif((opcode == '08')or(opcode == '8')):
            if(param1 == '0'):
                arg1 = seq[seq[idx+1]]
            else:
                arg1 = seq[idx+1]
            if(param2 == '0'):
                arg2 = seq[seq[idx+2]]
            else:
                arg2 = seq[idx+2]
            if(arg1==arg2):
                res = 1
            else:
                res = 0
            if(param3 == '0'):
                seq[seq[idx+3]] = res
            else:
                seq[idx+3] = res
            idx = idx+4
        elif(opcode == '99'):
            endreached = 1
        else:
            endreached = 1
    #return seq[0]
    return

file = open("input_day5.txt","r")
#file = open("test.txt","r")
line = file.readlines()
#print(line[0])
sequence = [int(val) for val in line[0].split(",")]
intcode(sequence,5)

