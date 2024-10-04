class Registration:
    def __init__(self, names, registration_number, email):
        self.name = names
        self.registration_number = registration_number
        self.email = email

    def register_student(self):
        if self.registration_number.startswith("B2"):
            print(f"Student {self.name} with registration number {self.registration_number} has been registered.")
            return self.name, self.registration_number
           
        else:
            print("Incorrect registration number.")
        

    def display_info(self):
            # print("REGISTERED STUDENT'S INFORMATION")
            return(f"Name: {self.name}, Registration Number: {self.registration_number}, Email: {self.email}")



student1 = Registration("Aber Charity", "B20244", "abercharity11@email.com")
student2 = Registration("Laker Joana", "B20249", "LJdove23@email.com")
student3 = Registration("Josh Kata", "S20302", "Jos.k@email.com")
student4 = Registration("Godfrey Ross", "B20598", "godross8@gmail.com")

student1.register_student()
student2.register_student()
student3.register_student()
student4.register_student()


# student1.display_info()
# student2.display_info()
# student3.display_info()
# student4.display_info()


students = [student1, student2, student4]

print("REGISTERED STUDENTS' INFORMATION")
for student in students:
 print(student.display_info())
          
          




          

        