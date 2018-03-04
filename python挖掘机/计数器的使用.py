# 1.python函数定义在运行时，会创建一个 add函数对象（唯一），在当前namespace，所有的add name都指向这个唯一函数对象。 
# 2. 由于_rel参数是一个list，mutable类型，其他任何_rel的使用都是对于这个list对象的引用 一般参数传递mutable对象要谨慎，在这种需求环境下使用是非常精妙的


def add(val,_rel=[0]):
    _rel[0]+=val
    return _rel[0]
for i in range(10):
    c=add(1)
    print(c)



