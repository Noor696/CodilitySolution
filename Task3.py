def solution(A):
    l = len(A)
    A.sort
    ans = 0

    for i in range(l):
        s = [A[i]]

        for j in range(i+1,l):
            if len(s)>=2 and A[j]-s[-1] == s[i]-s[0]:
                s.append(A[j])
                
        ans = max(ans, len(s))

    return ans

ex1 = solution([12,12,12,15,10])
print (ex1)

ex2 = solution([4,7,1,5,3])
print (ex2)
