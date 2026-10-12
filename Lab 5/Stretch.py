total=float(input('input a total'))
Region='South'
customer_type='Wholesale'
first_order=True
def Tier_discount(total):
    if total >= 500:
        discount = 0.15
    elif total >= 200:
        discount = 0.10
    elif total >= 100:
        discount = 0.05
    else:
        discount = 0

    return(discount)

extra_discount=0
first_order_discount=0
wholesale_discount =0
if Region=='South' and customer_type=='Wholesale' and first_order==True:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
    extra_discount=0.02
    print("adding South Discount")
    final=total * (1 - (discount+extra_discount))
    print('new price is ' + str(final))
    print("adding Wholesale discount")
    wholesale_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount))
    print('new price is ' + str(final))
    print('Adding first order discount')
    first_order_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount+first_order_discount))
    print("Final Price is "+str(final))
elif Region == 'South' and Customer_type=='Wholesale' and first_order != True:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
    extra_discount=0.02
    print("adding South Discount")
    final=total * (1 - (discount+extra_discount))
    print('new price is ' + str(final))
    print("adding Wholesale discount")
    wholesale_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount))
    print('new price is ' + str(final))
    print("Final Price is "+str(final))
elif Region == 'South' and custom_type != 'Wholesale' and first_order ==True:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
    extra_discount=0.02
    print("adding South Discount")
    final=total * (1 - (discount+extra_discount))
    print('new price is ' + str(final))
    print('Adding first order discount')
    first_order_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount+first_order_discount))
    print("Final Price is "+str(final))
elif Region == 'South' and customer_type != 'Wholesale' and first_order != True:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
    extra_discount=0.02
    print("adding South Discount")
    final=total * (1 - (discount+extra_discount))
    print('new price is ' + str(final))
    print("Final Price is "+str(final))
elif Region != 'South' and customer_type == 'Wholesale' and first_order == True:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
    print("adding Wholesale discount")
    wholesale_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount))
    print('new price is ' + str(final))
    print('Adding first order discount')
    first_order_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount+first_order_discount))
    print("Final Price is "+str(final))
elif Region != 'South' and customer_type == 'Wholesale' and first_order != True:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
    print("adding Wholesale discount")
    wholesale_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount))
    print('new price is ' + str(final))
    print("Final Price is "+str(final))
elif Region != 'South' and customer_type != "Wholesale" and first_order == True:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
    print("adding Wholesale discount")
    wholesale_discount=0.05
    final=total * (1 - (discount+extra_discount+wholesale_discount))
    print('new price is ' + str(final))
    print("Final Price is "+str(final))
else:
    Tier_discount(total)
    discount=Tier_discount(total)
    final=total * (1 - (discount+extra_discount))
    print('your price is ' + str(total))
        