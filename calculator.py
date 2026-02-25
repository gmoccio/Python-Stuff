def numcheck(numbers): #a function to determine whether or not the inputted numbers should be an integer (non-decimal) or a float (decimal)
   for i in numbers:
    if "." in i:
         numparse = [float(i) for i in numbers]
    else:
        numparse = [int(i) for i in numbers]
    return numparse

def math(numparse, operators): #the "brains" of the calculator, basically just the logic of the arithmetic. because functions are self-contained, the parameters are necessary for the function to read things outside it
    runtot = numparse[0]
    for num, op in zip(numparse[1:], operators):
        if op[0] == "+":
            runtot = runtot + num[1]
        elif op[0] == "-":
            runtot = runtot - num[1]
        elif op[0] == "*":
            runtot = runtot * num[1]
        elif op[0] == "/":
            runtot = runtot / num[1]
    total = runtot
    return total


    

def stop(): #function that allows for the app to close, mostly for me so I can close the app at anytime if I am testing particular logic 
    print("all done!")
    exit()

memory = [] #this is a list where the calculator memoery gets stored



while True:
    equation = input("enter your first number, or type stop to terminate, or type mem to pull previous numbers: ")
    if equation == "stop":
        stop()
    elif equation == "mem":
        if not memory:
            print("there is nothing in memory!")
        else:
            print("In memory is: ", memory)
        continue
    equation = equation.split()
    numbers = []
    operators = []

    for i in equation:
        if i.isnumeric():
            numbers.append(i)
            numbers = numcheck(numbers)
        else:
            operators.append(i)


     #calls function numcheck to determine number type
    total = math((numparse, operators)) #calls function math and parameters for math to take place

    print(total) #prints finalized answer in sentence format
    memory.append(total) #adds answer to calculator memory

    #next steps in this: allow for equations to be inputted in one sentence opposed to line by line, allow for compound statments (9*9/81), allow for more complicated functions like remainders,



 #original math function

        # if symbol == "+":
        #     total = num1 + num2
        # elif symbol == "-":
        #     total = num1 - num2
        # elif symbol == "*":
        #     total = num1 * num2
        # elif symbol == "/":
        #     total = num1 / num2
        # return total #calls the total outside the function

 #numcheck for the new equation variable
 # for i in num1:
    #     if "." in num1: 
    #         num1conv = float(num1)
    #     else:
    #         num1conv = int(num1)
    # for i in num2:
    #     if "." in num2:
    #         num2conv = float(num2) #same thing for the second number
    #     else:
    #         num2conv = int(num2)
    #     return num1conv, num2conv


    #original numcheck function body

     
    #  if "." in num1: 
    #         num1conv = float(num1)
    #     else:
    #         num1conv = int(num1)
    #     if "." in num2:
    #         num2conv = float(num2) #same thing for the second number
    #     else:
    #         num2conv = int(num2)
    #     return num1conv, num2conv  #return allows the converted numbers to be called outside the function
         


    #original entrance of values

    
# while True: #this is a loop so the calculator stays on, if this was not here the program would end after the answer is given 
#     print("enter your first number, or type stop to terminate, or type mem to pull previous numbers: " )
#     num1 = input()
#     if num1 == "stop": #if "stop" inputted, calls stop function
#         stop()
#     elif num1 == "mem":  
#         if not memory: #should be self explanatory; if nothing in memory, say so, or show whats in memory
#             print("There is nothing in memory!")
#         else:
#             print ("in memory are:", memory)
#         continue #continue restarts the loop from top so that you do not have to repeat yourself constantly during this if else logic. Without this, you would have to re-type all the print and if statements after every elif and else
#     print("mathematical symbol: ")
#     symbol = input() #where you put whether you want to add, subtract, multiply, divide
#     if symbol == "stop":
#          stop()
#     print("enter second number: ")
#     num2 = input()
#     if num2 == "stop":
#          stop()
#          """