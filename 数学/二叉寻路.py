class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # step1.找到最大的深度depth
        depth = 1
        max_num = 1
        while True:
            if (max_num << 1) - 1 >= label:
                break
            else:
                max_num = max_num << 1
                depth += 1

        # step2.遍历回去
        ans = []
        while depth!=1:
            ans.append(label)
            # 进入下一层
            if depth & 1 == 0:    # 当层数为偶数时候
                label = (pow(2,depth)+pow(2,depth-1)-1-label)//2
            else:
                label = pow(2,depth)+pow(2,depth-1)-1-label//2
            depth -= 1
        return ans[::-1]
