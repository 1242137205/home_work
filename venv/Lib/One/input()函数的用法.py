#在python3.x中的input（）接受一个标准的输入数据， 返回为 string类型的数据
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
#如果要转换为数值类型a = eval（input（"请输入："））
#强制类型转换 b = int（input（"请输入："））
os = eval(input("请输入您操作系统的成绩："))
py = int(input("请输入您python的成绩："))
salary = eval(input("请输入您暑假实习工资："))
#输出：
print("您的姓名", name)
print("您的年龄：", age)
print("您的操作系统成绩：", os)
print("您的Python成绩：", py)
print("您的平均成绩为：", (os + py) /2)
print("您的暑假工资为：", salary)