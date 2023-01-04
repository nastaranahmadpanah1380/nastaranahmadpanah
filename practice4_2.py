products = []

def read_file():
    f = open("database.txt","r")
    for line in f:
        result=line.split(",")
        my_dic={"id":result[0],"name":result[1],"price":result[2],"count":result[3]}
        products.append(my_dic)



def add():
    new1_id=input("id: ")
    new1_name=input("name: ")
    new1_price=input("price: ")
    new1_count=input("count: ")
    new_dice={"id":new1_id,"name":new1_name,"price":new1_price,"count":new1_count}
    products.append(new_dice)
    print(new_dice)

def remove():
    idkey1=input("enter your key:")
    for product in products:
       if product["id"] == idkey1 or product["name"]== idkey1 :    
          products.remove(product)
          print("How many items do you want?")
          break

def search():
    idkey=input("enter your key:")
    for product in products:
        if product["id"] == idkey or product["name"]== idkey :
            print(product)
            break
    else:
        print("not found")

def edit():
    print("1-name_edit")
    print("2-price_edit")
    print("3-count-edit")

def name():
    idkey3=input("enter your key:")
    new_name=input("please enter new name")
    for product in products:
        if product["id"] == idkey3 or product["name"]== idkey3 : 
            product["name"]=new_name
            print(product)
            print("name is changed")
            break 


def price(): 
    idkey4=input("enter your key:")
    new_price=int(input("please enter new price"))
    for product in products:
        if product["id"] == idkey4 or product["name"]== idkey4 : 
            product["price"]=new_price
            print(product)
            print("price is changed")
            break 

def count(): 
    idkey5=input("enter your key:")
    new_count=int(input("please enter new count"))
    for product in products:
        if product["id"] == idkey5 or product["name"]== idkey5 : 
            product["count"]=new_count
            print(product)
            print("count is changed")
            break 

def show_list():
     print("id\nname\tprice\tcount")
     for product in products:
         print(product["id"],"\t",product["name"],"\t",product["price"],product["count"])



def buy():
    sabad_kharid=[]
    while True:
        moshtari=input("Do you want to buy?""yes or no")
        if moshtari=="yes":
            print("please enter ID or Name product name") 

        if moshtari=="no":
            exit()

        idkey2=input("enter your key:")

        for product in products:
            if product["id"] == idkey2 or product["name"] == idkey2:
                print(product)
                mo=int(input("how many items do you want?"))
                x=int(product['count'])
                y=int(product['price'])

                if x==0:
                    print("the inventory has reached zero")
                elif mo >= x:
                    print("your request is more than stock")
                elif x <= mo:
                    z=mo*y
                    print(z)
                    sabad_kharid.append(z)
                    print(sabad_kharid)

        else:
            print("Does not exist")

def show_menu():
    print("1-Add")
    print("2-Remove")
    print("3-Search")
    print("4-edit")
    print("5-show list")
    print("6-Buy")
    print("7-Exit")

read_file()

while True:
    show_menu()

    user_choice=int(input("enter your choice: "))

    if user_choice==1:
        add()
    elif user_choice==2: 
        remove()
    elif user_choice==3: 
        search()
    elif user_choice==4:
        edit() 
        user_choice_edit=int(input("enter your choice for edit: "))
        if user_choice_edit==1:
            name()
        elif user_choice_edit==2:
            price()
        elif user_choice_edit==3:
            count()
        else:
            print("please select another")  
    elif user_choice==5: 
        show_list()
    elif user_choice==6: 
        buy()
    elif user_choice==7:
        save=input("do you want save it? yes or no")
        if save=="yes":
            f = open("store.txt","w")
            for product in products:
                f.write(product["id"]+product["name"]+product["price"]+product["count"])
                f.write("\n")
                f.close() 


        exit()  



    else:
        print("please select another")  