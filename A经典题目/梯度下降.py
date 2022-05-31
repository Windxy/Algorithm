import numpy as np
import random

def gen_line_data(sample_num=100):
    """
    y = 3*x1 + 4*x2
    :return:
    """
    x1 = np.linspace(0, 9, sample_num)
    x2 = np.linspace(1, 10, sample_num)
    x3 = np.linspace(2, 11, sample_num)
    x = np.concatenate(([x1], [x2], [x3]), axis=0).T
    y = np.dot(x, np.array([3, 4, 5]).T)  # y 列向量
    return x, y

# 批量梯度下降
def bgd(samples, y, step_size=0.01, max_iter_count=10000):
    sample_num, dim = samples.shape
    y = y.flatten()
    w = np.ones((dim,), dtype=np.float64)
    loss = 10
    iter_count = 0
    while loss > 0.00001 and iter_count < max_iter_count:
        loss = 0
        error = np.zeros((dim,), dtype=np.float64)
        for i in range(sample_num):
            predict_y = np.dot(w.T, samples[i])
            for j in range(dim):
                error[j] += (y[i] - predict_y) * samples[i][j]

        for j in range(dim):
            w[j] += step_size * error[j] / sample_num   # 批量更新权重 w

        for i in range(sample_num):
            predict_y = np.dot(w.T, samples[i])
            error = (1 / (sample_num * dim)) * np.power((predict_y - y[i]), 2)
            loss += error

        print("iter_count: ", iter_count, "the loss:", loss)
        iter_count += 1
    return w


# 随机梯度下降
def sgd(samples, y, step_size=0.01, max_iter_count=10000):
    sample_num, dim = samples.shape
    y = y.flatten()
    w = np.ones((dim,), dtype=np.float64)
    loss = 10
    iter_count = 0
    while loss > 0.00001 and iter_count < max_iter_count:
        loss = 0
        error = np.zeros((dim,), dtype=np.float64)
        for i in range(sample_num):
            predict_y = np.dot(w.T, samples[i])
            for j in range(dim):
                error[j] += (y[i] - predict_y) * samples[i][j]
                w[j] += step_size * error[j] / sample_num   # 每一个样本更新一次权重 w

        # for j in range(dim):
        #     w[j] += step_size * error[j] / sample_num

        for i in range(sample_num):
            predict_y = np.dot(w.T, samples[i])
            error = (1 / (sample_num * dim)) * np.power((predict_y - y[i]), 2)
            loss += error

        print("iter_count: ", iter_count, "the loss:", loss)
        iter_count += 1
    return w

# 小批量梯度下降
def mbgd(samples, y, step_size=0.01, max_iter_count=10000, batch_size = 0.2):
    sample_num, dim = samples.shape
    y = y.flatten()
    w = np.ones((dim,), dtype=np.float64)
    loss = 10
    iter_count = 0
    while loss > 0.00001 and iter_count < max_iter_count:
        loss = 0
        error = np.zeros((dim,), dtype=np.float64)

        # 随机选取小批量数据
        index = random.sample(range(sample_num), int(np.ceil(sample_num * batch_size)))
        batch_samples = samples[index]
        batch_y = y[index]

        for i in range(len(batch_samples)):
            predict_y = np.dot(w.T, batch_samples[i])
            for j in range(dim):
                # 计算小批量数据的损失函数
                error[j] += (batch_y[i] - predict_y) * batch_samples[i][j]

        # 更新小批量的权重
        for j in range(dim):
            w[j] += step_size * error[j] / len(batch_samples)


        for i in range(sample_num):
            predict_y = np.dot(w.T, samples[i])
            error = (1 / (sample_num * dim)) * np.power((predict_y - y[i]), 2)
            loss += error

        print("iter_count: ", iter_count, "the loss:", loss)
        iter_count += 1
    return w

if __name__ == '__main__':
    samples, y = gen_line_data()
    print(samples[0])
    print(samples[1])
    w = sgd(samples, y)
    print(w)  # 会很接近[3, 4, 5]
