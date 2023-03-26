import random
import itertools as it

#
# def maxElement(n, maxSum, k):
#     # Write your code here
#     t1 = [i for i in it.combinations_with_replacement(range(1, n+1), r=n)]
#     t2 = [i for i in t1 if sum(i) <= maxSum]
#     t2 = [list(i) for i in t2]
#     t3 = []
#     for i in t2:
#         for j in range(len(i) - 1):
#             if i[j+1] - i[j] > k:
#                 break
#
#     return max(i)
# print(ord('p'))
# print(hash('cAr1'))
#
#
#
# print(maxElement(3, 7, 1))
# print(maxElement(4, 6, 2))
import math
t = 'cAr1'
m = 0
for i in range(len(t)-1):
    if (len(t)-i) != 1:
        print(len(t)-i)
#        print(ord(t[i])*math.pow(131, len(t)-i))
        m += ord(t[i])*math.pow(131, len(t)-i)
    else:
        print("------------")
        print(len(t)-i)

#        print(math.pow(10, 9) + 7)
        m += math.pow(10, 9) + 7
print(m)
#223691457
#29155492179