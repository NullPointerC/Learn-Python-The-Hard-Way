# 模块,类和对象
# 模块(module)
# 1.模块是包含函数和变量的Python文件
# 2.可以导入这个文件
# 3.然后可以使用,操作符访问模块中的函数和变量
# Python里面有一个非常常用的模式
# 1.拿一个类似"键=值"风格的容器;
# 2.通过"键"的名称获取其中的值
# 对于字典来说,获得值的语法是"[key]".对于模块来说,key是函数或者变量的名称,而语法是".key"
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
