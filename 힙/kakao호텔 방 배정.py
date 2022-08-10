import heapq as pq

def solution(k, room_number):
    dic={}
    occ={}
    for i in room_number:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    rooms=list(dic.keys())
    rooms.sort(reverse=True)
    pre=-1
    while rooms:
        start = rooms.pop()
        move=dic[start]
        end=start+move
        if start>pre:
            for i in range(start,end):
                occ[i]=True
        else:
            start=pre+1
            end=start+move
            for i in range(start,end):
                occ[i]=True
        pre=end-1
    answer=[]
    people=[]
    q=[]
    for i in range(len(room_number)):
        people.append((i, room_number[i]))  # 우선순위, 방번호
    people.sort(key=lambda x: (-x[1], -x[0]))
    rooms=list(occ.keys())
    rooms.reverse()
    while rooms:
        while True:
            if people:
                if people[len(people)-1][1]==rooms[len(rooms)-1]:
                    pq.heappush(q,people.pop())
                else:
                    break
            else:
                break
        answer.append((pq.heappop(q)[0],rooms[len(rooms)-1]))
        rooms.pop()
    answer.sort(key=lambda x: x[0])
    sol = []
    for i in answer:
        sol.append(i[1])

    return sol
    rooms.sort(reverse=True)
    pre=-1
    while rooms:
        start = rooms.pop()
        move=dic[start]
        end=start+move
        if start>pre:
            for i in range(start,end):
                occ[i]=True
        else:
            start=pre+1
            end=start+move
            for i in range(start,end):
                occ[i]=True
        pre=end-1
    answer=[]
    people=[]
    q=[]
    for i in range(len(room_number)):
        people.append((i, room_number[i]))  # 우선순위, 방번호
    people.sort(key=lambda x: (-x[1], -x[0]))
    rooms=list(occ.keys())
    rooms.reverse()
    while rooms:
        while True:
            if people:
                if people[len(people)-1][1]==rooms[len(rooms)-1]:
                    pq.heappush(q,people.pop())
                else:
                    break
            else:
                break
        answer.append((pq.heappop(q)[0],rooms[len(rooms)-1]))
        rooms.pop()
    answer.sort(key=lambda x: x[0])
    sol = []
    for i in answer:
        sol.append(i[1])

    return sol


    return answer
# 백준 보석문제와 유사함