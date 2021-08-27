from functools import lru_cache
from fastcache import clru_cache

@lru_cache(32)
def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_dp(n-1)+climb_stairs_dp(n-2)

def climb_stairs_dp(n: int) -> int:
    fmt = "需要输入正数，然而你输入的是{}"
    assert isinstance(n, int) and n > 0, fmt.format(n)
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = (1, 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def climb_stairs_dp_g(n: int) -> int:
    fmt = "需要输入正数，然而你输入的是{}"
    assert isinstance(n, int) and n > 0, fmt.format(n)
    if n == 1:
        return 1
    if n == 2:
        return 2
    a = 1
    b = 2
    c = 0
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c

if __name__ == "__main__":
    print(climb_stairs_dp(10))
