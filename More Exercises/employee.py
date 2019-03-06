class Employee():
    def __init__(self, first, last, salary):
        self.first =  first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=''):
        if amount == '':
            self.salary += 5000
            return self.salary

        else:
            self.salary += amount
            return self.salary

employee = Employee('n', 'm', 1)
employee.give_raise()
print (employee.salary)
