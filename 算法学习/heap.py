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



A = heap_insert([7, 7, 5, 3, 6, 8], 5)
print(A)

B = heapify([0, 8, 7, 3, 6, 1], 0, 5)
print(B)

C = heapify([4, 4, 5, 1, 3, 2, 9], 0, 5)
print(C)

