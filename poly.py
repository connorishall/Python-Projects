#Parent class
class Car:
    name = "Mazda"
    email = "Miata"
    password = "White"

    def getLoginInfo(self):
        print("what is car your manufacture.")
        entry_name = input("Enter your name: ")
        print("What is your car model.")
        entry_email = input("Enter your email: ")
        print("What is your car color.")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class
class Employee(Car):
    base_pay = "manual"
    department = "155"
    

#Employee login

    def getLoginInfo(self):
        print("Do you have a manual or an automatic.")
        entry_name = input("Enter your transmission type: ")
        print("How much hourse power do you have?")
        entry_email = input("Enter your house power: ")
       
        if (entry_email == self.email):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")


customer = Car()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
        
