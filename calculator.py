def numcheck():
        if "." in num1:
            num1conv = float(num1)
        else:
            num1conv = int(num1)
        if "." in num2:
            num2conv = float(num2)
        else:
            num2conv = int(num2)
        return num1conv, num2conv

def math(num1, symbol, num2): 

        if symbol == "+":
            total = num1 + num2
        elif symbol == "-":
            total = num1 - num2
        elif symbol == "*":
            total = num1 * num2
        elif symbol == "/":
            total = num1 / num2
        return total

def stop():
    print("all done!")
    exit()

memory = []
while True:
    print("enter your first number, or type stop to terminate, or type mem to pull previous numbers: " )
    num1 = input()
    if num1 == "stop":
        stop()
    elif num1 == "mem":  
        if not memory:
            print("There is nothing in memory!")
        else:
            print ("in memory are:", memory)
        continue
    print("mathematical symbol: ")
    symbol = input()
    if symbol == "stop":
         stop()
    print("enter second number: ")
    num2 = input()
    if num2 == "stop":
         stop()
    num1, num2 = numcheck()
    total = math(num1, symbol, num2)

    print(num1, symbol, num2, "is", total, "!")
    memory.append(total)







    