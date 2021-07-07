"""
内容回顾
    什么是生成器
    生成器证明定义

生成器
    生成器表达式
    在函数中使用yield关键字：生成器
    协程是通过生成器实现的多任务，在任务间不停的切换

# 协程：微线程
协程的本质上是单任务
协程依赖于线程
协程相对与线程来说，占用的资源更少，几乎不要占用什么资源
"""

import time


def work1():
    for i in range(10):
        time.sleep(0.1)
        print("---work1----{}".format(i))
        yield


def work2():
    for i in range(10):
        time.sleep(0.1)
        print("---work2----{}".format(i))
        yield


# 创建两个生成器对象,实现多任务
g1 = work1()
g2 = work2()

while True:
    try:
        next(g1)
        next(g2)
    except StopIteration:
        break
