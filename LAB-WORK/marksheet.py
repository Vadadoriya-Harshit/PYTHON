s1=int(input("Enter the marks of subject 1 : "))
s2=int(input("Enter the marks of subject 2 : "))
s3=int(input("Enter the marks of subject 3 : "))
s4=int(input("Enter the marks of subject 4 : "))

if s1>=35 and s2>=35 and s3>=35 and s4>=35:
    total = s1+s2+s3+s4
    print("Total",total)

    per=total/4
    print("Percentage",per)

    if per>=70:
        print("Distinction")
    elif per>=60:
        print("First Class")
    elif per>=50:
        print("Second class")
    elif per>=40:
        print("Pass class")
else:
    print("Fail") 