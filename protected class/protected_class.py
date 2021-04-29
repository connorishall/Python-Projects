
#class protected
class Protected:
    #protected
    def __init__(self):
        self._ProtectedVar = 0
    #private
    def __init__(self):
        self.__privateVar = 16

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
        
#Ensures private cannot be changed
obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
obj._ProtectedVar = 50
print(obj._ProtectedVar)

