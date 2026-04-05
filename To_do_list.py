# 初始化全局变量
to_do_list = {}

def show_menu():
    print("\n-----代办事项管理系统------")
    print("1. 添加代办")
    print("2. 查看代办")
    print("3. 标记完成代办")
    print("4. 删除代办")
    print("5. 退出系统")
    print("------------------------")

def add_to_do_list():
    global to_do_list
    name = input("请输入代办事项：")
    if name in to_do_list:
        print("该代办事项已存在！")
    else:
        to_do_list[name] = False
        print("添加成功")

def view_to_do_list():
    global to_do_list
    if not to_do_list:
        print("暂无代办事项")
    else:
        print("\n当前代办事项：")
        for name, done in to_do_list.items():
            print(f"{name}: {'已' if done else '未'}完成")

def mark_done():
    global to_do_list
    name = input("请输入要标记完成的代办事项：")
    if name in to_do_list:
        to_do_list[name] = True
        print(f"已标记'{name}'为完成")
    else:
        print("未找到该代办事项")

def delete_to_do():
    global to_do_list
    name = input("请输入要删除的代办事项：")
    if name in to_do_list:
        del to_do_list[name]
        print(f"已删除代办事项'{name}'")
    else:
        print("未找到该代办事项")

# 主循环
def main():
    while True:
        show_menu()
        choice = input("请选择操作（1-5）：")
        
        if choice == "1":
            add_to_do_list()
        elif choice == "2":
            view_to_do_list()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_to_do()
        elif choice == "5":
            print("感谢使用，再见！")
            break
        else:
            print("请输入有效的数字（1-5）")

# 运行主函数
if __name__ == "__main__":
    main()
