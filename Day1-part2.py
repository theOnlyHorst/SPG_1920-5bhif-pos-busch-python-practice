

F= open("Day1-Inputs.txt","r")
nums = 0
for line in F:
    x=int(int(line)/3)-2
    nums+=x
    while x>0:
        x=int(int(x)/3)-2
        if x>0:
            nums+=x
print(nums)


