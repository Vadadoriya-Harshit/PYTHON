print("\n\n----------Find Maximum Number From Three Numbers-----------")
a=int(input("\n\n\t Enter A : "))
b=int(input("\n\n\t Enter B : "))
c=int(input("\n\n\t Enter C : "))
print("\n\n\t A is {}".format(a))
print("\t B is {}".format(b))
print("\t C is {}".format(c))

if a>b or a>c:
    print(f"\n\n\t\t {a} is Greater")
elif b>a or b>c:
    print(f"\n\n\t\t {b} is Greater")
else:
    print(f"\n\n\t\t {c} is Greater")
