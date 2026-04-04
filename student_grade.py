# 学生成绩管理系统
# 使用字典列表存储学生信息，每个学生是一个字典，包含姓名和成绩
students = []


def show_menu():
    """显示主菜单"""
    print("\n=====学生成绩管理系统=====")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改成绩")
    print("4. 查询成绩")
    print("5. 统计信息")
    print("6. 显示所有学生")
    print("7. 退出")
    print("=====================")


def find_student(name):
    """查找学生，返回学生在列表中的索引，如果没找到返回-1"""
    for i, student in enumerate(students):
        if student['name'] == name:
            return i
    return -1


def get_valid_score():
    """获取有效的成绩输入"""
    while True:
        score = input("请输入学生成绩（0-100）：")
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 100:
                return score
            else:
                print("成绩必须在0-100之间！")
        else:
            print("成绩必须是数字！")


def add_student():
    """添加学生"""
    name = input("请输入学生姓名：")
    # 检查学生是否已存在
    if find_student(name) != -1:
        print(f"学生{name}已存在！")
        return
    
    score = get_valid_score()
    students.append({'name': name, 'score': score})
    print(f"恭喜！学生{name}已添加，成绩{score}！")


def delete_student():
    """删除学生"""
    name = input("请输入要删除的学生姓名：")
    index = find_student(name)
    if index != -1:
        students.pop(index)
        print(f"学生{name}已被删除")
    else:
        print("未找到该学生")


def modify_score():
    """修改学生成绩"""
    name = input("请输入需要修改成绩的学生姓名：")
    index = find_student(name)
    if index != -1:
        new_score = get_valid_score()
        students[index]['score'] = new_score
        print(f"学生{name}的成绩已修改为{new_score}。")
    else:
        print("未找到该学生")


def query_score():
    """查询学生成绩"""
    name = input("请输入需要查询成绩的学生姓名：")
    index = find_student(name)
    if index != -1:
        print(f"学生{name}的成绩为{students[index]['score']}。")
    else:
        print("未找到该学生")


def show_statistics():
    """显示统计信息"""
    if not students:
        print("暂无学生数据")
        return
    
    scores = [student['score'] for student in students]
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    
    print(f"最高分为：{max_score}")
    print(f"最低分为：{min_score}")
    print(f"平均分为：{avg_score:.2f}")  # 保留两位小数


def show_all_students():
    """显示所有学生信息"""
    if not students:
        print("暂无学生数据")
        return
    
    print("-----学生成绩列表-----")
    for student in students:
        print(f"{student['name']}: {student['score']}")


# 主循环
while True:
    show_menu()
    choice = input("请选择操作（1-7）：")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        modify_score()
    elif choice == "4":
        query_score()
    elif choice == "5":
        show_statistics()
    elif choice == "6":
        show_all_students()
    elif choice == "7":
        print("感谢使用，再见！")
        break
    else:
        print("请输入有效的数字（1-7）")
        