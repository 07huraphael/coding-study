def solution(arr, K):
    arr.sort()

    return min(
        arr[i + K - 1] - arr[i]
        for i in range(len(arr) - K + 1)
    )