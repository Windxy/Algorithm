        ##
   ###
  ###
####
import sys
n = int(sys.stdin.readline().strip())
h = int(sys.stdin.readline().strip())
tips = []
for _ in range(h):
    s = list(map(int, input().strip().split(" ")))
    tips.append((s[1],s[0],s[2]))  #e, b ,t
tips.sort()
tree = [0]*n
for t in tips:
    tree_num = sum(tree[t[1]-1:t[0]])
    need_tree = t[2] - tree_num
    for i in range(t[0]-1,t[1]-2,-1):
        if need_tree > 0 and tree[i] == 0:
            tree[i] = 1
            need_tree -= 1
        if need_tree <= 0:
            break
print(int(sum(tree)))
