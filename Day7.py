class Intcode:
    def __init__(self, seq):
        self.sequence = seq
        self.input_val = 0
        self.output_val = 0
        self.wait = True
        self.completed = False
        self.pc = 0
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
                if(self.wait):
                    endreached = 1
                    continue
                input_val = self.input_val
                if(param1 == '0'):
                    seq[seq[idx+1]] = input_val
                else:
                    seq[idx+1] = input_val
                idx = idx+2
                self.wait = True
            elif((opcode == '04')or(opcode == '4')):
                if(param1 == '0'):
                    output_val = seq[seq[idx+1]]
                else:
                    output_val = seq[idx+1]
                #print(output_val)
                self.output_val = output_val
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
                self.completed = True
            else:
                endreached = 1
                self.completed = True
        #return seq[0]
        self.pc = idx
        return

file = open("input_day7.txt","r")
#file = open("test.txt","r")
line = file.readlines()
#print(line[0])
thrusterpower = 0
optphase = 0
#phase = 1233
phase = 56788
while phase<98765:
    phase = phase+1
    phase_str = str(phase)
    if(len(phase_str)==4):
        phase_str = '0'+phase_str
    sorted_value = ""
    sorted_value = sorted_value.join(sorted(phase_str))
    vectorfound = True
    for i,s in enumerate(sorted_value):
        if sorted_value[i] < '5':
            vectorfound = False
            break;
        elif i>=(len(sorted_value)-1):
            continue
        elif sorted_value[i]==sorted_value[i+1]:
            vectorfound = False
            break
    if(vectorfound==False):
        continue
    #print(phase)
    phasevector = [0,0,0,0,0]
    for i,s in enumerate(phasevector):
       phasevector[i] = int(phase_str[i]) 
    
    output_val = 0
    
    sequenceA = [int(val) for val in line[0].split(",")]
    ampA = Intcode(sequenceA)
    sequenceB = [int(val) for val in line[0].split(",")]
    ampB = Intcode(sequenceB)
    sequenceC = [int(val) for val in line[0].split(",")]
    ampC = Intcode(sequenceC)
    sequenceD = [int(val) for val in line[0].split(",")]
    ampD = Intcode(sequenceD)
    sequenceE = [int(val) for val in line[0].split(",")]
    ampE = Intcode(sequenceE)

    ampA.execute()
    ampA.input_val = phasevector[0]
    ampA.wait = False
    ampA.execute()
    ampA.input_val = output_val
    ampA.wait = False
    ampA.execute()
    output_val = ampA.output_val 

    ampB.execute()
    ampB.input_val = phasevector[1]
    ampB.wait = False
    ampB.execute()
    ampB.input_val = output_val
    ampB.wait = False
    ampB.execute()
    output_val = ampB.output_val 
    
    ampC.execute()
    ampC.input_val = phasevector[2]
    ampC.wait = False
    ampC.execute()
    ampC.input_val = output_val
    ampC.wait = False
    ampC.execute()
    output_val = ampC.output_val 
    
    ampD.execute()
    ampD.input_val = phasevector[3]
    ampD.wait = False
    ampD.execute()
    ampD.input_val = output_val
    ampD.wait = False
    ampD.execute()
    output_val = ampD.output_val 
    
    ampE.execute()
    ampE.input_val = phasevector[4]
    ampE.wait = False
    ampE.execute()
    ampE.input_val = output_val
    ampE.wait = False
    ampE.execute()
    output_val = ampE.output_val
    
    inprogress = True
    while(inprogress):
        if(ampA.completed == False):
            ampA.input_val = output_val
            ampA.wait = False
            ampA.execute()
            output_val = ampA.output_val
        if(ampB.completed == False):
            ampB.input_val = output_val
            ampB.wait = False
            ampB.execute()
            output_val = ampB.output_val
        if(ampC.completed == False):
            ampC.input_val = output_val
            ampC.wait = False
            ampC.execute()
            output_val = ampC.output_val
        if(ampD.completed == False):
            ampD.input_val = output_val
            ampD.wait = False
            ampD.execute()
            output_val = ampD.output_val
        if(ampE.completed == False):
            ampE.input_val = output_val
            ampE.wait = False
            ampE.execute()
            output_val = ampE.output_val
        if(((ampA.completed and ampB.completed)and(ampC.completed and ampD.completed))and(ampE.completed)):
            inprogress = False
  
    if(output_val>thrusterpower):
        thrusterpower = output_val
        optphase = phase
print(thrusterpower)
print(optphase)