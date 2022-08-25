num = int(input("Multiplication using value : "))

i=1 
while i <=num:
    j=1
    while j <= num:
        product = i*j 
        print(i, " * ", j, " = ", product, "\n") 
        j = j + 1
    print("\n")
    i = i + 1
