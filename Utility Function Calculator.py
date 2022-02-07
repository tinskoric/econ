# Utility Function Calculator

import sympy as sym

print('''Utility Function Calculator:

This tool will find the marginal rate of substitution (MRS) of a given utility function as well as give helpful 
definitions and tips related to the type of utility function at hand. To start, enter the letter (a,b,c, or d) that 
corresponds to the type of utility function at hand, here are some example forms of each function to help:

a) Linear Utility Function [U(x,y) = ax + by]
b) Quasi-Linear Utility Function [U(x,y) = x^a + by]
c) Cobb-Douglas Function [U(x,y) = x^a + y^b]
d) Leontief Function [U(x,y) = min{ax,by}]

Once the type of function at hand has been selected enter the values of a and b when prompted according to the example forms provided."
''')

x , y = sym.symbols('x y')

function_select = str(input("Select the type of utility function you are looking at:"))

if function_select == "a":

    print("Linear Utility Function [U(x,y) = ax + by]")

    function_a = float(input("Enter the value of a according to the example form:"))
    function_b = float(input("Enter the value of b according to the example form:"))

    MRS_linear = -function_a/function_b

    print(f'''
    Linear utility functions are easier than the others, the rule of thumb for them is that the MRS
    is just -a/b (given that the form of the function is U(x,y) = ax + by). So in this case, the MRS 
    of the function at hand is, -{function_a}/{function_b}. Linear utility functions imply that x 
    and y are perfect substitutes and have strong monotonicity, meaning that a change in either x 
    or y will impact how well off a given individual is.
    ''')

    print(f"MRS = {MRS_linear}")

elif function_select == "b":

    print("Quasi-Linear Utility Function [U(x,y) = x^a + by]")

    function_a = float(input("Enter the value of a according to the example form:"))
    function_b = float(input("Enter the value of b according to the example form:"))

    f = x**function_a + y*function_b

    dx = f.diff(x)
    dy = f.diff(y) 

    MRS_quasilinear = -dx/dy

    print(f'''
    Quasi-Linear utility functions look very similar to Cobb-Douglas functions but will have
    different substitution rates of substitution when calculated. Additionally, the function is
    only dependent on whichever variable is the one which is exponential in the expression.
    ''')

    print(f"MRS = {MRS_quasilinear}")

elif function_select == "c":

    print("Cobb-Douglas Function [U(x,y) = x^a + y^b]")

    function_a = float(input("Enter the value of a according to the example form:"))
    function_b = float(input("Enter the value of b according to the example form:"))
    
    f = x**function_a + y**function_b

    dx = f.diff(x)
    dy = f.diff(y) 

    MRS_Cobb_douglas = -dx/dy

    print(f'''
    Cobb-Douglas utility functions present bowed inward indifference curves, have a dimishing MRS,
    and have strong monotonicity, meaning that a change in either x or y will impact how well off 
    a given individual is.
    ''')

    print(f"MRS = {MRS_Cobb_douglas}")

elif function_select == "d":

    print("Leontief Function [U(x,y) = min{ax,by}]")

    function_a = float(input("Enter the value of a according to the example form:"))
    function_b = float(input("Enter the value of b according to the example form:"))

    point_leontief = function_a/function_b

    print(f'''
    Leontief functions imply that x and y are perfect compliments and thus there is no MRS
    for them however the points at which there is a corner in each L-shaped indifference curve
    formed by a Leontiev function can be defined by y = (a/b)x, thus, those points according to 
    the function at hand would be located at y = ({function_a}/{function_b})x. Leontief functions 
    have weak monotonicty because a change in *either* x or y does not impact how well of a given 
    individual is, which is what creates the L-shaped pattern of the indifference curves.
    ''')

    print(f"y={point_leontief}x")

else:

    print("Please renter the letter (a,b,c, or d) that corresponds to the utility function at hand.")