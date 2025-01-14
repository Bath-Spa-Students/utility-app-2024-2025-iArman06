from tabulate import tabulate #to make tables

#printing a welcome message for the vending machine
print("ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ")
print("ωєℓ¢σмє тσ αямαη'ѕ νєη∂ιηg мα¢нιηє")




#printing snacks
def snacks() : 
    print("====================ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ====================")
    print("====================S N A C K S=======================================")
    snacks = [
        ["01" ,  "Mixed Nuts"           , "AED 2.50" ],               # snack section in order of "Item Code","Item Name","Item Price".
        ["02" ,  "Popcorn"              , "AED 4.50" ],
        ["03" ,  "Oat Meal"             , "AED 5.50" ],
        ["04" ,  "Protein Bar"          , "AED 9.50" ],
        ["05" ,  "Yogurt"               , "AED 3.50" ],
        ["06" ,  "Biscuits"             , "AED 5.50" ],
        ["07" ,  "Salsa"                , "AED 10.50"],
        ["08" ,  "Mixed Fruits Platter" , "AED 5.50" ],
        ["09" ,  "White Sauce Pasta"    , "AED 10.00"],
        ["10" ,  "Red Sauce Pasta"      , "AED 10.50"]
    ]
    
    
    print(tabulate(snacks, headers=["Code","Item Name","Price (in AED)"],tablefmt="fancy_grid"))

#printing chips
def chips() : 
    print("====================ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ====================")
    print("====================C H I P S========================================")
    chips = [
        ["11" ,  "Doritos"             ,  "AED 3.50" ],                # chips section in order of "Item Code","Item Name","Item Price".
        ["12" ,  "Lays"                ,  "AED 1.50" ],
        ["13" ,  "Fins"                ,  "AED 6.50" ],
        ["14" ,  "Buggles (small)"     ,  "AED 0.50" ],
        ["15" ,  "Cheetos"             ,  "AED 5.50" ],
        ["16" ,  "Kurkure"             ,  "AED 5.00" ],
        ["17" ,  "Pringles"            ,  "AED 10.00"],
        ["18" ,  "Mr. Krisps"          ,  "AED 2.50" ],
        ["19" ,  "Takis"               ,  "AED 9.50" ],
        ["20" ,  "Bingo"               ,  "AED 5.50" ]
    ]
    
    print(tabulate(chips, headers=["Code","Item Name","Price (in AED)"],tablefmt="fancy_grid"))

#printing drinks
def drinks() : 
    print("====================ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ====================")
    print("====================D R I N K S========================================")
    drinks = [
        ["21" ,  "Water"               ,  "AED 1.50" ],               # drinks section in order of "Item Code","Item Name","Item Price".
        ["22" ,  "Cream Soda"          ,  "AED 3.68" ],
        ["23" ,  "Fanta"               ,  "AED 2.50" ],
        ["24" ,  "Mountain Dew"        ,  "AED 3.00" ],
        ["25" ,  "Thumbs Up"           ,  "AED 2.50" ],
        ["26" ,  "Red Bull"            ,  "AED 10.00"],
        ["27" ,  "Coca Cola"           ,  "AED 4.00" ],
        ["28" ,  "Sprite"              ,  "AED 2.50" ],
        ["29" ,  "Pepsi"               ,  "AED 3.50" ],
        ["30" ,  "Miranda"             ,  "AED 3.50" ]
    ]
    
    print(tabulate(drinks, headers=["Code","Item Name","Price (in AED)"],tablefmt="fancy_grid"))

#printing chocolates
def chocolates() : 
    print("====================ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ====================")
    print("====================C H O C O L A T E S========================================")
    chocolates = [
        ["31" , "Snickers"             ,  "AED 3.50" ],             # chocolates section in order of "Item Code","Item Name","Item Price".
        ["32" , "Mars"                 ,  "AED 1.50" ],
        ["33" , "Toblerone"            ,  "AED 6.50" ],
        ["34" , "Fix"                  ,  "AED 5.00" ],
        ["35" , "Break"                ,  "AED 3.50" ],
        ["36" , "Lindor"               ,  "AED 5.00" ],
        ["37" , "Galaxy"               ,  "AED 3.00" ],
        ["38" , "Dairy Milk"           ,  "AED 4.50" ],
        ["39" , "Feastables"           ,  "AED 35.00"],
        ["40" , "Hershey's"            ,  "AED 3.75" ]
    ]
    
    print(tabulate(chocolates, headers=["Code","Item Name","Price (in AED)"],tablefmt="fancy_grid"))

