value = 240920
end_value = 789857
counter = 0
while(value<end_value):
    check1 = False
    check2 = False
    string_value = str(value)
    sorted_value = ""
    sorted_value = sorted_value.join(sorted(string_value))
    if(string_value == sorted_value):
        check1 = True
        #print(value)
        i=0
        while(i<5):
            if(string_value[i]==string_value[i+1]):
                check2 = True
                if((i<4)and(string_value[i+1]==string_value[i+2])):
                    check2 = False
                elif((i>0)and(string_value[i]==string_value[i-1])):
                    check2 = False
                else:
                    break
            i = i+1
    if(check1 and check2):
        #print(value)
        counter = counter+1
    value = value+1
print(counter)