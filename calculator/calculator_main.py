'''Impor the logo from a art file'''
from art import logo

print(logo)

'''Import the Regular Expression module to search in a string'''
import re

'''Import Operator module to simplify the math code'''
import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    ':': operator.truediv,  
    '*': operator.mul
}

accepted_inputs = ["0","1","2","3","4","5","6","7","8","9","+","-","/",":","*"," "]

def calculator():
    print('\nType "C" to clear the session or "end" to finish!\n')
    calculate = input("Calculating: ").strip()
    if "end" in calculate.lower():
        return
    calculating = True

    while calculating:
        if "c" in calculate.lower():
            calculator()
            calculating = False
        if "end" in calculate.lower():
            calculating = False
        try:
            pattern = r'(-?\d*\.?\d+)([\+\-\*/:])(-?\d*\.?\d+)'
            match = re.search(pattern,calculate)
            first_number = float(match.group(1))
            operation = match.group(2)
            second_number = float(match.group(3))
    
            if operation in operations:
                result = operations[operation](first_number, second_number)
                new_calculate = (input(f"{result} ").strip())
                calculate = (str(result) + new_calculate).strip()
            else:
                print("Invalid operation")
    
        except:
            print("Please make sure you type only numbers and +,-,/,:,* without white space")
            calculator()  


    

if __name__ == "__main__":
    calculator()