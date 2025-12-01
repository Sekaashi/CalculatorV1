def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error, division by 0!"
    return x / y


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def main():
    print("Calculator v2")
    
    while True:
        while True:
            x_input = input("Enter first number or type 'quit' to exit: ").strip()
            if x_input.lower() == 'quit':
                print("Godbye!")
                return
            try:
                x = float(x_input)
                break
                
            except ValueError:
                print("Must be a number!")
        
        while True:
            y_input = input("Enter second number: ")
            try:
                y = float(y_input)
                break
            except ValueError:
                print("Invalid number! Try again.")
        
        
        while True:
            op = input("Choose operation (+ - * /): ")
            if op in operations:
                break
            print("Invalid operation! Use +, -, *, /")

    
    
        result = operations[op](x, y)
        print(f"Result: {x} {op} {y} = {result}\n")

if __name__ == "__main__":
    main()
        
        
        