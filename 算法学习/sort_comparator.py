import random


def random_list(max_len, max_num):
    # [0,1) -> [0,n) -> [0, n-1]
    length = int(random.random() * max_len)
    li = []
    for i in range(length):
        li.append(int(random.random() * max_num))
    return li


def comparator(exp_num=5):
    max_len = 100
    max_num = 200
    correct = True
    for i in range(exp_num):
        li = random_list(max_len, max_num)
        l1 = selection_sort(li)
        l2 = bubble_sort(li)
        if l1 != l2:
            print(li)
            print(l1)
            print(l2)
            correct = False
            break

    if correct:
        print("win!")
    else:
        print("you fucked up.")


def selection_sort(l):
    for i in range(len(l) - 1):  # 0 - n-1
        small = 99999999999
        index = -1
        for j in range(i, len(l)):  # i - n-1
            if l[j] < small:
                small = l[j]
                index = j
        # swap
        l[i], l[index] = l[index], l[i]
    return l


def bubble_sort(l):
    # l = [9, 4, 2, 1, 3, 4, 5]

    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                # swap
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def insertion_sort(l):
    for i in range(len(l)):  # 0 - n
        # 前i位 ok
        # num = l[i]
        for j in reversed(range(i)):  # i - 0
            if l[j] > l[j + 1]:
                # swap
                l[j], l[j + 1] = l[j + 1], l[j]
            else:
                break
    return l


def merge_sort(l):
    left = 0
    right = len(l)
    if right == 1:
        return l
    mid = (right - left >> 1) + left
    list_l = merge_sort(l[:mid])
    list_r = merge_sort(l[mid:])
    return merge(list_l, list_r)


def merge(ll, rr):
    p1 = 0
    p2 = 0
    length_l = len(ll)
    length_r = len(rr)
    final = []
    while True:
        if p1 > length_l - 1:
            final.extend(rr[p2:])
            break
        if p2 > length_r - 1:
            final.extend(ll[p1:])
            break

        if ll[p1] >= rr[p2]:
            final.append(rr[p2])
            p2 += 1
        else:
            final.append(ll[p1])
            p1 += 1
    return final


def quick_sort(l):
    length = len(l)
    if length <= 1:
        return l
    # 随机出一个pivot
    p = int(random.random()*(length-1))
    # 3pointers 把p放对位置
    l, p1, p2 = partition(l, l[p])
    # recursion
    l_l = quick_sort(l[:p1])
    l_r = quick_sort(l[p2+1:])
    # get the l
    l[:p1] = l_l
    l[p2+1:] = l_r
    return l

def partition(l, target):
    # modified triple_pointers
    if len(l) <= 1:
        return l, 0, 0
    p1 = p2 = 0
    p3 = len(l) - 1
    while p2 <= p3:
        if l[p2] < target:
            l[p1], l[p2] = l[p2], l[p1]
            p1 += 1
            p2 += 1
        elif l[p2] == target:
            p2 += 1
        else:  # if l[p2]> target
            l[p3], l[p2] = l[p2], l[p3]
            p3 -= 1
    # return p1 p3
    return l, p1, p3


def heap_sort(l):
    # add one by one
    for i in range(len(l)):
        l = heap_insert(l, i)

    # take away one by one
    for i in reversed(range(len(l))):
        # for each run, the l[i] is in correct place
        l[0], l[i] = l[i], l[0]
        l = heapify(l, 0, i-1)

    return l


def heap_insert(l, index):
    '''
    l = 数组/heap
    index = 这个insert得数字所在的位置
    *放在最后，往上看爹
    '''
    father_index = int((index - 1) / 2)
    while l[index] > l[father_index]:
        l[index], l[father_index] = l[father_index], l[index]
        index = father_index
        father_index = int((index - 1) / 2)
    return l


def heapify(l, index, heap_size):
    '''
    l = 数组/heap
    index = 这个新换来的得数字所在的位置
    heap_size = len(l)-1
    *放在最上，往下看孩子
    return： l
    '''
    left_child = 2 * index + 1

    while left_child <= heap_size-1:

        # 1. find biggest among left/ right
        left = l[left_child]
        right_child = 2 * index + 2
        if right_child <= heap_size-1:
            # right child exist
            if left > l[right_child]:
                largest = left_child
            else:
                largest = right_child
        else:
            # right child NOT exist
            largest = left_child

        # 2. find biggest among left/ right / father
        father = l[index]
        if father >= l[largest]:
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

'''
l = [9, 4, 2, 1, 3, 4, 5]

l1 = selection_sort(l)

l1 = bubble_sort(l)

l3 = insertion_sort(l)

l4 = merge_sort(l)

comparator(10000)
'''
l = [9, 4, 2, 1, 3, 4, 5]
print(quick_sort(l))
print(heap_sort(l))