#printing healthy_snacks
def healthy_snacks() : 
    print("====================ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ====================")
    print("====================H E A L T H Y=======================================")
    healthy_snacks = [
        ["41" , "Oats Bar"                  ,  "AED 1.50" ],          # healthy snacks section in order of "Item Code","Item Name","Item Price".
        ["42" , "Mixed Salads"              ,  "AED 10.00"],
        ["43" , "Apple"                     ,  "AED 2.50" ],
        ["44" , "Garlic Paste"              ,  "AED 7.50" ],
        ["45" , "Veggies and Chicken plater",  "AED 10.00"],
        ["46" , "Granola Bar"               ,  "AED 4.50" ],
        ["47" , "Trail Mix"                 ,  "AED 6.00" ],
        ["48" , "Rice Cakes"                ,  "AED 3.50" ],
        ["49" , "Hummus with Veggies"       ,  "AED 7.50" ],
        ["50" , "Fruit Cup"                 ,  "AED 5.00" ]
    ]
    
    print(tabulate(healthy_snacks, headers=["Code","Item Name","Price (in AED)"],tablefmt="fancy_grid"))

#printing combo_meals
def combo_meals() : 
    print("====================ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ====================")
    print("====================C O M B O=======================================")
    combo_meals = [
        ["51" , "Chips + Drink"                  ,  "AED 4.50" ],       # combo meals section in order of "Item Code","Item Name","Item Price".
        ["52" , "Chocolate + Drink"              ,  "AED 5.50" ],
        ["53" , "Snacks + Drink"                 ,  "AED 8.00" ],
        ["54" , "Healthy Snack + Orange Juice"   ,  "AED 10.00"],
        ["55" , "Oats + Milk"                    ,  "AED 10.50"],
        ["56" , "Cold Sandwich + Pepsi"          ,  "AED 19.50"],
        ["57" , "White Sauce Pasta + Water"      ,  "AED 10.00"],
        ["58" , "Grill platter + Garlic Paste"   ,  "AED 15.00"],
        ["59" , "French Fries + Ketchup"         ,  "AED 5.50" ],
        ["60" , "Doritos + Salsa"                ,  "AED 10.50"]
    ]
        
    print(tabulate(combo_meals, headers=["Code","Item Name","Price (in AED)"],tablefmt="fancy_grid"))

#printing desserts
def desserts() : 
    print("====================ＶＥＮＤＩＮＧ　ＭＡＣＨＩＮＥ====================")
    print("====================D E S S E R T S=======================================")
    desserts = [
        ["61" , "Chocolate Cake"         ,  "AED 10.00" ],             # desserts section in order of "Item Code","Item Name","Item Price".
        ["62" , "Brownies"               ,  "AED 10.50" ],
        ["63" , "Donut"                  ,  "AED 1.50"  ],
        ["64" , "Cupcake"                ,  "AED 3.50"  ],
        ["65" , "Ice Cream"              ,  "AED 5.00"  ],
        ["66" , "Lava Cake"              ,  "AED 8.00"  ],
        ["67" , "Cookies"                ,  "AED 1.00"  ],
        ["68" , "Falooda"                ,  "AED 12.00" ],
        ["69" , "Cold Coffee"            ,  "AED 15.00" ],
        ["70" , "Caramel Custard"        ,  "AED 5.00"  ]
    ]
        
    print(tabulate(desserts, headers=["Code","Item Name","Price (in AED)"],tablefmt="fancy_grid"))


#listed below are all the sections of the vending machine
#using the dictionary method to map the numbers to the corresponding sections
sections = {
    "1": snacks,
    "2": chips,
    "3": drinks,
    "4": chocolates,
    "5": healthy_snacks,
    "6": combo_meals,
    "7": desserts,
}


def get_item_by_code(section_items):
    while True:
        # Ask the user to enter an item code or quit
        item_code = input("\nEnter the item code to purchase (or 'q' to quit): ").strip()
        
        if item_code.lower() == 'q':  # Allow the user to quit
            print("Thank you for using the vending machine! Have a great day!")
            break
        
        # Search for the item in the section
        for item in section_items:
            if item[0] == item_code:
                print(f"\nYou selected: {item[1]} - {item[2]}")
                return

        print("Invalid code. Please try again.")



 # Displaying the menu when the program runs so the user can choose from the list
 #using main functio
