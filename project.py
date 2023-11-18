# Basic Calculus Calculation System
from decimal import *
getcontext().prec = 5

DIFFERENTIATION = 1
INDEFINITE_INTEGRATION = 2
DEFINITE_INTEGRATION = 3

def main():
    print("                        ~~~Basic Calculus Calculation System~~~\n")
    print("--------CAUTION: Numbers will be rounded for decimal arithmetics(precision: 5 digits)--------")
    print("Use this program with this in mind(don't take decimals suffixed with non-zero value as exact!)\n")
    mode = prompt_user()
    function = prompt_function()
    if mode == DIFFERENTIATION:
        print(f"The differentiated function: {differentiate(function)}")
    if mode == INDEFINITE_INTEGRATION:
        print(f"The indefinite integrated function: {indef_integrate(function)}")
    if mode == DEFINITE_INTEGRATION:
        print("---Enter the range definition---")
        while True:
            try:
                bot = float(input("From(bottom value)? "))
                top = float(input("To(top value)? "))
                break
            except ValueError:
                print("Invalid range value, please try again")
        print(f"The value of definite integration of the function(roughly): {def_integrate(function, bot, top)}")

def prompt_user():
    print("    Please Choose Calculation Mode By Entering The Numbers Below:\n")
    print("Differentiation--1   Indefinite Integration--2   Definite Integration--3\n")
    while True:
        try:
            choice = int(input("Your choice? "))
        except ValueError:
            print("Invalid choise, please try again")
            continue
        else:
            if choice in [DIFFERENTIATION, INDEFINITE_INTEGRATION, DEFINITE_INTEGRATION]:
                return choice
            print("Invalid choice, please try again")

def prompt_function():
    while True:
        try:
            degree = int(input("Degree of polynomial: "))
        except ValueError:
            print("Invalid degree, please try again")
            continue
        if degree < 0:
            print("Invalid degree, please try again")
            continue
        function = []
        power = degree
        degreeTest = True
        for _ in range(degree+1):
            while True:
                match power:
                    case 1:
                        rank = "1st"
                    case 2:
                        rank = "2nd"
                    case 3:
                        rank = "3rd"
                    case _:
                        rank = f"{power}th"
                co_value = input(f"What's the coefficient of the {rank} degree? ")
                try:
                    if float(co_value) == 0.0 and power == degree and degree != 0:
                        print(f"This isn't a {degree}th degree function, please try again")
                        degreeTest = False
                        break
                    function.append({"co": float(co_value), "power": power})
                    power -= 1
                    break
                except ValueError:
                    print("Invalid coefficient, please try again")
            if degreeTest == False:
                break
        if degreeTest == False:
            continue
        print(f"Your function is f(x)={function_display(function, degree)}, correct? ", end="")
        if correct_function():
            return function
        else:
            print("Enter the polynomial again, please")
            pass

def correct_function():
    while True:
        y_or_n = input("Enter Y/y if yes, N/n if no: ")
        if y_or_n.lower() == "y":
            return True
        if y_or_n.lower() == "n":
            return False
        print("Decision invalid")

def function_display(dictList, degree):
    function = ""
    power = degree
    for dict in dictList:
        if dict["co"] == 0 and degree == 0:
            return "0"
        if dict["co"] == 0:
            power -= 1
            continue
        if power == degree:
            if power != 1 and power != 0:
                if dict["co"] != 1:
                    function += f"{dict["co"]}x^{power}"
                else:
                    function += f"x^{power}"
            if power == 1:
                if dict["co"] != 1:
                    function += f"{dict["co"]}x"
                else:
                    function += "x"
            if power == 0:
                function += f"{dict["co"]}"
            power -= 1
            continue
        if power > 1:
            if dict["co"] > 0:
                if dict["co"] == 1:
                    function += f"+x^{power}"
                else:
                    function += f"+{dict["co"]}x^{power}"
            if dict["co"] < 0:
                function += f"{dict["co"]}x^{power}"
        if power == 1:
            if dict["co"] > 0:
                function += f"+{dict["co"]}x"
            if dict["co"] < 0:
                function += f"{dict["co"]}x"
        if power == 0:
            if dict["co"] == None and len(dictList) == 2:
                function += "C"
            elif dict["co"] == None:
                function += "+C"
                break
            elif dict["co"] > 0:
                function += f"+{dict["co"]}"
            else:
                function += f"{dict["co"]}"
        power -= 1
    return function

def differentiate(f):
    f_prime = []
    Count = 0
    for element in f:
        if element["power"] == 0 and len(f) == 1:
            return 0
        if element["power"] == 0 and len(f) > 1:
            Count += 1
            break
        co = Decimal(str(Decimal(element["co"]) * Decimal(element["power"])))
        power = element["power"] - 1
        f_prime.append({"co": co, "power": power})
        Count += 1
    return f"f'(x)={function_display(f_prime, Count-2)}"

def indef_integrate(f):
    f_sum = []
    Count = 0
    for element in f:
        power = element["power"] + 1
        co = Decimal(str(Decimal(element["co"]) / power))
        f_sum.append({"co": co, "power": power})
        Count += 1
    f_sum.append({"co": None, "power": 0})
    return f"∫f(x)dx={function_display(f_sum, Count)}"

def def_integrate(f, b, t):
    b_of_x = 0
    t_of_x = 0
    for element in f:
        power = element["power"] + 1
        co = Decimal(str(Decimal(element["co"]) / power))
        b_of_x += co*Decimal(pow(b, power))
        t_of_x += co*Decimal(pow(t, power))
    return Decimal(t_of_x-b_of_x)

if __name__ == "__main__":
    main()
