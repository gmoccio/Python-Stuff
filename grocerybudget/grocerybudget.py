from datetime import datetime
import os

#objectives: 
#1. make a grocery list take input for whether a new budget should be used or an existing one 2. allow each budget to be a readable txt file 3. allow budgets to be modifiable 4. name txt files Budget_MonthYear

class Budget:
    
    def __init__(self):
        self.store = []
        self.receipt = []
        self.total_spent = []
        self.budget = float()
        self.filepath = os.listdir("/home/gordon/projects/pythonstuff/grocerybudget")
        self.files = self.filepath


    def create_budget(self, uinput):
        now = datetime.now()
        month = now.strftime("%b")
        filename = f"Budget_{month}{now.strftime("%Y")}.txt"
        if filename in self.filepath:
            print("Budget already exists!")
        else:
            uinput = input("what is the budget you want to set for this month?: ")
            with open(filename, "w") as file:
                file.write(f"BUDGET: {uinput}")
            print("File created!")


    def list_append(self, money):
        self.store.append(money)
        if "." in i:
            self.total.append(float(i))
            
        print("list_append gg")
        self.math()
    
    def math(self):
        print("math ach")
        added_total = lambda receipt, total : [a + b for a, b in zip(self.receipt, self.total)]
        self.total_spent.append(added_total)
        print("math success")

    
    def modify_list(self, uinput, wbudg, file_map, filename):
        print(file_map)
        listnum = 0
        item_map = {}
        print(f"\nHere are the contents of {uinput}: ")
        for listnum, line, in enumerate(wbudg):
            listnum += 1
            print(f"{listnum}. {line}")
            item_map[listnum] = line
    
        uinput = input("would you like to add or remove something to this list? (add/remove): ")
        print(item_map)
        if uinput == "add":
            print(filename)
            while True:
                uinput = input("Add your purchases, or stop: ")
                if uinput == "stop":
                    break
                with open(filename, "a") as file:
                    file.write(uinput + "\n")
                    print("added!")
                
        elif uinput == "remove":
            while True:
                uinput = input("What would you like to remove, or stop: ")
                if uinput == "stop":
                    break
                uinput = int(uinput)
                if uinput in item_map:
                    wbudg.remove(item_map[uinput])
                    with open(file_map[1], "w") as file:
                        file.writelines(wbudg)
                        print("List updated!")

    def view_files(self, uinput):
        file_map = {}
        filenum = 0
        filename = None
        working_budget = None
        for file in self.filepath:
            if file.endswith(".txt"):
                filenum += 1
                print(f"{filenum}. {file}")
                file_map[filenum] = file
        uinput = int(input(f"Which budget would you like to load?: "))
        if uinput in file_map:
            filename = file_map[uinput]
            with open(file_map[uinput], "r") as file:
                working_budget = file.readlines()
                self.modify_list(file_map[uinput], working_budget, file_map, filename)
        else:
            print("Invalid Selection")
        return working_budget, file_map

budgets = Budget()

while True:
    user_input = input("Hello, would you like to create a new budget or load/modify an existing one? (create/load): ")
    if user_input == "create":
        budgets.create_budget(user_input)
    elif user_input == "load":
        budgets.view_files(user_input)
        
        
    #         
    #     user_input = input("would you like to modify this list?: ")
    #     if user_input == "yes":
    #         modify.list(uinput)
    # else:   
    #     budgets.list_append(user_input)