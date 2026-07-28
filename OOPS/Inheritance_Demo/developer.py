from employee import Employee


class Developer(Employee):

    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language

    # method only available for developer
    def show_experties(self):
        print(self.name, "is expert in coding in", self.programming_language)
