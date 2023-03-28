# Taking input from user
n = int(input("Enter the number of terms: "))

# Initializing variables
a = 0
b = 1

# Printing first two terms
print(a, b, end=" ")

# Finding and printing the next terms
for i in range(2,n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c