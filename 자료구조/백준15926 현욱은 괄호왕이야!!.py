import itertools

n = int(input())
bracket = input()
stack = []
check = [False] * n
for i, c in enumerate(bracket):
    if c == ")" and stack:
        check[stack.pop()] = True
        check[i] = True
    elif c == "(":
        stack.append(i)

answer = 0
for k, group in itertools.groupby(check):
    if k and group:
        answer = max(answer, len(list(group)))
print(answer)