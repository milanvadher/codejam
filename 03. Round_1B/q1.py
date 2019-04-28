def main():
    for i in range(1,int(input()) + 1):
        N,K = map(int,input().split())
        Ci = list(map(int,input().split()))
        Di = list(map(int,input().split()))
        ans = 0
        for j in range(N):
            for k in range(j,N):
                c_max = max(Ci[j:k+1])
                d_max = max(Di[j:k+1])
                if abs(c_max - d_max) <= K:
                    ans = ans + 1
        print("Case #{0}: {1}".format(i,ans))

if __name__ == "__main__":
    main()