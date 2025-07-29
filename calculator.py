# --- evaluate the input ---

def equals(prompt):
    """evaluate the string"""
    
    try :
        total = str(eval(prompt))
    
    #catch division by 0 error
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"      
    # catch syntax error
    except SyntaxError:
        return "Syntax error!" 

    return total


# --- number validation ---

def check_input(prompt):
    """check input and validate"""
    for char in prompt:
        if char.isalpha():
            return True
    return False

# --- Main Calculator Logic ---

def main():
    """Main function to run the simple calculator app"""
    print("\n=== Simple Command-Line Calculator ===")
    
    while True:
                
       print("\nWhat would you like to do?")
       print("1. Enter math problem")
       print("2. Exit")
       
       choice = input("Enter choice (1/2): ")
       if choice == '2':
           print("Exiting calculator. Goodbye!")
           break
       elif choice == '1':   
            print("\nEnter your math question: ")
            math_problem = input("\n(ie. 1+1 or 2-1 or 2/1 or 1*2): ")
            if check_input(math_problem):
                print("Invalid input. Please don't include characters.")
            else:
                result = equals(math_problem)
                print(f"{math_problem} = {result}")
                print("\n------------------------------------------------") #separator line 
       else:
            print("invalid choice. ")

if __name__ == "__main__":
    main()