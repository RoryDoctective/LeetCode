def max_l(l, left, right):
    if left == right:
        return l[left]
    mid = (right - left >> 1) + left
    ll = max_l(l, left, mid)
    rr = max_l(l, mid + 1, right)
    return max(ll,rr)

A = max_l([3,2,5,6,7,4,1], 0, 6)
print(A)
