# 内存拷贝

# 判断有效性
def judge(add,size):
    # 判断add是否达到对应的长度
    if len(add)!=size:
        return False
    else:
        return True

def func(ori_add,dec_add,size):
    # 1.判断地址参数有效性
    # 2.考虑安全拷贝，例如相对地址，例如size的大小
    if not judge(ori_add,size) or not judge(dec_add,size):
        return False
    if len(ori_add)!=dec_add:
        return False

    for i in range(ori_add):
        dec_add[i] = ori_add[i].deep_copy()

    return True
'''
ori:'12345678' : 4
               : 1
               : 6
'''