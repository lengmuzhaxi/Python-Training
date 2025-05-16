"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    if operation == "add":
        name, score = args
        students_dict[name] = score
        return students_dict
    
    elif operation == "remove":
        name = args[0]
        students_dict.pop(name, None)
        return students_dict
    
    elif operation == "update":
        name, new_score = args
        if name in students_dict:
            students_dict[name] = new_score
        return students_dict
    
    elif operation == "get":
        name = args[0]
        return students_dict.get(name, None)
    else:
        return None
    pass 