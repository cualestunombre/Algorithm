class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        self.build(0, 0, len(nums) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            self.build(left_node, start, mid)
            self.build(right_node, mid + 1, end)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, index, value):
        self.update_util(0, 0, len(self.nums) - 1, index, value)

    def update_util(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if index <= mid:
                self.update_util(left_node, start, mid, index, value)
            else:
                self.update_util(right_node, mid + 1, end, index, value)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def query(self, left, right):
        return self.query_util(0, 0, len(self.nums) - 1, left, right)

    def query_util(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        left_sum = self.query_util(left_node, start, mid, left, right)
        right_sum = self.query_util(right_node, mid + 1, end, left, right)
        return left_sum + right_sum



n,m,k = map(int,input().split())
q=[int(input()) for i in range(n)]
l=[tuple(map(int,input().split())) for i in range(m+k)]
segmentTree = SegmentTree(q)
answers=[]
for x,y,z in l:
    if x==2:
        answers.append(segmentTree.query(y-1,z-1))
    else:
        segmentTree.update(y-1,z)
for i in answers:
    print(i)

