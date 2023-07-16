def isPalindrome(string,n):
    for i in range(len(string)):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

def isSemiPalindrome(string,n):
    start, end = 0, len(string)-1
    while start < end :
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return isPalindrome(string[start+1:end+1],n) or isPalindrome(string[start:end],n)

    return True



n = int(input())
l = [list(input()) for i in range(n)]
answer = []
for i in l:
    if isPalindrome(i,n):
        answer.append(0)
    elif isSemiPalindrome(i,n):
        answer.append(1)
    else:
        answer.append(2)
for i in answer:
    print(i)