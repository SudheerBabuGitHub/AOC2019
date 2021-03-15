import numpy as np

def findfrequency(img,search_digit):
    freq = []
    for layer in img:
        cnt = 0
        for row in layer:
            for digit in row:
                if(digit == search_digit):
                    cnt = cnt+1
        freq.append(cnt)
    return freq
file = open("input_day8.txt","r")
#file = open("test.txt","r")
lines = file.readlines()
width = int(25)
height = int(6)
num_pixels = len(lines[0])
num_layers = int(num_pixels/(width*height))
image = np.zeros((num_layers,height,width))
#print(lines[0])
row = 0
col = 0
layer = 0
for i,c in enumerate(lines[0]):
    if(not(i==0) and (i%width == 0)):
        row = row+1
        col = 0
    if(not(i==0) and (i%(width*height) == 0)):
        layer = layer+1
        row = 0
    image[layer,row,col] = int(c)
    col = col+1
#print(image)
#freq0 = findfrequency(image,0)
#freq1 = findfrequency(image,1)
#freq2 = findfrequency(image,2)
#idx = freq0.index(min(freq0))
#print(freq1[idx]*freq2[idx])
colour = np.zeros((height,width))
for row,r in enumerate(colour):
    for col,c in enumerate(r):
        for layer,l in enumerate(image):
            if(l[row,col]==2):
                continue
            else:
                colour[row,col] = l[row,col]
                break
print(colour)

with open("output_day8.txt", 'w') as file:
    file.writelines(','.join(str(j) for j in i) + '\n' for i in colour)