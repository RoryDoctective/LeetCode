def find_num(l, num):
    n = len(l)
    left = 0
    right = n - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2  # = math.flor()
        count += 1
        print(mid)
        if num == l[mid]:
            return True, count
        elif num < l[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False, count


# >=某个数 最左侧的位置
def find_pos(l, num):
    n = len(l)
    left = 0
    right = n
    correct = n + 1
    wrong = -1
    while correct - wrong != 1:
        mid = (left + right) // 2
        if l[mid] >= num:
            correct = mid
            right = correct - 1
        else:
            wrong = mid
            left = wrong + 1

    return correct

def find_region_small(l):
    # check left
    if l[0] < l[1]:
        return l[0]
    left = 0

    # check right
    n = len(l)
    if l[n-2] > l[n-1]:
        return l[n-1]
    right = n-1

    # 开始
    while left <= right:
        mid = (right+left)//2
        ll = l[mid-1]
        mm = l[mid]
        rr = l[mid+1]
        if ll > mm and mm < rr:
            return mm
        elif ll < mm:
            right = mid-1
        else:
            left = mid+1
    return -1



l = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5]

p = find_pos(l, 5)
print(p)
print(l[p - 1], l[p], l[p + 1])

l = [6,5,5,4,4,3,3,2,1,-10,6]
print(find_region_small(l))
