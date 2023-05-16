Menu = {
    "COFEE" : {
      "Tea"        : 10.0,
      "Cofee"      : 22.5,
      "MOCHA"      : 25.0,
      "CAPPUCCINO" : 23.5
    },

    "DESSERT" :{
        "RED VELVET CAKE" : 25.0,
        "CHEESE CAKE"     : 27.5,
        "CHOCOLATE CAKE"  : 28.0,
        "CUP CAKE"        : 21.5
    },

    "FRESH JUICE" :{
        "ORANGE" : 15.0 ,
        "BANANA" : 15.0 ,
        "CARROT" : 15.0 ,
        "APPLE"  : 15.0 
    }
}

#List To Store The Order
Order = []

def Display_Menu():
    for Headers in Menu:
        print("_______________________________________________")
        print(f"{Headers} In Menu Include These Items : ")
        print("_______________________________________________")
        for Item in Menu[Headers] :
            print(f"{Item} Is : {Menu[Headers][Item]} EGP")


def Add_Order(item):
    Order.append(item)
    print("**************************************")
    print(item + " Added To The Order.")
    print("**************************************")


def Remove_Order(item):
    if item in Order:
        Order.remove(item)
        print("**************************************")
        print(item + " Removed From The Order.")
        print("**************************************")
    else:
        print("**************************************")
        print(item + " Is Not In The Order.")
        print("**************************************")



def view_order():
    if len(Order) == 0:
        print("**************************************")
        print("There Are No Items In The Order.")
        print("**************************************")
    else:
        total_Price = 0
        for item in Order:
            for items in Menu.values():
              if item in items:        
                total_Price += int(items[item])
                print(item + "->" + str(items[item]))
               
        print("------------------------------------")        
        print(f"-Total Price Is : {total_Price} EGP-" )
        print("------------------------------------")


while True:
    print("-------------Welcome In ITI Cafee-------------")
    print("      1. Display Menu")
    print("      2. Make Item In Your Order")
    print("      3. Remove Item From Your Order")
    print("      4. View Your Order")
    print("      5. Exit")

    choice = input("Enter Your Choice...")
    if  choice == '1':
        Display_Menu()

    elif choice == '2':
        item = input("Enter The Item Want To Add : ")
        Add_Order(item)

    elif choice == '3':
        item = input("Enter The Item Want To Remove : ")
        Remove_Order(item)

    elif choice == '4':
        view_order()

    elif choice == '5':
        print("Thank you for using the cafe management system!")
        break

    else:
        print("Invalid choice. Please try again.")
