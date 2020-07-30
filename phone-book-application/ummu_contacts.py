contact_dic = {"Ummu":8106,
 "Ozz":8099,
  "Aysu":2181,
   "Vili":9231,
   }
def find(name):
    name = name.title()
    return contact_dic.get(name,f"{name} is not in the phonebook")
def add(name ,number):
    name = name.title()
    if (name in contact_dic.keys()):
       if input(f"Are you sure you want to update {name} y/n: ").lower() == "y": 
           contact_dic[name] = number
           return f"Insterted name {name} with number {number} successfully"
       else:   
           if input("Would you like to add something to the end of name: ") == "y":
               name = name+input("What would you like to add :")
               contact_dic[name] = number
               return f"Inserted dublicate name {name} with number {number} successfully"
    else:
        contact_dic[name] = number
        return f"Updated name {name} with number {number} successfully"
def delete(name):
    name = name.title()
    if name in contact_dic.keys():
        if input(f"Are you sure you want to delete {name} y/n :").lower() == "y": 
            del contact_dic[name.title()]
            return f'Deleted name {name} successfully'
    else :
        return f"The name {name} is not in the list, try again"        
    #return  name not in contact_dic.keys()    
