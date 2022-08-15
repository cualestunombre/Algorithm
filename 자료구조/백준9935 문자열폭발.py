l=input()
comp=input()
dic={}
def islegit(arr): # legit한지 검사
    last = arr[len(arr)-1]
    if last not in dic:
        return False
    else:
        if len(arr)-1 in dic[arr[len(arr)-1]]:
            return True
        else:
            return False
for i in range(len(comp)): #딕셔너리에 자리 저장
    if comp[i] in dic:
        dic[comp[i]]+=[i]
    else:
        dic[comp[i]]=[i]
stack=[]
for i in l:
    if not stack:
        stack.append([i])
    else:
        cur=len(stack[len(stack)-1])
        if i in dic:
            temp=dic[i]
        else:
            temp=[]
        if cur in temp and islegit(stack[len(stack)-1]): #전에 것이 legit하고 자기 자리가 맞으면 넣기
            stack[len(stack)-1].append(i)
        else:
            stack.append([i])
    if len(stack[len(stack)-1])==len(comp) and islegit(stack[len(stack)-1]): #문자열이 다찼으면, pop하기 
        stack.pop()

if not stack:
    print('FRULA')
else:
    answer=[]
    for i in stack:
        for j in i:
            answer.append(j)
    print(''.join(answer))
