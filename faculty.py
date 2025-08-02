class Faculty:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def calculate_pay(self):
        raise NotImplementedError("Subclasses should implement this method")

class ParttimeFaculty(Faculty):
    def __init__(self, first_name, last_name, id, classes):
        super().__init__(first_name, last_name, id)
        self.classes = classes
    
    def calculate_pay(self):
        return 1000 * self.classes
    
class SalaryFaculty(Faculty):
    def __init__(self, first_name, last_name, id, salary):
        super().__init__(first_name, last_name, id)
        self.salary = salary
    
    def calculate_pay(self):
        return self.salary
    
class HourlyFaculty(Faculty):
    def __init__(self, first_name, last_name, id, hours_worked, hourly_rate):
        super().__init__(first_name, last_name, id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate