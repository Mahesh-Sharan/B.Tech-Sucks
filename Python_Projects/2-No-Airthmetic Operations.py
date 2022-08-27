#Taking a Function for defining the operations
def Operation():
    a = int(input('Enter 1st Number : '))
    b = int(input('Enter 2nd  Number : '))
    c = (input('Select Operation from the Following : "+" "-" "*" "/"   : '))
    d=0

    if c=='+' :
        d=a+b
        print('\nSolution is : ',d)
    elif c=='-' :
        d=a-b
        print('\nSolution is : ',d)
    elif c=='*' :
        d=a*b
        print('\nSolution is : ',d)
    elif c=='/' :
        d=a/b
        print('\nSolution is : ',d)
    else:
        print('\nInvalid Operation')       
Operation()

#Took 2nd Function for calling Repeat or Exit Functions
def End():
    z = input('\n\nPress "E" for Exit & "A" for Again : ')
    if z=='a':
        Operation();
    elif z=='e':
        print(exit)
        exit()
End()
