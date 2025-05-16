"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":
        if len(args) >= 1:
            students.append(args[0])

    elif operation == "remove":
        if len(args) >= 1 and args[0] in students:
            students.remove(args[0])

    elif operation == "update":
        # 这里根据测试用例改为通过旧名字找到索引并替换为新名字
        if len(args) >= 2:
            old_name, new_name = args[0], args[1]
            if old_name in students:
                index = students.index(old_name)
                students[index] = new_name

    return students

    pass 