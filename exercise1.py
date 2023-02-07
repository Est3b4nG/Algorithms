"""
Created by (Esteban Gómez) in  ${2022}
"""

class Bank:
    """This class creates a well structured credit card simulation in which you can introduce and get out money"""

    def __init__(self, customer=str, idCard=int, limit=float, balance=float):
        """This method both declares the attributes of the class and
        receives the initial value of all them.
        @param number 1: str
        @param number 2: int
        @param number 3: float
        @param number 4 : float   """

        self.customer = customer
        self.idCard = idCard
        self.limit = limit         #This is the limit of money the user can spend
        self.balance = 0    #This is the money spent


    def chargeprice(self, amount):
        if self.balance + amount <= self.limit:
            self.balance +=  amount
        else:
            self.balance = self.balance

    def make_deposit(self, amount):
        if self.balance>= amount:
            self.balance -= amount
        else:
            return "You can't do this operation"

    def __str__(self):
        return "Name:" + str(self.customer) + "\nBalance: " + str(self.balance) + "\n Limit:" + str(self.limit)


card= Bank( str(input("Name:")), int(input("ID:")), float(input("Limit:")) )

print(card)
amount=0
amount2=0
card.chargeprice(amount)
card.make_deposit(amount2)
loop=True

while amount!=0 or amount2!=0 or loop==True:
    amount=float(input("How much you want to spend: "))
    amount2 = float(input("How much you want to pay: "))
    card.chargeprice(amount)
    card.make_deposit(amount2)
    print(card)
    if amount==0 and amount2==0:
        loop=False
