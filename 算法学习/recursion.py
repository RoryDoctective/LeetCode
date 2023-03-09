def max_l(l, left, right):
    if left == right:
        return l[left]
    mid = (right - left >> 1) + left
    ll = max_l(l, left, mid)
    rr = max_l(l, mid + 1, right)
    return max(ll, rr)

# 小和问题
def merge_sort_mod(l):
    left = 0
    right = len(l)
    if right == 1:
        return l, 0
    mid = (right - left >> 1) + left
    list_l, sum_l = merge_sort_mod(l[:mid])
    list_r, sum_r = merge_sort_mod(l[mid:])
    temp_list, temp_num = merge_mod(list_l, list_r)
    # 这里，左半边得小和+右边得小和+merge得小和 = 整个的小和
    return temp_list, temp_num + sum_l + sum_r


def merge_mod(ll, rr):
    p1 = 0
    p2 = 0
    length_l = len(ll)
    length_r = len(rr)
    final = []
    count = 0
    while True:
        if p1 > length_l - 1:
            final.extend(rr[p2:])
            break
        if p2 > length_r - 1:
            final.extend(ll[p1:])
            break

        if ll[p1] >= rr[p2]: # here must be >=,不可以，=，先后顺序matters
            final.append(rr[p2])
            p2 += 1
        else:
            final.append(ll[p1])
            # count
            # here comes the difference,不仅仅加index得差数，还必须乘左pointer
            count = count + (length_r - p2 )*ll[p1]
            # print(length_r - p2)
            p1 += 1
    return final, count


# 逆序对问题
def merge_sort_mod_(l):
    left = 0
    right = len(l)
    if right == 1:
        return l, 0
    mid = (right - left >> 1) + left
    list_l, sum_l = merge_sort_mod_(l[:mid])
    list_r, sum_r = merge_sort_mod_(l[mid:])
    temp_list, temp_num = merge_mod_(list_l, list_r)
    # 这里，左半边得逆序对+右边得逆序对+merge得逆序对 = 整个的逆序对
    return temp_list, temp_num + sum_l + sum_r


def merge_mod_(ll, rr):
    p1 = 0
    p2 = 0
    length_l = len(ll)
    length_r = len(rr)
    final = []
    count = 0
    while True:
        if p1 > length_l - 1:
            final.extend(rr[p2:])
            break
        if p2 > length_r - 1:
            final.extend(ll[p1:])
            break

        if ll[p1] <= rr[p2]:  # here must be <=,不可以，=，先后顺序matters
            final.append(ll[p1])
            p1 += 1
        else:
            final.append(rr[p2])
            # 问的是个数 = 1 * (左边index得差数)
            count = count + length_l - p1
            p2 += 1
    return final, count

A = merge_sort_mod_([3, 2, 5, 6, 7, 4, 1])
print(A)
A = merge_sort_mod_([1, 3, 4, 2, 5])
print(A)
A = merge_sort_mod_([3, 2, 4, 5, 0])
print(A)
