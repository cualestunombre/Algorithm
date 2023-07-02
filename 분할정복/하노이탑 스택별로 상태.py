## 총 고리를 10개로 제한하는 대신에 각 스탭별로 상태를 출력하시오
import sys
sys.setrecursionlimit(10000)
global count,n
n = int(input())
count = 0
answer = []
stacks=[[],[],[]]
def tempFinder(start,target):
    dic = {}
    dic[start]=True
    dic[target]=True
    for ele in [0,1,2]:
        if ele not in dic:
            return ele

def printStack(index,stack):
    print(index,"번 스택을 출력합니다")
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])


def hanoi(start,target,amount):

    global count,n
    if amount==1:
        stacks[target].append(stacks[start].pop())
        print("스택출력!!!!!")
        for index,ele in enumerate(stacks):
            printStack(index,ele)
        print("출력끝!!!!")
        return
    temp = tempFinder(start,target)

    hanoi(start,temp,amount-1)
    hanoi(start,target,1)
    hanoi(temp,target,amount-1)

for i in range(n):
    stacks[0].append(n-i)

hanoi(0,2,n)
