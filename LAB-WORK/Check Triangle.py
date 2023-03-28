print("\n\n\t------------Check The Trianngle------------")
s1=int(input("\n\n\t\t Enter Side 1 : "))
s2=int(input("\n\t\t Enter Side 2 : "))
s3=int(input("\n\t\t Enter Side 3 : "))
print("\n\n\t\t The Sides Of Triangle Is : \n")
print("\t\t Side 1 is : ",s1)
print("\t\t Side 2 is : ",s2)
print("\t\t Side 3 is : ",s3)

if s1==s2==s3:
    print("\n\n\t\t The Triangle Is equilateral")
elif s1==s2 or s1==s3 or s2==s3:
    print("\n\n\t\t The Triangle Is isosceles")
else:
    print("\n\n\t\t The Triangle Is scalene")
    
    