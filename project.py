from cache import owner_dct as o_d, input_dct as i_d

class Owner():
    def __init__(self, name, investment=50000):
        self.portfolio = []
        self.name = name
        self._investment = investment
        self._income = 1
        self._expenses = 1 
        self._cashflow = 1
        self._roi = 1

    # getters
    @property
    def investment(self):
        return self._investment

    @property
    def monthly_income(self):
        return self._monthly_income

    @property
    def monthly_expenses(self):
        return self._monthly_expenses

    @property
    def monthly_cashflow(self):
        return self.monthly_income - self.monthly_expenses

    @property
    def yearly_income(self):
        return self._income * 12
        
    @property
    def yearly_expenses(self):
        return self._expenses * 12

    @property
    def yearly_cashflow(self):
        return (self.monthly_income - self.monthly_expenses) * 12

    @property
    def roi(self):
        print("Checking ROI")
        return self._roi

    # setters
    @investment.setter
    def change_investment(self, new_investment):
        if new_investment < 0:
            raise ValueError("You cannot have a negative investment.")
        self._investment = new_investment

    @monthly_income.setter
    def monthly_income(self, new=0):
        if new < 0:
            raise ValueError(f"You cannot have negative monthly expenses.")
        if self.rent:
            self._monthly_income = self.rent + self.laundry + self.storage + self.misc
        elif self.portfolio:
            new = [part.income for part in self.portfolio]
            self._monthly_income = sum(new)
        else:
            self._monthly_income = new

    @monthly_expenses.setter
    def monthly_expenses(self, new=0):
        if new < 0:
            raise ValueError(f"You cannot have negative monthly expenses.")
        if self._insurance:
            self._monthly_expenses =self.insurance + self.utilities + self.lawncare + self.mortgage + self.vacancy + self.repairs + self.cap_x + self.property_management
        elif self.portfolio:
            print("portmontaeu")
            new = [part.expenses for part in self.portfolio]
            self._monthly_expenses = sum(new)
        
        else:
            self._monthly_expenses = new
        # this is unnecessary
    # @monthly_cashflow.setter
    # def monthly_cashflow(self):
    #     self._monthly_cashflow = 
    
    @roi.setter
    def set_roi(self):
        # currently this is broken but functionality returns when changed to a 
        # property rather than a setter wit this function:
#         gogo = Owner('charles', 59000)
# gogo.set_roi
        print("setting roi")
        self._roi = self.yearly_cashflow / self._investment

    def __str__(self):
        return self.name.title()
    
    def __repr__(self) -> str:
        return self.name.title()


    
    def show_all(self, building, investment):
        building.monthly_expenses = 0
        building.monthly_income = 0

        print(building.name.title())
        print(f'''
Yearly Income: {building.monthly_income}
    +
Yearly Expenses: {building.monthly_expenses}
=
Cashflow: {building.monthly_cashflow}

And based on your investment your ROI is {building.yearly_cashflow / investment}''')

class Building(Owner):
    def __init__(self, name, investment):
        super().__init__(name)

         

# property price, number of units, monthly insurance,
    #lawn/snow costs, mortgage, and questions about utilities, laundry, and storage
    #        planned % of income for repairs, cap X, management, taxes
    # for units we need to pass in rent



