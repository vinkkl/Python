"""
Allowances:
HRA - 10000
Allowance - 15000
Deduction:
insurance - 20000
SchoolFees - 5000

Tax:

Calculation :
gross - Allowances
Net -> gross - deduction + tax
"""

class BasicSalary:
    def __init__(self,sal):
        self.sal=sal

class BasicAllowances(BasicSalary):


    def allowance(self):
        allowance_list = {"HRA": 30000, "allowance": 20000}
        total_allowance = 0
       # total_allowance = BasicAllowances.allowance_list["HRA"] + BasicAllowances.allowance_list["allowance"]
        total_allowance = allowance_list["HRA"] + allowance_list["allowance"]
        return total_allowance

    def deduction(self):
        deduction_list = {"insurance":20000, "school_fees" :24000}
        total_deduction = 0
        total_deduction = deduction_list["insurance"] + deduction_list["school_fees"]
        return  total_deduction
class GrossSalary(BasicAllowances):

    def Display(self):
        net = BasicAllowances.allowance(self) - BasicAllowances.deduction(self)
        print(net)


basic = BasicSalary(100)
salary=BasicAllowances(100)
grossalary= GrossSalary(salary)
salary.allowance()
grossalary.Display()



