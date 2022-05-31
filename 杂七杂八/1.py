import heapq
from collections import defaultdict

# dijkstra代码模板
def dijkstra(graph, start, end):
    '''
    garph例子
    G = {
        "B": [["C", 1]],
        "C": [["D", 1]],
        "D": [["F", 1]],
        "E": [["B", 1], ["F", 3]],
        "F": [],
    }
    '''
    # 初始化
    heap = [(0,start)]  # 利用堆来减低复杂度，（A,B）表示从start到B最小要花费A长度
    visited = set()

    while heap:
        cost, u = heapq.heappop(heap) # 每次遍历时，取出花费最小的顶点u，再从u开始出发找到最小的cost的顶点v
        # 每次取出从start到u的顶点，也就意味着该路径就是最短的路径
        # 因此下一次遍历到u顶点，就要pass掉，因为得到了start到u顶点最优的路径长度了
        visited.add(u)

        if u == end:    #如果找到了end，直接返回结果
            return cost

        for v,c in graph[u]:
            if v in visited:
                continue
            now_cost = c + cost
            heapq.heappush(heap,(now_cost,v))   # 利用最小堆，每次将最短路径放到顶端

    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    '''
    G = {
        "B": [["C", 1]],
        "C": [["D", 1]],
        "D": [["F", 1]],
        "E": [["B", 1], ["F", 3]],
        "F": [],
    }
    '''
    graph = defaultdict(list)       # 用defaultdict就不需要自己去定义和判断为空了

    while m:
        P1,P2,w = input().split()
        graph[P1].append([P2,int(w)])
        m-=1
    q = int(input())
    while q:
        start,end = input().split()
        ret = dijkstra(graph,start,end)
        if ret == -1:
            print("INF")
        else:
            print(ret)
        q-=1

