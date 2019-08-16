import numpy as np
import random
import pysnooper

@pysnooper.snoop()
def argmax(a):
    pos = -1
    a_max = max(a)
    counts = a.count(a_max)
    index = [0] * counts
    for i in range(counts):
        pos = a.index(a_max, pos + 1)
        index[i] = pos
    choose_index = random.randint(0, counts - 1)
    out = index[choose_index]
    return out
a = [2,3,4,5,6,6,6,6,6,6]
print(argmax(a))

    # counts = org.count(x)   #先求出org中包含x的个数
    # if counts == 0:    #个数为0，说明不存在x
    #     print(org, '中没有', x)
    # elif counts == 1:   #个数为1，说明结果唯一，直接返回index(x)
    #     print(org.index(x))
    # else:
    #     '''
    #     个数大于1时，从下标为0的位置开始查找
    #     找到一个后，先打印下标位置，再从该位置的下一个位置开始继续查找
    #     '''
    #     for i in range(counts):
    #         pos = org.index(x, pos + 1)
    #         print(pos,end=' ')
    #     print()
# org = [1, 2, 2, 33, 2, 4, 5, 2]
# findindex(org, 3)
# findindex(org, 2)