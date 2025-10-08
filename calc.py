import math

def sqrt_func(x):
    return math.sqrt(x)

def fact_func(x):
    return math.factorial(x)

def ln_func(x):
    return math.log(x)

def power_func(x, b):
    return math.pow(x, b)

if __name__ == "__main__":
    print("Scientific Calculator")
    print("sqrt(16) =", sqrt_func(16))
    print("factorial(5) =", fact_func(5))
    print("ln(2.71828) =", ln_func(2.71828))
    print("4^3 =", power_func(4, 3))
