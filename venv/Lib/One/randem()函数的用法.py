#导包
import random;
#random会生成返回一个0~1的随机数
print("返回一个0~1的随机实数：", random.random())
print("产生一个1~10的一个整数型随机实数", random.randint(1, 10))
print("产生一个1.1~5.4之间的浮点数，区间可以不是整数", random.uniform(1.1, 5.4))
print("在gengdan里面随机读取到一个元素：", random.choice("gengdan"))
print("随机读取字符串：", random.choice(["剪刀", "石头", "布"]))
print("生成1~100的间隔为2的随机整数：", random.randrange(1, 100, 2))
print("将序列a中的元素打乱：")
a = [1, 3, 5, 7, 9]
print("原始列表：", a)
random.shuffle(a)
print("打乱后的列表：", a)
