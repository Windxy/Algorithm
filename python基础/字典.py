dict = {"b":1,"c":2}
#  如果有a则返回a的值，否则，返回0
a = dict.get("a",0)
tim = "b" in dict
# print(tim,a)

for i in dict.items():
    print(i[0],i[1])

for key in dict:
    print(key,dict[key])
