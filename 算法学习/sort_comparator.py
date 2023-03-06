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

'''
l = [9, 4, 2, 1, 3, 4, 5]

l1 = selection_sort(l)

l1 = bubble_sort(l)

l3 = insertion_sort(l)

l4 = merge_sort(l)

comparator(10000)
'''
l = [9, 4, 2, 1, 3, 4, 5]
print(merge_sort(l))
