with open('4922.txt') as f:
    n, k = map(int,f.readline().split())
    a = [int(x) for x in f]
    count = [0] * k
    count[0] = 1
    sm = ans = 0
    for i in a:
        sm = (sm + i) % k # 1 инд посл  114 и 229 и
        ans += count[sm]
        #print(count)
        #print(ans, sm, i)
        count[sm] += 1
    print(ans)