# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）电话号码的字母组合
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/21 12:03
**************************************************
'''
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
dict = {
        '2':['a','b','c'],'3':['d','e','f'],
        '4':['g','h','i'],'5':['j','k','l'],
        '6':['m','n','o'],'7':['p','q','r','s'],
        '8':['t','u','v'],'9':['w','x','y','z']
        }
def fun(s):

    def helper(index,ans,path):
        '''
        :param index: 当前s的下标,初始化为0
        :param ans: 保存的所有值，初始化为[]
        :param path: 走过的路,初始化为[]，
        :return:
        '''
        if index == len(s):
            ans.append("".join(path))
            return

        for i in dict[s[index]]:
            helper(index+1,ans,path+[i])

        return ans
    ans = helper(0,[],[])

    # print(ans)
    return [] if s=='' else ans
s = '29'
print(fun(s))