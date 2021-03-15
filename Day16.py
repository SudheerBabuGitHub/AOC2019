import copy

file = open("input_day16.txt","r")
#file = open("test.txt","r")
line = file.readlines()
ip_str = '0'+line[0]
#print(ip_str)
offset = int(ip_str[0:8])
print(offset)

i=0
while(i<999):
    ip_str = ip_str + line[0]
    i=i+1

ip_len = len(ip_str)
#ip_vec = np.array([0])

rep_mat = [0]*(ip_len)
ip_vec = [0]*(ip_len)
op_vec = [0]*(ip_len)

i=0
while(i<ip_len-1):
    l=i+1
    rep_mat = [0]*(ip_len)
    sign=1
    row_sum = 0
    while(l<ip_len):
        j=0
        while(j<(i+1) and l+j<ip_len):
            #k = math.floor(j/(i+1))
            #val = math.sin(k*math.pi/2)
            #rep_mat[j] = int(val)*int(ip_str[j])
            #print(l,sign)
            row_sum = row_sum+sign*int(ip_str[l+j])
            j=j+1
        sign = -sign
        l=l+i+1+j
    print(i)
    i=i+1
    op_vec[i] = int(str(row_sum)[-1])
ip_vec = copy.copy(op_vec)
#rep_mat = np.delete(rep_mat,0,axis=1)
#print(ip_vec)
itr=1
#print(itr)
while(itr<100):
    i=0
    while(i<ip_len-1):
        l=i+1
        rep_mat = [0]*(ip_len)
        sign=1
        row_sum = 0
        while(l<ip_len):
            j=0
            while(j<(i+1) and l+j<ip_len):
                #k = math.floor(j/(i+1))
                #val = math.sin(k*math.pi/2)
                #rep_mat[j] = int(val)*int(ip_str[j])
                #print(l,sign)
                row_sum = row_sum+sign*int(ip_vec[l+j])
                j=j+1
            sign = -sign
            l=l+i+1+j
            #print(i)
        i=i+1
        op_vec[i] = int(str(row_sum)[-1])
    itr=itr+1
    print(itr)
    ip_vec = copy.copy(op_vec)
print(ip_vec[offset-1:offset+9])
#print(ip_vec)
