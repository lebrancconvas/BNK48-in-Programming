import random
class idol():
    def __init__(self,idol1,idol2):
        self.idol1 = idol1
        self.idol2 = idol2
    def shooting(self,idshoot1,idshoot2):
        if(idshoot1 > idshoot2):
            print("{} {} {}".format(self.idol1,"SHOOT",self.idol2))
            print("{} {}".format(self.idol2,"DEFEATED"))
        elif(idshoot2 > idshoot1):
            print("{} {} {}".format(self.idol2,"SHOOT",self.idol1))
            print("{} {}".format(self.idol1,"DEFEATED"))
        else:
            print("{}".format("DRAW"))

a = idol("Cherprang","Kaimook")
a.shooting(random.randint(1, 10),random.randint(1, 10))        
print("")
b = idol("Miori","Jane")
b.shooting(random.randint(1, 10),random.randint(1, 10)) 
print("")  
c = idol("Satchan","Pun")
c.shooting(random.randint(1, 10),random.randint(1, 10))  
print("") 
d = idol("Music","Jennis")
d.shooting(random.randint(1, 10),random.randint(1, 10))   