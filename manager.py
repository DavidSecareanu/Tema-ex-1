from employee import Employee

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, tasks, department):
        super().__init__(name, salary)
        self.tasks = tasks
        self.department = "F29" + department
        Manager.mgr_count += 1


    def display_employee(self):
        print("Name : ", self.name)




m1 = Manager("Ana", 5000, ["review", "report"], "HR")
m2 = Manager("Mihai", 6000, ["planning"], "IT")
m3 = Manager("Ioana", 5500, ["budget"], "Finance")

e1 = Employee("Alex", 3000)
e2 = Employee("Maria", 3200)

m1.display_employee()
m2.display_employee()
m3.display_employee()

e1.display_employee()
e2.display_employee()

e1.display_emp_count()
m1.display_emp_count()
print("Total number of managers is: ", m1.mgr_count)


#X = 5
#Y = 9
#X % 5 = 1
#Y / 3 = 9



