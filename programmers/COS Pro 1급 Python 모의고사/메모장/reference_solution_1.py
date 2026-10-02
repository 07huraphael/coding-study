def solution(K, words):
    answer = 1       # 첫 번째 줄부터 시작
    used = 0         # 현재 줄에서 사용한 칸 수

    for word in words:
        length = len(word)

        # 현재 줄에 아무것도 없는 경우
        if used == 0:
            used = length

        # 공백 1칸 + 단어를 현재 줄에 넣을 수 있는 경우
        elif used + 1 + length <= K:
            used += 1 + length

        # 현재 줄에 들어가지 않는 경우
        else:
            answer += 1
            used = length

    return answer