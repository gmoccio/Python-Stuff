def calcbrains(): #the "brains" of the calculator where the user input is parsed through a series of if-else statements in a loop. The loop is necessary to prevent the program from closing after doing an equation
    while True:
        equation = input("enter your equation, clear to clear, or mem to pull memory: ")
        if equation == "stop":
            print("all done!")
            exit()
        elif equation == "mem":
            if not memory:
                print("there is nothing in memory!")
            else:
                print("In memory is: ", memory)
        elif equation == "clear":
            memory.clear()
            print("memory cleared!")        
            continue
        else:
            return equation #allows for equation to be accessed outside this function

def storage(equation): #The numbers and operaters the user inputs are then parsed through here, with equation being fed into this function
    equation = equation.split() #this takes user input and splits each part of it into a list, so 5 + 3 becomes [5, +, 3]
    numbers = []
    operators = []
    for i in equation:
        if i.isnumeric() or "." in i: #this if statment checks equation (which is now a list) to see which values are numerical and puts them in the newly created list numbers
            numbers.append(i)
        else:
            operators.append(i) #this does the same for the mathematical operators
    return numbers, operators #allows for these new lists to be available outside the function

def numcheck(numbers): #a function to determine whether or not the inputted numbers should be an integer (non-decimal) or a float (decimal)
    numparse = []
    for i in numbers: #if the number has a decimal, make it a float, or else make it an int and put it in numparse
        if "." in i:
            numparse.append(float(i))
        else:
            numparse.append(int(i))
    return numparse
    

def math(numparse, operators): #the "brains" of the calculator, basically just the logic of the arithmetic. because functions are self-contained, the parameters are necessary for the function to read things outside it
    runtot = numparse[0] 
    for num, op in zip(numparse[1:], operators): 
        if op == "+":                            
            runtot = runtot + num
        elif op == "-":
            runtot = runtot - num
        elif op == "*":
            runtot = runtot * num
        elif op == "/":
            runtot = runtot / num
    total = runtot
    return total

# here is where the main starts

memory = []
while True:
    equation = calcbrains()
    numbers, operators = storage(equation)
    numparse = numcheck(numbers)
    total = math(numparse, operators)
    print(total) #prints finalized answer in sentence format
    memory.append(total) #adds answer to calculator memory