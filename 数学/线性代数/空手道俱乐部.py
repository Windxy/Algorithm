from networkx import to_numpy_matrix,karate_club_graph
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
zkc = karate_club_graph()
order = sorted(list(zkc.nodes()))
A = to_numpy_matrix(zkc, nodelist=order)
I = np.eye(zkc.number_of_nodes())
A_hat = A + I
D_hat = np.array(np.sum(A_hat, axis=0))[0]
D_hat = np.matrix(np.diag(D_hat))

'''随机初始化参数'''
W_1 = np.random.normal(
    loc=0.5, scale=1, size=(zkc.number_of_nodes(), 4))
W_2 = np.random.normal(
    loc=0.5, size=(W_1.shape[1], 2))

'''堆叠GCN层。我们在这里只使用单位矩阵作为特征表示'''
def gcn_layer(A_hat, D_hat, X, W):
    def func_relu(X: np.matrix):
        X[X < 0] = 0
        return X
    return func_relu(D_hat**-1 * A_hat * X * W)
H_1 = gcn_layer(A_hat, D_hat, I, W_1)
H_2 = gcn_layer(A_hat, D_hat, H_1, W_2)
output = H_2

'''提取特征表示'''
feature_representations = {
    node: np.array(output)[node]
    for node in zkc.nodes()
}


def plot_graph(G, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''

    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None

    if weight_name:
        weights = [int(G[u][v][weight_name]) for u, v in edges]
        labels = nx.get_edge_attributes(G, weight_name)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights);
    else:
        nodelist1 = []
        nodelist2 = []
        for i in range(34):
            if zkc.nodes[i]['club'] == 'Mr. Hi':
                nodelist1.append(i)
            else:
                nodelist2.append(i)
        # nx.draw_networkx(G, pos, edges=edges);
        nx.draw_networkx_nodes(G, pos, nodelist=nodelist1, node_size=300, node_color='r',with_label=True)
        nx.draw_networkx_nodes(G, pos, nodelist=nodelist2, node_size=300, node_color='b',with_label=True)
        nx.draw_networkx_edges(G, pos, edgelist=edges, alpha=0.4, with_label=True)
    plt.show()

plot_graph(zkc)

for i in range (34):
    if zkc.nodes[i]['club'] == 'Mr. Hi':
        plt.scatter(np.array(output)[i,0],np.array(output)[i,1] ,color = 'b',s = 100)
    else:
        plt.scatter(np.array(output)[i,0],np.array(output)[i,1] ,color = 'r',s = 100)
# plt.scatter(np.array(output)[:,0],np.array(output)[:,1])
plt.show()
'''注意，在这个例子中，随机初始化的权值很可能作为ReLU函数的结果在x轴或y轴上给出0值，因此需要多试几次。'''