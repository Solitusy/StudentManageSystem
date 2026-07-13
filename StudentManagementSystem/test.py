students = [
    {
        "id": "2024001",
        "name": "张三",
        "math": 90,
        "english": 88,
        "python": 95
    },
    {
        "id": "2024002",
        "name": "李四",
        "math": 85,
        "english": 91,
        "python": 89
    }
]

for student in students:
    print(f"学号：{student['id']}")
    print(f"姓名：{student['name']}")
    print(f"数学：{student['math']}")
    print(f"英语：{student['english']}")
    print(f"Python：{student['python']}")
    print("-" * 30)