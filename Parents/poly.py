#Parent class
class user:
    name = "connor"
    make = "mazda"
    model = "miata"
    color = "2016"
    
#user login
    def getLoginInfo(self):
        entry_name = input("What is your name: ")
        
        print("What is your car manufacture?")
        entry_make = input("Enter your make: ")
        
        print("What is your car model?")
        entry_model = input("Enter your model: ")
        
        print("When was your car made?")
        entry_color = input("Enter the year: ")

#conditonal statment to check if the information is correct 
        
        if (entry_model == self.model and entry_color == self.color and entry_make == self.make):
            print("Welcome back, {}!".format(entry_name))
            
        else:
            print("Please type in the car you own.")

        

#Child Class
class dealer(user):
    price = "19,000"
    pin = "1234"

#Employee login

    def getLoginInfo(self):
        entry_name = input("What is your name: ")
        
        print("What is your car manufacture?")
        entry_make = input("Enter your make: ")
        
        print("What is your car model?")
        entry_model = input("Enter your model: ")
        
        print("When was your car made?")
        entry_color = input("Enter the year: ")

        entry_pin = input("What is your pin: ")
        
#conditonal statment to check if the information is correct
       
        if (entry_model == self.model and entry_pin == self.pin):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Your information is incorrect.")


customer = user()
customer.getLoginInfo()

manager = dealer()
manager.getLoginInfo()
        
