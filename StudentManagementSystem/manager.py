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
    def search_student(self):
        id = input("输入学生ID: ")
        for student in self.students:
            if student.id == id:
                print(f"学生信息: 姓名: {student.name}, 年龄: {student.age}, ID: {student.id}, 专业: {student.major}")
                return
        print("未找到该学生信息。")
   