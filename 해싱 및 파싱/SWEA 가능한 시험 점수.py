answer=[]
for i in range(int(input())):
    m, l = int(input()), sorted(map(int, input().split()))
    dic = {0: True}
    [dic.update({k+j: True for k in dic if k+j not in dic}) for j in l]
    answer.append(f"#{i+1} {len(dic)}")
for i in answer:
    print(i)