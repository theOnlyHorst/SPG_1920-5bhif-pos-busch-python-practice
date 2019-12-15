
digitsMin = [1, 5, 3, 5, 1, 7]
digitsMax = [6, 3, 0, 3, 9, 5]

def combDigits(digitsIn):
    res = 0
    counter = len(digitsIn)-1
    while counter>=0:
        res+= digitsIn[len(digitsIn)-counter-1]*pow(10,counter)
        counter-=1
    return res

def pwRuleConform(digitsIn):
    if len(digitsIn)!=6:
        return False
    if combDigits(digitsIn)<combDigits(digitsMin) or combDigits(digitsIn)> combDigits(digitsMax):
        return False
    numPair = False
    numComboCount =0
    counter =1
    while counter<len(digitsIn):
        if digitsIn[counter] == digitsIn[counter-1]:
            numComboCount+=1
        else:
            if numComboCount==1:
                numPair = True
            numComboCount =0
        counter+=1
    if numComboCount==1:
        numPair = True
    if numPair==False:
        return numPair
    counter =1
    while counter<len(digitsIn):
        if digitsIn[counter] < digitsIn[counter-1]:
            return False
        counter+=1
    return True
    

countCorrectPw=0
digitsCurr = digitsMin.copy()

while combDigits(digitsCurr)< combDigits(digitsMax):
    if pwRuleConform(digitsCurr):
        countCorrectPw+=1
    x=5
    while digitsCurr[x] ==9:
        digitsCurr[x] = 0
        x-=1
    digitsCurr[x]+=1

print(countCorrectPw)