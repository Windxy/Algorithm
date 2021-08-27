# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （字符串）整数转罗马数字
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/16 9:01
**************************************************
'''
num = 3
tmp = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
tmp_T = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
# for k in tmp:
#     tmp_T[tmp[k]] = k
# print(tmp_T)
ans = ""
for i in tmp_T:
    while num//i:
        ans += tmp_T[i]
        num = num-i
print(ans)