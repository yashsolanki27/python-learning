# parent class Employee
# Every Employee has three common properties
class Employee:

    # constructor --run auto when Employee object is called
    def __init__(self, name, emp_id):
        self.name = name  # stores employees name inside the obj
        self.emp_id = emp_id  # stores employees unique id no. inside the obj

    # common method available to all child classes
    def show_info(self):
        print("Name: ", self.name)
        print("Employee Id: ", self.emp_id)
