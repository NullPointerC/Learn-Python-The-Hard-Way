# 习题44 继承和组合
# 继承就是用来指明一个类的大部分或者全部功能都是从一个父类中获得的
# class Foo(Bar)    ->  创建一个叫Foo的类,并让它继承自Bar
# 使用super的原因    ->  多重继承
# 定义的类继承了一个或多个类     ->      class SuperFun(Child, BadStuff):
# 创建了一个叫SuperFun的类,让它同时继承了Child和BadStuff两个类
# 则一旦在SuperFun调用任何隐式动作,Python就必须回到两个父类中查找可能的函数
# 而且必须要用固定调度顺序去查找,为实现这一点,Python使用了一个方法解析顺序(MRO),使用C3算法
# Python给用户super函数,用来在各种需要修改行为类型的场合处理
