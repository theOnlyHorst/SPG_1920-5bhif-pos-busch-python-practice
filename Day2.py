
F= open("Day2-Inputs.txt","r")
numbers = []
line = F.readline()
arr = line.split(",")
for it in arr:
    numbers.append(int(it))
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

for num in numbers:
    print(str(num) + ', ', end='')

    