# 특정좌표에 사람이 존재하는지 판별하는 함수
def existsPlayer(players, cx, cy):
    for i in players:
        x, y, d, s, w = players[i]
        if cx == x and cy == y:
            return i
    return "not"


n, m, k = map(int, input().split())
score = [0 for i in range(m)]
players = {}

l = [list(map(int, input().split())) for i in range(n)]
board = [[[] for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if l[i][j] != 0:
            board[i][j].append(l[i][j])

# x,y,d,s 방향, 능력치
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(m):
    x, y, d, s = map(int, input().split())
    players[i] = (x - 1, y - 1, d, s, 0)

round = 0
while True:
    round += 1

    seq = list(players.keys())
    seq.sort()
    for i in seq:

        x, y, d, s, w = players[i]
        dx, dy = dir[d]

        if not (dx + x >= 0 and dx + x < n and dy + y >= 0 and dy + y < n):
            dx = -dx
            dy = -dy
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            elif d == 3:
                d = 1

        # 플레이어가 없다면?
        playerNo = existsPlayer(players, dx + x, dy + y)

        if playerNo == "not":

            if len(board[dx + x][dy + y]) == 0:  # 총이 없음
                pass
            else:  # 격자에 총이 있음
                # 내가 총이없다면
                if w == 0:
                    board[dx + x][dy + y].sort()
                    w = board[dx + x][dy + y].pop()
                # 내가 총이 있다면
                else:
                    board[dx + x][dy + y].sort()
                    # 총의 공격력 최대값이 내총보다 커야함
                    if board[dx + x][dy + y][-1] > w:
                        temp = w
                        w = board[dx + x][dy + y].pop()
                        board[dx + x][dy + y].append(temp)
            players[i] = (dx + x, dy + y, d, s, w)
        # 사람이 겹침 즉, 승자패자가 갈림
        else:

            winner = 0
            loser = 0
            players[i] = (dx + x, dy + y, d, s, w)
            ex, ey, ed, es, ew = players[playerNo]
            lx, ly, ld, ls, lw = (0, 0, 0, 0, 0)
            wx, wy, wd, ws, ww = (0, 0, 0, 0, 0)
            myPower = w + s
            enomyPower = es + ew
            if myPower > enomyPower:
                winner = i
                loser = playerNo
                score[winner] += myPower - enomyPower

                wx, wy, wd, ws, ww = (x + dx, y + dy, d, s, w)
                lx, ly, ld, ls, lw = (x + dx, y + dy, ed, es, ew)
            elif myPower == enomyPower:
                if es > s:
                    winner = playerNo
                    loser = i
                    wx, wy, wd, ws, ww = (x + dx, y + dy, ed, es, ew)
                    lx, ly, ld, ls, lw = (x + dx, y + dy, d, s, w)
                else:
                    winner = i
                    loser = playerNo
                    lx, ly, ld, ls, lw = (x + dx, y + dy, ed, es, ew)
                    wx, wy, wd, ws, ww = (x + dx, y + dy, d, s, w)
            else:
                winner = playerNo
                loser = i
                score[winner] += enomyPower - myPower

                lx, ly, ld, ls, lw = (x + dx, y + dy, d, s, w)
                wx, wy, wd, ws, ww = (x + dx, y + dy, ed, es, ew)

            # 진플레이어는 총을 내려놓는다
            if lw != 0:
                board[lx][ly].append(lw)
                lw = 0
            while True:

                tx, ty = dir[ld]
                if not (lx + tx >= 0 and lx + tx < n and ly + ty >= 0 and ly + ty < n) or existsPlayer(players, lx + tx,
                                                                                                       ly + ty) != "not":
                    # 오른쪽 90도 회전
                    ld = (ld + 1) % 4

                else:
                    lx += tx
                    ly += ty
                    break

            if len(board[lx][ly]) == 0:
                pass
            else:
                board[lx][ly].sort()
                lw = board[lx][ly].pop()
            # 이긴플레이는 총을 줍는다
            if ww == 0:
                if len(board[wx][wy]) != 0:
                    board[wx][wy].sort()
                    ww = board[wx][wy].pop()
            else:
                if len(board[wx][wy]) != 0:
                    board[wx][wy].sort()
                    if board[wx][wy][-1] > ww:
                        temp = ww
                        ww = board[wx][wy].pop()
                        board[wx][wy].append(temp)
            players[winner] = (wx, wy, wd, ws, ww)
            players[loser] = (lx, ly, ld, ls, lw)

    if round == k:
        break
for i in score:
    print(i, end=" ")