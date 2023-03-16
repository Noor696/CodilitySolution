def solution(A):
    c = 0
    a = set(A)
    while (len(a)!= 1):
        maxi = max(A)
        ind = A.index(maxi)
        for i in range (ind):
            A[i]+=1
        for i in range(ind+1,len(A)):
            A[i]+=1
        c +=1
    return c

def solution2(A):
    minV= min(A)
    maxV= max(A)
    minS = float('inf')

    for i in range(minV,maxV+1):
        steps = 0
        for val in A:
            steps +=abs(val-i)
        if steps < minS:
            minS= steps
    return minS



ex1 = solution2([3,2,1,1,2,3,1])
print(ex1)

ex2 = solution2([4,1,4,1])
print(ex2)

ex3 = solution2([3,3,3])
print(ex3)

ex4 = solution2([5,5,5])
print(ex4)

ex5 = solution2([1,7,9])
print("ex5 ",ex5)

ex6 = solution2([2,4,5,7])
print("ex6 ",ex6)

ex7 = solution2([10,10,10])
print("ex7 ",ex7)

ex8 = solution2([4,5,6,7,8])
print("ex8 ",ex8)

ex9 = solution2([20,30,35,40])
print("ex9 ",ex9)
