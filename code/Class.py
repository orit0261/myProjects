class Employee():
    my_salary = 50000
    emp_Number = 0
    def __init__(self,name,salary):
        Employee.emp_Number+=1
        self.name = name
        self.salary = salary
        self.emp_num= Employee.emp_Number
        print(f'new employee created! employee num: {Employee.emp_Number}')

    def get_employee_details(self):
        new_str = f'name: {self.name}\t salary: {self.salary:,}\t emp_num:{self.emp_num}'
        return new_str

    def __del__(self):
        Employee.emp_Number-=1


emp01 = Employee('bill',12345)
emp02 = Employee('john',20000)
print(emp01.get_employee_details())
print(emp02.get_employee_details())
print("number of employees:",Employee.emp_Number)
print(emp01.my_salary)

emp01.my_salary= 8
print('emp01.my_salary',emp01.my_salary)

print('emp02.my_salary',emp02.my_salary)
Employee.my_salary=9
print('emp01.my_salary',emp01.my_salary)
print('emp02.my_salary',emp02.my_salary)
print('Employee.my_salary',Employee.my_salary)


print(emp01.get_employee_details())
print(emp02.get_employee_details())


del(emp01)
print("number of employees:",Employee.emp_Number)
del(emp02)
print("number of employees:",Employee.emp_Number)
