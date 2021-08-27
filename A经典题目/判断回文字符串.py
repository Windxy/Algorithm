# 问题一：回文数
# 输入：一个整型数字
# 输出：判断是否为回文数
from functools import reduce

# 递归法得到反转后的字符串
def reversed_str(st:str):
    if st == "":
        return ""
    return reversed_str(st[1:])+st[0]

def isPalindrome(x:int)->bool:
    if x<0:return False
    # # 方法1：转为字符串
    # x = str(x)
    # a = x
    # #判断：方法1:反转方法1.切片 2.栈模拟 3.先转为list然后使用.reverse函数 4.for循环 5.reduce函数 6.递归函数
    # #判断：方法2：双指针法
    # b = reduce(lambda x,y:y+x,a) #lambda匿名函数，冒号前为参数，冒号后为表达式
    # if a==b:
    #     return True
    # return False
    # 方法2：数学解法:
    div = 1
    while(x//div):
        div *= 10   #12212 : 100000
    div //= 10
    while(x>0):
        l = x//div
        r = x%10
        if l!=r:
            return False
        x = (x % div) // 10
        div//=100

    return True
# print(isPalindrome(121))

# 问题二：判断字符串有多少个回文子串(动态规划)
# 输入:一个字符串
# 输出:回文子串的个数
def countSubstrings(s: str) -> int:
    N = len(s)
    dp = [[False] * N for i in range(N)]
    count = 0
    for i in range(N):
        dp[i][i] = True
        count += 1
    # 提示：可以再优化为一维dp
    for j in range(N):
        for i in range(j + 1):
            if i == j:
                continue
            if j == i + 1 and s[i] == s[j]:
                dp[i][j] = True
                count += 1
            elif i+1 < N and dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                count += 1
    return count
# s = "abc"
# print(countSubstrings(s))

# 问题3：分割两个字符串得到回文字符串
def checkPalindromeFormation(a: str, b: str) -> bool:
    # def check(a):
    #     b = a[::-1]
    #     if a == b:
    #         return True
    #     return False
    # # 暴力法
    # N = len(a)
    # for i in range(N + 1):
    #     apre, asu = a[:i], a[i:]
    #     bpre, bsu = b[:i], b[i:]
    #     new_a = apre + bsu
    #     new_b = bpre + asu
    #     if check(new_a):
    #         return True
    #     if check(new_b):
    #         return True
    # return False

    # 中心向外扩展法
    N = len(a)
    left = N//2-1
    def check(a:str,b:str,index:int):
        '''
        :return:返回是否满足回文要求的index
        '''
        pass
    pass

a = "abda"
b = "acmc"
print(checkPalindromeFormation(a,b))