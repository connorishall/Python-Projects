
from abc import ABC, abstractmethod
#parent class
class mortgage(ABC):
    def paySlip(self, amount):
        print("On your mortgage you owe:",amount)


        @abstractmethod
        def payment(self, amount):
            pass
#child class
class MortgagePayment(mortgage):
    #Implementing the parent class
    def payment(self, amount):
        print('You only paid {} '.format(amount))

        

obj = MortgagePayment()
#Information used for child and parent class
obj.paySlip("$1002")
obj.payment("$500")

