# Reinforcement
#
# R-1.1 Write a short Python function, is multiple(n, m), 
# that takes two integer values and returns True if n is 
# a multiple of m, that is, n = mi for some integer i, 
# and False otherwise.

def is_multiple(n, m):
    i = 0
    while i < n:
        if (i * m <= n) and (i * m == n):
            return True
        i += 1
    return False

if __name__ == '__main__':
    print(is_multiple(1_000_000,5))
