# 2019.4.22
# Kick Start 2019 - Round C
# Practice Mode

def generate(N, K, x1, y1, C, D, E1, E2, F):
    arr = []

    for i in range(N):
        if i == 0:
            x = x1
            y = y1
            _x = x
            _y = y
        else:
            x = (C*_x + D*_y + E1) % F
            y = (D*_x + C*_y + E2) % F
            _x = x
            _y = y
            
        arr.append((x + y) % F)

    return arr


def brute(arr, N, K):
    cache = {}
    result = 0
    for k in range(1, K+1):
        for l in range(1, N+1):
            for r in range(l, N+1):
                for j in range(l, r+1):
                    result += arr[j-1] * pow(j-l+1, k)
                    result %= int(1e+9 + 7)

                    if cache.get(j-1):
                        cache[j-1] += pow(j-l+1, k)
                    else:
                        cache[j-1] = pow(j-l+1, k)
    print(cache)
    return result


def total_power(arr, N, K):
    modulo = int(1e+9 + 7)
    total = 0

    # --1 2 3 4 5--
    # 1, 2, 3, 4, 5
    # 12, 23, 34, 45
    # 123, 234, 345
    # 1234, 2345
    # 12345
    # -> 1 : 5
    # -> 2 : 4-4     
    # -> 3 : 3-3-3 
    # -> 4 : 2-2-2-2
    # -> 5 : 1-1-1-1-1
    mul = 0
    for j in range(N):
        mul += sum_of_powers(j+1, K)
        total = (total + (arr[j] * (N - j) * mul)) % modulo

    return total % modulo


def sum_of_powers(n, count):
    # sum = n + n**2 + ... + n**count
    if n == 1:
        return count
    else:
        return int((n**(count+1) - n) / (n - 1))
    

if __name__ == '__main__':
    case = int(input())
    results = []

    for i in range(case):
        config = list(map(int, input().strip().split()))

        arr = generate(*config)
        results.append(total_power(arr, *config[:2]))

    for i in range(case):
        print("Case #{}: {}".format(i+1, results[i]))
