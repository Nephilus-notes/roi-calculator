


class Unit():
    def __init__(self, rent, parking_cost, repairs, laundry, taxes) -> None:
        self.rent
        self.parking_cost
        self.repairs
        self.laundry
        self.taxes

    @classmethod
    def create_unit(cls):
        user_rent = input('rent: ')
        try:
            user_rent = int(user_rent)
        except:
            user_rent = input("try again: ")

        new_unit = cls(user_rent)

        user_parking_cost = input('How much is the parking cost? ')
        # try and except blocks
        new_unit.parking_cost = user_parking_cost


        return new_unit

unit = Unit.create_unit()