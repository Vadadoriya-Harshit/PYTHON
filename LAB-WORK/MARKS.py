print("\n\n\t\t-------------Student Result-----------")
s1=int(input("\n\t Enter Chemistry Mark : "))
s2=int(input("\n\t Enter Physics Mark : "))
s3=int(input("\n\t Enter Maths Mark : "))
s4=int(input("\n\t Enter English Mark : "))
s5=int(input("\n\t Enter Computer Mark : "))
print("\n\t\t--------------------------------")

total=s1+s2+s3+s4+s5
print("\n\t\t Total is : ",total)
per=total/4
print("\n\t Percentages is : ",per)

if per<25:
    print("\n\n\t\t Grade F")
elif per<45:
    print("\n\n\t\t Grade E")
elif per<50:
    print("\n\n\t\t Grade D")
elif per<60:
    print("\n\n\t\t Grade C")
elif per<80:
    print("\n\n\t\t Grade B")
elif per>80:
    print("\n\n\t\t Grade A")
