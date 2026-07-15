from student import Student
from manager import StudentManager
manager = StudentManager()
while True:
    print("====== 学生管理系统 ======")
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 删除学生")
    print("4. 修改学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出系统")
    choice = input("请输入操作编号: ")
    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.search_student()
    elif choice == "3":
        manager.delete_student()
    elif choice == "4":
        manager.update_student()
    elif choice == "5":
        manager.display_students()
    elif choice == "6":
        break
    else:
        print("无效的操作编号，请重新输入。")