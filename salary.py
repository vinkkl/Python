class Salary:
    def __init__(self,bsal):
        self._bsal=bsal
    def getBasicSalary(self):
        print('Basic Salry:',self._bsal)

        
class Allowance(Salary):
    s_allowances = {"HRA":0.4,"DA":0.3,"TA":0.15}:
    
    def calcAllowance(self):
        total_allowances = 0;
        for key in self.s_allowances:
            total_allowances+=self.s_allowances[key]*self._bsal;
            return total_allowances;    

class Deductions(Salary):
    s_deductions={"pf":0.12,"insurance":5000}
    
    def calcDeductions(self):
        total_deductions = 0;
        for key in self.s_deductions:
            if type(self.s_deductions[key]) is ot int:
                total_deductions +=self.s_deductions[key]*self._bsal
             else:
                 total_deductions+=self.s_deductions[key]
         return total_deductions

class SalaryCalculator(Allowance,Deductions):
    
    def __init__(self,bsal):
        self.bsal = bsal;
        
    def getsalarydetails(self):
        super().getBasicSalary()
        super().calcAllowance()
        super().calcDeductions()
        
s1=SalaryCalculator(12000)
s1.getsalarydetails()

    
              
