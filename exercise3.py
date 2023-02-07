"""
Created by (Esteban Gómez) in  ${2022}
"""
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients=coefficients

    def polynomial(self):
        expression="Q(x)= "
        n=0
        for i in range (len(self.coefficients)):
            expression+= str(self.coefficients[i])+ "x°"+str(n)+ " + "
            n+=1
        return expression[:-2]     #To delete the last element two elements "+ "

    def getDegree(self):
        return len(self.coefficients)-1

    def getCoefficient(self,n):
        coefficient= self.coefficients[n]
        return coefficient

    def setCoefficient(self,n, newvalue):
        self.coefficients[n]=newvalue
        return Polynomial.polynomial(self)

    def evaluate(self,x):
        a=0
        result=0
        for i in range(len(self.coefficients)):
            result+= self.coefficients[i] * (x ** a)
            a+=1
        return result

    def sum(self, p):
        for i in range (len(self.coefficients)):
            self.coefficients[i] = int(self.coefficients[i]) + int(p[i])
        return Polynomial.polynomial(self)



originallistCoef= [1,2,3,4,5]
listCoef= [1,2,3,4,5]

polynomial= Polynomial(listCoef)

my_poly=polynomial.polynomial()
print(my_poly)

degree= polynomial.getDegree()
print("The degree of the polynomial is: ", degree)


n=int(input("Of what degree you want to find the coefficient: "))
coefficient= polynomial.getCoefficient(n)
print("The coefficient of the degree {} is: ".format(n), coefficient)


degree=int(input("To what degree you want to change the coefficient: "))
newCoe=int(input("What will be the new value: "))
newpoly=polynomial.setCoefficient(degree,newCoe)
print("The new polynomial will be: ", newpoly)


x = int(input("What number you want to evaluate: "))
answer= polynomial.evaluate(x)
print("The result of this function evaluated in {} will be: ".format(x), answer )

poly=[]
p= None
while p != "*":
    p=(input("Introduce the coefficients, press * when you want to stop: "))
    if p!="*":
        poly.append(int(p))

result = polynomial.sum(poly)
print("The result of adding {} and {} is: ".format(originallistCoef,poly), result)