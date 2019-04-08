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