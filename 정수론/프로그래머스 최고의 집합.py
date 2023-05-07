def solution(n, s):
    if n > s:
        return [-1]
    l = []
    quotient, remainder = divmod(s, n)
    for i in range(n):
        if i < n - remainder:
            l.append(quotient)
        else:
            l.append(quotient + 1)
    return l