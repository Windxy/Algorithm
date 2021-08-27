# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 单词搜索（回溯）
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/13 20:25
**************************************************
'''
'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def exist(board, word):
    direction = [[0,1],[0,-1],[1,0],[-1,0]]#上下左右
    ans = False
    def helper(i,j,index):#dfs深度优先遍历,(i,j)是从(i,j)开始的起始点，index是位置
        if word[index] != board[i][j]:return False  #不是，回去
        if index == len(word)-1:return True         #最终返回，满足

        visited.add((i,j))  # 访问过了！
        result = False

        for direct in direction:    #需要，开始四周走
            x,y = direct
            if len(board)>x+i>-1 and len(board[0])>y+j>-1:#需要在界内
                if (x+i,y+j) not in visited:    #没有被访问
                    if helper(x+i,y+j,index+1):
                        result = True       # 满足条件
                        break
        #遍历结束，换条路，visited需要删除此路
        visited.remove((i,j))
        return result

    visited = set()
    for i in range(len(board)): # h
        for j in range(len(board[0])):# w
            if helper(i,j,0):return True
    return ans
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(exist(board,'ESEECFDAS'))