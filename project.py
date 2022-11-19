from cache import owner_dct as o_d, input_dct as i_d

class Owner():
    def __init__(self, name, investment=50000):
        self.portfolio = {}
        self.name = name
        self.investment = investment
        self.income = 0
        self.expenses = 0 
        self.yearly_roi = 0
        self.cashflow = 0

    @property
    def change_investment(self, new_investment):
        self.investment = new_investment

    @property
    def monthly_expenses(self,):
        return self.expenses

    @property
    def monthly_income(self,):
        return self.income

    @property
    def monthly_cashflow(self,):
        return self.income - self.expenses
        
    @property
    def yearly_roi(self):
        return self.yearly_cashflow / self.investment

    @property
    def yearly_expenses(self):
        self.expenses * 12

    @property
    def yearly_income(self):
        self.income * 12

    @property
    def yearly_cashflow(self):
        self.monthly_cashflow * 12



class Property(Owner):
    def __init__(self, name):
        super().__init__(name)

         

# property price, number of units, monthly insurance,
    #lawn/snow costs, mortgage, and questions about utilities, laundry, and storage
    #        planned % of income for repairs, cap X, management, taxes
    # for units we need to pass in rent



class Unit(Property):
    def __init__(self, name, rent =0,mortgage = 0, laundry_income=0, storage_income=0, misc_income=0, insurance=0, utilities=0, lawn_care_expense=0):
        self.name = name
        # income sources
        self.rent = rent
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.misc_income = misc_income
        # expense sources
        self.insurance = insurance
        self.utilities = utilities
        self.lawn_care_expense = lawn_care_expense
        self.mortgage = mortgage
        self.vacancy = self.rent *.05
        self.repairs = self.rent *.05
        self.cap_x = self.rent *.05
        self.prop_management = self.rent *.1

    def check_source(self, source):
        """Income checks"""
        if source == 'rent':
            print(f'Rent: {self.rent}')
        elif source == 'laundry':
            print(f'Monthly Laundry income: {self.laundry_income}')
        elif source == 'storage':
            print(f'Monthly Storage income: {self.storage_income}')
        elif source == 'misc':
            print(f'Monthly Misc income: {self.misc_income}')
        # '''Expense checks'''
        elif source == 'insurance':
            print(f'Monthly insurance cost: {self.insurance}')
        elif source == 'utilities':
            print(f'Monthly utilities cost: {self.utilities}')
        elif source == 'lawn':
            print(f'Monthly lawn care cost: {self.lawn_care_expense}')
        elif source == 'mortgage':
            print(f'Monthly mortgage cost: {self.mortgage}')
        elif source == 'vacancy':
            print(f'Monthly vacancy cost: {self.vacancy}')
        elif source == 'repairs':
            print(f'Monthly repairs cost: {self.repairs}')
        elif source == 'cap x':
            print(f'Monthly Cap X cost: {self.cap_x}')
        elif source == 'prop':
            print(f'Monthly Property Management cost: {self.prop_management}')
        
        
    # attribute setters and incrementers
    def st_rent(self, new_rent):
        self.rent = new_rent
    
    def inc_rent(self, increment):
        self.rent += increment
        print(f"Rent is now: {self.rent}" )

    def st_laundry_income(self, new_income):
        self.laundry_income = new_income

    def st_storage_income(self, new_income):
        self.laundry_income = new_income

    def st_misc_income(self, new_income):
        self.misc_income = new_income

    def st_lump_income(self, rent, laundry_income, storage_income, misc_income,):
        pass

    def st_lump_expenses(self, new_mortgage , new_insurance, new_utilities, new_lawn_care_expense, new_vacancy, new_repairs, new_cap_x, new_prop_management):
        self.insurance = new_insurance
        self.utilities = new_utilities
        self.lawn_care_expense = new_lawn_care_expense
        self.mortgage = new_mortgage
        self.vacancy = new_vacancy
        self.repairs = new_repairs
        self.cap_x = new_cap_x
        self.prop_management = new_prop_management



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
        self.prop_management = self.rent * percent
        

    def st_percent_all_expense(self, percent):
        self.insurance = self.rent * percent
        self.utilities = self.rent * percent
        self.lawn_care_expense = self.rent * percent
        self.mortgage = self.rent * percent
        self.vacancy = self.rent * percent
        self.repairs = self.rent * percent
        self.cap_x = self.rent * percent
        self.prop_management = self.rent * percent
        
    def st_percent_all_income(self, percent):
        self.laundry_income = self.rent * percent
        self.storage_income = self.rent * percent
        self.misc_income = self.rent * percent


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
            self.lawn_care_expense = self.rent * percent
            print(f'New monthly insurance cost set based on rent: {self.lawn_care_expense}')
        else:
            print("Something went wrong. Try this action again in a moment while we fix it.")


    # dynamic attribute setters

    @property
    def pull_income(self):
        self.income = self.rent + self.laundry_income + self.misc_income + self.storage_income

    @property
    def percent_expenses(self):
        return self.vacancy + self.repairs + self.cap_x + self.prop_management

    @property
    def set_expenses(self):
        self.insurance = self.insurance + self.utilities + self.lawn_care_expense + self.mortgage + self.percent_expenses
    # @property
    # def cash_flow(self, income, expenses):
    #     return income + expenses




# add a feature to create multiple identical units at once


    # what things do I want to pass into this program?
    # 

#        planned % of income for repairs, cap X, management, taxes
    # for units we need to pass in rent





# set attributes using a property decorator outside of class:

