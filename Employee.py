#TASK 4: METHOD OVERRIDING
class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def work(self):
        print("Manager is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

#creating objects
manager = Manager()
developer = Developer()


#calling the method
manager.work()
developer.work()
 