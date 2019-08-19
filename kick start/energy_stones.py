# 2019.8.19
# Kick Start 2019 - Round B
# Practice Mode
# TIME LIMIT EXCEEDED


def max_energy(stones):        
    stones.sort(key=lambda x : -calc_efficiency(x))
    cache = {}
    result = _energy(stones, cache=cache)
    del cache
    
    return result


def calc_efficiency(stone):
    return energy_leakage(stone) / seconds(stone)


def seconds(stone):
    return stone[0]


def init_energy(stone):
    return stone[1]


def energy_leakage(stone):
    return stone[2]


def _energy(stones, time=0, index=0, cache=None):
    # Terminal Conditions
    # 1. Out of Bound
    if index >= len(stones):
        return 0
    stone = stones[index]
    stone_energy = init_energy(stone) - time*energy_leakage(stone)
    # 2. Out of Energy
    if stone_energy < 0:
        return 0

    # CACHE
    if cache is None:
        cache = {}

    if cache.get((time, index)):
        return cache[(time, index)]

    eat = _energy(stones, time+seconds(stone), index+1) \
          + stone_energy
    do_not_eat = _energy(stones, time, index+1)

    optimal = max(eat, do_not_eat)
    cache[(time, index)] = optimal
    
    return optimal


if __name__ == '__main__':
    case = int(input())
    results = []

    for i in range(case):
        n_stones = int(input())
        stones = []

        for s in range(n_stones):
            stone = list(map(int, input().strip().split()))
            stones.append(stone)
            
        results.append(max_energy(stones))

    for i in range(case):
        print("Case #{}: {}".format(i+1, results[i]))
