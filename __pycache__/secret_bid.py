

def bids(dici):

    j=max(dici,key=dici.get)
    print(f"the winner is {j} has bid amount of {dici[j]}$ ")


no=True
dici={}
while no:
    name=input("enter your name: ")
    bid=int(input("enter your bid amount: "))
    dici[name]=bid
    cntue=input("do you want to continue(yes/no): ").lower()
    if cntue=="yes":
        no=True
        print("\n"*20)
    elif cntue =="no" :
        no=False
        bids(dici)
    else:
        print("enter valid input!")
        





# def find_winner(bids):
#     winner = max(bids, key=bids.get)
#     print(f"The winner is {winner} with a bid amount of ${bids[winner]}")


# import os

# bids = {}
# while True:
#     name = input("Enter your name: ")
#     bid_amount = int(input("Enter your bid amount: "))
#     bids[name] = bid_amount

#     cont = input("Do you want to continue (yes/no): ").lower()
#     if cont == "yes":
#         os.system('cls' )  # Clears screen
#     elif cont == "no":
#         find_winner(bids)
#         break
#     else:
#         print("Please enter a valid input!") 

