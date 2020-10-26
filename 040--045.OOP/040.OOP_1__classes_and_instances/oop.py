class Employee:
    def __init__(self, first, last, payment):
        self.first = first
        self.last = last
        self.payment = payment
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Adrija', 'Bhandari', 60000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())