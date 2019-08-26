

__author__= "nash"

w_rate = 3.9
e_rate = 0.5

class Calculate(object):

    def __init__(self, water_bill, electric_bill ):
        self.water = water_bill
        self.electric = electric_bill

    @staticmethod
    def water_bill_kit(new_meter, old_meter):
        bill_diff = int(new_meter) - int(old_meter)
        bill = bill_diff * w_rate
        return bill
    
    @staticmethod
    def water_bill_bath(new_meter, old_meter):
        bill_diff = int(new_meter) - int(old_meter)
        bill = bill_diff * w_rate
        return bill

    @staticmethod
    def electric_bill(new_meter, old_meter):
        bill_diff = int(new_meter) - int(old_meter)
        bill = bill_diff * e_rate
        return bill
    
    



