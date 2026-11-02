
menu={"espresso":{"name":"espresso","price":2.5,"milk":200,"coffe":18,"water":100},"cappuccino":{"name":"cappuccino","price":2.0,"milk":200,"coffe":15,"water":100},"latte":{"name":"latte","price":2.15,"water":200,"coffe":24,"milk":0}}
remaining={"water":2000,"milk":2000,"coffe":200,"money":0}

game=True
while game:
    print("welcome to the coffee machine!")
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "off":
        print("turning off the coffee machine.")
        game=False
        break

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":

        remaining["water"]-=menu[user_input]["water"]
        remaining["milk"]-=menu[user_input]["milk"]
        remaining["coffe"]-=menu[user_input]["coffe"]

        if((remaining["water"]<0) or (remaining["milk"]<0)  or (remaining["coffe"]<0)):
            print("not enough raw items")
            game=False
            break


        print(f"The {user_input} price is :{menu[user_input]["price"]}$")
        penny=int(input("enter how many penny's: "))
        penny_10=int(input("enter how many penny 10's: "))
        quarters=int(input("enter how many quarters: "))
        total=(penny*0.01)+(quarters*0.25)+(penny_10*0.10)
        remaining["money"]+=menu[user_input]["price"]
        if total<menu[user_input]["price"]:
            print(f"The {user_input} price is :{menu[user_input]["price"]}$")
            print("sorry, you don't have enough money!")
            money_again=input("do you want enter money again (continue/exit): ").lower()
            if money_again == "continue":
                game=True
            if money_again == "exit":
                game=False
        elif total>menu[user_input]["price"]:
            return_money=total-menu[user_input]["price"]
            print(f"here is your change sir! :{return_money}$")

    if user_input == "report":
        print(remaining)
    game_continue=input("do you want to continue order more (yes/no): ").lower()

    if game_continue == "yes":
        game=True
    elif game_continue == "no":
        game=False





