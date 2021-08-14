# 显示覆盖
# 隐式调用函数有一个问题,有时候需要让子类中的函数有不同的行为,这种情况下隐式继承是做不到的
# 这时需要覆盖子类中的函数,让他实现新功能
class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

dad.override()
son.override()
