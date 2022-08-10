def solution(play_time, adv_time, logs):
    maxtime = int(play_time[0:2])*3600+int(play_time[3:5])*60+int(play_time[6:])
    adtime = int(adv_time[0:2])*3600+int(adv_time[3:5])*60+int(adv_time[6:])
    arr=[0 for i in range(maxtime+1)]
    for i in logs:
        start=int(i[0:2])*3600+int(i[3:5])*60+int(i[6:8])
        end = int(i[9:11])*3600+int(i[12:14])*60+int(i[15:])
        arr[start]+=1
        arr[end]-=1

    for i in range(len(arr)):
        if i!=0:
            arr[i]=arr[i-1]+arr[i]

    for i in range(len(arr)):
        if i!=0:
            arr[i]=arr[i-1]+arr[i]
    start=0
    max_value=0
    time=0
    while True:
        if start+adtime-1>maxtime:
            break
        if start==0:
            if arr[start+adtime-1]>max_value:
                time=start
                max_value=arr[start+adtime-1]
        else:
            if arr[start+adtime-1]-arr[start-1]>max_value:
                time = start
                max_value = arr[start+adtime-1]-arr[start-1]
        start+=1


    h=time//3600
    m=(time-h*3600)//60
    s=(time-h*3600-m*60)
    if h==0:
        rh='00'
    elif h>0 and h<10:
        rh='0'+str(h)
    else:
        rh=str(h)
    if m == 0:
        rm = '00'
    elif m > 0 and m < 10:
        rm = '0' + str(m)
    else:
        rm = str(m)
    if s == 0:
        rs = '00'
    elif s > 0 and s < 10:
        rs = '0' + str(s)
    else:
        rs = str(s)

    return rh+':'+rm+':'+rs
