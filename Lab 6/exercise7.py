sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >=100:
        discount = 0.05
    else:
        discount = 0
    discounted_sale = sale * (1 - discount)
    print(f'${sale} -> {discount:.2%} -> ${discounted_sale:.2f}')
    total += sale   # update
print(f"Total: ${total}")