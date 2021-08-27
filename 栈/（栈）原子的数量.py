'''
给定一个化学式formula（作为字符串），返回每种原子的数量。
原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），
然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-atoms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
输入: 
formula = "H2O"
输出: "H2O"
解释: 
原子的数量是 {'H': 2, 'O': 1}。

输入: 
formula = "Mg(OH)2"
输出: "H2MgO2"
解释: 
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。

输入: 
formula = "K4(ON(SO3)2)2"
输出: "K4N2O14S4"
解释: 
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
'''
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        Char_dict = {}  #chr(i):0 for i in range(ord("A"),ord("Z")+1)
        stack = []  # stack.append进栈 stack.pop()出栈
        # 如果遇到大写字母，直接进栈
        # 如果遇到小写字母，直接进栈
        # 如果遇到数字（不会是1和0），出栈，如果第一个是），则
        # 如果遇到（，直接进栈
        # 如果遇到），直接进栈
        N = len(formula)
        i = 0
        while i < N:
            if formula[i].isalpha():
                if formula[i].isupper() and i<N-1 and formula[i+1].islower():
                    stack.append([formula[i:i+2],1])
                    i += 1
                else:
                    stack.append([formula[i],1])

            elif formula[i] == '(':
                stack.append('(')

            elif formula[i] == ')':
                stack.append(')')

            elif formula[i].isdigit():
                nums_temp = int(formula[i])
                while i+1<N and formula[i+1].isdigit():
                    nums_temp = nums_temp * 10 + int(formula[i+1])
                    i += 1
                # 出栈
                if stack[-1][0]==')':
                    stack.pop()
                    stack_temp = []
                    while stack[-1][0]!='(':
                        stack_temp.append([stack[-1][0],stack[-1][1]*nums_temp])
                        stack.pop()
                    stack.pop()
                    while stack_temp:
                        stack.append(stack_temp.pop())
                else:
                    stack[-1][1]*=nums_temp
            i += 1
        # print(stack)
        # # 再次遍历 判断栈中是否还有括号
        # if stack[-1][0] == ')':
        #     stack.pop()
        #     stack_temp = []
        #     while stack[-1][0] != '(':
        #         stack_temp.append([stack[-1][0], stack[-1][1]])
        #         stack.pop()
        #     stack.pop()
        #     while stack_temp:
        #         stack.append(stack_temp.pop())

        for c in stack:
            if len(c)==1:
                continue
            a,b = c
            if a in Char_dict:
                Char_dict[a]+=b
            else:
                Char_dict[a]=b
        # print(Char_dict)
        # def sort_my(x):
        Char_dict_list = [a for a,b in Char_dict.items()]
        Char_dict_list = sorted(Char_dict_list, key=lambda x:(x,len(x)))
        ans = ""
        for i in Char_dict_list:
            if Char_dict[i]==1:
                ans += i
            else:
                ans += i+str(Char_dict[i])
        print(ans)
        return ans

s = Solution()
s.countOfAtoms("Mg(H2O)N")