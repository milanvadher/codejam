# Limits
# 1 ≤ T ≤ 100.
# Time limit: 10 seconds per test set.
# Memory limit: 1GB.
# At least one of the digits of N is a 4.

# Test set 1 (Visible)
# 1 < N < 105.

# Test set 2 (Visible)
# 1 < N < 109.

# Solving the first two test sets for this problem should get you a long way toward advancing. The third test set is worth only 1 extra point, for extra fun and bragging rights!

# Test set 3 (Hidden)
# 1 < N < 10100.

# Sample

# Input         Output
 
# 3
# 4             Case #1: 2 2
# 940           Case #2: 852 88
# 4444          Case #3: 667 3777

# In Sample Case #1, notice that A and B can be the same. The only other possible answers are 1 3 and 3 1.

def main():
    # `t`: Number of test case
    t = int(input())
    for i in range(1,t+1):
        # `n`: Any number include `4`
        n = input()
        # replace `4` with `3`
        a = n.replace('4','3')
        print('Case #{0}: {1} {2}'.format(i, a, int(n)-int(a)))

if __name__ == "__main__":
    main()