def main():
    # `t`: No of test case
    t = int(input())
    for i in range(1,t+1):
        input()
        # Input space seprated input numbers
        nums =  [int(x) for x in input().split()]
        nums_copy = nums[:]
        # Move any preceding duplicates to `nums_removed` for later
        while nums[0] == nums[1]:
            nums = nums[1:]
        nums_removed = nums_copy[:len(nums_copy)-len(nums)][::-1]
        a, b = nums[:2]
        p = gcd(a,b)
        q = a // p
        # Initiate factored
        factored = [q, p, b // p]
        p = b // p
        # Add following primes
        for x in nums[2:]:
            p = x // p
            factored.append(p)
        # Add preceding primes (from `nums_removed`)
        # `reverse-append-reverse` instead of `insert` due to time complexity
        factored.reverse()
        for x in nums_removed:
            q = x // q
            factored.append(q)
        factored.reverse()
        # Get sorted list of unique primes
        primes = sorted(list(set(factored)))
        if len(primes) != 26:
            while(True):
                print(1)
        # Decoding dictionary
        dic = {primes[i]: chr(i+65) for i in range(26)}
        # Decode
        result = ''.join([dic[x] for x in factored])
        print('Case #{0}: {1}'.format(i, result))
        
# Greatest Common Divisor
def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b:
        return gcd(b, a % b)
    return b

if __name__ == "__main__":
    main()