# find maximal sequance of consecutive zeros.
# ex: 1001 -> Gap = 2 zeros / 1000010001 -> Gap = 4 zeros

def Solution(N):
    N = bin(N)[2:]
    b=0
    maxb=0

    for i in N:
        if int(i) == 0 :
            b+=1
        elif int(i) == 1 :
            maxb = max(b,maxb)
            b=0

    return maxb

userIn = int(input("enter binary number: "))
ex1 = Solution(userIn)
print(ex1)