def main():
    print("\nChoose a section to Display and Proceed :")
    print("1 - Snacks")           #section 1
    print("2 - Chips")            #section 2
    print("3 - Drinks")           #section 3
    print("4 - Chocolates")       #section 4
    print("5 - Healthy Snacks")   #section 5
    print("6 - Combo Meals")      #section 6
    print("7 - Desserts")         #section 7

  # Asking the user for their choice
    choice = input("\nEnter your choice from (1-7): ").strip()  # The user will enter a number corresponding to the section

    # Using a dictionary to map sections to their respective item lists
    items_menu = {
        "1": [
                ["01" ,  "Mixed Nuts"           , "AED 2.50" ],               # snack section in order of "Item Code","Item Name","Item Price".
        ["02" ,  "Popcorn"              , "AED 4.50" ],
        ["03" ,  "Oat Meal"             , "AED 5.50" ],
        ["04" ,  "Protein Bar"          , "AED 9.50" ],
        ["05" ,  "Yogurt"               , "AED 3.50" ],
        ["06" ,  "Biscuits"             , "AED 5.50" ],
        ["07" ,  "Salsa"                , "AED 10.50"],
        ["08" ,  "Mixed Fruits Platter" , "AED 5.50" ],
        ["09" ,  "White Sauce Pasta"    , "AED 10.00"],
        ["10" ,  "Red Sauce Pasta"      , "AED 10.50"],
        ],
        "2": [
                ["11" ,  "Doritos"             ,  "AED 3.50" ],                # chips section in order of "Item Code","Item Name","Item Price".
        ["12" ,  "Lays"                ,  "AED 1.50" ],
        ["13" ,  "Fins"                ,  "AED 6.50" ],
        ["14" ,  "Buggles (small)"     ,  "AED 0.50" ],
        ["15" ,  "Cheetos"             ,  "AED 5.50" ],
        ["16" ,  "Kurkure"             ,  "AED 5.00" ],
        ["17" ,  "Pringles"            ,  "AED 10.00"],
        ["18" ,  "Mr. Krisps"          ,  "AED 2.50" ],
        ["19" ,  "Takis"               ,  "AED 9.50" ],
        ["20" ,  "Bingo"               ,  "AED 5.50" ],
        ],
        "3": [
                ["21" ,  "Water"               ,  "AED 1.50" ],               # drinks section in order of "Item Code","Item Name","Item Price".
        ["22" ,  "Cream Soda"          ,  "AED 3.68" ],
        ["23" ,  "Fanta"               ,  "AED 2.50" ],
        ["24" ,  "Mountain Dew"        ,  "AED 3.00" ],
        ["25" ,  "Thumbs Up"           ,  "AED 2.50" ],
        ["26" ,  "Red Bull"            ,  "AED 10.00"],
        ["27" ,  "Coca Cola"           ,  "AED 4.00" ],
        ["28" ,  "Sprite"              ,  "AED 2.50" ],
        ["29" ,  "Pepsi"               ,  "AED 3.50" ],
        ["30" ,  "Miranda"             ,  "AED 3.50" ],
    ],
    "4": [
                 ["31" , "Snickers"             ,  "AED 3.50" ],             # chocolates section in order of "Item Code","Item Name","Item Price".
        ["32" , "Mars"                 ,  "AED 1.50" ],
        ["33" , "Toblerone"            ,  "AED 6.50" ],
        ["34" , "Fix"                  ,  "AED 5.00" ],
        ["35" , "Break"                ,  "AED 3.50" ],
        ["36" , "Lindor"               ,  "AED 5.00" ],
        ["37" , "Galaxy"               ,  "AED 3.00" ],
        ["38" , "Dairy Milk"           ,  "AED 4.50" ],
        ["39" , "Feastables"           ,  "AED 35.00"],
        ["40" , "Hershey's"            ,  "AED 3.75" ],
    ],
    "5" : [
                ["41" , "Oats Bar"                  ,  "AED 1.50" ],          # healthy snacks section in order of "Item Code","Item Name","Item Price".
        ["42" , "Mixed Salads"              ,  "AED 10.00"],
        ["43" , "Apple"                     ,  "AED 2.50" ],
        ["44" , "Garlic Paste"              ,  "AED 7.50" ],
        ["45" , "Veggies and Chicken plater",  "AED 10.00"],
        ["46" , "Granola Bar"               ,  "AED 4.50" ],
        ["47" , "Trail Mix"                 ,  "AED 6.00" ],
        ["48" , "Rice Cakes"                ,  "AED 3.50" ],
        ["49" , "Hummus with Veggies"       ,  "AED 7.50" ],
        ["50" , "Fruit Cup"                 ,  "AED 5.00" ],
    ],
    "6" : [
                ["51" , "Chips + Drink"                  ,  "AED 4.50" ],       # combo meals section in order of "Item Code","Item Name","Item Price".
        ["52" , "Chocolate + Drink"              ,  "AED 5.50" ],
        ["53" , "Snacks + Drink"                 ,  "AED 8.00" ],
        ["54" , "Healthy Snack + Orange Juice"   ,  "AED 10.00"],
        ["55" , "Oats + Milk"                    ,  "AED 10.50"],
        ["56" , "Cold Sandwich + Pepsi"          ,  "AED 19.50"],
        ["57" , "White Sauce Pasta + Water"      ,  "AED 10.00"],
        ["58" , "Grill platter + Garlic Paste"   ,  "AED 15.00"],
        ["59" , "French Fries + Ketchup"         ,  "AED 5.50" ],
        ["60" , "Doritos + Salsa"                ,  "AED 10.50"],
    ],
    "7" : [
                ["61" , "Chocolate Cake"         ,  "AED 10.00" ],             # desserts section in order of "Item Code","Item Name","Item Price".
        ["62" , "Brownies"               ,  "AED 10.50" ],
        ["63" , "Donut"                  ,  "AED 1.50"  ],
        ["64" , "Cupcake"                ,  "AED 3.50"  ],
        ["65" , "Ice Cream"              ,  "AED 5.00"  ],
        ["66" , "Lava Cake"              ,  "AED 8.00"  ],
        ["67" , "Cookies"                ,  "AED 1.00"  ],
        ["68" , "Falooda"                ,  "AED 12.00" ],
        ["69" , "Cold Coffee"            ,  "AED 15.00" ],
        ["70" , "Caramel Custard"        ,  "AED 5.00"  ],
    ]

    }

    if choice in items_menu:
            
            sections[choice]()  # Calling the function to display the items
            get_item_by_code(items_menu[choice])  # Select an item
    else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


