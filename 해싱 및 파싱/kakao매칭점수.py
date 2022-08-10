import re
dict={}
domIndex={}
relationship={}
def getscore(page,index,word):
    l=re.findall("<meta.+content=\"(.+?)\"",page)
    dict[index]={"domain":l[0]}
    domIndex[l[0]]=index
    l = re.findall("<a.+?href=\"(.+?)\"", page)
    dict[index]["links"]=tuple(l)
    for i in dict[index]["links"]: #i는 주소임
        if i in relationship:
            relationship[i].append(dict[index]["domain"])
        else:
            relationship[i]=[dict[index]["domain"]]
    l = list(page)
    for i in range(len(l)):
        if l[i].isupper():
            l[i] = l[i].lower()
        if not l[i].isalpha():
            l[i] = " "
    l=''.join(l).split(" ")
    dict[index]["bs"] = 0
    for i in l:
        if i==word:
            dict[index]["bs"]+=1
    return
def getref():
    for i in dict:
        ref=0
        if dict[i]["domain"] in relationship:
            for j in relationship[dict[i]["domain"]]:
                ref+=(dict[domIndex[j]]["bs"]/len(dict[domIndex[j]]["links"]))
        dict[i]["total"]=dict[i]["bs"]+ref
def solution(word, pages):
    word=word.lower()
    for i in range(len(pages)):
        getscore(pages[i],i,word)
    getref()
    answer=[(i,dict[i]["total"]) for i in dict]
    answer.sort(key=lambda x:(-x[1],x[0]))
    return answer[0][0]
word="Muzi"
pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word,pages))
