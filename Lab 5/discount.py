#question 1

total = float(input("enter cart total: $"))
#add your if/elif/else here

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

#Exercise 2
if final > 1000: #strictly greater than. 
    status = "manager_approval_required"
else: 
    status = "auto_approved"
print(f"Status: {status}")

#Exercise 3
region = 'South' #S is capitalized

if region == 'South' and total >=100:
    extra_discount = 0.02
    print("Region bonus Applied: additional 2% off")
else:
    extra_discount = 0

final=total * (1 - (discount+extra_discount))
print(f"Discount: {discount*100:.0f}%")
print(f"Extra Discount: {extra_discount*100:.0f}%")


#Exercise 4
customer_type='Wholesale'
if region ==  'South' and total >= 100 and customer_type=='Wholesale':
    extra_discount=0.03



#Exercise 5
amount = 0

if amount <= 0:
    print("SUSUPICOIS")
elif amount < 10000:
    print("NORMAL")
else:
    print("Large -- Review requiered ")


#Exercise 6

has_outstanding_balance=False
orders=15
spending=105
vip_upgrade=True
if spending>2000 or orders>10 and not has_outstanding_balance:
    vip_upgrade=True
else:
    vip_upgrade=False   
first_order==True
# Stretch 1
