# 2019.4.20
# Kick Start 2019 - Round A
# Practice Mode

def book(num_seats: int, booking: list):
    booking.sort(key=lambda x : num_of_seats(x))
    
    union = []
    answer = None
    
    for b in booking:
        count, union = merge(union, b)

        if answer is None:
            answer = count
        else:
            answer = min(answer, count)

        if answer == 0:
            break

    return answer
        

def sort_booking(booking: list):
    # Sort booking
    # Smallest R value first, if same Smallest L value first
    booking.sort(reverse=True)
    booking.sort(key = lambda x : x[1])
    return booking


def merge(union: list, new: list) -> (int, list):
    # If empty
    if len(union) == 0:
        return num_of_seats(new), [new]
    
    # Find Left and Right
    left, right = len(union), 0
    for i, sect in enumerate(union):
        # new and sect intersect
        if new[0] <= sect[1]+1 and sect[0]-1 <= new[1]:
            left = min(left, i)
            right = max(right, i)

    # Doest not intersect
    if left > right:
        merged = union + [new]
        sort_booking(merged)
        return num_of_seats(new), merged

    # Does intersect
    count = sum(map(num_of_seats, union[left:right+1]))
    new_sect = [min(new[0], union[left][0]), max(new[1], union[right][1])]
    merged = union[:left] + [new_sect] + union[right+1:]
    sort_booking(merged)
    return num_of_seats(new_sect) - count, merged

            
def num_of_seats(sect):
    return sect[1] - sect[0] + 1


if __name__ == '__main__':
    case = int(input())
    results = []

    for i in range(case):
        total_seats, num_of_requests = map(int, input().strip().split())
        booking = []

        for j in range(num_of_requests):
            booking.append(list(map(int, input().strip().split())))

        results.append(book(total_seats, booking))

    for i in range(case):
        print("Case #{}: {}".format(i+1, results[i]))
