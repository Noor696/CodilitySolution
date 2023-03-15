def Solution(A,k):
    N = len(A)
    B = A.copy()
    #B = [None]*N

    for i in range(0,N):
        B[(i+k)%N] = A[i]

    return B

#____________________#

# the formula solution is: 
# (L0 + k )% size A = L1


case1 = Solution([3,8,9,7,6],3)
print (case1) # [9, 7, 6, 3, 8]

case2 = Solution(["a","b","c","d"],1)
print (case2) # ['d', 'a', 'b', 'c']