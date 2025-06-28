def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        print("Denominator cannot be zero")
    else:
        return x/y
    
def calculator():
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")

    choice=input("Enter a choice(1/2/3/4):")

    if choice in('1','2','3','4'):
        try:
            x=float(input("Enter first number:"))
            y=float(input("Enter second number: "))

        except ValueError:
            print("Invalid input.Enter a number")
            return
    
    if choice=='1':
        print(f"The result is{add(x,y)}")

    elif choice=='2':
        print(f"The result is{subtract(x,y)}")

    elif choice=='3':
        print(f"The result is{multiply(x,y)}")

    elif choice=='4':
        print(f"The result is{divide(x,y)}")

    else:
        print("Please enter a correct option")


calculator()
