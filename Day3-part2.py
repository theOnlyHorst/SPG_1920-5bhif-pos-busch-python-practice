class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def add(self,x,y):
        return Point(self.x+x,self.y+y)
    
    def sub(self,other):
        return Point(self.x-other.x,self.y-other.y)

    def __eq__(self,other):
        if not isinstance(other, Point):
            # don't attempt to compare against unrelated types
            return NotImplemented
        
        return self.x == other.x and self.y == other.y

    def manhattenDist(self,other):
        if not isinstance(other, Point):
            return NotImplemented
        return abs(self.x - other.x)+abs(self.y - other.y)

F= open("Day3-Inputs.txt","r")
line = F.readline()
wirePath1 = line.split(",")
line = F.readline()
wirePath2 = line.split(",")

wire1 = []
wire2 = []

wire1.append(Point(0,0))
wire2.append(Point(0,0))
for instruct in wirePath1:
    direction = instruct[0]
    diststr = instruct[1:]
    dist = int(diststr)
    if direction == "R":
        wire1.append(wire1[len(wire1)-1].add(dist,0))
    elif direction == "L":
        wire1.append(wire1[len(wire1)-1].add(dist*-1,0))
    elif direction == "U":
        wire1.append(wire1[len(wire1)-1].add(0,dist))
    elif direction == "D":
        wire1.append(wire1[len(wire1)-1].add(0,dist*-1))

for instruct in wirePath2:
    direction = instruct[0]
    diststr = instruct[1:]
    dist = int(diststr)
    if direction == "R":
        wire2.append(wire2[len(wire2)-1].add(dist,0))
    elif direction == "L":
        wire2.append(wire2[len(wire2)-1].add(dist*-1,0))
    elif direction == "U":
        wire2.append(wire2[len(wire2)-1].add(0,dist))
    elif direction == "D":
        wire2.append(wire2[len(wire2)-1].add(0,dist*-1))

countW1=1
countCross=0
cross = []
while countW1<len(wire1):

    wLineDist1 = wire1[countW1].sub(wire1[countW1-1])

    countW2 = 1
    if wLineDist1.x ==0:
        while countW2<len(wire2):
            wLineDist2 = wire2[countW2].sub(wire2[countW2-1])
            if wLineDist2.x==0:
                countW2+=1
                continue
            wLineX1 = wire1[countW1].x
            wLineY2 = wire2[countW2].y
            if wLineDist2.x <0:
                if wLineX1>=wire2[countW2].x and wLineX1<=wire2[countW2-1].x:
                    if wLineDist1.y<0:
                        if wLineY2>=wire1[countW1].y and wLineY2<=wire1[countW1-1].y:
                            cross.append(Point(wLineX1,wLineY2))
                    else:
                        if wLineY2<=wire1[countW1].y and wLineY2>=wire1[countW1-1].y:
                            cross.append(Point(wLineX1,wLineY2))
            else:
                if wLineX1<=wire2[countW2].x and wLineX1>=wire2[countW2-1].x:
                    if wLineDist1.y<0:
                        if wLineY2>=wire1[countW1].y and wLineY2<=wire1[countW1-1].y:
                            cross.append(Point(wLineX1,wLineY2))
                    else:
                        if wLineY2<=wire1[countW1].y and wLineY2>=wire1[countW1-1].y:
                            cross.append(Point(wLineX1,wLineY2))
            countW2+=1
    else:
        while countW2<len(wire2):
            wLineDist2 = wire2[countW2].sub(wire2[countW2-1])
            if wLineDist2.y==0:
                countW2+=1
                continue
            wLineX2 = wire2[countW2].x
            wLineY1 = wire1[countW1].y
            if wLineDist2.y <0:
                if wLineY1>=wire2[countW2].y and wLineY1<=wire2[countW2-1].y:
                    if wLineDist1.x<0:
                        if wLineX2>=wire1[countW1].x and wLineX2<=wire1[countW1-1].x:
                            cross.append(Point(wLineX2,wLineY1))
                    else:
                        if wLineX2<=wire1[countW1].x and wLineX2>=wire1[countW1-1].x:
                            cross.append(Point(wLineX2,wLineY1))
            else:
                if wLineY1<=wire2[countW2].y and wLineY1>=wire2[countW2-1].y:
                    if wLineDist1.x<0:
                        if wLineX2>=wire1[countW1].x and wLineX2<=wire1[countW1-1].x:
                            cross.append(Point(wLineX2,wLineY1))
                    else:
                        if wLineX2<=wire1[countW1].x and wLineX2>=wire1[countW1-1].x:
                            cross.append(Point(wLineX2,wLineY1))
            countW2+=1
    countW1+=1


crossSteps = []
for crossPt in cross:
    currX = 0
    currY = 0
    stepCount = 0
    for instruct in wirePath1:
        direction = instruct[0]
        diststr = instruct[1:]
        dist = int(diststr)
        distcount =0
        cont = True
        while distcount<dist and cont ==True:
            if direction == "R":
                currX+=1
            elif direction == "L":
                currX-=1
            elif direction == "U":
                currY+=1
            elif direction == "D":
                currY-=1
            stepCount+=1
            if crossPt.x == currX and crossPt.y == currY:
                cont =False
            distcount+=1
        if cont == False:
            break
    currX = 0
    currY = 0
    for instruct in wirePath2:
        direction = instruct[0]
        diststr = instruct[1:]
        dist = int(diststr)
        distcount =0
        cont = True
        while distcount<dist and cont ==True:
            if direction == "R":
                currX+=1
            elif direction == "L":
                currX-=1
            elif direction == "U":
                currY+=1
            elif direction == "D":
                currY-=1
            stepCount+=1
            if crossPt.x == currX and crossPt.y == currY:
                cont =False
            distcount+=1
        if cont == False:
            break
    crossSteps.append(stepCount)


crossSteps.sort()

for steps in crossSteps:
    print(steps)
