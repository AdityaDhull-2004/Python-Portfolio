def addition(num1,num2):
    return num1 + num2
def substraction(num1,num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1 * num2
def division(num1,num2):
    return num1/num2
def exponent(num1,num2):
    return num1**num2


operations = {"+" : addition
, "-" : substraction
, "*" : multiplication
, "/" : division
, "**" : exponent
}

def calculator():
    num1 = float(input("enter the first number for the calculations \n"))
    for i in operations:
        print(i)
    operation = input("choose an operator \n")
    num2 = float(input("enter the second number to perform the calculations \n"))
    function = operations[operation]
    answer = function(num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")
    reply = input('type "yes" to continue with the calculations with the same number, "no" to start new calculations and "end" to end the calculations \n')
    if reply == "end":
        return
    elif reply == "no":
        calculator()
    while reply =="yes":
        for i in operations:
            print(i)
        new_operator = input("enter another operator to continue the calculations \n")
        num3 = float(input("enter the next number \n"))
        function = operations[new_operator]
        new_answer = function(answer,num3)
        print(f"{answer} {new_operator} {num3} = {new_answer}")
        reply = input('type "yes" to continue with the calculations with the same number, "no" to start new calculations and "end" to end the calculations \n')
        if reply == "end":
            return
        elif reply == "no":
            calculator()
        if reply == "yes":
            answer = new_answer

calculator()

