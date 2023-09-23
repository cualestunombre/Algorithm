#include <iostream>
#include <vector>
#include <climits>  // for INT_MAX
#include <algorithm>  // for min

const int INF = INT_MAX;
const std::vector<std::pair<int, int>> DIR = {{0, 0}, {0, -1}, {0, 1}, {1, 
0}, {-1, 0}};

void rotate(std::vector<std::vector<int>>& clockHands, int x, int y, int 
i) {
    int n = clockHands.size();
    for (const auto& d : DIR) {
        int dx = d.first;
        int dy = d.second;
        if (0 <= x + dx && x + dx < n && 0 <= y + dy && y + dy < n) {
            clockHands[x + dx][y + dy] = (clockHands[x + dx][y + dy] + i) 
% 4;
        }
    }
}

void counterRotate(std::vector<std::vector<int>>& clockHands, int x, int 
y, int i) {
    int n = clockHands.size();
    for (const auto& d : DIR) {
        int dx = d.first;
        int dy = d.second;
        if (0 <= x + dx && x + dx < n && 0 <= y + dy && y + dy < n) {
            clockHands[x + dx][y + dy] = (clockHands[x + dx][y + dy] - i + 
4) % 4;
        }
    }
}

bool finalCheck(const std::vector<std::vector<int>>& clockHands) {
    for (const auto& row : clockHands) {
        for (int cell : row) {
            if (cell != 0) {
                return false;
            }
        }
    }
    return true;
}

int search(std::vector<std::vector<int>>& clockHands, int x, int y, int 
move, int minimum) {
    int n = clockHands.size();
    if (x == n) {
        if (finalCheck(clockHands)) {
            return move;
        }
        return INF;
    }

    if (move >= minimum) {
        return INF;
    }

    int result = INF;

    for (int i = 0; i < 4; ++i) {
        rotate(clockHands, x, y, i);
        if (x - 1 >= 0 && clockHands[x - 1][y] != 0) {
            counterRotate(clockHands, x, y, i);
            continue;
        }
        int nx = (y + 1 == n) ? x + 1 : x;
        int ny = (y + 1) % n;
        result = std::min(result, search(clockHands, nx, ny, move + i, 
minimum));
        counterRotate(clockHands, x, y, i);
    }

    return result;
}

int solution(std::vector<std::vector<int>> clockHands) {
    int minimum = INF;
    int result = search(clockHands, 0, 0, 0, minimum);
    return (result != INF) ? result : -1;
}

