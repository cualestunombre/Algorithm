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




    def queryMax(self, left, right):
        return self.queryMaxUtil(0, 0, len(self.nums) - 1, left, right)

    def queryMaxUtil(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.maxTree[node]
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        left_sum = self.queryMaxUtil(left_node, start, mid, left, right)
        right_sum = self.queryMaxUtil(right_node, mid + 1, end, left, right)
        return max(left_sum,right_sum)
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


n,m=map(int,input().split())
l=[int(input()) for i in range(n)]
seg = SegmentTree(l)
answers=[]
querys = [map(int,input().split()) for i in range(m)]
for x,y in querys:
    answers.append((seg.queryMin(x-1,y-1),seg.queryMax(x-1,y-1)))
for x,y in answers:
    print(str(x)+" "+str(y))


