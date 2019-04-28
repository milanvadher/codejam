# Limits
# 1 ≤ T ≤ 100.
# Time limit: 15 seconds per test set.
# Memory limit: 1GB.
# P contains exactly N - 1 E characters and exactly N - 1 S characters.

# Test set 1 (Visible)
# 2 ≤ N ≤ 10.

# Test set 2 (Visible)
# 2 ≤ N ≤ 1000.

# Test set 3 (Hidden)
# For at most 10 cases, 2 ≤ N ≤ 50000.
# For all other cases, 2 ≤ N ≤ 10000.

# Sample

# Input         Output 
 
# 2
# 2
# SE            Case #1: ES
# 5
# EESSSESE      Case #2: SEEESSES

# In Sample Case #1, the maze is so small that there is only one valid solution left for us.

# Sample Case #2 corresponds to the picture above. Notice that it is acceptable for the paths to cross.

def main():
    # `t`: Number of test case
    t = int(input())
    for i in range(1,t+1):
        # Not needed
        input()
        p = input()
        # Swap `E` with `S`
        res = p.replace('E','0').replace('S','E').replace('0','S')
        print("Case #{0}: {1} {2}".format(i, p, res))

if __name__ == "__main__":
    main()