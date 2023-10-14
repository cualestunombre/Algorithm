# 문자 하나를 파싱하는 함수
def parseChar(l):
    return l.pop(0)

# 괄호가 들어간 것을 파싱하는 함수
def parseBracket(l):
    left, right = 1, 0
    cur = 1

    while left > right:
        if l[cur] == "(":
            left += 1
        if l[cur] == ")":
            right += 1
        cur += 1
    temp = [l.pop(0) for i in range(cur)]
    temp.pop(0), temp.pop()
    return ''.join(parse(temp))

# 연산자를 파싱하는 함수
def findOperand(l):
    ret = []
    if l[0].isupper():
        ret.append(parseChar(l))
    elif l[0] == "(":
        ans = parseBracket(l)
        ret.append(ans)

    return ret

# 연산자를 재귀적으로 파싱하는 함수
def findOperandRecursive(l):
    ret = []
    if l[0].isupper():
        ret.append(parseChar(l))
    elif l[0] == "(":
        ans = parseBracket(l)
        ret.append(ans)

    if len(l) == 0:
        return ret


    operator = l[0]


    if operator == "+" or operator == "-":
        return ret

    else:
        l.pop(0)
        ans = findOperandRecursive(l)

        ans.insert(1,operator)
        return ret + ans

# 파싱을 수행하는 함수
def parse(l):
    stack = []
    while l:
        # 첫번째 연산자를 찾는다
        ret = findOperand(l)

        for i in ret:
            stack.append(i)

        if not l:
            break

        operator = l.pop(0)

        if operator in ["+","-"]:
            ret = findOperandRecursive(l)
            for i in ret:
                stack.append(i)
        else:
            ret = findOperand(l)
            for i in ret:
                stack.append(i)
        stack.append(operator)
    return stack




l = list(input())
answer = parse(l)
for i in answer:
    print(i,end="")


