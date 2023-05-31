n , k = map(int,input().split())
number = input()
numbers = []
for num in number:
    numbers.append(num)
stack = [numbers[0]]
for index in range(1,n):
    if numbers[index] <= stack[-1]:
        stack.append(numbers[index])
    else:
        while len(stack)!=0 and stack[-1] < numbers[index] and k>=1:
            k-=1
            stack.pop()
        stack.append(numbers[index])

while k>=1:
    stack.pop()
    k-=1
print("".join(stack))