class TreeObj:
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
    
    def __eq__(self,other):
        if isinstance(other,TreeObj)
        return self.name==other.name and self.parent==other.parent

F = open("Day6-Inputs.txt")
COM = TreeObj("COM",None)
for line in F:
    splLine= line.split(")")
    TreeObj(splLine[1],splLine[0])