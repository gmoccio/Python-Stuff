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

    
    def modify_list(self, uinput, wbudg):
        
        print(f"Here are the contents of {uinput}: \n")
        for index, line in enumerate(wbudg):
            print(f"{index+1}. {line}", end="\n")
    
        uinput = input("would you like to modify this list or add to it? (modify/remove): ")
        if uinput == "modify":
           pass
        elif uinput == "remove":
            input("What would you like to remove?: ")
            for index, line in enumerate(wbudg):
                if user_input == line:
                    wbudg.pop(index)
                    with open(uinput, "w") as file:
                        file.writelines(wbudg)
                        print("List updated!")

    def view_files(self):
        for file in self.filepath:
            if file.endswith(".txt"):
                print(file)
        
budgets = Budget()

while True:
    user_input = input("Hello, would you like to create a new budget or view/modify an existing one? (create or view): ")
    if user_input == "create":
        budgets.create_budget(user_input)
    elif user_input == "view":
        budgets.view_files()
        user_input = input(f"Which budget would you like to view?: ")
        with open(user_input, "r") as file:
            working_budget = file.readlines()
        budgets.modify_list(user_input, working_budget)
        
    #         
    #     user_input = input("would you like to modify this list?: ")
    #     if user_input == "yes":
    #         modify.list(uinput)
    # else:   
    #     budgets.list_append(user_input)