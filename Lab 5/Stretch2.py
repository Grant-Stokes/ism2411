#2nd Stretch Goal
taxable_income=float(input('Enter taxable income'))
first_increiment=1160.1
first_tax_bracket=11601
second_increiment=4266
second_tax_bracket=35550

if taxable_income > 47151:
    Tax=(((taxable_income-first_tax_bracket-second_tax_bracket)*0.22)+first_increiment+second_increiment)
    print('Your tax is ' + str(Tax))
    print('Your remaining income is '+ str(taxable_income-Tax))
elif taxable_income > 11601:
    Tax=((taxable_income-first_tax_bracket)*0.12)+first_increiment
    print('Your tax is ' + str(Tax))
    print('Your remaining income is '+ str(taxable_income-Tax))
else:
    Tax=taxable_income*0.1
    print('Your tax is ' + str(Tax))
    print('Your remaining income is '+ str(taxable_income-Tax))