class Tree:
    def __init__(self, name, availability, requirement):
        self.name = name
        self.availability = availability
        self.requirement = requirement
        self.surplus = 0
        self.children = []
        self.proportion = []
    def insert(self, node):
        self.children.append(node)
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
        
    def updatereq(self,req):
#        if(self.name == "VPVL"):
#            print(req)
        if(self.surplus<req):
            shortage = req-self.surplus
            add_req = int(shortage/self.availability) * self.availability
            self.surplus = 0
            if(add_req<shortage):
                add_req = add_req+self.availability
                self.surplus = add_req-shortage
            for i,child in enumerate(self.children):
                child.updatereq(int(add_req/self.availability)*self.proportion[i])
            self.requirement = self.requirement+add_req
        else:
            self.surplus = self.surplus-req
        return
        
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
    def printtree(self,level):
        i=0
        print_str = ""
        while(i<level):
            print_str=print_str+"    "
            i = i+1
        print_str=print_str+'+'+str(self.requirement)+'/'+self.name+'/'+str(self.availability)
        print(print_str)
        for child in self.children:
            child.printtree(level+1)
        return

file = open("input_day14.txt","r")
#file = open("test.txt","r")
lines = file.readlines()
#print(line[0])
sequence = [val.rstrip() for line in lines for val in line.split(")")]
    
floatingtrees = []

for eqn in sequence:
    num_str = ""
    num = 0
    name = ""
    #isnumber = False
    isname = False
    reactants = []
    reactants_q = []
    new_node = None
    removelist = []
    for c in eqn:
        if(c>='0' and c<='9'):
            #isnumber = True
            num_str = num_str + c
        elif(c>='A' and c<='Z'):
            isname = True
            name = name+c
        elif(c==' ' or c==','):
            if(isname):
                num = int(num_str)
                num_str = ""
                isname = False
                new_node = None
                for fltree in floatingtrees:
                    new_node = fltree.findnode(name)
                    if(new_node):
                        if(fltree.name == name):
                            removelist.append(fltree)
                            #floatingtrees.remove(fltree)
                        break
                if(new_node):
                    reactants.append(new_node)
                    #new_node.updatereq(num)
                else:
                    new_node = Tree(name,1,0)
                    reactants.append(new_node)
                name = ""
                reactants_q.append(num)
    num = int(num_str)
    new_node = None
    for fltree in floatingtrees:
        new_node = fltree.findnode(name)
        if(new_node):
            break
    if(new_node == None):
        new_node = Tree(name,num,0)
        floatingtrees.append(new_node)
    else:
        new_node.availability = num
    for i,node in enumerate(reactants):
        #node.updatereq(reactants_q[i])
        new_node.proportion.append(reactants_q[i])
        new_node.insert(node)
    for node in removelist:
        floatingtrees.remove(node)

#print(len(floatingtrees))
ore = floatingtrees[0].findnode("ORE")
fuel = 0
while(ore.requirement<=1000000000000):
    fuel = fuel+1
    floatingtrees[0].updatereq(1)
    if(fuel%10000==0):
        print(fuel,ore.requirement)
#floatingtrees[0].printtree(0)
#ore = floatingtrees[0].findnode("ORE")
print(fuel,ore.requirement)