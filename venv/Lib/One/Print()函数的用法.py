#输出一段文字并换行
print('Hello world')
#输出真实学号和姓名
print("我的学号：" + "180809216" + "我的姓名：" + "王国礼")
#输出空行
print()
#输出数字
print(393)
#输出表达式计算结果
print(45 + 29)
#字符串连接
print("您好" + "老师！")
#用逗号连接多个输出，中间用空格分隔
print("我有几个朋友" , 2, 3, 4, 5)
#指定分隔符
print(45, 45, 67, 87,sep = ":")
#printm默认换行，默认end的值是\n，如果需要打印不换行，那就把它改成其他的字符
print(1, 2, 3, 4, 5, end=";")
print(end = "\n")
#str()把数值转换为字符串
print("今天第几周：" + str(1))
#保留两位小数 方法1：
print("%.2f" % 3.141592654)
#保留两位小数 方法2：
print("{:.2f}".format(3.141592654))
#保留两位小数 方法3：
print(round(3.141592654, 2))
#向文件中写入数据
with open("text", "w", encoding="utf-8") as f:
    print("我正在文件中写入数据：\n", "Hello world", "\nSee you!", sep="########", end="", file=f)
#读取文件中的类容并输出
with open("text", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
