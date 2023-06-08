class StaticClass:
    def __init__(self, n, m):
        self.max = 0
        self.visited = [[False] * m for _ in range(n)]
        self.n = n
        self.m = m
        self.count = 0

    def findNext(self):
        for dx in range(self.n):
            for dy in range(self.m):
                if not self.visited[dx][dy]:
                    return (dx, dy)
        return (-1, -1)

    def searchAll(self, l, cur, summation):
        self.count += 1
        x, y = cur

        # 종료 조건
        if cur == (-1, -1):
            if summation > self.max:
                self.max = summation
            return

        # 세로로 확장
        for dx in range(self.n - x):
            if not self.visited[x + dx][y]:
                number = ''
                for ddx in range(dx + 1):
                    number += l[x + ddx][y]
                    self.visited[x + ddx][y] = True

                number = int(number)
                target = self.findNext()
                self.searchAll(l, target, summation + number)
                for ddx in range(dx + 1):
                    self.visited[x + ddx][y] = False
            else:
                break

        # 가로로 확장
        for dy in range(self.m - y):
            if not self.visited[x][y + dy]:
                number = ''
                for ddy in range(dy + 1):
                    number += l[x][y + ddy]
                    self.visited[x][y + ddy] = True

                number = int(number)
                target = self.findNext()
                self.searchAll(l, target, summation + number)
                for ddy in range(dy + 1):
                    self.visited[x][y + ddy] = False
            else:
                break

if __name__ == "__main__":
    n, m = map(int, input().split())
    l = [input() for _ in range(n)]

    static_obj = StaticClass(n, m)
    static_obj.searchAll(l, (0, 0), 0)
    print(static_obj.max)