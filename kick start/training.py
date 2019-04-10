# 2019.4.11
# Kick Start 2019 - Round A
# Practice Mode

def min_train(array:list, num_selected):
    array.sort()
    training_costs = []
    subtotal = None

    for i in range(-1, len(array) - num_selected):
        # Like a sliding window,
        # get subtotals of sorted array
        if subtotal == None:
            subtotal = sum(array[:num_selected])
        else:
            subtotal += array[num_selected+i] - array[i]

        cost = array[num_selected+i] * num_selected - subtotal
        training_costs.append(cost)

    return min(training_costs)


if __name__ == '__main__':
    case = int(input())
    results = []

    for i in range(case):
        total_student, selection = map(int, input().strip().split())
        results.append(min_train(list(map(int, input().strip().split())),
                                 selection))

    for i in range(case):
        print("Case #{}: {}".format(i+1, results[i]))
