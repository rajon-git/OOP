class Student:
    def __init__(self,name,id,current_class):
        self.name=name 
        self.id=id
        self.current_class=current_class

    def __repr__(self) -> str:
        return f"Student with name: {self.name}, Class: {self.current_class}, id: {self.id}"
    
class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id
    def __repr__(self) -> str:
        return f"Teacher with name: {self.name}, Subject: {self.subject}, id: {self.id}"

class School:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
    def enroll(self,name,fee):
        if fee > 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name,'C',id)
            self.students.append(student)
            return f"{name} enroll with id: {id}, extra money: {fee - 6500}"
        
    def __repr__(self) -> str:
        print('Welcome to:', self.name)
        print('-------------Our Teachers--------------')
        for teacher in self.teachers:
            print(teacher)
        print('-------------Our Students--------------')
        for student in self.students:
            print(student)

        return 'All Done For Now'

# alia = Student('Alia',4,'Ten')
# ranbeer = Teacher('Ranbir','Math',101)
# print(alia)
# print(ranbeer)

phitron = School('Phitron', 'Dhaka')
phitron.enroll('Alia', 5200)
phitron.enroll('Rani', 7000)
phitron.enroll('Alia', 5200)

phitron.add_teacher('Rajon','Algorithm')
phitron.add_teacher('Rakib','DS')
phitron.add_teacher('Rajon2','Graph')

print(phitron)