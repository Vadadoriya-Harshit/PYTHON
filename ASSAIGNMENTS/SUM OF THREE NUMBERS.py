a=int(input("\n\n\t\t Enter A : "))
b=int(input("\n\n\t\t Enter B : "))
c=int(input("\n\n\t\t Enter C : "))
print("A : ",a)
print("B : ",b)
print("C : ",c)
 
if a==b or b==a or c==a or c==a or b==c or c==b:
    print("The sum is 0")
else: 
    print("The sum is :",a+b+c)
