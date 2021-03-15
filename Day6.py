class Tree:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
    def insert(self, node):
        self.children.append(node)
    def setvalue(self,value):
        self.value = value
        for child in self.children:
            child.setvalue(value+1)
    def findnode(self,name):
        if(self.name==name):
            return self
        elif(len(self.children)>0):
            for child in self.children:
                node = child.findnode(name)
                if(node):
                    return node
        else:
            return None
    def getnodepath(self,name,path):
        if(self.name==name):
            path.append(self.name)
            return self
        elif(len(self.children)>0):
            for child in self.children:
                node = child.getnodepath(name,path)
                if(node):
                    path.append(self.name)
                    return node
        else:
            return None
    def gettotalvalue(self,currvalue):
        totalvalue = currvalue+self.value
        for child in self.children:
            totalvalue = child.gettotalvalue(totalvalue)
        return totalvalue

file = open("input_day6.txt","r")
#file = open("test.txt","r")
lines = file.readlines()
#print(line[0])
sequence = [val.rstrip() for line in lines for val in line.split(")")]
#print(sequence)
i=0
parent_node = Tree(sequence[i],0)
child_node = Tree(sequence[i+1],1)
parent_node.insert(child_node)
i = i+2
floatingtrees = []
floatingtrees.append(parent_node)
while(i<len(sequence)):
    for fltree in floatingtrees:
        if(fltree.name == 'C9Q'):
            i=i
        parent_node = fltree.findnode(sequence[i])
        if(parent_node):
            break
    for fltree in floatingtrees:
        child_node = fltree.findnode(sequence[i+1])
        if(child_node):
            break
    if(parent_node and child_node):
        parent_node.insert(child_node)
        child_node.setvalue(parent_node.value+1)
        floatingtrees.remove(child_node)
    elif(child_node):
        parent_node = Tree(sequence[i],0)
        parent_node.insert(child_node)
        child_node.setvalue(parent_node.value+1)
        floatingtrees.remove(child_node)
        floatingtrees.append(parent_node)
    elif(parent_node):
        child_node = Tree(sequence[i+1],parent_node.value+1)
        parent_node.insert(child_node)
    else:
        parent_node = Tree(sequence[i],0)
        child_node = Tree(sequence[i+1],1)
        parent_node.insert(child_node)
        floatingtrees.append(parent_node)
    i = i+2

#a_node.pre_order()

#print(node.name)
you_path = []
san_path = []
print(floatingtrees[0].gettotalvalue(0))
comnode = floatingtrees[0]
comnode.getnodepath('YOU',you_path)
comnode.getnodepath('SAN',san_path)
for i,name in enumerate(you_path):
    if(you_path[-i-1]==san_path[-i-1]):
        continue
    else:
        break
print(len(you_path)-i)
print(len(san_path)-i)