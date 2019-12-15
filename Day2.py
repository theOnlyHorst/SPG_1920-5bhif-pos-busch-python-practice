def runComp (noun,verb):
    F= open("Day2-Inputs.txt","r")
    numbers = []
    line = F.readline()
    arr = line.split(",")
    for it in arr:
        numbers.append(int(it))
    numbers[1]=noun
    numbers[2]=verb
    ptr =0

    while True:
        code = numbers[ptr]
        if code == 1:
            num1 = numbers[numbers[ptr+1]]
            num2 = numbers[numbers[ptr+2]]
            numbers[numbers[ptr+3]] = num1+num2
        elif code == 2:
            num1 = numbers[numbers[ptr+1]]
            num2 = numbers[numbers[ptr+2]]
            numbers[numbers[ptr+3]] = num1*num2
        elif code == 99:
            break
        else:
            print("Error Illegal Opcode")
            break
        ptr+=4

    return numbers[0]
resInNoun=0
resInVerb=0
resOutNum=0
counter =0
loopEnd = False
while counter<100 and loopEnd==False:
    counter2=0
    while counter2<100 and loopEnd==False:
        resOutNum = runComp(counter,counter2)
        if resOutNum==19690720:
            resInNoun=counter
            resInVerb=counter2
            loopEnd=True
        counter2+=1
    counter+=1
print(str(resInNoun)+ ", "+ str(resInVerb))