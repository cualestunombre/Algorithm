def solution(lines):
    count=0
    candTimes=[]
    for i in lines:
        temp = i.split(" ")[1]
        endTime=int((float(temp[0:2])*3600+float(temp[3:5])*60+float(temp[6:]))*1000)
        temp = i.split(" ")[2]
        startTime = endTime-int(float(temp[:-1])*1000)+1
        candTimes.append((startTime,endTime))
    candTimes.sort(key=lambda x:(x[0],x[1]))
    for time in candTimes:
        temp=0
        start=time[1]
        end=time[1]+999
        for x,y in candTimes:
            if end>=x and start<=y:
                temp+=1
        if temp>count:
            count=temp
    return count


