num_list1 = [0]*5                           #创建一维数组
num_list2 = [[0] * 5 for i in range(2)]     #创建二维数组
num_list3 = [[0] * 5] * 2                   #这样子是有问题的，相当于把[0]*5复制了一次，会导致在赋值num_list3[i][j]时，同时赋值了num_list3[k][j],k!=i