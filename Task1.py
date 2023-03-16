def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i] and i < len(B):
            return a
    return -1

ex3 = solution([3,5,7],[4,6,7,8])
print(ex3)

a = [1,3,2,1]
b = [4,2,5,3,2]

c = [2,1]
d = [3,3]



ex1 = solution(a,b)
print(ex1)

ex2 = solution(c,d)
print(ex2)

