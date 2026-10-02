def print_main_menu():
    print(
"""
==============================
          TRACE 🔎
     Lost & Found Matcher
==============================

1. Report Lost Item
2. Report Found Item
3. Find Possible Match
4. View All Reports
5. Statistics
0. Exit

==============================
"""
)


def sys_main_menu():
    while True:
        print_main_menu()
        choice=input("Enter Your Choice : ")
        list_valid_choices=list(range(0,6))
        
        try:
            number = int(choice)
        except ValueError:
            print("Please enter a number!")
            continue

        if number in list_valid_choices:
            return number
        else:
            print("Wrong Choice!!!!!")
            print("Please Enter Valid Choice :-)")
       

##############################################

def report_lost_item():
    print("\n🔴 REPORT LOST ITEM\n")

    item_name = input("Item Name: ")
    category = input("Category: ")
    brand = input("Brand: ")
    color = input("Color: ")
    location = input("Location: ")
    date = input("Date: ")
    time = input("Time: ")
    description = input("Description: ")

    lost_item= {
        "item_name":item_name,
        "category":category,
        "brand":brand,
        "color":color,
        "location":location,
        "date":date,
        "time":time,
        "description":description
    }

    return lost_item


def save_lost_item(item):
    file=open("lost_items.txt","a")
    file.write(
        item["item_name"]+'|'+
        item["category"]+'|'+
        item["brand"]+'|'+
        item["color"]+'|'+
        item["location"]+'|'+
        item["date"]+'|'+
        item["time"]+'|'+
        item["description"]+'\n'
    )
    file.close()

##############################################


def report_found_item():
    print("\n🟢 REPORT FOUND ITEM\n")

    item_name = input("Item Name: ")
    category = input("Category: ")
    brand = input("Brand: ")
    color = input("Color: ")
    location = input("Location: ")
    date = input("Date: ")
    time = input("Time: ")
    description = input("Description: ")

    found_item= {
        "item_name":item_name,
        "category":category,
        "brand":brand,
        "color":color,
        "location":location,
        "date":date,
        "time":time,
        "description":description
    }

    return found_item

def save_found_item(item):
    file=open("found_items.txt","a")
    file.write(
        item["item_name"]+'|'+
        item["category"]+'|'+
        item["brand"]+'|'+
        item["color"]+'|'+
        item["location"]+'|'+
        item["date"]+'|'+
        item["time"]+'|'+
        item["description"]+'\n'
    )
    file.close()

##############################################

def read_items_from_file(file_name):
    items=[]

    file=open(file_name,"r")

    for line in file:
        item_as_list=line.strip().split("|")
        
        item_as_dic={
        "item_name":item_as_list[0],
        "category":item_as_list[1],
        "brand":item_as_list[2],
        "color":item_as_list[3],
        "location":item_as_list[4],
        "date":item_as_list[5],
        "time":item_as_list[6],
        "description":item_as_list[7]
        }

        items.append(item_as_dic)
    
    file.close()    
    
    return items    

def view_all_reports():
    
    lost_items=read_items_from_file("lost_items.txt")
    found_items=read_items_from_file("found_items.txt")

    if(len(lost_items)==0):
        print("No Lost Items !!!")
        return
    
    if(len(found_items)==0):
        print("No Found Items !!!")
        return

    print("="*50)
    print("🔴 LOST ITEMS")
    print("="*50)
    for item in lost_items:
        print("Item : ",item["item_name"])
        print("Category : ",item["category"])
        print("Brand : ", item["brand"])
        print("Color : ", item["color"])
        print("Location : ", item["location"])
        print("Date : ", item["date"])
        print("Time : ", item["time"])
        print("Description : ", item["description"])
        print("-"*50)

    print("="*50)
    print("🟢 FOUND ITEMS")
    print("="*50)
    for item in found_items:
            print("Item : ",item["item_name"])
            print("Category : ",item["category"])
            print("Brand : ", item["brand"])
            print("Color : ", item["color"])
            print("Location : ", item["location"])
            print("Date : ", item["date"])
            print("Time : ", item["time"])
            print("Description : ", item["description"])
            print("-"*50)    


