"""
Created by (Esteban Gómez) in  ${2022}
"""

class Vector:

    def __init__(self,dim):
        self.dim = dim
        self.list_vector = [1,1,1,1,1]
        #for i in range(self.dim):
         #   self.list_vector.append(0)

    def __len__(self):
        return len(self.list_vector)

    def __getitem__(self, item, vector):
        return vector[item]

    def __setitem__(self, i , newvalue):
        self.list_vector[i]= newvalue
        return self.list_vector

    def __add__(self,other):
        NewVector=[]
        for i in range(len(self.list_vector)):
            value=self.list_vector[i] + other[i]
            NewVector.append(value)
        return NewVector

    def __eq__(self, other):
        equal=True
        count=0
        while equal==True and count <= self.dim:
            if self.dim == self.dim:
                for i in range (self.dim):
                    if self.list_vector[i]== other[i]:
                        equal=True
                        count+=1
                    else:
                        equal=False
            else:
                equal=False
        return equal

    def __dot__(self, other):
        scalarProduct=[]
        for i in range(self.dim):
            new_value= self.list_vector[i] * other[i]
            scalarProduct.append(new_value)
        return scalarProduct


    def cosine_distance(self,other):
        suma=0
        for i in range(len(other)):
            suma+= other[i]**2
        distance= suma ** 0.5
        return distance

    def __str__(self):
        return str(self.list_vector)


vector=Vector(5)

print(vector)

New_vector=[1,2,3,4,5]

add= vector.__add__(New_vector)
print("The addition of the original vector and this new one is: ",add)

cosine_distance= vector.cosine_distance(New_vector)
print("The cosine distance od this new vector is:" , cosine_distance)


len = vector.__len__()
print("The dimension of the vector is: ", len)

i=3
get_item= vector.__getitem__(i, New_vector)
print("The item in the position %d of the vector %s is: " %(i,New_vector), get_item)

newvalue=5
set_newValue= vector.__setitem__(i,newvalue)
print("We can change a specific element of the original vector, like here we change\nthe element in the position {} "
      "for the value {}:".format(i,newvalue), set_newValue)

scalarProduct=vector.__dot__(New_vector)
print("The Scalar Product between {} and {} is: ".format(vector,New_vector),scalarProduct)

equality= vector.__eq__(New_vector)
print("The vector {} and {} are equal? ".format(vector,New_vector), equality)

