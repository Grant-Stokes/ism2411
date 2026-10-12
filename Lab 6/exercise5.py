#Exercise 5
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0  

for sale in sales:
    if sale > 400:
        print(f'Alert: outlier found-'+f' ${sale} '+ f'stopping.')
        break
    else:
        if sale >100:
            print(sale)
