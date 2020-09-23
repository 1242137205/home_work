#format()函数的用法
print("{} {}".format("hello", "world"))#不指定位置，按默认顺序
print("{0} {1}".format("hello", "world"))#设置指定位置
print("{0} {1} {0}".format("hello", "world"))#设置指定位置
print("网站名：{name}, 网站地址：{url}".format(name = "耿丹学院~~~", url="www.gengdan.cn"))
#通过字典设置参数
site = {"name":"耿丹学院~~", "url":"www.gengdan.cn"}
print("网站名：{name}, 网站地址：{url}".format(**site))
#通过列表索引设置参数
my_list = ["耿丹学院~", "www.gengdan.cn"]
print("网站名：{0[0]}, 网站：{0[1]}".format(my_list))#0是必须的
# str.format()格式化数字
print("{:.2f}".format(3.141592654))  #保留小数点后两位
print("{:+.2f}".format(3.141592654))    #带符号保留小数点后两位
print("{:+.0f}".format(3.141592654))    #不带小数
print("{:0>10d}".format(12345)) #数字补零（填充左边，宽度为10）
print("{:x<10d}".format(12345)) #数字补X（填充右边，宽度为10）
print("{:,}".format(12345)) #以逗号分隔的数字形式
print("{:.2%}".format(0.25678))#百分比格式
print("{:.2e}".format(123456))#指数计发
print("{:>10d}".format(12345))#右对其（默认宽度为10，左边边补空格）
print("{:<10d}".format(12345))#左对齐（宽度为10，右边补空格）
print("{:^10d}".format(12345))#中间对齐（宽度为10，左右补空格）

#b, d, o, x 分别是二进制，十进制，八进制，十六进制
print("{:b}".format(11)) #二进制1101
print("{:d}".format(11))    #十进制11
print("{:o}".format(11))    #八进制13
print("{:x}".format(31))    #十六进制1f

#可以用大括号{}来转义大括号
print("{} 对应的位置是 {{0}}".format("gengdan"))

