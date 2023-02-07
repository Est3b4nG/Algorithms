"""
Created by (Esteban Gómez) in  ${2022}
"""


class Range:

    def __init__(self,start, end, step=1):
        if step == 0:
            raise ValueError("This value is not correct")
        if start>end:
            raise ValueError("You can not have a start bigger than end")
        self.start=start
        self.end=end
        self.items=[]

    def listcreation(self):
        value = self.start
        while value < self.end:
            self.items.append(value)
            value += 1
        return self.items


start=int(input("What is the begginning number: "))
end=int(input("What is the ending number: "))
range = Range(start,end,1)

print("The range is from {} to {} ".format(start,end))

my_range= range.listcreation()
print(my_range)

