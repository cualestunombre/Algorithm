global maxx
maxx=-10000000000000000
def bruteForce(l,str,current):
    global maxx
    if current>len(str):
        q=[]
        cur=0
        while cur<len(str):
            if cur==len(str)-1:
                q.append(int(str[cur]))
                cur += 1
                continue
            if cur not in l:
                q.append(int(str[cur]))
                q.append(str[cur+1])
                cur+=2
            else:
                a=int(str[cur])
                b=int(str[cur+2])
                operator=str[cur+1]
                ans=0
                if operator=='+':
                    ans=a+b
                elif operator=='-':
                    ans=a-b
                elif operator=="*":
                    ans=a*b
                q.append(ans)
                if cur+3 < len(str):
                    q.append(str[cur+3])
                cur+=4
        answer=q.pop(0)
        while q:
            operator=q.pop(0)
            number=q.pop(0)
            if operator=='+':
                answer+=number
            elif operator=="-":
                answer-=number
            else:
                answer*=number
        if answer>maxx:
            maxx=answer
        return
    if l and l[-1]+2==current:
        bruteForce(l,str,current+2)
    else:
        l.append(current)
        bruteForce(l,str,current+2)
        l.pop()
        bruteForce(l,str,current+2)
    return


n=int(input())
str=input()
l=[0]
bruteForce(l,str,2)
l.pop()
bruteForce(l,str,2)
print(maxx)
