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

    
    def modify_list(self, uinput):
        print(f"Here are the contents of {working_budget}: \n")
        for i in enumerate(working_budget):
            print(f"{i+1}. {working_budget}", end="")
        budgets.output()
        user_input = input("would you like to modify this list or add to it? (modify/add)")
        if user_input == "modify":
            budgets.modify_list(user_input)
            user_input == input("What would you like to remove? ")
            for i in enumerate(working_budget):
                if user_input == working_budget[i]:
                    working.budget.pop(i)
                    with open(working_budget, "w") as file:
                        print("List updated!")

    def view_files(self):
        for file in self.filepath:
            if file.endswith(".txt")
        print(file)
        
budgets = Budget()

while True:
    user_input = input("Hello, would you like to create a new budget or view/modify an existing one? (create or view): ")
    if user_input == "create":
        budgets.create_budget(user_input)
    elif user_input == "view":
        user_input = input(f"Which budget would you like to view?: {budgets.view_files}")
        with open(user_input, "r") as file:
            working_budget = file.readlines()
    else:   
        budgets.list_append(user_input)