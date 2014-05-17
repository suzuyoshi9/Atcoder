N = input()
s = []
dic = {}

for num in range(0,N):
    name = raw_input()
    s.append(name)

for name in s:
    if name not in dic:
        dic[name] = 1
    else:
        dic[name] = dic[name] + 1

result = max((v,k) for (k,v) in dic.items())[1]

print result
