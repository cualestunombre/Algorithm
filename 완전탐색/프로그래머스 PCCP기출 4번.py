global_minimum = 10**20
DIR = [(0,-1),(0,1),(1,0),(-1,0)]

def solution(maze):
    global n,m,target_red, target_blue, global_minimum

    n,m = len(maze), len(maze[0])

    # 초기 전처리
    for row in range(n):
        for col in range(m):
            if maze[row][col] == 1:
                red = (row,col)
            elif maze[row][col] == 2:
                blue = (row,col)
            elif maze[row][col] == 3:
                target_red = (row,col)
            elif maze[row][col] == 4:
                target_blue = (row,col)


    # red, blue 방문 별도 기록
    red_visited, blue_visited = {red:True}, {blue:True}

    brute_force(maze,red_visited,blue_visited,red,blue,0)

    return global_minimum if global_minimum != 10**20 else 0

def brute_force(maze,red_visited,blue_visited,red,blue,turn):
    global n, m, target_red, target_blue, global_minimum

    # global_minumum을 업데이트 하는 조건!!
    if red == target_red and blue == target_blue:
        global_minimum = min(global_minimum,turn)
        return


    # cal_cand에서 거르는 조건
    # 조건 1. 칸을 벗어나지 않는다
    # 조건 2. visited 딕셔너리에 가려는 칸이 없다
    # 조건 3. 벽이 아니다
    # 조건 5. 현재 목표에 도달 했으면 움직이지 않는다
    red_candidates, blue_candidates = cal_cand(red,maze,red_visited,target_red), cal_cand(blue,maze,blue_visited,target_blue)


    for rc in red_candidates:
        for bc in blue_candidates:
            # 도달한 곳이 같으면 안된다, 자리 바꿔치기를 하면 안된다
            if rc != bc and (rc,bc) != (blue,red):

                # 도착하면 visited를 체크하지 않는다
                if rc != target_red:
                    red_visited[rc] = True
                if bc != target_blue:
                    blue_visited[bc] = True

                brute_force(maze,red_visited,blue_visited,rc,bc,turn+1)

                # visited 체크 해제
                if rc in red_visited:
                    del red_visited[rc]
                if bc in blue_visited:
                    del blue_visited[bc]


# cur:본인위치, maze:미로, visited: 본인 visited, target:최종 목적지
def cal_cand(cur,maze,visited,target):
    global n,m
    answer = []

    # 이미 도착했으면 도착한 곳을 리턴
    if cur == target:
        return [target]

    x,y = cur
    # 조건 1. 칸을 벗어나지 않는다
    # 조건 2. visited 딕셔너리에 가려는 칸이 없다
    # 조건 3. 벽이 아니다
    for dx,dy in DIR:
        if x+dx >=0 and x+dx<n and y+dy >= 0 and y+dy<m and (x+dx,y+dy) not in visited and \
            maze[x+dx][y+dy] != 5:
            answer.append((x+dx,y+dy))

    return answer



