# 双指针
def double_pointers(l, target):
    p1 = p2 = 0
    while p2 < len(l):
        if l[p2] <= target:
            l[p1], l[p2] = l[p2], l[p1]
            p1 += 1
            p2 += 1
        else: # l[p2]> target
            p2 += 1
    return l


def triple_pointers(l,target):
    p1 = p2 = 0
    p3 = len(l)-1
    while p2 <= p3:
        if l[p2] < target:
            l[p1], l[p2] = l[p2], l[p1]
            p1 += 1
            p2 += 1
        elif l[p2] == target:
            p2 += 1
        else: # if l[p2]> target
            l[p3], l[p2] = l[p2], l[p3]
            p3 -= 1
    return l


A = triple_pointers([3,5,6,7,4,3,9,3,5,5,8], 5)
print(A)