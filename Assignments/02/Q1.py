def query(x):
    return -1 * (x - 7)**2 + 49  # Peak at x = 7

def find_peak(N: int) -> int:
    low = 0
    high = N
    while low < high:
        mid = (low + high) // 2
        if query(mid) < query(mid + 1):
            low = mid + 1
        else:
            high = mid
    return low
