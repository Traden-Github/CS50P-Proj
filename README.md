# Basic Calculus Calculation System
    #### Video Demo:  https://youtu.be/7qUXj4B4CoU
    #### Description:
    **This is a program that enables user to perform basic calculations for Calculus

      For user:
        1. inputs choice of method (differentiation, indefinite integration, definite integration)
        2. inputs function
        3. confirm
        4. see result

      For programmer:
        1. imports _decimal module for revised floating point arithmetics_
        2. set precision, symbolic constants
        3. ***main*** defined: 1 prompt method, 2 prompt function, 3 output result
        4. ***prompt_user***, ***prompt_function*** defined: get method from user, stores function in a list of   dicts with "coefficient" and "power" as keys
        5. ***correct_function*** defined: to confirm user's function
        6. ***function_display*** defined: converts function list to a user-friendly function string
        7. ***differentiate***, ***indef_integrate***, ***def_integrate*** defined: to calculate the output using key, value pairs from function (for def_integrate gets additional arguments: top value and bottom value)

      Notes:
        1. function deals with polynomials with natural-number-powers only
        2. even with the decimal module, decimal values can still be estimations(rounded values), so it's best not to take the results as exact
        3. C represents arbitrary constant in indefinite integration
        4. tested for corner-cases/bugs for quite some time, though there might still be a few of them left

      Style choice:
        1. old-school procedural programming approach with some abstracted functions, some exceptions can be hard to read but is the most straightforward way of catching corner-cases from my point of view
        2. indented as the standard regulation for Python
        3. I was mainly focusing on optimizing user experience rather than that of the programmer, also I still need to learn more about how to be consistent with your style, so many stylistic changes might be needed in the future**
