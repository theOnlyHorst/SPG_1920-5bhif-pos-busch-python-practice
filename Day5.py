
def runComp():
    F= open("Day5-Inputs.txt","r")
    numbers = []
    line = F.readline()
    arr = line.split(",")
    for it in arr:
        numbers.append(int(it))
    ptr =0

    while True:
        instruction = int(numbers[ptr])
        code = instruction%100
        instruction/=100
        parmMode1 = int(instruction%10)
        instruction/=10
        parmMode2=int(instruction%10)
        instruction/=10
        parmMode3 = int(instruction%10)

        print("Instruct: "+ str(code))
        if code == 1:
            num1=0
            num2=0
            if parmMode1==1:
                num1=numbers[ptr+1]
            else:
                num1 = numbers[numbers[ptr+1]]
            if parmMode2==1:
                num2=numbers[ptr+2]
            else:
                num2 = numbers[numbers[ptr+2]]
            if parmMode3==1:
                numbers[ptr+3]=num1+num2
            else:
                numbers[numbers[ptr+3]]=num1+num2
            ptr+=4
        elif code == 2:
            num1=0
            num2=0
            if parmMode1==1:
                num1=numbers[ptr+1]
            else:
                num1 = numbers[numbers[ptr+1]]
            if parmMode2==1:
                num2=numbers[ptr+2]
            else:
                num2 = numbers[numbers[ptr+2]]
            if parmMode3==1:
                numbers[ptr+3]=num1*num2
            else:
                numbers[numbers[ptr+3]]=num1*num2
            ptr+=4
        elif code ==3:
            numIn = int(input())
            if parmMode1==1:
                numbers[ptr+1] = numIn
            else:
                numbers[numbers[ptr+1]]= numIn
            ptr+=2
        elif code ==4:
            if parmMode1==1:
                print(numbers[ptr+1])
            else:
                print(numbers[numbers[ptr+1]])
            ptr+=2
        elif code ==5:
            parm1=0
            parm2=0
            if parmMode1==1:
                parm1 = numbers[ptr+1]
            else:
                parm1 = numbers[numbers[ptr+1]]
            if parmMode2==1:
                parm2=numbers[ptr+2]
            else:
                parm2=numbers[numbers[ptr+2]]
            if parm1!=0:
                ptr=parm2
            else:
                ptr+=3
        elif code ==6:
            parm1=0
            parm2=0
            if parmMode1==1:
                parm1 = numbers[ptr+1]
            else:
                parm1 = numbers[numbers[ptr+1]]
            if parmMode2==1:
                parm2=numbers[ptr+2]
            else:
                parm2=numbers[numbers[ptr+2]]
            if parm1==0:
                ptr=parm2
            else:
                ptr+=3
        elif code ==7:
            parm1=0
            parm2=0
            if parmMode1==1:
                parm1 = numbers[ptr+1]
            else:
                parm1 = numbers[numbers[ptr+1]]
            if parmMode2==1:
                parm2=numbers[ptr+2]
            else:
                parm2=numbers[numbers[ptr+2]]
            
            if parm1<parm2:
                if parmMode3==1:
                    numbers[ptr+3]=1
                else:
                    numbers[numbers[ptr+3]]=1
            else:
                if parmMode3==1:
                    numbers[ptr+3]=0
                else:
                    numbers[numbers[ptr+3]]=0
            ptr+=4
        elif code ==8:
            parm1=0
            parm2=0
            if parmMode1==1:
                parm1 = numbers[ptr+1]
            else:
                parm1 = numbers[numbers[ptr+1]]
            if parmMode2==1:
                parm2=numbers[ptr+2]
            else:
                parm2=numbers[numbers[ptr+2]]
            
            if parm1==parm2:
                if parmMode3==1:
                    numbers[ptr+3]=1
                else:
                    numbers[numbers[ptr+3]]=1
            else:
                if parmMode3==1:
                    numbers[ptr+3]=0
                else:
                    numbers[numbers[ptr+3]]=0
            ptr+=4
        elif code == 99:
            break
        else:
            print("Error Illegal Opcode")
            break
runComp()