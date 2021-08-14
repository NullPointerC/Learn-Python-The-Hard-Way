# 隐式继承
# 在父类中定义了一个函数但没有在子类中定义时会发生的隐式行为
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
# 此函数依然可以工作,调用了父类中定义的这个函数
son.implicit()
