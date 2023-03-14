# 几乎有序得数组

import heapq
# 利用heapq
def heapq_nearly_sort(l, k):
    # make a heap
    a = l[:k]
    heapq.heapify(a)

    # add one pop one
    res = []
    p2 = k
    while p2 < len(l):
        res.append(heapq.heapreplace(a, l[p2]))
        p2 += 1

    # pop all
    while a:
        res.append(heapq.heappop(a))

    return res


# 纯手写
def heap_nearly_sort(l, k):
    '''
    :param l:小根堆！
    :param k:
    :return:
    '''
    # all in: insert 和 heapify 二选一
    for i in reversed(range(k)):
        # 0, 1, 2, 3
        l = heapify_small(l, i, k)

    # plus
    heap = l[:k]
    p2 = k
    res = []
    while p2 < len(l):
        # pop
        res.append(heap[0])
        heap[0] = l[p2]

        # push
        heap = heapify_small(heap, 0, k)
        p2 += 1

    # all pop
    while True:
        res.append(heap[0])
        # maintain
        temp = heap.pop()  # pop the last
        if heap:
            heap[0] = temp  # make last the first
            heap = heapify_small(heap, 0, len(heap))  # do insert
        else:
            break

    return res


def heap_insert_small(l, index):  # mod to 小根堆
    '''
    l = 数组/heap
    index = 这个insert得数字所在的位置
    *放在最后，往上看爹
    '''
    father_index = int((index - 1) / 2)
    while l[index] < l[father_index]:
        l[index], l[father_index] = l[father_index], l[index]
        index = father_index
        father_index = int((index - 1) / 2)
    return l


def heapify_small(l, index, heap_size):  # mod to 小根堆
    '''
    l = 数组/heap
    index = 这个新换来的得数字所在的位置
    heap_size = len(l)
    *放在最上，往下看孩子
    return： l
    '''
    left_child = 2 * index + 1

    while left_child <= heap_size - 1:

        # 1. find small among left/ right
        left = l[left_child]
        right_child = 2 * index + 2
        if right_child <= heap_size - 1:
            # right child exist
            if left < l[right_child]:
                largest = left_child
            else:
                largest = right_child
        else:
            # right child NOT exist
            largest = left_child

        # 2. find biggest among left/ right / father
        father = l[index]
        if father <= l[largest]:
            largest = index

        # 3. 最大的不是父亲就得swap
        if largest != index:
            l[index], l[largest] = l[largest], l[index]
            index = largest
            left_child = 2 * index + 1
        else:
            # 3. 最大的是父亲就得停
            break
    return l


# A = heap_insert([7, 7, 5, 3, 6, 8], 5)
# print(A)
#
# B = heapify([0, 8, 7, 3, 6, 1], 0, 5)
# print(B)
#
# C = heapify([4, 4, 5, 1, 3, 2, 9], 0, 5)
# print(C)

D = heapq_nearly_sort([2,3,0,1,5,4,6], 3)
print(D)