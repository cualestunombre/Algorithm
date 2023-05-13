from itertools import permutations
def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak]  # 선형으로

    for i, start in enumerate(weak):
        for friends in permutations(dist):  # 순열 이용
            count = 1
            position = start
            # 친구 조합 배치
            for friend in friends:
                position += friend
                # 끝 포인트까지 도달 못했을 때
                if position < weak_point[i+L-1]:
                    count += 1  # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    position = [w for w in weak_point[i+1:i+L]
                                if w > position][0]
                else:  # 끝 포인트까지 도달
                    cand.append(count)
                    break

    return min(cand) if cand else -1