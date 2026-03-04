
class List: #defines the list
    def __init__(self, list, flattened_list): #defining the variables in the code
        self.list = list #set list to be list
        self.flattened_list = flattened_list #same with flattened list

    def flatten(self, item): #def item parameter to pass list through
        if not isinstance(item, list): #if item is not a list
            self.flattened_list.append(item) #add it to flattened_list
        elif isinstance(item, list): #if the item is a list
            for i in item: #for every number that is a list
                self.flatten(i) #call the function again to move it outside the list


    

my_list = List([1, 2, 3, [4, [5, 6,]], 7, [8, 9]], []) #this is the way the outside looks into class List. the first list in this becomes self.list, the second becomes self.flattened list. 
                                                        #to call things in the list, you just do my_list.value or my_list.function because my_list acts as the "class outside the class" or the window into the house

my_list.flatten(my_list.list) #call function with the list

print(my_list.flattened_list) #print output



