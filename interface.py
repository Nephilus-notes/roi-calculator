from cache import owner_dct as o_d, input_dct as i_d, expense_dict as e_d
from project import Owner, Building, Unit
txt = {
'wrong_num': "Something went wrong. We're looking for a number: "
}



class Driver():
    def __init__(self) -> None:
        pass

    def create_owner(self, name, investment):
        o_d[name] = name
        o_d[name] = Owner(name, investment=investment)
        print("Congratulations, we've created your profile!")
        return o_d[name]
        

    def create_building_dict(self):
        name = input("""What would you like to call this building? 
Individual names are encouraged to avoid confusion. """)
        investment = input("And how much did you invest in this building? ")
        while True:
            try: 
                investment = int(investment)
                break
            except:
                investment = input(txt["wrong_num"])
        
        unit_num = input(f"Got it. How many units does {name.title()} have? ")
        while True:
            try: 
                unit_num = int(unit_num)
                print("Let's name the units individually to prevent confusion.")
                break
            except:
                unit_num = input(txt["wrong_num"])
        unit_list = []
            
        for unit in range(unit_num):
            print(f"Unit {unit + 1}")
            unit_name = input("""What would you like to call this unit? """)
            unit_name = {'name':unit_name, }
            unit_list.append(unit_name)
        name = {'name':name, 'investment':investment, 'unit_list': unit_list}
        return name

    def create_building(self, user, building):
        unit_list = []
        for unit in building['unit_list']:
            print(unit)
            unit = Unit(**unit)
            unit_list.append(unit)
        building = Building(building['name'], building['investment'])
        user.portfolio.append(building)
        for unit in unit_list:
            building.portfolio.append(unit)
        return building
        

    def main(self):
        name = input("""Welcome to our software. Please input your name: """).lower().strip()
        while True:
            if name in o_d:
                input("Welcome back! Ready to get back to taking over the world?")
                # start owner main page  
                break
            else:
                new_user =input(f"Hi {name.title()} looks like you're a new user, right? ")
                if new_user in i_d['yes']:
                    self.new_user_build_portfolio(name)
                    break

            name = input("Looks like something went wrong.  Input your name again here: ")

    def new_user_build_portfolio(self, user):
        print("Fantastic! Ready for us to help you take over the world?")
        investment = input("First off we'd like to ask how much you've already invested: ")
        while True:
            try: 
                investment = int(investment)
                break
            except:
                investment = input(txt["wrong_num"])
        user = self.create_owner(user, investment)
        prop_num = input("Now how many building have you invested in? ")
        while True:
            try: 
                prop_num = int(prop_num)
                break
            except:
                prop_num = input(txt["wrong_num"])
        count = 0
        building_list = []
        for buildings in range(prop_num):
            count += 1
            building_list.append(self.create_building_dict())
            if prop_num > count:
                finish = input("""We have put together your building. Would you 
    like to [Input] specifics or [Continue] putting together your building portfolio? """).lower().strip()
                while True:
                    if finish in  ['i','in', 'input']:
                        building = building_list[-1]
                        self.rent_prompt(building['name'], building['unit_list'])
                        slm_income_dict = self.get_building_slm_income() 
                        unit_slm = {k: v/len(building['unit_list'])-1 for k,v in slm_income_dict.items()}
                        for unit in building['unit_list']:
                            unit.update(unit_slm.copy())
                        self.expenses_main(building)
                        # for unit in building['unit_list']:
                            # print(unit)
                        building = self.create_building(user, building)
                        for unit in building.portfolio:
                            print("\n")
                            unit.show_all_monthly()
                        print(building)
                        break
                    elif finish in ['c', 'continue', 'con']:
                        break
                    else:
                        finish =input("What was that again? [Input] or [Continue]:")
        # investment = investment / len(user.portfolio)
        for building in building_list:
            print(building['name'].title())
            self.rent_prompt(building['name'], building['unit_list'])
            slm_income_dict = self.get_building_slm_income() 
            unit_slm = {k: v/len(building['unit_list'])-1 for k,v in slm_income_dict.items()}
            for unit in building['unit_list']:
                unit.update(unit_slm.copy())
            self.expenses_main(building)
            # for unit in building['unit_list']:
                # print(unit)
            building = self.create_building(user, building)
            for unit in building.portfolio:
                print("\n")
                unit.show_all_monthly()
            print(building)
            # prop.show_all(prop_object, investment)
           


    def rent_prompt(self, building_name, unit_list):
        rent_method = input("Would you like to set unit rent (I)ndividually or for the (B)uilding? ").lower().strip()
        while True:
            if rent_method in ['i', 'indiv', 'in', 'individually']:
                for unit in unit_list:
                    print(unit['name'].title())
                    unit['rent'] = self.blanket_rent_get(unit['name'])
                    
                break
                # need to add function here
            elif rent_method in ['b', 'build', 'building']:
                self.set_building_rent(building_name, unit_list)
                break
            else:
                rent_method = input("Come again? Set rent (I)ndividually or for the (B)uilding.")
                

    def set_building_rent(self, building_name, unit_list):
        rent = self.blanket_rent_get(building_name)
        for unit in unit_list:
            unit['rent'] = rent


    def get_building_slm_income(self):
        income_method = input("""And do you have other income streams to set for the building? 
(S)torage
(L)aundry
(M)isc
(A)ll of the above
""").lower().strip()
        slm_income = {'storage': 0, 'laundry': 1, 'misc': 1}
        while True:
            if income_method in ['s', 'stor', 'store', 'storage']:
                try:
                    slm_income['storage'] = int(input("What is your monthly income from storage fees? "))
                except:
                    print(txt['wrong_num'])
                income_method = input('Do you have any other income sources? \n(L)aundry\n(M)isc\n(No):').lower().strip()
            
            elif income_method in ['l', 'laundry']:
                try:
                    slm_income['laundry'] = int(input("What is your monthly income from laundry fees? "))
                except:
                    print(txt['wrong_num'])
                income_method = input('Do you have any other income sources? \n(S)torage\n(M)isc\n(No):').lower().strip()
            
            elif income_method in ['m', 'misc']:
                try:
                    slm_income['misc'] = int(input("What is your monthly misc income? "))
                except:
                    print(txt['wrong_num'])
                income_method = input('Do you have any other income sources? \n(S)torage\n(L)aundry\n(No):').lower().strip()
            elif income_method in i_d['no']:
                return slm_income
                break
            else:
                income_method = input("what was that?")
            

    def blanket_rent_get(self, name):
        rent_running = True
        while rent_running:
            try: 
                rent = int(input(f'How much is the rent for {name.title()}? '))
                return rent
                rent_running = False
                break
            except:
                rent = input("What number would you like to set the rent to? ")
                # return rent

    # def set_building_income(self, slm_income_dict, prop_object):
    #     for unit in prop_object.portfolio:
    #         unit.storage = slm_income_dict['storage']
    #         unit.laundry = slm_income_dict['laundry']
    #         unit.misc = slm_income_dict['misc']

    def expenses_main(self, building):                   
        expense_method = input("""What format would you like to give us expenses in? 
    (L)ump: expenses for the building
    (p)ercentage: We'll base your expenses off a percentage of the rent.
    (S)et: choose specific numbers for individual units.""").lower().strip()
        while True:
            if expense_method in ['l', 'lump']:
                building_expenses = self.expenses_get()
                # unit_expenses = list(map(lambda kv: (kv[0]: kv[1] / len(prop_object.portfolio)), property_expenses))
                unit_expenses = {k: v/len(building['unit_list'])-1 for k,v in building_expenses.items()}
                for unit in building['unit_list']:
                    unit.update(unit_expenses.copy())
                    print(unit)
                break
            elif expense_method in ['p', 'percentage']:
                perc = self.percentage_get()
                for unit in building['unit_list']:
                    for expense in e_d.keys():
                        unit[expense] = unit['rent'] * perc
                break
            elif expense_method in ['s', 'set']:
                self.unit_expenses(building)
                break
            # elif expense_method in ['w', 'wait']:
            #     pass
            else:
                expense_method = input("What was that? (L)ump, (P)ercent, or (S)et: ")
        

    def percentage_get(self):
        percent_running = True
        while percent_running:
            try:
                percent = int(input("What percentage would you like to set for your expenses? "))/100
                return percent
                percent_running= False
            except:
                quit = input("One of those numbers didn't work. Let's try this again. Skip this step by hitting (W). ").lower().strip()

                # expense_method = input(txt["wrong_num"])

    def expenses_get(self):
        while True:
            try:
                monthly_insurance = int(input("How much is your monthly insurance cost? " ))
                monthly_utilities = int(input("How much is your monthly utilities cost? " ))
                monthly_lawncare = int(input("How much is your monthly lawncare cost? " ))
                monthly_mortgage = int(input("How much is your monthly mortgage cost? " ))
                monthly_vacancy = int(input("How much is your monthly vacancy budget? " ))
                monthly_repairs = int(input("How much is your monthly repairs budget? " ))
                monthly_cap_x = int(input("How much is your monthly Capital Expenditure budget? " ))
                monthly_prop_management = int(input("How much is your monthly property management budget? " ))
                expense_dict = {
                    'insurance':monthly_insurance, 'utilities':monthly_utilities, 
                    'lawncare':monthly_lawncare, 'mortgage':monthly_mortgage, 
                    'vacancy':monthly_vacancy, 'repairs':monthly_repairs, 
                    'cap_x':monthly_cap_x, 'property_management':monthly_prop_management
                }
                return expense_dict
            except:
                quit = input("One of those numbers didn't work. Let's try this again. Skip this step by hitting (W). ").lower().strip()
                if quit == 'w':
                    break
                

    def unit_expenses(self, building):
        for unit in building['unit_list']:
            while True:
                choice = input(f"Would you like to (S)et {unit}'s expenses or leave them as a (P)ercentage? ")
                if choice in ['s', 'set']:
                    unit_expenses = self.expenses_get()
                    unit.update(unit_expenses.copy())
                    break
                if choice in ['p', 'per', 'perc', 'percentage', 'percent']:
                    percent = self.percentage_get()
                    for expense in e_d.keys():
                        unit[expense] = unit['rent'] * percent
                    break
                else:
                    input("Try that again. (S)et or (P)ercent.")

    def expense_assign(self, unit, expense_dict):
        unit.insurance = expense_dict['insurance']
        unit.utilities = expense_dict['utilities']
        unit.lawncare = expense_dict['lawncare']
        unit.mortgage =expense_dict['mortgage']
        unit.vacancy =expense_dict['vacancy']
        unit.repairs =expense_dict['repairs']
        unit.cap_x =expense_dict['cap_x']
        unit.property_management =expense_dict['prop_management']


    def returning_user(self):
        print(f"Welcome to your roi portfolio {self}!\n?")
        while True:
            task = input(f"""Do you want to work with your (P)ortfolio
building(Y)
or (U)nits""").lower().strip()
            if task in ['p', 'port', 'portfolio', 'folio']:
                pass
            # access the user and use the generic menu
            elif task in ['y', 'prop','ty', 'building']:
                pass
            # a function that uses the generic menu to access all the buildings
            elif task in ['u', 'unit', 'un']:
                pass
            # 


    def invest_calc_slapstick(self, user):
        print(f'investment: {user.investment}')


#     def building_show_all(self, building, investment):
#         building.monthly_expenses = 0
#         building.monthly_income = 0

#         print(building.name.title())
#         print(f'''
# Yearly Income: {building.monthly_income}
#     +
# Yearly Expenses: {building.monthly_expenses}
# =
# Cashflow: {building.monthly_cashflow}

# And based on your investment your ROI is {building.yearly_cashflow / investment}''')
        

    def folio_menu(self, user):
        user.monthly_income
        user.monthly_expenses
        user.monthly_cashflow
        user.yearly_cashflow
        print("Let's check out your portfolio!")
        check = input(f"""ROI:  {user.roi}\n""")





gogo = Driver()
gogo.main()