class Unit(Building):
    def __init__(self, name, rent =0,mortgage = 0, laundry=0, storage=0, misc=0, insurance=1, utilities=1, lawncare=1,property_management=1, cap_x=1,repairs=1,vacancy=1):
        self.name = name
        super().__init__(name, investment=0)
        # income sources
        self._rent = rent
        self._laundry_income = laundry
        self._storage_income = storage
        self._misc_income = misc
        # expense sources
        self._insurance = insurance
        self._utilities = utilities
        self._lawn_care_expense = lawncare
        self._mortgage = mortgage
        self._vacancy = vacancy
        self._repairs = repairs
        self._cap_x = cap_x
        self._property_management = property_management

    # def check_source(self, source):
    #     """Income checks"""
        # if source == 'rent':
        #     print(f'Rent: {self.rent}')
        # elif source == 'laundry':
        #     print(f'Monthly Laundry income: {self.laundry_income}')
        # elif source == 'storage':
        #     print(f'Monthly Storage income: {self.storage_income}')
        # elif source == 'misc':
        #     print(f'Monthly Misc income: {self.misc_income}')
        # # '''Expense checks'''
        # elif source == 'insurance':
        #     print(f'Monthly insurance cost: {self.insurance}')
        # elif source == 'utilities':
        #     print(f'Monthly utilities cost: {self.utilities}')
        # elif source == 'lawn':
        #     print(f'Monthly lawn care cost: {self.lawn_care_expense}')
        # elif source == 'mortgage':
        #     print(f'Monthly mortgage cost: {self.mortgage}')
        # elif source == 'vacancy':
        #     print(f'Monthly vacancy cost: {self.vacancy}')
        # elif source == 'repairs':
        #     print(f'Monthly repairs cost: {self.repairs}')
        # elif source == 'cap x':
        #     print(f'Monthly Cap X cost: {self.cap_x}')
        # elif source == 'prop':
        #     print(f'Monthly Property Management cost: {self.prop_management}')
        


        # income getters
    @property
    def rent(self):
        return self._rent

    @property
    def laundry(self):
        return self._laundry_income

    @property
    def storage(self):
        return self._storage_income

    @property
    def misc(self):
        return self._misc_income
    

        # expense getters
    @property
    def insurance(self):
        return self._insurance

    @property
    def utilities(self):
        return self._utilities

    @property
    def lawncare(self):
        return self._lawn_care_expense

    @property
    def mortgage(self):
        return self._mortgage

    @property
    def vacancy(self):
        return self._vacancy

    @property
    def repairs(self):
        return self._repairs

    @property
    def cap_x(self):
        return self._cap_x

    @property
    def property_management(self):
        return self._prop_management

    # attribute setters and incrementers
    #       income
    @rent.setter
    def rent(self, new_rent=0):
        self._rent = new_rent
    
    def inc_rent(self, increment):
        self.rent += increment
        print(f"Rent is now: {self.rent}" )

    @laundry.setter
    def laundry(self, new_income=0):
        self._laundry_income = new_income

    @storage.setter
    def storage(self, new_income=0):
        self._storage_income = new_income

    @misc.setter
    def misc(self, new_income=0):
        self._misc_income = new_income

        # expenses
    @insurance.setter
    def insurance(self, new_insurance=0):
        self._insurance = new_insurance
    
    @utilities.setter
    def utilities(self, new_utilities=0):
        self._utilities = new_utilities

    @lawncare.setter
    def lawncare(self, new_lawncare=0):
        self._lawn_care_expense = new_lawncare

    @mortgage.setter
    def mortgage(self, new_mortgage=0):
        self._mortgage = new_mortgage

    @vacancy.setter
    def vacancy(self, new_vacancy=0):
        self._vacancy = new_vacancy

    @repairs.setter
    def repairs(self, new_repairs=0):
        self._repairs = new_repairs
    
    @cap_x.setter
    def cap_x(self, new_cap_x=0):
        self._cap_x = new_cap_x

    @property_management.setter
    def property_management(self, new_prop_management=0):
        self._prop_management = new_prop_management


    def st_lump_income(self, rent, laundry_income, storage_income, misc_income,):
        pass

    def st_lump_expenses(self, new_mortgage , new_insurance, new_utilities, new_lawn_care_expense, new_vacancy, new_repairs, new_cap_x, new_prop_management):
        self.insurance = new_insurance
        self.utilities = new_utilities
        self.lawncare = new_lawn_care_expense
        self.mortgage = new_mortgage
        self.vacancy = new_vacancy
        self.repairs = new_repairs
        self.cap_x = new_cap_x
        self.property_management = new_prop_management

    def st_expenses_all(self):
        pass

    # percent modifiers
    def st_percent_all(self, percent):
        self.laundry_income = self.rent * percent
        self.storage_income = self.rent * percent
        self.misc_income = self.rent * percent
        # expense sources
        self.insurance = self.rent * percent
        self.utilities = self.rent * percent
        self.lawn_care_expense = self.rent * percent
        self.mortgage = self.rent * percent
        self.vacancy = self.rent * percent
        self.repairs = self.rent * percent
        self.cap_x = self.rent * percent
        self.property_management = self.rent * percent
        
    # @property
    def st_percent_all_expense(self, percent):
        self.insurance = self.rent * percent
        self.utilities = self.rent * percent
        self.lawncare = self.rent * percent
        self.mortgage = self.rent * percent
        self.vacancy = self.rent * percent
        self.repairs = self.rent * percent
        self.cap_x = self.rent * percent
        self.property_management = self.rent * percent
        
    def st_percent_all_income(self, percent):
        self.laundry = self.rent * percent
        self.storage = self.rent * percent
        self.misc = self.rent * percent


    def st_percent_specific(self, source, percent):
        if source == 'insurance':
            self.insurance = self.rent * percent
            print(f'New monthly insurance cost set based on rent: {self.insurance}')
        elif source == 'utilities':
            self.utilities = self.rent * percent
            print(f'New monthly utilities cost set based on rent: {self.utilities}')
        elif source == 'lawn':
            self.lawn_care_expense = self.rent * percent
            print(f'New monthly lawncare expense set based on rent: {self.lawn_care_expense}')
        elif source == 'mortgage':
            self.mort = self.rent * percent
            print(f'New monthly mortgage cost set based on rent: {self.mortgage}')
        elif source == 'vacancy':
            self.vacancy = self.rent * percent
            print(f'New monthly vacancy saving set based on rent: {self.vacancy}')
        elif source == 'repairs':
            self.repairs = self.rent * percent
            print(f'New monthly repairs saving set based on rent: {self.repairs}')
        elif source == 'cap x':
            self.cap_x = self.rent * percent
            print(f'New monthly Cap X savings set based on rent: {self.cap_x}')
        elif source == 'prop':
            self._property_management = self.rent * percent
            print(f'New monthly insurance cost set based on rent: {self.lawn_care_expense}')
        else:
            print("Something went wrong. Try this action again in a moment while we fix it.")


    # dynamic attribute setters

    @property
    def pull_income(self):
        self.income = self.rent + self.laundry_income + self.misc_income + self.storage_income

    @property
    def percent_expenses(self):
        return self.vacancy + self.repairs + self.cap_x + self.property_management

    @property
    def set_expenses(self):
        self.insurance = self.insurance + self.utilities + self.lawn_care_expense + self.mortgage + self.percent_expenses

    def show_all_monthly(self):
        self.monthly_expenses = 0
        self.monthly_income = 0

        print(self.name.title())
        print(f'''Income Sources:
Rent: {self.rent} \nLaundry: {self.laundry} \nStorage:{self.storage} \nMisc: {self.misc}
Total Income: {self.monthly_income}
Expenses: \nInsurance: {self.insurance} \nUtilities: {self.utilities}
Lawncare: {self.lawncare} \nMortgage: {self.mortgage} \nVacancy: {self.vacancy}
Repairs: {self.repairs} \nCap X: {self.cap_x} \nProperty Management: {self.property_management}
Total Expenses: {self.monthly_expenses}

Cashflow: {self.monthly_cashflow}''')

    # @property
    # def cash_flow(self, income, expenses):
    #     return income + expenses



# add a feature to create multiple identical units at once


    # what things do I want to pass into this program?
    # 

#        planned % of income for repairs, cap X, management, taxes
    # for units we need to pass in rent





# set attributes using a property decorator outside of class:

