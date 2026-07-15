from student import Student


class StudentManager:
    def __init__(self):
        self.students = []
        
    def add_student(self):
        name = input("输入名字")
        age = int(input("输入年龄: "))
        id = input("输入学生ID: ")
        major = input("输入学生专业: ")
        student = Student(name, age, id, major)
        self.students.append(student) 
        print("添加成功")
   