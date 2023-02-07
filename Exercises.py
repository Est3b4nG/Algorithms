"""
Created by (Esteban Gómez) in  ${2022}
"""

from stack import Stack


newStack= Stack()

def reverse(word):
    for i in word:
        newStack.push(i)
        print(newStack)    #Test Material

    reword=""
    for i in range(len(newStack)):
        reword = reword + newStack.pop()   #Lo elimina y te lo devuelve
        print(reword)
    return reword



print(reverse("hello"))

""""
Problem 1 – Balanced arithmetic expression.
Implement a Python class to guess if the delimiters (,),{,},[,] in an arithmetic expression
(e.j. [(5+x)-(y+z)]) are balanced.
● Correct expression example: ()(()){([()])}
● Incorrect expression example: ({[])}
Use a stack to implement your solution. Consider the following hints:
● If an opening symbol is found [,(,{ it must be pushed.
● If a closing symbol is found ],},) the element at the top of the stack must be
queried. If both symbols belong to the same type, the element must be removed.
● The arithmetic expression is balanced if at the end of the process the stack is
empty."""

mathStack = Stack()
mathQueue = Queue()
class Arithmetic:
    def __init__(self,expression):
        self.expression=expression

    # def balance(self):
    #     for i in range(len(self.expression)):
    #         if self.expression[i]=="(" or self.expression[i]=="[" or self.expression[i]=="{":
    #             mathStack.push(self.expression[i])
    #         if self.expression[i]==")":
    #             if mathStack.Top()=="(":
    #                 mathStack.pop()
    #         if self.expression[i]=="]":
    #             if mathStack.Top()=="[":
    #                 mathStack.pop()
    #         if self.expression[i]=="}":
    #             if mathStack.Top()=="{":
    #                 mathStack.pop()

    def balance(self):
        for i in range(len(self.expression)):
            if self.expression[i]=="(":
                mathStack.push(self.expression[i])
            elif self.expression[i]==")":
                if mathStack.isEmpty():
                    return "Not correct"
                else:
                    mathStack.pop()

            elif self.expression[i]=="[":
                mathStack.push(self.expression[i])

            elif self.expression[i] == "]":
                if mathStack.isEmpty():
                    return "Not correct"
                else:
                    mathStack.pop()

            elif self.expression[i]=="{":
                mathStack.push(self.expression[i])

            elif self.expression[i]=="}":
                if mathStack.isEmpty():
                    return "Not correct"
                else:
                    mathStack.pop()

        if len(mathStack)!=0:
            return "Not correct"
        else:
            return "Correct"




f= str(input("Put your equation: "))

equation= Arithmetic(f)


test=equation.balance()
print(test)