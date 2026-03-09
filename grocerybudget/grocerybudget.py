from datetime import datetime
import os

#objectives: 
#1. make a grocery list take input for whether a new budget should be used or an existing one 2. allow each budget to be a readable txt file 3. allow budgets to be modifiable 4. name txt files Budget_MonthYear

class Budget:
    
    def __init__(self):
        self.stores = []
        self.receipts = None
        self.total_spent = 0
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
    
   
        

    def view_files(self, uinput):
        file_map = {}
        filenum = 0
        filename = None
        for file in self.filepath:
            if file.endswith(".txt"):
                filenum += 1
                print(f"{filenum}. {file}")
                file_map[filenum] = file
        uinput = int(input(f"Which budget would you like to load?: "))
        if uinput in file_map:
            filename = file_map[uinput]
            with open(file_map[uinput], "r") as file:
                self.receipts = file.readlines()
            self.math()
            self.modify_list(file_map[uinput], file_map, filename)       
        else:
            print("Invalid Selection")
        return file_map


    def math(self):
        print(self.receipts)
        self.receipts
        for i in self.receipts:
            store, price = i.strip().split()
            self.stores.append(store)
            self.total_spent += float(price)
        print(self.stores)
        print(self.total_spent)



    def modify_list(self, uinput, file_map, filename):
        listnum = 0
        item_map = {}
        print(f"\nHere are the contents of {uinput}: ")
        for listnum, line, in enumerate(self.receipts):
            if line is None:
                print("Nothing in budget!")
            listnum += 1
            print(f"{listnum}. {line}")
            item_map[listnum] = line
    
        uinput = input("would you like to add or remove something to this list? (add/remove): ")
        if uinput == "add":
            print(filename)
            while True:
                uinput = input("Add your purchases, or stop: ")
                if uinput == "stop":
                    break
                with open(filename, "a") as file:
                    file.write(uinput + "\n")
                    print("added!")
                    self.receipts.append(uinput)
                    self.math()
                
        elif uinput == "remove":
            while True:
                uinput = input("What would you like to remove, or stop: ")
                if uinput == "stop":
                    break
                uinput = int(uinput)
                if uinput in item_map:
                    self.receipts.remove(item_map[uinput])
                    with open(file_map[1], "w") as file:
                        file.writelines(self.receipts)
                        print("List updated!")

budgets = Budget()

while True:
    user_input = input("Hello, would you like to create a new budget or load/modify an existing one? (create/load): ")
    if user_input == "create":
        budgets.create_budget(user_input)
    elif user_input == "load":
        budgets.view_files(user_input)
        
        
    