"""
构造函数又称构造方法，构造器
作用：创建对象时调用，用来初始化对象数据
构造函数特点：当类中无显式创建构造函数时，系统会自动生成一个无参构造函数。
return 结束函数执行的关键字
有参数构造函数：
    def __init__(self):
        语句
有参数构造函数：
    def __init(self,参数1,参数2)
        语句
"""

class Cat:
    age=0
    name=""
    def sleep(self):
        print("sleep()")

    def __init__(self):
        self.name="喵喵"
        self.age=2
        print("无参数构造函数执行")

cat=Cat()
print(cat.name)
print(cat.age)
