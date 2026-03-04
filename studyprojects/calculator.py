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


def numcheck(equation): #a function to determine whether or not the inputted numbers should be an integer (non-decimal) or a float (decimal)
    print("numparse reached")
    placeholder = equation.split()
    numparse = []
    for i in placeholder: #if the number has a decimal, make it a float, or else make it an int and put it in numparse
        if "." in i:
            numparse.append(float(i))
        elif i.isnumeric():
            numparse.append(int(i))
        else:
            numparse.append(i)
    print(numparse)
    print("numparse success")
    return numparse
    

def math(numparse): #the "brains" of the calculator, basically just the logic of the arithmetic. because functions are self-contained, the parameters are necessary for the function to read things outside it 
    print("math achieved")
    for index, i in enumerate(numparse):
        if i == "*":
            numparse.append(numparse[index-1] * numparse[index+1])
        if i == "/":
            numparse.append(numparse[index-1] / numparse[index+1])
        if i == "+":
            numparse.append(numparse[index-1] + numparse[index+1])
        if i == "-":
            numparse.append(numparse[index-1] - numparse[index+1])
    print("successful mathing")
    return numparse

# here is where the main starts

memory = []
while True:
    equation = calcbrains()
    numparse = numcheck(equation)
    total = math(numparse)
    print(total) #prints finalized answer in sentence format
    memory.append(total) #adds answer to calculator memory