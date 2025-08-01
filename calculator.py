import math

# --- Arithmetic Functions ---

def add(x,y):
    """return the sum of two numbers."""
    return x + y

def subtract(x,y):
    """return the difference of two numbers."""
    return x - y

def multiply(x,y):
    """return the product of two numbers."""
    return x * y

def divide(x,y):
    """return the division of two numbers."""
    return x / y

def square(x):
    """return the square of first number"""
    return x ** 2

def power(x,y):
    """return x raised to the power of y"""
    return x ** y

def square_root(x):
    """return square root of x"""
    return x ** 0.5

# --- User Interaction Functions ---

def get_input(prompt):
    """Get input and validate"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input, please enter a number.")

# --- Main Calculator Logic ---

def main():
    """Main function to run the simple calculator app"""
    print("\n=== Simple Command-Line Calculator ===")
    
    while True:
        
        number1 = get_input("Enter the first number: ")
        
        print("\nSelect operations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Squared (^2)")
        print("6. Exponent (^y)")
        print("7. Square root (√)")
        print("8. Exit")
        
        choice = input("Enter choice(1/2/3/4/5/6/7/8): ")
        
        if choice == '8':
            print("Exiting calculator. Goodbye!")
            break
        elif choice == '5':
            print(f"{number1} ^2 = {square(number1):.2f}")
        elif choice == '7':
            print(f"√{number1} = {square_root(number1):.2f}")
        
        elif choice in ('1', '2', '3', '4','6'):
            number2 = get_input("Enter the second number: ")
            
            if choice == '1':
                print(f"{number1} + {number2} = {add(number1, number2):.2f}")
            elif choice == '2':
                print(f"{number1} + {number2} = {subtract(number1, number2):.2f}")
            elif choice == '3':
                print(f"{number1} + {number2} = {multiply(number1, number2):.2f}")
                #handle division by 0
            elif choice == '4':
                if number2 == 0:
                    print("Error: cannot divide by zero!")
                else:
                    print(f"{number1} + {number2} = {divide(number1, number2):.2f}")  
            elif choice == '6':
                print(f"{number1} ^ {number2} = {power(number1,number2):.2f}")
                
        else:
            print("Invalid input. Please enter a valid number.")
            
        print("\n------------------------------------------------") #separator line 

if __name__ == "__main__":
    main()