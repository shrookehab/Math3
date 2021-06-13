# import product procedure (function) to generate truth table values
from itertools import product

# read line and convert to int
vars_num = int(input("Please enter the number of variables :  "))
# read line and split to list ex: p q r => [p, q, r]
variables = input("Please enter the variables :  ").split()
# read proposition line
prop = input("Please enter the Proposition :  ")

for var in variables:
    print(var, end=" | ")  # print variable and add " | " to the end

print(prop)  # print proposition and new line

'''
replace every operator
ex:
iff    ==
imply, implies <=
xor    ^
'''
prop = prop.replace("iff", "==")
prop = prop.replace("imply", "<=")
prop = prop.replace("implies", "<=")
prop = prop.replace("xor", "^")

'''
product(("True", "False"), repeat=vars_num)
generates all possible combinations of True and False with length equals to variables number
ex: number = 3, vars = [p, q, r]
generates
(True, True, True)
(True, True, False)
(True, False, True)
(True, False, False)
(False, True, True)
(False, True, False)
(False, False, True)
(False, False, False)
'''
for combination in product(("True", "False"), repeat=vars_num):
    p = prop
    for i in range(vars_num):  # loop from 0 to vars_num
        print(combination[i][0], end=" | ")  # print the first char of boolean value
        '''
        replace every variable with its value

        wrong way:
        if we replace every variable called n with its value which is True as an example directly
        variable op will be also affected : on => oTrue
        and operator not will be affected : not => Trueot

        right way:
        using regex (regular expressions) but we didn't study it yet

        another way:
        replace all variable representations
        the var can be started with ( and end with space like "(p "
        or starts with space and ends with ) like " var)"
        or start and end with spaces like " test "
        '''
        p = p.replace("(" + variables[i] + " ", "(" + combination[i] + " ")
        p = p.replace(" " + variables[i] + ")", " " + combination[i] + ")")
        p = p.replace(" " + variables[i] + " ", " " + combination[i] + " ")
    print(str(eval(p))[0])  # convert output to string and print the first char only
