# 2019.4.10
# Kick Start 2018 - Round B
# Practice Mode

def no_nine(start: str, end: str):
    return count_legal(end) - count_legal(start) + 1


def brute_count_legal(num):
    count = 0
    for i in range(1, num+1):
        count += is_legal(i)
    return count


def is_legal(num):
    if num % 9 != 0 and '9' not in str(num):
        return 1
    return 0
    

def count_legal(num_string: str):
    last = len(num_string) - 1
    count = 0
    
    for i, num in enumerate(num_string):
        num = int(num)
        
        if i == last:
            if i == 0:
                count = num
            elif int(num_string) % 9 <= num:
                '''
                Ex1) 28 % 9 = 1 < 8
                from 20-28, there are 8 legal numbers
                Ex2) 278 % 9 = 8 == 8
                from 270-278, there are 8 legal numbers
                '''
                count += num
            else:
                '''
                Ex3) 26 % 9 = 8 > 6
                from 20-26, there are 7 legal numbers
                '''
                count += num + 1
        else:
            '''
            Ex) 2000 : interpret with base 9
            2000 = 2 * (9 ** 3)
            1/9 of them are divisable by 9.
            2 * (9 ** 3) * (8 / 9) = 2 * 8 * (9 ** 2)
            '''
            count += num * 8 * (9 ** (last - i - 1))

    return count


if __name__ == '__main__':
    count = int(input().strip())
    results = []

    for i in range(count):
        start, end = input().strip().split()
        results.append(no_nine(start, end))

    for i in range(count):
        print("Case #{}: {}".format(i+1, results[i])) 

    
