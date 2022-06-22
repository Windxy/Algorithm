# Q1重复数字的计数
str = input()
ret = 0
hash = set()
for char in str:
    if char in hash:
        ret += 1
    hash.add(char)
print(ret)

# Q2不重复的计数
str = input()
ret = 0
hash = {}
for char in str:
    if char not in hash:
        hash[char] = 1
    else:
        hash[char] += 1
for k,v in hash.items():
    if v == 1:
        ret += 1
print(ret)