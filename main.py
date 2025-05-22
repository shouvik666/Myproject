a = "Shouvik"
print(a)
#age = int(input("Enter Your Age"))
#length = float(input("Enter the length"))
#eval = eval(input("Write the Equation"))

a = len(a)
b = "40"
b = int(b) #Expplicit TypeCasting
print(a,b)
a,b = b,a
print(a,b)
b -= 3
if (not(a<b) and not(a == b) and a is not b):
    for i in range(1,b):
        print(i,"True")
