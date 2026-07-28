class Student:  # class created

    # constructor initalize object data
    def __init__(self, name, age):
        self.name = name  # store name in the object
        self.age = age  # store age in the object

    # method to display student details
    def display(self):
        print(self.name)
        print(self.age)


# objects created
student1 = Student("Alex Stienner", 27)
student2 = Student("Yash SOLANKI", 28)

# calling the display method/function

student1.display()
student2.display()
