import csv
import pandas as pd

print('''********** Welcome to Shopping ******* See the below Choice
          choice1:Display Menu Items
          choice2:Add the Item to Cart
          choice3:Remove the Item from Cart
          choice4:View the Purchased Items
          choice5:Invoice
          Choice6:Exit
   ''')




class Shopping:
    stock_items= {}
    price = 0
    final_product = []
    final_price = []
    final_quantity =[]
    def AddItems():

        Itemlist = {"Maggi": 45, "Butter": 120, "Biscuit": 20, "Sunflower oil": 180}
        continue_to_cart = "yes"
        total_price =0
        while continue_to_cart:
            sel_item = input("Enter the Item:\n")
            sel_item = sel_item.capitalize()
            sel_qty = int(input("Enter the Quantity:\n"))
            item_price = 0
            for items in Itemlist:
                if sel_item == items:
                    item_price = Itemlist[items] * sel_qty
            total_price += item_price
            Shopping.stock_items[sel_item] = [sel_qty, item_price]
            print(f"Selected Item is {sel_item} and the price of the item is {item_price} ")
            sel_cont = input("Are you want to Continue: Yes/ No \n")
            if sel_cont.capitalize() == "Yes":
                continue_to_cart = 1
            else:
                continue_to_cart = 0
                print(f"Total Price for the selected Items: {total_price}")
        print(Shopping.stock_items)

        Shopping.choose_choice()


    def displaymenu():
        with open("vin.csv") as file:
            item_list = file.readlines()
            for row in item_list:
                print(row)
        Shopping.choose_choice()

    def choose_choice():
        choice = int(input("Enter the Choice: \n"))
        if choice == 1:
            Shopping.displaymenu()
        elif choice == 2:
            Shopping.AddItems()
        elif choice == 4:
            Shopping.remove()
        elif choice == 5:
            Shopping.invoice()
        elif choice == 6:
            exit()
        else:
            print("Invalid choice")

    def remove():

        rem_item = input("enter the item to be removed from the Cart: \n")
        rem_item = rem_item.capitalize()
        Shopping.stock_items.pop(rem_item)
        print(f"Items for Billing :{Shopping.stock_items}")
        Shopping.choose_choice()

    def invoice():
        for row in Shopping.stock_items:
            Shopping.price += Shopping.stock_items[row][1]
            Shopping.final_product.append(row)
            Shopping.final_quantity.append(Shopping.stock_items[row][0])
            Shopping.final_price.append(Shopping.stock_items[row][1])

        final_data=pd.DataFrame({"Product":Shopping.final_product, "Quantity" :Shopping.final_quantity,"Price":Shopping.final_price })
        final_data.to_csv("invoice.csv", index=False)
        print(final_data)
        print (f"Total Amount: {Shopping.price}")

Shopping.choose_choice()




