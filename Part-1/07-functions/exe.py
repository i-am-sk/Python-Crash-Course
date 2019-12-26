### calculate a fahrenit from celsius

def cel_to_far():
    celsius = float(input("Enter Celsiu value: "))

    fahrenit = (celsius * 1.8) + 32
    print(f"Fahrenit value is: {fahrenit}")

cel_to_far()

def prime_not():
    value = int(input("Enter a value: "))

    if value % 2 == 0 :
        print(f"{value} is a prime number")
    else:
        print(f"{value} is not a prime number")

prime_not()