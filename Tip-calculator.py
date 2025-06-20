print("Welcome to the tip calculator")
bill=int(input("what was the total bill?"))
tip=int(input("How much tip would you like to pay? 10, 12, or 15?"))
person=int(input("How many people to split the bill?"))
tip_percentage=tip/100
total_tip_amount=bill*tip_percentage
total_bill=total_tip_amount+bill
bill_per_person=bill/person
final_amount=round(bill_per_person,2)
print(f"Each person should pay:{final_amount}")