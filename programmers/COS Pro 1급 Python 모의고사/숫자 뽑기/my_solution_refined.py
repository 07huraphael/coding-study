def solution(arr, K):
    # 오름차순 정렬 - 버블 정렬
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # K개의 숫자를 선택했을 때
    # 최댓값과 최솟값의 차이 중 최솟값 찾기
    answer = 10000

    for i in range(len(arr) - K + 1):
        diff = arr[i + K - 1] - arr[i]

        if diff < answer:
            answer = diff

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4

ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")