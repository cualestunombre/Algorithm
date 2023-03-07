global number
import sys
limit_number = 120000 #재귀제한을 10만이상으로 둬야함
sys.setrecursionlimit(limit_number)
cost={(1,1):1,(1,2):2,(1,3):4,(1,4):2,(1,5):3,(1,6):5,(1,7):4,(1,8):5,(1,9):6,(0,0):1,(0,1):7,(0,2):6,(0,3):7,(0,4):5,(0,5):4,
      (0,6):5,(0,7):3,(0,8):2,(0,9):3,(2,2):1,(2,3):2,(2,4):3,(2,5):2,(2,6):3,(2,7):5,(2,8):4,(2,9):5,
      (3,3):1,(3,4):5,(3,5):3,(3,6):2,(3,7):6,(3,8):5,(3,9):4,(4,4):1,(4,5):2,(4,6):4,(4,7):2,(4,8):3,
      (4,9):5,(5,5):1,(5,6):2,(5,7):3,(5,8):2,(5,9):3,(6,6):1,(6,7):5,(6,8):3,(6,9):2,(7,7):1,(7,8):2,(7,9):4,
      (8,8):1,(8,9):2,(9,9):1
      }  #자판간 거리를 노가다로 구하였음

newCost = {}
for x,y in cost:
    if (y,x) not in cost:
        newCost[(str(y),str(x))]=cost[(x,y)]
        newCost[(str(x),str(y))]=cost[(x,y)]
    else:
        newCost[(str(x),str(y))]=cost[(x,y)] #하고 보니 스트링으로 바꿀 필요가 있어서 키를 스트링으로 바꿈 + 위에는 너무많아서 a,b형태만 기록했는데 b,a형태도 기록함
cost.update(newCost) #newCost에 있는걸 cost에 반영함
cache={}

def dp(left,right,order):
    if (left,right,order) in cache:
        return cache[(left,right,order)]
    if (right,left,order) in cache:
        return cache[(right,left,order)]
    if order>=len(number):
        return 0  #캐쉬에 있으면 cache에 담긴 것을 반환 함 이때, 좌우가 바뀌어도 상관이 없는게 핵심임 + 더이상 남은 숫자가 없으면 0을 반환함
    target=number[order]
    if target==left:
        cache[(left,right,order)] = dp(left,right,order+1) + 1
        return cache[(left,right,order)]
    if target==right:
        cache[(left,right,order)] = dp(left,right,order+1) + 1
        return cache[(left,right,order)] #만약 target과 왼쪽, 오른쪽 자판의 숫자가 같으면 둘 간의 대소비교가 필요하지 않음
    leftValue = dp(target,right,order+1) + cost[(left,target)]
    rightValue = dp(left,target,order+1) + cost[(right,target)] #왼쪽과 오른쪽의 대소 비교를 통해 작은 것을 캐쉬에 담고 리턴함
    cache[(left,right,order)] = min(leftValue,rightValue)
    return cache[(left,right,order)]

def solution(numbers):
    global number
    number = numbers
    answer = dp("4","6",0)
    return answer

#길이가 10만이여도 잘 작동하는 이유 -> 최악의 상황에서도 order(재귀 깊이)당 생성될 수 있는 경우의 수는 100개이하임(10*10) 또한 좌우가 논리적으로 같아서 실제는 그 이하의 함수가 호출 됨
#10만 * 100 -> 1000만에서 어차피 cache되어 있는 것은 더이상 함수 호출을 하지 않고 좌우가 논리적으로 같아 실제 함수 호출은 1000만에 훨씬 못미침