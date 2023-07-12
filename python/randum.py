#This program will find the percentage of a number

#Will handle the math
def percent(x,y):
    return x * y

while True:
    #Ask for user input
    num1 = float(input("Input your first number: "))
    num2 = float(input("Input your Second number: "))
    #Data validation
    if num1 > 1 and num2 > 1:
        print("Input atleast one percentage number (decimal format)")
    else:
        #Finds the percentage of one of the numbers
        print(num1, " * ", num2, " = ", percent(num1, num2))
        #Ask if the user wants to do another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
        elif next_calculation == "yes":
            continue
        else:
            print("Invalid Value")