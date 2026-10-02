def solution(K, words):
    answer = 1
    length = len(words[0])

    for word in words[1:]:
        if length + len(word) + 1 <= K:
            length += len(word) + 1
        else:
            answer += 1
            length = len(word)

    return answer