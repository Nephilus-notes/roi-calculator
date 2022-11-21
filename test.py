from cache import owner_dct as o_d, input_dct as i_d
from project import Owner, Property, Unit
from interface import Driver
txt = {
'wrong_num': "Something went wrong. We're looking for a number."
}

# gogo = Owner('charles', 59000)
# gogo.set_roi()

# print(gogo.roi)

# john = o_d['john']
# for property in john.portfolio:
#     property.monthly_income = 0
#     property.monthly_expenses = 0
    
#     print(property.monthly_income)

gogo = Driver()
gogo.main()


# # # my_str= "abcdefg"

# if 'a' in my_str:
#     print("sweet")

# cabin = Unit('cabin')
# cabin.rent = 1000
# cabin.storage = 500
# cabin.st_percent_all_income(.09)
# cabin.st_percent_all_expense(.1)
# # cabin.monthly_cashflow
# cabin.show_all_monthly()

