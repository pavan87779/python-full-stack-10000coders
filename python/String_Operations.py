#String Operations
fname = "Pavan"
lname = "Babu"
print(fname,lname)
#Pavan Babu
print(fname[1]) #a
print(fname[1:]) #avan
print(fname[2:4]) #va
print(fname[0],fname[-1]) #pn
print(fname[:2],fname[-2:]) #pa na
print(fname[0] + (len(fname)-2)*"*"+ fname[-1]) #p***n
print("-----------------------------------")
print(fname[:2]+"*"+fname[3:]) #pa*an
print("---------------------------------")
fullname = "GoulikarPavanBabu"
mid = len(fullname)//2
print(fullname[:mid]) #firsthalf-- Goulikar
print(fullname[mid:]) #secondhalf-- PavanBabu

name ="PavanBabu"
num = 3
print(3*name)