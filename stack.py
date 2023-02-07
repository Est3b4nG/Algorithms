"""
Created by (Esteban Gómez) in  ${2022}
"""

class Stack:

    def __init__(self):
        self.items=[]

    def __str__(self):
        return str(self.items)

    def __len__(self):
       return len(self.items)

    def Top(self):
        return self.items[0]

    def isEmpty(self):
        return len(self)==0

    def push(self,e):
        self.items.append(e)

    def pop(self):
        if self.isEmpty()==True:
            return None
        else:
            return self.items.pop()


myStack= Stack()

#myStack.push("A")
#myStack.push("B")
#print(myStack)
#myStack.pop()
#myStack.isEmpty()
#print(myStack)
#print(myStack.Top())

if myStack.pop()==None:
    myStack.push("C")

#print(myStack)

#print(myStack.items)



class Example:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        text= "{} {} {}".format(self.a,self.b,self.c)
        #text = ("Soy el robot %i , me llamo %f, tengo esta lista %s" % (self.a, self.b, self.c ))
        return text


#ex = Example(1,"Pepe", [5,2,3])
#print(ex.b)
#print(ex)

