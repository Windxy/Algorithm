'''

'''
'''
给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。
它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。
给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。
示例 1：
输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
示例 2：
输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-xored-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
# from functools import reduce
def decode(encoded: List[int]) -> List[int]:
    ''''''
    '''
    perm: A B C D E
    encoded : a1 a2 a3 a4
    满足：A = (A^B^C^D^E) ^ (B^C^D^E) = (1~n的累计异或)^(a2^a4) = a^b
    异或性质：a ^ b = c  <==>   a ^ c = b  
    '''
    n = len(encoded) + 1
    a = 0       # 第一项
    b = 0       # 第二项
    for i in range(1,n+1):
        a ^= i
    for i in range(1,len(encoded),2):
        b ^= encoded[i]
    first = a^b

    res = [first]
    for i in encoded:
        res.append(res[-1]^i)
    return res

encoded = [6,5,4,6]
print(decode(encoded))