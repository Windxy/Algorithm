# Factorial of a number using memoization

from functools import lru_cache
from fastcache import clru_cache


@lru_cache(32)
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Number should not be negative.")

    return 1 if num in (0, 1) else num * factorial(num - 1)

def factorial_dp(num):
    if num == 0:
        return 1
    dp = [1] * (num + 1)
    for i in range(1,num+1):
        dp[i] = dp[i-1]*i
    return dp[num]

def factorial_dp_g(num):
    if num == 0:
        return 1
    a = 1
    b = 1
    for i in range(1,num+1):
        b = a*i
        a = b
    return b

if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=False)#verbose=True为测试通过与未通过都将消息显示出来,默认为False，只显示失败信息。

    print(factorial_dp(7))
