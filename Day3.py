
#file = open("test.txt","r")
file = open("input_day3.txt","r")
lines = file.readlines()
wire1 = lines[0].split(",")
wire2 = lines[1].split(",")
#wire1 = ["R8","U5","L5","D3"]
#wire2 = ["U7","R6","D4","L4"]
#obtain x and y coordinates
wire1_x = []
xcoord1 = 0
wire1_y = []
ycoord1 = 0
wire2_x = []
xcoord2 = 0
wire2_y = []
ycoord2 = 0
for str in wire1:
    if(str[0] == 'R'):
        xcoord1 = xcoord1+int(str[1:(len(str))])
        wire1_x.append(xcoord1)
        wire1_y.append(ycoord1)
    elif(str[0] == 'L'):
        xcoord1 = xcoord1-int(str[1:(len(str))])
        wire1_x.append(xcoord1)
        wire1_y.append(ycoord1)
    elif(str[0] == 'U'):
        ycoord1 = ycoord1+int(str[1:(len(str))])
        wire1_y.append(ycoord1)
        wire1_x.append(xcoord1)
    elif(str[0] == 'D'):
        ycoord1 = ycoord1-int(str[1:(len(str))])
        wire1_y.append(ycoord1)
        wire1_x.append(xcoord1)
    else:
        #error
        print("error")
for str in wire2:
    if(str[0] == 'R'):
        xcoord2 = xcoord2+int(str[1:(len(str))])
        wire2_x.append(xcoord2)
        wire2_y.append(ycoord2)
    elif(str[0] == 'L'):
        xcoord2 = xcoord2-int(str[1:(len(str))])
        wire2_x.append(xcoord2)
        wire2_y.append(ycoord2)
    elif(str[0] == 'U'):
        ycoord2 = ycoord2+int(str[1:(len(str))])
        wire2_y.append(ycoord2)
        wire2_x.append(xcoord2)
    elif(str[0] == 'D'):
        ycoord2 = ycoord2-int(str[1:(len(str))])
        wire2_y.append(ycoord2)
        wire2_x.append(xcoord2)
    else:
        #error
        print("error")
#print(wire1_x)
#print(wire1_y)
#print(wire2_x)
#print(wire2_y)
#find intersection points
x_segment1 = 0
distance = 1000000000000000000000000000000000000000000000
len1 = abs(wire1_x[0]+wire1_y[0])
#len2 = abs(wire2_x[0]+wire2_y[0])
hops = []
for i,x1 in enumerate(wire1_x):
    if(i<len(wire1_x)-1):
        if(wire1_x[i] == wire1_x[i+1]):
            x_segment1 = 1
            len1 = len1+abs(wire1_y[i+1]-wire1_y[i])
            #print(len1)
        else:
            x_segment1 = 0
            len1 = len1+abs(wire1_x[i+1]-wire1_x[i])
            #print(len1)
        len2 = abs(wire2_x[0]+wire2_y[0])
        for j,y2 in enumerate(wire2_y):
            if((x_segment1==1) and (j<len(wire2_y)-1)):
                if((wire2_y[j] == wire2_y[j+1])):
                    len2 = len2+abs(wire2_x[j+1]-wire2_x[j])
                    if((((x1 - wire2_x[j])*(x1 - wire2_x[j+1]))<0) and ((y2 - wire1_y[i])*(y2 - wire1_y[i+1]))<=0):
                        temp1 = len1
                        temp2 = len2
                        len1 = len1-abs(wire1_y[i+1]-wire1_y[i])+abs(y2-wire1_y[i])
                        len2 = len2-abs(wire2_x[j+1]-wire2_x[j])+abs(x1-wire2_x[j])
                        #print(len1,len2,len1+len2)
                        hops.append(len1+len2)
                        len1 = temp1
                        len2 = temp2
                        if((abs(x1)+abs(y2))<distance):
                            distance = abs(x1)+abs(y2)
                    #print("   ",len2)
                elif((wire2_x[j] == wire2_x[j+1])):
                    len2 = len2+abs(wire2_y[j+1]-wire2_y[j])
                    #print("   ",len2)
            elif((x_segment1==0) and (j<len(wire2_y)-1)):
                if((wire2_x[j] == wire2_x[j+1])):
                    len2 = len2+abs(wire2_y[j+1]-wire2_y[j])
                    if((((wire1_y[i] - wire2_y[j])*(wire1_y[i] - wire2_y[j+1]))<0) and ((wire2_x[j] - x1)*(wire2_x[j] - wire1_x[i+1]))<=0):
                        temp1 = len1
                        temp2 = len2
                        len1 = len1-abs(wire1_x[i+1]-wire1_x[i])+abs(wire2_x[j]-wire1_x[i])
                        len2 = len2-abs(wire2_y[j+1]-wire2_y[j])+abs(wire1_y[i]-wire2_y[j])
                        #print(len1,len2,len1+len2)
                        hops.append(len1+len2)
                        len1 = temp1
                        len2 = temp2
                        if((abs(wire2_x[j])+abs(wire1_y[i]))<distance):
                            distance = abs(wire2_x[j])+abs(wire1_y[i])
                    #print("   ",len2)
                elif((wire2_y[j] == wire2_y[j+1])):
                    len2 = len2+abs(wire2_x[j+1]-wire2_x[j])
                    #print("   ",len2)
print(min(hops))