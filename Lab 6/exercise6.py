sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0            # index
while i < len(sales):
    total += sales[i]
    i += 1
print(f'Total: ${total}')