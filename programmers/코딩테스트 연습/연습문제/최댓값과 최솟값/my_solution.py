def solution(s):
    a=s.split()
    min=100000000
    max=-100000000
    for stri in a:
        inte=int(stri)
        if inte<min:
            min=inte
        if inte>max:
            max=inte
    answer=str(min)+' '+str(max)
    return answer