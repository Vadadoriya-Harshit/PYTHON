n=int(input("\n\t Enter Any Number"))
factorial=1
i=1
if n<0:
    print("\n\t The Number Is Nagative Please Input Positive Number")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial of",n,"is",factorial)