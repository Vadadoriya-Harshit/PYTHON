status=True
def menu():
    print("\t\t------------Menu------------")
    print("\t\t| press 1 for Registration |")
    print("\t\t| press 2 for Login        |")
    print("\t\t| press 0 for Exit         |")
    print("\t\t|--------------------------|")

db = {}
def Registration(name, email, password):
    db["name"] = name
    db["email"] = email
    db["password"] = password
    print("\n\t\t!---Registration Successful--!")

def login(email,password):
    if email == db["email"] and password == db["password"]:
      print("\n\t\tWELCOME",db["name"],"You Are Successfully Login")
    else :
       return print("Invalid Email or Password") 
    
def choice():
   reply=int(input("\n\t\t Enter Your Choice : "))
   if (reply==1):
      name=input("\n\t\t Enter Name              : ")
      email=input("\n\t\t Enter Email            : ")
      password=input("\n\t\t Enter Your Password : ")
      Registration(name,email,password)
   elif (reply==2):
      email=input("\n\t\t Enter email       :")
      password=input("\n\t\t Enter Password :")
      login(email,password)
   else:
        print("You are exited")

menu()
choice()
menu()
choice()
