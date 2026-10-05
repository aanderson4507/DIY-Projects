def addition(num1: float, num2: float) -> float:
    """This function adds two numbers together

        Args: 
            num1: first number
            num2: second number

        Returns:
            The sum
    """
    return num1 + num2

def subtraction(num1: float, num2: float) -> float:
    """This fuction subtracts one number from another

        Args:
            num1: number to subtract from
            num2: number to subtract by

        Returns:
            The diffrence
    """

    return num1 - num2

def mutliplication(num1: float, num2: float) -> float:
    """This function mutiplies two numbers togther

        Args: 
            num1: multiplicand
            num2: multiplier

        Returns:
            The product
    """

    return num1 * num2

def division(num1: float, num2: float) -> float | str:
    """This function divides one number by another

        Args: 
            num1: dividend
            num2: divisor

        Returns:
            The quotient or a divide by zero error
    """

    if(num2 == 0):
        return "Error: Division by Zero"

    #Note: Division always results in a float 
    return num1 / num2

def exponentiation(num1: float, num2: float) -> float:
    """This function raises one number by another

        Args:
            num1: base
            num2: exponet

        Returns:
            The value of the base times itself the amount of the exponet times
    """

    return num1 ** num2

def main():
    keep_running = True
    choice = 0
    while keep_running == True:
        print("Austin's Calculator (Version 0.1.0)")
        print("Options: ")
        print("Type 0 to Quit")
        print("Type 1 to do Addition")
        print("Type 2 to do Subtraction")
        print("Type 3 to do Multiplication")
        print("Type 4 to do Division")
        print("Type 5 to do Exponentiation")

        choice = int(input("Please make a selection: "))

        if choice == 0:
            keep_running = False
        elif choice == 1:
            val1 = float(input("Please enter the first number: "))
            val2 = float(input("Please enter the second number: "))

            print(addition(val1, val2))
        elif choice == 2:
            val1 = float(input("Please enter the number to subtract from: "))
            val2 = float(input("Please enter the number to subtract by: "))
            
            print(subtraction(val1, val2))
        elif choice == 3:
            val1 = float(input("Please enter the first number: "))
            val2 = float(input("Please enter the second number: "))

            print(mutliplication(val1, val2))
        elif choice == 4:
            val1 = float(input("Please enter the dividend: "))
            val2 = float(input("Please enter the divisor: "))

            print(division(val1, val2))
        elif choice == 5:
            val1 = float(input("Please enter the base: "))
            val2 = float(input("Please enter the exponet"))

            print(exponentiation(val1, val2))
        else:
            print("Please select one of the available options")

    print("Thanks for using Austin's calculator!")

if __name__ == "__main__":
    main()