#payment part of the vending machine 
def vending_machine():
    print("Great Choice!")
    
    # Initializin an empty cart to store items with their prices
    cart = []

    while True:
        #to allow the users to add multiple items to the card
        item_name = input("\n Enter the name of the item you want to add to the cart : ").strip()
        item_price = float(input(f"Enter the price of ' {item_name}' (AED) : "))
        cart.append((item_name, item_price))
        print(f"'{item_name}' has been added to your cart for AED {item_price:.2f}.")
        
        #asking the user if he/she wants to add more items to their cart 
        add_more = input("Do you want to add more items? (yes/no): ").strip().lower()

        #if no then the payment process will start and if yes the user will get a chance to add more items to their cart 
        if add_more == 'no':
            break

    #Displaying the items in the cart and the total price
    print("\nYour Cart :")
    total_price = 0
    for item, price in cart:
        print(f"- {item} : AED{price:.2f}")
        total_price += price
    print(f"Total: AED {total_price:.2f}")



#payment process 
    while True:
        
        #asking the user if he/she wants to proceed to the payment process 
        proceed = input("\n Do you want to proceed to payment? (yes/no) : ").strip().lower()


        #if the answer is yes then the vending machine will provide two options of payment (card or cash )
        if proceed == 'yes':
            # Ask for the preferred payment method
            payment_method = input("How would you like to pay? (card/cash): ").strip().lower()


            #card payment 
            if payment_method == 'card':
                # Process card payment
                card_number = input("Please enter your card number: ").strip()
                print("Transaction in progress...")
                print("Payment successfully done. Thank you for your purchase!")
                break  #end of the the payment loop
            
            #cash payment
            elif payment_method == 'cash':
                # Process cash payment
                amount_entered = float(input(f"Total price is AED{total_price :.2f}. Please enter the amount you are paying: AED"))
                

                #in case the cash amount given is more than the actualy amount , the vending machine have the feature of giving back the change 
                if amount_entered > total_price:
                    change = amount_entered - total_price
                    print(f"""Payment successfully received. Your remaining change is : AED {change:.2f}. 
                    Thank you for your purchase!""")
                elif amount_entered < total_price:
                    remaining_balance = total_price - amount_entered
                    print(f"Insufficient payment. You still need to pay: AED {remaining_balance:.2f}. Please retry.")
                    continue  #allows the user to retry their payment
                else:
                    print("Exact payment received. Thank you for your purchase!")
                break  #end of the the payment loop
            
            else:
                print("Invalid payment method. Please restart the transaction.")
                continue  #the payment process begins again incase it fails
        



        #if the users doesn't want to start the payent process then he/she can add more itmes to their cart again
        elif proceed == 'no':
            print("You can add more items or exit the vending machine.")
            retry = input("Do you want to add more items? (yes/no) : ").strip().lower()


            #if answer is yes , the user can start selecting items frm the vending machine section again
            if retry == 'yes':
                return vending_machine()  # Restart the item selection process
            else:
                print("Transaction cancelled. Thank you for visiting the vending machine!")
                break  #the loop finishes if the user decides not to retry
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# To run the vending machine function
vending_machine()
