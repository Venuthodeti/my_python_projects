print("welcome to the tip calcutator")
bill=int(input("what is the total bill? :"))
persentage=int(input("what is the tip persentage? :"))
tip=(bill/100)*persentage
sharing=int(input("how many people want to share the bill? :"))
total_bill=(tip+bill)/sharing
round_fig=round(total_bill,2)
print(f"each person have to pay :{round_fig} ")
print(f"each person have to pay the tip :{tip} ")
