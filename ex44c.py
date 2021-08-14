# 在运行前或运行后替换
# 如果想在父类中定义的内容运行之前或者之后再修改行为.
# 可以覆盖函数,再接着用super来调用父类的版本
class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()
