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
        print("5. Exit")
        
        choice = input("Enter choice(1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
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
        else:
            print("Invalid input. Please enter a valid number.")
            
        print("\n------------------------------------------------") #separator line 

if __name__ == "__main__":
    main()