class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.maxTree = [0] * (4 * len(nums))
        self.minTree = [0] * (4 * len(nums))
        self.build(0, 0, len(nums) - 1)

    def build(self, node, start, end):
        if start == end:
            self.maxTree[node] = self.nums[start]
            self.minTree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            self.build(left_node, start, mid)
            self.build(right_node, mid + 1, end)
            self.maxTree[node] = max(self.maxTree[left_node] , self.maxTree[right_node])
            self.minTree[node] = min(self.minTree[left_node] ,self.minTree[right_node])

    def update(self, index, value):
        self.update_util(0, 0, len(self.nums) - 1, index, value)

    def update_util(self, node, start, end, index, value):
        if start == end:
            self.minTree[node] = value
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if index <= mid:
                self.update_util(left_node, start, mid, index, value)
            else:
                self.update_util(right_node, mid + 1, end, index, value)
            self.minTree[node] = min(self.minTree[left_node] ,self.minTree[right_node])




    def queryMin(self, left, right):
        return self.queryMinUtil(0, 0, len(self.nums) - 1, left, right)

    def queryMinUtil(self, node, start, end, left, right):
        if left > end or right < start:
            return 1000000000000
        if left <= start and end <= right:
            return self.minTree[node]
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        left_sum = self.queryMinUtil(left_node, start, mid, left, right)
        right_sum = self.queryMinUtil(right_node, mid + 1, end, left, right)
        return min(left_sum,right_sum)


n=int(input())
l=list(map(int,input().split()))
m=int(input())
seg = SegmentTree(l)
answers=[]
querys = [tuple(map(int,input().split())) for i in range(m)]
for x,y,z in querys:
    if x==1:
        seg.update(y-1,z)
    else:
        answers.append(seg.queryMin(y-1,z-1))
for x in answers:
    print(x)
