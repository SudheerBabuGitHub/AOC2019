import numpy

def fun1(deck):
    return numpy.flip(deck)

def fun2(deck,N):
    deck2 = numpy.empty(deck.shape)
    if(N>=0):
        deck2[-N::] = deck[0:N]
        deck2[0:(-N)] = deck[N::]
    else:
        N = -N
        deck2[0:N] = deck[-N::]
        deck2[N::] = deck[0:(-N)]
    return deck2

def fun3(deck,N):
    deck2 = -1*numpy.ones(deck.shape)
    temp = numpy.arange(deck.size)
    ind = temp*N
    idx = numpy.take(temp,ind,mode='wrap')
    i=0
    while(i<deck.size):
        k=idx[i]
        if(deck2[k]==-1):
            deck2[k] = deck[i]
        else:
            j=1
            while(j<=N):
                if(deck2[k+j]==-1):
                    deck2[k+j] = deck[i]
                    break
                j=j+1
        i=i+1
    return deck2

file = open("input_day22.txt","r")
#file = open("test3.txt","r")
lines = file.readlines()

deck = numpy.arange(10007)
for line in lines:
    space_cnt = 0
    for c in line:
        if(c==' '):
            space_cnt = space_cnt+1
    if(space_cnt==1):
        #cut
        i=3
        while(not line[-i]==' '):
            i=i+1
        N = int(line[-(i-1):-1])
        deck = fun2(deck,N)
        print("cut",N)
    elif(space_cnt==3):
        if(line[-2]>='0' and line[-2]<='9'):
            #deal with increment
            i=3
            while(not line[-i]==' '):
                i=i+1
            N = int(line[-(i-1):-1])
            deck = fun3(deck,N)
            print("deal with increment",N)
        else:
            #deal
            deck = fun1(deck)
            print("deal")
            
for i,card in enumerate(deck):
    if(card==2019):
        print(i)
        break
