from datetime import datetime
import os

#objectives: 
#1. make a grocery list take input for whether a new budget should be used or an existing one 2. allow each budget to be a readable txt file 3. allow budgets to be modifiable 4. name txt files Budget_MonthYear

class Budget:
    
    def __init__(self):
        self.stores = []
        self.receipts = None
        self.total_spent = 0
        self.budget = None
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
                file.write(f"BUDGET: {uinput} \n")
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
                lines = file.readlines()
                result = next((line.replace("BUDGET: ", "").strip() for line in lines if line.startswith("BUDGET: ")), None) 
                self.budget = float(result) if result is not None else 0.0
                self.receipts = [line for line in lines if not line.startswith(("BUDGET: ", "TOTAL SPENT: ", "You are", "you are"))] #this was fixed last
                self.math()
                self.modify_list(file_map[uinput], file_map, filename)       
        else:
            print("Invalid Selection")
        return file_map


    def math(self):
        self.total_spent = 0
        self.stores = []
        for i in self.receipts:
            store, price = i.strip().rsplit(" ", 1)
            self.stores.append(store)
            self.total_spent += float(price)



    def modify_list(self, uinput, file_map, filename): #make this printed list show budget and total spent if the list already exists and contains it
        listnum = 0
        item_map = {}
        for listnum, line in enumerate(self.receipts):
            listnum += 1
            print(f"{listnum}. {line}")
            item_map[listnum] = line
        print(f"BUDGET: {self.budget}")
        with open (filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("TOTAL SPENT:"):
                    print(line)    
        uinput = input("would you like to add or remove something to this list? (add/remove): ")
        if uinput == "add":
            self.add_items(uinput, file_map, filename, item_map)
            return item_map
        elif uinput == "remove":
            self.remove_items(uinput, file_map, filename, item_map)
            return item_map




    def add_items(self, uinput, file_map, filename, item_map):
        while True:
            uinput = input("Add your purchases, or type remove to remove or stop to stop: ")
            if uinput == "stop":
                with open(filename, "a") as file:
                    file.write(f"TOTAL SPENT: {round(self.total_spent, 2)} \n")
                    if self.budget - self.total_spent > 100:
                        file.write(f"You are in Budget this month by {round(self.budget - self.total_spent, 2)}!")
                    elif abs(self.budget - self.total_spent) <= 100:
                        file.write(f"you are close to budget by {round(self.budget - self.total_spent, 2)}")
                    elif self.total_spent > self.budget:
                        file.write(f"You are over budget by {round(self.total_spent - self.budget, 2)}!")       
                break
            elif uinput == "remove":
                self.remove_items(uinput, file_map, filename, item_map)
            else:
                with open(filename, "a") as file:
                    file.write(uinput + "\n")
                    print("added!")
                    self.receipts.append(uinput)
                    print(f"before math: {self.receipts}")
                    self.math()
                    for listnum, line in enumerate(self.receipts):
                        if line.startswith(("BUDGET: ", "TOTAL SPENT: ", "you have", "You are")):
                            continue
                        listnum += 1
                        print(f"{listnum}. {line}")
                        item_map[listnum] = line
                    print(f"Total Spent: {self.total_spent}")
                    print(f"Total Budget: {self.budget}")
                    if self.budget - self.total_spent > 100:
                        print(f"You have {round(self.budget - self.total_spent, 2)} remaining!")
                    elif abs(self.budget - self.total_spent) <= 100:
                        print(f"You have {round(self.budget - self.total_spent, 2)} remaining!")
                        print("You are close to budget!")
                    elif self.total_spent > self.budget:
                        print(f"You are over budget by {round(self.total_spent - self.budget, 2)}!")

    def remove_items(self, uinput, file_map, filename, item_map):
        while True:
            listnum = 0
            item_map = {}
            for line in self.receipts:
                if line.startswith(("BUDGET: ", "TOTAL SPENT: ", "you have", "You are")):
                    continue
                listnum += 1
                print(f"{listnum}. {line}")
                item_map[listnum] = line
            uinput = input("What would you like to remove? Type add to add or stop to stop: ")
            if uinput == "stop":
                break
            elif uinput == "add":
                self.add_items(uinput, file_map, filename, item_map)
            else:
                uinput = int(uinput)
                if uinput in item_map:
                    self.receipts.remove(item_map[uinput])
                    with open(filename, "w") as file:
                        file.writelines(f"BUDGET: {self.budget} \n")
                        file.writelines(self.receipts)
                        print("List updated!")


budgets = Budget()

while True:
    budgets.__init__()
    user_input = input("Hello, would you like to create a new budget or load/modify an existing one? (create/load): ")
    if user_input == "create":
        budgets.create_budget(user_input)
    elif user_input == "load":
        budgets.view_files(user_input)
        
        
    