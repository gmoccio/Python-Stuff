def numcheck(): #a function to determine whether or not the inputted numbers should be an integer (non-decimal) or a float (decimal)
        if "." in num1: #basically says "if there is a decimal in the input of the first number, then make it a float, or else make it an integer"
            num1conv = float(num1)
        else:
            num1conv = int(num1)
        if "." in num2:
            num2conv = float(num2) #same thing for the second number
        else:
            num2conv = int(num2)
        return num1conv, num2conv #return allows the converted numbers to be called outside the function

def math(num1, symbol, num2): #the "brains" of the calculator, basically just the logic of the arithmetic 

        if symbol == "+":
            total = num1 + num2
        elif symbol == "-":
            total = num1 - num2
        elif symbol == "*":
            total = num1 * num2
        elif symbol == "/":
            total = num1 / num2
        return total #calls the total outside the function

def stop(): #function that allows for the app to close, mostly for me so I can close the app at anytime if I am testing particular logic 
    print("all done!")
    exit()

memory = [] #this is a list where the calculator memoery gets stored
while True: #this is a loop so the calculator stays on, if this was not here the program would end after the answer is given 
    print("enter your first number, or type stop to terminate, or type mem to pull previous numbers: " )
    num1 = input()
    if num1 == "stop": #if "stop" inputted, calls stop function
        stop()
    elif num1 == "mem":  
        if not memory: #should be self explanatory; if nothing in memory, say so, or show whats in memory
            print("There is nothing in memory!")
        else:
            print ("in memory are:", memory)
        continue #continue restarts the loop from top so that you do not have to repeat yourself constantly during this if else logic. Without this, you would have to re-type all the print and if statements after every elif and else
    print("mathematical symbol: ")
    symbol = input() #where you put whether you want to add, subtract, multiply, divide
    if symbol == "stop":
         stop()
    print("enter second number: ")
    num2 = input()
    if num2 == "stop":
         stop()
    num1, num2 = numcheck() #calls function numcheck to determine number type
    total = math(num1, symbol, num2) #calls function math and parameters for math to take place

    print(num1, symbol, num2, "is", total, "!") #prints finalized answer in sentence format
    memory.append(total) #adds answer to calculator memory

    #next steps in this: allow for equations to be inputted in one sentence opposed to line by line, allow for compound statments (9*9/81), allow for more complicated functions like remainders,







    