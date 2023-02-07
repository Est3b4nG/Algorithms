"""
Created by (Esteban Gómez) in  ${2022}
"""



class Queue:

    def __init__(self):
        self.items=[]

    def __str__(self):
        return str(self.items)

    def __len__(self):
       return len(self.items)

    def isEmpty(self):
        return len(self)==0

    def enqueue(self,e):
        self.items.append(e)


    def dequeue(self):
        if self.isEmpty()==True:
            return None
        else:
            return self.items.pop(0)

    def front(self):
        if self.isEmpty():
            print('Error: Queue is empty')
            return None

        return self.items[0]


myqueue= Queue()

myqueue.enqueue("e")
myqueue.enqueue("B")
print(myqueue)
myqueue.dequeue()
myqueue.isEmpty()
print(myqueue)