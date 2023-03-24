##  比较器

明文规定：cmp(a,b)

- return -1 : a 放前面
- return 1 : b 放前面
- return 0 : 无所谓

也就是说：

- ascending：a - b
- descending: b - a
- 





比较器：

- C++ —— 重载比较运算符
- Java – 告诉他两个东西怎么比较大小
- Python – 

1. #### 自定义比较项

可以通过修改 `key=` 参数，使用 `lambda` 将输入的元素映射成一个值，这个值就代表了这个元素的大小。

- e.g. 
  - `key = lambda x, y : x + y`
  - `key = lambda t : 100*t.x. + t.y`



2. #### 自定义比较方法

可以通过修改 `key=` 参数，并借助内置的 `cmp_to_key` ，重写对两个元素的比较方法。

1. 自定义函数

2. 用lambda

   ```python
   from functools import cmp_to_key
   
   def cmp(t1, t2):
       """
       比较函数，需要满足：
       t1> t2  return  +
       t1< t2  return  -
       t1 = t2 return 0
       """
       if t1[0] == t2[0]:
           return t1[1] - t2[1]
   	return t1[0] - t2[0]
   
   l2 = sorted(l, key = cmp_to_key(cmp))
   
   ------------------------------------------
   l2 = sorted(l, key=cmp_to_key( lambda a,b : a[0]-b[0] if a[0] != b[0] else a[y] - b[y]))
   ```

   