F= open("Day1-Inputs.txt","r")
x = 0
for line in F:
    x+=int(int(line)/3)-2
print(x)