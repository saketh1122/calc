import math
#comment
def sqrt_func(x):
    return math.sqrt(x)

def fact_func(x):
    return math.factorial(x)

def ln_func(x):
    return math.log(x)

def power_func(x, b):
    return math.pow(x, b)

if __name__ == "__main__":
    while True:
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Logarithm (ln)")
        print("4. Power")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            x = float(input("Enter number: "))
            print("Result =", sqrt_func(x))
        elif choice == '2':
            x = int(input("Enter integer: "))
            print("Result =", fact_func(x))
        elif choice == '3':
            x = float(input("Enter number: "))
            print("Result =", ln_func(x))
        elif choice == '4':
            x = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result =", power_func(x, b))
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

