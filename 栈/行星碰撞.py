class Solution:
    def asteroidCollision(self, asteroids) :
        # 栈
        stack = []
        for a in asteroids:
            if stack == [] or stack[-1]*a > 0 or (stack[-1]<0 and a>0):
                stack.append(a)
            if stack[-1]*a < 0:
                while stack != [] and stack[-1]*a < 0 and abs(a) > stack[-1]:
                    stack.pop(-1)

                if stack != []:
                    if a*stack[-1] > 0:
                        stack.append(a)
                    if stack[-1]*a<0 and abs(a)==abs(stack[-1]):
                        stack.pop(-1)
                elif stack == []:
                    stack.append(a)
            # print(stack)
        return stack

if __name__ == '__main__':
    s = Solution()
    s.asteroidCollision([-2,-1,1,2])
