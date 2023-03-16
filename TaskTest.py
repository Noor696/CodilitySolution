# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    a = set(A)
    smallestN = 1

    while a:
        if smallestN in A:
            smallestN +=1
        else : 
            return smallestN
        
def solution2(A):
    a = set(A)
    smallestN = 1

    while smallestN in a :
        smallestN+=1
    return smallestN 

        
ex1 = solution([1,3,4,5])
print(f"the smallest positive integer that does not occur in [1,3,4,5] : {ex1}")

ex2 = solution([1, 3, 6, 4, 1, 2])
print(f"the smallest positive integer that does not occur in [1, 3, 6, 4, 1, 2] : {ex2}")

ex3 = solution([1, 3, 6, 5, 1, 2])
print(f"the smallest positive integer that does not occur in [1, 3, 6, 4, 1, 2] : {ex3}")
