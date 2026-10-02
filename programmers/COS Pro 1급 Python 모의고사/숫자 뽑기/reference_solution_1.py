def solution(arr, K):
    arr.sort()

    answer = float('inf')

    for i in range(len(arr) - K + 1):
        difference = arr[i + K - 1] - arr[i]
        answer = min(answer, difference)

    return answer


# 테스트
arr = [9, 11, 9, 6, 4, 19]
K = 4

ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")