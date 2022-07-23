class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # 构建图节点和入度
        # 根据拓扑排序，判断是否只通过一条路径就能走完所有节点
        # 如果不能通过一条路径，说明可重复，答案不唯一
        # 否则为true
        N = len(nums)
        graph = defaultdict(list)  # 序号-->序号
        in_order = [0] * N
        q = deque()

        for edge in sequences:
            for in_n, out_n in pairwise(edge):
                graph[in_n - 1].append(out_n - 1)
                in_order[out_n - 1] += 1

        for idx, num in enumerate(in_order):
            if num == 0:
                q.append(idx)

        if len(q) > 1:
            return False

        while q:
            if len(q) > 1:  # 有多个度为0的，所有有多条路径
                return False
            node = q.popleft()
            for num in graph[node]:
                in_order[num] -= 1
                if in_order[num] == 0:
                    q.append(num)
        return True


