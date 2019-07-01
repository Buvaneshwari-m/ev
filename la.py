k1 = float(input("Enter first number: "))
k2 = float(input("Enter second number: "))
k3 = float(input("Enter third number: "))
 
if (k1 > k2) and (k1 > k3):
   largest = k1
elif (k2 > k1) and (k2 > k3):
   largest = k2
else:
   largest = k3
 
print("The largest number is",largest)
