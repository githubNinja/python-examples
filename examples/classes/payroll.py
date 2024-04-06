class Payroll:
    def __int__(self, name, empId):
       self.name = name
       self.empId = empId

    def print_info(self):
        print(f"Payroll details - Name:{self.name}, {self.empId}")
