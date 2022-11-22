owner_dct = {}

expense_dict = {
                    'insurance':0, 'utilities':0, 
                    'lawncare':0, 'mortgage':0, 
                    'vacancy':0, 'repairs':0, 
                    'cap_x':0, 'property_management':0
                }
input_dct = {
    'set_options' : ['rent',
 'laundry_income',
'storage_income',
'misc_income',
        # expense sources
'insurance',
'utilities',
'lawn_care_expense',
'mortgage',
'vacancy',
'repairs', 'cap_x', 'prop_management'],
'yes':['yes','y','ye','yeah','yup','sure','mhm'],
'no': ['no','nope','naw','nuh uh', 'na', 'negatory', 'negative', 'n']
}

txt = {
    'monthly_plural' :"Your monthly expenses at this level are: {expenses}",
    "monthly_other" : 'Monthly insurance cost: {insurance}',
    "wait_part": '(W)ait: put your portfolio together, then adjust the numbers.',
}