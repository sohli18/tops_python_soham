name = input("Enter your name")
gender = str(input("Enter your gender"))
age = int(input("Enter your age"))

product = input("Enter produduct")
weight  = int(input("enter the weight of gold"))
print("current gold price per 1g : 5752")
total_gold_rate = int(weight*5752)
print("Total gold rate: " + str(total_gold_rate))

print("making charges per 1g gold : 845")
total_makin_charge = int(weight*845)
print(" total making charge is" + str(total_makin_charge))

total_ammnt = int(total_gold_rate + total_makin_charge)
print("Total ammount is " + str(total_ammnt))

if gender=="male":
     if age>65:
         if total_ammnt>21000 and total_ammnt<31000:
             disc = 0.8
         elif total_ammnt>31000 and total_ammnt<51000:
             disc = 0.7
         else:
             disc = 0.65
     else:
         if total_ammnt>21000 and total_ammnt<31000:
             disc = 0.9
         elif total_ammnt>31000 and total_ammnt<51000:
             disc = 0.8
         else:
             disc = 0.75
if gender=="female":
     if age>65:
         if total_ammnt>21000 and total_ammnt<31000:
             disc = 0.75
         elif total_ammnt>31000 and total_ammnt<51000:
             disc = 0.65
         else: 
             disc = 0.6
     else:
         if total_ammnt>21000 and total_ammnt<31000:
             disc = 0.85
         elif total_ammnt>31000 and total_ammnt<51000:
             disc = 0.75
         else:
             disc = 0.7
diskount = int(100*(1-disc))
print("discount: " + str(diskount)) 

total_net_ammount = int(total_ammnt*disc)
print("total net ammount is " + str(total_net_ammount))