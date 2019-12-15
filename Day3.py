F= open("Day3-Inputs.txt","r")
line = F.readline()
wirePath1 = line.split(",")
line = F.readline()
wirePath2 = line.split(",")
wire1X = []
wire1Y = []
wire2X = []
wire2Y = []

wire1X.append(0)
wire1Y.append(0)
wire2X.append(0)
wire2Y.append(0)
for instruct in wirePath1:
    direction = instruct[0]
    diststr = instruct[1:]
    dist = int(diststr)
    distcount =1
    while distcount<=dist:
        if direction == "R":
            wire1X.append(wire1X[len(wire1X)-1]+1)
            wire1Y.append(wire1Y[len(wire1Y)-1])
        elif direction == "L":
            wire1X.append(wire1X[len(wire1X)-1]-1)
            wire1Y.append(wire1Y[len(wire1Y)-1])
        elif direction == "U":
            wire1Y.append(wire1Y[len(wire1Y)-1]+1)
            wire1X.append(wire1X[len(wire1X)-1])
        elif direction == "D":
            wire1Y.append(wire1Y[len(wire1Y)-1]-1)
            wire1X.append(wire1X[len(wire1X)-1])
        distcount+=1

for instruct in wirePath2:
    direction = instruct[0]
    diststr = instruct[1:]
    dist = int(diststr)
    distcount=1
    while distcount<=dist:
        if direction == "R":
            wire2X.append(wire2X[len(wire2X)-1]+1)
            wire2Y.append(wire2Y[len(wire2Y)-1])
        elif direction == "L":
            wire2X.append(wire2X[len(wire2X)-1]-1)
            wire2Y.append(wire2Y[len(wire2Y)-1])
        elif direction == "U":
            wire2Y.append(wire2Y[len(wire2Y)-1]+1)
            wire2X.append(wire2Y[len(wire2X)-1])
        elif direction == "D":
            wire2Y.append(wire2Y[len(wire2Y)-1]-1)
            wire2X.append(wire2Y[len(wire2X)-1])
        distcount+=1

if len(wire1X)!=len(wire1Y):
    print("ERROR Wire1 parsing failed")
if len(wire2X)!=len(wire2Y):
    print("ERROR Wire2 parsing failed")

wire1Xtmp=wire1X.copy()
wire1Ytmp=wire1Y.copy()
wire2Xtmp=wire2X.copy()
wire2Ytmp=wire2Y.copy()

crossX=[]
crossY=[]

countW1=0
countCross=0
while countW1<len(wire1X):
    
    countW1+=1
print(countCross)
crossCount=0
while crossCount<len(crossX):
    #print(str(crossX[crossCount])+", "+str(crossY[crossCount]))
    crossCount+=1

