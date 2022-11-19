from cache import owner_dct as o_d, input_dct as i_d
from project import Owner, Property, Unit
txt = {
'wrong_num': "Something went wrong. We're looking for a number."
}



class Driver():
    def __init__(self) -> None:
        pass

    def create_owner(self, name, investment):
        o_d[name] = name
        o_d[name] = Owner(name, investment=investment)
        print("Congratulations, we've created your profile!")
        

    def create_property(self, owner):
        name = input("""What would you like to call this property? 
Individual names are encouraged to avoid confusion. """)
        name = Property(name)
        owner.portfolio[name] = name
        unit_num = input(f"Got it. How many units does {name} have?")
        while True:
            try: 
                unit_num = int(unit_num)
                break
            except:
                unit_num = input(txt["wrong_num"])
        for unit in range(unit_num):
            unit_name = input("""What would you like to call this unit? 
Individual names are encouraged to avoid confusion. """)
        self.create_unit(name, unit_name)
        return owner.portfolio[name], unit_num


    def create_unit(self, property, name, *args):
        name = Unit(name, *args)
        property.portfolio[name] = name

    def main(self):
        name = input("""Welcome to our software. Please input your name: """).lower().strip()
        while True:
            if name in o_d:
                input("Welcome back! Ready to get back to taking over the world?")
                # start owner main page  
                break
            else:
                new_user =print("Great looks like you're a new user, right?")
                if new_user in i_d['yes']:
                    self.new_user(name)
                    break

            name = input("Looks like something went wrong.  Let's try your name again. ")

    def new_user(self, user):
        print("Fantastic! Ready for us to help you take over the world?")
        investment = input("First off we'd like to ask how much you've already invested: ")
        while True:
            try: 
                investment = int(investment)
                break
            except:
                investment = input(txt["wrong_num"])
        self.create_owner(user)
        prop_num = input("Now how many properties have you invested in? ")
        while True:
            try: 
                prop_num = int(prop_num)
                break
            except:
                prop_num = input(txt["wrong_num"])
        for properties in range(prop_num):
            self.create_property(user)
            if prop_num > 1:
                finish = input("""We have put together your property. Would you 
    like to [Input] specifics or [Continue] putting together properties? """).lower().strip()
                while True:
                    if finish in  ['i', 'input']:
                        self.expenses
                        break
                    elif finish in ['c', 'continue', 'con']:
                        break
                    else:
                        print("What was that again? [Input] or [Continue]:")
                


    def expenses(self, prop_name, unit_num):                    
        expense_method = input("""What format would you like to give us expenses in? 
    (L)ump: expenses for the property
    (p)ercentage: We'll base our expenses off a percentage of the rent.
    (S)et: choose specific numbers for individual units.
    (W)ait: put your portfolio together, then adjust the numbers.""").lower().strip()
        while True:
            if expense_method in ['l', 'lump']:
                lump_expenses = self.lump_expense_get()
            elif expense_method in ['p', 'percentage']:
                pass
                
        if lump_expenses:
            lump_expenses = [expense/ unit_num for expense in lump_expenses]
        
    def lump_expense_get(self):
        while True:
            try:
                monthly_insurance = int(input("How much is your monthly insurance cost?"))
                monthly_utilities = int(input("How much is your monthly utilities cost?"))
                monthly_lawncare = int(input("How much is your monthly lawncare cost?"))
                monthly_mortgage = int(input("How much is your monthly mortgage cost?"))
                monthly_vacancy = int(input("How much is your monthly vacancy budget?"))
                monthly_repairs = int(input("How much is your monthly repairs budget?"))
                monthly_cap_x = int(input("How much is your monthly Capital Expenditure budget?"))
                monthly_prop_man = int(input("How much is your monthly property management budget?"))
                expense_list = [ monthly_insurance, monthly_utilities, monthly_lawncare, monthly_mortgage, monthly_vacancy, monthly_repairs, monthly_cap_x, monthly_prop_man]
                return expense_list
            except:
                quit = input("One of those numbers didn't work. Let's try this again. Skip this step by hitting (W).").lower().strip()
                if quit == 'w':
                    break
        