#1 Exercise 1
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
count=0
current_max=0
sale_above_100 = 0
sale_above_100_total = 0
for sale in sales:
    total += sale   # update
    count += 1
    #exercise 3 inside origninal loop
    if sale > current_max:
        current_max = sale
    #Exercise 4 inside original loop
    if sale > 100:
        sale_above_100 += 1
        sale_above_100_total += sale

    
#Exercise 2 also combined

print(f"Total: ${total}")
print(f'Count: {count}')
print(f'Average: ${total/count:.2f}')
print(f'Maximum: ${current_max}')
print(f'Sales above $100: {sale_above_100}')
print(f'Total of sales above $100: ${sale_above_100_total}')