##############################################

def calculate_match_score(lost_item,found_item):
    score=0
    if lost_item["item_name"].lower() == found_item["item_name"].lower():
        score += 25

    if lost_item["category"].lower() == found_item["category"].lower():
        score += 20

    if lost_item["brand"].lower() == found_item["brand"].lower():
        score += 15

    if lost_item["color"].lower() == found_item["color"].lower():
        score += 15

    if lost_item["location"].lower() == found_item["location"].lower():
        score += 15

    if lost_item["date"] == found_item["date"]:
        score += 10

    return score

def get_match_level(score):

    if score >= 90:
        return "Very Strong Match :-)"

    elif score >= 75:
        return "Strong Match"

    elif score >= 50:
        return "Possible Match"

    elif score >= 30:
        return "Weak Match"

    else:
        return "Unlikely Match :-("

def find_possible_match():
    
    lost_items=read_items_from_file("lost_items.txt")
    found_items=read_items_from_file("found_items.txt")

    if(len(lost_items)==0):
        print("No Lost Items !!!")
        return

    if(len(found_items)==0):
        print("No Found Items !!!")
        return
    print("-"*50)
    print("LOST ITEMS".center(50," "))
    print("-"*50)
    i=1
    for item in lost_items:
        print(f'{i} - {item["item_name"]} , {item["brand"]} , {item["color"]}')
        i+=1 

    lost_index_search_item=int(input("choose lost item : "))-1
    lost_item=lost_items[lost_index_search_item]

    no_matches=True

    for item in found_items:
        score=calculate_match_score(lost_item,item)
        matching_level=get_match_level(score)

        if score>=30:
            if not no_matches:
                no_matches=False
            print("-"*50)
            print(f"Found Item : {item["item_name"]}")
            print(f"Brand : {item["brand"]}")
            print(f"Color : {item["color"]}")
            print(f"Location : {item["location"]}")
            print(f"Date : {item["date"]}")
            print(f"Score : {score} / 100")
            print(f"Match Level : {matching_level}")

    if no_matches:
        print("Sorry There is No match with this Item :-( ")    

##############################################
        
def show_statics():
    lost_items=read_items_from_file("lost_items.txt")
    found_items=read_items_from_file("found_items.txt")

    if(len(lost_items)==0):
        print("No Lost Items !!!")
        return
    
    if(len(found_items)==0):
        print("No Found Items !!!")
        return

    
    print("-"*50)
    print("📊 TRACE STATISTICS".center(50," "))
    print("-"*50)
    print(f"Total Lost Items : {len(lost_items)}")
    print(f"Total Found Items : {len(found_items)}")
    print(f"Total Reports : {len(lost_items)+len(found_items)}\n")
    lost_catg={}
    found_catg={}

    for item in lost_items:
        category=item["category"]

        if category in lost_catg:
            lost_catg[category]+=1
        else:
            lost_catg[category]=1
    
    for item in found_items:
        category=item["category"]

        if category in found_catg:
            found_catg[category]+=1
        else:
            found_catg[category]=1

    print("Lost by Category : \n")
    for key,val in lost_catg.items():
        print(f"{key} : {val}")

    print("\nFound by Category : \n")
    for key,val in found_catg.items():
        print(f"{key} : {val}")


###############################################

def main_sys_func():
    while True: 
        choice=sys_main_menu()
        print("-="*25)
        if choice==1:
            save_lost_item(report_lost_item())
            print("="*50)
        
        elif choice==2:
            save_found_item(report_found_item())
            print("="*50)
        
        elif choice==3:
            find_possible_match()
            print("="*50)
        
        elif choice==4:
            view_all_reports()
            print("="*50)
        
        elif choice==5:
            show_statics()
            print("="*50)        
    
        elif choice==0:
            print("Good Bye".center(50," "))
            print("With My Best Wishes Eng : Ahmed Ali Said :-) ".center(50," "))
            break

        print("-="*25)
    
            
    
main_sys_func()    
    
    
    
    