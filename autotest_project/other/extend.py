"""
概念：一个新类从已有类获得其所有变量和所有函数，称为继承
"""

class Animal:
    name="huahua"
    age=0
    def sleep(self):
        print("animal sleep()")

class Cat(Animal):
    def showInfo(self):
        print(self.name)
        print(self.age)
        self.sleep()


cat=Cat()
cat.showInfo()