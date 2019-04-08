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