def solution(s):
    count = 0

    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1

        # 닫는 괄호가 먼저 나온 경우
        if count < 0:
            return False

    # 모든 괄호의 짝이 맞아야 함
    return count == 0