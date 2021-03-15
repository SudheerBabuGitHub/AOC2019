import math
from operator import itemgetter
file = open("input_day10.txt","r")
#file = open("test.txt","r")
lines = file.readlines()
#print(line[0])
x = []
y = []
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if(c=="#"):
          y.append(i)
          x.append(j)
LOS=[]
for i,asy in enumerate(y):
    num=0
    slope=[]
    index=[]
    for j,as1x in enumerate(x):
        if(i==j):
            continue
        else:
            if(not(y[i]==y[j])):
                curr_slope = (x[i]-x[j])/(y[i]-y[j])
            else:
                curr_slope = ((x[i]-x[j])/abs(x[i]-x[j]))*100000
            k=0
            while(k<len(slope)):
                if(slope[k]==curr_slope):
                    if(((x[index[k]]-x[i])*(x[j]-x[i]) > 0 ) or ((y[index[k]]-y[i])*(y[j]-y[i]) > 0)):
                        break
                    else:
                        k = k+1
                else:
                    k = k+1
            if(k==len(slope)):
                slope.append(curr_slope)
                index.append(j)
                num = num+1
    LOS.append(num)
x0 = x[LOS.index(max(LOS))]
y0 = y[LOS.index(max(LOS))]
print(x0,y0,max(LOS))

#shift origin
xs = []
ys = []
for i,asx in enumerate(x):
    if(not(i==LOS.index(max(LOS)))):
        xs.append((asx-x0))
        ys.append((y[i]-y0))
    
#segregate into laft and right
xl=[]
yl=[]
xr=[]
yr=[]
for i,asx in enumerate(xs):
    if(asx>=0):
        xr.append(asx)
        yr.append(ys[i])
    else:
        xl.append(asx)
        yl.append(ys[i])
#print(yl,xl)
#print(yr,xr)
#find r and theta
rl = [math.sqrt(asx*asx + yl[i]*yl[i]) for i,asx in enumerate(xl)]
thetal = []
for i,asx in enumerate(xl):
    if(asx==0):
        thetal.append(90)
    else:
        thetal.append(180/math.pi*math.atan(yl[i]/asx))

rr = [math.sqrt(asx*asx + yr[i]*yr[i]) for i,asx in enumerate(xr)]
thetar = []
for i,asx in enumerate(xr):
    if(asx==0):
        if(yr[i]<0):
            thetar.append(-90)
        else:
            thetar.append(90)
    else:
        thetar.append(180/math.pi*math.atan(yr[i]/asx))

rthetal=[]
rthetar = []
#create a 2D list
for i,asr in enumerate(rr):
    rthetar.append([asr,thetar[i]])
for i,asr in enumerate(rl):
    rthetal.append([asr,thetal[i]])
#sort
rthetar.sort(key=itemgetter(1), reverse=False)
rthetal.sort(key=itemgetter(1), reverse=False)
#print(rthetal)
#print(rthetar)
cnt=0
while(cnt<len(x)-1):
    repeat_list = []
    i=0
    while(len(rthetar)>0):
        coord = rthetar[i]
        if(i<len(rthetar)-1):
            if(coord[1]==rthetar[i+1][1]):
                repeat_list.append(coord[0])
                i=i+1
            elif(len(repeat_list)>0):
                repeat_list.append(coord[0])
                idx = len(repeat_list) - repeat_list.index(min(repeat_list))
                idx = idx-1
                cnt = cnt+1
                if(cnt==200):
                    temp1 = rthetar[i-idx][0]
                    temp2 = math.pi/180*rthetar[i-idx][1]
                    print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
                del rthetar[i-idx]
                repeat_list = []
            else:
                cnt = cnt+1
                if(cnt==200):
                    temp1 = rthetar[i-idx][0]
                    temp2 = math.pi/180*rthetar[i-idx][1]
                    print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
                del rthetar[i]
        elif(len(repeat_list)>0):
            repeat_list.append(coord[0])
            idx = len(repeat_list) - repeat_list.index(min(repeat_list))
            idx = idx-1
            cnt = cnt+1
            if(cnt==200):
                temp1 = rthetar[i-idx][0]
                temp2 = math.pi/180*rthetar[i-idx][1]
                print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
            del rthetar[i-idx]
            repeat_list = []
        else:
            cnt = cnt+1
            if(cnt==200):
                temp1 = rthetar[i-idx][0]
                temp2 = math.pi/180*rthetar[i-idx][1]
                print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
            del rthetar[i]
        #print(rthetar)
        if(i==len(rthetar)):
            print("right",cnt)
            break
    repeat_list = []
    i=0
    while(len(rthetal)>0):
        coord = rthetal[i]
        if(i<len(rthetal)-1):
            if(coord[1]==rthetal[i+1][1]):
                repeat_list.append(coord[0])
                i=i+1
            elif(len(repeat_list)>0):
                repeat_list.append(coord[0])
                idx = len(repeat_list) - repeat_list.index(min(repeat_list))
                idx = idx-1
                cnt = cnt+1
                if(cnt==200):
                    temp1 = rthetal[i-idx][0]
                    temp2 = math.pi/180*rthetal[i-idx][1]
                    print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
                del rthetal[i-idx]
                repeat_list = []
            else:
                cnt = cnt+1
                if(cnt==200):
                    temp1 = rthetal[i-idx][0]
                    temp2 = math.pi/180*rthetal[i-idx][1]
                    print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
                del rthetal[i]
        elif(len(repeat_list)>0):
            repeat_list.append(coord[0])
            idx = len(repeat_list) - repeat_list.index(min(repeat_list))
            idx = idx-1
            cnt = cnt+1
            if(cnt==200):
                temp1 = rthetal[i-idx][0]
                temp2 = math.pi/180*rthetal[i-idx][1]
                print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
            del rthetal[i-idx]
            repeat_list = []
        else:
            cnt = cnt+1
            if(cnt==200):
                temp1 = rthetal[i-idx][0]
                temp2 = math.pi/180*rthetal[i-idx][1]
                print(x0-temp1*math.cos(temp2),y0-temp1*math.sin(temp2))
            del rthetal[i]
        #print(rthetal)
        if(i==len(rthetal)):
            print("left",cnt)
            break
